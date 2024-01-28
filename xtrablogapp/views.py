from django.shortcuts import render
from .models import Post

# Create your views here.

# home page view
def home_page_view(request):
    all_article = Post.objects.all()
    context = {
        'articles':all_article
    }
    return render(request, 'main/index.html', context)

# about page
def about_page_view(request):

    return render(request, 'main/about.html')

# contact page
def contact_page_view(request):

    return render(request, 'main/contact.html')

# post page
def post_page_view(request):

    return render(request, 'main/post.html')

# single blog post page
def single_blog_post(request, blog_id):
    post = Post.objects.get(id=blog_id)
    context={
        'article' : post
    }
    return render(request, 'main/post.html', context)

  
