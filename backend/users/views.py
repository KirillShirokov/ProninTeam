from djoser.views import UserViewSet
from rest_framework.pagination import LimitOffsetPagination

from users.serializers import UserSerializer
from users.models import User


class CustomUserViewSet(UserViewSet):
    """Вьюсет пользователей."""

    serializer_class = UserSerializer
    queryset = User.objects.all()
    pagination_class = LimitOffsetPagination
