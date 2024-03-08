from locust import FastHttpUser, task, between

class staticUser(FastHttpUser):
#    wait_time = between(10, 15)

    @task()
    def static(self):
        self.client.get("/static/js/main.c462f54a.js")
#        self.client.get("/static/css/main.e088fd2e.css")
#        self.client.get("/favicon.ico")
        self.client.get("/static/media/BCSans-Bold.252ecf87ea37c93b293c.woff")
        self.client.get("/static/media/BCSans-Regular.0079ea8e42d4e81a13d2.woff")
#        self.client.get("/static/media/dbc-logo.db01b0c208d3fc8c9685639093aa724d.svg")
#        self.client.get("/static/media/BCHwyCrest1.3250c217efd2de2b79cf66242614ec2b.svg")
#        self.client.get("/static/media/BCHwyCrest.9291029e030864484ab6e32a1356dc1a.svg")
#        self.client.get("/static/media/colocated-camera.db3f3531300ceed4b5c080dc1ae007ff.svg")
#        self.client.get("/manifest.json")
#        self.client.get("/django-media/original_images/lytton.jpg")
#        self.client.get("/django-media/original_images/barnstonisland.jpg")



