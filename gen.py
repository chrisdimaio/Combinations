from zipfile import ZipFile

import math
import os
import time
import sys
import time
import timeit

path = '.'
start = 97
end = 123
length = 8

def dump(chunks, fn0, fn1, fn2):
    f = open('{0}/{1} words from {2} to {3}.txt'.format(path, fn0, fn1, fn2), 'a')
    chunks.sort()
    for chunk in chunks:
        f.write(chunk + '\n')
    f.close()


def generate(start, end, wordLength):
    ONE_MILLION = 1000000
    DUMP_AT = 15 * ONE_MILLION
    REFRESH_RATE = 10000
    counter = 0
    numberOfChars = end - start
    numberOfCombinations = numberOfChars ** wordLength
    if numberOfCombinations > DUMP_AT:
        bufferSize = DUMP_AT
    else:
        bufferSize = numberOfCombinations
    words = [None] * bufferSize
    calcs = [start] * wordLength
    tstart = 0
    tstop = 0
    tdelta = 1
    x = 0
    while(x < numberOfCombinations):
        word = ''
        tstart = time.time()
        for y in reversed(range(0, wordLength)):
            if x % numberOfChars ** y == 0:
                calcs[y - 1] = (calcs[y - 1] + 1) % numberOfChars
            word += '{0}'.format(chr(calcs[y - 1] + start))
        if test(word):
            return word
            # sys.exit(1)
        # words[x % bufferSize] = word
        # if (x + 1) % DUMP_AT == 0:
        #     print 'Dump...'
        #     # dump(words, wordLength, start, end)
        #     tstop = time.time()
        #     tdelta = (tstop - tstart)
        #     trate = DUMP_AT / tdelta
        #     print '{0} w/ms.'.format(tdelta)
        #     sys.stdout.flush()
        if x % REFRESH_RATE == 0:
            print '.',
            sys.stdout.flush()
        x += 1
    # dump(words, wordLength, start, end)

def test(word):
    with ZipFile(path) as zf:
        try:
            zf.extractall(pwd=word)
            return True
        except Exception as e:
            # print e.message
            return False

if len(sys.argv) > 1:
    path = sys.argv[1]
    # if not os.path.isdir(path):
    #     os.mkdir(path)
if len(sys.argv) > 2:
    length = int(sys.argv[2])

print generate(start, end, length)

print 'Done!'

