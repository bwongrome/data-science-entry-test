prompt_a = """
I am a marketing manager at a retail company and we have just finished 
a three-month campaign. My team has collected customer feedback through 
an online survey and we now have about 500 responses stored in a 
spreadsheet. Each response includes the customer's age group, the 
product they purchased, their satisfaction rating from 1 to 5, and a 
short written comment. I need to present the findings to our CEO next 
Friday in a way that is easy to understand. Can you analyse this data 
for me, highlight which age groups and products have the lowest 
satisfaction scores, identify the most common complaints from the 
written comments, and summarise everything in a short paragraph I can 
use as an executive summary?
"""

prompt_b = """
Role: You are a data analyst helping a retail marketing team.
Task: Analyse customer survey data from a 3-month campaign.
Data: 500 responses containing age group, product purchased, 
satisfaction rating (1-5), and written comments.
Steps:
1. Identify age groups and products with the lowest satisfaction scores.
2. Extract the most common themes from the written comments.
3. Summarise findings in an executive summary paragraph.
Audience: CEO presentation on Friday.
Constraints: Keep the summary concise and free of technical jargon.
"""


# Task 1
# Read both prompts above carefully, then answer the questions below as comments.

# Q8a: Which prompt do you think will get a better response from an AI?
# Your answer:
prompt_b will get a better response from AI. 


# Q8b: Give TWO reasons to support your choice.
# Your answer (Reason 1):
# Your answer (Reason 2):
Reason 1 - Prompt_b provides a role to the agent i.e telling the AI agent as data analyst. It gives what a perspective to use.
It can shape what the agent pays attention and be more specific on the task required by specifying the operation mode.  

Reason 2 - Prompt_b provides planning steps to the AI agent to avoid the cost of wrong assumption. It turns the complext tasks
into a plan which can be evaluated and most AI agent includes planning mode which produces a structured task breakdown that 
explains what it intends to do and in what order.


# Q8c: What is ONE strength of the prompt you did NOT choose?
# Your answer:
Provide keywords and using chain-of-densityn(CoD) is one of the strength which I did not choose. AI agents are prediction systems and depends on keywords as part of prompt quality. CoD increases with density of information especially with keywords and this is suitable to keep summary concise. 

# Task 2
# Rewrite either prompt by borrowing ONE element from the other
# to make it stronger. Explain what you borrowed and why.
# Your answer:
prompt_a_rewrite = """
I am a data analyst at a retail company.
Analyse customer data from a 3-month campaign.
My team has collected customer feedback through an online survey and we now have about 500 responses stored in a 
spreadsheet. Each response includes the customer's age group, the 
product they purchased, their satisfaction rating from 1 to 5, and a 
short written comment. I need to present the findings to our CEO next 
Friday in a way that is easy to understand. 
Steps:
1. Identify age groups and products with the lowest satisfaction scores.
2. Identify the most common complaints from the written comments.
3. Summarise findings in a short paragraph as an executive summary
"""
In prompt_b, it tells AI agent what is the role to use. So, this is rewritten in prompt_a. Providing steps-by-steps in prompt_a will help the AI agent to go into planning mode and avoid hallucination.

