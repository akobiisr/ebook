from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from .models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import get_object_or_404

# Create your views here.
def home(request):
    template = loader.get_template('ebookweb/index.html')

    context = {

    }
    return HttpResponse(template.render(context, request))

