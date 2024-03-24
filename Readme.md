# Lip Reading System with Deep Learning

This repository contains an AI model for lipreading, which can be used to predict spoken words from lip movements in videos.

## How to Use

### 1. Clone the Repository

Clone this repository to your local machine using the following command:

```bash
git clone https://github.com/Rohanjai/AI-Lipreading-Model.git
```

### 2. Create a Virtual Environment with Conda

Navigate to the project directory and create a virtual environment using conda:

```bash
cd AI-Lipreading-Model
conda create --p venv python=3.8
```

Activate the virtual environment:

```bash
conda activate venv
```

### 3. Install Required Packages

Install all the required packages listed in `requirements.txt` using pip:

```bash
pip install -r requirements.txt
```

### 4. Data Collection

To collect data for training the model, run the `collect.py` script located in the data collection folder:

```bash
python data_collection/collect.py
```

This script will collect and preprocess the data to create the dataset.

### 5. Live Predictions

To perform live predictions using the trained model, run the `predict_live.py` script:

```bash
python demo/predict_live.py
```

This script will use the trained model to predict spoken words from lip movements in live video streams.

### 6. API Reference

For API reference and to interact with the model through a user-friendly interface, a Streamlit web application has been provided. Run the following command to start the Streamlit app:

```bash
streamlit run app.py
```

This will launch the web application in your default web browser.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
