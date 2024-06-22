from rest_framework import serializers

from lms.models import Course, Lesson, Subscription
from lms.validators import YoutubeLinkValidator


class LessonSerializer(serializers.ModelSerializer):
    validators = [YoutubeLinkValidator(field='video')]

    class Meta:
        model = Lesson
        fields = '__all__'


class CourseSerializer(serializers.ModelSerializer):
    information_all_lessons = LessonSerializer(many=True, source='course')
    number_of_lessons = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Course
        fields = ['id', 'title', 'description', 'number_of_lessons', 'information_all_lessons']

    def get_number_of_lessons(self, course):
        return Lesson.objects.filter(course=course).count()

    def create(self, validated_data):
        lesson = validated_data.pop('information_all_lessons')
        course = Course.objects.create(**validated_data)
        for lesson in lesson:
            Lesson.objects.create(course=course, **lesson)
            return course


class CourseDitailSerializer(serializers.ModelSerializer):
    number_of_lessons = serializers.SerializerMethodField(read_only=True)
    information_all_lessons = LessonSerializer(many=True, source='course')
    subscription = serializers.SerializerMethodField(read_only=True)

    def get_number_of_lessons(self, course):
        return Lesson.objects.filter(course=course).count()

    def get_subscription(self, course):
        user = self.context.get('request').user
        course = self.context.get('view').kwargs.get('pk')
        subscription = Subscription.objects.filter(user=user, course=course)
        if subscription.exists():
            return True
        else:
            return False

    class Meta:
        model = Course
        fields = ['id', 'title', 'description', 'number_of_lessons', 'information_all_lessons', 'subscription']


class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = '__all__'
