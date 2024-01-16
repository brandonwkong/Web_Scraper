import requests
from bs4 import BeautifulSoup
#Danireon
search = "pokemon elite trainer box"
base_url = f"https://www.danireon.com/collections/{search.replace(' ', '-')}"
cheapest_set= 0
cheapest_price = 1000.00
page_counter = 1
while True:
    url = f"{base_url}?page={page_counter}"
    page = requests.get(url)
    
    # Check if the page exists
    if page.status_code == 404:
        #print(f"Page {page_counter} not found. Exiting the loop.")
        break

    soup = BeautifulSoup(page.content, "html.parser")
    result = soup.find(id="shopify-section-template--16972069798123__main")
    price_elements = soup.find_all("div", class_="product-block__inner")
    if not price_elements:
            #print(f"No items found on page {page_counter}. Exiting the loop.")
            break
    for price in price_elements:
        product_name = price.find("a", class_="title").text.strip()
        product_price =price.find("span", class_="amount theme-money").text.strip()
        final_price = ''.join(char for char in product_price if char.isdigit() or char == '.')
        final_price = float(final_price)
        if final_price < cheapest_price:
             cheapest_price = final_price
             cheapest_set = product_name
    #print(f"{cheapest_set} is the cheapest at {cheapest_price}!")
    page_counter+=1



    
cheapestTitle = "none"
cheapestPrice = 10000.0

pageNum = 1
URL = f"https://kanzengames.com/collections/pokemon-elite-trainer-box?page={pageNum}"

#checks each page of products, checking if page has any grid element (product):
while(len(BeautifulSoup(requests.get(URL).content, "html.parser").find(id="shopify-section-template--16751113961687__content").find_all("div", class_="productCard__card")) > 0):
    #if page has products, output the product info:
    #print(f"Page: {pageNum}")
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    grid = soup.find(id="shopify-section-template--16751113961687__content")
    product_elements = grid.find_all("div", class_="productCard__card")
    #iterating through each product on page:
    for product_element in product_elements:
        title_element = product_element.find("p", class_="productCard__title").text.strip()
        price_element = product_element.find("p", class_="productCard__price")
        #accounting for if there is sale price:
        if(price_element.find("strong") == None):
            price_element = price_element.text
        else:
            price_element = price_element.find("strong").text
        price_element = float(price_element.replace("CAD","").replace("$","").replace(",","").strip())
        if(price_element < cheapestPrice):
            cheapestPrice = price_element
            cheapestTitle = title_element
    #next page iteration
    pageNum += 1
    URL = f"https://kanzengames.com/collections/pokemon-elite-trainer-box?page={pageNum}"

#print(f"The cheapest product is {cheapestTitle} for ${cheapestPrice} CAD")
    
if cheapestPrice < cheapest_price:
     print(f"The cheapest product is {cheapestTitle} for ${cheapestPrice} CAD!")
else:
     print(f"The cheapest product is{cheapest_set} for ${cheapest_price} CAD!")


