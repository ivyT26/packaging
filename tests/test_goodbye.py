from greetings.goodbye import bye


def test_main():
    message = bye()
    assert message == "Bye, see you soon!"
