from rest_framework import serializers

from .models import Product


class Productserializers(serializers.ModelSerializer):
    my_discount = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Product
        fields = [
            'title',
            'content',
            'price',
            'sale_price',
            'my_discount',  # is show as 'get_my_discount' instead of 'my_discount'
        ]

    def get_my_discount(self, obj):
        # try:
        #     return obj.get_discount()
        # except:
        #     return None

        if not hasattr(obj, 'id'):
            return None
        if not isinstance(obj, Product):
            return None
        return obj.get_discount()
