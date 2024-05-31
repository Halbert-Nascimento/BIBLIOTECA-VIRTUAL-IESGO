from django import forms
from .models import Book


class RegistroForm(forms.ModelForm):
  class Meta:
    model = Book
    fields = ['title', 'author', 'published_date', 'book_cover']

# class LivroForm(forms.Form):
#   title = forms.CharField(max_length=100)
#   author = forms.CharField(max_length=100)
#   published_date = forms.DateField(widget=forms.DateInput(format='%d/%m/%Y'))
#   book_cover = forms.ImageField()