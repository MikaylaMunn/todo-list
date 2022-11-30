from django.shortcuts import redirect, render
from django.views import View
# Create your views here.

from todo_app.models import Task, Comment
from todo_app.forms import TaskForm, CommentForm

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
        return redirect('home')
class TaskDetailView(View):
    def get(self,request,task_id):
        task = Task.objects.get(id=task_id)
        task_form = TaskForm(instance=task)
        comment = Comment.objects.filter(task_id = task_id)
        comment_form = CommentForm(task_object = task)
        html_data = {
            'task': task,
            'form' : task_form,
            'comment_list': comment,
            'comment_form': comment_form
        }
        return render (
            request = request,
            template_name= 'details.html',
            context = html_data
        )
    def post(self, request, task_id):
        task = Task.objects.get(id=task_id)
        task_form = TaskForm(request.POST, instance = task)
        if 'update' in request.POST: 
            task_form.save()
        elif 'delete' in request.POST:
            task.delete()
        elif 'add' in request.POST:
            comment_form = CommentForm(request.POST, task_object = task)
            comment_form.save()
            return redirect('task_detail', task.id)
        return redirect('home')