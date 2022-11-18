# Docker and Flask

For this assignment you will be creating a flask application to generate a QR code based on form input.

Submission Requirements:

1. QR code that links to your own project image on Dockerhub

Example:

* [My Project on Docker Hub QR Code](readme_images/docker_hub.png) <-view with your phone camera and click to go to the site

## Lesson Video

[Instructor Video](https://youtu.be/ATajsJRFWEs)

## Readings - No, really you should read these

* [How to Dockerize a Flask  Application](https://www.freecodecamp.org/news/how-to-dockerize-a-flask-app/)
* 
## Bonus Task - Good Docker practice, it demonstrates using JavaScript / NodeJS

* https://docs.docker.com/get-started/

## Helpful Info

* https://echohack.medium.com/patterns-with-python-poll-an-api-832173a03e93
* https://stackoverflow.com/questions/2083987/how-to-retry-after-exception

## Code Photos

* [Dockerfile](readme_images/Dockerfile.png)
* [docker-compose.yml](readme_images/docker-compose.png)
* [main.py](readme_images/main_py.png)
* [config.py](readme_images/config_python.png)
* [qr_dode dunder init](readme_images/qr_creation_code.png) <-must make folder called "qrcodegenerator" and put the code
  in the __
  init__.py

## Command Reference - No Particular Order

* docker build -t kaw393939/python312 . <- builds image called "kaw393939/python312"
* docker run -it kaw393939/python312   <- Runs python type exit() to get out
* docker run -it kaw393939/python312 <- Runs the default main.py CMD in the dockerfile
* docker run -it kaw393939/python312 app.py  <-overrides cmd/command in dockerfile to run app.py instead
* docker compose up --build < runs the service defined through the docker-compose.yml file that tells it to build the
  Dockerfile
* docker compose up <- Runs the program but doesn't build a new image
* docker run --volume /Users/keithwilliams/Desktop/fall2022/qrprog/qr_generator_service/images:/home/myuser/images
  Note:  You need to build each time you change your dockerfile
* docker exec -it <container ID> bash allows you to login to the running container
* docker tag local-image:tagname new-repo:tagname <renames the image
* docker push new-repo:tagname <pushes the image to docker hub
* docker login <- login to dockerhub if it says access denied when you try to push
curl -X POST https://reqbin.com/echo/post/form
   -H "Content-Type: application/x-www-form-urlencoded" 
   -d "param1=value1&param2=value2"


curl -X POST http://flask:8080 -H "Content-Type: application/x-www-form-urlencoded" -d "qrurl=http://wwww.yahoo.com" --output 