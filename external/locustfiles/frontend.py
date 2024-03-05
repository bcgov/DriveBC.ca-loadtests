from locust import FastHttpUser, LoadTestShape, task, events, between

class DriveBcUser(FastHttpUser):

    @task
    def frontend(self):
        self.client.get("/")
        self.client.get("/static/js/main.c462f54a.js")
        self.client.get("/static/css/main.e088fd2e.css")
        self.client.get("/manifest.json")
        self.client.get("/favicon.ico")
        self.client.get("/api/cms/advisories/?")
        self.client.get("/static/media/BCSans-Regular.0079ea8e42d4e81a13d2.woff")
        self.client.get("/static/media/BCSans-Bold.252ecf87ea37c93b293c.woff")
        self.client.get("/api/webcams/?")
        self.client.get("/static/media/dbc-logo.db01b0c208d3fc8c9685639093aa724d.svg")

        ## DEBUG calls. Turn these on to confirm path/asset validity.

        # with self.client.get("/", catch_response=True) as response:
        #     try:
        #         assert response.status_code == 200
        #     except AssertionError as err:
        #         err = "Response type does not match"
        #         response.failure(err)
        #         return False, err

        # with self.client.get("/static/js/main.c462f54a.js", catch_response=True) as response:
        #     try:
        #         assert response.status_code == 200
        #     except AssertionError as err:
        #         err = "Response type does not match"
        #         response.failure(err)
        #         return False, err

        # with self.client.get("/static/css/main.e088fd2e.css", catch_response=True) as response:
        #     try:
        #         assert response.status_code == 200
        #     except AssertionError as err:
        #         err = "Response type does not match"
        #         response.failure(err)
        #         return False, err

        # with self.client.get("/assets/axe.min.js.f5f67518.js", catch_response=True) as response:
        #     try:
        #         assert response.status_code == 200
        #     except AssertionError as err:
        #         err = "Response type does not match"
        #         response.failure(err)
        #         return False, err

        # with self.client.get("/assets/content.js.4b3e743a.js", catch_response=True) as response:
        #     try:
        #         assert response.status_code == 200
        #     except AssertionError as err:
        #         err = "Response type does not match"
        #         response.failure(err)
        #         return False, err

        # with self.client.get("/assets/SelectorHelper.js.839362d1.js", catch_response=True) as response:
        #     try:
        #         assert response.status_code == 200
        #     except AssertionError as err:
        #         err = "Response type does not match"
        #         response.failure(err)
        #         return False, err

        # with self.client.get("/assets/issueTemplate.d5db62cd.js", catch_response=True) as response:
        #     try:
        #         assert response.status_code == 200
        #     except AssertionError as err:
        #         err = "Response type does not match"
        #         response.failure(err)
        #         return False, err

        # with self.client.get("/assets/messages.31e9ecf6.js", catch_response=True) as response:
        #     try:
        #         assert response.status_code == 200
        #     except AssertionError as err:
        #         err = "Response type does not match"
        #         response.failure(err)
        #         return False, err

        # with self.client.get("/assets/helper.8643157e.js", catch_response=True) as response:
        #     try:
        #         assert response.status_code == 200
        #     except AssertionError as err:
        #         err = "Response type does not match"
        #         response.failure(err)
        #         return False, err

        # with self.client.get("/assets/ATRules.67f6a2fa.js", catch_response=True) as response:
        #     try:
        #         assert response.status_code == 200
        #     except AssertionError as err:
        #         err = "Response type does not match"
        #         response.failure(err)
        #         return False, err

        # with self.client.get("/assets/settings.a4a1891b.js", catch_response=True) as response:
        #     try:
        #         assert response.status_code == 200
        #     except AssertionError as err:
        #         err = "Response type does not match"
        #         response.failure(err)
        #         return False, err

        # with self.client.get("/assets/v4.08a953c1.js", catch_response=True) as response:
        #     try:
        #         assert response.status_code == 200
        #     except AssertionError as err:
        #         err = "Response type does not match"
        #         response.failure(err)
        #         return False, err

        # with self.client.get("/assets/_commonjsHelpers.712cc82f.js", catch_response=True) as response:
        #     try:
        #         assert response.status_code == 200
        #     except AssertionError as err:
        #         err = "Response type does not match"
        #         response.failure(err)
        #         return False, err

        # with self.client.get("/src/runtime/injectGlobal.js", catch_response=True) as response:
        #     try:
        #         assert response.status_code == 200
        #     except AssertionError as err:
        #         err = "Response type does not match"
        #         response.failure(err)
        #         return False, err

        # with self.client.get("/manifest.json", catch_response=True) as response:
        #     try:
        #         assert response.status_code == 200
        #     except AssertionError as err:
        #         err = "Response type does not match"
        #         response.failure(err)
        #         return False, err

        # with self.client.get("/favicon.ico", catch_response=True) as response:
        #     try:
        #         assert response.status_code == 200
        #     except AssertionError as err:
        #         err = "Response type does not match"
        #         response.failure(err)
        #         return False, err

        # with self.client.get("/api/cms/advisories/?", catch_response=True) as response:
        #     try:
        #         assert response.status_code == 200
        #     except AssertionError as err:
        #         err = "Response type does not match"
        #         response.failure(err)
        #         return False, err

        # with self.client.get("/static/media/BCSans-Regular.0079ea8e42d4e81a13d2.woff", catch_response=True) as response:
        #     try:
        #         assert response.status_code == 200
        #     except AssertionError as err:
        #         err = "Response type does not match"
        #         response.failure(err)
        #         return False, err

        # with self.client.get("/static/media/BCSans-Bold.252ecf87ea37c93b293c.woff", catch_response=True) as response:
        #     try:
        #         assert response.status_code == 200
        #     except AssertionError as err:
        #         err = "Response type does not match"
        #         response.failure(err)
        #         return False, err

        # with self.client.get("/api/webcams/?", catch_response=True) as response:
        #     try:
        #         assert response.status_code == 200
        #     except AssertionError as err:
        #         err = "Response type does not match"
        #         response.failure(err)
        #         return False, err

        # with self.client.get("/static/media/dbc-logo.db01b0c208d3fc8c9685639093aa724d.svg", catch_response=True) as response:
        #     try:
        #         assert response.status_code == 200
        #     except AssertionError as err:
        #         err = "Response type does not match"
        #         response.failure(err)
        #         return False, err

# class StagesShape(LoadTestShape):
#     """
#     A shape class that has different user and spawn_rate at different stages.

#     Keyword arguments:

#         stages -- A list of dicts, each representing a stage with the following keys:
#             duration -- When this many seconds pass the test is advanced to the next stage
#             users -- Total user count
#             spawn_rate -- Number of users to start/stop per second
#             stop -- A boolean that can stop that test at a specific stage

#         stop_at_end -- Can be set to stop once all stages have run.
#     """

#     stages = [
#         {"duration": 60, "users": 100, "spawn_rate": 10},
#         {"duration": 180, "users": 1000, "spawn_rate": 10},
#     ]

#     def tick(self):
#         run_time = self.get_run_time()

#         for stage in self.stages:
#             if run_time < stage["duration"]:
#                 tick_data = (stage["users"], stage["spawn_rate"])
#                 return tick_data

#         return None
