from django.contrib import admin

#from django.db import models
from django import forms
from django.utils.html import strip_tags
from django.utils.translation import ugettext_lazy as _
from blog.models import Category, Post

# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('id', 'created',)
    fieldsets = [
        (None,  {'fields': ['id']}),                 
        (None,  {'fields': ['category']}),
        (None,  {'fields': ['description']}),
        (None,  {'fields': ['order']}),        
        (None,  {'fields': ['created']}),        
    ]
    list_display = ('id', 'category', 'description', 'order', 'status', 'created',)
    date_hierarchy = 'created'
    save_on_top = True
    save_as = True
    search_fields = ('category',)
    list_editable = ('order',)
    list_filter = ('created', 'status',)
    ordering = ('-created',)
    list_display_links = ('id', 'category',)
    actions = ['make_published' , 'make_unpublished']   

    def make_published(self, request, queryset):
        rows_updated = queryset.update(status=True)
        if rows_updated == 1:
            message_bit = "1 category was"
        else:
            message_bit = "%s categories were" % rows_updated
        self.message_user(request, "%s successfully marked as published." % message_bit)
    make_published.short_description = "Mark selected categories as published"
                
    def make_unpublished(self, request, queryset):
        rows_updated = queryset.update(status=False)
        if rows_updated == 1:
            message_bit = "1 category was"
        else:
            message_bit = "%s categories were" % rows_updated
        self.message_user(request, "%s successfully marked as Unpublished." % message_bit)    
    make_unpublished.short_description = "Mark selected categories as Unpublished"
     
    class CategoryForm(forms.ModelForm):
        class Meta:
            model = Category
            
        def clean_description(self):
            data = strip_tags(self.cleaned_data["description"])
            return data
                        
    form = CategoryForm
        
        

class PostAdmin(admin.ModelAdmin):
    readonly_fields = ('id', 'modified', 'created',)
    fieldsets = [
        (None,  {'fields': ['id','title']}),
        (None,  {'fields': ['slug']}),        
        (None,  {'fields': ['intro']}),
        (None,  {'fields': ['body']}),
        (None,  {'fields': ['tags']}),
        (None,  {'fields': ['metadesc']}),
        (None,  {'fields': ['metakeywords']}),
        ('Publish Info & Options',  {'fields': (('status','order','modified','created'),'pub_date')}),                      
    ]

    date_hierarchy = 'created'
    save_on_top = True
    save_as = True
    list_display = ('id', 'title', 'order', 'slug', 'status', 'pub_date', 'modified', 'created',)
    search_fields = ('title','slug',)
    list_editable = ('order',)
    list_filter = ('pub_date', 'status',)
    ordering = ('-created',)
    list_display_links = ('id', 'title',)
    actions = ['make_published' , 'make_unpublished']
    

    def make_published(self, request, queryset):
        rows_updated = queryset.update(status=True)
        if rows_updated == 1:
            message_bit = "1 story was"
        else:
            message_bit = "%s stories were" % rows_updated
        self.message_user(request, "%s successfully marked as published." % message_bit)
    make_published.short_description = "Mark selected stories as published"
                
    def make_unpublished(self, request, queryset):
        rows_updated = queryset.update(status=False)
        if rows_updated == 1:
            message_bit = "1 story was"
        else:
            message_bit = "%s stories were" % rows_updated
        self.message_user(request, "%s successfully marked as Unpublished." % message_bit)    
    make_unpublished.short_description = "Mark selected stories as Unpublished"    
    
    
#   formfield_overrides = { models.TextField: {'widget': forms.Textarea(attrs={'class':'ckeditor','rows':15, 'cols':20})}, 
#                            models.CharField: {'widget': forms.TextInput(attrs={'size':'80'})},                               
#                           }     
    class PostForm(forms.ModelForm):
        class Meta:
            model= Post
                         
            widgets = {
                'id' : forms.TextInput(attrs={'size':10}),                       
                'title' : forms.TextInput(attrs={'class':'special','size':80}),
                'order' : forms.TextInput(attrs={'size':5}),
                'intro' : forms.Textarea(attrs={'class':'intro','rows':3, 'cols':80}),
                'body'  : forms.Textarea(attrs={'class':'ckeditor','rows':15, 'cols':80}),
                'tags'  : forms.TextInput(attrs={'size':80}),
                'slug'  : forms.TextInput(attrs={'size':50}),
                'metadesc' : forms.Textarea(attrs={'class':'intro','rows':3, 'cols':80}),
                'metakeywords' : forms.TextInput(attrs={'size':80}),
                }
                        
        def clean_intro(self):
            intro = strip_tags(self.cleaned_data["intro"])
            return intro
                           
        class Media:
            js = ('assets/js/ckeditor/ckeditor.js',)

    form = PostForm


        
admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)





