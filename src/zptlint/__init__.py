import sys

from zope.tales.engine import Engine
from zope.pagetemplate.pagetemplate import PageTemplate
from zope.contentprovider.tales import TALESProviderExpression

# Chameleon support
try:
    from five.pt.engine import Program
except Exception:
    # Nothing to do
    pass
else:
    from zope.component import getGlobalSiteManager

    getGlobalSiteManager().registerUtility(Program)


def run():
    if len(sys.argv) < 2:
        print("zptlint file [files...]")
        sys.exit(1)

    errors = False
    registerTALESExpressionType("provider", TALESProviderExpression)
    for arg in sys.argv[1:]:
        if not test(arg):
            errors = True

    if errors:
        sys.exit(1)


def registerTALESExpressionType(name, handler):
    Engine.registerType(name, handler)


def test(file):
    raw_data = open(file, "r").read()
    pt = PageTemplate()
    pt.pt_source_file = lambda: file
    pt.write(raw_data)
    if pt._v_errors:
        print("*** Error in:", file)
        for error in pt._v_errors[1:]:
            formatted = error.replace("\n", " ")
            linepos = formatted.rfind(", at line")
            if linepos != -1:
                formatted, formatted2 = (formatted[:linepos], formatted[linepos:])
            else:
                formatted2 = ""
            print("    ", formatted)
            print("    ", formatted2)
        print()
        return False
    return True
