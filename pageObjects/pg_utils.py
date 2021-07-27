from datetime import datetime

class date:
    def date_timestamp(self):
        now = datetime.now()
        date_now = now.strftime("%Y-%f")
        return date_now



