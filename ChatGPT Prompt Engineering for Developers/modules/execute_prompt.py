import yaml
import openai

#Reading values from yaml file
with open('D:\Knowledge Hub\Workspace\ChatGPT\config\open_ai_config.yaml') as f:
    value = yaml.safe_load(f)

#Storing config values in variables
api_key=value['api_key']
model=value['model']
max_tokens=value['max_tokens']
temperature=value['temperature']

#Setting up api key
openai.api_key = api_key

#Function to make api call
def execute_prompt(prompt, model=model):
    messages = [{"role": "user", "content": prompt}]

    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        max_tokens=max_tokens,
        temperature=temperature, # this is the degree of randomness of the model's output
    )
    #return response
    return response.choices[0]["message"]["content"]