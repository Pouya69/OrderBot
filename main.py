from playsound import playsound
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from src.bot import BestBuyBot, AmazonBot, MicrosoftBot


CVV = "957"
#Microsoft Password
PASSWORD = ""
# This is the URL of the products
BEST_BUY_PRODUCT_URL = "https://www.bestbuy.ca/en-ca/product/playstation-5-digital-edition-console-online-only/14962184"
AMAZON_PRODUCT_URL = "https://www.amazon.ca/Playstation-3005721-PlayStation-Digital-Edition/dp/B08GS1N24H"
#Xbox Series X Halo Infinite Console
MICROSOFT_PRODUCT_URL = "https://www.xbox.com/en-us/configure/8RPM8T9CK0P6?ranMID=24542&ranEAID=AKGBlS8SPlM&ranSiteID=AKGBlS8SPlM-xudy84QJWx1blRDEoUU_Mg&epi=AKGBlS8SPlM-xudy84QJWx1blRDEoUU_Mg&irgwc=1&OCID=AID2200057_aff_7593_1243925&tduid=%28ir__nxpdxmc0tgkf6nvysnvndaaqq22xowa6bgpcqyhc00%29%287593%29%281243925%29%28AKGBlS8SPlM-xudy84QJWx1blRDEoUU_Mg%29%28%29&irclickid=_nxpdxmc0tgkf6nvysnvndaaqq22xowa6bgpcqyhc00"

# This is the expected prices of the product. ( For avoiding resellers)
AMAZON_EXPECTED_PRICES = [499.99, 529.99, 539.99, 519.99]


def check_availability_all(bots):
    done = False
    while done is False:
        for bot in bots:
            result = bot.check_availability_and_buy()
            if result is True:
                done = True
                print("WOOOOOOOOOOOHOOOOOOOOOOOOOO!!!!!!!!!!!!!!!!")
                break
    for _ in range(100):
        playsound(r'src/beep.mp3')
    input("....")
    exit(0)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # Setting up the driver
    print("Hey! I am the Automatic Order Bot! BestBuy, Amazon. Let's get started..\n")
    opts = Options()
    opts.add_argument("--remote-debugging-port=9222")
    EXEC_PATH = r"src/chromedriver"
    DRIVER = webdriver.Chrome(executable_path=EXEC_PATH, options=opts)

    best_buy_bot = BestBuyBot(BEST_BUY_PRODUCT_URL, CVV, DRIVER)
    bots_c = [best_buy_bot]
    best_buy_bot.bestbuy_login()
    amazon_bot = AmazonBot(AMAZON_PRODUCT_URL, CVV, DRIVER, AMAZON_EXPECTED_PRICES)
    amazon_bot.amazon_login()
    bots_c.append(amazon_bot)
    microsoft_bot = MicrosoftBot(MICROSOFT_PRODUCT_URL, PASSWORD, DRIVER)
    microsoft_bot.microsoft_login()
    bots_c.append(microsoft_bot)
    check_availability_all(bots_c)





