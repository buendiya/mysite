 # -*- coding: utf-8 -*- 
import logging
from models import *
from django.contrib import admin
from django.contrib.auth.models import User


class GarmentSubitemInlineAdmin(admin.TabularInline):
    model = GarmentSubitem
    extra = 1
    class Media:
<<<<<<< HEAD
        js = ("jquery-1.11.1.js", "jquery-ui.js", "garment.js", )

=======
        js = ("garment.js",)
>>>>>>> 72db141e217743239d1f442ec542016ecd7160aa

class GarmentItemMatchDetailInlineAdmin(admin.TabularInline):
    model = GarmentItemMatchDetail
    extra = 1
    def get_formset(self, request, obj=None, **kwargs):
        self.exclude = []
        if not request.user.is_superuser:
            self.can_delete = False
        return super(GarmentItemMatchDetailInlineAdmin, self).get_formset(request, obj, **kwargs)

class GarmentItemAdmin(admin.ModelAdmin):
    inlines = [GarmentSubitemInlineAdmin, GarmentItemMatchDetailInlineAdmin, ]
    list_display = ('item_id', )
    search_fields = ('item_id', )

    
admin.site.register(GarmentItem, GarmentItemAdmin)
