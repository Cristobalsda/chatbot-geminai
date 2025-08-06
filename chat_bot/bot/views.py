from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from .services.twilio import send_whatsapp_message
from .services.gemini import ask_gemini
from .models import Conversation, Message

@csrf_exempt
def bot(request):
    if request.method == 'POST':
        try:
            user_phone = request.POST['From']
            message_body = request.POST["Body"]

            if not user_phone or not message_body:
                return HttpResponse('Datos incompletos', status = 400)
            
            conversation, _= Conversation.objects.get_or_create(
                phone_number = user_phone
            )
            message, _ = Message.objects.create(
                conversation = conversation,
                body = message_body,
                is_bot = False
            )
            gemini_response = ask_gemini(message_body)

            send_whatsapp_message(
                body=gemini_response,
                to=user_phone
            )
            return HttpResponse('ok')
        except Exception as e:
            print(f"Error en el bot: {e}")
            return HttpResponse('Error interno', status=500)
    return HttpResponse('Método no permitido', status = 405)


            # print(message)
            # response = ask_gemini(message)
            # print(response)

            # if message:
            #     send_whatsapp_message(response, 'whatsapp:+56990503206')
            # return HttpResponse('Hello')