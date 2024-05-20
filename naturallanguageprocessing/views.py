from django.shortcuts import render

# Create your views here.
def index(request):
    print("hello")
    return render(request, 'naturallanguageprocessing/home.html')


import google.generativeai as genai
import os

genai.configure(api_key='AIzaSyAnS7GaNb01fS1rcrCcr21zgNt30BY3DXM')

model = genai.GenerativeModel()

chat = model.start_chat()


from django.views.decorators.csrf import csrf_protect
@csrf_protect
def chat_view(request):
  # Initialize conversation object
  # conv = conversation.Conversation(api_key=API_KEY)

  if request.method == 'POST':
    user_message = request.POST.get('message')
    if user_message:
      # Send user message to Gemini and get response
      response = chat.send_message(user_message)
      chat_history = [(user_message, "You"), (response.text, "Gemini")]
  else:
    chat_history = []

  return render(request, 'naturallanguageprocessing/chat.html', {'chat_history': chat_history})
