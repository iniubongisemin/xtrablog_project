from django.shortcuts import render
from .models import Post
from .models import Category

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
    categories = Category.objects.all()
    similar_post = Post.objects.filter(category = post.category).exclude(id=post.id)
    context={
        'article' : post,
        'categories' : categories,
        'similar_articles' : similar_post
    }
    return render(request, 'main/post.html', context)

  
