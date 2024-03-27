from django.contrib import admin
from . import models

# Register your models here.

# import our models
# we can use this way


@admin.register(models.Post)
# and we can use this way
# admin.site.register(models.post)
# for customize
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'datetime_modified', )
    ordering = ('datetime_modified', )



# admin.site.register(models.Post, PostAdmin)

