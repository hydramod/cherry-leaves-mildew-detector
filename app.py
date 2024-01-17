import streamlit as st
from app_pages.multipage import MultiPage
from app_pages.summary import page_summary_body
from app_pages.leaves_visualizer import page_leaves_visualizer_body
from app_pages.mildew_detector import page_mildew_detector_body
from app_pages.project_hypothesis import page_project_hypothesis_body
from app_pages.ml_performance import page_ml_performance_metrics


def add_pages(app, pages):
    """
    Add pages to the MultiPage app.
    """
    for page_name, page_body in pages:
        app.add_page(page_name, page_body)


def main():
    """
    Main function to run the Streamlit app.
    """
    app = MultiPage(app_name="🍒Farmy & Foods: Cherry leaf mildew detector🍒")

    pages = [
        ("🗒️📌 Project Summary", 
            lambda: page_summary_body(app)),
        ("🌿🍃🌳 Leaves Visualizer",
            lambda: page_leaves_visualizer_body(app)),
        ("🕵️‍♂️🍂 Mildew Detection",
            lambda: page_mildew_detector_body(app)),
        ("🤔💭🔍 Project Hypothesis",
            lambda: page_project_hypothesis_body(app)),
        ("📊📈📉 ML Performance Metrics",
            lambda: page_ml_performance_metrics(app)),
    ]

    add_pages(app, pages)

    app.run()


if __name__ == "__main__":
    main()
