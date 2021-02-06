from django.contrib import admin

from attribute.models import MainCategory, SubCategory, TertiaryCategory, UnderTertiaryCategory, Brand, Colour, Size, MadeIn, SameDayDelivary, NextDayDelivary

# Register your models here.

admin.site.register(MainCategory)
admin.site.register(SubCategory)
admin.site.register(TertiaryCategory)
admin.site.register(UnderTertiaryCategory)
admin.site.register(Brand)
admin.site.register(Colour)
admin.site.register(Size)
admin.site.register(MadeIn)
admin.site.register(SameDayDelivary)
admin.site.register(NextDayDelivary)
