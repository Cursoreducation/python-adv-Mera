# Pull official base image.
FROM python:3.10

# set working directory
WORKDIR /app

# Set environment varibles
# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE 1
# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED 1
# Install fault handlers for the SIGSEGV, SIGFPE, SIGABRT, SIGBUS, and SIGILL signals
ENV PYTHONFAULTHANDLER 1
# Disable pip's cache files in the container
ENV PIP_NO_CACHE_DIR off
# Don’t periodically check PyPI to determine whether a new version of pip is available for download
ENV PIP_DISABLE_PIP_VERSION_CHECK on
# Keeps Poetry from automatically creates virtual environments
ENV POETRY_VIRTUALENVS_CREATE false

# Install poetry
RUN curl -sSL https://install.python-poetry.org | python3 -
ENV PATH="${PATH}:/root/.local/bin"
RUN poetry self update


# Install dependencies
COPY pyproject.toml .
COPY poetry.lock .
RUN poetry install --only main --no-interaction --no-ansi

# Copy project
COPY . .
