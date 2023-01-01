from rest_framework import authentication, generics, mixins
from rest_framework.response import Response
from products.models import Product
from products.serializers import ProductSerializer
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404

from api.authentication import TokenAuthentication
from api.mixins import StaffEditorPermissionMixin


class ProductListAPIView(StaffEditorPermissionMixin, generics.ListAPIView):
    """List."""

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    authentication_classes = [
        authentication.SessionAuthentication,
        TokenAuthentication,
    ]


product_list_view = ProductListAPIView.as_view()


class ProductDetailAPIView(StaffEditorPermissionMixin, generics.RetrieveAPIView):
    """Detail."""

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    authentication_classes = [
        authentication.SessionAuthentication,
        TokenAuthentication,
    ]


product_detail_view = ProductDetailAPIView.as_view()


class ProductUpdateAPIView(StaffEditorPermissionMixin, generics.UpdateAPIView):
    """Update."""

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = "pk"
    authentication_classes = [
        authentication.SessionAuthentication,
        TokenAuthentication,
    ]

    def perform_update(self, serializer):
        instance = serializer.save()
        if not instance.content:
            instance.content = instance.title


product_update_view = ProductUpdateAPIView.as_view()


class ProductDeleteAPIView(StaffEditorPermissionMixin, generics.DestroyAPIView):
    """Delete."""

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = "pk"
    authentication_classes = [
        authentication.SessionAuthentication,
        TokenAuthentication,
    ]

    def perform_destroy(self, instance):
        return super().perform_destroy(instance)


product_delete_view = ProductDeleteAPIView.as_view()


class ProductCreateAPIView(StaffEditorPermissionMixin, generics.CreateAPIView):
    """Create."""

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    authentication_classes = [
        authentication.SessionAuthentication,
        TokenAuthentication,
    ]

    def perform_create(self, serializer):
        # This is for removing email from data used for creating Product object.
        serializer.validated_data.pop("email")
        title = serializer.validated_data.get("title")
        content = serializer.validated_data.get("content") or None
        if content is None:
            content = title
        serializer.save(content=content)


product_create_view = ProductCreateAPIView.as_view()


# TEST Function view.
@api_view(["GET", "POST"])
def product_alt_view(request, pk=None, *args, **kwargs):
    """"""
    if request.method == "GET":
        if pk is None:
            queryset = Product.objects.all()
            data = ProductSerializer(queryset, many=True).data
            return Response(data)
        else:
            obj = get_object_or_404(Product, pk=pk)
            data = ProductSerializer(obj).data
            return Response(data)

    if request.method == "POST":
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            title = serializer.validated_data.get("title")
            content = serializer.validated_data.get("content") or None
            if content is None:
                content = title
            serializer.save(content=content)
            return Response(serializer.data)
        else:
            return Response({"Invalid": "Wrong Data."}, status=400)


# Test Class View.
class ProductMixinView(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    generics.GenericAPIView,
):
    """Test View"""

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = "pk"

    def get(self, request, *args, **kwargs):
        pk = kwargs.get("pk")
        if pk is not None:
            return self.retrieve(request, *args, **kwargs)
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def perform_create(self, serializer):
        content = serializer.validated_data.get("content") or None
        if content is None:
            content = "This is a single view doing create magic..."
        serializer.save(content=content)


product_mixin_view = ProductMixinView.as_view()
