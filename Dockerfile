FROM nova:latest as base

# Set the working directory in the container
WORKDIR /usr/src/app

# Switch to the non-privileged user to run the application.
USER root

# Download dependencies as a separate step to take advantage of Docker's caching.
# Leverage a cache mount to /root/.cache/pip to speed up subsequent builds.
# Leverage a bind mount to requirements.txt to avoid having to copy them into
# into this layer.
RUN --mount=type=cache,target=/root/.cache/pip \
  --mount=type=bind,source=requirements.txt,target=bootstrap-requirements.txt \
  python -m pip install -r bootstrap-requirements.txt

# Switch to the non-privileged user to run the application.
USER appuser

# Copy the current directory contents into the container at /usr/src/app
COPY ./runner.py ./nova/model/
# Uncomment the line below to include model files in the Docker image
# and comment the `model_files/` line in the `.dockerignore` file.
COPY ./model_files ./model_files


ENTRYPOINT ["/usr/src/app/entrypoint.sh"]
