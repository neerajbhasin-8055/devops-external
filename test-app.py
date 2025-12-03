import app

def test_add():
    result = app.add(2, 3)
    print(f"The result of 2 + 3 is: {result}") 
    assert result == 5
