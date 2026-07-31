from django.shortcuts import render, redirect
from .forms import SubscriberForm

def subscribe(request):
    if request.method == "POST":
        form = SubscriberForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    return redirect('/')