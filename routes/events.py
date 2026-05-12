# event.py

from datetime import datetime


class Event:
    def __init__(
        self,
        event_id,
        title,
        category,
        city,
        venue,
        date,
        status="upcoming",
        latitude=None,
        longitude=None,
    ):
        self.event_id = event_id
        self.title = title
        self.category = category
        self.city = city
        self.venue = venue
        self.date = date
        self.status = status
        self.latitude = latitude
        self.longitude = longitude
        self.created_at = datetime.now()

    # =========================
    # TO DICT
    # =========================

    def to_dict(self):
        return {
            "id": self.event_id,
            "title": self.title,
            "category": self.category,
            "city": self.city,
            "venue": self.venue,
            "date": self.date,
            "status": self.status,
            "latitude": self.latitude,
            "longitude": self.longitude,
            "created_at": self.created_at.strftime(
                "%Y-%m-%d %H:%M:%S"
            ),
        }

    # =========================
    # FORMAT DATE
    # =========================

    def formatted_date(self):
        try:
            return datetime.strptime(
                self.date, "%Y-%m-%d"
            ).strftime("%B %d, %Y")
        except Exception:
            return self.date

    # =========================
    # STATUS CHECKS
    # =========================

    def is_active(self):
        return self.status.lower() == "active"

    def is_upcoming(self):
        try:
            event_date = datetime.strptime(
                self.date, "%Y-%m-%d"
            )
            return event_date > datetime.now()
        except Exception:
            return False

    # =========================
    # UPDATE EVENT
    # =========================

    def update(self, **kwargs):
        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)

    # =========================
    # DISPLAY EVENT
    # =========================

    def display(self):
        print(f"Event: {self.title}")
        print(f"Category: {self.category}")
        print(f"City: {self.city}")
        print(f"Venue: {self.venue}")
        print(f"Date: {self.formatted_date()}")
        print(f"Status: {self.status}")