

# 1-storefront

## Add toolbar in Django
> Django debug toolbar

```bash
python -m pip install django-debug-toolbar
```

[https://django-debug-toolbar.readthedocs.io/en/latest/installation.html](https://django-debug-toolbar.readthedocs.io/en/latest/installation.html)

---
# 2- Models

> Building an e-commerce data model
- relation btw products with collection
- ![products with collection](docs/imgs/Sandeep%20Makwana%20-%20Screen%20Shot%202022-11-29%20at%207.51.14%20PM.png)<br>

- relation btw products ,cart,cartitem

- ![products ,cart,cartitem](docs/imgs/Sandeep%20Makwana%20-%20Screen%20Shot%202022-11-29%20at%207.51.24%20PM.png)<br>

- relation btw products , orders, orderItem ,customer
- ![products , orders, orderItem ,customer](docs/imgs/Sandeep%20Makwana%20-%20Screen%20Shot%202022-11-29%20at%207.51.31%20PM.png)<br>
- relation btw products and tag
- ![](docs/imgs/Sandeep%20Makwana%20-%20Screen%20Shot%202022-11-29%20at%207.51.37%20PM.png)<br>

<br>
<br>

> Organizing Models in Apps
>> ![](docs/imgs/Sandeep%20Makwana%20-%20Screen%20Shot%202022-11-29%20at%208.02.14%20PM.png)<br>

> Let's create a 2 django
app

```bash
python manage.py startapp store
python manage.py startapp tags
```


> Creating Models
[https://docs.djangoproject.com/en/4.1/ref/models/fields/](https://docs.djangoproject.com/en/4.1/ref/models/fields/)
<br>

> - one_to_one
> - one_to_many
> - Circular dependency

Model file for store app
store-[model.py](1-storefront/store/models.py)


> - Generic Relationships
>
<mark>pending<mark>

Model file for tags app
tags-[model.py](1-storefront/tags/models.py)

---

# DataBase
`create migrations,running migration,reversiong mirgartions
,pupulation the database`

> - create mirgration
```bash
python manage.py makemigrations
```
all migrations created on migration folder -->
inner your store-app folder

>> create migration for spacific `app`
```bash
python manage.py makemigrations <app-name(store)>
```

imported notes:
![makemigration-error-in-module-1](docs/imgs/makemigration-1.png)
![makemigration-error-in-module-2](docs/imgs/makemigration-2.png)


> - Running migrations

```bash
python manage.py migrate
```

> <mark> sqlmigrate <mark>

- if you want to see the sql queries of your migration on the time of creation

```bash
python manage.py sqlmigrate
```

```bash
python manage.py sqlmigrate <app_name>
```


```bash
python manage.py sqlmigrate <app_name> <spacific migration (0003)>
```
![sqlmigrate](docs/imgs/sqlmigrate.png)


> customizing database schema

- change table name in database or much more
[django model metadata](https://docs.djangoproject.com/en/4.1/ref/models/options/)

- to change table name we need to go
`models.py`
```python
# add
class Meta:
  db_table='store_new_customer'

```
or you can add much more
```python
# add
class Meta:
  db_table='store_new_customer'
  indexes =[
    models.Index(fields=['last_name','first_name'])
  ]
```


> - Reverting Migrations

find migrations folder --> and inside of them delete last migration .py(like last file is 0004_smedfdfa.py) file
And run
```bash
python manage.py migration store(app-name) 0003(2nd-last-file-number)
```

<mark>but there as an issue<mark>

we deleted only migration file but the code change is still remaining that's why we `use git for this `

<mark> use git reset for reverting migrations <mark>
```gitbash
git reset --hard HEAD~1
```

UTC
> Running Custom SQL


![custom-sql-1](docs/imgs/custom_sql-1.png)

![custom-sql-2](docs/imgs/custom-sql-2.png)

![custom-sql-3](docs/imgs/custom-sql-3.png)

![custom-sql-4](docs/imgs/custom-sql-4.png)



> Generating Dummy Data<br>
[www.mockaroo.com/](https://www.mockaroo.com/)


---

# Django ORM (Object-relational Mappers)
~~sql='SELECT * FROM product~~
products= Product.objects.all()

benifits:
- Reduce complexity in code
- Make the code more understandable
- Help us get more done in less time

The best code is no code
,A good software engineer delivers working software in time



# Django Admin

- customizing the adming interface
- adding computed columns
- loading related objects
- adding search & filter
- implementing cutom actions
- Adding data validation

## setting up the Admin Site

```bash
python manage.py createsuperuser
```

> for change password
```bash
python manage.py changepassword admin
```

## to site_header
[project_urls](1-storefront/storefront/urls.py)


## Registering Models
[store_admin.py](1-storefront/store/admin.py)


----------------
---

# Django-Rest-API

## Building Restful APIs
- introduction to Restful APIs
- installing Django REST Framework
- creating API views
- Creating serializers
- serializing and deserializing models


## RESOURCES :
- Product
- Collection
- Cart

> URL (Uniform Resource Locator)
> - http://localhost:8000/products
> - http://localhost:8000/products/1
> - http://localhost:8000/products/1/reviews

## REPRESENTATIONS (Resource Representations):
- HTML
- XML
- JSON(javaScript Object Notation)


## HTTP Methods

- GET
- POST
- PUT (update hole thing)
- PATCH (update a single field)
- DELETE


# installing Django REST Framework
```bash
pipenv install djangorestframework
```


# let's Create API Views
[django-rest-api/store/views.py](django-rest-api/store/views.py)



# Serializer:(converts a model instace to a dictionary)
- [x] We need to convert product object to a JSON object
- [x] Serializer converts the product object to dict object

- [x] rest_framework have a jsocnrenderer class and this class have to render a method accept a dict object and returns json object.


install  django -nested- routs

```bash
pip install drf-nested-routers
```

install genric-filters
[django filters]()
```bash
pip install django-filter
```
set the app in installed app
===django_filters===,


# create a genric filters
[x] create filters.py and start writing
    [filters.py](2-Advanced-rest-api-viewset/store/filters.py)


# create searching
[store-views.py](2-Advanced-rest-api-viewset/store/views.py)


# Sorting

[store-views.py](2-Advanced-rest-api-viewset/store/views.py)


# Pagination
[store-views.py](2-Advanced-rest-api-viewset/store/views.py)
REST_FRAMEWORK = {
    "COERCE_DECIMAL_TO_STRING": False,
    "PAGE_SIZE": 10,
}

?\>> you can also add limit offset with this
\> and you can create own paginations

---

# Designing a shopping Card API

- creating a cart `post - /carts/` - {}
- getting a cart `get - /carts/:id` -{}
- deleting a cart `delete - /carts/:id` -{}
- Adding an item `post - /carts/:id/items` - {prodId,qty} - item
- Updating an item `patch -/carts/:id/items/:id` - {qty} - {qty}
- deleting an item `delete -/carts/:id/items/:id` - {} - {}

[source-files](3-Advanced-rest-api-building-shopping-cart-api/store/)


