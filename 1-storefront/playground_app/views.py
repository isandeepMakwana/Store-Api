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

    return render(request, "hello.html", {"products": queryset})
    # --------------------------------------------




# def say_hello(request):
