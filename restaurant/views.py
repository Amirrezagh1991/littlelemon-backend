from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Menu, Booking
from .serializers import MenuSerializer, BookingSerializer



# Create your views here.
def index(request):
    return render(request, 'index.html', {})


class MenuItemsView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class BookingViewSet(viewsets.ModelViewSet):
   queryset = Booking.objects.all()
   serializer_class = BookingSerializer
   permission_classes = [IsAuthenticated]

# class MenuItemsView(generics.ListCreateAPIView):
#     queryset = MenuItem.objects.all()
#     serializer_class = MenuItemSerializer
#     search_fields = ['category__title']
#     ordering_fields = ['price', 'inventory']

#     def get_permissions(self):
#         permission_classes = []
#         if self.request.method != 'GET':
#             permission_classes = [IsAuthenticated]

#         return [permission() for permission in permission_classes]


# class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = MenuItem.objects.all()
#     serializer_class = MenuItemSerializer

#     def get_permissions(self):
#         permission_classes = []
#         if self.request.method != 'GET':
#             permission_classes = [IsAuthenticated]

#         return [permission() for permission in permission_classes]
