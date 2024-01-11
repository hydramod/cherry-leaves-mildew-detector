import streamlit as st


class MultiPage:
    """
    A class for creating multi-page Streamlit applications.

    Parameters:
    - app_name (str): The title of the Streamlit application.
    """

    def __init__(self, app_name) -> None:
        """
        Initializes the MultiPage instance.

        Parameters:
        - app_name (str): The title of the Streamlit application.
        """
        self.pages = []
        self.app_name = app_name

        st.set_page_config(
            page_title=self.app_name,
            page_icon="🌳",
            initial_sidebar_state="expanded"
        )

    def add_page(self, title, func) -> None:
        """
        Adds a new page to the Streamlit application.

        Parameters:
        - title (str): The title of the page.
        - func (callable): The function that defines the content of the page.

        Returns:
        None
        """
        self.pages.append({"title": title, "function": func})

    def run(self):
        """
        Runs the Streamlit application.

        Returns:
        None
        """
        st.title(self.app_name)
        page = st.sidebar.radio(' McGuineys ',
                                self.pages,
                                format_func=lambda page: page['title'])
        page['function']()
