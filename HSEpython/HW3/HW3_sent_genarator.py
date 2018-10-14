import random

def words_from_files(f):
    lines = (f.read()).lower()
    words = lines.split(', ')
    for i, word in enumerate(words):
        words[i] = word.strip(',')
    return words


def noun():
    file = "nouns.tsv"
    with open(file) as f:
        nouns = words_from_files(f)
    return random.choice(nouns)


def adverb():
    file = "adverbs.tsv"
    with open(file) as f:
        adverbs = words_from_files(f)
    return random.choice(adverbs)


def intensifier(adv):
    file = "intensifiers.tsv"
    with open(file) as f:
        intensifiers = words_from_files(f)
    random_intensifier = random.choice(intensifiers)
    if random_intensifier == 'enough':
        result = adv + ' ' + random_intensifier
    else:
        result = random_intensifier + ' ' + adv
    return result


def adjective(word):
    file = "adjectives.tsv"
    with open(file) as f:
        adjectives = words_from_files(f)
    return random.choice(adjectives) + ' ' + word


def verb_of_thought(subj):
    file = "verbs_of_thought.tsv"
    with open(file) as f:
        verbs = words_from_files(f)
    return subj + ' ' + random.choice(verbs)


def verb_transitive(obj):
    file = "verbs.tsv"
    with open(file) as f:
        verbs = words_from_files(f)
    return random.choice(verbs) + ' ' + obj


def conditional_s(subj, pr):
    file = "conjunction.tsv"
    with open(file) as f:
        conjunctions = words_from_files(f)
    return random.choice(conjunctions) + ' ' + subj + 's ' + pr


def random_affirmative():
    affirmative = 'The ' + verb_of_thought(adjective(noun())) + \
               ' that ' + adjective(noun() + 's') + ' ' + verb_transitive(noun() + 's') + \
               ' ' + intensifier(adverb()) + '.'
    return affirmative


def random_question():
    question = '\nDoes the ' + adjective(noun()) + ' ' + verb_transitive(noun() + 's') + \
               ' ' + intensifier(adverb()) + '?'
    return question


def random_negation():
    negation = '\nThe ' + adjective(noun()) + ' doesn\'t ' + verb_transitive(noun() + 's') + '.'
    return negation


def random_conditional():
    conditional = '\nThe ' + adjective(noun()) + ' will only ' + verb_transitive(noun() + 's') + \
               ' ' + conditional_s(adjective(noun()), verb_transitive(noun() + 's')) + '.'
    return conditional


def random_imperative():
    imperative = '\n' + verb_transitive(noun() + 's').capitalize()  + ' ' + intensifier(adverb()) + \
                 ', do.'
    return imperative


def main():
    f = open('result.txt', 'w')
    s = random_affirmative() + random_question() + random_negation() + random_conditional() + \
        random_imperative()
    f.write(s)
    f.close()
    return 0


if __name__ == '__main__':
    main()
