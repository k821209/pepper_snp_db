from django.shortcuts import render
from .models import snpdb

def index(request):
     snpdb    = snpdb.objects.order_by('?')[0:2] 
     return render(request, 'snpdb/index.html', {'snpdb' : snpdb})


