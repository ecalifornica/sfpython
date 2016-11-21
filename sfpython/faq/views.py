from django.shortcuts import render
from django.shortcuts import render, get_object_or_404

from .models import Faq

def list(request):
  return render(request, "faq/index.html", {'objects': Faq.visible.all().order_by('order')})
  
def detail(request, slug):
  print slug
  object = get_object_or_404(Faq, url=slug)
  return render(request, "faq/detail.html", {'object': object})
  

