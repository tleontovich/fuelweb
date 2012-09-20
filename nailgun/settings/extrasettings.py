# -*- coding: utf-8 -*-

import os

LOGFILE = "nailgun.log"

COBBLER_URL = "http://localhost/cobbler_api"
COBBLER_USER = "cobbler"
COBBLER_PASSWORD = "cobbler"
COBBLER_PROFILE = "centos-6.3-x86_64"

home = os.getenv("HOME")
PATH_TO_SSH_KEY = home and os.path.join(home, ".ssh", "id_rsa") or None
PATH_TO_BOOTSTRAP_SSH_KEY = home and \
    os.path.join(home, ".ssh", "bootstrap.rsa") or None
