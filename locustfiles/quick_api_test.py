from locust import FastHttpUser, task, between

class apiUser(FastHttpUser):
#    wait_time = between(10, 15)

    @task()
    def api(self):
        self.client.get("/api/webcams/")
        self.client.get("/api/events/")
        self.client.get("/api/cms/ferries/")
        self.client.get("/api/cms/advisories/")
        self.client.get("/api/cms/bulletins/")
        self.client.get("/api/webcams/330/")
