from datetime import datetime


class IdGenerator:
    @staticmethod
    def generate_unique_id():
        return datetime.now().strftime("%Y%m%d%H%M%S")