from avg_word_length import average_length


def test_average_length():
    assert average_length("Hi") == 2
    assert average_length("Onomatopoeia!!!!!!!!!!!!!!!") == 12
    assert average_length("I am") == 1.5

