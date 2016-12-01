from django.contrib import admin
from mezzanine.core.admin import TabularDynamicInlineAdmin
from mezzanine.pages.admin import PageAdmin
from .models import HomePage, Slide, Portfolio

# Register your models here.
class SlideInline(TabularDynamicInlineAdmin):
    model = Slide

#class IconInline(TabularDynamicInlineAdmin):
#    model = IconBlurb

class HomePageAdmin(PageAdmin):
    model = HomePage
    inlines = [
        SlideInline,
    ]

admin.site.register(HomePage, HomePageAdmin)
admin.site.register(Portfolio, PageAdmin)
