import streamlit as st


def page_project_hypothesis_body():
    """
    Display the section on Project Hypothesis and Validation.

    This section outlines the hypotheses and validations for the project,
    focusing on the program's ability to accurately
    distinguish between leaves without mildew infection and leaves with mildew
    infection.

    The general accuracy rate is reported to be 99%.

    Returns:
    None
    """
    st.image("/workspace/cherry-leaves-mildew-detector-project-5/app_pages/images/tree.jpg", use_column_width=True)
    
    st.write("### Project Hypothesis and Validation")

    st.success("* This program is designed to effectively separate leaves "
               "without mildew infection from leaves with mildew infection.\n"
               "* The overall accuracy rate is reported to be 99%.")
