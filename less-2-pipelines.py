import os
import fnmatch
import bz2
import gzip
import re
import shutil

TMP_DIR = '/private/tmp'


def gen_find(filepath, top):
    for path, dirlist, filelist in os.walk(top):
        for name in fnmatch.filter(filelist, filepath):
            yield os.path.join(path, name)


def gen_open(filename):
    for name in filename:
        if name.enswith('.gz'):
            yield gzip.open(name)
        elif name.enswith('.bz2'):
            yield bz2.BZ2File(name)
        else:
            yield open(name)


def gen_cat(sources):
    for s in sources:
        for item in s:
            yield item


def gen_grep(pat, lines):
    patc = re.compile(pat)
    for line in lines:
        if patc.search(line):
            yield line


pat = r'/static/.*\.jpg'
logdir = TMP_DIR
filenames = gen_find('access-*.log', logdir)
logfiles = gen_open(filenames)
loglines = gen_cat(logfiles)
patlines = gen_grep(pat, loglines)
bytecol = (line.rsplit(None, 1)[1] for line in patlines)
bytes = (int(x) for x in bytecol if x != '-')

print('Total', sum(bytes))
shutil.rmtree(TMP_DIR)
