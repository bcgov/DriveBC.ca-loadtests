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
        self.client.get("/api/webcams/1065/")
        self.client.get("/api/webcams/1065/replayTheDay/")
        self.client.get("/api/weather/current/")
        self.client.get("/api/weather/regional/")
        self.client.get("/api/weather/hef/")
        self.client.get("/api/reststops/")
        self.client.get("/api/bordercrossings/")
        self.client.get("/api/wildfires/")
        self.client.get("/api/dms/")
