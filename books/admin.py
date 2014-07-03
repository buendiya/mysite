# Register your models here.
from django.contrib import admin
from models import Publisher, Author, Book


class BookInline(admin.TabularInline):
    model = Book
    extra = 1

class PublisherAdmin(admin.ModelAdmin):
    inlines = [BookInline, ]

class AuthorAdmin(admin.ModelAdmin):
    pass
    
class BookAdmin(admin.ModelAdmin):
    date_hierarchy = 'publication_date'
    def save_model(self, request, obj, form, change):
        super(BookAdmin, self).save_model(request, obj, form, change)


admin.site.register(Publisher, PublisherAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)