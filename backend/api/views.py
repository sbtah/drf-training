import json
from rest_framework.decorators import api_view
from rest_framework.response import Response

from django.forms.models import model_to_dict

# from django.http import JsonResponse, HttpResponse
from products.models import Product
from products.serializers import ProductSerializer


@api_view(["POST"])
def api_home(request, *args, **kwargs):
    """
    DRF Api view.
    """

    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        # instance = serializer.save()
        # print(instance)
        # print(serializer.data)
        return Response(serializer.data)
    else:
        return Response({"Invalid": "Wrong Data."}, status=400)
