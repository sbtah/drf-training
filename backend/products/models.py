from django.conf import settings
from django.db import models


User = settings.AUTH_USER_MODEL  # Custom User model.


class ProductQuerySet(models.QuerySet):
    def is_public(self):
        return self.filter(public=True)


class ProductManage(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return ProductQuerySet(self.model, using=self._db)

    def search(self, query, user=None):
        return self.get_queryset().filter(public=True).filter(title__icontains=query)


class Product(models.Model):

    user = models.ForeignKey(User, default=1, null=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=15, decimal_places=2, default=99.99)
    public = models.BooleanField(default=True)

    @property
    def sale_price(self):
        return "%.2f" % (float(self.price) * 0.8)

    def get_discount(self):
        return 123
