from modules.execute_prompt import *

#How to use Large Language Models for text transformation tasks such as language translation, spelling and grammar checking, tone adjustment, and format conversion.
#Translation
#ChatGPT is trained with sources in many languages. This gives the model the ability to do translation. Here are some examples of how to use this capability.

prompt = f"""
Translate the following English text to Spanish: \ 
```Hi, I would like to order a blender```
"""
response = execute_prompt(prompt)
print(response)

prompt = f"""
Tell me which language this is: 
```Combien coûte le lampadaire?```
"""
response = execute_prompt(prompt)
print(response)

prompt = f"""
Translate the following  text to French and Spanish
and English pirate: \
```I want to order a basketball```
"""
response = execute_prompt(prompt)
print(response)

prompt = f"""
Translate the following text to Spanish in both the \
formal and informal forms: 
'Would you like to order a pillow?'
"""
response = execute_prompt(prompt)
print(response)

#Universal Translator
#Imagine you are in charge of IT at a large multinational e-commerce company. Users are messaging you with IT issues in all their native languages. Your staff is from all over the world and speaks only their native languages. You need a universal translator!

user_messages = [
  "La performance du système est plus lente que d'habitude.",# System performance is slower than normal         
  "Mi monitor tiene píxeles que no se iluminan.",# My monitor has pixels that are not lighting
  "Il mio mouse non funziona",# My mouse is not working
  "Mój klawisz Ctrl jest zepsuty",# My keyboard has a broken control key
  "我的屏幕在闪烁"# My screen is flashing
]

for issue in user_messages:
    prompt = f"Tell me what language this is: ```{issue}```"
    lang = execute_prompt(prompt)
    print(f"Original message ({lang}): {issue}")

    prompt = f"""
    Translate the following  text to English \
    and Korean: ```{issue}```
    """
    response = execute_prompt(prompt)
    print(response, "\n")

#Tone Transformation

prompt = f"""
Translate the following from slang to a business letter: 
'Dude, This is Joe, check out this spec on this standing lamp.'
"""
response = execute_prompt(prompt)
print(response)

#Format Conversion
#ChatGPT can translate between formats. The prompt should describe the input and output formats

data_json = { "resturant employees" :[ 
    {"name":"Shyam", "email":"shyamjaiswal@gmail.com"},
    {"name":"Bob", "email":"bob32@gmail.com"},
    {"name":"Jai", "email":"jai87@gmail.com"}
]}

prompt = f"""
Translate the following python dictionary from JSON to an HTML \
table with column headers and title: {data_json}
"""
response = execute_prompt(prompt)
print(response)

from IPython.display import display, Markdown, Latex, HTML, JSON
display(HTML(response))

#Spellcheck/Grammar check
#Here are some examples of common grammar and spelling problems and the LLM's response.
#To signal to the LLM that you want it to proofread your text, you instruct the model to 'proofread' or 'proofread and correct'.

text = [ 
  "The girl with the black and white puppies have a ball.",  # The girl has a ball.
  "Yolanda has her notebook.", # ok
  "Its going to be a long day. Does the car need it's oil changed?",  # Homonyms
  "Their goes my freedom. There going to bring they're suitcases.",  # Homonyms
  "Your going to need you're notebook.",  # Homonyms
  "That medicine effects my ability to sleep. Have you heard of the butterfly affect?", # Homonyms
  "This phrase is to cherck chatGPT for speling abilitty"  # spelling
]

for t in text:
    prompt = f"""Proofread and correct the following text
    and rewrite the corrected version. If you don't find
    and errors, just say "No errors found". Don't use 
    any punctuation around the text:
    ```{t}```"""
    response = execute_prompt(prompt)
    print(response)

text = f"""
Got this for my daughter for her birthday cuz she keeps taking \
mine from my room.  Yes, adults also like pandas too.  She takes \
it everywhere with her, and it's super soft and cute.  One of the \
ears is a bit lower than the other, and I don't think that was \
designed to be asymmetrical. It's a bit small for what I paid for it \
though. I think there might be other options that are bigger for \
the same price.  It arrived a day earlier than expected, so I got \
to play with it myself before I gave it to my daughter.
"""
prompt = f"proofread and correct this review: ```{text}```"
response = execute_prompt(prompt)
print(response)

from redlines import Redlines

diff = Redlines(text,response)
display(Markdown(diff.output_markdown))

prompt = f"""
proofread and correct this review. Make it more compelling. 
Ensure it follows APA style guide and targets an advanced reader. 
Output in markdown format.
Text: ```{text}```
"""
response = execute_prompt(prompt)
display(Markdown(response))