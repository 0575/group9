from rest_framework import serializers
from .models import UserFav
from rest_framework.validators import UniqueTogetherValidator

class UserFavSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )
    class Meta:
        model = UserFav
        validators = [
            UniqueTogetherValidator(
                queryset=UserFav.objects.all(),
                fields=('user', 'goods'),
                message="already favorited"
            )
        ]
        fields = ("user", "goods", "id")