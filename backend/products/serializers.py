from rest_framework import serializers
from rest_framework.reverse import reverse
from products.models import Product
from products.validators import validate_title, unique_product_title
from api.serializers import UserPublicSerializer


class ProductSerializer(serializers.ModelSerializer):

    owner = UserPublicSerializer(source="user", read_only=True)
    # my_user_data = serializers.SerializerMethodField(read_only=True)
    discount = serializers.SerializerMethodField(read_only=True)
    edit_url = serializers.SerializerMethodField(read_only=True)
    url = serializers.HyperlinkedIdentityField(
        view_name="products:product-detail", lookup_field="pk"
    )
    # email = serializers.EmailField(source="user.email", read_only=True)
    title = serializers.CharField(validators=[unique_product_title])
    # name = serializers.CharField(source="title", read_only=True)

    class Meta:
        model = Product
        fields = [
            "owner",
            "url",
            "edit_url",
            # "email",
            "pk",
            "title",
            #    "name",
            "content",
            "price",
            "sale_price",
            "discount",
        ]

    # def validate_title(self, value):
    #     # If you wish to access request... there is a way in context.
    #     request = self.context.get("request")
    #     user = request.user

    #     # if there is a user relation...
    #     qs = Product.objects.filter(user=user, title__iexact=value)
    #     qs = Product.objects.filter(user=user, title__iexact=value)
    #     if qs.exists():
    #         raise serializers.ValidationError(f"{value}: is already a Product name.")
    #     return value

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
        # Request is in context here.
        request = self.context.get("request")
        if request is None:
            return None
        return reverse(
            "products:product-update", kwargs={"pk": obj.pk}, request=request
        )

    # This can be done with serializer (UserPublicSerializer...)
    # def get_my_user_data(self, obj):
    #     return {
    #         "username": obj.user.username,
    #     }
