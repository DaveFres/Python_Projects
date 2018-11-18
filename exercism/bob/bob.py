def hey(phrase):
    if phrase == '':
        return 'Fine. Be that way!'

    try:
        if phrase.rstrip()[len(phrase.rstrip()) - 1] == '?':
            if str.isupper(phrase.rstrip()):
                return 'Calm down, I know what I\'m doing!'
            return 'Sure.'

    except IndexError:
        return 'Fine. Be that way!'

    if str.isupper(phrase):
        return 'Whoa, chill out!'

    return 'Whatever.'
