from django.contrib import admin
from .models import Token

class TokenAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'get_user_email', 'get_user_phone', 'key', 'state',
        'refresh_key', 'created_at', 'expires_at', 'revoked'
    )
    search_fields = ('user__email_address', 'user__phone_number')
    ordering = ('user__email_address',)

    def get_user_email(self, obj):
        return obj.user.email_address
    get_user_email.short_description = "User Email"

    def get_user_phone(self, obj):
        return obj.user.phone_number
    get_user_phone.short_description = "User Phone"

