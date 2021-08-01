from rest_framework import serializers
from .models import Messages


class MessagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Messages
        fields = ('user_name', 'text', 'message_time', )

