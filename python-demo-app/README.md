<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://cdn.autoblocks.ai/images/logos/dark.png">
    <source media="(prefers-color-scheme: light)" srcset="https://cdn.autoblocks.ai/images/logos/light.png">
    <img alt="Autoblocks Logo" width="300px" src="https://cdn.autoblocks.ai/images/logos/light.png">
  </picture>
</p>
<p align="center">
  📚
  <a href="https://docs.autoblocks.ai/">Documentation</a>
  &nbsp;
  •
  &nbsp;
  🖥️
  <a href="https://app-v2.autoblocks.ai/">Application</a>
  &nbsp;
  •
  &nbsp;
  🏠
  <a href="https://www.autoblocks.ai/">Home</a>
</p>

# Development Setup

* Install [`pyenv`](https://github.com/pyenv/pyenv)
  * Install python 3.12: `pyenv install 3.12`
* Install [`pyenv-virtualenv`](https://github.com/pyenv/pyenv-virtualenv)
* Install [`poetry`](https://python-poetry.org/docs/#installation)
* Create a virtualenv: `pyenv virtualenv 3.12 python-demo-app`
  * Activate the virtualenv: `pyenv activate python-demo-app`
* Install dependencies: `poetry install`
* Install pre-commit: `poetry run pre-commit install`

# Running the app

## Create app in Autoblocks

Create a new app of type Prompt named "Doctor GPT" in the Autoblocks platform.

## Set environment variables

You can either create a `.env` file (copy from `.env.example`) in the root of the project or set the following environment variables:

```bash
export AUTOBLOCKS_TEST_RUN_MESSAGE="Made prompt more concise"
```

```bash
export AUTOBLOCKS_V2_API_KEY=<your-api-key>
```

**Note:** You can get your Autoblocks API key from the [Autoblocks settings page](https://app-v2.autoblocks.ai/settings/api-keys).

```bash
export OPENAI_API_KEY=<your-api-key>
```

**Note:** You can get your OpenAI API key from the [OpenAI dashboard](https://platform.openai.com/api-keys).

## Create prompts

Run the following script to create the prompts:

```bash
poetry run create_prompts
```

Then generate the prompt classes:

```bash
poetry run prompts generate-v2 --output-dir python_demo_app/autoblocks_prompts
```

## Create a dataset

Run the following script to setup the dataset and test cases:

```bash
poetry run create_dataset
```

## Run the tests

```bash
poetry run run_tests
```

## Running in CI

First, fork the repository to your own GitHub account.

**Note:** After forking, you will need to enable actions on the forked repository. See [this issue](https://github.com/github/docs/issues/15761) for more information.

Then, set the following repository secrets:

1. `AUTOBLOCKS_V2_API_KEY`
2. `OPENAI_API_KEY`

**Note:** You can view how these are used in the [`.github/workflows/autoblocks_tests.yml`](.github/workflows/autoblocks_tests.yml) file.

Now you can run the workflow in the Actions tab on the GitHub UI.

## View results

Go to your application at [app-v2.autoblocks.ai](https://app-v2.autoblocks.ai) and view the results.
