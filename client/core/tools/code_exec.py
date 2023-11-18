import random
def main(code):
    '''
    save the code to a random file, and execute
    '''
    filename = '/tmp/' + ''.join(random.sample('abcdefghijklmnopqrstuvwxyz', 10))
    with open(filename, 'w') as f:
        f.write(code)
    os.system('chmod +x ' + filename)