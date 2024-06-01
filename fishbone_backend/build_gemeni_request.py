
import json
from fishbone_backend.gemeni_functions import gemeni_functions

def all_keys_none(d):
    '''
    returns True if all values in a dictionary are None
    '''
    return all(value is None for value in d.values())

def build_messages(problem: str, causes: dict | None = None):
    '''
    Takes a string problem, and any cause categories and causes and returns a list of messages formatted for gemeni api messages body and tools object
    '''
    if causes is None:
        tools = [gemeni_functions['add_categories']]
    else:
        tools = [gemeni_functions['update_causes']]

    if causes is None:
        messageHistory = [
            {
                "role": "user",
                "parts": [f"You are a tool used for creating fishbone diagrams, also known as Ishikawa diagram. Given the following problem statement: {problem} get the possible causes categories to put into a Ishikawa diagram. For example for an engineering problem you would return the categories: materials, methods, machines, man, maintenance, measurement, and environment."]
            }
        ]
    elif all_keys_none(causes) is True:
        causes_categories_array = causes.keys()
        cause_categories_str = ' '.join(causes_categories_array)
        messageHistory = [
            {
                "role": "user",
                "parts": [f"You are a tool used for creating fishbone diagrams, also known as Ishikawa diagram. You are given a problem and the identified cause categories and some causes. Using this information fill out the first layer of possible causes for each category. For example if the problem is too much chatter in production of a part and one of the cause categories is machine then a possible cause in that category might be worn out tooling. Go ahead and begin. The problem is: {problem} The following cause categories {cause_categories_str} have been identified."]
            }
        ]
    else: 
        causes_str = json.dumps
        messageHistory = [
            {
                "role": "user",
                "parts": [f"You are a tool used for creating fishbone diagrams, also known as Ishikawa diagram. You are given a problem and the identified cause categories and some causes, using this information go one layer deeper in listing causes if possible. For example, if the problem is too much chatter in production of a part and listed under the cause category of machine is worn out tooling, then the next layer might be high variation in tooling life or lack of tooling assesment measures. Go ahead and begin. The problem is: {problem} The following causes and cause categories have been identified: {causes_str}"]
            }
        ]
    return messageHistory, tools
