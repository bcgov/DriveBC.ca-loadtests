from locust import FastHttpUser, LoadTestShape, task, events, between
from common.frontend_tasks import load_homepage
import random

def txt_to_list(filename):  
  text_list = []
  with open(filename) as f:
    text_list = f.read().splitlines()
  return text_list

def select_random_item(list):
  return random.choice(list)

webcams_list = txt_to_list('./data/webcam_list.txt')

class imageCacheLoader(FastHttpUser):
    global webcams_list

    @task
    def image_cache(self):
        self.client.get(f"webcam/api/v1/webcams/{select_random_item(webcams_list)}/imageDisplay")


