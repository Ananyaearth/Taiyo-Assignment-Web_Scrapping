import requests
from bs4 import BeautifulSoup
import pandas as pd
import tqdm

class DataScraper:
    def __init__(self, base_urls):
        self.base_urls = base_urls

    def scrape(self):
        csv_file = []
        for base_url in self.base_urls:
            for page in tqdm.tqdm(range(1, 125)):
                r = requests.get(base_url + str(page))
                c = r.content
                soup = BeautifulSoup(c, 'html.parser')
                all_data = soup.find_all("div", {"class": "search-result"})
                for item in all_data:
                    d = {
                        "Tender": item.find("a", {"class": ["govuk-link", "search-result-rwh", "break-word"]}).text,
                        "Company": item.find("div", {"class": ["search-result-sub-header", "wrap-test"]}).text,
                        "Procurement": item.find_all("div", {"class": "search-result-entry"})[0].text.replace("Procurement stage", " "),
                        "Notice": item.find_all("div", {"class": "search-result-entry"})[1].text.replace("Notice status", " "),
                        "Location": item.find_all("div", {"class": "search-result-entry"})[3].text.replace("Contract location", " ")
                    }
                    try:
                        d["Closing"] = item.find_all("div", {"class": "search-result-entry"})[2].text.replace("Closing", " ")
                    except:
                        d["Closing"] = "None"
                    try:
                        d["Value"] = item.find_all("div", {"class": "search-result-entry"})[4].text.replace("Contract value", " ")
                    except:
                        d["Value"] = "None"
                    try:
                        d["Date"] = item.find_all("div", {"class": "search-result-entry"})[5].text.replace("Publication date", " ")
                    except:
                        d["Date"] = "None"
                    csv_file.append(d)
        df = pd.DataFrame(csv_file)
        return df

if __name__ == "__main__":
    base_urls = ["https://www.contractsfinder.service.gov.uk/Search/Results?&page="]
    scraper = DataScraper(base_urls)
    df = scraper.scrape()
    df.to_csv("raw_data.csv", index=False)
    print("Scraping completed and data saved to raw_data.csv")
