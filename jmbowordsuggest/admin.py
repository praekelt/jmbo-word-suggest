from django.contrib import admin
from jmbowordsuggest.models import AcceptedWord, AcceptedWordCategory

class AcceptedWordAdmin(admin.ModelAdmin):
    search_fields = ('word',)
    
admin.site.register(AcceptedWord, AcceptedWordAdmin)
admin.site.register(AcceptedWordCategory)
