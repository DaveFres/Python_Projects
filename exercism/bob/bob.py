def hey(phrase):

    phrase = phrase.rstrip()

    if phrase == '':
        return 'Fine. Be that way!'

    if phrase[-1] == '?':
        if str.isupper(phrase.rstrip()):
            return 'Calm down, I know what I\'m doing!'
        return 'Sure.'

    if str.isupper(phrase):
        return 'Whoa, chill out!'

    return 'Whatever.'
