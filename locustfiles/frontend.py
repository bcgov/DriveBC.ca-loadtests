from locust import FastHttpUser, LoadTestShape, task, events, between


class DriveBcUser(FastHttpUser):
    # wait_time = between(1, 5)

    @task
    def frontend(self):
        self.client.get("/")
        self.client.get("/static/js/main.2f8c977e.js")
        self.client.get("/static/css/main.77abc6c4.css")
        self.client.get(
            "/static/media/BCSans-Regular.0079ea8e42d4e81a13d2.woff")
        self.client.get(
            "/static/media/BCID_H_rgb_pos.d9a69baa85bde64a610a.png")


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
