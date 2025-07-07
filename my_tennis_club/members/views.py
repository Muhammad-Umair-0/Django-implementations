from django.http import HttpResponse
from django.template import loader
from .models import Members

def main(request):
  template = loader.get_template('main.html')
  return HttpResponse(template.render())

def members(request):
  mymembers = Members.objects.all().values()
  template = loader.get_template('all_members.html')
  context = {
    'mymembers': mymembers,
  }
  return HttpResponse(template.render(context, request))
  
def details(request, id):
  mymember = Members.objects.get(id=id)
  template = loader.get_template('details.html')
  context = {
    'mymember': mymember,

  }
  return HttpResponse(template.render(context, request))
  

def testing(request):
  mymember = Members.objects.all().values()
  template = loader.get_template('template.html')
  context = {
    'mymember': mymember,
    # 'firstname': "Umair",

    'fruits': ['Apple', 'Banana', 'Cherry']
  }
  return HttpResponse(template.render(context, request))

def partner(request):

  template = loader.get_template('myfirst.html')
  context = {
    'partner': ['Rao','Umair']
  }
  return HttpResponse(template.render(context, request))


def test(request):
  data = Members.objects.all()
  # data = Members.objects.all().values,# to get all values
  # data = Members.objects.values_list('firstname'),# to get specific column
  # data = Members.objects.filter(fitstname='Rao').values(), #for specific Row
  template = loader.get_template('test.html')
  context = {
    'mymembers' :data
  }
  return HttpResponse(template.render(context,request))