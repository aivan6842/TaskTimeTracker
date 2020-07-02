from django.forms import ModelForm
from .models import User, Task, TrainImage

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password')

class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ('taskName', 'description')

class ImageForm(ModelForm):
    class Meta:
        model = TrainImage
        fields = ('image', )
