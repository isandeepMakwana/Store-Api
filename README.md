

# 1-storefront

> Django debug toolbar

`python -m pip install django-debug-toolbar`

[https://django-debug-toolbar.readthedocs.io/en/latest/installation.html](https://django-debug-toolbar.readthedocs.io/en/latest/installation.html)

# 2- Models

> Building an e-commerce data model
- relation btw products with collection
![products with collection](docs/imgs/Sandeep%20Makwana%20-%20Screen%20Shot%202022-11-29%20at%207.51.14%20PM.png)

- relation btw products ,cart,cartitem

![products ,cart,cartitem](docs/imgs/Sandeep%20Makwana%20-%20Screen%20Shot%202022-11-29%20at%207.51.24%20PM.png)

- relation btw products , orders, orderItem ,customer
![products , orders, orderItem ,customer](docs/imgs/Sandeep%20Makwana%20-%20Screen%20Shot%202022-11-29%20at%207.51.31%20PM.png)
- relation btw products and tag
![](docs/imgs/Sandeep%20Makwana%20-%20Screen%20Shot%202022-11-29%20at%207.51.37%20PM.png)

> Organizing Models in Apps
>> ![](docs/imgs/Sandeep%20Makwana%20-%20Screen%20Shot%202022-11-29%20at%208.02.14%20PM.png)

> Let's create a 2 django
app

```bash
python manage.py startapp store
python manage.py startapp tags
```


> Creating Models
[https://docs.djangoproject.com/en/4.1/ref/models/fields/](https://docs.djangoproject.com/en/4.1/ref/models/fields/)
---

```python
from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    # 9999.99
    price = models.DecimalField(max_digits=6, decimal_places=2)
    inventory = models.IntegerField()
    last_update = models.DateTimeField(auto_now=True)


class Customer(models.Model):
    MEMBERSHIP_BRONZE='B'
    MEMBERSHIP_SILVER='S'
    MEMBERSHIP_GOLD='G'
    MEMBERSHIP_CHOICES=[
        (MEMBERSHIP_BRONZE,'Bronze'),
        (MEMBERSHIP_SILVER,'Sliver'),
        (MEMBERSHIP_GOLD,'Gold')
        ]
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.IntegerField(max_length=10)
    birth_date = models.DateField(null=True)
    membership = models.CharField(max_length=1 , choices=MEMBERSHIP_CHOICES , default=MEMBERSHIP_BRONZE)

class Orders(models.Model):
    PAYMENT_STATUS_CHOICE = [("P", "Pending"), ("C", "Complete"), ("F", "Failed")]
    placed_at = models.DateTimeField(auto_now_add=True)
    payment_status = models.CharField(
        max_length=1, choices=PAYMENT_STATUS_CHOICE, default="P"
    )

```


===


















> What is docker

A platform for biulding running and shipping application and consistently build,run and ship application

> Container

- An isolated environment for running an application

- Allow running multiple app in isolation
Are lightweight
Use os of the host
start queickly
need less hardware resource

`let's geate project and dockerzie`

create Folder :
```bash
 mkdir hello-docker
```

> Inside of this folder and create one file
 ```javascript
  -->file_name.js<--
  console.log("hello World");
  ```


> Instruction To Deploy Application

- start with os
- install node
- copy app files
- run node file-name.js (main_file)

go-back to hello-docker folder and create one file <mark>Dockerfile<mark>

	-->dockerfile<---
