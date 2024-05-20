#
# import google.generativeai as genai
# import os
#
# genai.configure(api_key='AIzaSyAnS7GaNb01fS1rcrCcr21zgNt30BY3DXM')
#
# model = genai.GenerativeModel()
# response = model.generate_content('Please summarise this document: ...')
#
# print(response.text)


import google.generativeai as genai
import os

genai.configure(api_key='AIzaSyAnS7GaNb01fS1rcrCcr21zgNt30BY3DXM')

model = genai.GenerativeModel()

chat = model.start_chat()
response = chat.send_message("Hello")
print(response.text)
print(chat.history)