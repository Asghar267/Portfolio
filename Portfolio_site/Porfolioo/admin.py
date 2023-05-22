from django.contrib import admin

from .models import Contact


# Register your models here.
class ContactsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'subject', 'message')


admin.site.register(Contact, ContactsAdmin)
