from django.conf.urls import url, include
from rest_framework_jwt.views import obtain_jwt_token
<<<<<<< HEAD

=======
>>>>>>> 5c8885099d01975c7b8f8ab06edcb6cf0fa43440
urlpatterns = [
	url(r'^sensei/', include('sensei.urls_api')),
	url(r'^alumni/', include('alumni.urls_api')),
	url(r'^auth/', obtain_jwt_token),
<<<<<<< HEAD
=======

>>>>>>> 5c8885099d01975c7b8f8ab06edcb6cf0fa43440
	# url(r'^cinta/', include('desescuela.urls_api'))
]
