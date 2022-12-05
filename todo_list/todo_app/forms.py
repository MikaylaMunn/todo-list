from django.forms import ModelForm
from todo_app.models import Task, Comment, Tag

class TaskForm(ModelForm):
    '''
    creating a task form the input box and the field required is called description
    '''
    class Meta:
        model = Task
        fields = ['description']

class TagForm(ModelForm):
    class Meta:
        model = Tag
        fields = ['name']
class CommentForm(ModelForm):
    '''
    creating a field for the body and calling it body
    '''
    class Meta:
        model = Comment
        fields = ['body']
    def __init__(self, *args,**kwargs):
        task = kwargs.pop('task_object')
        super().__init__(*args,**kwargs)
        self.instance.task = task