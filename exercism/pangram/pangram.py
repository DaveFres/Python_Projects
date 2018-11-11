def is_pangram(sentence):
    sentence = sentence.lower()
    for i in list(map(chr, range(ord('a'), ord('z')+1))):
        if sentence.count("{}".format(i)) < 1:
            return False

    return True

