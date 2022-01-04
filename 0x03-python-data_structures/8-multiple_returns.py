#!/usr/bin/python3
def multiple_returns(sentence):
    lensent = len(sentence)
    return lensent, sentence[0] if lensent > 0 else None
