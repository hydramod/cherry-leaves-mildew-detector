import streamlit as st


def page_summary_body():
    """
    Display the summary page body with general info and details about
    requirements and quality.

    This page provides an overview of the project, including info about
    the built-in machine learning system
    for detecting mildew infection in cherry leaf images. It also highlights
    the optimization of images and presents
    achievements in meeting accuracy goals.

    Additionally, users can find more info about business requirements,
    statistical details in Project Hypothesis,
    and insights into Machine Learning and Convolutional Neural Networks in
    Project Performance.

    For additional details, users are encouraged to read the Project README
    file on GitHub.

    Returns:
    None
    """
    st.image("/workspace/cherry-leaves-mildew-detector-project-5/app_pages/images/farmy foods.jpg", use_column_width=True)

    st.info("### General info\n"
            "This website incorporates a built-in machine learning system "
            "designed for detecting mildew infection in cherry leaf images. "
            "It can quickly distinguish between healthy leaves and those with "
            "powdery mildew. "
            "Click on Mildew Detection in the sidebar to upload your image. "
            "Before doing that, take a look at the Image Montage in the "
            "Leaves Visualizer to see how images are optimized.")

    st.write("---")

    st.success("### Requirements and Quality\n"
               "Our goal was to achieve over ±2 standard deviations from the "
               "mean, and we are proud to announce that we have surpassed the "
               "97% range, exceeding our accuracy goal.")

    if st.button("Info"):
        st.write("* You can find extra info about business "
                 "requirements and statistical info in Project "
                 "Hypothesis.\n * You can find additional info about "
                 "Machine Learning and Convolutional Neural Networks in "
                 "Project Performance.")

        st.warning("For more details, please visit and read the "
                   "[Project README file](https://github.com/hydramod/"
                   "cherry-leaves-mildew-detector-project-5/blob/main/"
                   "README.md).")
