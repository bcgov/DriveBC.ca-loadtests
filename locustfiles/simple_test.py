from locust import FastHttpUser, task, between

class QuickstartUser(FastHttpUser):

    def on_start(self):
        self.client.headers['User-Agent'] = "Mozilla/5.0"

    @task(1)
    def api(self):
        self.client.get("/api/webcams/")
        self.client.get("/api/events/")
        self.client.get("/api/cms/ferries/")
        self.client.get("/api/cms/advisories/")
        self.client.get("/api/webcams/330/")

    @task(2)
    def static(self):
        self.client.get("/static/js/main.3995aa4e.js")
        self.client.get("/static/css/main.cff652a0.css")
        self.client.get("/favicon.ico")
        self.client.get("/static/media/BCSans-Bold.252ecf87ea37c93b293c.woff")
        self.client.get("/static/media/BCSans-Regular.0079ea8e42d4e81a13d2.woff")
        self.client.get("/static/media/dbc-logo.db01b0c208d3fc8c9685639093aa724d.svg")
        self.client.get("/manifest.json")

    @task(3)
    def cameras(self):
        self.client.get("/webcam/api/v1/webcams/531/imageSource")
        self.client.get("/webcam/api/v1/webcams/330/imageSource")
        self.client.get("/webcam/api/v1/webcams/331/imageSource")
        self.client.get("/webcam/api/v1/webcams/332/imageSource")
        self.client.get("/webcam/api/v1/webcams/334/imageSource")
        self.client.get("/webcam/api/v1/webcams/79/imageSource")
        self.client.get("/webcam/api/v1/webcams/80/imageSource")
        self.client.get("/webcam/api/v1/webcams/81/imageSource")
        self.client.get("/webcam/api/v1/webcams/82/imageSource")
