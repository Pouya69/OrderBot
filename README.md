# OrderBot
A simple Python bot that orders a product from BestBuy and Amazon ( Whichever is available first and worldwide ). PS5, XBOX series X,S, RTX 3000 series and more!

# Installation and Usage
IMPORTANT : You should have a BestBuy and an Amazon account already that the default address adn the default credit card is assigned.

First download or git clone the source code. Then download the selenium chrome web driver based on your operating system and replace r"src/chromedriver" in main.py file with your own chrome web driver in src folder and delete the previous one. ( Remember that the webdriver version should be the same as your Chrome browser version )
https://chromedriver.chromium.org/downloads

The second step is to install the requirements in the requirements.txt file using :
pip install -r requirements.txt
OR
pip3 install -r requirements.txt


The third step is assigning the product that you want! Go to Amazon and BestBuy and choose your product and copy the URL and replace the URLS with your own URLs in main.py

Also replace the AMAZON_EXPECTED_PRICES with your own expected prices for the product so that the bot will not buy stuff from the resellers.

The last step is changing the CVV to your own card's CVV for the final purchase.

If you have any problems or questions.. Go to the tutorial on the YouTube video for the demo and if you have any questions just comment.
https://youtu.be/4Ld1JAgRnis


NOTICE THAT THE BOT SOURCE CODE IS HERE. THE BOT JUST NEEDS YOUR INFO FOR THE PURCHASE AND NOTHING ELSE.. YOU CAN TAKE A LOOK AT IT YOURSELF.
I WON'T BE RESPONSIBLE FOR ANY BAD PURPOSES FOR THIS PROJECT.
