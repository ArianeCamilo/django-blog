from django.http import HttpResponse

# criando a função
def hello_world(request):
    return HttpResponse("Hello world")