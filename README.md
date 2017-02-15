# python-test-app
Test app for various container clusters

Execute commands in context of webcontainer "docker-compose run web python manage.py migrate"
Launch Python shell in web container "python manage.py shell"
Create shell in running container "sudo docker exec -i -t 85301203afa6  /bin/bash"

Create DB with "python manage.py migrate"
Load data with "python manage.py loaddata polls.json"
