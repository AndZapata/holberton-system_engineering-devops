# 0x1A-application_server

## Project from Holberton School


Manage puppet for debbuging

| task | description |
| --- | --- |
| 0. Set up development with Python | Configure the file web_flask/0-hello_route.py to serve its content from the route /airbnb-onepage/ on port 5000 |
| 1. Set up production with Gunicorn | ou will serve the same content from the same route as in the previous task. You can verify that it’s working by binding a Gunicorn instance to localhost listening on port 5000 with your application object as the entry point |
| 2. Serve a page with Nginx | Building on your work in the previous tasks, configure Nginx to serve your page from the route /airbnb-onepage/ |
| 3. Add a route with query parameters | Nginx should proxy requests to the route /airbnb-dynamic/number_odd_or_even/(any integer) the process listening on port 5001 |
| 4. Let's do this for your API | Setup Nginx so that the route /api/ points to a Gunicorn instance listening on port 5002 |
| 5. Serve your AirBnB clone | Gunicorn instance should serve content from web_dynamic/2-hbnb.py on port 5003 |

