from rest_framework import serializers

from tasks.models import Task, Comment


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = Task.Meta.fields


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = Comment.Meta.fields
