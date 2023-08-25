# Hypothesis API batch scripts

Python scripts for performing bulk operations against the Hypothesis API.

## Installation

This project uses [Pipenv](https://pipenv.pypa.io). To install dependencies,
run:

```sh
pipenv install
```

## Usage

1. Generate a developer token at https://hypothes.is/account/developer, or otherwise
   obtain a Hypothesis access token.

2. Set the `HYPOTHESIS_API_KEY` env var to the access token

   ```sh
   export HYPOTHESIS_API_KEY={YOUR_KEY}
   ```

3. Run the specific batch tool you want using `pipenv run <tool>`. See
   the `[scripts]` section of `Pipfile` for a list of available scripts.

### Bulk annotation delete

Delete all annotations on `URL` in `GROUP_ID`.

```sh
pipenv run bulk_delete URL GROUP_ID --endpoint https://hypothes.is/api
```
