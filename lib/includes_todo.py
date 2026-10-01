
def includes_todo(notes):
    if "#TODO" in notes.upper():
        return True
    else:
        return False