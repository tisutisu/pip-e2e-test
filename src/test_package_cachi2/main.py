"""
A simple script for checking pre-installed packages provided by Cachi2
"""

import io
from dockerfile_parse import DockerfileParser


if __name__ == '__main__':
    dfp = DockerfileParser(fileobj=io.BytesIO())
    # Or we can try to request actual ContainerFile via requests
    dfp.content = (
        "FROM registry.fedoraproject.org/fedora-minimal:36\n"
        'LABEL maintainer="Red Hat"\n'
        "RUN pip3 install -r requirements.txt"
    )

    # Print parent image
    print(dfp.parent_images[0])
