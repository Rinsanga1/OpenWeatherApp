
# My Flask Weather App

This is a simple Flask application for checking weather conditions based on user input.

## Prerequisites

- Python 3 or higher
- [Pip](https://pip.pypa.io/en/stable/installation/) (Python package installer)

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/Rinsanga1/OpenWeatherApp.git
    ```

2. Navigate to the project directory:

    ```bash
    cd OpenWeather
    ```

3. Install the required dependencies:

    ```bash
    pip install flask
    pip install requests 
    pip install python-dotenv

    ```

## Usage

1. Set up your OpenWeather API key:

    - [Sign up](https://home.openweathermap.org/users/sign_up) for a free OpenWeather account.
    - Obtain your API key from the OpenWeather dashboard.

2. Modify the `.env` file in the project root and add your API key:

    ```dotenv
    API_KEY=your_openweather_api_key
    ```

3. Run the Flask application:

    ```bash
    python app.py
    ```

4. Open your web browser and go to [http://localhost:5000/](http://localhost:5000/).

5. Enter the city, state, and country in the form and click "Search" to get weather information. eg : Aizawl , MZ , India
