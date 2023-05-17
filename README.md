# Introduce
It's a docker image for `Continuous Deployment`. It will help you execute `CI/CD` scripts anywhere.

# Status
Pause（SSH key in environment variable may causing security problem)

# Usage

* directly
  ```bash
  docker run --rm -it ghcr.io/docker-users/ansible-runner 
  ```

* base image
  ```
  FROM ghcr.io/docker-users/ansible-runner 
  RUN ...
  ```