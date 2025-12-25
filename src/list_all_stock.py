import os
import sys
import signal
import atexit
import yfinance as yf
import pandas as pd
import json
from datetime import datetime

file_path = "src/resources/sp500_full_table.csv"

def load_sp500_table():
    """
    Loads the S&P 500 full table from a CSV file.
    """
    file_path = "src/resources/sp500_full_table.csv"
    try:
        sp500_table = pd.read_csv(file_path, delimiter='\t', quoting=1)
        return sp500_table
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
        return None

def list_stock(symbol):
    return yf.Ticker(symbol).info

def dump_output(output_dir, output_file_path):
    os.makedirs(os.path.dirname(output_file_path), exist_ok=True)
    with open(output_file_path, "w") as output_file:
        json.dump(output_dir, output_file, indent=4, default=str)

if __name__ == "__main__":
    sp500_table = load_sp500_table()
    if sp500_table is None:
        sys.exit(1)

    timestamp = datetime.now().strftime("%Y_%m_%d")
    output_file_path = f"output/output_{timestamp}.json"

    try:
        with open(output_file_path, "r") as output_file:
            output_dir = json.load(output_file)
    except FileNotFoundError:
        output_dir = {}

    # mutable state for signal handlers / atexit
    state = {"pending": 0}

    def safe_dump_and_exit(signum=None, frame=None):
        if state["pending"] > 0:
            print("Saving pending results before exit...")
            dump_output(output_dir, output_file_path)
            state["pending"] = 0
            print(f"Output written to {output_file_path}")
        sys.exit(0)

    # handle interrupts/termination
    signal.signal(signal.SIGINT, safe_dump_and_exit)
    signal.signal(signal.SIGTERM, safe_dump_and_exit)
    atexit.register(lambda: dump_output(output_dir, output_file_path) if state["pending"] > 0 else None)

    processed_since_last_dump = 0
    try:
        for _, row in sp500_table.iterrows():
            symbol = row.get("Symbol") if hasattr(row, "get") else row["Symbol"]
            if not symbol:
                continue
            if symbol in output_dir:
                continue

            print(symbol)
            stock_info = list_stock(symbol)
            output_dir[symbol] = stock_info

            processed_since_last_dump += 1
            state["pending"] = processed_since_last_dump

            if processed_since_last_dump >= 50:
                dump_output(output_dir, output_file_path)
                print(f"Output written to {output_file_path}")
                processed_since_last_dump = 0
                state["pending"] = 0

    except KeyboardInterrupt:
        # will be handled by signal handler, but keep here defensively
        safe_dump_and_exit()

    # final flush if there are remaining unsaved items
    if processed_since_last_dump > 0:
        dump_output(output_dir, output_file_path)
        print(f"Final output written to {output_file_path}")
        processed_since_last_dump = 0
        state["pending"] = 0