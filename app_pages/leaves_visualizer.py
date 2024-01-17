import streamlit as st
import os
import matplotlib.pyplot as plt
from matplotlib.image import imread
import itertools
import random


def page_leaves_visualizer_body(app):
    """
    Streamlit page for visualizing leaves.

    Returns:
    None
    """
    app.load_page_image("leaves.jpg")

    st.write("### Leaves Visualizer")

    st.info(
        "To observe visual differences or explore Image Montage, "
        "click the button below."
    )

    version = 'v1'

    if st.checkbox("Difference between average and variability image"):
        st.warning("In the variability difference, the darker area indicates "
                   "similarities between the images. The lighter area shows "
                   "differences.")

        avg_mildew = plt.imread(f"outputs/{version}/"
                                "avg_var_powdery_mildew.png")
        avg_healthy = plt.imread(f"outputs/{version}/avg_var_healthy.png")

        st.image(avg_mildew,
                 caption='Unhealthy Leaf - Average and Variability')
        st.image(avg_healthy,
                 caption='Healthy Leaf - Average and Variability')

        st.write("---")

    if st.checkbox("Differences between average unhealthy and average healthy "
                   "leaf"):
        diff_between_avgs = plt.imread(f"outputs/{version}/avg_diff.png")

        st.image(diff_between_avgs,
                 caption='Difference between average images')
        st.warning(
            "In the difference between averages, the darker area indicates "
            "similarities, while the lighter part shows differences."
        )

    if st.checkbox("Image Montage"):
        st.write("To refresh the montage, click on 'Create Montage' button")
        my_data_dir = 'inputs/cherry_leaves_dataset/cherry-leaves'
        labels = os.listdir(f"{my_data_dir}/validation")
        label_to_display = st.selectbox(label="Select label",
                                        options=labels, index=0)

        if st.button("Create Montage"):
            image_montage(dir_path=f"{my_data_dir}/validation",
                          label_to_display=label_to_display,
                          nrows=3, ncols=3, figsize=(10, 15))

        st.write("---")


def image_montage(dir_path, label_to_display, nrows, ncols, figsize=(15, 10)):
    """
    Create and display a montage of leaf images.

    Parameters:
    - dir_path (str): Directory path containing leaf images.
    - label_to_display (str): Label to display in the montage.
    - nrows (int): Number of rows in the montage.
    - ncols (int): Number of columns in the montage.
    - figsize (tuple): Figure size for the montage.

    Returns:
    None
    """
    labels = os.listdir(dir_path)

    if label_to_display in labels:
        images_list = os.listdir(f"{dir_path}/{label_to_display}")

        if nrows * ncols < len(images_list):
            img_idx = random.sample(images_list, nrows * ncols)

        list_rows = range(0, nrows)
        list_cols = range(0, ncols)
        plot_idx = list(itertools.product(list_rows, list_cols))

        fig, axes = plt.subplots(nrows=nrows, ncols=ncols, figsize=figsize)
        for x in range(0, nrows * ncols):
            img = imread(f"{dir_path}/{label_to_display}/{img_idx[x]}")
            img_shape = img.shape
            axes[plot_idx[x][0], plot_idx[x][1]].imshow(img)
            axes[plot_idx[x][0],
                 plot_idx[x][1]].set_title(
                     f"Width {img_shape[1]}px x Height {img_shape[0]}px")
            axes[plot_idx[x][0], plot_idx[x][1]].set_xticks([])
            axes[plot_idx[x][0], plot_idx[x][1]].set_yticks([])

        plt.tight_layout()
        st.pyplot(fig=fig)
