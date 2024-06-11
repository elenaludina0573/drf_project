from rest_framework import serializers

from lms.models import Course, Lesson


class LessonSerializer(serializers.ModelSerializer):
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

    def get_number_of_lessons(self, course):
        return Lesson.objects.filter(course=course).count()

    class Meta:
        model = Course
        fields = ['id', 'title', 'description', 'number_of_lessons', 'information_all_lessons']
