from locust import FastHttpUser, LoadTestShape, task, events, between
from common.frontend_tasks import load_homepage


class DriveBcUser(FastHttpUser):
    wait_time = between(1, 5)

    @task
    def homepage(self):
        load_homepage(self)

    @task
    def webcams_page(self):
        self.client.get("/cameras-page")

    # Until we get URL slugs worked out, we hit Events page instead of a webcam detail page.
    @task
    def webcam_detail_page(self):
        self.client.get("/events-page")
