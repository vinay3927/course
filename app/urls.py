from django.urls import path
from . import views

urlpatterns = [
    # Courses API
    path('courses/', views.getCourses, name='course-list'),
    path('courses/<int:pk>/', views.getCourseDetail, name='course-detail'),

    # Course Deliveries API
    path('instances/', views.getCourseDeliveries, name='course-delivery'),
    path('instances/<int:year>/<int:semester>/', views.getCourseDeliveries, name='list-course-deliveries'),
    path('instances/<int:year>/<int:semester>/<int:instance_id>/', views.getCourseDeliveries, name='course-delivery-detail'),

    # Get Routes
    path('getroutes/', views.getRoutes, name='get-routes'),
]
