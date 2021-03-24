import os

from setuptools import setup, find_packages

def readme() -> str:
    """Utility function to read the README.md.

    Used for the `long_description`. It's nice, because now
    1) we have a top level README file and
    2) it's easier to type in the README file than to put a raw string in below.

    Args:
        nothing

    Returns:
        String of readed README.md file.
    """
    return open(os.path.join(os.path.dirname(__file__), 'README.md')).read()

setup(
    name='{{ cookiecutter.project_module_name }}',
    version='{{ cookiecutter.project_version }}',
    author='{{ cookiecutter.project_author_name.replace("\'", "\\\'") }}',
    author_email='{{ cookiecutter.project_author_email }}',
    description='{{ cookiecutter.project_description }}',
    python_requires='>=3',
    license='{% if cookiecutter.project_open_source_license == 'MIT' %}MIT{% elif cookiecutter.project_open_source_license == 'BSD-3-Clause' %}BSD-3{% endif %}',
    url='',
    packages=find_packages(),
    long_description=readme(),
)