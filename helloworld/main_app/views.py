from django.http import HttpResponse


def homeView(request):
    return HttpResponse('Hello world....')

def anotherView(request):
    return HttpResponse("<h1>Another<h1>")


# Create your views here.
