from locust import FastHttpUser, task, between

class QuickstartUser(FastHttpUser):

    @task()
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
