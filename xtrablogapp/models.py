from django.db import models

# Create your models here. i.e database tables
# dbTable1
class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name

# dbTable2
class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name

# dbTable3
class Comment(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=200, verbose_name='Email Address')
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name

# dbTable4
class Post(models.Model):
    title = models.CharField(max_length=250, verbose_name='blog_title')
    description = models.TextField()
    article = models.TextField()
    published_date = models.DateField(auto_now_add=True)
    author = models.CharField(max_length=100)
    thumbnail = models.ImageField(upload_to='thumbnail', default='example.png')
    # ForeignKey is used to create a many to one relationship
    category = models.ForeignKey(Category, related_name='articles', on_delete=models.CASCADE, default=1) 
    # when you delete an object in a category then the other objects connected to it are also deleted
    # category = models.ForeignKey(Category, on_delete=models.PROTECT) # when you attempt to delete an object in a category with other objects connected to it, it prevents the delete action! 
    # category = models.ForeignKey(Category, on_delete=models.DO_NOTHING) # when you delete an object in a category then nothing is done to the other objects connected to it 
    # category = models.ForeignKey(Category, on_delete=models.SET_NULL) # when you delete an object in a category then the other objects connected to it are set to null PS: you must set null=True  
    tags = models.ManyToManyField(Tag)
    
    def __str__(self) -> str:
        return self.title
    
    def __str__(self) -> str:
        return self.article

# steps
# python manage.py makemigrations
# python manage.py migrate
# open admin panel and select the related fields in tags
# add a new category e.g Tech
# add a new post with lorem text


# cmd in vscode 
# python manage.py shell 
# to get all posts that belong to a particular category 
# from main_app.models import Post, Category, Tag
# Making query across relationships
# post = Post.objects.filter(category__name='business') NB: name is the field in the category 
# post
# single_post = Post.objects.gey(id=1)
# single_post.category
# output:
# cat = Category.objects.get(id=1)
# cat.articles.all()
# output:
# to count the number of blog post that belongs to this category 
# cat.articles.count()
# output:
# cat.articles.filter(author='john') NB: this filter operation is carried out on the post table 
# output:
# cat.articles.create(title:'test postt', description='testing', article=testing article', author='inie') NB: this adds a new blog post directly to this category 
# output: 
# cat.articles.all()
# output:
# get_post=Post.objects.get(id=4)
# cat.articles.add 


















