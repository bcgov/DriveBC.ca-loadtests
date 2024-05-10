from locust import FastHttpUser, task, between

class QuickstartUser(FastHttpUser):
#    wait_time = between(10, 15)

    @task()
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
