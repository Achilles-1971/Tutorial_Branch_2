from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic

from .models import Book, Author, Bookinstance, Genre


class BookListView(generic.ListView):
    model = Book
    template_name = "catalog/book_list.html"
    context_object_name = "Book_list"  # Optional:  Customizes the context variable name.  Defaults to 'object_list'


def index(request):
    # Генерация "количеств" некоторых главных объектов
    num_books = Book.objects.all().count()
    num_instances = Bookinstance.objects.all().count()
    # Доступные книги (статус = 'На складе')
    # Здесь метод 'all()' применен по умолчанию.
    num_instances_available = Bookinstance.objects.filter(status__exact=2).count()
    # Авторы книг,
    num_authors = Author.objects.count()
    # Отрисовка HTML-шаблона index.html с данными
    # внутри переменной context
    return render(
        request,
        "index.html",
        context={
            "num_books": num_books,
            "num_instances": num_instances,
            "num_instances_available": num_instances_available,
            "num_authors": num_authors,
        },
    )
