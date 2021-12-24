"""First task."""
def direction(facing, turn):
    """Check passed arguments."""
    try:
        list_turn = ['N', 'NE', 'E', 'SE', 'S', 'SW', 'W', 'NW']
        index = list_turn.index(facing)+int(turn/45)
        if index > 0:
            while index > 7:
                index-=8
        elif index < 0:
            while index < -8:
                index+=8
        return list_turn[index]
    except IndentationError:
        print('Invalid parameters passed')
