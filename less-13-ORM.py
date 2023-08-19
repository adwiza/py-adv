from django.db import models
from django.db.models import Q
from django.utils import timezone
from django.db import connection


class CommonnInfo(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()

    class Meta:
        abstract = True


class Student(CommonnInfo):
    home_group = models.CharField(max_length=5)


class Place(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=80)


class Restaurant(Place):
    serves_hot_dogs = models.BooleanField(default=False)
    serves_pizza = models.BooleanField(default=False)


class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)


# Proxy models
#     table created  only for original model
#     cannot change the model behavior


class MyPerson(Person):
    class Meta:
        proxy = True

    def do_something(self):
        # ...
        pass


#  CRUD

# from flavors.model import Flavor
# from store.exceptions import OutOfStock, CorruptedDatabase

# def list_flavor_line_item(sku):
#     try:
#         return Flavor.objects.get(sku=sku, quantity__gt=0)
#     except Flavor.DoesNotExists:
#         msg = 'We are out of {}'.format(sku)
#     except Flavor.MultipleObjectReturned:
#         msg = 'Multiple items have SKU {}. Please fix'.format(sku)
#         raise CorruptedDatabase(msg)

# from promos.models import Promo

# def fun_function(**kwargs):
#     """Find working ice cream promo"""
#     results = Promo.objects.active()
#     results = results.filter(
#         Q(name__startswith=name) |
#         Q(description__icontaints=name)
#     )
#     results = results.exclude(status='melted')
#     results == results.select_related('flavors')
#     return results

#  Object managers


class PublishedManager(models.Manager):
    use_for_related_fields = True

    def published(self, **kwargs):
        return self.filter(pub_date__lte=timezone.now(), **kwargs)


class FlavorReview(models.Model):
    review = models.CharField(max_length=255)
    pub_date = models.DateTimeField()

    # add our custom model manager
    objects = PublishedManager()


def my_custom_sql(self):
    cursor = connection.cursor()
    cursor.execute("UPDATE bar SET foo = 1 WHERE baz - %s", [self.baz])
    cursor.execute("SELECT foo FROM bar WHERE baz = %s", [self.baz])
    row = cursor.fetchone()
    return row

