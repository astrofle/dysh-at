# `dysh-at`
## `dysh` Acceptance Testing

A place to keep the artifacts from acceptance testing.

## Usage

### At GBO

```bash
cd /home/sandboxes/psalas/Dysh/acceptance/
source py3.9/bin/activate
cd dysh-at
pytest
```

### Outside of GBO

Install `dysh` from its main branch with dev dependencies.

Download the contents of [https://www.gb.nrao.edu/dysh/acceptance\_testing/data/](https://www.gb.nrao.edu/dysh/acceptance_testing/data/)
and put them under `/home/dysh/acceptance_testing/data/` (or change the paths in the tests).

