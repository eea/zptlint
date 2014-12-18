import sys

from zope.tales.engine import Engine
from zope.pagetemplate.pagetemplate import PageTemplate

from zope.contentprovider.tales import TALESProviderExpression


def run():
    if len(sys.argv) < 2:
        print "zptlint file [files...]"
        sys.exit(1)
    else:
        registerTALESExpressionType('provider', TALESProviderExpression)
        for arg in sys.argv[1:]:
            test(arg)


def registerTALESExpressionType(name, handler):
    Engine.registerType(name, handler)


def test(file):
    raw_data = open(file, 'r').read()
    pt = PageTemplate()
    pt.write(raw_data)
    if pt._v_errors:
        print "*** Error in:", file
        for error in pt._v_errors[1:]:
            formatted = error.replace('\n', ' ')
            linepos = formatted.rfind(', at line')
            if linepos != -1:
                formatted, formatted2 = (
                    formatted[:linepos], formatted[linepos:])
            else:
                formatted2 = ''
            print '    ', formatted
            print '    ', formatted2
        print
