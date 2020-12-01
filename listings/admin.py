from django.contrib import admin
from .models import Listing, Category , HomeImage
# Register your models here.

class ListingAdmin(admin.ModelAdmin):
    list_display = ('id','product','model','is_published','price','rep')
    list_display_links = ('model','product')
    # list_filter = ('price',)
    list_editable = ('is_published',)
    search_fields = ('product','model','price','category')
    list_per_page = 20



admin.site.register(Listing,ListingAdmin)
admin.site.register(Category)
admin.site.register(HomeImage)