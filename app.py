import csv
import argparse


def append_to_csv(filename, exit_key):
    print(f"Enter text to append to '{filename}'. Type '{exit_key}' to quit.")
    with open(filename, mode="a", newline="") as file:
        writer = csv.writer(file)
        while True:
            user_input = input("Input: ")
            if user_input.lower() == exit_key.lower():
                print("Exiting input loop.")
                break
            writer.writerow([user_input])
            print(f"Appended: {user_input}")


def main():
    parser = argparse.ArgumentParser(
        description="Append keyboard input to CSV until exit key is pressed."
    )
    parser.add_argument(
        "--exit-key", type=str, default="q", help="Key to exit input loop (default: q)"
    )
    parser.add_argument(
        "--file",
        type=str,
        default="output.csv",
        help="CSV file name (default: output.csv)",
    )
    args = parser.parse_args()

    append_to_csv(args.file, args.exit_key)


if __name__ == "__main__":
    main()
