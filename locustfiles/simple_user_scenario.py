from locust import FastHttpUser, LoadTestShape, task, events, between


class DriveBcUser(FastHttpUser):
    wait_time = between(1, 5)

    @task
    def homepage(self): # TODO: flesh this out
        self.client.get("/")
        self.client.get("/static/js/main.82121cbc.js")
        self.client.get("/static/css/main.b733ae68.css")
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

    @task
    def webcams_page(self):
        self.client.get("/cameras")
        self.client.get("/static/js/main.c462f54a.js")
        self.client.get("/static/css/main.e088fd2e.css")
        self.client.get("/favicon.ico")
        self.client.get("/manifest.json")
        self.client.get("/static/media/dbc-logo.db01b0c208d3fc8c9685639093aa724d.svg")
        self.client.get("/static/media/BCSans-Regular.0079ea8e42d4e81a13d2.woff")
        self.client.get("/static/media/BCSans-Bold.252ecf87ea37c93b293c.woff")
        self.client.get("/static/media/BCHwyCrest.9291029e030864484ab6e32a1356dc1a.svg")
        self.client.get("/static/media/BCHwyCrest1.3250c217efd2de2b79cf66242614ec2b.svg")
        self.client.get("/static/media/colocated-camera.db3f3531300ceed4b5c080dc1ae007ff.svg")

        ## DEBUG calls. Turn these on to confirm path/asset validity.

        # with self.client.get("/cameras", catch_response=True) as response:
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

        # with self.client.get("/assets/_commonjsHelpers.712cc82f.js", catch_response=True) as response:
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

        # with self.client.get("/src/runtime/injectGlobal.js", catch_response=True) as response:
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

        # with self.client.get("/manifest.json", catch_response=True) as response:
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

        # with self.client.get("/static/media/BCHwyCrest.9291029e030864484ab6e32a1356dc1a.svg", catch_response=True) as response:
        #     try:
        #         assert response.status_code == 200
        #     except AssertionError as err:
        #         err = "Response type does not match"
        #         response.failure(err)
        #         return False, err

        # with self.client.get("/static/media/BCHwyCrest1.3250c217efd2de2b79cf66242614ec2b.svg", catch_response=True) as response:
        #     try:
        #         assert response.status_code == 200
        #     except AssertionError as err:
        #         err = "Response type does not match"
        #         response.failure(err)
        #         return False, err

        # with self.client.get("/static/media/colocated-camera.db3f3531300ceed4b5c080dc1ae007ff.svg", catch_response=True) as response:
        #     try:
        #         assert response.status_code == 200
        #     except AssertionError as err:
        #         err = "Response type does not match"
        #         response.failure(err)
        #         return False, err

    @task
    def webcam_detail_page(self):
        self.client.get("/cameras/719") # TODO: Make this pull from the cams list
        self.client.get("/static/js/main.c462f54a.js")
        self.client.get("/static/css/main.e088fd2e.css")
        self.client.get("/favicon.ico")
        self.client.get("/manifest.json")
        self.client.get("/static/media/dbc-logo.db01b0c208d3fc8c9685639093aa724d.svg")
        self.client.get("/static/media/BCSans-Regular.0079ea8e42d4e81a13d2.woff")
        self.client.get("/static/media/BCSans-Bold.252ecf87ea37c93b293c.woff")
        self.client.get("/api/webcams/?")
        self.client.get("/api/webcams/719/?") # TODO: Make this pull from the cams list
        self.client.get("/api/events/?")
        # self.client.get("/ReplayTheDay/json/719.json") # TODO: Make this pull from the cams list
        self.client.get("/static/media/BCHwyCrest.9291029e030864484ab6e32a1356dc1a.svg")
        self.client.get("/static/media/colocated-camera.db3f3531300ceed4b5c080dc1ae007ff.svg")
        self.client.get("/images/719.jpg") # TODO: Make this pull from the cams list

        ## DEBUG calls. Turn these on to confirm path/asset validity.

        # # TODO: Make this pull from the cams list
        # with self.client.get("/cameras/719", catch_response=True) as response:
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

        # with self.client.get("/favicon.ico", catch_response=True) as response:
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

        # with self.client.get("/static/media/dbc-logo.db01b0c208d3fc8c9685639093aa724d.svg", catch_response=True) as response:
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

        # # TODO: Make this pull from the cams list
        # with self.client.get("/api/webcams/719/?", catch_response=True) as response:
        #     try:
        #         assert response.status_code == 200
        #     except AssertionError as err:
        #         err = "Response type does not match"
        #         response.failure(err)
        #         return False, err

        # with self.client.get("/api/events/?", catch_response=True) as response:
        #     try:
        #         assert response.status_code == 200
        #     except AssertionError as err:
        #         err = "Response type does not match"
        #         response.failure(err)
        #         return False, err

        # # TODO: Make this pull from the cams list
        # with self.client.get("/ReplayTheDay/json/719.json", catch_response=True) as response:
        #     try:
        #         assert response.status_code == 200
        #     except AssertionError as err:
        #         err = "Response type does not match"
        #         response.failure(err)
        #         return False, err

        # with self.client.get("/static/media/BCHwyCrest.9291029e030864484ab6e32a1356dc1a.svg", catch_response=True) as response:
        #     try:
        #         assert response.status_code == 200
        #     except AssertionError as err:
        #         err = "Response type does not match"
        #         response.failure(err)
        #         return False, err

        # with self.client.get("/static/media/colocated-camera.db3f3531300ceed4b5c080dc1ae007ff.svg", catch_response=True) as response:
        #     try:
        #         assert response.status_code == 200
        #     except AssertionError as err:
        #         err = "Response type does not match"
        #         response.failure(err)
        #         return False, err

        # # TODO: Make this pull from the cams list
        # with self.client.get("/images/719.jpg", catch_response=True) as response:
        #     try:
        #         assert response.status_code == 200
        #     except AssertionError as err:
        #         err = "Response type does not match"
        #         response.failure(err)
        #         return False, err

    @task
    def events_page(self): # TODO: flesh this out with any relevant calls
        self.client.get("/delays")
        self.client.get("/static/js/main.c462f54a.js")
        self.client.get("/static/css/main.e088fd2e.css")
        self.client.get("/favicon.ico")
        self.client.get("/manifest.json")
        self.client.get("/static/media/dbc-logo.db01b0c208d3fc8c9685639093aa724d.svg")
        self.client.get("/static/media/BCSans-Bold.252ecf87ea37c93b293c.woff")
        self.client.get("/static/media/BCSans-Regular.0079ea8e42d4e81a13d2.woff")
        self.client.get("/api/cms/advisories/?")

        ## DEBUG calls. Turn these on to confirm path/asset validity.

        # with self.client.get("/delays", catch_response=True) as response:
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

        # with self.client.get("/assets/_commonjsHelpers.712cc82f.js", catch_response=True) as response:
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

        # with self.client.get("/src/runtime/injectGlobal.js", catch_response=True) as response:
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

        # with self.client.get("/manifest.json", catch_response=True) as response:
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

        # with self.client.get("/static/media/BCSans-Bold.252ecf87ea37c93b293c.woff", catch_response=True) as response:
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

        # with self.client.get("/api/cms/advisories/?", catch_response=True) as response:
        #     try:
        #         assert response.status_code == 200
        #     except AssertionError as err:
        #         err = "Response type does not match"
        #         response.failure(err)
        #         return False, err

    @task
    def advisories_page(self):
        self.client.get("/advisories")
        self.client.get("/static/js/main.852d04b2.js")
        self.client.get("/static/css/main.cff652a0.css")
        self.client.get("/favicon.ico")
        self.client.get("/manifest.json")
        self.client.get("/static/media/dbc-logo.db01b0c208d3fc8c9685639093aa724d.svg")
        self.client.get("/static/media/BCSans-Regular.0079ea8e42d4e81a13d2.woff")
        self.client.get("/static/media/BCSans-Bold.252ecf87ea37c93b293c.woff")

        ## DEBUG calls. Turn these on to confirm path/asset validity.

        # with self.client.get("/advisories", catch_response=True) as response:
        #     try:
        #         assert response.status_code == 200
        #     except AssertionError as err:
        #         err = "Response type does not match"
        #         response.failure(err)
        #         return False, err

        # with self.client.get("/static/js/main.852d04b2.js", catch_response=True) as response:
        #     try:
        #         assert response.status_code == 200
        #     except AssertionError as err:
        #         err = "Response type does not match"
        #         response.failure(err)
        #         return False, err

        # with self.client.get("/static/css/main.cff652a0.css", catch_response=True) as response:
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

        # with self.client.get("/assets/_commonjsHelpers.712cc82f.js", catch_response=True) as response:
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

        # with self.client.get("/src/runtime/injectGlobal.js", catch_response=True) as response:
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

        # with self.client.get("/manifest.json", catch_response=True) as response:
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

    @task
    def bulletins_page(self):
        self.client.get("/bulletins")
        self.client.get("/static/js/main.852d04b2.js")
        self.client.get("/static/css/main.cff652a0.css")
        self.client.get("/favicon.ico")
        self.client.get("/manifest.json")
        self.client.get("/static/media/dbc-logo.db01b0c208d3fc8c9685639093aa724d.svg")
        self.client.get("/static/media/BCSans-Regular.0079ea8e42d4e81a13d2.woff")
        self.client.get("/static/media/BCSans-Bold.252ecf87ea37c93b293c.woff")

        ## DEBUG calls. Turn these on to confirm path/asset validity.

        # with self.client.get("/bulletins", catch_response=True) as response:
        #     try:
        #         assert response.status_code == 200
        #     except AssertionError as err:
        #         err = "Response type does not match"
        #         response.failure(err)
        #         return False, err

        # with self.client.get("/static/js/main.852d04b2.js", catch_response=True) as response:
        #     try:
        #         assert response.status_code == 200
        #     except AssertionError as err:
        #         err = "Response type does not match"
        #         response.failure(err)
        #         return False, err

        # with self.client.get("/static/css/main.cff652a0.css", catch_response=True) as response:
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

        # with self.client.get("/assets/_commonjsHelpers.712cc82f.js", catch_response=True) as response:
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

        # with self.client.get("/favicon.ico", catch_response=True) as response:
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

        # with self.client.get("/static/media/dbc-logo.db01b0c208d3fc8c9685639093aa724d.svg", catch_response=True) as response:
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