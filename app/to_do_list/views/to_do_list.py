from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from to_do_list.models import ToDo


def home_view(request: WSGIRequest):
    to_do_list = ToDo.objects.all()
    to_do_status = ToDo().choices
    for to_do in to_do_list:
        for status in to_do_status:
            if status[0] == to_do.status:
                to_do.status = status[1]
    context = {
        'to_do_list': to_do_list
    }
    return render(request, 'home_page.html', context=context)


def add_view(request: WSGIRequest):
    if not request.POST:
        return render(request, 'add_page.html')
    if request.POST.get('date') == "":
        date = None
    else:
        date = request.POST.get('date')
    to_do_add = {
        'description': request.POST.get('description'),
        'status': request.POST.get('status'),
        'date': date,
        'title': request.POST.get('title')
    }
    ToDo.objects.create(**to_do_add)
    return redirect(reverse('to_do_list'))


def detail_view(request, pk):
    to_do = get_object_or_404(ToDo, pk=pk)
    to_do_status = ToDo().choices
    for status in to_do_status:
        if status[0] == to_do.status:
            to_do.status = status[1]
    if to_do.date == None:
        to_do.date = ''
    return render(request, 'to_do_page.html', context={
        'to_do': to_do,
        'to_do_status': to_do_status
    })

def update_view(request, pk):
    to_do = get_object_or_404(ToDo, pk=pk)
    if not request.POST:
        to_do_status = ToDo().choices
        return render(request, 'to_do_update.html', context={
            'to_do': to_do,
            'to_do_status': to_do_status
        })
    to_do.title = request.POST.get('title')
    to_do.description = request.POST.get('description')
    to_do.status = request.POST.get('status')
    to_do.save()
    return redirect('to_do_detail', pk=to_do.pk)

