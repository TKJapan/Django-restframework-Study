# ①インポート

from django.contrib import admin
from django.urls import path

# ②includeを追加
from django.conf.urls import include

# pathとviewを紐づけている
urlpatterns = [
    path('admin/', admin.site.urls),
    # ③追記
    path('api/', include('api.urls')),
    path('authen/', include('djoser.urls.jwt'))
]
