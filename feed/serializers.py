"""
Serializers allow complex data such as querysets and model instances
to be converted to native Python datatypes that can then be easily
rendered into JSON, XML or other content types.
"""

from rest_framework import serializers
from .models import Course, CourseReviewData

class CourseSerializer(serializers.HyperlinkedModelSerializer):
    """Serializer for Course model."""
    class Meta:
        model = Course
        fields = ('code', 'name', 'semester')

class ReviewSerializer(serializers.HyperlinkedModelSerializer):
    """Serializer for CourseReviewData model."""
    class Meta:
        model = CourseReviewData
        fields = ('course', 'course_instructor', 'session')
        