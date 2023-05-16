from codecarbon import OfflineEmissionsTracker

class GreenAnalyticsTracker(OfflineEmissionsTracker):
    tracker = OfflineEmissionsTracker(software_name="green-analytics-python", measure_power_secs=1)

    def __init__(self, secret):
        self.secret = secret

    def start(self):
        self.tracker.start()

    def stop(self):
        data = self.tracker.stop()
        
        self.send(data)

    def send(self, data):
        # Send the data collected to the green-analytics.com dashboard

        print(data)


