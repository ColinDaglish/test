<a id="readme-top"></a>
<div style="display:flex; background-color: #f2f2f2; padding: 10px; width:100%;">
    <img src="/app/static/images/data-science-campus-logo-new.svg" width="auto" height="100" alt="Data Science Campus Logo" style="margin-right:30px;">
    <img src="/app/static/images/Flask.svg" width="auto" height="100" alt="Flask Logo"  style="margin-left: auto;">
</div>

# flask-template  <!-- omit in toc -->

> A template repository for ONS themed flask applications.

For detailed guidance on how to use this Flask template to build your own web applications, please refer to the project [wiki](https://github.com/datasciencecampus/flask-template/wiki).

## Contents <!-- omit in toc -->
- [Getting started](#getting-started)
  - [Requirements](#requirements)
  - [Installation](#installation)
- [Pre-Commit Hooks](#pre-commit-hooks)
  - [Installing Pre-commit Hooks](#installing-pre-commit-hooks)
  - [Running Pre-commit Hooks](#running-pre-commit-hooks)
- [Contributing](#contributing)
- [Licence](#licence)
- [Acknowledgements](#acknowledgements)


## Getting started

### Requirements
- [Python](https://www.python.org/) `>=3.12`
- [Git](https://git-scm.com/) (for cloning the repository)


### Installation
1) Clone the repository:
```sh
git clone https://github.com/your-username/flask-template.git
```

2) Create a virtual environment (recommended):
```sh
python -m venv env
```

3) Activate the virtual environment:
  - On Windows:
  ```sh
  env\Scripts\activate
  ```
  - On Unix or macOS:
  ```sh
  source env/bin/activate
  ```
4) Install the required packages:
``` sh
pip install -r requirements.txt
```
5) Run the flask application locally:
```sh
flask --app run app
```
The application should now be running at http://localhost:5000.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Pre-Commit Hooks
This repository uses [pre-commit](https://pre-commit.com/) hooks to maintain code quality and consistency. The pre-commit hooks are configured to run automatically during the `git commit` process, ensuring that your code meets certain standards before being committed.

### Installing Pre-commit Hooks
Before you can use the pre-commit hooks, you need to install the pre-commit package and the hook repositories. Follow these steps:

1) Make sure you have a `Python` virtual environment set up and requirements installed.
2) Install the hook repositories:

```sh
pre-commit install
```
This will install the hook repositories specified in the `.pre-commit-config.yaml` file.

### Running Pre-commit Hooks

The pre-commit hooks will run automatically when you try to create a new commit. If any of the hooks fail, the commit will be blocked, and you'll need to fix the issues before you can commit your changes.

If you want to run the hooks against all files in your repository (not just the staged files), you can use the following command:

```sh
pre-commit run --all-files
```

> [!NOTE]
> To skip commit hooks during a commit, you can use the --no-verify option with git commit. This option bypasses both the pre-commit and commit-msg hooks.
<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Contributing
Contributions to this project are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request. When contributing, please follow the code style guidelines and ensure that your changes pass the pre-commit hooks.
<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Licence
This code is released under [the MIT Licence][mit].
The documentation for this work is subject to [© Crown copyright][copyright] and is available under the terms of the [Open Government 3.0][ogl] licence.

[mit]: LICENCE
[copyright]: http://www.nationalarchives.gov.uk/information-management/re-using-public-sector-information/uk-government-licensing-framework/crown-copyright/
[ogl]: http://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/
<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Acknowledgements
- This repository was created using the [flask-template](https://github.com/datasciencecampus/flask-template) repository.
<p align="right">(<a href="#readme-top">back to top</a>)</p>

