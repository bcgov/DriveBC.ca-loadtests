from locust import FastHttpUser, task, events


class DriveBcUser(FastHttpUser):
    @task
    def backend(self):
        with self.client.get("/api/test/appdb/", catch_response=True) as response:

            try:
                assert response.text.istuple()
            except AssertionError as err:
                err = "Response type does not match"
                response.failure(err)
                return False, err
