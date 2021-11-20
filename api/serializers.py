from rest_framework import serializers


class MemoSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'

