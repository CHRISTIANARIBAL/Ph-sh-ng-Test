from django.contrib import admin
from .models import UserCredential

@admin.register(UserCredential)
class UserCredentialAdmin(admin.ModelAdmin):
    list_display = ('username', 'password')  # Show password directly in list view
