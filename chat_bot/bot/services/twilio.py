from twilio.rest import Client as TwilioClient
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from .gemini import ask_gemini
from django.conf import settings

account_sid = settings.ACCOUNT_SID
auth_token = settings.AUTH_TOKEN
clientTwilio = TwilioClient(account_sid, auth_token)

def send_whatsapp_message(body, to):
    clientTwilio.messages.create(
        from_='whatsapp:+14155238886',
        body=body,
        to=to
    )