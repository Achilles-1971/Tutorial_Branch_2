from django.contrib import admin
from.models import Author, Book, Genre, Language, Status, Bookinstance, AuthorAdmin, BookAdrnin, BookinstanceAdmin
#admin.site.register(Author)
admin.site.register(Author,AuthorAdmin)
#admin.site.register(Book) 
admin.site.register(Genre) 
admin.site.register(Language) 
admin.site.register(Status) 
#admin.site.register(Bookinstance)
admin.register(Book)
admin.register(Bookinstance)