import os
from api.models import File
from api.serializers import FileSerializer, FileFieldFileSerializer
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.conf import settings


class FileTests(APITestCase):
    def test_no_files_list(self):
        url = reverse('api1:list_files')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 0)

    def test_upload_file(self):
        url = reverse('api1:upload_file')
        test_files_dir = os.path.join(settings.BASE_DIR, "api", "files_for_tests")
        for file_name in os.listdir(test_files_dir):
            file_path = os.path.join(test_files_dir, file_name)
            with open(file_path, "rb") as file:
                response = self.client.post(url, data={"file": file}, format='multipart')
                self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_list_files(self):
        url = reverse('api1:list_files')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        expected_data = FileSerializer(File.objects.all(), many=True).data
        self.assertEqual(expected_data, response.data)