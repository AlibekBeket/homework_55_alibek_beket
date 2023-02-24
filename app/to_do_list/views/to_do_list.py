from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

from to_do_list.forms import ToDoForm
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


def add_view(request):
    if not request.POST:
        form = ToDoForm()
        context = {
            'form': form
        }
        return render(request, 'add_page.html', context=context)
    form = ToDoForm(data=request.POST)
    if not form.is_valid():
        context = {
            'form': form
        }
        return render(request, 'add_page.html', context=context)
    else:
        to_do = ToDo.objects.create(**form.cleaned_data)
        return redirect('/to_do/' + str(to_do.pk))


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
    to_do_dict = {
        'title': to_do.title,
        'description': to_do.description,
        'status': to_do.status,
        'date': to_do.date
    }
    form = ToDoForm(data=to_do_dict)
    if not request.POST:
        return render(request, 'to_do_update.html', context={
            'form': form,
            'to_do': to_do
        })
    if not form.is_valid():
        context = {
            'form': form,
            'to_do': to_do
        }
        return render(request, 'add_page.html', context=context)
    to_do.title = request.POST.get('title')
    to_do.description = request.POST.get('description')
    to_do.status = request.POST.get('status')
    if request.POST.get('date') == '':
        date = None
    else:
        date = request.POST.get('date')
    to_do.date = date
    to_do.save()
    return redirect('to_do_detail', pk=to_do.pk)


def delete_view(request, pk):
    to_do = get_object_or_404(ToDo, pk=pk)
    to_do_status = ToDo().choices
    for status in to_do_status:
        if status[0] == to_do.status:
            to_do.status = status[1]
    if to_do.date == None:
        to_do.date = ''
    return render(request, 'to_do_confirm_delete.html', context={'to_do': to_do})


def confirm_delete(request, pk):
    to_do = get_object_or_404(ToDo, pk=pk)
    to_do.delete()
    return redirect('to_do_list')
