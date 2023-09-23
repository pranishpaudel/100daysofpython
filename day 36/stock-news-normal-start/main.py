import requests
from datetime import datetime as dt
from itertools import islice


CURRENT_DAY= dt.now().day
STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
NEWS_API= "548382078a5a4ac59a0c27cafb2054f0"
STOCK_API= "JATXMDCUYLSXJTC8"

# STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

stock_params = {
    "apikey": STOCK_API,
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
}

stock_req = requests.get(STOCK_ENDPOINT, stock_params)
stock_req_json = stock_req.json()["Time Series (Daily)"]


def extract_closing_price(RAW_DAY):
    if len(str(RAW_DAY))<2:
        RAW_DAY= f"0{RAW_DAY}"
    closing_price= stock_req_json[f"2023-09-{RAW_DAY}"]["4. close"]
    return closing_price



# # TODO 1. - Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g. [new_value for (key, value) in dictionary.items()]
yesterday_closing_price= int(float(extract_closing_price(CURRENT_DAY-1)))




# # TODO 2. - Get the day before yesterday's closing stock price
day_before_yesterday_closing_price= int(float(extract_closing_price(CURRENT_DAY-3)))

# # TODO 3. - Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp
# difference_closing= yesterday_closing_price - day_before_yesterday_closing_price
diff_closing= yesterday_closing_price- day_before_yesterday_closing_price

# # TODO 4. - Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.
def calculate_percentage_difference(value1, value2):
    # Calculate the percentage difference
    percentage_difference = abs((value1 - value2) / ((value1 + value2) / 2)) * 100
    return int(percentage_difference)

diff_per_closing= calculate_percentage_difference(yesterday_closing_price,day_before_yesterday_closing_price )

if diff_closing<0:
    diff_per_emoji= f"🔻{diff_per_closing}%"
else:
    diff_per_emoji= f"🔺{diff_per_closing}%"
    

# # TODO 5. - If TODO4 percentage is greater than 5 then print("Get News").
if diff_per_closing>5:
        news_req = requests.get(f"https://newsapi.org/v2/everything?q=tesla&from=2023-08-23&sortBy=publishedAt&apiKey={NEWS_API}").json()["articles"]
        news_list= []
        for num in range(1,4):
         news_list.append(news_req[:num])
 
        news_title_list= []
        news_description_list= []

        for num in range (0,3):
            news_title_list.append(news_list[num][num]['title'])
            news_description_list.append(news_list[num][num]['description'])

        final_message= f"{COMPANY_NAME}:{diff_per_emoji}\n Headline: {news_title_list[2]} \n Description: {news_description_list[2]} "
else:
    print(f"Less than 5 : {diff_per_closing}")


print(final_message)
print(news_title_list[2])


# # STEP 2: https://newsapi.org/
# # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.




# # 6. - Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.

# # 7. - Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation

# # STEP 3: Use twilio.com/docs/sms/quickstart/python
# # to send a separate message with each article's title and description to your phone number.

# # 8. - Create a new list of the first 3 article's headline and description using list comprehension.

# # 9. - Send each article as a separate message via Twilio.

# # Optional: Format the message like this:
# """
# TSLA: 🔺2%
# Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?.
# Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
# or
# "TSLA: 🔻5%
# Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?.
# Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
# """
