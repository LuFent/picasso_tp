from rest_framework.generics import CreateAPIView, ListAPIView
from .serializers import FileFieldFileSerializer, FileSerializer
from rest_framework import status
from rest_framework.response import Response
from .tasks import process_file
from .models import File


class UploadFileApiView(CreateAPIView):
    serializer_class = FileFieldFileSerializer

    def perform_create(self, serializer):
        instance = serializer.save()
        return instance

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        instance = self.perform_create(serializer)
        try:
            process_file.apply_async(kwargs={'file_id': instance.id})
        except Exception:
            instance.delete()
            return Response({"message": "Failed to start file processing"})
        headers = self.get_success_headers(serializer.data)
        instance_serializer = FileSerializer(instance)
        return Response(instance_serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class ListFilesApiView(ListAPIView):
    queryset = File.objects.all()
    serializer_class = FileSerializer