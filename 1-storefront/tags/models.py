from django.db import models
from django.contrib import contenttypes
# Create Genric Relationships

# class Tag(models.Model):
#     label = models.CharField(max_length=255)

# class TagItem(models.Model):
#     #what tag applied to what object
#     tag = models.ForeignKey(Tag,on_delete=models.CASCADE)
#     #type (product , video , artical)
#     content_types = models.ForeignKey(contenttypes, on_delete=models.CASCADE)
#     # ID
#     object_id = models.PositiveIntegerField()
