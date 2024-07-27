from rest_framework import serializers
from .models import RetreatDetails, BookingDetails
from .utils.date_time_util import get_date_time_dict_in_ist

class RetreatSerializer(serializers.ModelSerializer):
    class Meta:
        model = RetreatDetails
        fields = '__all__'

    def validate_title(self, value):
        if RetreatDetails.objects.filter(title=value).exists():
            raise serializers.ValidationError("A retreat with this title already exists.")
        return value

    def create(self, validated_data):
        return RetreatDetails.objects.create(**validated_data)
    
    def to_representation(self, instance):
        """
        Convert the instance to its serialized representation.
        """
        representation = super().to_representation(instance)

        representation["created_at"] = get_date_time_dict_in_ist(
            datetime_utc_object=instance.created_at, noon_format=True
        )
        return representation

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookingDetails
        fields = '__all__'
        read_only_fields = ['id', 'created_at']

    def validate(self, data):
        user_id = data.get('user_id')
        retreat_id = data.get('retreat')
        booking_date = data.get('booking_date')

        # Check if the booking already exists for the given user, retreat, and date
        if BookingDetails.objects.filter(user_id=user_id, retreat_id=retreat_id, booking_date=booking_date).exists():
            raise serializers.ValidationError("Retreat already booked by the user for this date.")

        return data

    def create(self, validated_data):
        return BookingDetails.objects.create(**validated_data)


    def to_representation(self, instance):
        """
        Convert the instance to its serialized representation.
        """
        representation = super().to_representation(instance)

        representation["created_at"] = get_date_time_dict_in_ist(
            datetime_utc_object=instance.created_at, noon_format=True
        )
        return representation

