# Api app for processing pictures

Test assignment for a vacancy - Django app that provides several endpoints, for processing files.

API is made using Django Rest Framework. File processing runs as Celery task asynchronously.
If file that is uploaded to API is a valid picture, app turns it to black and white format and adds frame.

## Start in Docker


### Start locally
To start in docker locally you should use commands:

```
sudo docker compose build
sudo docker compose up
```
App will appear at *http://127.0.0.1/api/files/*


### Start on prod

To start in docker on production you should add environment variable to  **server** container configuration in docker-compose.yml:

```
server:
  ...
  environment:
    ALLOWED_HOSTS: <Your production server ip>
  ...
```

And then run

```
sudo docker compose up --build -d
```


## API endpoints:

* **/api/upload/**

   Endpoint to upload files.

   Request code example:
   ```
    >>> url = ".../api/upload/"
    >>> image_path = "/home/user/Pictures/image.png"
    >>> requests.post(url, files={"file": open(image_path, "rb")})
   ```
   Response:
   ```
    {"id":1,
     "file":"/media/uploaded_files/image.png","uploaded_at":"2023-09-23T10:28:55.011098Z",
     "processed":false}
   ```

* **api/files/**

  Endpoint to list all files.

  Request code example:
  ```
   >>> url = ".../api/files/"
   >>> requests.get(url)
  ```
  Response:
  ```
  [
      {
          "id": 1,
          "file": "http://<HOST>/media/uploaded_files/test_file.txt",
          "uploaded_at": "2023-09-23T09:51:47.014173Z",
          "processed": true
      },
      {
          "id": 2,
          "file": "http://<HOST>/media/uploaded_files/image.png",
          "uploaded_at": "2023-09-23T10:28:55.011098Z",
          "processed": true
      }
  ]
  ```
