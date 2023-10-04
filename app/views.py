from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .utils import getCourseDetail, getCourseDeliveryDetail, getCoursesList, createCourse, deleteCourse, deleteCourseDelivery, listCourseDeliveriesByYearAndSemester, createCourseDelivery,getCourseDeliveryList

# Create your views here.


@api_view(['GET'])
def getRoutes(request):
    routes = [
        {
            'Endpoint': '/api/courses/',
            'method': 'GET',
            'body': None,
            'description': 'Returns a list of all courses'
        },
        {
            'Endpoint': '/api/courses/<int:pk>/',
            'method': 'GET',
            'body': None,
            'description': 'Returns details of a specific course'
        },
        {
            'Endpoint': '/api/courses/',
            'method': 'POST',
            'body': {
                'title': 'Course Title',
                'course_code': 'Course Code',
                'description': 'Course Description'
            },
            'description': 'Creates a new course'
        },
        {
            'Endpoint': '/api/courses/<int:pk>/',
            'method': 'DELETE',
            'body': None,
            'description': 'Deletes a specific course'
        },
        {
            'Endpoint': '/api/instances/',
            'method': 'POST',
            'body': {
                'year': 'YYYY',
                'semester': 'N',
                'course_id': 'Course ID'
            },
            'description': 'Creates a new instance of a course delivery'
        },
        {
            'Endpoint': '/api/instances/<int:year>/<int:semester>/',
            'method': 'GET',
            'body': None,
            'description': 'Returns a list of course deliveries for a specific year and semester'
        },
        {
            'Endpoint': '/api/instances/<int:year>/<int:semester>/<int:instance_id>/',
            'method': 'GET',
            'body': None,
            'description': 'Returns details of a specific course delivery'
        },
        {
            'Endpoint': '/api/instances/<int:year>/<int:semester>/<int:instance_id>/',
            'method': 'DELETE',
            'body': None,
            'description': 'Deletes a specific course delivery'
        },
    ]
    return Response(routes)


#Courses

@api_view(['GET', 'POST'])
def getCourses(request):

    if request.method == 'GET':
        return getCoursesList(request)

    if request.method == 'POST':
        return createCourse(request)


@api_view(['GET', 'DELETE'])
def getCourseDetail(request, pk):

    if request.method == 'GET':
        return getCourseDetail(request, pk)

    if request.method == 'DELETE':
        return deleteCourse(request, pk)

#Courses Deliveries

@api_view(['GET', 'DELETE', 'POST'])
def getCourseDeliveries(request, year=None, semester=None, instance_id=None):
    if year is None and semester is None and instance_id is None:
        if request.method == 'POST':
            # Call the createCourseDelivery function and pass the request
            return createCourseDelivery(request)
        elif request.method == 'GET':
            # Handle other cases (e.g., GET for listing deliveries)
            return getCourseDeliveryList(request)
    
    elif year is not None and semester is not None and instance_id is None:
        if request.method == 'GET':
            return listCourseDeliveriesByYearAndSemester(request, year, semester)
        elif request.method == 'DELETE':
            return deleteCourseDelivery(request, year, semester)
        
    else:
        if request.method == 'GET':
            # Call the getCourseDeliveryDetail function and pass the request, year, semester, and instance_id
            return getCourseDeliveryDetail(request, year, semester, instance_id)
        elif request.method == 'DELETE':
            # Call the deleteCourseDelivery function and pass the request, year, semester, and instance_id
            return deleteCourseDelivery(request, year, semester, instance_id)

    return Response(status=status.HTTP_400_BAD_REQUEST)