from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SectionViewSet, SubsectionViewSet, section_list, subsection_detail, subsection_list

router = DefaultRouter()
router.register(r'sections', SectionViewSet)
router.register(r'subsections', SubsectionViewSet)

urlpatterns = [
    path('api/sections/', section_list),
    path('api/subsections/', subsection_list),
    path('api/subsection/<int:pk>/', subsection_detail, name='subsection-detail'),
    path('', include(router.urls)),
]
