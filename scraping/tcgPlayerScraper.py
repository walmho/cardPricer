from bs4 import BeautifulSoup as bs
import time

def getPage(setName):
    """ Access tcgplayer.com card dataset from specific release
    
        Args:
            setName (str): Specific set release to access

        Returns:
            driver (WebElement): webdriver being used
    """

    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(options=options)
    link =f"""
    https://www.tcgplayer.com/search/pokemon/{setName}?
    =grid&productLineName=pokemon&setName={setName}
    """
    driver.get(link)
    driver.fullscreen_window()
    time.sleep(5)
    return driver

def findAll(driver, className):
    """ find all elements on driver's page
    
        Args:
            driver (WebElement): webdriver being used
            className (str): html class name to find

        Returns:
            element (list): all elements found
            
    """

    element = driver.find_elements(By.CLASS_NAME, className)
    return element

def screenshotAll(driver, images, fileLocation):
    """ take screenshots of all image elements
    
        Args:
            driver (WebElement): webdriver being used
            images (list): all image elements
            fileLocation (str): local location to save images to

        Returns:
            saves .png image screenshots to fileLocation
            imageKey (list): list of all image names, in order
            
    """
    imageKey = []
    for i in range(len(images)):
        driver.execute_script('arguments[0].scrollIntoView({block: "center"});', images[i])
        images[i].screenshot(f"{fileLocation}\\training_{i+1}.png")
        imageKey.append(f"training_{i+1}.png")

    driver.quit()
    return imageKey

def nameAll(names):
    """ extract text values out of webelement names
    
        Args:
            names (list): list of html elements found

        Returns:
            nameList (list): list of text within each element
            
    """

    nameList = []
    for i in range(len(names)):
        nameList.append(names[i].text)

    print(nameList)
    return nameList

def loadPairs(names, imageKey):
    """ turn name and image lists into dict
    
        Args:
            names (list): list of card names
            imageKey (list): list of image names

        Returns:
            element (list): all elements found
            
    """
    answers = dict(zip(names, imageKey))
    return answers