from django.conf.urls import url, include
from rest_framework import routers
from smb import views

router = routers.DefaultRouter()
router.register('elements', views.ElementViewSet)
router.register('temperatures', views.TemperatureViewSet)


urlpatterns = [
    url(r'^$', views.index),
    url(r'^', include(router.urls)),
    # url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]