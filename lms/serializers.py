from rest_framework import serializers

from lms.models import Course, Lesson


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'


class CourseSerializer(serializers.ModelSerializer):
    information_all_lessons = LessonSerializer(source='lesson_set', many=True)
    number_of_lessons = serializers.SerializerMethodField()

    class Meta:
        model = Course
        fields = '__all__'

    def get_number_of_lessons(self, course):
        return Lesson.objects.filter(course=course).count()

    def create(self, validated_data):
        lesson = validated_data('lesson_set')
        course = Course.objects.create(**validated_data)
        for lesson in lesson:
            Lesson.objects.create(course=course, **lesson)
            return course


class CourseDitailSerializer(serializers.ModelSerializer):
    number_of_lessons = serializers.SerializerMethodField()
    information_all_lessons = LessonSerializer(many=True)

    def get_number_of_lessons(self, course):
        return Lesson.objects.filter(course=course).count()

    class Meta:
        model = Course
        fields = ['id', 'title', 'description', 'number_of_lessons', 'information_all_lessons']
