from Command.Command import Command
from Editor.TextEditor import TextEditor


class CommandManager:

    def __init__(self, editor:TextEditor):
        self.textEditor = editor
        self.history = []

    def execute_command(self, command:Command):
        command.execute()
        self.history.append(command)

    def undo(self):
        last_command:Command = self.history.pop()
        last_command.undo()