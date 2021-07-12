from django.contrib import admin

from .models import Category_product, Name


admin.site.register(Category_product)

admin.site.register(Name)

admin.site.site_header = 'Purbeurre Administration'

admin.site.site_title = 'Purbeurre'
