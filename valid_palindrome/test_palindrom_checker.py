from palindrome_checker import palin_maker


def test_palin_maker():

    answerKey = {"high": True, "Cupcake": False, "banana": True, "Hannah": True, 'radkar': True}

    for key in answerKey.keys():
        assert palin_maker(key)[0] == answerKey[key]

