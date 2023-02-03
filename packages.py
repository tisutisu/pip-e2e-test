"""
A simple script for checking pre-installed packages
with different dependencies (PyPi, HTTPS and VCS) in final image

(see osbsqe/osbs_tests/test_cachito.py::test_cachito_pip_dependencies test
in osbs-integration-tests repository)
"""


if __name__ == '__main__':
    try:
        import click  # pylint: disable=unused-import
    except ImportError:
        pass
    else:
        print("A package with PyPi dependency has been installed")

    try:
        import operator_manifest  # pylint: disable=unused-import
    except ImportError:
        pass
    else:
        print("A package with HTTPS dependency has been installed")

    try:
        import dockerfile_parse  # pylint: disable=unused-import
    except ImportError:
        pass
    else:
        print("A package with VCS dependency has been installed")
