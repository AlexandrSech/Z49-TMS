# This is a comment
FROM ubuntu:14.04

WORKDIR /Users/johnray/Desktop/repos/repo1/Z49-TMS/docs/examples/dj_docker/
COPY *.py ./
COPY . .
MAINTAINER Alex Sech <ksmith@example.com>
RUN apt-get update && apt-get install -y python
CMD ["python", "src/main.py"]