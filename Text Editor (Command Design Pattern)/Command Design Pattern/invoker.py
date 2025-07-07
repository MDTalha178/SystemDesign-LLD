from Command.CommandManager import CommandManager
from Command.DeleteFromLastCommand import DeleteFromLastCommand
from Command.TypeCommand import TypeCommand
from Editor.TextEditor import TextEditor

text_editor = TextEditor()


command_obj = CommandManager(text_editor)

command_obj.execute_command(TypeCommand(text_editor, 'Hello'))
command_obj.execute_command(TypeCommand(text_editor, "World"))
command_obj.execute_command(TypeCommand(text_editor, "Python"))

print(command_obj.textEditor.text)

command_obj.execute_command(DeleteFromLastCommand(text_editor, 6))

print(command_obj.textEditor.text)

command_obj.undo()

print(command_obj.textEditor.text)
