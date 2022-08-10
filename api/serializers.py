from rest_framework import serializers
from .models import Task
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        # どのモデルのシリアライザーか定義する
        model = User
        # GETで表示させる項目を定義
        fields = ('id', 'username', 'password')
        # パスワードはWriteOnlyに設定
        extra_kwargs = {'password': { 'write_only': True, 'required': True}}
    # 必要に応じてオーバーライドする内容を書く
    # パスワードをハッシュ化した
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

class TaskSerializer(serializers.ModelSerializer):
    # created_atを読みやすい表記に設定する
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M", read_only=True)
    updated_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M", read_only=True)

    class Meta:
        model = Task
        fields = ('id', 'title', 'created_at', 'updated_at')