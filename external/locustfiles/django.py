from locust import FastHttpUser, task, events


class DriveBcUser(FastHttpUser):
    @task
    def backend(self):
        with self.client.get("/api/test/app/", catch_response=True) as response:

            try:
                # assert response.text.isdigit()
                pass
            except AssertionError as err:
                err = f"Response type does not match '{response.text}'"
                response.failure(err)
                return False, err
