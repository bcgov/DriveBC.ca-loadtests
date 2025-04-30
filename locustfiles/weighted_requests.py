import json
import random
import os
from locust import HttpUser, task, between

# 1. Load your URL hit data from JSON on disk
data_path = os.path.join(os.path.dirname(__file__), "..", "data", "weighted_requests.json")
try:
    with open(data_path, "r") as f:
        url_hit_data = json.load(f)
except Exception as e:
    raise RuntimeError(f"Failed to load URL data from {data_path}: {e}")

# 2. Filter and extract
url_hit_data = [item for item in url_hit_data if item.get("count", 0) > 0]
target_urls = [item["url"] for item in url_hit_data]
hit_counts  = [item["count"] for item in url_hit_data]

if not target_urls:
    raise RuntimeError("No valid URLs found in weighted_requests.json")

# 3. Create Locust User Class
class WebsiteUser(HttpUser):
    """
    User class that simulates requests to URLs based on weighted probabilities
    derived from historical hit counts.
    """
    # wait_time defines the pause time between executing tasks (e.g., 1 to 3 seconds)
    wait_time = between(1, 3)

    # host = "http://your-target-website.com" # Optional: Set default host

    def on_start(self):
        """ Optional: Code to run when a User starts """
        if not target_urls:
            print(f"User {self.environment.runner.user_id if self.environment.runner else ''} stopping: No target URLs defined.")
            # Stop this user if there's no data
            self.environment.runner.quit()
        print("User started, targeting URLs based on weights.")


    # 4. Implement Weighted Task
    @task
    def hit_weighted_url(self):
        """
        Picks a URL randomly based on the weights (hit counts) and sends a GET request.
        """
        if not target_urls:
             # Should not happen if on_start check works, but defensive check
            print("Warning: No target URLs available for task execution.")
            return

        # Use random.choices to pick one URL based on the hit counts as weights.
        # random.choices returns a list (even with k=1), so get the first element [0].
        chosen_url = random.choices(target_urls, weights=hit_counts, k=1)[0]

        # Make the GET request.
        # Use 'name' to group stats by the actual URL path in the Locust UI,
        # otherwise dynamic paths might get aggregated incorrectly.
        self.client.get(chosen_url, name=chosen_url)

# How to Run:
# 1. Save the code above as a Python file (e.g., `weighted_requests.py`).
# 2. Make sure you have Locust installed (`pip install locust`).
# 3. Open your terminal or command prompt.
# 4. Run Locust:
#    locust -f weighted_requests.py --host http://your-target-website.com
#    (Replace `http://your-target-website.com` with the actual base URL of your target application)
# 5. Open your web browser to `http://localhost:8089` (or the address Locust indicates).
# 6. Enter the number of users and spawn rate, then start swarming.

# Locust's statistics table will show requests grouped by the `name` provided
# (which is the URL path in this case), and the request counts should, over time,
# reflect the proportions defined by your original `hit_counts`.