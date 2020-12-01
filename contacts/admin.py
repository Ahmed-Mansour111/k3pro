from django.contrib import admin
from .models import Contact
# Register your models here.
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name','listing','email','phone','contact_date')
    list_display_links = ('name',)
    search_fields = ('name','mail','phone','contact_date','listing')
    list_per_page = 20

admin.site.register(Contact , ContactAdmin)