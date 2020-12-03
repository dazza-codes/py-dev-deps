# Install

The following should work; the intention is to use this
package only for development dependencies.

## Package extra options

See the `pyproject.toml` file for available extras.

## Install from pypi

#### poetry

```sh
poetry add -D py-dev-deps
```

#### pip

```sh
cat >> dev-requirements.txt <<EOF
py-dev-deps
EOF

pip install -r dev-requirements.txt
```

## Install from git repository

If this library is not published to a public or private repository service, it
can be installed directly from the git repository.

### Using a git protocol

#### poetry

```sh
poetry add -D 'git+https://git@github.com/dazza-codes/py-dev-deps.git'
```

```toml
# pyproject.toml snippet

[tool.poetry.dependencies]
python = "^3.7"

[tool.poetry.dev-dependencies]
py-dev-deps = {git = "https://git@github.com/dazza-codes/py-dev-deps.git"}

## if a release version is required and any extras, try:
# py-dev-deps = {git = "https://git@github.com/dazza-codes/py-dev-deps.git", rev = "0.1", extras = ["all"]}
```

#### pip

```sh
pip install "git+https://git@github.com/dazza-codes/py-dev-deps.git"

# or use git refs
pip install "git+https://git@github.com/dazza-codes/py-dev-deps.git@master"
pip install "git+https://git@github.com/dazza-codes/py-dev-deps.git@0.1.0"
```

#### pipenv

```sh
pipenv install "git+https://git@github.com/dazza-codes/py-dev-deps.git"
```

```ini
# Pipfile snippet
[packages]
py-dev-deps = {git = "https://git@github.com/dazza-codes/py-dev-deps.git"}

# optional git refs:
# py-dev-deps = {git = "https://git@github.com/dazza-codes/py-dev-deps.git", ref = "master"}
```

#### conda

Copy this example conda environment into `environment.yaml`:

```yaml
channels:
    - conda-forge

dependencies:
    - ipython
    - pip
    - pip:
       - "--editable=git+https://github.com/dazza-codes/py-dev-deps.git"
```

To install the package, and it's dependencies, then create and activate a new
conda environment (this one is named 'tmp', but you can name it anything):

```sh
conda env create --name tmp --file environment.yaml
conda activate tmp
```
