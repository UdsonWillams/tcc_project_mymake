from cart.api.v1.helper import actualize_cart, devoluting_products
from cart.models import Carts
from products.models import Products
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

from .serializers import CreateCartsSerializer, ConcluirCartsSerializer, ListCartsSerializer
from rest_framework.response import Response
from rest_framework.status import HTTP_204_NO_CONTENT,HTTP_201_CREATED, HTTP_400_BAD_REQUEST
from rest_framework.generics import (
    CreateAPIView,
    ListAPIView, 
    UpdateAPIView,
    DestroyAPIView
)

class CreateCartsView(CreateAPIView):
    serializer_class = CreateCartsSerializer

class ListCartsView(ListAPIView):
    serializer_class = ListCartsSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = Carts.objects.all()    
        return queryset

class ListCartsByIdView(ListAPIView):
    serializer_class = ConcluirCartsSerializer

    def get_queryset(self):
        queryset = Carts.objects.all()    
        return queryset
class DeleteCartsView(DestroyAPIView):
    serializer_class = ConcluirCartsSerializer

    def get_queryset(self):
        queryset = Carts.objects.all()    
        return queryset

    def delete(self, request, *args, **kwargs):
        try:
            devoluting_status = devoluting_products(kwargs)
            if devoluting_status:
                return Response({"has_devoluting": devoluting_status}, status=HTTP_204_NO_CONTENT)
            else:
                return Response({"has_devoluting": devoluting_status}, status=HTTP_400_BAD_REQUEST)
        except Exception:
            raise ValueError()

class FinalizeCartsView(DestroyAPIView):
    serializer_class = ConcluirCartsSerializer

    def get_queryset(self):
        queryset = Carts.objects.all()    
        return queryset

class UpdateProductsView(UpdateAPIView):
    serializer_class = ConcluirCartsSerializer

    def get_queryset(self):
        queryset = Carts.objects.all()    
        return queryset

    def put(self, request, *args, **kwargs):
        try:
            import ipdb
            ipdb.set_trace()
            devoluting_status = actualize_cart(url=kwargs, body=request.data)
            if devoluting_status:
                return Response({"is_actualize": devoluting_status}, status=HTTP_201_CREATED)
            else:
                return Response({"is_actualize": devoluting_status}, status=HTTP_400_BAD_REQUEST)
        except Exception:
            raise ValueError()
