# -*- coding: utf-8 -*-
# Author: michalspano
# Pascal's Triangle with graphical interface
# Time decorator

def timeit(method):
    import time

    def timed(*args, **kwargs):
        time_start = time.time()
        result = method(*args, **kwargs)
        time_end = time.time()
        print('Read elapsed: %2.5f sec' % (time_end - time_start))
        return result
    return timed
