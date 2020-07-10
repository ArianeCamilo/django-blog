from django.shortcuts import render
from .models import Post, Contact

# Create your views here.
def hello_blog(request):
    lista = ['django', 'python','git', 'html', 'Nginx']
    #list_posts = Post.objects.all()
    list_posts = Post.objects.filter(deleted=False)

    data = {'name': 'Curso de Django 3', 
            'lista_tecnologias': lista,
            'posts': list_posts}
    
    return render(request, 'index.html', data)

def post_detail(request, id):
        post = Post.objects.get(id=id)
        return render(request, 'post_detail.html', {'post': post})

def save_form(request):
        name = request.POST['name']
        Contact.objects.create( # cria o contato no BD
                name = name,
                email=request.POST['email'],
                message=request.POST['message']
        )
        return render(request, 'contact_success.html', {'name_contact': name})    