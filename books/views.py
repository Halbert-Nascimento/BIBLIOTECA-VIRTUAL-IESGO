from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .models import Book
from .forms import RegistroForm
# Create your views here.

def index(request):
  template = loader.get_template('book_list.html')
  context = {
    'title': 'Home pag'
  }

  return HttpResponse(template.render(context, request))

def list_books(request):
  template = loader.get_template('book_list.html')

  books = Book.objects.all()

  context = {
    'books': books,
    'title': 'Lista de livros',
  }
  

  return HttpResponse(template.render(context, request))

def book_register(request):
  if request.method == 'POST':
    form = RegistroForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('list_books')
    
  else:
    form = RegistroForm()

    


  template = loader.get_template('book_register.html')
  context={
    'title': 'Cadastro de livros',
    'form':form,
  }

  return HttpResponse(template.render(context, request))