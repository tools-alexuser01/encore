import sys

def write_static(s):
    """ Write some text, then backspace to original position
    
    Does not work correctly if there is a newline in the string.
    """
    sys.stdout.write('\b%s%s' % (s, '\b'*len(s)))
    sys.stdout.flush()
