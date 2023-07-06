import yaml
import openai

#Reading values from yaml file
with open('D:\Workspace\Chat GPT\ChatGPT Prompt Engineering for Developers\Setting Up\config\open_ai_config.yaml') as f:
    value = yaml.safe_load(f)

#Storing config values in variables
api_key=value['api_key']
model=value['model']
max_tokens=value['max_tokens']
temperature=value['temperature']

#Setting up api key
openai.api_key = api_key

#Function to make api call
def get_completion(prompt, model=model):
    messages = [{"role": "user", "content": prompt}]

    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        max_tokens=max_tokens,
        temperature=temperature, # this is the degree of randomness of the model's output
    )
    #return response
    return response.choices[0]["message"]["content"]

text = f"""
The French Revolution was a period of radical political and societal change in France that began with the Estates General of 1789 and ended with the formation of the French Consulate in November 1799. Many of its ideas are considered fundamental principles of liberal democracy while the values and institutions it created remain central to French political discourse.
Its causes are generally agreed to be a combination of social, political and economic factors, which the Ancien Régime proved unable to manage. In May 1789, widespread social distress led to the convocation of the Estates General, which was converted into a National Assembly in June. Continuing unrest culminated in the Storming of the Bastille on 14 July, which led to a series of radical measures by the Assembly, including the abolition of feudalism, the imposition of state control over the Catholic Church in France, and extension of the right to vote.
The next three years were dominated by the struggle for political control, exacerbated by economic depression and civil disorder. Austria, Britain, Prussia and other external powers sought to restore the Ancien Régime by force, while many French politicians saw war as the best way to unite the nation and preserve the revolution by exporting it to other countries. These factors resulted in the outbreak of the French Revolutionary Wars in April 1792, abolition of the French monarchy and proclamation of the French First Republic in September 1792, followed by the execution of Louis XVI in January 1793.
The Paris-based Insurrection of 31 May - 2 June 1793 replaced the Girondins who dominated the National Assembly with the Committee of Public Safety, headed by Maximilien Robespierre. Attempts to eliminate his opponents sparked the Reign of Terror, with an estimated 16,000 killed by the time it ended in July 1794. As well as external enemies, the Republic faced internal opposition from both Royalists and Jacobins and in order to deal with these threats, the French Directory took power in November 1795. Despite a series of military victories, many won by Napoleon Bonaparte, political divisions and economic stagnation resulted in the Directory being replaced by the Consulate in November 1799. This is generally seen as marking the end of the Revolutionary period.
"""
prompt = f"""
Summarize the text delimited by triple backticks into a single sentence.
```{text}```
"""
response = get_completion(prompt)
print(response)