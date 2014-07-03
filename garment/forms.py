# -*- coding: utf-8 -*-
"""
Created on Wed Apr 30 15:05:26 2014

@author: jingsz
"""

from django import forms
    
class BasicInfoForm(forms.Form):
    ShopOwner = forms.ChoiceField(label = u"店主ID", required=True)
    GarmentItem = forms.CharField(label = u"衣服种类编号", max_length=100, required=True)
    GarmentSubitem = forms.CharField(label = u"衣服编号", max_length=100, required=True)
    color = forms.CharField(label = u"颜色", max_length=10, required=True)
    size = forms.CharField(label = u"大小", max_length=10, required=True)
    chest = forms.FloatField(label = u"胸围", max_value=1000, min_value=0, required=False)
    height = forms.FloatField(label = u"身高", max_value=1000, min_value=0, required=False)
    waist = forms.FloatField(label = u"腰围", max_value=1000, min_value=0, required=False)
    hip = forms.FloatField(label = u"臀围", max_value=1000, min_value=0, required=False)
    shoulder = forms.FloatField(label = u"肩宽", max_value=1000, min_value=0, required=False)
    material = forms.ChoiceField(label = u"衣服材质", required=False)
    cloth_type = forms.ChoiceField(label = u"衣服类型", required=False)
    delta = forms.CharField(label = u"delta", widget=forms.Textarea, required=False)
    description = forms.CharField(label = u"描述", widget=forms.Textarea, required=False)