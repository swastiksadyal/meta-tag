import http
from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse
from.forms import input_form
from .getInfo import getinfo

def info_request(request):
    outputs = {}
    if request.method == 'POST':
        form = input_form(request.POST)
        if form.is_valid():
            name = form.cleaned_data['website']
            outputs["name"] = name
            outputs["result"] = getinfo(name)
            print(outputs['result'])

    
    form = input_form()
    outputs["form"] = form
    return render(request, 'form.html', outputs)