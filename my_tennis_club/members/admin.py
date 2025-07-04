from django.contrib import admin
from .models import Members

class MemberAdmin(admin.ModelAdmin):
    list_display = ("firstname", "lastname", "joined_date","phone","salary",)

# Create your models here.
admin.site.register(Members, MemberAdmin)
# Register your models here.
