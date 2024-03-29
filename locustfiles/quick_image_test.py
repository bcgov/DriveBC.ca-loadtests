from locust import FastHttpUser, task, between

class QuickstartUser(FastHttpUser):
#    wait_time = between(10, 15)

    @task()
    def cameras(self):
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
