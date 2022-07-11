from rest_framework import serializers
from api.models import Dialogues

class DialoguesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dialogues
        fields = ('QANumber', 'UserTEXT', 'BotTEXT')
        # fields = ('UserTEXT', 'BotTEXT')