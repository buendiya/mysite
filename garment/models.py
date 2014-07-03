 # -*- coding: utf-8 -*- 
from django.db import models

class GarmentItem(models.Model):
    id = models.IntegerField(primary_key=True)
    item_id = models.CharField(max_length=100) # input content when shop owner publish garment item
    update_time = models.DateTimeField(auto_now_add=True, auto_now=True)
    create_time = models.DateTimeField(auto_now_add=True)
    def __unicode__(self):
        return "%s"%(self.id)

    
class GarmentItemMatchDetail(models.Model):
    garment_item = models.OneToOneField(GarmentItem, primary_key=True, related_name='match_detail')
    update_time = models.DateTimeField(auto_now=True, auto_now_add=True)
    create_time = models.DateTimeField(auto_now_add=True)


class GarmentSubitem(models.Model):
    id = models.AutoField(primary_key=True, blank=True)
    garment_item = models.ForeignKey(GarmentItem, related_name='subitems')
    subitem_id = models.CharField(max_length=100) # input content when shop owner publish garment item
    color = models.CharField(max_length=10)
    size = models.CharField(max_length=10)
    detail_info = models.CharField(max_length=500, null=True)
    update_time = models.DateTimeField(auto_now_add=True, auto_now=True)
    create_time = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return "%s-%s-%s"%(self.garment_item, self.color, self.size)

