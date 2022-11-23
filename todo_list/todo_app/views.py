from django.shortcuts import render
from django.views import View
# Create your views here.

from todo_app.models import Task
from todo_app.forms import TaskForm

class HomeView(View):
    def get(self, request):
        tasks = Task.objects.all()
        task_form = TaskForm()
        html_data =  {
            'task_list': tasks,
            'form': task_form
        }
        return render(
            request = request,
            template_name= 'index.html',
           
            context = html_data
        )
    def post(self, request):
        tasks = Task.objects.all()
        task_form = TaskForm(request.POST)
        task_form.save()
        html_data =  {
            'task_list': tasks,
            'form': task_form
        }
        return render(
            request = request,
            template_name= 'index.html',
           
            context = html_data
        )