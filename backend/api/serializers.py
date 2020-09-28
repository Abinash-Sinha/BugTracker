from rest_framework import serializers
from .models import NewBug

class NewBugSerializer(serializers.ModelSerializer):

    class Meta:
        model = NewBug
        fields = ('pk', 'name', 'email', 'bugName', 'bugDescription', 'project', 'date')