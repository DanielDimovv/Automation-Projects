from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time




chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

EMAIL, PASSWD = "email", "password"


def log_id(scrolls):
    driver.get("https://www.strava.com/")
    
    time.sleep(5)
    driver.find_element(By.CSS_SELECTOR,
                        'a.Footer_highlight__zd8_L').click()
    time.sleep(25)

    driver.find_element(By.ID, "email").send_keys(EMAIL)
    driver.find_element(By.ID, "password").send_keys(PASSWD)
    driver.find_element(By.ID, "login-button").click()
    for i in range(0, scrolls):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(5)


def clik_like_buttons():
    counter = 0
    direct_divs = driver.find_elements(By.CSS_SELECTOR, ".feed-ui > div")

    for i, div in enumerate(direct_divs):
        try:
            kudos_button = div.find_element(By.CSS_SELECTOR, 'button[title="Give kudos"]')
            print(kudos_button.text)
        except NoSuchElementException:
            print("Error")
            continue
        else:
            title = kudos_button.get_attribute("data-testid")
            print(title)
            time.sleep(1)
            if title == "filled_kudos":
                continue
            else:
                kudos_button.click()
                counter += 1
                print(f"Number of clicked buttons {counter}")
        finally:
            continue


def main():
    log_id(10)
    clik_like_buttons()


if __name__ == "__main__":
    main()
