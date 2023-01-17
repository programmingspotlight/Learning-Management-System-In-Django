from django.contrib import admin
from .models import CustomUser
from .forms import SignupForm

# Register your models here.
@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    model = CustomUser
    # Form For Creating Users From The Admin Panel.
    add_form = SignupForm

    """ Fieldsets are used to control the layout of the user admin panel.
        They consist of a list of one or more tuple,
        Each tuple has a title for each fieldset (section) and a dictionary that contains the list fields
    """
    fieldsets = [
        (
            'Main Information', {
                'fields': ['username', 'email', 'first_name', 'last_name', 'phone_number', 'password']
        }),
        (
            'Groups & Permissions', {
                'fields': ['groups', 'user_permissions']
        }),
        (
            'Extra Information', {
                'fields': ['is_staff', 'is_active', 'is_superuser', 'date_joined', 'last_login', 'avatar', 'bio',]
        }),
        (
            'User Role', {
                'fields': ['is_instructor', 'is_student']
        }),
    ]



