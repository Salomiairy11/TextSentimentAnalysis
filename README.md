# Text Sentiment Analysis 📝🔍

This project focuses on analyzing the sentiment of text data, specifically movie reviews from the IMDB dataset. The goal is to classify reviews as positive or negative using natural language processing (NLP) techniques and machine learning models.

---

## Dataset 📊

The project utilizes the **IMDB Dataset**, which contains a collection of movie reviews labeled by sentiment. The dataset is stored in the file `IMDB Dataset.csv`.

---

## Project Structure 📂

- `IMDB Dataset.csv`: The dataset containing movie reviews and their corresponding sentiment labels.
- `sentiment review nlp.ipynb`: Jupyter Notebook detailing the data analysis, preprocessing steps, model training, and evaluation.
- `nlp_kathford.joblib`: Serialized machine learning model saved for future predictions.

---

## Requirements 🛠️

To run the code and experiments in this project, ensure you have the following Python libraries installed:

- `pandas`: For data manipulation and analysis.
- `numpy`: For numerical computations.
- `scikit-learn`: For machine learning algorithms and evaluation metrics.
- `nltk`: The Natural Language Toolkit for text processing.
- `joblib`: For model serialization.

You can install these dependencies using `pip`:

```bash
pip install pandas numpy scikit-learn nltk joblib
