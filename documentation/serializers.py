from rest_framework import serializers
from .models import Section, Subsection

class SectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Section
        fields = ['id', 'title', 'order', 'markdown_content', 'html_content']
        read_only_fields = ['html_content']  # Make html_content read-only

class SubsectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subsection
        fields = ['id', 'section', 'title', 'order', 'markdown_content', 'html_content']
        read_only_fields = ['html_content']  # Make html_content read-only
