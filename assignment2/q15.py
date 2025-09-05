commands_received = {"MOVE", "TURN_LEFT", "TURN_RIGHT", "STOP"}
commands_executed = {"MOVE", "TURN_LEFT", "STOP"}

not_executed = []

for cmd in commands_received:
    if cmd not in commands_executed:
        not_executed.append(cmd)

print("Commands not executed:", not_executed)
