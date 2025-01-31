from django import forms

class FoundationCalcForm(forms.Form):
    length = forms.FloatField(label='Длина фундамента (м)', min_value=0)
    width = forms.FloatField(label='Ширина фундамента (м)', min_value=0)
    height = forms.FloatField(label='Высота фундамента (м)', min_value=0)

class FloorAreaCalcForm(forms.Form):
    length = forms.FloatField(label='Длина пола (м)', min_value=0)
    width = forms.FloatField(label='Ширина пола (м)', min_value=0)
