import streamlit as st
from src.data_management import load_pkl_file


def load_test_evaluation(version):
    """
    Load evaluation data for the test set.

    Parameters:
    - version (str): The version identifier for the model and its associated "
    "evaluation data.

    Returns:
    pd.DataFrame: Evaluation data for the test set.
    """
    return load_pkl_file(f'outputs/{version}/evaluation.pkl')
