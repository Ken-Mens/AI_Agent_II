Features
Multimodal Input: Accepts a visual floorplan image and a text design style prompt.

Iterative Design: Generates up to 5 distinct images, one for each major room identified in the floorplan (e.g., Living Room, Kitchen, Bedrooms).

Custom Tool Integration: Uses a custom tool (save_design_data_to_database) to structure and save generated design details (furniture, color palette, style) after each image is created.

Guardrails: Employs an input guardrail to ensure the user's floorplan is valid and the design request is appropriate.

Secure Output: Saves all generated images to a local output/ directory.

🛠️ Setup and Installation
1. Clone the Repository
Bash

git clone https://github.com/Ken-Mens/AI_Agent_II.git
cd AI_Agent_II
2. Environment Setup
This project requires a Python virtual environment.

Bash

# Create the virtual environment
python -m venv .venv

# Activate the virtual environment
# Windows:
.\.venv\Scripts\activate
# macOS/Linux:
# source .venv/bin/activate
3. Install Dependencies
Install the required packages using the requirements.txt file:

Bash

pip install -r requirements.txt
4. API Key Configuration (Crucial)
The project requires an OpenAI API key for the gpt-4.1 model and image generation. For security, this key is not tracked by Git.

Create a file named .env in the root directory of the project.

Add your key inside the file in the following format:

Excerpt


OPENAI_API_KEY="sk-YOUR_SECRET_KEY_HERE"
🚀 How to Run the Agent
The main script is configured to run the agent with a predefined floorplan image (resources/floorplan.jpg) and a design style.

You can modify the style in main.py before running.

Run the project from the root directory with the virtual environment activated:

Bash

python main.py
Expected Output
The script will:

Print the final text output (the structured design data saved by the custom tool).

Automatically open the up to 5 generated .png image files (e.g., generated_image_0.png through generated_image_4.png) from the output/ directory.

📂 Project Structure
AI_Agent_II/
├── .venv/                     # Python Virtual Environment (Ignored by Git)
├── lib/
│   ├── agent.py               # Main Agent definition, instructions, and run loop
│   ├── files.py               # Utility functions (open_file, retrieve_image, ensure_output_dir)
│   └── tools.py               # Custom tool definition (save_design_data_to_database)
├── output/                    # Generated images and design_output.txt (Ignored by Git)
├── resources/
│   └── floorplan.jpg          # Input image file
├── .gitignore                 # Specifies files/folders to ignore (.env, .venv/, output/)
├── main.py                    # Entry point for the application
└── requirements.txt           # Project dependencies
