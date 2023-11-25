#!/usr/bin/python3
"""Prints a text with 2 new lines after each of these characters:[ . | ? | :]

    Examples:
        >>> text_sample = "Lorem ipsum is placeholder. text commonly used in \
the graphic, print, and publishing? industries for previewing. \
layouts and visual mockups."
        >>> text_indentation(text_sample)
        Lorem ipsum is placeholder.
        <BLANKLINE>
        text commonly used in the graphic, print, and publishing?
        <BLANKLINE>
        industries for previewing.
        <BLANKLINE>
        layouts and visual mockups.
        <BLANKLINE>
    """


def text_indentation(text):
    """Prints text with 2 new lines after each of these characters:
    < . | ? | : >

    Args:
        text (string): string containing text
    Raises:
        TypeError: raised if text is not a string
    """
    if type(text) is not str:
        raise TypeError("text must be a string")
    # Break text string by delimiters <., ? and :> and store in temp_list
    temp_list = []
    final_list = []
    sub_str = ""
    for c in text:
        if c == '.' or c == '?' or c == ':':
            sub_str += c
            temp_list.append(sub_str)
            sub_str = ""
        else:
            sub_str += c
    temp_list.append(sub_str)
    # Strip begining and end whitespaces with strip and store to final_list
    for s in temp_list:
        s = s.strip()
        final_list.append(s)
    # Convert list to string with join() and store in final_str
    final_str = "".join(final_list)
    # print 2 newlines when delimiter characters are found
    for c in final_str:
        if c == '.' or c == '?' or c == ':':
            print("{}".format(c))
            print()
        else:
            print("{}".format(c), end="")


if __name__ == '__main__':
    import doctest
    doctest.testfile('./tests/5-text_indentation.txt')
