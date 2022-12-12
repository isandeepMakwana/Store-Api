from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q, F, DecimalField
from django.db.models import Count, Max, Min, Avg
from django.db.models import Value, Func, ExpressionWrapper
from django.db.models.functions import Concat
from store.models import Product, OrderItem, Order, Customer


def say_hello(request):

    #-----------------------

    # Querying Generic Relationships









    return render(request, "hello.html", {"products": queryset})
    # --------------------------------------------


# def say_hello(request):
