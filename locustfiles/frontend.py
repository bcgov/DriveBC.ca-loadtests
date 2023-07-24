from locust import HttpUser, task, events, between


class DriveBcUsers(HttpUser):
    wait_time = between(1, 5)

    @task
    def frontend(self):
        self.client.get("/")
        self.client.get("/static/js/main.2f8c977e.js")
        self.client.get("/static/css/main.77abc6c4.css")
        self.client.get("/static/css/main.77abc6c4.css")
        self.client.get(
            "/static/media/BCSans-Regular.0079ea8e42d4e81a13d2.woff")
        self.client.get(
            "/static/media/BCID_H_rgb_pos.d9a69baa85bde64a610a.png")
        self.client.get("/manifest.json")
        self.client.get("/favicon.ico")
