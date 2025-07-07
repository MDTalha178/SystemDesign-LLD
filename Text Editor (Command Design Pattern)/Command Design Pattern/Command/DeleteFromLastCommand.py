from Command.Command import Command
from Editor.TextEditor import TextEditor


class DeleteFromLastCommand(Command):

    def __init__(self, editor:TextEditor, length):
        self.text_editor =editor
        self.length = length
        self.deleted_text = []

    def execute(self):
        self.deleted_text.append(self.text_editor.text[-self.length:])
        self.text_editor.delete(self.length)

    def undo(self):
        if self.deleted_text:
            self.text_editor.type(self.deleted_text.pop())