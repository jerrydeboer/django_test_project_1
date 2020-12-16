from django.shortcuts import render, HttpResponse, redirect
from django.forms import modelform_factory
from .models import EdosTemplate

EdosTemplateForm = modelform_factory(EdosTemplate, exclude=[])

def new_template(request):
    if request.method == "POST":
        # form submitted
        form = EdosTemplateForm(request.POST)
        if form.is_valid():
            form.save()
            # ToDo return redirect("home")
    else:
        form = EdosTemplateForm()
    return render(request, "edos/new-template.html", {"form": form})
