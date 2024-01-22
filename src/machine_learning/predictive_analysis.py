import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px
from tensorflow.keras.models import load_model
from PIL import Image
from src.data_management import load_pkl_file


def plot_predictions_probabilities(pred_proba, pred_class):
    """
    Plot prediction probability results.

    Parameters:
    - pred_proba (float): The predicted probability.
    - pred_class (str): The predicted class.

    Returns:
    None
    """
    prob_per_class = pd.DataFrame(
        data=[0, 0],
        index={'healthy': 0, 'powdery_mildew': 1}.keys(),
        columns=['Probability']
    )
    prob_per_class.loc[pred_class] = float(pred_proba)
    for x in prob_per_class.index.to_list():
        if x not in pred_class:
            prob_per_class.loc[x] = 1 - float(pred_proba)
    prob_per_class = prob_per_class.round(3)

    prob_per_class['Probability'] = prob_per_class['Probability'].astype(
        'int64')

    prob_per_class['Diagnostic'] = prob_per_class.index

    fig = px.bar(
        prob_per_class,
        x='Diagnostic',
        y=prob_per_class['Probability'],
        range_y=[0, 1],
        width=600, height=300, template='seaborn'
    )
    st.plotly_chart(fig)


def resize_input_image(img, version):
    """
    Reshape image to the average image size.

    Parameters:
    - img (PIL.Image.Image): The input image.
    - version (str): The version identifier for the model.

    Returns:
    np.ndarray: The resized image as a NumPy array.
    """
    image_shape = load_pkl_file(file_path=f"outputs/{version}/image_shape.pkl")
    img_info = (
        f"Image Info:\n"
        f"  Mode: {img.mode}\n"
        f"  Size: {img.size}\n"
        f"  Format: {img.format}"
    )

    try:
        if img.mode != 'RGB':
            img = img.convert('RGB')

        img_resized = img.resize((image_shape[1], image_shape[0]))
    except Exception as e:
        print("Error resizing image:", e)
        raise e

    my_image = np.expand_dims(img_resized, axis=0) / 255

    return my_image


def load_model_and_predict(my_image, version):
    """
    Load and perform ML prediction over live images.

    Parameters:
    - my_image (np.ndarray): The input image as a NumPy array.
    - version (str): The version identifier for the model.

    Returns:
    Tuple[float, str]: The predicted probability and class.
    """
    model = load_model(f"outputs/{version}/mildew_detector_model.keras")

    pred_proba = model.predict(my_image)[0, 0]

    target_map = {v: k for k, v in {'healthy': 0, 'powdery_mildew': 1}.items()}
    pred_class = target_map[pred_proba > 0.5]
    if pred_class == target_map[0]:
        pred_proba = 1 - pred_proba

    return pred_proba, pred_class
