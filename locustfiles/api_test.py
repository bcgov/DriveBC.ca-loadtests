from locust import FastHttpUser, task, constant

class DriveBcUser(FastHttpUser):
    # Set the wait time between tasks (optional)
    wait_time = constant(1)

    # Cleaned list of endpoints (stripped of the host for flexibility)
    endpoints = [
        "/api/areas/?",
        "/api/bordercrossings/?",
        "/api/cms/advisories/?",
        "/api/cms/bulletins/?",
        "/api/cms/emergency-alert/?",
        "/api/events/?",
        "/api/events/DBCRCON-13053/?",
        "/api/eventspolling/?",
        "/api/eventspolling/DBCRCON-13053/?",
        "/api/ferries/?",
        "/api/ferries/coastal",
        "/api/reststops/?",
        "/api/weather/current/?",
        "/api/weather/hef/?",
        "/api/weather/regional/?",
        "/api/webcams/?",
        "/api/webcams/343/?",
        "/api/wildfires/?"
    ]

    @task
    def backend_api_suite(self):
        """Iterates through all endpoints in the list"""
        for path in self.endpoints:
            # The 'name' argument groups these in the Locust UI
            self.client.get(path, name=path)

    @task
    def debug_with_validation(self):
        """
        An alternative task that includes the error handling 
        logic from your original snippet.
        """
        for path in self.endpoints:
            with self.client.get(path, catch_response=True, name=path) as response:
                if response.status_code != 200:
                    response.failure(f"Path {path} failed with {response.status_code}")