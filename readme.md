# Celebrity GPT

Celebrity GPT is a Streamlit-based application that utilizes OpenAI's GPT models to fetch and display information about celebrities. The app provides a brief biography, date of birth, and five major historical events from the celebrity's birth date.

## Features
- Input a celebrity's name to retrieve their biography.
- Get the birth date formatted as `Month Day, Year`.
- Display five significant events that occurred on the birth date.
- Includes a **Refresh** button to reload the app and a **Clear** button to reset all inputs and session states.

## Installation

### Prerequisites
Ensure you have the following installed:
- Python 3.8+
- `pip` (Python package manager)
- OpenAI API key stored in `secrets.toml`

### Steps
1. Clone the repository:
   ```sh
   git clone https://github.com/your-repo/celebrity-gpt.git
   cd celebrity-gpt
   ```

2. Create and activate a virtual environment:
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

4. Set up your OpenAI API key:
   - Create a `.streamlit/secrets.toml` file and add:
     ```toml
     [secrets]
     OPENAI_API_KEY = "your-api-key-here"
     ```

5. Run the Streamlit app:
   ```sh
   streamlit run Celebrity_GPT.py
   ```

## Usage
1. Enter a celebrity's name in the input field.
2. Click **Submit** to fetch details.
3. Use the **Clear** button to reset the inputs and memory.
4. Use the **Refresh** button to reload the app.

## Future Enhancements
- Improve response accuracy using fine-tuned LLMs.
- Add an image-fetching feature for celebrities.
- Implement multi-language support.

## License
This project is licensed under the MIT License.

