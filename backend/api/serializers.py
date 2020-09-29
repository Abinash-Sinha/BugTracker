from rest_framework import serializers
from .models import NewBug, NewProject

class NewBugSerializer(serializers.ModelSerializer):

    class Meta:
        model = NewBug
        fields = ('pk', 'name', 'email', 'bugName', 'bugDescription', 'project', 'date')

class NewProjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = NewProject
        fields = ('pk', 'name', 'email', 'project_name', 'project_desc', 'date')
