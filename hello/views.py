from django.shortcuts import HttpResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def webhook(request):

    if request.method == 'POST':
        data = request.body
        print('Entro un nuevo mensaje!')
        print(data)
        return HttpResponse.status_code(200)
        
    if request.method == 'GET':
        data = request.GET
        data_dict = data.dict()
        token = data_dict['hub.verify_token']
        mode = data_dict['hub.mode']
        challenge = data_dict['hub.challenge']
        if token and mode:
            if mode == 'subscribe' and token == 'betun':
                return HttpResponse(challenge)

    return HttpResponse('No hay data')
    
