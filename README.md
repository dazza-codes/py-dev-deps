# py-dev-deps

A project that only manages python development dependencies

The aim of this project is to provide a common denominator for python development dependencies
in one package that can be added as a development dependency to other projects.  By using
poetry to resolve and maintain a common set of compatible development dependencies, it may
help to reduce the burdens of package installations for projects using this project as a
development dependency.

## Install

See [INSTALL](INSTALL.md) for more details; the following should work; note that
the intention is to use this package only for development dependencies.

#### poetry

```sh
poetry add -D 'py-dev-deps'
```

#### pip

```sh
cat >> dev-requirements.txt <<EOF
py-dev-deps
EOF

pip install -r dev-requirements.txt
```
