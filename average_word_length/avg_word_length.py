#!/usr/bin/env python3

def average_length(sentance):
    '''
    Returns the average word length in a given sentance

    Args: 
        sentance (str): a sentance

    Returns:
        floating point value for the average word length
    '''
    # Removing punctionation
    for p in "!?',;.":
        sentance = sentance.replace(p, '')
    return sum(len(word) for word in sentance.split())/len(sentance.split())


def main():
    # Testing
    sent1 = "Hi, my name is Jackson...I am originally from Houston."
    sent2 = "Onomatopoeia!!!!!!!!!!!!!!!"
    sent3 = "I am"
    print(average_length(sent1))
    print(average_length(sent2))
    print(average_length(sent3))

if __name__ == "__main__":
    main()