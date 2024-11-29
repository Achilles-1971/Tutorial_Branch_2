from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic

from .models import Book, Author, Bookinstance, Genre


class BookListView(generic.ListView):
 model = Book
class BookDetailView(generic.DetailView):
 model = Book
   
def index(request):
    num_books = Book.objects.all().count()
    num_instances = Bookinstance.objects.all().count()
    num_instances_available = Bookinstance.objects.filter(status__exact=2).count()
    num_authors = Author.objects.count()
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
