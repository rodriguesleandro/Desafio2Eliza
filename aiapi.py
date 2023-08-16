import openai
import config
import json

api_key = config.DevelopmentConfig.OPENAI_KEY

openai.api_key = api_key

def generateChatResponse(prompt):
    
    messages = json.loads(prompt)

    response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages= messages["messages"])

    try:
        answer = response['choices'][0]['message']['content'].replace('\n', '<br>')
    except:
        answer = 'OOPS Not Skynet. This is free app with limitations. So try again later. Please.'

    return answer


