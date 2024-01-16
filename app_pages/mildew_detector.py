import streamlit as st
from PIL import Image
import numpy as np
import pandas as pd
from src.data_management import download_dataframe_as_csv
from src.machine_learning.predictive_analysis import (
    load_model_and_predict,
    resize_input_image,
    plot_predictions_probabilities
)


def page_mildew_detector_body():
    """
    Page to upload and analyze leaf samples for mildew detection.

    Users can upload multiple leaf images, and the system will analyze and
    predict whether each leaf
    has mildew infection or not. The predictions are displayed along with a
    certainty percentage.

    Returns:
    None
    """
    st.image("/workspace/cherry-leaves-mildew-detector-project-5/app_pages/images/mildew.jpg", use_column_width=True)
    
    images_buffer = st.file_uploader('Upload leaf samples. '
                                     'You may select more than one.',
                                     type=['jpg', 'png'],
                                     accept_multiple_files=True)

    df_reports = []

    if images_buffer is not None:
        for image in images_buffer:
            img_pil = Image.open(image)
            st.info(f"Leaf Sample: **{image.name}**")
            img_array = np.array(img_pil)
            st.image(
                img_pil,
                caption=(
                    f"Image Size: {img_array.shape[1]}px width "
                    f"x {img_array.shape[0]}px height"
                )
            )

            resized_img = resize_input_image(img=img_pil, version='v1')
            pred_proba, pred_class = load_model_and_predict(resized_img,
                                                            version='v1')

            if float(pred_proba) < 0.9:
                st.warning("## Uncertain Images, cannot determine object")
            else:
                plot_predictions_probabilities(pred_proba, pred_class)

                df_report = pd.DataFrame({"Name": [image.name],
                                         'Result': [pred_class]})
                df_reports.append(df_report)

    if df_reports:
        df_report = pd.concat(df_reports, ignore_index=True)
        st.success(
            f"##### AI is **{100 * pred_proba:.2f}**% certain "
            f"it is {pred_class}."
        )

        st.table(df_report)

        st.markdown(download_dataframe_as_csv(df_report),
                    unsafe_allow_html=True)
