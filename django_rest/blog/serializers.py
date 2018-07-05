from blog.models import Event
from rest_framework import serializers

class EventSerializer(serializers.ModelSerializer):
	class Meta:
		model = Event
		fields = ('event_id', 'name', 'date', 'text')
#
#	def create(self, validated_data):
#		return Event.objects.create(**validated_data)

#	def update(self, instance, validated_data):
#		instance.event_id = validated_data.get('event_id', instance.event_id)
#		instance.name = validated_data.get('name', instance.name)
#		instance.date = validated_data.get('date', instance.date)
#		instance.text = validated_data.get('text', instance.text)
#		instance.save()
#		return instance
