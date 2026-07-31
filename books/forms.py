from django import forms
from .models import Book


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = [
            'title',
            'isbn',
            'author',
            'category',
            'price',
            'stock',
            'description',
            'cover_image',
            'published_date',
            'availability_status',
        ]

        widgets = {
            'published_date': forms.DateInput(attrs={'type': 'date'}),
            'description': forms.Textarea(attrs={'rows': 4}),
        }