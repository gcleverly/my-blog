from django.contrib import admin
from .models import Project, Image

class ProjectAdmin(admin.ModelAdmin):
	model = Project
	filter_horizontal =('images',)

admin.site.register(Image)		
admin.site.register(Project, ProjectAdmin)
# Register your models here.
