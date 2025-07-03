from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# def members(request):
#     return HttpResponse("Hello! welcome to MEri_Tech")
# # This view function returns a simple HTTP response with the text "Hello! welcome to MEri_Tech".
def members(request):
    template  = loader.get_template('myfirst.html')
    return HttpResponse(template.render())
