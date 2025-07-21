"""
This script logs user input to a specified CSV file.
The user can configure the exit key and the CSV file name via command-line arguments.
By default, the exit key is 'q', and the CSV file is 'inputs.csv'.
"""

import argparse
import csv

# Set up argument parser
parser = argparse.ArgumentParser(description='Log user input to a CSV file.')
parser.add_argument(
    '--exit-key', type=str, default='q', help='Key to exit the program (default: "q").'
)
parser.add_argument(
    '--csv-file',
    type=str,
    default='inputs.csv',
    help='CSV file to store inputs (default: "inputs.csv").',
)

# Parse arguments
args = parser.parse_args()
exit_key = args.exit_key
csv_file = args.csv_file

# Inform the user about the configured exit key and CSV file
print(f'Using "{exit_key}" as the exit key and "{csv_file}" as the CSV file.')

# Main loop to capture user input
while True:
    # Prompt the user for input
    user_input = input(f'Enter a character (Press {exit_key} to exit): ')

    # Check if the user wants to exit
    if user_input == exit_key:
        print('Exiting...')
        break

    # Append the user input to the specified CSV file
    with open(csv_file, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow([user_input])

    # Confirm the input back to the user
    print(f'You entered: {user_input}')
