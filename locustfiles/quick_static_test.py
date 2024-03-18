from locust import FastHttpUser, task, between

class staticUser(FastHttpUser):
#    wait_time = between(10, 15)

    @task()
    def static(self):
        self.client.get("/static/js/main.3c3de86c.js")
        self.client.get("/static/css/main.6478c6cd.css")
        self.client.get("/favicon.ico")
        self.client.get("/static/media/BCSans-Bold.252ecf87ea37c93b293c.woff")
        self.client.get("/static/media/BCSans-Regular.0079ea8e42d4e81a13d2.woff")
        self.client.get("/static/media/dbc-logo.db01b0c208d3fc8c9685639093aa724d.svg")
        self.client.get("/static/media/BCHwyCrest1.3250c217efd2de2b79cf66242614ec2b.svg")
        self.client.get("/static/media/BCHwyCrest.9291029e030864484ab6e32a1356dc1a.svg")
        self.client.get("/static/media/colocated-camera.db3f3531300ceed4b5c080dc1ae007ff.svg")
        self.client.get("/manifest.json")
#        self.client.get("/django-media/original_images/lytton.jpg")
#        self.client.get("/django-media/original_images/barnstonisland.jpg")

#In the pod, you can always go to /usr/share/nginx/html/static and then navigate to the sub-folders to get all the static content

#Other static content:
#BCHwyCrest16.b7711d9f1ab74ccb1b65c271be0047b4.svg
#BCHwyCrest3.bb76abbbf906b24dc1b65af9816fe902.svg
#BCHwyCrest5.c1f2abb9851cd82502539b6de46a69ff.svg
#BCSans-BoldItalic.73ed5137b2c4a42b754f.woff
#BCSans-Italic.9c3be03a06d30a6ecff0.woff
#dbc-logo--white.65faa8197962aff247256fb5a076da97.svg