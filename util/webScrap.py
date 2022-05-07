import requests

from bs4 import BeautifulSoup


def getProductTitle(soup):
    return soup.find("span", class_="a-size-large product-title-word-break").text


def getAmountFromAmazonProduct(productUrl):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:94.0) Gecko/20100101 Firefox/94.0',
        'Accept-Language': 'en-US, en;q=0.5'
    }
    source = requests.get(
        productUrl,
        headers=headers)
    soup = BeautifulSoup(source.content, "html.parser")
    # rejectedList = soup.findAll("p", class_="a-last") isRejected = rejectedList != [] and rejectedList[ 0].text ==
    # "Sorry, we just need to make sure you're not a robot. For best results, please make sure your browser is
    # accepting cookies.";
    print(productUrl)
    productPrice = getProductPrice(soup)
    productTitle = getProductTitle(soup).strip()
    print(productPrice)
    return productTitle + " :: " + productPrice.text[1:]


def getProductPrice(soup):
    productPriceDetails = soup.find_all("span", class_="a-price a-text-price a-size-medium apexPriceToPay")
    return productPriceDetails[0].find("span", class_="a-offscreen")
