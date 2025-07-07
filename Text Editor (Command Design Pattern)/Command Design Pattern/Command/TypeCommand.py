from Command.Command import Command
from Editor.TextEditor import TextEditor


class TypeCommand(Command):
    textEditor:TextEditor
    text: str

    def __init__(self, textEditor:TextEditor, text):
        self.textEditor = textEditor
        self.text = text

    def execute(self):
        self.textEditor.type(self.text)

    def undo(self):
        self.textEditor.delete(len(self.text))