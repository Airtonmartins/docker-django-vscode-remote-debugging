from django.http import HttpResponse

def home(request):
    msg = "hello world"
    print("msg")
    return HttpResponse(msg)