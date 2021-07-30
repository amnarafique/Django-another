from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render, redirect

from .forms import TaskForm
from .models import Task

def register():
	pass


def task_create(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
            # cd = form.cleaned_data
            # title = cd.get('title')
            # description = cd.get('description')
            # dead_line = cd.get('dead_line')

            # Task.objects.create(
            #     title=title,
            #     description=description,
            #     dead_line=dead_line
            # )

            # task = Task(
            #     title=title,
            #     description=description,
            #     dead_line=dead_line
            # )



    form = TaskForm()
    return render(request, 'tasks/create_task.html',
                  context={'form': form})


def main(request):
    tasks = Task.not_completed.all()
    paginator = Paginator(tasks, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'tasks/index.html',
                  context={'page_obj': page_obj})


def update_task(request, pk):
    task = Task.objects.filter(id=pk).first()
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('/')
    form = TaskForm(instance=task)
    return render(request, 'tasks/task_detail.html',
                  context={'form': form})


def delete_task(request, pk):
    task = Task.objects.filter(id=pk).first()
    task.delete()
    return redirect('/')


def search(request):
    query = request.GET.get('q')
    tasks = Task.objects.filter(done=False).filter(
       Q(title__icontains=query) | Q(description__icontains=query))
    return render(request, 'tasks/index.html',
                  context={'tasks': tasks})


def complete_task(request, pk):
    task = Task.objects.filter(id=pk).first()
    task.done = True
    task.save()
    return redirect('/completed')


def completed_list(request):
    tasks = Task.objects.filter(done=True)
    return render(request, 'tasks/completed.html',
                  context={'tasks':tasks})





