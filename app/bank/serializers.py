from rest_framework import serializers
from bank.models import Branch


# class Branch_Serializer(serializers.Serializer):
#     #id, location_name, location
#     id = serializers.IntegerField(read_only=True)
#     location_name = serializers.CharField(max_length=30)
#     location = serializers.CharField(max_length=30)

#     def create(self, validated_data):
#         return Bank.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         instance.location_name = validated_data.get('name', instance.location_name)
#         instance.location = validated_data.get('location', instance.location)
#         instance.save()
#         return instance
class Branch_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Branch
        fields = [
            'id',
            'location_name',
            'location'
        ]