from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q, F, DecimalField
from django.db.models import Count, Max, Min, Avg
from django.db.models import Value, Func, ExpressionWrapper
from django.db.models.functions import Concat
from django.contrib.contenttypes.models import ContentType
from store.models import Product, OrderItem, Order, Customer, Collection
from tags.models import TaggedItem


# def say_hello(request):
#     from django.shortcuts import render


# from django.http import HttpResponse
# from django.core.exceptions import ObjectDoesNotExist
# from django.db.models import Q, F
# from django.db.models import Count, Max, Min, Avg
# from django.db.models import Value
# from store.models import Product, OrderItem, Order, Customer

# {% for product in products %}
#     <p>{{product.id}} - {{product.customer.first_name}}</p>
#     {% endfor %}


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
    # queryset = Product.objects.all()[:5]
    # # 5,6,7,8,9
    # queryset = Product.objects.all()[5:10]

    # ---------------------------

    # Selecting Fields to Query

    # queryset = Product.objects.values("id", "title")  # return dict objects
    # queryset = Product.objects.values("id", "title", "collection__title")
    """
    SELECT "store_product"."id",
       "store_product"."title",
       "store_collection"."title"
    FROM "store_product"
    INNER JOIN "store_collection"
        ON ("store_product"."collection_id" = "store_collection"."id")
    """
    # queryset = Product.objects.values_list(
    #     "id", "title", "collection__title"
    # )  # return tuple objects
    # # ------------------------
    # distinct

    # queryset = OrderItem.objects.values("product_id").distinct()

    # # in or nested query
    # queryset = Product.objects.filter(
    #     id__in=OrderItem.objects.values("product_id").distinct()
    # ).order_by("title")

    # -------------------------
    # deferring Fields
    # not remmended method
    # queryset = Product.objects.only("id", "title")  # drow back if try to get
    """
    product.unit_price
    then yee 1000 spreate queries karta hai like this

    SELECT "store_product"."id",
       "store_product"."title"
    FROM "store_product"

    SELECT "store_product"."id",
           "store_product"."unit_price"
    FROM "store_product"
    WHERE "store_product"."id" = 1
    LIMIT 21
    then 1000 more querys for id 2 to 1000
    """

    # -------------

    # queryset = Product.objects.defer("description")
    """isme only descripition load nhi hota baki sub hota hai
    SELECT "store_product"."id",
       "store_product"."title",
       "store_product"."slug",
       "store_product"."unit_price",
       "store_product"."inventory",
       "store_product"."last_update",
       "store_product"."collection_id"
    FROM "store_product"
    """

    # ---------------------------

    # Selecting Related Objects

    # select_releted(1) “follows” foreign-key relationships, selecting additional related-object data when it executes its query
    # prefetch_related(n) does a separate lookup for each relationship and does the “joining” in Python.

    # One uses select_related when the object that you're going to be selecting is a single object, so OneToOneField or a ForeignKey. You use prefetch_related when you're going to get a “set” of things, so ManyToManyFields as you stated or reverse ForeignKeys.

    """
    {% for product in products %}
    <p>{{product.title}} - {{product.collection.title}}</p>
    """
    # queryset = Product.objects.all()
    # 1001 queries just becouse we call collection.title

    ## solv :- we need to pre-load data so we use select_related()
    queryset = Product.objects.select_related("collection").all()
    # return data in 1 query becouse it use inner-join
    # Forward ForeignKey relationship
    """
    SELECT "store_product"."id",
       "store_product"."title",
       "store_product"."slug",
       "store_product"."description",
       "store_product"."unit_price",
       "store_product"."inventory",
       "store_product"."last_update",
       "store_product"."collection_id",
       "store_collection"."id",
       "store_collection"."title",
       "store_collection"."featured_product_id"
    FROM "store_product"
    INNER JOIN "store_collection"
    ON ("store_product"."collection_id" = "store_collection"."id")
    """

    # queryset = Product.objects.select_related("collection__someOtherField").all()

    # queryset = Product.objects.prefetch_related(
    #     "promotions"
    # ).all()  # Reverse ForeignKey relationship
    """
    SELECT "store_product"."id",
       "store_product"."title",
       "store_product"."slug",
       "store_product"."description",
       "store_product"."unit_price",
       "store_product"."inventory",
       "store_product"."last_update",
       "store_product"."collection_id"
    FROM "store_product"

    SELECT ("store_product_promotions"."product_id") AS "_prefetch_related_val_product_id",
       "store_promotion"."id",
       "store_promotion"."description",
       "store_promotion"."discount"
    FROM "store_promotion"
    INNER JOIN "store_product_promotions"
        ON ("store_promotion"."id" = "store_product_promotions"."promotion_id")
    WHERE "store_product_promotions"."product_id" IN (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25,..............1000)

    """

    # note:
    # 1. select_related me single filed connected like forigenkey wali field le sakte ho
    # 2. pefech_related me manytomany jisme object se object connected ho .

    # wer can use both in same time

    # queryset =Product.objects.prefetch_related("promotions").select_related("collection").all()

    # Get the las 5 orders with their customer and items (incl product)

    # queryset = (
    #     Order.objects.select_related("customer")
    #     .prefetch_related("orderitem_set__product")
    #     .order_by("-placed_at")[:5]
    # )

    # ---------------

    # Aggregating Objects

    #  count = Product.objects.aggregate(Count("id"))
    #  count = Product.objects.aggregate(Count("description"))
    #  count = Product.objects.aggregate(count=Count("id"))
    #  count = Product.objects.aggregate(discriptions_count=Count("description"))
    #  count = Product.objects.aggregate(count=Count("id"), min_price=Min("unit_price"))
    #  count = Product.objects.filter("collection__id=1").aggregate(
    #      count=Count("id"), min_price=Min("unit_price")
    #  )
    # --------------
    # Annotating Objects (means create new fild )
    # sometime we need aditional attribute object while quering theam

    #  queryset = Customer.objects.annotate(is_new=True) # error : boolean value not accepted

    # in django have Expression class which is a base class of all type of expression_classes
    #  - Value
    #  - F
    #  - Func
    #  - Aggregate

    #  queryset = Customer.objects.annotate(is_new=Value(True))
    # queryset = Customer.objects.annotate(new_id=F("id") + 1)
    # ---------------------
    # calling database functions

    # CONCAT
    # queryset = Customer.objects.annotate(
    #     full_name=Func(F("first_name"), Value(" "), F("last_name"), function="CONCAT")
    # )

    # # OR

    # queryset = Customer.objects.annotate(
    #     full_name=Concat("first_name", Value(" "), "last_name")
    # )

    # [django database functions](https://docs.djangoproject.com/en/4.1/ref/models/database-functions/)

    # --------------------
    # Grouping Data

    # djang have a restrictions we can't able to use order_set
    # instead of order_set we use order
    queryset = Customer.objects.annotate(order_count=Count("order"))

    # ------------------
    # Working with Expression Wrappers
    # Expression is base class of all the expression classes
    # - Value , F , Func , Aggregate , ExpressionWrapper

    # queryset = Product.objects.annotate(discounted_price=F('unit_price')*0.8) #error decimal filed can't multlply by floadfiled

    # queryset = Product.objects.annotate(
    #     discounted_price=ExpressionWrapper(
    #         F("unit_price") * 0.8, output_field=DecimalField()
    #     )
    # )

    # OR

    # discounted_price = ExpressionWrapper(
    #     F("unit_price") * 0.8, output_field=DecimalField()
    # )
    # queryset = Product.objects.annotate(discounted_price=discounted_price)

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
    )  # convert kiya list me and store kiya cache me but queryset of zero ka data cache se le liya so useko kam traverse karna pada.

    return render(request, "hello.html", {"products": queryset})


def say_hello2(request):
    # ======================================================================================================================================

    # Creating Objects
    # method 1:(Remmanded)

    # collection = Collection()
    # collection.title = "video Games"
    # collection.featured_product = Product(pk=1)
    # collection.featured_product_id = 1
    # collection.save()

    # method 2:

    # collection = Collection(
    #     title="video game2", featured_product=Product(pk=1), featured_product_id=12
    # )
    # collection.save()

    # # method 3:
    # # short method

    # Collection.objects.create(title="a",featured_product=Product(pk=1), featured_product_id=12)


    
    return render(request, "hello.html")
