
# My Flask Weather App

This is a simple Flask application for checking weather conditions based on user input.

## Prerequisites

- Python 3 or higher

## Usage

1. Set up your OpenWeather API key:

    - [Sign up](https://home.openweathermap.org/users/sign_up) for a free OpenWeather account.
    - Obtain your API key from the OpenWeather dashboard.

2. Modify the `.env` file in the project root and add your API key:

    ```dotenv
    API_KEY=your_openweather_api_key
    ```

3. Activate the python virtual environment(type 'deavtivate' to quit)

    ```bash
    cd OpenWeather
    source venv/bin/activate
    ```

3. Run the Flask application( at the end for debug):

    ```bash
    flask run 
    ```

4. Open your web browser and go to the host provided when you run flask

5. Enter the city, state, and country in the form and click "Search" to get weather information. eg : Aizawl , MZ , India
