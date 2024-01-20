
from greetings.hello import hello

def test_main():
    message = hello()
    assert message == "Hello my friend!"
