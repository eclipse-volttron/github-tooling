from pathlib import Path

# Resolve from the location of this file the README.md file.
readme_path = Path(__file__).resolve().parent.parent.joinpath("README.md")

preamble = """
VOLTTRON™ is an open source platform for distributed sensing and control. The platform provides services for collecting and storing data from buildings and devices and provides an environment for developing applications which interact with that data.
"""
repositories = [
# github-tooling

## volttron-core
# [![Pytests - develop](https://github.com/eclipse-volttron/volttron-core/actions/workflows/run-tests.yml/badge.svg?branch=develop)](https://github.com/eclipse-volttron/volttron-core/actions/workflows/run-tests.yml)
# [![Pytests - main](https://github.com/eclipse-volttron/volttron-core/actions/workflows/run-tests.yml/badge.svg?branch=main)](https://github.com/eclipse-volttron/volttron-core/actions/workflows/run-tests.yml)
# [![pypi version](https://img.shields.io/pypi/v/volttron.svg)](https://pypi.org/project/volttron-core/)

## volttron-testing
# [![Run Pytests](https://github.com/eclipse-volttron/volttron-testing/actions/workflows/run-tests.yml/badge.svg)](https://github.com/VOLTTRON/volttron-testing/actions/workflows/run-tests.yml)
# [![pypi version](https://img.shields.io/pypi/v/volttron-testing.svg)](https://pypi.org/project/volttron-testing/)

    'volttron-core',
    'volttron-platform-driver',
    'volttron-lib-base-driver',
    'volttron-lib-fake-driver',
    'volttron-lib-bacnet-driver',
    'volttron-lib-actuator',
    'volttron-lib-historian-base',
    'volttron-lib-sql-historian',
    'volttron-lib-historian-sqlite',
    'volttron-lib-historian-postgres',
    

## volttron-openadr-ven

## volttron-2030_5

## volttron-listener

## volttron-actuator

## volttron-web-service

## volttron-auth-service

## volttron-zmq-service

## volttron-rmq-service

]

link_pypi = '[![pypi version](https://img.shields.io/pypi/v/{repo}.svg)](https://pypi.org/project/{repo}/)'
link_pytest = '[![Run Pytests](https://github.com/eclipse-volttron/{repo}/actions/workflows/run-tests.yml/badge.svg)](https://github.com/eclipse-volttron/{repo}/actions/workflows/run-tests.yml)'

with open(readme_path, 'w') as fp:
    fp.write(preamble)
    for repo in repositories:
        fp.write(f"## {repo}\n\n")
        fp.write(link_pypi.format(repo=repo) + "\n")
        fp.write(link_pytest.format(repo=repo) + "\n")
