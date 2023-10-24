from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import TodoViewSet

app_name = 'todo_api'

router = DefaultRouter()
router.register(r'todos', TodoViewSet)

urlpatterns = [
    path('api/', include(router.urls))
]


