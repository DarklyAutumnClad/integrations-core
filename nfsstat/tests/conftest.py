# (C) Datadog, Inc. 2020-present
# All rights reserved
# Licensed under a 3-clause BSD style license (see LICENSE)
import pytest

from datadog_checks.dev import docker_run

from . import common


@pytest.fixture(scope='session')
def dd_environment():
    instance = {"tags": ["tag1:value1"]}  # Shouldn't be empty (is this a bug?).

    with docker_run(common.COMPOSE_FILE, env_vars=common.E2E_ENV_VARS):
        yield instance, common.E2E_METADATA
