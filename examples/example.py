import os
from topic_ai import TopicAI

# Create an instance of TopicAI
topic_ai = TopicAI(api_key=os.getenv('OPENAI_API_KEY'), 
                   api_version=os.getenv('AZURE_API_VERSION'), 
                   azure_endpoint=os.getenv('OPENAI_AZURE_ENDPOINT'),
                   model = 'gpt-4o')

# Process a CSV file
topic_ai.process_csv(
    input_file='./examples/example-input.csv', 
    text_column='Comments', 
    output_file='./examples/example-output.csv',
    output_column='Topics',
    system_message=
    '''
    You receive open-ended comments from an employee survey at a government agency. 
    Your job is to identify topics from the comments. 
    Limit your response to a few words or phrases. Use commas to separate the topics. Do not use bullet points or numbed lists. Do not end sentences with periods and do not include quotation marks. 
    If there is not enough information from the comments or the comments are simply "No" or "None", respond with "No topics identified".
    ''',
    pre_specified_topics=
    '''
    Use the following list of topics as a starting point: 
    Workplace environment and culture: Physical and social aspects of the workplace, including office layout, colleague interactions, and organizational culture.
    Telework and work schedules: Flexibility and structure of work schedules, including telework policies and their impact on work-life balance.
    Communication and transparency: Clarity and openness of communication within the organization, particularly from upper management.
    Career advancement and opportunities: Processes and fairness of hiring, promotion, and career progression within the organization.
    Training and professional development: Availability and quality of training and development opportunities for employees.
    Compensation and benefits: Issues related to employee compensation, including salary disparities, cost-of-living adjustments, and benefits adequacy.
    Mission and vision: Alignment of the organization's actions and decisions with its stated mission and vision.
    IT and administrative processes: Efficiency and effectiveness of the organization's IT and administrative processes.
    ''')