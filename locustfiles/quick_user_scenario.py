from locust import FastHttpUser, task, between

class fullTestUser(FastHttpUser):
#    wait_time = between(10, 15)

    @task(1)
    def initalLoad(self):
        self.client.get("/static/js/main.c462f54a.js")
        self.client.get("/static/css/main.e088fd2e.css")
        self.client.get("/favicon.ico")
        self.client.get("/static/media/BCSans-Bold.252ecf87ea37c93b293c.woff")
        self.client.get("/static/media/BCSans-Regular.0079ea8e42d4e81a13d2.woff")
        self.client.get("/static/media/dbc-logo.db01b0c208d3fc8c9685639093aa724d.svg")
        self.client.get("/static/media/BCHwyCrest1.3250c217efd2de2b79cf66242614ec2b.svg")
        self.client.get("/static/media/BCHwyCrest.9291029e030864484ab6e32a1356dc1a.svg")
        self.client.get("/api/cms/advisories/")
        self.client.get("/api/webcams/")
        self.client.get("/api/cms/ferries/")
        self.client.get("/api/events/")

    @task(3)
    def cameraPage(self):
        self.client.get("/webcam/api/v1/webcams/719/imageSource")
        self.client.get("/webcam/api/v1/webcams/945/imageSource")
        self.client.get("/webcam/api/v1/webcams/720/imageSource")
        self.client.get("/webcam/api/v1/webcams/797/imageSource")
        self.client.get("/webcam/api/v1/webcams/827/imageSource")
        self.client.get("/webcam/api/v1/webcams/695/imageSource")
        self.client.get("/webcam/api/v1/webcams/826/imageSource")
        self.client.get("/webcam/api/v1/webcams/853/imageSource")
        self.client.get("/webcam/api/v1/webcams/228/imageSource")
        self.client.get("/webcam/api/v1/webcams/446/imageSource")
        self.client.get("/webcam/api/v1/webcams/904/imageSource")
        self.client.get("/webcam/api/v1/webcams/912/imageSource")
        self.client.get("/webcam/api/v1/webcams/707/imageSource")
        self.client.get("/webcam/api/v1/webcams/852/imageSource")
        self.client.get("/webcam/api/v1/webcams/278/imageSource")
        self.client.get("/webcam/api/v1/webcams/297/imageSource")
        self.client.get("/webcam/api/v1/webcams/663/imageSource")
        self.client.get("/webcam/api/v1/webcams/109/imageSource")
        self.client.get("/webcam/api/v1/webcams/739/imageSource")
        self.client.get("/webcam/api/v1/webcams/703/imageSource")

    @task(5)
    def lookAroundMap(self):
        self.client.get("/webcam/api/v1/webcams/719/imageSource")
        self.client.get("/webcam/api/v1/webcams/945/imageSource")
        self.client.get("/webcam/api/v1/webcams/720/imageSource")
        self.client.get("/webcam/api/v1/webcams/797/imageSource")
        self.client.get("/webcam/api/v1/webcams/827/imageSource")
        self.client.get("/webcam/api/v1/webcams/695/imageSource")
        self.client.get("/webcam/api/v1/webcams/826/imageSource")
        self.client.get("/webcam/api/v1/webcams/853/imageSource")
        self.client.get("/webcam/api/v1/webcams/228/imageSource")
        self.client.get("/webcam/api/v1/webcams/446/imageSource")
        self.client.get("/webcam/api/v1/webcams/904/imageSource")
        self.client.get("/webcam/api/v1/webcams/912/imageSource")
        self.client.get("/webcam/api/v1/webcams/707/imageSource")
        self.client.get("/webcam/api/v1/webcams/852/imageSource")
        self.client.get("/webcam/api/v1/webcams/278/imageSource")
        self.client.get("/webcam/api/v1/webcams/297/imageSource")
        self.client.get("/webcam/api/v1/webcams/663/imageSource")
        self.client.get("/webcam/api/v1/webcams/109/imageSource")
        self.client.get("/webcam/api/v1/webcams/739/imageSource")
        self.client.get("/webcam/api/v1/webcams/703/imageSource")
        self.client.get("/django-media/original_images/lytton.jpg")
        self.client.get("/django-media/original_images/barnstonisland.jpg")
        self.client.get("/django-media/original_images/kootenaylakeosprey.jpg")
        self.client.get("/django-media/original_images/needlescable.jpg")

    @task(2)
    def reloadApi(self):
        self.client.get("/static/js/main.c462f54a.js")
        self.client.get("/api/cms/advisories/")
        self.client.get("/api/webcams/")
        self.client.get("/api/cms/ferries/")
        self.client.get("/api/events/")
        self.client.get("/api/cms/bulletins/")

    @task(2)
    def openBulletinAdvisories(self):
        self.client.get("/django-media/images/workers-above-highway.width-500.png")
        self.client.get("/static/media/BCSans-Italic.9c3be03a06d30a6ecff0.woff")
        self.client.get("/api/cms/advisories/17/")
        self.client.get("/django-media/original_images/Shift-Into-Winter-LOGO.jpg")
