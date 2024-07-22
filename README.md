# Topic AI <img src="logo-whitebg.png" align="right" width="20%" height="20%" />
Topic Generator is a Python package that generates topics from open-ended text data using the Azure OpenAI Chat Completions API. It processes a CSV file containing text data, generates topics for text data, and saves the updated data to a new CSV file.

## Features 
- Generates topics from text data using OpenAI GPT-4o
- Allows users to specify system messages and examples
- More flexible than traditional topic modeling software

# Showcase
Below is an example of topics generated from fabricated employee survey comments: 

```python
prompt = "You receive open-ended comments from an employee survey at a government agency. 
    Your job is to identify topics from the comments. 
    Limit your response to a few words or comma separated phrases."
```

**Output:**

| ID | Comments                                                                                    | Topics                                                                                     |
|----|---------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------|
| 1  | The agency provides good benefits but there is little room for career growth.               | Opportunities for Advancement, Employee Benefits                                           |
| 2  | I feel proud to serve the community through my work at this agency.                         | Employee pride, community service                                                          |
| 3  | The workload is overwhelming at times due to understaffing in our department.               | Workload, understaffing                                                                    |
| 4  | My supervisor is supportive and encourages me to develop new skills.                        | Supportive supervisor, skill development encouragement                                     |


## Installation
Using `pip`:
```python
pip install git+https://github.in.dc.gov/OCTO/topic-ai.git
```

Alternatively, you can:
1. Clone the repostory
2. Navigate to the project directory
3. Install the package and dependencies using `pip install .`

## Configuration
Before using the Topic Generator, you need to set the following environment variables:

- `AZURE_OPENAI_API_KEY`: Your OpenAI API key.
- `AZURE_OPENAI_ENDPOINT`: The Azure endpoint for OpenAI.

You can set these environment variables using the following commands in your terminal or command prompt:
```cmd
set OPENAI_API_KEY=your_api_key
set OPENAI_AZURE_ENDPOINT=your_azure_endpoint
```
Replace `your_api_key` and `your_azure_endpoint` with your actual API key and Azure endpoint, respectively.
Make sure to also specify your `api_version` and `model` in the initial setup. 

## Usage
Here's an example of how to use the AI Topic Generator package:
```python
from topic_ai import TopicAI

# Create an instance of TopicAI
topic_ai = TopicAI(api_key=os.getenv('OPENAI_API_KEY'), 
                   api_version='2024-02-15-preview', 
                   azure_endpoint=os.getenv('OPENAI_AZURE_ENDPOINT'),
                   model='gpt-4o')

# Process a CSV file
result = topic_ai.process_csv(
    input_file='input.csv',
    text_column='Comments',
    system_message='Your system message'
)
```
The process_csv method takes the following parameters:

`input_file`: The path to the input CSV file containing the survey data.  
`text_column`: The name of the column containing the open-ended responses.  
`system_message`: The system message to guide the topic extraction process.  
`pre_specified_topics` (optional): A string containing pre-specified topics to use as a starting point for topic extraction.  
`output_file` (optional): The path to the output CSV file to save the results. If not provided, the method will return a DataFrame with the results.  
`output_column` (options, default 'Result'): The name of the column where the topics are written.

## Example
An example script is provided in the [`examples/`](examples/) directory.

## Contributing
Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.
