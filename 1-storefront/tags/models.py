from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

# Create Genric Relationships

# --------------------------
# create custom manager
class TaggedItemManager(models.Manager):
    def get_tags_for(self, obj_type, obj_id):
        content_type = ContentType.objects.get_for_model(obj_type)
        quereyset = TaggedItem.objects.select_related("tag").filter(
            content_type=content_type, object_id=obj_id
        )
        return quereyset


# -------------------------


class Tag(models.Model):
    label = models.CharField(max_length=255)

    def __str__(self):
        return self.label


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

    # -----------------------
    objects = TaggedItemManager()
