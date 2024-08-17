Setup and Running Instructions for Amazon Order Scraper
This document provides step-by-step instructions for setting up and running the Amazon Order Scraper agent.
Prerequisites
Before you begin, ensure you have the following installed on your system:

Python 3.7 or higher
pip (Python package manager)
Git (for cloning the repository)
Chrome browser (the default WebDriver used in this project)

Setup Instructions

Clone the repository:
git clone https://github.com/yourusername/amazon-order-scraper.git
cd amazon-order-scraper

Create a virtual environment (recommended):
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`

Install the required packages:
pip install -r requirements.txt

Set up your OpenAI API key:

Copy the .env.example file to a new file named .env
Open the .env file and replace your_openai_api_key_here with your actual OpenAI API key


Download and install ChromeDriver:

Visit the ChromeDriver download page
Download the version that matches your Chrome browser version
Extract the executable and add its location to your system PATH



Running the Agent

Ensure you're in the project directory and your virtual environment is activated.
Run the main script:
python main.py

The script will prompt you for your Amazon login credentials. Enter them when requested.
The agent will start navigating through your Amazon order history, extracting order details.
Extracted order data will be saved as JSON files in the order_data directory.
The process will continue until all orders have been processed, or you can interrupt it by pressing Ctrl+C.