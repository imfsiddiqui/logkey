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

#### Install Dependencies

Ensure you have Python installed, then run:

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

