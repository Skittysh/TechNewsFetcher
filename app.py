import requests
from bs4 import BeautifulSoup
import openai


client = openai.OpenAI(api_key="here-your-key")

urlchoice = input("Do you want to see the latest tech news from CNN or FOX? (CNN/FOX): ")


if(urlchoice == 'CNN'):
    url = 'https://www.cnn.com/business/tech'
elif(urlchoice == 'FOX'):
    url = 'https://www.foxnews.com/tech'
    
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')



if urlchoice == 'CNN':
    data = soup.find_all('span', class_='container__headline-text')
    for headline in data:
        print(headline.text)
        print("\n")
elif urlchoice == 'FOX':
    data = soup.find_all('h4', class_='title')
    for headline in data:
        print(headline.text)
        print("\n")

aichoice = input("Do you have tokens to use the AI? (Y/N): ")
if aichoice == 'Y':
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "user",
                "content": "In one sentence, what important news happened today?",
            },
        ],
    )
    print(completion.choices[0].message.content)

