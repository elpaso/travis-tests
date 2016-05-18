# -*- coding: utf-8 -*-

"""
***************************************************************************
    Launches a unit test inside QGIS and exit the application.

    Arguments:

    accepts a single argument with the package name in python dotted notation,
    the program tries first to load the module and launch the `run_all`
    function of the module, if that fails it considers the last part of
    the dotted path to be the function name and the previous part to be the
    module.

    Example run:

    # Will load geoserverexplorer.test.catalogtests and run `run_all`
    GSHOSTNAME=localhost python qgis_testrunner.py \
        geoserverexplorer.test.catalogtests

    # Will load geoserverexplorer.test.catalogtests and run `run_my`
    GSHOSTNAME=localhost python qgis_testrunner.py \
        geoserverexplorer.test.catalogtests.run_my

    ---------------------
    Date                 : April 2016
    Copyright            : (C) 2016 by Alessandro Pasotti
    Email                : apasotti at boundlessgeo dot com
***************************************************************************
*                                                                         *
*   This program is free software; you can redistribute it and/or modify  *
*   it under the terms of the GNU General Public License as published by  *
*   the Free Software Foundation; either version 2 of the License, or     *
*   (at your option) any later version.                                   *
*                                                                         *
***************************************************************************
"""
from __future__ import print_function

__author__ = 'Alessandro Pasotti'
__date__ = 'May 2016'

import os
import re
import sys
import signal
import importlib
from pexpect import run
from pipes import quote

from qgis.utils import iface

def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

if iface is None:
    """
    Launch QGIS and passes itself as an init script
    """
    try:
        me = __file__
    except NameError:
        me = sys.argv[0]
    args = [
        'qgis',
        '--nologo',
        '-f',
        me,
        sys.argv[-1],
    ]
    print("QGIS Test Runner - launching QGIS ...")
    out, returncode = run("sh -c " + quote(' '.join(args)), withexitstatus=1)
    print("QGIS Test Runner - QGIS exited with returncode: %d" % returncode)
    ok = out.find('(failures=') < 0 and \
        len(re.findall(r'Ran \d+ tests in\s',
                       out, re.MULTILINE)) > 0
    if not ok:
        eprint(out)
    else:
        print(out)
    if len(out) == 0:
        print("QGIS Test Runner - [WARNING] subprocess returned no output")

    print("QGIS Test Runner - finished with exit code: %d" % (0 if ok else returncode))
    sys.exit(0 if ok else 1)

else: # We are inside QGIS!
    # Start as soon as the initializationCompleted signal is fired
    from qgis.core import QgsApplication
    from PyQt.QtCore import QDir
    from qgis.utils import iface
    from capturer import CaptureOutput

    # Add current working dir to the python path
    sys.path.append(QDir.current().path())

    def __run_test():
        """
        Run the test specified as last argument in the command line.
        """
        try:
            test_module_name = QgsApplication.instance().argv()[-1]

            print("Trying to import %s" % test_module_name)
            try:
                test_module = importlib.import_module(test_module_name)
                function_name = 'run_all'
            except ImportError, e:
                # Strip latest name
                pos = test_module_name.rfind('.')
                if pos <= 0:
                    raise e
                test_module_name, function_name = test_module_name[:pos], test_module_name[pos+1:]
                print("Trying to import %s" % test_module_name)
                test_module = importlib.import_module(test_module_name)
            getattr(test_module, function_name)()
        except Exception, e:
            eprint("QGIS Test Runner exception: %s" % e)
        app = QgsApplication.instance()
        os.kill(app.applicationPid(), signal.SIGTERM)

    iface.initializationCompleted.connect(__run_test)
