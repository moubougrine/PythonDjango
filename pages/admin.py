from django.contrib import admin
from .models import LoGing
from .forms import Test

class Tryadmin(admin.ModelAdmin):
    form = Test

admin.site.register(LoGing)
admin.site.site_header='ABDELMOUGHIT'
admin.site.site_title='ABDELMOUGHIT'
