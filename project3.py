from flask import Flask, jsonify
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

def get_latest_stories():
    url = "https://time.com"
    response = requests.get(url)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        articles = soup.find_all('article', class_='homepage-module--headline--1UP8V')
        latest_stories = []
        
        for article in articles[:6]:
            title = article.find('a', class_='headline').text.strip()
            link = article.find('a', class_='headline')['href']
            latest_stories.append({'title': title, 'link': link})
        
        return latest_stories
    else:
        print("Failed to retrieve data from Time.com")
        return []

@app.route('/getTimeStories')
def get_time_stories():
    latest_stories = get_latest_stories()
    return jsonify(latest_stories)

if __name__ == '__main__':
    app.run(debug=True)
