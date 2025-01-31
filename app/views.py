from django.shortcuts import render
from .forms import FoundationCalcForm, FloorAreaCalcForm

def home(request):
    return render(request, 'home.html')

def foundation_calc(request):
    result = None
    if request.method == 'POST':
        form = FoundationCalcForm(request.POST)
        if form.is_valid():
            length = form.cleaned_data['length']
            width = form.cleaned_data['width']
            height = form.cleaned_data['height']
            result = length * width * height  # Расчет объема
    else:
        form = FoundationCalcForm()
    return render(request, 'foundation_calc.html', {'form': form, 'result': result})

def floor_area_calc(request):
    result = None
    if request.method == 'POST':
        form = FloorAreaCalcForm(request.POST)
        if form.is_valid():
            length = form.cleaned_data['length']
            width = form.cleaned_data['width']
            result = length * width  # Расчет площади
    else:
        form = FloorAreaCalcForm()
    return render(request, 'floor_area_calc.html', {'form': form, 'result': result})
