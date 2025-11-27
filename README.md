🏠 AI Interior Design Agent
This project implements a multi-step AI Agent designed to generate interior design concepts for every room in a user-provided floorplan, based on a specified design style. The agent is driven by a Streamlit UI for easy interaction.

🌟 Features
Streamlit UI: Provides a simple web interface for uploading floorplans and submitting design styles.

Multimodal Input: Accepts a visual floorplan image and a text design style prompt.

Iterative Design: Generates up to 5 distinct images, one for each major room identified.

Custom Tool Integration: Uses a custom tool (save_design_data_to_database) to structure and save generated design details (furniture, color palette, style) after each image is created.

Guardrails: Employs an input guardrail to ensure the user's floorplan is valid and the design request is appropriate.

Secure Output: Saves all generated images to a local output/ directory and displays them in the UI.

🛠️ Setup and Installation
1. Clone the Repository
Bash

git clone https://github.com/Ken-Mens/AI_Agent_II.git
cd AI_Agent_II
2. Environment Setup
Bash

# Create and activate the virtual environment (e.g., for Windows):
python -m venv .venv
.\.venv\Scripts\activate
3. Install Dependencies
Install all required packages (including streamlit, asyncio, etc.) from the requirements.txt file:

Bash

pip install -r requirements.txt
4. API Key Configuration (Crucial)
The project requires an OpenAI API key. This key must be stored in a local, untracked file.

Create a file named .env in the root directory.

Add your key inside the file in the following format:

Extrait de code

OPENAI_API_KEY="sk-YOUR_SECRET_KEY_HERE"
🚀 Running the Application
The agent is now run via the Streamlit interface using the app.py file.

Ensure your virtual environment is active.

Run the application using the Streamlit command:

Bash

streamlit run app.py
The application will open automatically in your browser (usually at http://localhost:8501).

Usage Instructions:
Enter your desired Interior Design Styling (e.g., "Bohemian with warm colors").

Upload your floorplan image using the file uploader.

Click "Run Agent".

Expected Output
The application will display:

The structured Design Plan (Style, Rooms, Furniture, etc.).

The up to 5 generated interior design images for the rooms.

📂 Project Structure
AI_Agent_II/
├── .venv/                     # Python Virtual Environment (Ignored by Git)
├── app.py                     # Streamlit UI interface (NEW)
├── lib/
│   ├── agent.py               # Main Agent definition, instructions, and run loop (MODIFIED)
│   ├── files.py               # Utility functions
│   └── tools.py               # Custom tool definition
├── output/                    # Generated images and design_output.txt (Ignored by Git)
├── resources/
│   └── floorplan.jpg          # Input image file
├── .gitignore                 # Specifies files/folders to ignore
├── main.py                    # (No longer used to run the agent)
└── requirements.txt           # Project dependencies