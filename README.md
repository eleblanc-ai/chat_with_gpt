# Chat with GPT - README

## Overview

This project is a web application that allows users to interact with OpenAI's GPT models through a chat interface. The app is built using Flask for the backend and plain HTML/CSS/JavaScript for the frontend. The application supports streaming responses from the GPT model to provide a real-time chat experience.

### Motivation

One of the key motivations behind this project is to ensure the privacy and security of user data. By utilizing the API, the data inputted by users is not used for training purposes by OpenAI. This approach allows users to interact with the models while ensuring that their data remains private and secure, adhering to best practices for data protection and user confidentiality.

## Features

- Interactive chat interface to communicate with GPT models.
- Supports multiple GPT models: GPT-4o, GPT-4, and GPT-3.5 Turbo.
- Streams responses in real-time.
- Maintains conversation history locally in the browser.
- Provides an option to clear the conversation history.

## Prerequisites

- Python 3.7+
- Flask
- OpenAI Python client library
- dotenv

## Setup Instructions

1. **Clone the repository:**

    ```bash
    git clone https://github.com/eleblanc-ai/chat_with_gpt.git
    cd chat_with_gpt
    ```

2. **Create and activate a virtual environment:**

    - On Windows:

        ```bash
        python -m venv venv
        venv\Scripts\activate
        ```

    - On macOS/Linux:

        ```bash
        python -m venv venv
        source venv/bin/activate
        ```

3. **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Set up environment variables:**

    Create a `.env` file in the root directory of your project and add your OpenAI API key:

    ```bash
    OPENAI_API_KEY=your_openai_api_key
    ```

5. **Run the application:**

    ```bash
    python app.py
    ```

6. **Open the application in your browser:**

    Go to `http://127.0.0.1:5000/` to access the chat interface.

7. **Deactivate the virtual environment:**

    To deactivate the virtual environment, simply run:

    ```bash
    deactivate
    ```

## File Structure

- `app.py`: The main Flask application file that handles the backend logic, including routing and interaction with the OpenAI API.
- `index.html`: The frontend of the application that provides the chat interface.

## Usage

1. **Start the application:**

    Run the Flask application by executing `python app.py`. Open your browser and navigate to `http://127.0.0.1:5000/`.

2. **Chat with GPT:**

    - Enter your message in the input box.
    - Select the desired GPT model from the dropdown menu.
    - Click the send button or press `Enter` to send your message.
    - The model's response will be streamed and displayed in real-time.

3. **Clear conversation history:**

    Click the "Clear Context" button to clear the current conversation history.

## Customization

### Styling

To customize the appearance of the chat interface, modify the CSS in the `<style>` section of `index.html`.

### Backend

To extend or modify the backend functionality, edit the `app.py` file. Ensure to handle any additional routes or logic needed for your specific use case.

## Troubleshooting

- **API Key Errors:**

    Ensure that the `OPENAI_API_KEY` is correctly set in the `.env` file.

- **Dependencies:**

    Verify that all dependencies are installed by running `pip install -r requirements.txt` if you have a `requirements.txt` file, or manually install the required packages.

[//]: # ()
[//]: # (## License)

[//]: # ()
[//]: # (This project is licensed under the MIT License.)

[//]: # ()
[//]: # (---)

Feel free to reach out for any further assistance or questions regarding the setup and usage of this application.
