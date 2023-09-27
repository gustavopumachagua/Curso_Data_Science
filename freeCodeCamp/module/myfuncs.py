def printMe(msg='No message was supplied'):
    """ This function prints a msg supplied by the caller
        In case no message is supplied from the caller it prints "No message was supplied" """
    print(msg)


def printList(L=[]):
    """ This function prints the list elements
        The input is a list and defult is empty list"""
    for x in L:
        print(x)