from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone
from django.utils.text import slugify

User = get_user_model()

class Categories(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

def get_first_category():
    return Categories.objects.first()

def get_first_user():
    return User.objects.first()

class Post(models.Model):
    
    class PostObjects(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(status='published')
    
    OPTIONS = (
        ('draft', 'draft',),
        ('published', 'published',),
    )
    
    category = models.ForeignKey(Categories, on_delete = models.PROTECT, default=get_first_category, related_name='category_posts')
    title = models.CharField(max_length=250)
    excerpt = models.TextField()
    content = models.TextField()
    slug = models.SlugField(max_length=250, unique_for_date='published', blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_posts',default=get_first_user)
    image = models.ImageField(upload_to='images/', blank=False , null=False)
    published = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=10, choices=OPTIONS, default='published')
    objects = models.Manager() #default manager
    postobjects = PostObjects() #custom manager
    
    class Meta:
        ordering = ('-published',)
    
    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
