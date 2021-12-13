command = input()
_command = command.split(" ")
new_command = "\", \"".join(_command)
new_command = "\"" + new_command
new_command = new_command + "\""
print(new_command)