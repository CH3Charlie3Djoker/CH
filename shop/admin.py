
# admin.py
from django.contrib import admin
from .models import Product, Review

# MyModel имеется ввиду любая ваша модель...

@admin.register(Product)
class ProductlAdmin(admin.ModelAdmin):
    list_display = ("name",  "rating",  "price", "discount", "stock",) # указываем названия полей как в модели
    list_editable = ("price", "stock",)

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ("autor", "product", "like", "dislike", ) # указываем названия полей как в модели
    
