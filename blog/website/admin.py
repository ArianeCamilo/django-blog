from django.contrib import admin
from .models import Post, Contact

class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'sub_title', 'full_name', 'categories', 'deleted']
    search_fields = ['title', 'sub_title'] # cria campo dde busca para título e subtítulo
    
    # def get_queryset(self, request):
    #     return Post.objects.filter(deleted=False)

# Register your models here.
admin.site.register(Post, PostAdmin)
admin.site.register(Contact)