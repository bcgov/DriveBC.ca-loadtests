from locust import FastHttpUser, task, between

class QuickstartUser(FastHttpUser):

    @task()
    def static(self):
        self.client.get("/static/js/main.3995aa4e.js")
        self.client.get("/static/css/main.cff652a0.css")
        self.client.get("/favicon.ico")
        self.client.get("/static/media/BCSans-Bold.252ecf87ea37c93b293c.woff")
        self.client.get("/static/media/BCSans-Regular.0079ea8e42d4e81a13d2.woff")
        self.client.get("/static/media/dbc-logo.db01b0c208d3fc8c9685639093aa724d.svg")
        self.client.get("/manifest.json")