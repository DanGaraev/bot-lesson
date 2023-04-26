class CezarGenerator:
    def __init__(self, message):
        self.message = message

    def __generate_cezar(self):
        CezarReady = ''
        if self.message:
            message = self.message.split(' ')
            for i in message[0]:
                CezarReady = CezarReady + str(chr(ord(i) + int(message[1])))
            return CezarReady

    @property
    def cezar(self):
        return self.__generate_cezar()