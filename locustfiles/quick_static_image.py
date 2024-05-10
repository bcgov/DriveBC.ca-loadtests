#This tries to hit the static pods and image caching pod to see how much bandwith we can use between them combined

from locust import FastHttpUser, task, between

class fullTestUser(FastHttpUser):

    @task(1)
    def static(self):
        self.client.get("/static/js/main.82121cbc.js")
        self.client.get("/static/css/main.b733ae68.css")
        self.client.get("/favicon.ico")
        self.client.get("/static/media/BCSans-Bold.252ecf87ea37c93b293c.woff")
        self.client.get("/static/media/BCSans-Regular.0079ea8e42d4e81a13d2.woff")
        self.client.get("/static/media/dbc-logo.db01b0c208d3fc8c9685639093aa724d.svg")
        self.client.get("/static/media/BCHwyCrest1.3250c217efd2de2b79cf66242614ec2b.svg")
        self.client.get("/static/media/BCHwyCrest.9291029e030864484ab6e32a1356dc1a.svg")
        self.client.get("/static/media/colocated-camera.db3f3531300ceed4b5c080dc1ae007ff.svg")
        self.client.get("/manifest.json")

    @task(5)
    def cameras(self):
        self.client.get("/images/719.jpg")
        self.client.get("/images/945.jpg")
        self.client.get("/images/720.jpg")
        self.client.get("/images/797.jpg")
        self.client.get("/images/827.jpg")
        self.client.get("/images/695.jpg")
        self.client.get("/images/826.jpg")
        self.client.get("/images/853.jpg")
        self.client.get("/images/228.jpg")
        self.client.get("/images/446.jpg")
        self.client.get("/images/904.jpg")
        self.client.get("/images/912.jpg")
        self.client.get("/images/707.jpg")
        self.client.get("/images/852.jpg")
        self.client.get("/images/278.jpg")
        self.client.get("/images/297.jpg")
        self.client.get("/images/663.jpg")
        self.client.get("/images/109.jpg")
        self.client.get("/images/739.jpg")
        self.client.get("/images/703.jpg")

