from rest_framework import serializers

from invoice.models import Customer
from snippets.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES



class CustomerSerializer(serializers.Serializer):
    name = serializers.CharField()
    address = serializers.CharField()
    phone = serializers.CharField()

    def create(self, validated_data):
        return Customer.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.address = validated_data.get('address', instance.address)
        instance.phone = validated_data.get('phone', instance.phone)
        instance.save()
        return instance

""" 


class Product(serializers.Serializer):
    name = serializers.CharField(max_length=100, blank=True, default='')
    price = serializers.IntegerField()


class Invoice(serializers.Serializer):
    customer_id = serializers.ForeignKey(Customer)
    discount = serializers.IntegerField()
    total = serializers.IntegerField()


class InvoiceItem(serializers.Serializer):
    invoice_id =  serializers.ForeignKey(Invoice)
    product_id =  serializers.ForeignKey(Product)
    quantity =  serializers.IntegerField()


class SnippetSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(required=False, allow_blank=True, max_length=100)
    code = serializers.CharField(style={'base_template': 'textarea.html'})
    linenos = serializers.BooleanField(required=False)
    language = serializers.ChoiceField(choices=LANGUAGE_CHOICES, default='python')
    style = serializers.ChoiceField(choices=STYLE_CHOICES, default='friendly')

    def create(self, validated_data):
        return Snippet.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.code = validated_data.get('code', instance.code)
        instance.linenos = validated_data.get('linenos', instance.linenos)
        instance.language = validated_data.get('language', instance.language)
        instance.style = validated_data.get('style', instance.style)
        instance.save()
        return instance
        
        
"""