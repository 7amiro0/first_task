"""First task."""
def direction(facing, turn, list_turn):
    """Check passed arguments."""
    cheking(facing, turn, list_turn)
    index = list_turn.index(facing)+int(turn/45)
    return list_turn[index % 8]

def cheking(facing_get, turn, facing):
    if turn % 45 != 0:
        raise Exception("Direction is not modulo 45")
    if facing_get not in facing:
        raise Exception(f"Not corection facing: {facing_get}")

list_turn = ['N', 'NE', 'E', 'SE', 'S', 'SW', 'W', 'NW']
direction('N', 180, list_turn)
