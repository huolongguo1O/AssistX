import os
import random
import time
def main(code):
    '''
    save the code to a random file, and execute
    '''
    filename = '/tmp/' + ''.join(random.sample('abcdefghijklmnopqrstuvwxyz', 10))
    with open(filename, 'w') as f:
        f.write(code)
    r = os.popen("python3 "+filename)
    time.sleep(3)
    res = r.read()