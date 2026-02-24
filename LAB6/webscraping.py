# import requests
# from bs4 import BeautifulSoup

# url = 'https://www.google.com'

# headers = {
#     "User-Agent": "Mozilla/5.0"
# }

# response = requests.get(url, headers=headers)

# if response.status_code == 200:
#     soup = BeautifulSoup(response.text, 'html.parser')
#     headings = soup.find_all('div')

#     for heading in headings:
#         print(heading.text.strip())

#     print('Web scraping is done')
# else:
#     print('Failed to retrieve the web page')


import requests
from bs4 import BeautifulSoup

# url = 'https://www.flipkart.com/search?q=power+bank'

# headers = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
# }

# response = requests.get(url, headers=headers)

# if response.status_code != 200:
#     print("Failed to load the page")
#     exit()

# soup = BeautifulSoup(response.text, 'html.parser')

# products = []

# for card in soup.find_all('div', class_='_1AtVbE'):

#     title_tag = card.find('div', class_='_4rR01T')
#     price_tag = card.find('div', class_='_30jeq3')
#     rating_tag = card.find('div', class_='_3LWZlK')

#     if title_tag and price_tag:
#         products.append({
#             'title': title_tag.text.strip(),
#             'price': price_tag.text.strip(),
#             'rating': rating_tag.text.strip() if rating_tag else "No Rating"
#         })

# for product in products:
#     print(product)

url = 'https://webscraper.io/test-sites/e-commerce/allinone/computers'
# response = requests.get(url)
# soup = BeautifulSoup(response.text, 'html.parser')
# products = []
# for card in soup.find_all('div', class_='product-wrapper'):
#     title = card.find('a', class_='title').text.strip()
#     description = card.find('p', class_='description').text.strip()
#     price = card.find('h4', class_='price').text.strip()
#     rating = len(card.find('div', class_='ratings').find_all('span',
#                                                              class_='ws-icon-star'))
#     # reviews = card.find('p', class_='review-count').text.strip().split('')[0]
# products.append({
#     'title': title,
#     'description': description,
#     'price': price,
#     'rating': rating,
#     # 'reviews': reviews
# })
# for product in products:
#     print(product)

html_content = """
<div>
<div>
<div>
<img src="/path/to/image1.png">
<div>
<h4>$107.99</h4>
<h4>Galaxy Tab 3</h4>
<p>7", 8GB, Wi-Fi, Android 4.2, Yellow</p>
</div>
<div>
<p>14 reviews</p>
<p>Rating: ★★★☆☆</p>
</div>
</div>
</div>
<div>
<div>
<img src="/path/to/image2.png">
<div>
<h4>$50.01</h4>
<h4>Second I phone</h4>
<p>Blue night</p>
</div>
<div>
<p>10 reviews</p>
<p>Rating: ★★☆☆☆</p>
</div>
</div>
</div>
</div>
"""
soup = BeautifulSoup(html_content, 'html.parser')
products = []
for div in soup.div.find_all('div', recursive=False):
    img_src = div.div.img['src']
    price = div.div.find_next('h4').text
    title = div.div.find_next('h4').find_next_sibling('h4').text
    description = div.div.find('p').text
    reviews = div.div.find_all('p')[1].text.split(' ')[0]
    rating = div.div.find_all('p')[2].text.count('★')
products.append({
    'img_src': img_src,
    'price': price,
    'title': title,
    'description': description,
    'reviews': reviews,
    'rating': rating
})
for product in products:
    print(product)
