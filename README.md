# Tech News Fetcher
Tech News Fetcher is a simple Python script that allows you to grab the latest tech headlines from CNN and FOX News. Additionally, if you have an OpenAI API key with available tokens, you can generate a very brief summary of the day's important news.

## Features
- **Get Latest Tech Headlines:** Choose between CNN and FOX News to fetch the most recent tech news. 
- **AI Summary:** With an OpenAI API key, you can get a brief, AI-powered sumamry of today's top news.

## Dependencies
Before you start, make sure you have the following installed:
- Python 3.x 
- `requests` library: Install with `pip install requests`
- `BeautifulSoup` library: Install with `pip install beautifulsoup4`
- OpenAI API key (*optional*)

## Installation
1. **Clone the Repository:** 
```bash
git clone https://github.com/Skittysh/TechNewsFetcher.git
```
2. **Go to the Project Directory:**
```bash
cd tech-news-fetcher
```
3. **Install Required Libraries:** (*optional*)
```bash
pip install -r requirements.txt
```
## How to Use It
1. **Run the Script:** 
 ```bash
python3 app.py
```
2. **Pick your preferred News Source:** When asked, type `CNN` or `FOX` to select your news network. 
3. **Get the AI Summary:** (*optional*) If you have OpenAI tokens, answer `Y` to get a short summary of the day's important news.

## License
This project is open-source and available under the MIT License. See [LICENSE](https://github.com/nokia/RED/blob/main/LICENSE) for details.
