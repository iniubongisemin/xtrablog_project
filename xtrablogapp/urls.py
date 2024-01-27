from django.urls import path
from .views import home_page_view, about_page_view, contact_page_view, post_page_view, single_blog_post

urlpatterns = [
    path('', home_page_view, name = 'home'),
    path('about/', about_page_view, name = 'about'),
    path('contact/', contact_page_view, name = 'contact'),
    path('post/', post_page_view, name = 'post'),
    path('blog/<int:blog_id>/', single_blog_post, name = 'blog') 
] 