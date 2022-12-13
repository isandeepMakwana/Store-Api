from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

# Create Genric Relationships


class Tag(models.Model):
    label = models.CharField(max_length=255)


class TaggedItem(models.Model):
    # what tag applied to what object
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    # type (product , video , artical)
    # ID
    # real product object

    # product = models.ForeignKey(ContentType , on_delete=models.CASCADE)
    # or
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)

    object_id = (
        models.PositiveIntegerField()
    )  # drowback is if the object primary key is not integer then we trable

    # product_object = GenericForeignKey()
    content_object = GenericForeignKey()
