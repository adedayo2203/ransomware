# Ransomware Classification Web Application

This project is a web-based implementation of a ransomware classification system using Random Forest and Naive Bayes algorithms for model comparison. The models were trained using scikit-learn, and the web application was built using Django, HTML, CSS, JavaScript, and Bootstrap.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Technologies Used](#technologies-used)
- [Contributing](#contributing)
- [License](#license)

## Overview

The goal of this project is to classify ransomware using machine learning models. Two models, Random Forest and Naive Bayes, are used to compare their effectiveness. The web application allows users to upload data, run classifications, and view the results.

## Features

- Upload datasets for classification
- Compare the performance of Random Forest and Naive Bayes models
- Visualize classification results
- User-friendly web interface

## Installation

To get started with this project, follow these steps:

1. **Clone the repository:**
   ```sh
   git clone https://github.com/JayBeloved/ransomware.git
   cd ransomware
   ```

2. **Create and activate a virtual environment:**
   ```sh
   python -m venv venv
   source venv/bin/activate   # On Windows, use `venv\Scripts\activate`
   ```

3. **Install the required packages:**
   ```sh
   pip install -r requirements.txt
   ```

4. **Set up the Django project:**
   ```sh
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Run the Django development server:**
   ```sh
   python manage.py runserver
   ```

6. **Open your browser and navigate to:**
   ```
   http://127.0.0.1:8000
   ```

## Usage

- **Upload Data:** Use the web interface to upload your dataset for classification.
- **Run Classification:** Choose between Random Forest and Naive Bayes models to classify the uploaded data.
- **View Results:** Visualize the classification results and compare the performance metrics of both models.

## Technologies Used

- **Django**: Web framework for building the web application.
- **HTML, CSS, JavaScript**: Frontend technologies for building the user interface.
- **Bootstrap**: CSS and JavaScript framework for responsive design.
- **scikit-learn**: Machine learning library for training and using the Random Forest and Naive Bayes models.

## Contributing

Contributions are welcome! Please fork the repository and submit pull requests.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
