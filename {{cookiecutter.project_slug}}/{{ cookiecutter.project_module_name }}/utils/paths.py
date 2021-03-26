from pyhere import here
from pathlib import PosixPath
from typing import (
    Union,
    Callable,
    Iterable,
)

def make_dir_function(
    dirname: Union[str, Iterable[str]]
) -> Callable[..., PosixPath]:
    """Generate a fucntion that converts a string or iterable of strings into
    a path relative to the project directory.
    Args:
        dirname: Name of the subdirectories to extend the path of the main
            project.
            If an iterable of strings is passed as an argument, then it is
            collapsed to a single steing with anchors dependent on the
            operating system.
    Returns:
        A function that returns the path relative to a directory that can
        receive `n` number of arguments for expansion.
    """

    def dir_path(*args) -> PosixPath:
        if type(dirname) == str:
            return here(dirname, *args)
        else:
            return here(*dirname, *args)

    return dir_path

for dir_type in [
        ["data"],
        ["data", "raw"],
        ["data", "processed"],
        ["data", "interim"],
        ["data", "external"],
        ["models"],
        ["notebooks"],
        ["references"],
        ["reports"],
        ["reports", "figures"],
        ["src"]
    ]:
    dir_var = '_'.join(dir_type) + "_dir"
    exec(f"global {dir_var}; {dir_var} = make_dir_function({dir_type})")