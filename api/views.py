from rest_framework.permissions import AllowAny
from rest_framework import generics
from rest_framework import viewsets
from .serializers import TaskSerializer, UserSerializer
from .models import Task

# createに特化したAPIビュー
# 新規でアカウントを作るビュー
class CreateUserView(generics.CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)

# ユーザープロフィールを表示
class MyProfileView(generics.RetrieveUpdateAPIView):
    serializer_class = UserSerializer
    def get_object(self):
        return self.request.user

# ３行書けばデフォルトでCreate,Update,Delete,Readができる
class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer