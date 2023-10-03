import requests
from bs4 import BeautifulSoup

def get_hacker_news_top_article():
    response = requests.get("https://news.ycombinator.com/")
    yc_web_page = response.text
    
    if response.status_code != 200:
        print(f"Failed to fetch the webpage: {response.status_code}")
        return
    
    soup = BeautifulSoup(yc_web_page, 'html.parser')
    
    article_titles = [article_tag.get_text() for article_tag in soup.find_all(name="a", class_="storylink")]
    article_links = [article_tag.get("href") for article_tag in soup.find_all(name="a", class_="storylink")]
    
    article_upvotes = []
    for subtext in soup.find_all(name="td", class_="subtext"):
        score = subtext.find(name="span", class_="score")
        article_upvotes.append(int(score.get_text().split()[0]) if score else 0)
    
    if not article_titles or not article_links or not article_upvotes:
        print("No articles were found.")
        return
    
    max_points_index = article_upvotes.index(max(article_upvotes))
    
    print(
        f"{article_titles[max_points_index]}, "
        f"{article_upvotes[max_points_index]} points, "
        f"available at: {article_links[max_points_index]}."
    )

if __name__ == "__main__":
    get_hacker_news_top_article()
