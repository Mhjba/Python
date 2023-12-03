#!/usr/bin/python3
def multiple_returns(sentence):
    if len(sentence) == 0:
        tup = (0, None)
    else:
        tup = (len(sentence), sentence[:1])
    return(tup)
