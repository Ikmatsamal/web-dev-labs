from rest_framework import generics
from rest_framework import mixins
from api.models import Product
from api.serializers import ProductSerializer
from rest_framework.response import Response
from rest_framework import status


class ProductListAPIView(mixins.ListModelMixin,
                         mixins.CreateModelMixin,
                         generics.GenericAPIView):
    
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

  
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs) 

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs) 

class ProductDetailAPIView(mixins.RetrieveModelMixin,
                           mixins.UpdateModelMixin,
                           mixins.DestroyModelMixin,
                           generics.GenericAPIView):
    
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_url_kwarg = 'product_id' 

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs) 

    def put(self, request, *args, **kwargs):
        instance = self.get_object()
        
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        
        is_changed = False
        for field, value in serializer.validated_data.items():
            if hasattr(instance, field):
                old_value = getattr(instance, field)
                
                print(f"Checking field: {field}")
                print(f"Old: {old_value} (type: {type(old_value)})")
                print(f"New: {value} (type: {type(value)})")
                
                
                if old_value != value:
                    is_changed = True
                    break
                
        if not is_changed:
            return Response(
                {"detail": "No changes detected."}, 
                status=status.HTTP_400_BAD_REQUEST
            )
            
        return self.update(request, *args, **kwargs) 

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs) 