from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q, F, DecimalField
from django.db.models import Count, Max, Min, Avg
from django.db.models import Value, Func, ExpressionWrapper
from django.db.models.functions import Concat
from django.contrib.contenttypes.models import ContentType
from store.models import Product, OrderItem, Order, Customer
from tags.models import TaggedItem


def say_hello(request):

    # -----------------------

    # Querying Generic Relationships

    # content_type = ContentType.objects.get_for_model(Product)
    # queryset = TaggedItem.objects.filter(content_type=content_type, object_id=1)

    content_type = ContentType.objects.get_for_model(Product)
    queryset = TaggedItem.objects.select_related("tag").filter(
        content_type=content_type, object_id=1
    )

    # --------------------------------------------

    # custom Managers

    # every time product and id pura nhi nhi pass karne wale , let's create a custom manager

    TaggedItem.objects.get_tags_for(Product, 1)

    # ===> get_tags_for function banana hai tags ke model me
    """
    class TaggedItemManager(models.Manager):
    def get_tags_for(self, obj_type, obj_id):
        content_type = ContentType.objects.get_for_model(obj_type)
        quereyset = TaggedItem.objects.select_related("tag").filter(
            content_type=content_type, object_id=obj_id
        )
        return quereyset


    and
    class taggedItem
    append one more filed
    objects = TaggedItemManager()
    """

    # then it works

    #  --------------------------

    # understanding QuerySet Cache

    # you need write you operation with queryset basic of Cache handling

    # like:
    queryset = Product.objects.all()  # we get queryset
    list(queryset)  # convert kiya list me and store kiya cache me
    queryset[0]  # it produce the output of 0th index

    # ===> but isme problem yee hai ki jab hum queryset[0] karte hai to wo queryset pe fir se opreation karta hai <===

    # ======><><><><> sol:
    queryset = Product.objects.all()
    queryset[0]
    list(
        queryset
    )  # convert kiya list me and store kiya cache me but queryset of zero ka data cache se le liya so useko kam traverse karna pada

    return render(request, "hello.html", {"products": queryset})


# def say_hello(request):
