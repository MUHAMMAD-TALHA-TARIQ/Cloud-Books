from django.shortcuts import render, redirect, HttpResponse
from rest_framework.mixins import CreateModelMixin
from rest_framework.generics import GenericAPIView
from django.http import JsonResponse
from django.db.models import Q
from .b_serializer import *
from .models import *


# Home Page
def home(request):
    response = Books_Section.objects.filter(Q(parent_id="") | Q(parent_id="-"))
    return render(request, 'books/index.html', {'response': response})


# sub Categorisation
def sub_sections(request, section):
    response = Books_Section.objects.filter(parent_id=section)
    return render(request, 'books/index.html', {'response': response, 'parent_id': section})


# Create sections
def create_section(request):
    if request.method == 'POST':
        section_parent_id = request.POST.get("p_id")
        section_heading = request.POST.get('s_head')
        section_para = request.POST.get('s_para')
        if section_parent_id == "" or section_parent_id == "-":
            Books_Section.objects.create(parent_id="-", heading=section_heading, paragraph=section_para)
            return redirect(f'/books')
        else:
            Books_Section.objects.create(parent_id=section_parent_id, heading=section_heading, paragraph=section_para)
            return redirect(f'/books/sub/{section_parent_id}')
    else:
        return HttpResponse("Bad Request !")


# Update the sections
def update_section(request):
    if request.method == 'POST':
        section_parent_id = request.POST.get("p_id")
        section_self_id = request.POST.get('s_id')
        section_heading = request.POST.get('s_head')
        section_para = request.POST.get('s_para')
        Books_Section.objects.update_or_create(self_id=section_self_id,
                                               defaults={"heading": section_heading, "paragraph": section_para})
        if section_parent_id == "":
            return redirect(f'/books')
        else:
            return redirect(f'/books/sub/{section_parent_id}')
    else:
        return HttpResponse("Bad Request !")


# Rest Framework Creation
class create_section_module(GenericAPIView, CreateModelMixin):
    queryset = Books_Section.objects.all()
    serializer_class = Books_Section_Serializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


# json tree Response
def json_tree(request):
    response = section_distribution()
    return JsonResponse(response, safe=False)


# function for json tree creation
def section_distribution(*args):
    dataset = list()
    if args:
        data_objs = Books_Section.objects.filter(parent_id=args[0])
        for obj in data_objs:
            if Books_Section.objects.filter(parent_id=obj.self_id).exists():
                stack = section_distribution(obj.self_id)
                dataset.append({'heading': obj.heading, 'paragraph': obj.paragraph, 'sub_sections': stack})
            else:
                dataset.append({'heading': obj.heading, 'paragraph': obj.paragraph})
        return dataset
    else:
        data_objs = Books_Section.objects.filter(parent_id="-")
        for obj in data_objs:
            stack = section_distribution(obj.self_id)
            dataset.append({'heading': obj.heading, 'paragraph': obj.paragraph, 'sub_sections': stack})
    return dataset
