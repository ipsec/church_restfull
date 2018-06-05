from rest_framework import viewsets

from news.models import News
from news.serializers import NewsSerializer


class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.filter(public=True).order_by('published_data')
    serializer_class = NewsSerializer
    http_method_names = ['get']
