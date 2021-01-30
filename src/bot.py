from time import sleep
from playsound import playsound
from datetime import datetime


log_file = open("log.txt", "w+")
log_file.truncate(0)


class Bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


# BEST BUY Web Elements
ADD_TO_CART_BTN_VALUE_XPATH = "/html/body/div[1]/div/div[4]/div[1]/div[2]/div[2]/div[3]/div/div/div/form/button"
CHECKOUT_BTN_XPATH = "/html/body/div[1]/div/div[4]/div[2]/div[2]/section/div/section/section[2]/div[2]/div/a"


class BestBuyBot:
    def __init__(self, best_buy_product_url, cvv, driver_c):
        self.driver = driver_c
        self.driver.get("https://www.bestbuy.ca/")
        self.id = "BestBuy-ca"
        self.CVV = cvv
        self.BEST_BUY_PRODUCT_URL = best_buy_product_url
        print(f"[!] Your BestBuy specs by now :\nBestBuy Product URL : {self.BEST_BUY_PRODUCT_URL}\nCVV: {self.CVV}\n")

    def bestbuy_login(self):
        input(f"{Bcolors.UNDERLINE}Please login to your BestBuy account manually. When finished, just click enter here...{Bcolors.ENDC}")

    def goto_cart(self):
        self.driver.get("https://www.bestbuy.ca/en-ca/basket")
        sleep(2.8)
        while True:
            try:
                log_file.write(f"[{datetime.now().strftime('%H:%M:%S')}] [$] CLicking on Checkout")
                self.driver.find_element_by_xpath(CHECKOUT_BTN_XPATH).click()
                break
            except:
                sleep(1)
                log_file.write(f"[{datetime.now().strftime('%H:%M:%S')}] [$] CLicking on Checkout AGAIN")
        sleep(3.7)
        log_file.write(f"[{datetime.now().strftime('%H:%M:%S')}] [$] Sending CVV")
        while True:
            try:
                self.driver.find_element_by_id("cvv").send_keys(self.CVV)
                break
            except:
                sleep(1)
        self.driver.find_element_by_xpath("/html/body/div/div[5]/div[2]/div/div/div/section[2]/main/div[2]/section/section[1]/button").click()
        log_file.write(f"[{datetime.now().strftime('%H:%M:%S')}] [$$$$$$$$] BESTBUY DONE")

        print(f"[{datetime.now().strftime('%H:%M:%S')}] {Bcolors.OKGREEN}BOUGHT A PS5 FROM : {self.id}{Bcolors.ENDC}")
        return True

    def check_availability_and_buy(self):
        add_to_cart_btn = None
        self.driver.switch_to.window(self.driver.window_handles[0])
        available = False
        self.driver.get(self.BEST_BUY_PRODUCT_URL)
        sleep(3.6)
        try:
            add_to_cart_btn = self.driver.find_element_by_xpath(ADD_TO_CART_BTN_VALUE_XPATH)
        except:
            self.check_availability_and_buy()
        try:
            if add_to_cart_btn is not None:
                if add_to_cart_btn.is_enabled():
                    playsound('beep.mp3')
                    log_file.write(
                        f"[{datetime.now().strftime('%H:%M:%S')}] [$] PRODUCT IS AVAILABLE in BestBuy! Attempting to buy it..")
                    print(
                        f"[{datetime.now().strftime('%H:%M:%S')}] {Bcolors.OKGREEN}[$] PRODUCT IS AVAILABLE in BestBuy! Attempting to buy it..{Bcolors.ENDC}")
                    available = True
                if available:
                    add_to_cart_btn.click()
                    log_file.write(f"[{datetime.now().strftime('%H:%M:%S')}] [$] Clicked on add_to_cart")
                    sleep(2.7)
                    self.goto_cart()
                    return True
                else:
                    print(
                        f"[{datetime.now().strftime('%H:%M:%S')}] {Bcolors.FAIL}{self.id} :: OUT OF STOCK{Bcolors.ENDC}")
                    return False
            else:
                self.check_availability_and_buy()

        except:
            print(f"[{datetime.now().strftime('%H:%M:%S')}] {Bcolors.FAIL}{self.id} :: OUT OF STOCK{Bcolors.ENDC}")


