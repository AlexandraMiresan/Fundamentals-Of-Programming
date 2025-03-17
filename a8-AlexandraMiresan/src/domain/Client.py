class Client:
    def __init__(self, client_id:int, name:str):
        self._client_id = client_id
        self._name = name

    def __str__(self):
        return "The client's name is " + self._name + " with id: " + str(self._client_id)

    @property
    def client_id(self):
        return self._client_id

    @property
    def name(self):
        return self._name


    def set_name(self, name):
        self._name = name
