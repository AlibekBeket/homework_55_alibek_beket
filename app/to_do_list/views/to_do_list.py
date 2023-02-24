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
    errors = {}
    if not request.POST:
        to_do_status = ToDo().choices
        context = {
            'to_do_status': to_do_status
        }
        return render(request, 'add_page.html', context=context)
    if len(request.POST.get('title')) <= 1 or ' ' == request.POST.get('title')[0]:
        errors['title_error'] = 'Вы ничего не ввели в поле заголовка или ввели 1 символ или ввели один пробел и больше в начало загаловка'
    elif len(request.POST.get('title')) > 200:
        errors['title_error'] = 'Вы ввели больше 200 символов'
    if len(request.POST.get('description')) > 1000 or len(request.POST.get('description')) > 0 and ' ' == request.POST.get('description')[0]:
        errors['description_error'] = 'Вы ввели больше 1000 символов в поле описания или ввели один пробел и больше в начало загаловка'
    to_do_add = ToDo()
    to_do_add.title = request.POST.get('title')
    to_do_add.description = request.POST.get('description')
    to_do_add.status = request.POST.get('status')
    if request.POST.get('date') == "":
        to_do_add.date = None
    else:
        to_do_add.date = request.POST.get('date')
    if errors:
        to_do_status = ToDo().choices
        context = {
            'to_do': to_do_add,
            'errors': errors,
            'to_do_status': to_do_status
        }
        return render(request, 'add_page.html', context=context)
    to_do_add_create = {
        'title': to_do_add.title,
        'description': to_do_add.description,
        'status': to_do_add.status,
        'date': to_do_add.date
    }
    to_do = ToDo.objects.create(**to_do_add_create)
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