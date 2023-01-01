from rest_framework import serializers
from rest_framework.reverse import reverse
from products.models import Product


class ProductSerializer(serializers.ModelSerializer):

    discount = serializers.SerializerMethodField(read_only=True)
    edit_url = serializers.SerializerMethodField(read_only=True)
    url = serializers.HyperlinkedIdentityField(
        view_name="products:product-detail", lookup_field="pk"
    )
    email = serializers.EmailField(write_only=True)

    class Meta:
        model = Product
        fields = [
            "url",
            "edit_url",
            "email",
            "pk",
            "title",
            "content",
            "price",
            "sale_price",
            "discount",
        ]

    def validate_title(self, value):
        return value

    def create(self, validated_data):
        # email = validated_data.pop("email")
        obj = super().create(validated_data)
        # print(email, obj)
        return obj

    def get_discount(self, obj):
        if isinstance(obj, Product):
            return obj.get_discount()
        else:
            return None

    def get_edit_url(self, obj):
        request = self.context.get("request")
        if request is None:
            return None
        return reverse(
            "products:product-update", kwargs={"pk": obj.pk}, request=request
        )
