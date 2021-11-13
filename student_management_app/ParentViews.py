from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib import messages
from .models import Parents


def parent_home(request):

    context={

    }
    return render(request, "parent_template/parent_home_template.html", context)