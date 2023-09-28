import openai
import ChatGPTCred

model="gpt-3.5-turbo"
#model="text-davinci-002"

completion = openai.ChatCompletion.create(
  model= model,
  messages=[
    {"role": "user", "content": "Tell the world about the ChatGPT API in the style of a pirate."}
  ]
)

print(completion.choices[0].message.content)

