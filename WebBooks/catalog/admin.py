from django.contrib import admin
from .models import Author, Book, Genre, Language, Status, Bookinstance

# admin.site.register(Author)
# admin.site.register(Book)
admin.site.register(Genre)
admin.site.register(Language)
admin.site.register(Status)
# admin.site.register(Bookinstance)

admin.register(Book)
admin.register(Bookinstance)


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    pass


@admin.register(Bookinstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ("book", "status", "borrower", "due_back", "id")
    list_filter = ("status", "due_back")
    fieldsets = (
        (None, {"fields": ("book", "imprint", "inv_nom")}),
        ("Availability", {"fields": ("status", "due_back", "borrower")}),
    )

    def get_queryset(self):
        return Bookinstance.objects.filter(
            borrower=self.request.user, status__exact="2"
        ).order_by("due_back")


class AuthorAdmin(admin.ModelAdmin):
    list_display = ("last_name", "first_name", "date_of_birth", "date_of_death")


admin.site.register(Author, AuthorAdmin)
