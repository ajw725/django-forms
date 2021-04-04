from django.shortcuts import render
from . import forms

# Create your views here.


def index(request):
    return render(request, 'forms_app/index.html')


def form_name_view(request):
    form = forms.FormName

    if request.method == 'POST':
        form = forms.FormName(request.POST)
        if form.is_valid():
            print(f'name: {form.cleaned_data["name"]}')
        else:
            print('FORM DATA INVALID')

        form = forms.FormName

    ctx = {'form': form}
    return render(request, 'forms_app/form.html', context=ctx)
