from django.contrib import admin

from apps.users.models import User


class UserAdmin(admin.ModelAdmin):
    search_fields = ("username", "first_name", "last_name")
    list_display = ("id", "username", "first_name", "last_name")
    list_display_links = (
        "id",
        "username",
    )

    fieldsets = (
        ("Personal info", {"fields": ("id", "username", "first_name", "last_name")}),
        ("Contact info", {"fields": ("email",)}),
        ("Permissions", {"fields": ("is_staff", "is_superuser", "groups", "user_permissions")}),
        (
            "Other",
            {
                "fields": (
                    "is_active",
                    "password",
                )
            },
        ),
        ("Important dates", {"fields": ("date_joined", "last_login", "updated_at")}),
    )
    readonly_fields = (
        "id",
        "updated_at",
    )


# Register your models here.
admin.site.register(User, UserAdmin)
