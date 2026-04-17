def make_steak(d, *other):
    '''做一份牛排'''
    print('Make a steak well done in %d ' % d + 'with the other:')
    for o in other:
        print('- ' + o)