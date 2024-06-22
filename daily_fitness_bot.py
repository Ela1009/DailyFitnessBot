import pywhatkit
import schedule
import time
import random
import requests
import sqlite3
from datetime import datetime, timedelta


conn = sqlite3.connect('fitness_bot.db')
cursor = conn.cursor()


fitness_tips_url = "https://fitness-api.example.com/tips"
workout_routines_url = "https://fitness-api.example.com/workouts"
motivational_quotes_url = "https://quotes-api.example.com/motivational"


def get_fitness_tip():
    try:
        response = requests.get(fitness_tips_url)
        response.raise_for_status()
        data = response.json()
        return random.choice(data['tips'])
    except requests.RequestException:
        return "Stay active and healthy!"


def get_workout_routine():
    try:
        response = requests.get(workout_routines_url)
        response.raise_for_status()
        data = response.json()
        return random.choice(data['workouts'])
    except requests.RequestException:
        return "Try a 30-minute brisk walk!"


def get_motivational_quote():
    try:
        response = requests.get(motivational_quotes_url)
        response.raise_for_status()
        data = response.json()
        return random.choice(data['quotes'])
    except requests.RequestException:
        return "You are capable of amazing things!"


def send_whatsapp_message(phone_number, message):
    pywhatkit.sendwhatmsg_instantly(phone_number, message)


def send_daily_fitness_content():
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    
    for user in users:
        user_id, phone_number, preferred_time, workout_preference, tip_preference, last_sent = user
        
        
        if last_sent and datetime.strptime(last_sent, "%Y-%m-%d").date() == datetime.now().date():
            continue

        tip = get_fitness_tip() if tip_preference else "Remember to stay hydrated!"
        workout = get_workout_routine() if workout_preference else "Go for a walk!"
        quote = get_motivational_quote()
        
        message = f"🌟 Daily Fitness Motivation 🌟\n\n{tip}\n\nToday's Workout:\n{workout}\n\nMotivation:\n{quote}"
        send_whatsapp_message(phone_number, message)
        
        
        cursor.execute("UPDATE users SET last_sent = ? WHERE id = ?", (datetime.now().strftime("%Y-%m-%d"), user_id))
        conn.commit()


def schedule_jobs():
    cursor.execute("SELECT DISTINCT preferred_time FROM users")
    times = cursor.fetchall()
    
    for (preferred_time,) in times:
        schedule.every().day.at(preferred_time).do(send_daily_fitness_content)


def add_user(phone_number, preferred_time, workout_preference=None, tip_preference=None):
    cursor.execute("INSERT INTO users (phone_number, preferred_time, workout_preference, tip_preference, last_sent) VALUES (?, ?, ?, ?, ?)",
                   (phone_number, preferred_time, workout_preference, tip_preference, None))
    conn.commit()


if __name__ == "__main__":
    
    #("+1234567890", (datetime.now() + timedelta(minutes=2)).strftime("%H:%M"), workout_preference=True, tip_preference=True)
    add_user("+385989905242", "12:15", workout_preference=True, tip_preference=True)
    
    schedule_jobs()
    
    while True:
        schedule.run_pending()
        time.sleep(1)
