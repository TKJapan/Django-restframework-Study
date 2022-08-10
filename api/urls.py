# ①インポート
from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from api.views import TaskViewSet, CreateUserView, MyProfileView

# ②routerを設定
router = routers.DefaultRouter()
# ModelViewSetを継承しているものは、routerに登録
router.register('tasks', TaskViewSet, basename='tasks')

urlpatterns = [
    # Genericsを継承しているものは、urlpatternsに含める
    # myselfというパスに、MyProfileViewを紐づける
    path('myself/', MyProfileView.as_view(), name='myself'),
    path('register/', CreateUserView.as_view(), name='register'),
    path('', include(router.urls)),
]