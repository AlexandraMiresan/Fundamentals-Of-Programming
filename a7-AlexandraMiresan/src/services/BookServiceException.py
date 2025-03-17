class BookServiceException(Exception):
    def __init__(self, message_list):
        self._message_list = message_list

    def __str__(self):
        result = ""
        for message in self._message_list:
            result += str(message) + "\n"
        return result