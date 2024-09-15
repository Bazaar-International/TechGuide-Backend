from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.decorators import action
from .models import Section, Subsection
from .serializers import SectionSerializer, SubsectionSerializer

class SectionViewSet(viewsets.ModelViewSet):
    queryset = Section.objects.all()
    serializer_class = SectionSerializer

    def perform_update(self, serializer):
        instance = serializer.save()
        instance.html_content = markdown(instance.markdown_content)
        instance.save()

class SubsectionViewSet(viewsets.ModelViewSet):
    queryset = Subsection.objects.all()
    serializer_class = SubsectionSerializer

    def perform_update(self, serializer):
        instance = serializer.save()
        instance.html_content = markdown(instance.markdown_content)
        instance.save()


@api_view(['GET'])
def section_list(request):
    sections = Section.objects.all()
    serializer = SectionSerializer(sections, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def subsection_list(request):
    subsections = Subsection.objects.all()
    serializer = SubsectionSerializer(subsections, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def subsection_detail(request, pk):
    try:
        subsection = Subsection.objects.get(pk=pk)
    except Subsection.DoesNotExist:
        raise Http404("Subsection does not exist")

    serializer = SubsectionSerializer(subsection)
    return Response(serializer.data)