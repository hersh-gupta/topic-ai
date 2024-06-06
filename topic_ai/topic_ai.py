import os
import pandas as pd
from openai import AzureOpenAI, APIError, AuthenticationError

class TopicAI:
    def __init__(self, api_key, api_version, azure_endpoint, model='gpt-4o'):
        try:
            self.client = AzureOpenAI(
                api_key=api_key,
                api_version=api_version,
                azure_endpoint=azure_endpoint
            )
            self.model = model
        except AuthenticationError as e:
            print(f"Authentication Error: {str(e)}")
            exit(1)

    def process_csv(self, input_file, text_column, system_message, pre_specified_topics=None, output_file=None, output_column='Result'):
        # Load CSV
        df = pd.read_csv(input_file)

        # Apply function to non-null comments and write to new file
        df[output_column] = df.apply(lambda row: self._get_response(row[text_column], system_message, pre_specified_topics) if pd.notnull(row[text_column]) else None, axis=1)
        
        if output_file:
            df.to_csv(output_file, index=False, encoding="utf-8")
        
        return df

    def _get_response(self, comment, system_message, pre_specified_topics=None):
        """
        Takes a comment and returns a response from the Azure OpenAI API Chat Completions endpoint.

        Args:
            comment (str): The comment to be processed.
            system_message (str): The system message to guide the response.
            pre_specified_topics (str, optional): Pre-specified topics to use as a starting point.

        Returns:
            str: The response from the OpenAI API, or an error message if the API call fails.
        """
        messages = [
            {"role": "system", "content": system_message},
        ]
        
        if pre_specified_topics:
            messages.append({"role": "system", "content": pre_specified_topics})
        
        messages.append({"role": "user", "content": comment})
        
        try:
            response = self.client.chat.completions.create(
                model=self.model,
                temperature=0.1,
                messages=messages
            )
            return response.choices[0].message.content
        except (APIError) as e:
            print(f"OpenAI API Error: {str(e)}")
            return "Error: Unable to process comment"