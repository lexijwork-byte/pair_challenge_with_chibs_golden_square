from lib.includes_todo import *

def test_returns_true_if_todo_is_in_notes():
    assert includes_todo("#TODO buy milk") == True

def test_returns_false_if_todo_not_in_notes():
    assert includes_todo("drink tea") == False