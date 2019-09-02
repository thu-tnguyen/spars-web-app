from rest_framework import serializers

from pages.models import Project

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = [
            'title', 
            'division', 
            'mentor', 
            'year', 
            'author'
        ]