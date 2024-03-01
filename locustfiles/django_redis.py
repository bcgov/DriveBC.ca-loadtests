from locust import FastHttpUser, task, events


class DriveBcUser(FastHttpUser):
    @task
    def backend(self):
        self.client.get("/api/test/appcache/")

        ## DEBUG calls. Turn these on to confirm path/asset validity.

        # with self.client.get("/api/test/appcache/", catch_response=True) as response:

        #     try:
        #         assert response.status_code == 200
        #         assert response.text.isdigit()
        #     except AssertionError as err:
        #         err = "Response type or status code do not match"
        #         response.failure(err)
        #         return False, err
