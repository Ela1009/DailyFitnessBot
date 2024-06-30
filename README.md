<h1>DailyFitnessBot </h1>

DailyFitnessBot is a Python script that sends daily fitness tips, workout routines, and motivational quotes to users via WhatsApp. It fetches data from various fitness APIs and schedules messages based on user preferences stored in a SQLite database.

<h2>Features</h2>

Sends daily fitness tips, workout routines, and motivational quotes via WhatsApp.
Uses SQLite for user data storage.
Integrates with external fitness APIs to fetch real-time data.

<h2>Requirements</h2>

Python 3.x
Required Python packages (install using pip install -r requirements.txt):
pywhatkit
schedule
requests
sqlite3

<h2>Setup Instructions</h2>

<h3>Clone the repository:</h3>
git clone https://github.com/yourusername/DailyFitnessBot.git
cd DailyFitnessBot

<h3>Database setup:</h3>
Ensure you have SQLite installed.
Create a new SQLite database file (fitness_bot.db).
Initialize the database schema using create_table.py:python create_table.py

<h3>Add a user (for testing purposes):</h3>
Edit daily_fitness_bot.py and uncomment the example usage in the main block
Add a user by running the script:python daily_fitness_bot.py

