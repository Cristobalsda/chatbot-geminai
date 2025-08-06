from google import genai
from django.conf import settings

client = genai.Client(api_key=settings.GOOGLE_API_KEY)

def ask_gemini(message):
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=message
    )
    return response.text if hasattr(response, 'text') else str(response)