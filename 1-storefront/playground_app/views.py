from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q, F
from store.models import Product


def say_hello(request):
    # # get all product data(object)
    # query_set = Product.objects.all()
    # # for product in query_set:
    # #     print(product)
    # print(list(query_set))

    # ----
    # retrieving Objects
    # product = Product.objects.get(id=1)
    # product = Product.objects.get(pk=1)

    # -------
    # try:
    #     product = Product.objects.get(pk=0)
    # except ObjectDoesNotExist:
    #     pass

    # -------

    # product = Product.objects.filter(pk=0).exists()
    # print(product)
    # return render(request, "hello.html", {"name": product})

    # ----------

    # Filtering Objects

    # queryset = Product.objects.filter(unit_price=20)
    # queryset = Product.objects.filter(unit_price > 20)  # NOT WROKING
    # queryset = Product.objects.filter(unit_price__gt=20)

    # [queryset api](https://docs.djangoproject.com/en/4.1/ref/models/querysets/)
    # queryset = Product.objects.filter(unit_price__range=(20,30))
    # -----

    # keyword=value
    # queryset = Product.objects.filter(collection_id=1)
    # queryset = Product.objects.filter(collection__id__range=(1, 3))
    # queryset = Product.objects.filter(title__icontains="coffee") # it check case incase sensitive
    # # queryset = Product.objects.filter(title__icontains="-coffee")
    # queryset = Product.objects.filter(last_update__year=2021)
    # queryset = Product.objects.filter(description__isnull=True)

    # -------

    # complex lookups Using Q objects

    # inventory < 10 AND price <20

    # queryset = Product.objects.filter(inventory__lt=10, unit_price__lt=20)
    # or
    # queryset = Product.objects.filter(inventory__lt=10).filter(unit_price__lt=20)

    # return render(request, "hello.html", {"name": queryset})

    # inventory < 10 OR price <20
    # queryset = Product.objects.filter(Q(inventory__lt=10) | Q(unit_price__lt=20))
    # queryset = Product.objects.filter(Q(inventory__lt=10) & ~Q(unit_price__lt=20))

    # ------
    # Referencing Fields using F Objects

    # Products : inventory = price
    # queryset = Product.objects.filter(inventory="unit_price") #error
    # queryset = Product.objects.filter(inventory=F("unit_price"))
    # queryset = Product.objects.filter(~Q(inventory=F("collection__id")))

    # -----------
    # sorting

    # queryset = Product.objects.order_by("title")  # title ASC
    # queryset = Product.objects.order_by("-title")  # title DESC
    # queryset = Product.objects.order_by("unit_price", "-title")
    # queryset = Product.objects.order_by("unit_price", "-title").reverse()
    # queryset = Product.objects.filter(collection_id=1).order_by("unit_price")

    # product = Product.objects.order_by("unit_price")[0]  # return product
    # # or
    # product = Product.objects.latest("unit_price")  # without sort it return product

    # -------------

    # Lilmiting Results and offset

    # 0,1,2,3,4
    queryset = Product.objects.all()[:5]
    # 5,6,7,8,9
    queryset = Product.objects.all()[5:10]

    return render(request, "hello.html", {"name": list(queryset)})

    # --------------------------------------------


# def say_hello(request):
