from django.shortcuts import render
from blog.models import Post, Categoria

# Create your views here.

def blog(request):
    posts = Post.objects.all() # para que importe todos los posts

    return render(request, 'blog/blog.html', {'posts': posts}) 



# para que cuando apretamos las categorias aparezcan

def categoria(request, categoria_id):
    categoria = Categoria.objects.get(id=categoria_id)

    posts = Post.objects.filter(categorias=categoria)

    return render(request, 'blog/categoria.html', {'categoria': categoria, 'posts': posts})
