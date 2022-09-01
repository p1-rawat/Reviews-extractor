import pandas as pd
from bs4 import BeautifulSoup
import random
import requests

reviewlist = []

def getRandomProxy():
    pxy = {
        "http": f"xxxx-->paste Proxy<--xxxx:{9000 + random.randint(0, 9)}",
        "https": f"xxxx-->paste Proxy<--xxxx:{9000 + random.randint(0, 9)}"
    }
    return pxy
 
def totalPages(productUrl):
    resp = requests.get(productUrl, proxies=getRandomProxy())
    soup = BeautifulSoup(resp.text, 'html.parser')
    reviews = soup.find('div', {'data-hook':"cr-filter-info-review-rating-count"})
    return int(reviews.text.strip().split(', ')[1].split(" ")[0])

def extractReviews(reviewUrl, pageNumber):
    resp = requests.get(reviewUrl, proxies=getRandomProxy())
    soup = BeautifulSoup(resp.text, 'html.parser')
    reviews = soup.findAll('div', {'data-hook':"review"})
    for item in reviews:
        with open('html/file.html', 'w', encoding='utf-8') as f:
            f.write(str(item))
        
        '''
        review = {
            'productTitle': soup.title.text.replace("Amazon.in:Customer reviews: ", "").strip(),
            'Review Title': item.find('a', {'data-hook':"review-title"}).text.strip(),
            'Rating': item.find('i', {'data-hook': 'review-star-rating'}).text.strip(),
            'Review Body': item.find('span', {'data-hook': 'review-body'}).text.strip() ,
        }
        reviewlist.append(review) 
         
        '''

def main():
    productUrl = "xxxx-->paste Link<--xxxx"
    reviewUrl = productUrl.replace("dp", "product-reviews") + "?pageNumber=" + str(1)
    totalPg = totalPages(reviewUrl)
    print(totalPg)

    for i in range(totalPg//10):
        print(f"Running for page {i}")
        try: 
            reviewUrl = productUrl.replace("dp", "product-reviews") + "?pageNumber=" + str(i)
            extractReviews(reviewUrl, i)
        except Exception as e:
            print(e)
    
    '''
    df = pd.DataFrame(reviewlist)
    df.to_excel('output.xlsx', index=False)
    
    '''

main()