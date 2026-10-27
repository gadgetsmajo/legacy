from rest_framework import serializers

from .models import Inquiry


class InquirySerializer(serializers.ModelSerializer):
    kind = serializers.ChoiceField(choices=Inquiry.Kind.choices, write_only=True)
    status = serializers.CharField(read_only=True)
    created_at = serializers.DateTimeField(read_only=True)

    class Meta:
        model = Inquiry
        fields = (
            'id', 'kind', 'name', 'email', 'phone', 'business_name',
            'product', 'quantity', 'subject', 'message', 'status', 'created_at',
        )
        read_only_fields = ('id', 'status', 'created_at')

    def validate(self, attrs):
        kind = attrs.get('kind')
        if kind == Inquiry.Kind.QUOTE:
            if not attrs.get('product') or not attrs.get('quantity'):
                raise serializers.ValidationError('Quote requests require a product and quantity.')
        if kind == Inquiry.Kind.PARTNER and not attrs.get('business_name'):
            raise serializers.ValidationError('Partner inquiries require a business name.')
        return attrs
