#!python
# Copyright (c) 2000-2011 ActiveState Software Inc.
# See the file LICENSE.txt for licensing information.

# Simple Django syntax checker
# args: pathname djangoProjectPath
# returns: 0 or 1
# writes error messages to stderr
# cd to '.../lib/mozilla/extensions/django_language@ActiveState.com/pylib'
# The first {% block %} tag to appear in any of my templates displays an error: 
# "Invalid block tag: 'block'". Subsequent block tags are okay, but if I delete 
# the first one, then the error appears on the new first one.

import os, sys
from django.template import loader, Template, TemplateSyntaxError

def loadTemplate(pathname):
    f = open(pathname)
    try:
        s = f.read()
    finally:
        f.close()
    try:
        t = Template(s)
    except TemplateSyntaxError, ex:
        sys.stderr.write("TemplateSyntaxError: %s\n" % ex[0])
        return 1
    return 0

def main(argv):
    pathname, projectPath = argv[1:3]
    sys.path.insert(0, os.path.dirname(projectPath))
    sys.path.insert(0, projectPath)
    os.environ["DJANGO_SETTINGS_MODULE"] = "%s.settings" % os.path.basename(projectPath)
    return loadTemplate(pathname)
    
if __name__ == "__main__":
    sys.exit(main(sys.argv))
