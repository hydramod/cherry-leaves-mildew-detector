import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
from src.machine_learning.evaluate_clf import load_test_evaluation


def page_ml_performance_metrics():
    """
    Display the machine learning model performance metrics.

    This page showcases various metrics, including label distribution, model
    training history graphs (accuracy and loss),
    model architecture, and general performance on the test set.

    Returns:
    None
    """
    version = 'v1'
    
    st.image("images/tree farm.jpg", use_column_width=True)

    st.write("### Train, Validation, and Test Set: Labels Frequencies")

    labels_distribution = plt.imread(
        f"outputs/{version}/labels_distribution.png")
    st.image(labels_distribution,
             caption='Labels Distribution on Train, Validation, and Test Sets')
    st.write("---")

    st.write("### Model History")

    model_acc = plt.imread(f"outputs/{version}/model_training_accuracy.png")
    st.image(model_acc, caption='Model Training Accuracy')
    st.info("Training Accuracy refers to the accuracy from the training set. "
            "Validation accuracy refers to the Training accuracy against the "
            "validation set.")

    model_loss = plt.imread(f"outputs/{version}/model_training_loss.png")
    st.image(model_loss, caption='Model Training Losses')
    st.info("Loss is the training metric of the ML to adjust its weights and "
            "biases for better predictions.")

    st.write("---")

    if st.checkbox('Model Architecture: Sequential'):
        st.text(
            """
            Model Architecture: Sequential
            _________________________________________________________________
            Layer (type)                Output Shape              Param #
            =================================================================
            conv2d (Conv2D)             (None, 254, 254, 24)      672
            _________________________________________________________________
            max_pooling2d (MaxPooling2  (None, 127, 127, 24)      0
            D)
            _________________________________________________________________
            conv2d_1 (Conv2D)           (None, 125, 125, 12)      2604
            _________________________________________________________________
            max_pooling2d_1 (MaxPoolin  (None, 62, 62, 12)        0
            g2D)
            _________________________________________________________________
            conv2d_2 (Conv2D)           (None, 60, 60, 8)         872
            _________________________________________________________________
            max_pooling2d_2 (MaxPoolin  (None, 30, 30, 8)         0
            g2D)
            ...
            Total params: 155,371 (606.92 KB)
            Trainable params: 155,371 (606.92 KB)
            Non-trainable params: 0 (0.00 Byte)
            _________________________________________________________________
            """
        )

    if st.checkbox('Sequential Model Layers'):
        st.text(
            """
            model = Sequential()

            # First convolutional layer
            model.add(Conv2D(filters=24, kernel_size=(3, 3),
                      input_shape=image_shape, activation='relu'))
            model.add(MaxPooling2D(pool_size=(2, 2)))

            # Second convolutional layer
            model.add(Conv2D(filters=12, kernel_size=(3, 3),
                      activation='relu'))
            model.add(MaxPooling2D(pool_size=(2, 2)))

            # Third convolutional layer
            model.add(Conv2D(filters=8, kernel_size=(3, 3), activation='relu'))
            model.add(MaxPooling2D(pool_size=(2, 2)))

            # Fourth convolutional layer
            model.add(Conv2D(filters=6, kernel_size=(3, 3), activation='relu'))
            model.add(MaxPooling2D(pool_size=(2, 2)))

            # Flatten layer
            model.add(Flatten())

            # Dense layer
            model.add(Dense(128, activation='relu'))

            # Dropout layer to prevent overfitting
            model.add(Dropout(0.5))

            # Output layer with sigmoid activation for binary classification
            model.add(Dense(1, activation='sigmoid'))

            # Compile the model
            model.compile(loss='binary_crossentropy', optimizer='adam',
                          metrics=['accuracy'])
            """
        )

    if st.checkbox('Generalised Performance Metrics'):
        st.dataframe(pd.DataFrame(load_test_evaluation(version),
                                  index=['Loss', 'Accuracy']))
