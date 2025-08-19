from django.shortcuts import render

def lista_blog(request):
    return render(request, 'blog/blog.html') 
