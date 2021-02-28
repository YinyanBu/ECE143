def is_string_integer(item):
    '''
    takes a single string character as input and returns True or False
    if that character represents a valid integer in base 10.
    parameter item:input character
    type item: str

    '''
    assert isinstance(item,str)
    assert len(item)==1
    return item.isdigit()
