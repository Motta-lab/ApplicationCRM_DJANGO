from django.contrib import admin

# Register your models here.
from .models import Produit,Tag

admin.site.register(Produit)
admin.site.register(Tag)