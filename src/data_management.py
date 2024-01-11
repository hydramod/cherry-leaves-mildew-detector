import numpy as np
import pandas as pd
import os
import base64
from datetime import datetime
import joblib


def download_dataframe_as_csv(df):
    """
    Generate a base64-encoded CSV download link for a Pandas DataFrame.

    Parameters:
    - df (pd.DataFrame): The DataFrame to be converted to CSV.

    Returns:
    str: The HTML code for a download link.
    """
    datetime_now = datetime.now().strftime("%d%b%Y_%Hh%Mmin%Ss")
    csv = df.to_csv().encode()
    b64 = base64.b64encode(csv).decode()
    href = f"""
        <a href="data:file/csv;base64,{b64}" 
           download="Report {datetime_now}.csv" 
           target="_blank">Download Report</a>
    """
    return href


def load_pkl_file(file_path):
    """
    Load a Pickle (.pkl) file using joblib.

    Parameters:
    - file_path (str): The path to the Pickle file.

    Returns:
    Any: The content of the Pickle file.
    """
    return joblib.load(filename=file_path)
