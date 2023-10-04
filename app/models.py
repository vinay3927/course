from django.db import models

class Course(models.Model):
    title = models.CharField(max_length=255)
    course_code = models.CharField(max_length=20)
    description = models.TextField()

    def __str__(self):
        return self.title

class CourseDelivery(models.Model):
    year = models.PositiveIntegerField()
    semester = models.PositiveSmallIntegerField()
    course = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.course} - {self.year} - {self.semester}"

    def get_course_code(self):
        try:
            course_obj = Course.objects.get(title=self.course)
            return course_obj.course_code
        except Course.DoesNotExist:
            return None
