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
    category = models.ForeignKey(Category, )

    def __str__(self) -> str:
        return self.title
