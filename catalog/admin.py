from catalog.models import Author, Book, BookInstance, Genre, Language
from django.contrib import admin

# Register your models here.
admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Genre)
admin.site.register(BookInstance)
admin.site.register(Language)