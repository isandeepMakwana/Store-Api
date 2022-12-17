from django.contrib import admin, messages
from . import models
from django.db.models import Count
from django.urls import reverse
from django.utils.html import format_html, urlencode

# TODO registring Models
"""
# from .models import *
# admin.site.register(models.Address)
# admin.site.register(models.Customer)
# admin.site.register(models.Product)

# admin.site.register(models.Collection)
# admin.site.register(models.Order)
# admin.site.register(models.OrderItem)
# admin.site.register(models.Cart)
# admin.site.register(models.CartItem)
# admin.site.register(models.Promotion)
"""

# TODO Customizing the List Page


@admin.register(models.Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ["first_name", "last_name", "membership"]
    list_editable = ["membership"]
    ordering = ["first_name", "last_name"]
    list_per_page = 10
    # NOTE add search to the list page
    search_fields = ["first_name__istartswith", "last_name__istartswith"]


"""
assignment
@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["title", "unit_price"]
    list_editable = ["unit_price"]  # make field editable
    list_per_page = 10  # records in one page
"""

# NOTE [django ModelAdmin](https://docs.djangoproject.com/en/4.1/ref/contrib/admin/filters/)


# TODO Adding Computed Columns

# create a inventory_status columns


# @admin.register(models.Product)
# class ProductAdmin(admin.ModelAdmin):
#     list_display = ["title", "unit_price", "inventory_status"]
#     list_editable = ["unit_price"]
#     list_per_page = 10

#     @admin.display(ordering="inventory")
#     def inventory_status(self, product):
#         return "Low" if product.inventory < 10 else "OK"


# TODO selecting Related Objects


@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = [
        "title",
        "unit_price",
        "inventory_status",
        "collection",
        # "collection__id", # not able to use
        "collection_title",
    ]
    list_editable = ["unit_price"]
    list_per_page = 10
    # quesyset.select_releated
    list_select_related = ["collection"]
    # NOTE add filtering on list page
    list_filter = ["collection", "last_update"]
    # NOTE adding custom actions
    actions = ["clear_inventory"]

    search_fields = ["title"]

    # TODO customizing Forms(add product form)

    """exclude = ["promotions"]
    autocomplete_fields = ["collection"]  # it need search field in collection class
    prepopulated_fields = {"slug": ["title"]}
    # if you want some filed not neccesary to fill the add in model like descriptions=models.TextFiled(null=True,blank=True)
    # [django validators](https://docs.djangoproject.com/en/4.1/ref/validators/)"""

    @admin.display(
        ordering="collection"
    )  # instend of using collection_title we need to use collection it's django rules i don't know
    def collection_title(self, product):
        return product.collection.title

    @admin.display(ordering="inventory")
    def inventory_status(self, product):
        return "Low" if product.inventory < 10 else "OK"

    def clear_inventory(self, request, queryset):
        updated_count = queryset.update(inventory=0)
        self.message_user(
            request,
            f"{updated_count} products were successfully updated",
            messages.success,
        )


# TODO Overriding the Base QuerySet


# @admin.register(models.Collection)
# class CollectionAdmin(admin.ModelAdmin):
#     list_display = ["title", "products_count"]

#     @admin.display(ordering="products_count")
#     def products_count(self, collection):
#         return collection.products_count

#     def get_queryset(self, request):
#         return super().get_queryset(request).annotate(products_count=Count("product"))


# TODO Providing Links to Other Pages


@admin.register(models.Collection)
class CollectionAdmin(admin.ModelAdmin):
    list_display = ["title", "products_count"]
    search_fields = ["title"]

    @admin.display(ordering="products_count")
    def products_count(self, collection):
        url = (
            reverse("admin:store_product_changelist")
            + "?"
            + urlencode({"collection__id": str(collection.id)})
        )
        return format_html(
            "<a href='{}'>{}</a>",
            url,
            collection.products_count,
        )

    def get_queryset(self, request):
        return super().get_queryset(request).annotate(products_count=Count("product"))


# TODO Editing Children Using inline


# class OrderItemInline(admin.TabularInline):
#     model = models.OrderItem


class OrderItemInline(admin.TabularInline):
    autocomplete_fields = ["product"]
    model = models.OrderItem
    min_num = 1
    max_num = 10
    extra = 0


@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ["id", "placed_at", "customer"]
    autocomplete_fields = ["customer"]
    inlines = [OrderItemInline]
