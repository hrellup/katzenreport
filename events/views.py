# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse


from .forms import EventForm

@csrf_exempt
def events_new(request):
    if request.method == "POST":
        form = EventForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse('event upload success')
    else:
        form = EventForm()
    return render(request, 'events/event_form.html', {'form': form})

