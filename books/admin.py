from django.contrib import admin
from .models import Category, Author, Book


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email')
    search_fields = ('name', 'email')


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
        'author',
        'category',
        'price',
        'stock',
        'availability_status',
        'published_date',
    )

    search_fields = (
        'title',
        'isbn',
        'author__name',
        'category__name',
    )

    list_filter = (
        'category',
        'availability_status',
        'published_date',
    )