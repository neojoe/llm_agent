Amazon Order Scraper - Design Document
1. System Overview
The Amazon Order Scraper is an autonomous agent designed to fetch user-level order details from the Amazon website. It utilizes Large Language Models (LLMs) for natural language understanding, decision-making, and navigation.
2. Key Components
2.1 Agent Controller
Coordinates the overall process, including task planning and action execution.
2.2 Web Interaction Module
Handles interactions with the Amazon website, including login and navigation.
2.3 Data Extractor
Extracts relevant information from web pages using BeautifulSoup and LLM-generated extraction rules.
2.4 Data Storage
Stores extracted order details in JSON format.
2.5 LLM Interface
Provides an interface to interact with the Large Language Model for decision-making and information extraction.
3. Workflow

The agent starts by logging into the Amazon website.
It navigates to the order history page.
For each order:

The agent extracts order details.
It stores the extracted data in JSON format.


The process continues until all orders are processed.
The agent terminates the process.

4. Security Considerations

User credentials are not stored and are input securely at runtime.
The system uses HTTPS for all web interactions.
API keys are stored securely in environment variables.

5. Scalability and Performance

The system is designed to handle varying numbers of orders efficiently.
Rate limiting is implemented to respect Amazon's servers and avoid being blocked.

6. Limitations and Future Improvements

Currently, the system does not handle pagination for users with a large number of orders.
Error handling could be improved for production use.
The system could be extended to handle multiple e-commerce platforms.

7. Ethical Considerations

The system is designed for educational purposes and should be used in compliance with Amazon's terms of service.
Users should obtain proper authorization before deploying this system.