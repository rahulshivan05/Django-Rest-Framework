from rest_framework import generics, mixins
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Product
from .serializers import Productserializers
from api.mixins import StaffEditorPermissionMixin

# from django.http import Http404
from django.shortcuts import get_object_or_404
# Create your views here.


class ProductListCreateAPIView(StaffEditorPermissionMixin, generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = Productserializers
    # authentication_classes = [
    #     authentication.SessionAuthentication,
    #     TokenAuthentication,
    # ]
    # permission_classes = [permissions.DjangoModelPermissions]

    # I comment out below code because i use StaffEditorPermissionMixin
    # permission_classes = [permissions.IsAdminUser, IsStaffEditorPermission]

    def perform_create(self, serializer):
        # return super().perform_create(serializer)
        # serializer.save(user=self.request.user)
        # print(serializer.validated_data)
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content')
        if content is None:
            content = title
        serializer.save(content=content)
        # Send a Django signal


product_list_create_view = ProductListCreateAPIView.as_view()


class ProductDetailAPIView(StaffEditorPermissionMixin, generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = Productserializers
    # lookup_field = 'id or pk'
    # permission_classes = [permissions.IsAdminUser, IsStaffEditorPermission]


# you can also do this yourself
product_detail_view = ProductDetailAPIView.as_view()


class ProductUpdateAPIView(StaffEditorPermissionMixin, generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = Productserializers
    lookup_field = 'pk'
    # permission_classes = [permissions.IsAdminUser, IsStaffEditorPermission]

    def perform_update(self, serializer):
        instance = serializer.save()
        if not instance.content:
            instance.content = instance.title
            # instance.save()


# you can also do this yourself
product_update_view = ProductUpdateAPIView.as_view()


class ProductDeleteAPIView(StaffEditorPermissionMixin, generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = Productserializers
    # permission_classes = [permissions.IsAdminUser, IsStaffEditorPermission]
    # lookup_field = 'id or pk'

    def perform_destroy(self, instance):
        super().perform_destroy(instance)


# you can also do this yourself
product_delete_view = ProductDeleteAPIView.as_view()


# class ProductListAPIView(generics.ListAPIView):
#     '''
#     Not gonna use this method
#     '''
#     queryset = Product.objects.all()
#     serializer_class = Productserializers


class ProductMixinView(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    generics.GenericAPIView
):
    queryset = Product.objects.all()
    serializer_class = Productserializers
    lookup_field = 'pk'

    def get(self, request, *args, **kwargs):  # HTTP --> Get
        # print(args, kwargs)
        pk = kwargs.get('pk')
        if pk is not None:
            return self.retrieve(request, *args, **kwargs)
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    # def perform_create(self, serializer):
    #     # return super().perform_create(serializer)
    #     # serializer.save(user=self.request.user)
    #     # print(serializer.validated_data)
    #     title = serializer.validated_data.get('title')
    #     content = serializer.validated_data.get('content')
    #     if content is None:
    #         content = title
    #     serializer.save(content=content)

    # def post(): # HTTP --> Post returns


product_mixin_view = ProductMixinView.as_view()


@api_view(['GET', 'POST'])
def product_alt_view(request, pk=None, *args, **kwargs):
    method = request.method

    if method == 'GET':
        # url_args??
        # get request -> detail view
        if pk is not None:
            obj = get_object_or_404(Product, pk=pk)
            data = Productserializers(obj, many=False).data
            return Response(data)

        ########### 1st option ###########
        # if pk is not None:
        #     queryset = Product.objects.filter(pk=pk)
        #     if queryset.exists():
        #         raise Http404

        # list view
        queryset = Product.objects.all()
        data = Productserializers(queryset, many=True).data
        return Response(data)

    if method == 'POST':
        serializer = Productserializers(data=request.data)
        if serializer.is_valid(raise_exception=True):
            title = serializer.validated_data.get('title')
            content = serializer.validated_data.get('content')
            if content is None:
                content = title
            serializer.save(content=content)
            return Response(serializer.data)
        return Response({"Invalid": "Please enter a valid data"}, status=400)
