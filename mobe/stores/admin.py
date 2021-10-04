from django.contrib import admin
from stores.models import Store, Category

class StoreAdmin(admin.ModelAdmin):
    pass

class CategoryAdmin(admin.ModelAdmin):
    pass

admin.site.register(Store, StoreAdmin)
admin.site.register(Category, CategoryAdmin)
