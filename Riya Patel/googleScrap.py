import requests
from bs4 import BeautifulSoup
import pandas as pd

def search_google(query):
    url = f"https://www.google.com/search?q={query}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.text
    else:
        print("Failed to fetch Google search results.")
        return None

def extract_results(html):
    soup = BeautifulSoup(html, "html.parser")
    results = []
    for g in soup.find_all('div', class_='tF2Cxc'):
        title = g.find('h3').text if g.find('h3') else None
        link = g.find('a')['href'] if g.find('a') else None
        description = g.find('span', class_='aCOpRe').text if g.find('span', class_='aCOpRe') else None
        if title and link and description:
            results.append({"Title": title, "URL": link, "Description": description})
    return results

def save_to_csv(data, filename="search_results.csv"):
    df = pd.DataFrame(data)
    df.to_csv(filename, index=False)
    print(f"Data saved to {filename}")

if __name__ == "__main__":
    query = "internshala"
    html = search_google(query)
    if html:
        results = extract_results(html)
        if results:
            save_to_csv(results)
        else:
            print("No results found.")
    else:
        print("Unable to perform search.")
