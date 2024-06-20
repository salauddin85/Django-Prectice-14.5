from django.shortcuts import render
from .forms import Formapi
from .forms import ModelForm
# Create your views here.
def home(request):
    if request.method =='POST':
        form = Formapi(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
    else:
        form = Formapi()
    return render(request,'home.html',{'form':form})


def model(request):
    if request.method == 'POST':
        model_form = ModelForm(request.POST)
        if model_form.is_valid():
            print(model_form.cleaned_data)
    else:
        model_form = ModelForm()
    return render(request,'model.html',{'form':model_form})