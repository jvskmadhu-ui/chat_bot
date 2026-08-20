from datetime import datetime
import re

from flask import Flask, request, jsonify, send_from_directory

app = Flask(__name__)


@app.route('/')
def home():
    return send_from_directory(app.root_path, 'index.html')


@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json(silent=True) or {}
    message = data.get('message')

    if not message:
        return jsonify({'error': 'No message provided'}), 400
    elif not isinstance(message, str):
        return jsonify({'error': 'Message must be a string'}), 400
    elif len(message) > 500:
        return jsonify({'error': 'Message is too long'}), 400
    elif len(message) < 1:
        return jsonify({'error': 'Message is too short'}), 400
    elif message == "Hello":
        return jsonify({'response': 'Hi there! How can I help you today?'}), 200
    elif message == "What is your name?":
        return jsonify({'response': 'Nice to meet you!'}), 200
    elif message == "What can you do?":
        return jsonify({'response': 'I can assist you with various tasks and answer your questions!'}), 200
    elif message == "goodmorning":
        return jsonify({'response': 'Good morning! How can I assist you today?'}), 200
    elif message == "goodnight":
        return jsonify({'response': 'Good night! Sleep well and have a great day tomorrow!'}), 200
    elif message == "what is your favorite color?":
        return jsonify({'response': 'I like all colors equally!'}), 200
    elif message.lower() == "what is the weather like today?":
        return jsonify({'response': 'The weather is quite pleasant today!'}), 200
    elif message == "tell me a joke":
        return jsonify({'response': 'Why did the scarecrow win an award? Because he was outstanding in his field!'}), 200
    elif message == "tell me a fun fact":
        return jsonify({'response': 'Did you know that honey never spoils? Archaeologists have found pots of honey in ancient Egyptian tombs that are over 3,000 years old and still perfectly edible!'}), 200
    elif message == "what is the time now?":
        current_time = datetime.now().strftime("%H:%M:%S")
        return jsonify({'response': f'The current time is {current_time}'}), 200
    elif message == "what is the date today?":
        current_date = datetime.now().strftime("%Y-%m-%d")
        return jsonify({'response': f'Today\'s date is {current_date}'}), 200
    elif message == "what is the day today?":
        current_day = datetime.now().strftime("%A")
        return jsonify({'response': f'Today is {current_day}'}), 200
    elif message == "what is the month today?":
        current_month = datetime.now().strftime("%B")
        return jsonify({'response': f'This month is {current_month}'}), 200
    elif message == "what is the year today?":
        current_year = datetime.now().strftime("%Y")
        return jsonify({'response': f'This year is {current_year}'}), 200
    elif message == "what is summ of its digits?":
        return jsonify({'response': 'Please provide a number to calculate the sum of its digits.'}), 200
    match = re.search(r'\d+', message)
    if match:
        number = match.group()
        digit_sum = sum(int(digit) for digit in number)
        return jsonify({'response': f'The sum of the digits in {number} is {digit_sum}'}), 200
    elif message == "what is the factorial of a number?":
        return jsonify({'response': 'Please provide a number to calculate its factorial.'}), 200
    match = re.search(r'\d+', message)
    if match:
        number = int(match.group())
        factorial = 1
        for i in range(1, number + 1):
            factorial *= i
        return jsonify({'response': f'The factorial of {number} is {factorial}'}), 200
    elif message == "what is the fibonacci of a number?":
        return jsonify({'response': 'Please provide a number to calculate its Fibonacci sequence.'}), 200
    match = re.search(r'\d+', message)
    if match:
        number = int(match.group())
        fibonacci_sequence = [0, 1]
        for i in range(2, number):
            next_number = fibonacci_sequence[i - 1] + fibonacci_sequence[i - 2]
            fibonacci_sequence.append(next_number)
        return jsonify({'response': f'The Fibonacci sequence up to {number} is {fibonacci_sequence[:number]}'}), 200
    elif message == "open a website":
        return jsonify({'response': 'Please provide a website URL to open.'}), 200
    match = re.search(r'(https?://[^\s]+)', message)
    if match:
        url = match.group(1)
        return jsonify({'response': f'Opening website: {url}'}), 200
    elif message == "search for something":
        return jsonify({'response': 'Please provide a search query.'}), 200
    match = re.search(r'search for (.+)', message, re.IGNORECASE)
    if match:
        query = match.group(1)
        return jsonify({'response': f'Searching for: {query}'}), 200
    elif message == "play a song":
        return jsonify({'response': 'Please provide a song name to play.'}), 200
    match = re.search(r'play (.+)', message, re.IGNORECASE)
    if match:
        song_name = match.group(1)
        return jsonify({'response': f'Playing song: {song_name}'}), 200
    elif message == "set a reminder":
        return jsonify({'response': 'Please provide a reminder message and time.'}), 200
    match = re.search(r'set a reminder for (.+) at (.+)', message, re.IGNORECASE)
    if match:
        reminder_message = match.group(1)
        reminder_time = match.group(2)
        return jsonify({'response': f'Reminder set for {reminder_time}: {reminder_message}'}), 200
    elif message == "tell me the news":
        return jsonify({'response': 'Please provide a news topic or category.'}), 200
    match = re.search(r'tell me the news about (.+)', message, re.IGNORECASE)
    if match:
        news_topic = match.group(1)
        return jsonify({'response': f'Fetching news about: {news_topic}'}), 200
    elif message == "what is the score of a cricket match?":
        return jsonify({'response': 'Please provide the teams or match details to get the score.'}), 200
    match = re.search(r'what is the score of (.+) vs (.+)', message, re.IGNORECASE)
    if match:
        team1 = match.group(1)
        team2 = match.group(2)
        return jsonify({'response': f'Fetching score for {team1} vs {team2}'}), 200
    elif message == "what is the score of a football match?":
        return jsonify({'response': 'Please provide the teams or match details to get the score.'}), 200
    match = re.search(r'what is the score of (.+) vs (.+)', message, re.IGNORECASE)
    if match:
        team1 = match.group(1)
        team2 = match.group(2)
        return jsonify({'response': f'Fetching score for {team1} vs {team2}'}), 200
    elif message == "tell about my courses":
        return jsonify({'response': 'Please provide the course name or details to get information.'}), 200
    match = re.search(r'tell about my courses (.+)', message, re.IGNORECASE)
    if match:
        course_name = match.group(1)
        return jsonify({'response': f'Fetching information about your course: {course_name}'}), 200
    elif message == "tell about my nationality":
        return jsonify({'response': 'Please provide your nationality to get information.'}), 200
    match = re.search(r'tell about my nationality (.+)', message, re.IGNORECASE)
    if match:
        nationality = match.group(1)
        return jsonify({'response': f'Fetching information about your nationality: {nationality}'}), 200
    elif message == "tell about my religion":
        return jsonify({'response': 'Please provide your religion to get information.'}), 200
    match = re.search(r'tell about my religion (.+)', message, re.IGNORECASE)
    if match:
        religion = match.group(1)
        return jsonify({'response': f'Fetching information about your religion: {religion}'}), 200
    elif message == "tell a best way or app to learn chess":
        return jsonify({'response': 'One of the best ways to learn chess is through online platforms like Chess.com or Lichess.org. They offer tutorials, puzzles, and the ability to play against other players at various skill levels.'}), 200
    elif message == "tell a best way or app to learn coding":
        return jsonify({'response': 'A great way to learn coding is through platforms like Codecademy, freeCodeCamp, or LeetCode. They provide interactive lessons and challenges to help you improve your coding skills.'}), 200
    elif message == "tell a best way or app to learn programming":
        return jsonify({'response': 'To learn programming, you can use platforms like Coursera, Udemy, or edX. They offer courses in various programming languages and concepts, suitable for beginners to advanced learners.'}), 200   
    elif message == "tell about myself":
        return jsonify({'response': 'I am an AI chatbot designed to assist you with various tasks and answer your questions. I can provide information, help with calculations, and engage in casual conversation.'}), 200
    elif message == "tell about yourself":
        return jsonify({'response': 'I am an AI chatbot created to help you with a wide range of topics. I can provide information, answer questions, and assist with various tasks. My goal is to make your experience as smooth and helpful as possible.'}), 200
    elif message == "tell any ideas to make money online":
        return jsonify({'response': 'There are several ways to make money online, such as freelancing, starting a blog or YouTube channel, selling products on e-commerce platforms, participating in online surveys, or offering online courses or tutoring.'}), 200

    else:
        return jsonify({'response': "I'm not sure how to respond to that."}), 200


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

