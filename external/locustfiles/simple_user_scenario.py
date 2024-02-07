from locust import FastHttpUser, LoadTestShape, task, events, between


class DriveBcUser(FastHttpUser):
    wait_time = between(1, 5)

    @task
    def homepage(self):
        self.client.get("/")
        self.client.get("/static/js/main.2f8c977e.js")
        self.client.get("/static/css/main.77abc6c4.css")
        self.client.get("/static/media/BCSans-Regular.0079ea8e42d4e81a13d2.woff")
        self.client.get("/static/media/BCID_H_rgb_pos.d9a69baa85bde64a610a.png")

    @task
    def webcams_page(self):
        self.client.get("/cameras-page")

    @task
    def webcam_detail_page(self):
        self.client.get("https://images.drivebc.ca/ReplayTheDay/json/719.json")
        self.client.get("/static/media/BCID_H_rgb_pos.d9a69baa85bde64a610a.png")
        # self.client.get("https://www.arcgis.com/sharing/rest/content/items/b1624fea73bd46c681fab55be53d96ae/resources/styles/root.json")
        self.client.get("/static/media/BCHwyCrest.9291029e030864484ab6e32a1356dc1a.svg")
        self.client.get("https://images.drivebc.ca/webcam/api/v1/webcams/719/imageSource")
        # self.client.get("https://tiles.arcgis.com/tiles/ubm4tcTYICKBpist/arcgis/rest/services/BC_BASEMAP/VectorTileServer/tile/9/175/81.pbf")
        # self.client.get("https://tiles.arcgis.com/tiles/ubm4tcTYICKBpist/arcgis/rest/services/BC_BASEMAP/VectorTileServer/tile/9/175/82.pbf")
        self.client.get("/api/webcams/")
        self.client.get("/api/events/")
        # self.client.get("https://www.arcgis.com/sharing/rest/content/items/b1624fea73bd46c681fab55be53d96ae/resources/sprites/sprite-1668107067528@2x.json")
        # self.client.get("https://www.arcgis.com/sharing/rest/content/items/b1624fea73bd46c681fab55be53d96ae/resources/sprites/sprite-1668107067528@2x.png")

    @task
    def events_page(self):
        self.client.get("/events-page")