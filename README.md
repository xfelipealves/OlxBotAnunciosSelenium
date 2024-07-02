# OlxBotAnunciosSelenium

This project is a bot developed to automate the posting of ads on the OLX platform using Selenium.

## Technologies Used

- **Python**: Main programming language.
  - **pandas**: Data manipulation and analysis.
  - **time**: Timing control.
  - **os**: Interaction with the operating system.
- **Selenium**: Library for web automation.
  - **WebDriver**: Browser control.
  - **WebDriverWait**: Implementation of explicit waits.
  - **ExpectedConditions**: Definition of waiting conditions.
  - **By**: Locating elements on the web page.

## Project Structure

- **bot.py**: Main script containing the automation logic.
- **requirements.txt**: File with the necessary dependencies.
- **config/**: Directory for configuration files, such as login credentials and ad details.
- **logs/**: Directory for storing log files.

## How to Run

1. Clone the repository:
    ```bash
    git clone https://github.com/xfelipealves/OlxBotAnunciosSelenium.git
    ```
2. Navigate to the project directory:
    ```bash
    cd OlxBotAnunciosSelenium
    ```
3. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```
4. Configure the bot by updating the necessary files in the `config` directory.
5. Execute the script:
    ```bash
    python bot.py
    ```

## Contribution

Feel free to fork the project and submit pull requests. Suggestions and improvements are welcome!

## License

This project does not have a specific license.
