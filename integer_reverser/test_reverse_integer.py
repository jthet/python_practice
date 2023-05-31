from reverse_integer import reverser


def test_reverser():
    assert reverser(12345) == "54321"
    assert reverser(-5124) == "-4215"