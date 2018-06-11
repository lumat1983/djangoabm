from django.http import HttpResponse

def hola(request):
    return HttpResponse("Hola Mundo!")  