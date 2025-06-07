---
layout: default
---

<!-- markdownlint-disable MD024 MD033 MD041 -->

<a id="top"></a>

<div align=center>

<p>
  🌍 <strong><a href="https://imfsiddiqui.github.io/logkey">Web Page</a></strong>
  |
  💻 <strong><a href="https://github.com/imfsiddiqui/logkey">Source Code</a></strong>
  |
  🚀 <strong><a href="https://github.com/imfsiddiqui/logkey/releases">Releases</a></strong>
</p>

</div>

<div align=center>

<p>
  🎁 <strong><a href="https://github.com/imfsiddiqui?tab=packages&amp;repo_name=logkey">Packages</a></strong>
  |
  🐳 <strong><a href="https://hub.docker.com/r/imfsiddiqui/logkey">Docker Hub</a></strong>
</p>

</div>

# 📝 logkey

A lightweight Python application to log user inputs into a CSV file with Docker support for easy deployment and GitHub Actions to automate key workflows.

<div align="center">
  <img
    src="https://raw.githubusercontent.com/imfsiddiqui/logkey/refs/heads/main/.github/pages/assets/images/logkey.png"
    style="border-radius: 10px"
    alt="logkey"
  />
</div>

## 📚 Table of Contents

- [📝 logkey](#-logkey)
  - [📚 Table of Contents](#-table-of-contents)
  - [📌 About](#-about)
  - [🚀 How to Run?](#-how-to-run)
    - [🐍 Without Docker](#-without-docker)
      - [📂 Clone the Repository](#-clone-the-repository)
      - [📦 Install Dependencies](#-install-dependencies)
      - [▶️ Run the Application](#️-run-the-application)
      - [💡 Example](#-example)
    - [🐳 With Docker](#-with-docker)
      - [📥 Pull the Docker Image](#-pull-the-docker-image)
      - [▶️ Run the Application](#️-run-the-application-1)
        - [🐧 Linux](#-linux)
        - [🪟 Windows: PowerShell](#-windows-powershell)
      - [💡 Example](#-example-1)
        - [🐧 Linux](#-linux-1)
        - [🪟 Windows: PowerShell](#-windows-powershell-1)
  - [🛠️ Development](#️-development)
    - [📋 Update the `requirements.txt` File](#-update-the-requirementstxt-file)
    - [🏗️ Build the Docker Image](#️-build-the-docker-image)
      - [🐧 Linux](#-linux-2)
      - [🪟 Windows: PowerShell](#-windows-powershell-2)
    - [🧪 Test the Docker Image Locally](#-test-the-docker-image-locally)
      - [🐧 Linux](#-linux-3)
      - [🪟 Windows: PowerShell](#-windows-powershell-3)
    - [🏷️ Tag the Docker Image](#️-tag-the-docker-image)
    - [📤 Push the Docker Image to Docker Hub](#-push-the-docker-image-to-docker-hub)
    - [✅ Verify the Published Image](#-verify-the-published-image)
      - [🐧 Linux](#-linux-4)
      - [🪟 Windows: PowerShell](#-windows-powershell-4)
  - [🐙 GitHub Actions](#-github-actions)
    - [🤖 `.github/workflows/pages.yml`](#-githubworkflowspagesyml)
    - [🤖 `.github/workflows/release.yml`](#-githubworkflowsreleaseyml)
    - [🤖 `.github/workflows/package.yml`](#-githubworkflowspackageyml)

<p align="right">(<a href="#top">🔝 back to top</a>)</p>

## 📌 About

`logkey` is a Python-based application that logs user input into a CSV file. Users can configure the exit key and the CSV file name via command-line arguments. By default, the exit key is `q`, and the inputs are stored in `inputs.csv`.

<p align="right">(<a href="#top">🔝 back to top</a>)</p>

## 🚀 How to Run?

### 🐍 Without Docker

#### 📂 Clone the Repository

```shell
git clone https://github.com/imfsiddiqui/logkey
cd logkey
```

- `imfsiddiqui` is the GitHub username.
- `logkey` is the repository name.

#### 📦 Install Dependencies

Ensure Python installed, then run:

```shell
pip install -r requirements.txt
```

#### ▶️ Run the Application

```shell
python app.py --exit-key <key> --csv-file <filename>
```

- Replace `<key>` with your desired exit key (default is `q`).
- Replace `<filename>` with your desired CSV file name (default is `inputs.csv`).

#### 💡 Example

```shell
python app.py --exit-key x --csv-file user_inputs.csv
```

This will log inputs to `user_inputs.csv` and exit when `x` is pressed.

### 🐳 With Docker

Ensure Docker installed, then follow the below instructions.

> ***Note***
>
> In all the following commands:
>
> - `imfsiddiqui` is the Docker Hub username.
> - `logkey` is the Docker image name.

#### 📥 Pull the Docker Image

Pull the prebuilt Docker image from Docker Hub:

```shell
docker pull imfsiddiqui/logkey
```

#### ▶️ Run the Application

Use the following command to run the application in a Docker container:

##### 🐧 Linux

```shell
docker run -it --rm -v $(pwd)/:/app/data/ imfsiddiqui/logkey \
  python app.py --exit-key <key> --csv-file /app/data/<filename>
```

##### 🪟 Windows: PowerShell

```powershell
docker run -it --rm -v ${PWD}/:/app/data/ imfsiddiqui/logkey `
  python app.py --exit-key <key> --csv-file /app/data/<filename>
```

- The `-v $(pwd)/:/app/data/` or `-v ${PWD}/:/app/data/` option mounts the current working directory from host machine to the `/app/data/` directory inside the container. This ensures that any CSV files created or updated by the application are stored persistently on host machine, even after the container stops.
- Replace `<key>` with your desired exit key (default is `q`).
- Replace `<filename>` with your desired CSV file name (default is `inputs.csv`).

#### 💡 Example

##### 🐧 Linux

```shell
docker run -it --rm -v $(pwd)/:/app/data/ imfsiddiqui/logkey \
  python app.py --exit-key x --csv-file /app/data/user_inputs.csv
```

##### 🪟 Windows: PowerShell

```powershell
docker run -it --rm -v ${PWD}/:/app/data/ imfsiddiqui/logkey `
  python app.py --exit-key x --csv-file /app/data/user_inputs.csv
```

This will log inputs to `user_inputs.csv` in the current directory on host machine and exit when `x` is pressed.

<p align="right">(<a href="#top">🔝 back to top</a>)</p>

## 🛠️ Development

If made any changes to the Python script `app.py` or update the `requirements.txt` file, follow these steps to rebuild and publish the Docker image.

### 📋 Update the `requirements.txt` File

New dependencies or libraries can be added to the project by adding their name in the `requirements.txt` file.

### 🏗️ Build the Docker Image

Rebuild the Docker image to include the latest changes:

#### 🐧 Linux

```shell
docker build -t logkey:latest -f ./Dockerfile .
```

#### 🪟 Windows: PowerShell

```powershell
docker build -t logkey:latest -f .\Dockerfile .
```

### 🧪 Test the Docker Image Locally

Run the updated Docker image locally to ensure everything works as expected:

#### 🐧 Linux

```shell
docker run -it --rm -v $(pwd)/:/app/data/ logkey:latest \
  python app.py --exit-key x --csv-file /app/data/user_inputs.csv
```

#### 🪟 Windows: PowerShell

```powershell
docker run -it --rm -v ${PWD}/:/app/data/ logkey:latest `
  python app.py --exit-key x --csv-file /app/data/user_inputs.csv
```

### 🏷️ Tag the Docker Image

Tag the Docker image with a version number or `latest`:

```shell
docker tag logkey:latest imfsiddiqui/logkey:<version>
```

Replace `<version>` with the appropriate version number e.g. `1.0.1` or `latest`.

### 📤 Push the Docker Image to Docker Hub

Publish the updated Docker image to Docker Hub:

```shell
docker push imfsiddiqui/logkey:<version>
```

`latest` tag can also be published:

```shell
docker push imfsiddiqui/logkey:latest
```

### ✅ Verify the Published Image

Pull the image from Docker Hub to verify it was published correctly:

```shell
docker pull imfsiddiqui/logkey:<version>
```

or

```shell
docker pull imfsiddiqui/logkey:latest
```

Run the pulled image to ensure it works as expected:

#### 🐧 Linux

```shell
docker run -it --rm -v $(pwd)/:/app/data/ imfsiddiqui/logkey \
  python app.py --exit-key x --csv-file /app/data/user_inputs.csv
```

#### 🪟 Windows: PowerShell

```powershell
docker run -it --rm -v ${PWD}/:/app/data/ imfsiddiqui/logkey `
  python app.py --exit-key x --csv-file /app/data/user_inputs.csv
```

By these steps, this can be ensured that updates are reflected in the Docker image and published for others to use.

<p align="right">(<a href="#top">🔝 back to top</a>)</p>

## 🐙 GitHub Actions

Following GitHub Actions are being used to automate key workflows:

### 🤖 `.github/workflows/pages.yml`

Automatically builds and deploys the documentation website using Jekyll whenever changes are pushed to the default branch `main`, a new tag starting with `v` (e.g., `v1.0.0`) is pushed, or the workflow is manually triggered.

### 🤖 `.github/workflows/release.yml`

Creates a new GitHub release when a tag starting with `v` is pushed. This automates the release process and makes new versions easily accessible to users.

### 🤖 `.github/workflows/package.yml`

Builds a Docker image and publishes it to GitHub Container Registry (`ghcr.io`) every time a new tag starting with `v` (e.g., `v1.0.0`) is pushed. This ensures the latest version of the application is always available as a container image.

<p align="right">(<a href="#top">🔝 back to top</a>)</p>
