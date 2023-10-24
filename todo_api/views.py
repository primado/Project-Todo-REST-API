from django.http import HttpResponse
from rest_framework  import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import permissions
from rest_framework import status
from todo.models import Todo
from .serializers import *
from .permissions import *
from rest_framework.exceptions import PermissionDenied
# from django.shortcuts import render

# Create your views here.





class TodoViewSet(viewsets.ViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]

    def list(self, request):
        todos = Todo.objects.filter(user=request.user)
        serializer = []

        for todo in todos:
            self.check_object_permissions(request, todo)
            serializer_todo = TodoSerializer(todo, context={'request': request})
            serializer.append(serializer_todo.data)

        return Response(serializer, status=status.HTTP_200_OK)
  
    

    def create(self, request):
        serializer = TodoSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data['user']
            user == request.user
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def retrieve(self, request, pk=None):

        try:
            todos = self.queryset.get(pk=pk)

        except Todo.DoesNotExist as e:
            return Response({"errors": e}, status=status.HTTP_404_NOT_FOUND)
        
        self.check_object_permissions(request, todos)
        serilizer = TodoSerializer(todos)
          
        return Response(serilizer.data, status=status.HTTP_200_OK)
       
        
    def update(self, request, pk=None):
        try:
            todo = self.queryset.get(pk=pk)
            self.permission_classes = [permissions.IsAuthenticated, IsOwnerCanEdit]
            self.check_object_permissions(request, todo)
            serializer = TodoSerializer(todo, data=request.data)
            if serializer.is_valid():
                serializer.validated_data['user'] = request.user
                
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Todo.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        except PermissionDenied:
            return Response({"detail": "You do not have permission to update this todo item"}, status=status.HTTP_403_FORBIDDEN)
        
    def destroy(self, request, pk=None):
        try: 
            todo = self.queryset.get(pk=pk)

            if  todo.user == request.user:
                todo.delete()
                return Response(status=status.HTTP_204_NO_CONTENT)
            else:
                return Response("Permission denied", status=status.HTTP_403_FORBIDDEN)

        except Todo.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
            
        
        


