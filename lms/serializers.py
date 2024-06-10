from rest_framework import serializers

from lms.models import Course, Lesson


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'


class CourseSerializer(serializers.ModelSerializer):
    information_all_lessons = LessonSerializer(many=True, read_only=True)
    number_of_lessons = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Course
        fields = ['id', 'title', 'description', 'number_of_lessons', 'information_all_lessons']

    def get_number_of_lessons(self, course):
        return Lesson.objects.filter(course=course).count()

    def create(self, validated_data):
        lesson = validated_data.pop('information_all_lessons')
        course = Course.objects.create(**validated_data)
        for lessson in lesson:
            Lesson.objects.create(course=course, **lessson)
            return course


class CourseDitailSerializer(serializers.ModelSerializer):
    number_of_lessons = serializers.SerializerMethodField(read_only=True)
    information_all_lessons = LessonSerializer(many=True, read_only=True)

    def get_number_of_lessons(self, course):
        return Lesson.objects.filter(course=course).count()

    class Meta:
        model = Course
        fields = ['id', 'title', 'description', 'number_of_lessons', 'information_all_lessons']
