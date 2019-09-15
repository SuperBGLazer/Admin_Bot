class Command:
    pass

    def __init__(self, command, message):
        """

        :type command: str
        :type message str
        """
        self.command = command
        self.message = message

    def check_message(self, command):
        return self.command == command


c = Command("^test", "test")
commands = {c}
commands.remove(c)
