from locust import FastHttpUser, task, between

class ApiUser(FastHttpUser):
    # Uncomment wait_time if you want pacing between tasks
    # wait_time = between(10, 15)

    # Adding default headers for all requests sent by this user class
    headers = {
        "Accept-Encoding": "zstd, gzip, deflate, br"
    }

    @task
    def test_all_apis(self):
        # Existing endpoints
        self.client.get("/api/webcams/", headers=self.headers)
        self.client.get("/api/events/", headers=self.headers)
        self.client.get("/api/cms/ferries/", headers=self.headers)
        self.client.get("/api/cms/advisories/", headers=self.headers)
        self.client.get("/api/cms/bulletins/", headers=self.headers)
        self.client.get("/api/webcams/1065/", headers=self.headers)
        self.client.get("/api/webcams/1065/replayTheDay/", headers=self.headers)
        self.client.get("/api/weather/current/", headers=self.headers)
        self.client.get("/api/weather/regional/", headers=self.headers)
        self.client.get("/api/weather/hef/", headers=self.headers)
        self.client.get("/api/reststops/", headers=self.headers)
        self.client.get("/api/bordercrossings/", headers=self.headers)
        self.client.get("/api/wildfires/", headers=self.headers)
        self.client.get("/api/dms/", headers=self.headers)
