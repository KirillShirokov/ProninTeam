from django.urls import include, path
from rest_framework import routers

from collects.views import CollectsViewSet
from payments.views import PaymentsViewSet
from users.views import CustomUserViewSet


router_v1 = routers.DefaultRouter()
router_v1.register(r'collects', CollectsViewSet)
router_v1.register(r'payments', PaymentsViewSet)
router_v1.register(r'users', CustomUserViewSet)

urlpatterns = [
    path('', include(router_v1.urls)),
    path('auth/', include('djoser.urls.authtoken')),
]
