from rest_framework import serializers

from lms.models import Course, Lesson


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'


class CourseSerializer(serializers.ModelSerializer):
    information_all_lessons = LessonSerializer()

    class Meta:
        model = Course
        fields = "__all__"


class CourseDitailSerializer(serializers.ModelSerializer):
    number_of_lessons = serializers.SerializerMethodField()
    information_all_lessons = LessonSerializer()

    def get_number_of_lessons(self, course):
        return Lesson.objects.filter(course=course).count()

    class Meta:
        model = Course
        fields = ('id', 'title', 'description', 'number_of_lessons')
