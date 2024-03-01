from locust import FastHttpUser, task, events


class DriveBcUser(FastHttpUser):
    @task
    def backend(self):
        self.client.get("/api/test/app/")

        ## DEBUG calls. Turn these on to confirm path/asset validity.

        # with self.client.get("/api/test/app/", catch_response=True) as response:

        #     try:
        #         assert response.status_code == 200
        #     except AssertionError as err:
        #         err = "Response type does not match"
        #         response.failure(err)
        #         return False, err
