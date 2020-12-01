from django.contrib import admin
from .models import Rep
# Register your models here.

class RepAdmin(admin.ModelAdmin):
    list_display = ('name','email','phone','is_mvp')
    list_display_links = ('name',)
    # list_filter = ('price',)
    list_editable = ('is_mvp',)
    search_fields = ('name','email','phone')
    list_per_page = 20


admin.site.register(Rep , RepAdmin)