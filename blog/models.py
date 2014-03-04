'''
@author: ks-net
'''
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse
#from django.utils.html import format_html
from django.utils.timezone import now

# Start Model here

class Category(models.Model):
    category = models.CharField(max_length=100, null=True)
    order = models.SmallIntegerField(default=0)    
    description = models.TextField(max_length=250, blank = True)
    status = models.BooleanField("published", default=False)    
    created = models.DateTimeField(auto_now_add = True, default= now())
    
    class Meta:
        ordering = ["-created"]
        verbose_name_plural = "categories"
        

class Post(models.Model):    
    title = models.CharField(max_length=120)
    order = models.SmallIntegerField(default=0)
    intro = models.CharField("Intro Text",max_length=250, blank=True)
    body = models.TextField("Main Text", )
    tags = models.CharField("Tag Entries",max_length=100, blank=True)
    slug = models.SlugField(max_length=100, unique=True, help_text="Do not use spaces or special chars... use only Latin characters, numbers, dashes and underscores")
    status = models.BooleanField("Published", default=False) 
    pub_date = models.DateTimeField(default= now())  
    modified = models.DateTimeField(auto_now = True, default= now())
    created = models.DateTimeField(auto_now_add = True, default= now())
    metadesc = models.TextField("Meta Description",max_length=250, blank=True)
    metakeywords = models.CharField("Keywords",max_length=250, blank=True)
        
    class Meta:
        ordering = ["-created"]
        verbose_name_plural = "posts"    
          
    def get_absolute_url(self):
        return reverse('blog:detail', args=[str(self.slug)])

    
    # TODO fix this
    def next_post(self):
        Post.get_next_by_created()   
        return self    
    def prev_post(self):
        Post.get_previous_by_created()
        return self
        

        
   
        