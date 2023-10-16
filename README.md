# Creating with Bing Image Creator - README.md

[![License: MPL 2.0](https://img.shields.io/badge/License-MPL%202.0-brightgreen.svg)](https://opensource.org/licenses/MPL-2.0)
[![Bandit](https://github.com/genai-musings/creating-with-BingImageCreator/actions/workflows/bandit.yml/badge.svg)](https://github.com/genai-musings/creating-with-BingImageCreator/actions/new?category=security)
[![Super-Linter](https://github.com/genai-musings/creating-with-BingImageCreator/actions/workflows/linter.yml/badge.svg)](https://github.com/marketplace/actions/super-linter)
[![CodeQL](https://github.com/genai-musings/creating-with-BingImageCreator/workflows/CodeQL/badge.svg?branch=main)
[![Markdown Links Check](https://github.com/genai-musings/creating-with-BingImageCreator/actions/workflows/md-links.yml/badge.svg)](https://github.com/gaurav-nelson/github-action-markdown-link-check)
[![Spell-Checker](https://github.com/genai-musings/creating-with-BingImageCreator/actions/workflows/spellcheck.yaml/badge.svg)](https://github.com/rojopolis/spellcheck-github-actions)
[![Unit-Tests](https://github.com/genai-musings/creating-with-BingImageCreator/actions/workflows/test.yaml/badge.svg)](https://github.com/actions/setup-python)
[![Code-Coverage](https://github.com/genai-musings/creating-with-BingImageCreator/actions/workflows/coverage.yaml/badge.svg)](https://github.com/actions/setup-python)
[![Docker-Build-Push](https://github.com/genai-musings/creating-with-BingImageCreator/actions/workflows/docker-build-push.yml/badge.svg)](https://hub.docker.com/)
[![Docker-Push-README](https://github.com/genai-musings/creating-with-BingImageCreator/actions/workflows/docker-push-readme.yml/badge.svg)](https://hub.docker.com/)

## Archived

**Note:** This repository has been archived as it relies on a reverse engineered API located in the [BingImageCreator](https://github.com/acheong08/BingImageCreator) repository which has been archived by its owner.

## Repository for creating with Bing Image creator

 This repository contains Python code, and associated unit tests, for high quality image generation by[Microsoft Bing Image Creator](https://www.bing.com/create) using the reverse engineered [BingImageCreator](https://github.com/acheong08/BingImageCreator) API. The code takes the input from the user and generates a response using Bing image creator. You just need to provide a description and Bing will generate the image.

## Pre-requisites

Install BingImageCreator module

```shell
pip3 install --upgrade BingImageCreator
```

## To run program

Your Bing key is passed to program via an environment variable

```shell
export BING_KEY="Your Bing key"
python main.py
```

### To Generate a Key

To generate a key browse to the [Getting Authentication](https://github.com/acheong08/BingImageCreator#getting-authentication) details section of the [BingImageCreator README.md](https://github.com/acheong08/BingImageCreator#readme) and follow the instructions given.

### Program Options

```shell
usage: main.py [-h] [--output_dir OUTPUT_DIR]
               [--download_count DOWNLOAD_COUNT]

Script for generating and saving images using Bing Image Creator.

options:
  -h, --help            show this help message and exit
  --output_dir OUTPUT_DIR
                        Path to the output directory
  --download_count DOWNLOAD_COUNT
                        Number of images to download
```

## To run unit tests

```shell
pytest
```

## To build and run an instance of a Docker image locally.

The username and password for Docker Hub are stored as secrets this GitHub repository.

**Note:** To set up the secrets in your GitHub repository, go to the repository page, navigate to the "Settings" tab, and then select "Secrets" from the left menu. Add a secret named DOCKERHUB_USERNAME with the Docker Hub username to be used, and another secret named DOCKERHUB_PASSWORD with the Docker Hub password to be used.

### Build

Build the Docker image.

```shell
docker build -t creating-with-bingimagecreator .
```

### Run

Run the Docker image as a container.

```shell
export BING_KEY="Your Bing key"
docker run -it -e BING_KEY=$BING_KEY creating-with-bingimagecreator
```

## To pull and run an instance of the Docker image from Docker Hub

### Pull

```shell
docker pull <dockerhub-username>/creating-with-bingimagecreator:<tag>
```

Replace <dockerhub-username> with your Docker Hub username and <tag> with the specific tag of the Docker image you want to pull.

### Run

```shell
export BING_KEY="Your Bing key"
docker run -it -e BING_KEY=$BING_KEY <dockerhub-username>/creating-with-bingimagecreator:<tag>
```

## BingImageCreator API Reference

For more information on the API available see the [BingImageCreator Repository](https://github.com/acheong08/BingImageCreator).
