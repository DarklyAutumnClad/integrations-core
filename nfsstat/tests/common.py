# (C) Datadog, Inc. 2020-present
# All rights reserved
# Licensed under a 3-clause BSD style license (see LICENSE)
import os

from datadog_checks.dev import get_here

HERE = get_here()

COMPOSE_FILE = os.path.join(HERE, 'compose', 'docker-compose.yml')
SCRIPTS_DIR = os.path.join(HERE, 'compose', 'scripts')
NFS_DIR = os.path.join(HERE, 'compose', 'nfs-share')

E2E_ENV_VARS = {
    'NFS_DIR': NFS_DIR,
}

E2E_METADATA = {
    'start_commands': [
        'apt-get update',
        'apt-get install -o Dpkg::Options::="--force-confdef" -o Dpkg::Options::="--force-confold" -y docker.io',
        '/bin/dd-scripts/setup',
    ],
    'docker_volumes': ['/var/run/docker.sock:/var/run/docker.sock', '{}:/bin/dd-scripts'.format(SCRIPTS_DIR)],
    'docker_cap_add': ['SYS_ADMIN'],  # Required to be able to `mount` filesystems (eg using NFS).
}
