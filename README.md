<!-- markdownlint-disable MD024 -->

# logkey

## About

`logkey` is a Python-based application that logs user input into a CSV file. Users can configure the exit key and the CSV file name via command-line arguments. By default, the exit key is `q`, and the inputs are stored in `inputs.csv`.

## How to Run?

### Without Docker

#### Clone the Repository

```sh
git clone https://github.com/imfsiddiqui/logkey
cd logkey
```

- `imfsiddiqui` is the GitHub username.
- `logkey` is the repository name.

#### Install Dependencies

Ensure Python installed, then run:

```python
pip install -r requirements.txt
```

#### Run the Application

```python
python app.py --exit-key <key> --csv-file <filename>
```

- Replace `<key>` with your desired exit key (default is `q`).
- Replace `<filename>` with your desired CSV file name (default is `inputs.csv`).

#### Example

```sh
python app.py --exit-key x --csv-file user_inputs.csv
```

This will log inputs to `user_inputs.csv` and exit when `x` is pressed.

### With Docker

Ensure Docker installed, then follow the below instructions.

#### Pull the Docker Image

Pull the prebuilt Docker image from Docker Hub:

```sh
docker pull imfsiddiqui/logkey
```

- `imfsiddiqui` is the Docker Hub username.
- `logkey` is the Docker image name.

#### Run the Application

Use the following command to run the application in a Docker container:

##### Linux

```sh
docker run -it --rm -v $(pwd)/:/app/data/ imfsiddiqui/logkey \
  python app.py --exit-key <key> --csv-file /app/data/<filename>
```

#### Windows: PowerShell

```ps1
docker run -it --rm -v ${PWD}/:/app/data/ imfsiddiqui/logkey \
  python app.py --exit-key <key> --csv-file /app/data/<filename>
```

- The `-v $(pwd)/:/app/data/` or `-v ${PWD}/:/app/data/` option mounts the current working directory from host machine to the `/app/data/` directory inside the container. This ensures that any CSV files created or updated by the application are stored persistently on host machine, even after the container stops.
- Replace `<key>` with your desired exit key (default is `q`).
- Replace `<filename>` with your desired CSV file name (default is `inputs.csv`).

#### Example

##### Linux

```sh
docker run -it --rm -v $(pwd)/:/app/data/ imfsiddiqui/logkey \
  python app.py --exit-key x --csv-file /app/data/user_inputs.csv
```

##### Windows: PowerShell

```sh
docker run -it --rm -v ${PWD}/:/app/data/ imfsiddiqui/logkey \
  python app.py --exit-key x --csv-file /app/data/user_inputs.csv
```

This will log inputs to `user_inputs.csv` in the current directory on host machine and exit when `x` is pressed.
