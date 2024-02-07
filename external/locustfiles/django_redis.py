from locust import FastHttpUser, task, events


class DriveBcUser(FastHttpUser):
    @task
    def backend(self):
        with self.client.get("/api/test/appcache/", catch_response=True) as response:

            try:
                assert response.text.isdigit()
            except AssertionError as err:
                err = "Response type does not match"
                response.failure(err)
                return False, err
