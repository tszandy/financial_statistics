import yfinance as yf
import pandas as pd
import json
from datetime import datetime

file_path="src/resources/sp500_full_table.csv"

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


if __name__ == "__main__":
    # list_all_stocks()
    sp500_table = load_sp500_table()
    timestamp = datetime.now().strftime("%Y_%m_%d")
    
    # Load existing data from output.json if it exists
    output_file_path = f"output/output_{timestamp}.json"
    try:
        with open(output_file_path, "r") as output_file:
            output_dir = json.load(output_file)
    except FileNotFoundError:
        output_dir = {}

    for row_obj in sp500_table.iloc:
        symbol = row_obj["Symbol"]
        if symbol in output_dir:
            continue
        print(symbol)
        print(list_stock(symbol))
        stock_info = list_stock(symbol)
        # output_dir[symbol] = {"trailingPE": stock_info.get("trailingPE"),"forwardPE": stock_info.get("forwardPE")}
        output_dir[symbol] = stock_info
        with open(output_file_path, "w") as output_file:
            json.dump(output_dir, output_file, indent=4)
        print(f"Output written to {output_file_path}")
    # symbol_first_row = sp500_table.iloc[0]["Symbol"]
    # stock_info = list_stock(symbol_first_row).info
    # print(sp500_table)
    # print(sp500_table[0]["symbol"])
    # print(list_stock(symbol_first_row).info["trailingPE"])
    # print(list_stock(symbol_first_row).info["forwardPE"])