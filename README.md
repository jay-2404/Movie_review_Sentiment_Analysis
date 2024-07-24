# Movie Review Sentiment Analysis

Welcome to the Movie Review Sentiment Analysis app! This Streamlit application predicts whether a movie review is positive or negative using a machine learning model.

Site is Live at: https://movie-review-sentiment-analysis-2.onrender.com/

## Features

- Enter a movie review and get an instant prediction of its sentiment.
- The app uses a pre-trained model and scaler to process and predict the sentiment of the review.


## Technologies Used

- **Python**: Programming language used.
- **Streamlit**: Framework for building the interactive web application.
- **Scikit-learn**: Library for machine learning and model prediction.
- **Pandas**: Data manipulation library.
- **Pickle**: Serialization library to load the pre-trained model and scaler.

## Setup

1. **Clone the Repository**:

   ```sh
   git clone https://github.com/your-username/movie-review-sentiment-analysis.git
   cd movie-review-sentiment-analysis
   ```

2. **Create a Virtual Environment**:

   ```sh
   python -m venv env
   source env/bin/activate  # On Windows use `env\Scripts\activate`
   ```

3. **Install Dependencies**:

   ```sh
   pip install -r requirements.txt
   ```

4. **Run the Application**:

   ```sh
   streamlit run app.py
   ```

   This command will start the Streamlit server and open the app in your default web browser.

##Screenshots
![image](https://github.com/user-attachments/assets/25daef01-2c4a-41cd-9ac7-de61baad417c)
![image](https://github.com/user-attachments/assets/9aa53f73-814b-41f5-9621-5034d9171d68)



## Files

- `app.py`: The main Python script containing the Streamlit app.
- `model.pkl`: The pre-trained machine learning model used for sentiment prediction.
- `scaler.pkl`: The scaler used to preprocess the review text before prediction.
- `requirements.txt`: A file listing the Python dependencies for the project.

## Contributing

Feel free to fork the repository and submit pull requests. If you find any issues or have suggestions, please open an issue on GitHub.

