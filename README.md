<!-- markdownlint-disable MD024 MD033 MD040 -->

# logkey

<div align="center">

![logkey](https://raw.githubusercontent.com/imfsiddiqui/logkey/refs/heads/main/images/logkey.png)

</div>

## Table of Contents

- [logkey](#logkey)
  - [Table of Contents](#table-of-contents)
  - [About](#about)
  - [How to Run?](#how-to-run)
    - [Without Docker](#without-docker)
      - [Clone the Repository](#clone-the-repository)
      - [Install Dependencies](#install-dependencies)
      - [Run the Application](#run-the-application)
      - [Example](#example)
    - [With Docker](#with-docker)
      - [Pull the Docker Image](#pull-the-docker-image)
      - [Run the Application](#run-the-application-1)
        - [Linux](#linux)
      - [Windows: PowerShell](#windows-powershell)
      - [Example](#example-1)
        - [Linux](#linux-1)
        - [Windows: PowerShell](#windows-powershell-1)
  - [Development](#development)
    - [Update the `requirements.txt` File](#update-the-requirementstxt-file)
    - [Build the Docker Image](#build-the-docker-image)
    - [Test the Docker Image Locally](#test-the-docker-image-locally)
      - [Linux](#linux-2)
      - [Windows: PowerShell](#windows-powershell-2)
    - [Tag the Docker Image](#tag-the-docker-image)
    - [Push the Docker Image to Docker Hub](#push-the-docker-image-to-docker-hub)
    - [Verify the Published Image](#verify-the-published-image)
      - [Linux](#linux-3)
      - [Windows: PowerShell](#windows-powershell-3)

## About

`logkey` is a Python-based application that logs user input into a CSV file. Users can configure the exit key and the CSV file name via command-line arguments. By default, the exit key is `q`, and the inputs are stored in `inputs.csv`.

## How to Run?

### Without Docker

#### Clone the Repository

```
git clone https://github.com/imfsiddiqui/logkey
cd logkey
```

- `imfsiddiqui` is the GitHub username.
- `logkey` is the repository name.

#### Install Dependencies

Ensure Python installed, then run:

```
pip install -r requirements.txt
```

#### Run the Application

```
python app.py --exit-key <key> --csv-file <filename>
```

- Replace `<key>` with your desired exit key (default is `q`).
- Replace `<filename>` with your desired CSV file name (default is `inputs.csv`).

#### Example

```
python app.py --exit-key x --csv-file user_inputs.csv
```

This will log inputs to `user_inputs.csv` and exit when `x` is pressed.

### With Docker

Ensure Docker installed, then follow the below instructions.

> ***Note***
>
> In all the following commands:
>
> - `imfsiddiqui` is the Docker Hub username.
> - `logkey` is the Docker image name.

#### Pull the Docker Image

Pull the prebuilt Docker image from Docker Hub:

```
docker pull imfsiddiqui/logkey
```

#### Run the Application

Use the following command to run the application in a Docker container:

##### Linux

```
docker run -it --rm -v $(pwd)/:/app/data/ imfsiddiqui/logkey \
  python app.py --exit-key <key> --csv-file /app/data/<filename>
```

#### Windows: PowerShell

```
docker run -it --rm -v ${PWD}/:/app/data/ imfsiddiqui/logkey `
  python app.py --exit-key <key> --csv-file /app/data/<filename>
```

- The `-v $(pwd)/:/app/data/` or `-v ${PWD}/:/app/data/` option mounts the current working directory from host machine to the `/app/data/` directory inside the container. This ensures that any CSV files created or updated by the application are stored persistently on host machine, even after the container stops.
- Replace `<key>` with your desired exit key (default is `q`).
- Replace `<filename>` with your desired CSV file name (default is `inputs.csv`).

#### Example

##### Linux

```
docker run -it --rm -v $(pwd)/:/app/data/ imfsiddiqui/logkey \
  python app.py --exit-key x --csv-file /app/data/user_inputs.csv
```

##### Windows: PowerShell

```
docker run -it --rm -v ${PWD}/:/app/data/ imfsiddiqui/logkey `
  python app.py --exit-key x --csv-file /app/data/user_inputs.csv
```

This will log inputs to `user_inputs.csv` in the current directory on host machine and exit when `x` is pressed.

## Development

If makes any changes to the Python script `app.py` or update the `requirements.txt` file, follow these steps to rebuild and publish the Docker image.

### Update the `requirements.txt` File

New dependencies or libraries can be added to the project by adding their name in the `requirements.txt` file.

### Build the Docker Image

Rebuild the Docker image to include the latest changes:

```
docker build -t logkey -f .\Dockerfile .
```

### Test the Docker Image Locally

Run the updated Docker image locally to ensure everything works as expected:

#### Linux

```
docker run -it --rm -v $(pwd)/:/app/data/ logkey \
  python app.py --exit-key x --csv-file /app/data/user_inputs.csv
```

#### Windows: PowerShell

```
docker run -it --rm -v ${PWD}/:/app/data/ logkey `
  python app.py --exit-key x --csv-file /app/data/user_inputs.csv
```

### Tag the Docker Image

Tag the Docker image with a version number or `latest`:

```
docker tag logkey:latest imfsiddiqui/logkey:<version>
```

Replace `<version>` with the appropriate version number e.g. `1.0.1` or `latest`.

### Push the Docker Image to Docker Hub

Publish the updated Docker image to Docker Hub:

```
docker push imfsiddiqui/logkey:<version>
```

`latest` tag can also be published:

```
docker push imfsiddiqui/logkey:latest
```

### Verify the Published Image

Pull the image from Docker Hub to verify it was published correctly:

```
docker pull imfsiddiqui/logkey:<version>
```

or

```
docker pull imfsiddiqui/logkey:latest
```

Run the pulled image to ensure it works as expected:

#### Linux

```
docker run -it --rm -v $(pwd)/:/app/data/ imfsiddiqui/logkey \
  python app.py --exit-key x --csv-file /app/data/user_inputs.csv
```

#### Windows: PowerShell

```
docker run -it --rm -v ${PWD}/:/app/data/ imfsiddiqui/logkey `
  python app.py --exit-key x --csv-file /app/data/user_inputs.csv
```

By these steps, this can be ensured that updates are reflected in the Docker image and published for others to use.
