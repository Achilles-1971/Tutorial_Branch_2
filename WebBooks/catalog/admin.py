from django.contrib import admin
from.models import Author, Book, Genre, Language, Status, Bookinstance

#admin.site.register(Author)
#admin.site.register(Book) 
admin.site.register(Genre) 
admin.site.register(Language) 
admin.site.register(Status) 
#admin.site.register(Bookinstance)

admin.register(Book)
admin.register(Bookinstance)


@admin.register(Book) 
class BookAdmin(admin.ModelAdmin):
    pass
@admin.register(Bookinstance)
class BookinstanceAdmin(admin.ModelAdmin): 
    pass

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
admin.site.register(Author, AuthorAdmin)