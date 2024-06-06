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
    You receive open-ended comments from an employee survey at the District Department of Transportation(DDOT). 
    Your job is to help the user parse them and identify topics from the comments. 
    Limit your response to a few words or comma separated phrases.
    ''',
    pre_specified_topics=
    '''
    Use the following list of topics as a starting point: 
    Work schedule and telework: Desire for more flexible work schedules and additional telework days due to physical and mental exhaustion from commuting.
    Workplace environment and culture: Need for better communication, respect, and courtesy among staff and management, and addressing inappropriate comments and behavior.
    Opportunities for advancement: Concerns about the slow and seemingly unfair process for career advancement within the agency.
    Management and leadership: Issues with management and leadership, including lack of proper goal setting, accountability, and vision.
    Training and development: Need for better training and development opportunities, including comprehensive systems, SOPs, and training on various processes.
    HR processes: Concerns about slow and non-transparent HR processes, leading to loss of recruits and dissatisfaction among current employees.
    Communication and collaboration: Need for better communication and collaboration within and between departments, and more trust and autonomy in areas of expertise.
    ''')