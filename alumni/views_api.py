from rest_framework import generics
from rest_framework.response import Response
from rest_framework import filters
from .serializers import AlumniSerializer
from .models import Alumni



class AlumniList(generics.ListCreateAPIView):

	queryset = Alumni.objects.all()
	serializer_class = AlumniSerializer
	filter_backends = (filters.SearchFilter, filters.DjangoFilterBackend)
	filter_fields = ('is_active')
	filter_fields = ('name', 'mail')

class AlumniDetail(generics.RetrieveUpdateDestroyAPIView):
	
	queryset = Alumni.objects.all()
	serializer_class = AlumniSerializer