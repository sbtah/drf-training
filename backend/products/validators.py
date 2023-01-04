from products.models import Product
from rest_framework.validators import UniqueValidator
from rest_framework import serializers


def validate_title(value):
    qs = Product.objects.filter(title__iexact=value)
    if qs.exists():
        raise serializers.ValidationError(f"{value}: is already a Product name.")
    return value


# another way of doing validation.
unique_product_title = UniqueValidator(queryset=Product.objects.all(), lookup="iexact")
