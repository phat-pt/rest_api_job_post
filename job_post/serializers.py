from rest_framework import serializers

from job_post.models import JobPost

class JobPostSerializer(serializers.ModelSerializer):

    class Meta: 
        model = JobPost
        fields = ('__all__')