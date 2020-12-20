


def compter_les_mots(list_of_words):

    results = {}
    all_words = ' '.join(x.lower() for x in list_of_words)
    all_words = all_words.split()

    for word in all_words:
        if word not in results:
            results[word] = all_words.count(word)

    return results


def test_compter_les_mots():
    list_of_words = [
        "Ce qu'on sait savoir qu'on le sait",
        "ce qu'on ne sait pas savoir qu'on ne le sait pas",
        "c'est savoir véritablement."
    ]

    expected = {
      'le': 2,
      'véritablement.': 1,
      "c'est": 1,
      'pas': 2,
      'savoir': 3,
      'ce': 2,
      'ne': 2,
      "qu'on": 4,
      'sait': 4
    }

    assert sorted(expected.items()) == sorted(compter_les_mots(list_of_words).items())
