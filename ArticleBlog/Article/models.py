from django.db import models
class Author(models.Model):                    # 作者
    name = models.CharField(max_length=32)
    age = models.IntegerField()
    gender = models.CharField(max_length=32)
    birthday = models.DateField()
    email = models.EmailField()
    adress = models.TextField()
    photo = models.ImageField(upload_to='images')
    def __str__(self):
        return self.name
class ArticleType(models.Model):                  #类型
    label = models.CharField(max_length=32)
    description = models.TextField()
    def __str__(self):
        return self.label
class Article(models.Model):                       #文章
    title = models.CharField(max_length=32)
    article_author = models.ForeignKey(to=Author,on_delete=models.CASCADE)  #作者删除，文章删除
    description = models.TextField()
    content = models.TextField()
    article_type = models.ManyToManyField(to=ArticleType)
    public_time = models.DateField(auto_now=True)
    picture = models.ImageField(upload_to='images')

# Create your models here.
