from selenium import webdriver
import time

driver = webdriver.Chrome()

def openSite(amount, chapter):
	driver.get('https://pixabay.com/' + chapter + '/search/?order=ec')
	resultImg, resultURL = toGetToSitePhotos(amount, chapter)
	return resultImg, resultURL


def toGetToSitePhotos(amount, chapter):

	# Count veriables
	i = 0
	q = 0
	z = 0

	all_urls = [None] * amount
	imageElementsMain = [None] * amount
	time.sleep(2.5)
	imageElements = driver.find_elements_by_class_name('link--h3bPW')

	while i < amount:

		all_urls[i] = imageElements[i].get_attribute('href')
		i += 1

	for url in all_urls:

		try:
			driver.get(url)
			imageElementsMain[q] = driver.find_element_by_tag_name('img').get_attribute('src')
			imageElementsMain[q]
		except:
			#driver.close()
			return imageElementsMain, all_urls

		q += 1

	#driver.close()
	#print (imageElementsMain)
	#print (all_urls)
	return imageElementsMain, all_urls

if __name__ == '__main__':

	resultImg, resultURL = openSite(10, 'photos')
