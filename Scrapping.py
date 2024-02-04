import requests
from bs4 import BeautifulSoup
import pandas as pd
url = "https://www.theguardian.com/technology/2024/feb/03/ai-artificial-intelligence-tools-hiring-jobs?ref=upstract.com"
page = requests.get(url)
soup = BeautifulSoup(page.content,"html5")
title = soup.find(class_="dcr-qao4mw").text
content = soup.find(class_="dcr-ch7w1w").text.replace("\n","").replace("Explore more on these topicsArtificial intelligence (AI)The ObserverWork & careersJob huntingJournalism booksComputing and the net booksfeaturesReuse this content","")
data = [[url,title,content]]
df = pd.DataFrame(data,columns=['url','title','content'])
df.to_csv("Scrapping_By_Ammad.csv")
