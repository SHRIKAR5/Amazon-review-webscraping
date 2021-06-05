import pandas as pd 
import requests
from bs4 import BeautifulSoup


u = 'https://www.amazon.in/OnePlus-Nord-Gray-128GB-Storage/product-reviews/B08695ZSP6/ref=cm_cr_arp_d_paging_btm_next_2?ie=UTF8&reviewerType=all_reviews&pageNumber='

def amazon(link,Number_of_pages):
    r={}
    allreview1 = pd.DataFrame(r)
    name=[]
    body = []
    star_rating = []
    review = []
    urls=[]    
    for i in range(1,Number_of_pages+1):
        i=str(i)
        a=u+i
        urls.append(a)
 
    for i in urls:
        data = requests.get(i)
        data
        data.content
        soup = BeautifulSoup(data.content,'html.parser')
        soup.title
        # if any tag i.e.div, a,span,i,etc has class  use it in soup.findAll 
        # div is not compulsory always 
        #if span doec not has itemprop use parent class (could be a, div, span,i, etc)
        
        name1 = soup.findAll('div', class_=['a-profile-content'])
        ct=0
        for i in name1:
            if ct>=2:
                name.append(i.find('span', class_=['a-profile-name']).text)
            ct+=1
        
        
        title1 = soup.findAll('a', attrs={'data-hook' : 'review-title'}, class_=['a-size-base a-link-normal review-title a-color-base review-title-content a-text-bold'])
        for i in title1:
            review.append(i.find('span').text)
       
        
        rating = soup.findAll('i', attrs={'data-hook' : 'review-star-rating'}) 
        for i in rating:
            star_rating.append(i.find('span', class_=['a-icon-alt']).text) 
            
            
        body1 = soup.findAll('span', attrs={'data-hook' : 'review-body'},class_=['a-size-base review-text review-text-content'])
        for i in body1:
            body.append(i.find('span').text)    
    
    allreview1['name'] = name
    allreview1['review'] = review
    allreview1['star_rating'] = star_rating
    allreview1['body'] = body
    
    allreview1.to_csv(r'C:\...\allreview1.csv')
    


amazon(u,3)








