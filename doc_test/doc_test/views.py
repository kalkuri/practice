from django.http import HttpResponse

def home(request):
    return HttpResponse('response to check docker deployement...........')