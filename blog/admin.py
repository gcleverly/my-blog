from django.contrib import admin
from .models import Post, Image


class PostAdmin(admin.ModelAdmin):
	model = Post
	filter_horizontal =('images',)

admin.site.register(Image)		
admin.site.register(Post, PostAdmin)