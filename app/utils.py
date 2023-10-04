from rest_framework import status
from rest_framework.response import Response
from .models import Course, CourseDelivery
from .serializers import CourseSerializer, CourseDeliverySerializer

# Courses API

def createCourse(request): 
    data = request.data
    course = Course.objects.create(
        title = data['title'],
        course_code = data['code'],
        description = data['description'],
    )
    serializer = CourseSerializer(course, many = False)
    return Response(serializer.data, status=status.HTTP_201_CREATED)


def getCoursesList(request):
    courses = Course.objects.all()
    serializer = CourseSerializer(courses, many=True)
    return Response(serializer.data)

def getCourseDetail(request, pk):
    course = Course.objects.get(pk=pk)
    serializer = CourseSerializer(course)
    return Response(serializer.data)


def deleteCourse(request, pk):
    course = Course.objects.get(pk=pk)
    course.delete()
    return Response('Course was deleted!', status=status.HTTP_204_NO_CONTENT)

# Course Deliveries API

def createCourseDelivery(request): 
    data = request.data
    delivery = CourseDelivery.objects.create(
        year = data['year'],
        semester = data['semester'],
        course = data['course'],
    )
    serializer = CourseDeliverySerializer(delivery, many = False)
    return Response(serializer.data, status=status.HTTP_201_CREATED)

def getCourseDeliveryList(request):
    deliveries = CourseDelivery.objects.all()

    serialized_data = []

    for delivery in deliveries:
        serialized_delivery = CourseDeliverySerializer(delivery).data
        serialized_delivery['course_code'] = delivery.get_course_code()
        serialized_data.append(serialized_delivery)

    return Response(serialized_data, status=status.HTTP_200_OK)

def listCourseDeliveriesByYearAndSemester(request, year, semester):
    course_deliveries = CourseDelivery.objects.filter(year=year, semester=semester)

    serialized_data = []

    for delivery in course_deliveries:
        serialized_delivery = CourseDeliverySerializer(delivery).data
        serialized_delivery['course_code'] = delivery.get_course_code()
        serialized_data.append(serialized_delivery)

    return Response(serialized_data, status=status.HTTP_200_OK)


def getCourseDeliveryDetail(request, year, semester, instance_id):
    course_delivery = CourseDelivery.objects.get(year=year, semester=semester, pk=instance_id)
    serializer = CourseDeliverySerializer(course_delivery)
    return Response(serializer.data)


def deleteCourseDelivery(request, year, semester, instance_id):
    course_delivery = CourseDelivery.objects.get(year=year, semester=semester, pk=instance_id)
    course_delivery.delete()
    return Response('Course delivery was deleted!', status=status.HTTP_204_NO_CONTENT)
