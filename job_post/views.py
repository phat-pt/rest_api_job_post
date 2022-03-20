from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import get_object_or_404

from rest_framework import viewsets
from .models import JobPost
from datetime import datetime, timedelta
from .serializers import JobPostSerializer


class JobPostViewSet(viewsets.ModelViewSet):
    today = datetime.today()
    queryset = JobPost.objects.filter(ingestion_time__gte = datetime.now() - timedelta(days=1))
    serializer_class = JobPostSerializer
     