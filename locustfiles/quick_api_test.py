from locust import FastHttpUser, task, between

class QuickstartUser(FastHttpUser):

    @task()
    def api(self):
        self.client.get("/api/webcams/")
        self.client.get("/api/events/")
        self.client.get("/api/cms/ferries/")
        self.client.get("/api/cms/advisories/")
        self.client.get("/api/webcams/330/")
