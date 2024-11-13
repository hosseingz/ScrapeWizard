# Scrape Wizard 🕸️✨

**Scrape Wizard** is an AI-powered web scraping tool designed to make it easy to extract specific information from web pages. With a user-friendly interface built on **Streamlit** and backed by an **AI-driven query system**, Scrape Wizard takes your custom prompts and retrieves targeted content directly from any URL.

## Key Features
- **Simple, Intuitive Interface**: Easily navigate and interact with the tool without a steep learning curve.
- **Customizable Queries**: Enter a URL and a specific prompt, and the AI will extract precisely what you're looking for.
- **Robust Error Handling**: Handles network issues, timeouts, and general errors to ensure reliable scraping.
- **AI Integration**: Uses an **Ollama** AI model to parse and understand your specific content requests on any webpage.

---

## Installation 📥

To get started, follow these steps to set up the project and install the necessary dependencies.

### 1. Clone the Repository
```bash
git clone https://github.com/hosseingz/ScrapeWizard.git
cd ScrapeWizard
```

### 2. Install Python Dependencies
Make sure you have [Python](https://www.python.org/) installed. Then, install the project dependencies:

```bash
pip install -r requirements.txt
```

### 3. Install and Set Up Ollama 🧠
**Ollama** is the AI engine used by Scrape Wizard for interpreting and fulfilling content requests. To install and configure the Ollama model required for this project:

1. **Install the Ollama CLI**  
   Ollama provides a command-line tool that allows you to manage and run AI models locally. Download and install it by following instructions on their [official site](https://ollama.com).

2. **Install the Required Model**
   For this project, we use the `phi3:mini` model. Run the following command to download the model via Ollama:

   ```bash
   ollama pull phi3:mini
   ```

3. **Verify the Installation**
   Ensure Ollama is running and accessible. If the `phi3:mini` model was successfully installed, you’re all set to start using the AI scraper.

---

## Usage 🚀

1. **Run the Streamlit Application**
   Start the application with the following command:

   ```bash
   streamlit run main.py
   ```

2. **Enter URL and Query Prompt**
   - **URL**: Paste the URL of the webpage you want to scrape.
   - **Prompt**: Use the prompt input box to specify exactly what you’re looking to extract from the page.

3. **View Results**
   Once you submit, the AI will process the webpage and display relevant content based on your query.

---

## Example Query 📝
1. **Input URL**: `https://example.com`
2. **Prompt**: "Extract the main article title and summary."

The AI will retrieve and display the title and summary as specified in your prompt.

---

## Contributing 🤝
Contributions are welcome! Feel free to fork the repository, submit issues, or create pull requests.

---

## License 📄
This project is licensed under the MIT License.

---

Happy scraping!