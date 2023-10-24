from rest_framework import serializers
from accounts.models import CustomUser
from todo.models import Todo



class TodoSerializer(serializers.ModelSerializer):

    class Meta: 
        model = Todo
        fields = '__all__'

