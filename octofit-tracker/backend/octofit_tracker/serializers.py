from rest_framework import serializers

# Example serializer for ObjectId conversion
class ObjectIdField(serializers.Field):
    def to_representation(self, value):
        return str(value)
    def to_internal_value(self, data):
        return data
