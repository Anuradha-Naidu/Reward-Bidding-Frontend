# Reward Bidding Solution (Frontend)

# Project Structure
The project is structured into frontend and backend components:

## Backend
*The backend is built using Python and Flask framework. It handles the business logic, data management, and API endpoints.*

backend/: Contains all backend files.
__init__.py: Initializes the package.
app.py: Flask application defining API endpoints.
main.py: Main script for running the auction system through CLI.
auction_system.py: Manages auction operations using classes and functions.
event.py: Defines the Event class and related functions.
member.py: Defines the Member class and related functions.

## Frontend
*The frontend is implemented using HTML, CSS, and JavaScript. It provides a user interface to interact with the auction system.*

frontend/: Contains all frontend files.
static/: Static assets.
css/: Contains styles.css for styling.
js/: Contains scripts.js for handling frontend logic.
templates/: Contains index.html as the main HTML template.
Virtual Environment
venv/: Virtual environment (optional but recommended).

# Requirements
Python 3.7 or higher installed.
Flask framework (flask package) installed.
Web browser (Google Chrome, Mozilla Firefox, etc.).

Installation
1. Clone the repository:
```bash
git clone https://github.com/Anuradha-Naidu/Reward-Bidding-Frontend.git 
```

2. Set up a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate
```
On Windows use `venv\Scripts\activate`

3. Install dependencies:
```bash
pip install -r requirements.txt
```

# Running the Application

1. Backend
Navigate to the backend directory:
```bash
cd backend
```
Run the Flask application:
```bash
python app.py
```

This will start the backend server at http://localhost:5001. or 5000 (check once on your local server)

2. Frontend
Open another terminal window/tab.
Navigate to the frontend directory:

```bash
cd frontend
```
Open index.html in a web browser directly or use a web server like Python's built-in server:

```bash
python -m http.server
```
Then, open http://localhost:8000 in your web browser.

# Using the Application
1.The frontend provides forms to add members, add events, register members for events, submit bids, and declare winners.
2. Fill out the forms and submit data to interact with the auction system.

# Output (Screeenshots of Frontend Part only) 

<img width="1438" alt="reward1" src="https://github.com/Anuradha-Naidu/Reward-Bidding-Frontend/assets/88324015/03eab852-721c-42fe-8073-f40f4ab4ba0c">

<img width="1438" alt="reward2" src="https://github.com/Anuradha-Naidu/Reward-Bidding-Frontend/assets/88324015/7b52f49e-6e60-4bc6-a822-aee7bb238d9f">

<img width="1438" alt="reward3" src="https://github.com/Anuradha-Naidu/Reward-Bidding-Frontend/assets/88324015/9589d429-36e6-4e26-bf41-faecbc345693">