class AmazonBot:
    def __init__(self, amazon_product_url, cvv, driver_c, expected_prices):
        self.driver = driver_c
        self.expected_prices = expected_prices
        self.driver.execute_script("window.open('');")
        self.driver.switch_to_window(self.driver.window_handles[1])
        self.driver.get("https://www.amazon.ca/")
        self.id = "Amazon-ca"
        self.CVV = cvv
        self.AMAZON_PRODUCT_URL = amazon_product_url
        print(f"[!] Your Amazon specs by now :\nBestBuy Product URL : {self.AMAZON_PRODUCT_URL}\nCVV: {self.CVV}\n")

    def amazon_login(self):
        input(f"{Bcolors.UNDERLINE}Please login to your Amazon account manually. When finished, just click enter here...{Bcolors.ENDC}")

    def goto_cart(self, num=0):
        self.driver.get("https://www.amazon.ca/gp/buy/spc/handlers/display.html?hasWorkingJavascript=1")
        done = False
        if num == 4:
            self.goto_cart(0)
        else:
            while True:
                try:
                    self.driver.find_element_by_name("placeYourOrder1").click()
                    done = True
                    break
                except:
                    self.goto_cart(num + 1)
                    sleep(1)
        if done is True:
            log_file.write(f"[{datetime.now().strftime('%H:%M:%S')}] [$$$$$$$$] Amazon DONE")

    def check_availability_and_buy(self):
        self.driver.switch_to_window(self.driver.window_handles[1])
        add_to_cart_btn = None
        final_price = 0.0
        self.driver.get(self.AMAZON_PRODUCT_URL)
        sleep(3.5)
        attt = 0
        while True:
            try:
                self.driver.find_element_by_id("productTitle")
                break
            except:
                if attt == 6:
                    self.check_availability_and_buy()
                attt += 1
                sleep(1)
        index = 0
        done_2 = False
        try:
            final_price_text = self.driver.find_element_by_id("price_inside_buybox").text
            temp = ""
            for letter in final_price_text:
                if letter == ".":
                    temp = temp + "."
                else:
                    try:
                        s = float(letter)
                        temp = temp + letter
                    except:
                        continue
            if not temp == "":
                final_price = float(temp)
                if final_price in self.expected_prices:
                    add_to_cart_btn = self.driver.find_element_by_id("add-to-cart-button")
                    done_2 = True
                else:
                    done_2 = False
                    for pps in self.expected_prices:
                        if final_price <= pps:
                            done_2 = True
                            break
            else:
                done_2 = False
            if done_2 is True:
                playsound('beep.mp3')
                log_file.write(f"[{datetime.now().strftime('%H:%M:%S')}] [$] PRODUCT IS AVAILABLE in Amazon! Attempting to buy it..")
                print(f"[{datetime.now().strftime('%H:%M:%S')}] {Bcolors.OKGREEN}[$] PRODUCT IS AVAILABLE in Amazon! Attempting to buy it..{Bcolors.ENDC}")
        except:
            try:
                self.driver.find_element_by_id("buybox-see-all-buying-choices-announce").click()
                sleep(1.8)
                prices = self.driver.find_elements_by_class_name("a-price-whole")
                for price in prices:
                    tt = price.text
                    tt = tt.replace(",", "")
                    p = float(tt)
                    if p in self.expected_prices:
                        final_price = p
                        add_to_cart_btn = self.driver.find_elements_by_name("submit.addToCart")[index]
                        playsound('beep.mp3')
                        log_file.write(f"[{datetime.now().strftime('%H:%M:%S')}] [$] PRODUCT IS AVAILABLE in Amazon! Attempting to buy it..")
                        print(f"[{datetime.now().strftime('%H:%M:%S')}] {Bcolors.OKGREEN}[$] PRODUCT IS AVAILABLE in Amazon! Attempting to buy it..{Bcolors.ENDC}")
                    else:
                        for po in self.expected_prices:
                            if p <= po:
                                add_to_cart_btn = self.driver.find_elements_by_name("submit.addToCart")[index]
                                playsound('beep.mp3')
                                log_file.write(
                                    f"[{datetime.now().strftime('%H:%M:%S')}] [$] PRODUCT IS AVAILABLE in Amazon! Attempting to buy it..")
                                print(
                                    f"[{datetime.now().strftime('%H:%M:%S')}] {Bcolors.OKGREEN}[$] PRODUCT IS AVAILABLE in Amazon! Attempting to buy it..{Bcolors.ENDC}")
                                break
                    index += 1
            except:
                add_to_cart_btn = None
        if add_to_cart_btn is not None:
            while True:
                try:
                    log_file.write(f"[{datetime.now().strftime('%H:%M:%S')}] [$] Clicking on Add to cart Amazon")
                    add_to_cart_btn.click()
                    break
                except:
                    log_file.write(f"[{datetime.now().strftime('%H:%M:%S')}] [$] Clicking on Add to cart Amazon TRYING AGAIN")
                    sleep(1)
            sleep(2)
            ll = 0
            done_1 = False
            while True:
                if ll == 4:
                    self.check_availability_and_buy()
                else:
                    try:
                        log_file.write(f"[{datetime.now().strftime('%H:%M:%S')}] [$] Clicking on Checkout cart Amazon")
                        self.driver.find_element_by_id("hlb-ptc-btn-native").click()
                        done_1 = True
                        break
                    except:
                        ll += 1
                        sleep(1)
                        log_file.write(f"[{datetime.now().strftime('%H:%M:%S')}] [$] Clicking on Checkout Amazon TRYING AGAIN")
            if done_1 is False:
                return False
            sleep(2.5)
            oo = 0
            done = False
            while True:
                if oo == 4:
                    self.goto_cart()
                else:
                    try:
                        self.driver.find_element_by_name("placeYourOrder1").click()
                        done = True
                        break
                    except:
                        oo += 1
                        sleep(1)
            if done is True:
                log_file.write(f"[{datetime.now().strftime('%H:%M:%S')}] [$$$$$$$$] Amazon DONE")
                print(f"[{datetime.now().strftime('%H:%M:%S')}] {Bcolors.OKGREEN}BOUGHT A PS5 FROM : {self.id}{Bcolors.ENDC}")
                return True
            else:
                return False
        else:
            print(f"[{datetime.now().strftime('%H:%M:%S')}] {Bcolors.FAIL}{self.id} :: OUT OF STOCK{Bcolors.ENDC}")
            return False
