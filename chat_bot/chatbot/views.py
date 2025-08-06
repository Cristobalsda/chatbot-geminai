from django.shortcuts import render
from django.http import JsonResponse
from google import genai

GOOGLE_API_KEY = 'AIzaSyDAcQg29X4OAn2TxFsy1Ch4FvpzyUegsDE'
client = genai.Client(api_key=GOOGLE_API_KEY)

def ask_gemini(message):
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=message
    )
    return response.text

def chatbot(request):
    if request.method == "POST":
        message = request.POST.get('message')
        response = ask_gemini(message)
        return JsonResponse({'message': message, 'response': response})
    return render(request, 'chatbot.html')