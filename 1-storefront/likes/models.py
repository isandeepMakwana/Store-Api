from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.auth.models import User

# Create another genric reationship
# not good paractices , please use genric as refrence tags app


class LikedItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    liked_item_object = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    liked_item_id = models.PositiveIntegerField()
    user_object = GenericForeignKey("liked_item_object", "liked_item_id")


# to craete instance of LikedItem
# LikedItem(
#    user=user_name,
#    user_object=ContentType.objects.get_for_model(car1),
#    liked_item_id=car.id
# )
