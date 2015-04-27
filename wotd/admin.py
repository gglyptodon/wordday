from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models import Word

class WordAdmin(admin.ModelAdmin):
    list_display = (
        'title','language','description','dateShown'
    )

admin.site.register(Word, WordAdmin)
# Register your models here.
