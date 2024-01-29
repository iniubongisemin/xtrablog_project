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
    message = models.Textfield()
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
    category = models.ForeignKey(Category, related_name='articles, on_delete=models.CASCADE, default=1) 
    # when you delete an object in a category then the other objects connected to it are also deleted
    # category = models.ForeignKey(Category, on_delete=models.PROTECT) # when you attempt to delete an object in a category with other objects connected to it, it prevents the delete action! 
    # category = models.ForeignKey(Category, on_delete=models.DO_NOTHING) # when you delete an object in a category then nothing is done to the other objects connected to it 
    # category = models.ForeignKey(Category, on_delete=models.SET_NULL) # when you delete an object in a category then the other objects connected to it are set to null PS: you must set null=True  
    tags = models.ManyToManyField(Tag)
    
    def __str__(self) -> str:
        return self.title

# steps
# python manage.py makemigrations
# python manage.py migrate
# open admin panel and 
