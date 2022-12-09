from pathlib import Path
from typing import List
from typing import Union

LIB = "pyalgs"

DOIT_CONFIG = {
    "default_tasks": ["_list"],
    "action_string_formatting": "old",
}


def task_cleanup():
    return {
        "actions": ["echo 'clean'"],
        "task_dep": [
            "_cleanup_build",
            "_cleanup_dist",
            "_cleanup_eggs",
            "_cleanup_mypy",
            "_cleanup_pycache",
            "_cleanup_pytest",
        ],
    }


# TODO: depends on poetry
def task_init():
    return {
        "actions": [
            """
poetry env info
[[ -f pip.conf ]] && cp pip.conf $(poetry env info -p)
poetry run python -m pip install --upgrade pip
poetry install -v --no-interaction --extras all
pre-commit install
"""
        ],
        "verbosity": 2,
    }


def task_flake8():
    return {
        "actions": [f"poetry run flake8 --ignore=E501 {LIB}"],
        # Want this task to run every time it is called
        # "file_dep": list(Path(LIB).glob("**/*.py")),
        "task_dep": ["cleanup"],
        "verbosity": 2,
    }


def task_lint():
    return {
        "actions": [f"poetry run pylint {LIB}"],
        # Want this task to run every time it is called
        # "file_dep": list(Path(LIB).glob("**/*.py")),
        "task_dep": ["cleanup"],
        "verbosity": 2,
    }


#
# Private functions and tasks
#


def _dir_files(_dir: Union[Path, str]) -> List[Path]:
    _dir = Path(_dir)
    if _dir.exists():
        return list(_dir.glob("**/*"))
    else:
        return []


def task__list():
    return {
        "actions": ["python -m doit list"],
        "verbosity": 2,
    }


def task__cleanup_build():
    # Note: cannot use file_dep when deleting files
    return {
        "actions": ["rm -rf build"],
    }


def task__cleanup_dist():
    # Note: cannot use file_dep when deleting files
    return {
        "actions": ["rm -rf dist/*"],
    }


def task__cleanup_eggs():
    # Note: cannot use file_dep when deleting files
    return {
        "actions": ["rm -rf .eggs *.egg-info"],
    }


def task__cleanup_pycache():
    # Note: cannot use file_dep when deleting files
    return {
        "actions": [
            "find . -type d -name '__pycache__' -exec rm -rf {} +",
            "find . -type f -name '*.py[co]' -exec rm -rf {} +",
        ],
    }


def task__cleanup_pytest():
    # Note: cannot use file_dep when deleting files
    return {
        "actions": [
            "find . -type d -name '*pytest_cache*' -exec rm -rf {} +",
            "rm -rf .benchmarks .coverage coverage.xml htmlcov prof report.xml .tox",
        ],
    }


def task__cleanup_mypy():
    # Note: cannot use file_dep when deleting files
    return {
        "actions": ["find . -type d -name '.mypy_cache' -exec rm -rf {} +"],
    }
