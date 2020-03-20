import os
import requests  # noqa We are just importing this to prove the dependency installed correctly


def main():
    my_input = os.environ["INPUT_IGNORE"]

    my_output = f"Hello {ignore}"
    assert False, "falsy"
    print(f"::set-output name=output::{output}")


if __name__ == "__main__":
    main()
