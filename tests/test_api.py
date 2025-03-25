import requests
import pytest

API_URL = "https://www.szse.cn/api/market/ssjjhq/getTimeData"
PARAMS = {
    "random": "0.7088729318306961",
    "marketId": "1",
    "code": "000001",
    "language": "EN"
}
HEADERS = {
    # "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36",
    # "Accept": "application/json, text/javascript, */*; q=0.01",
    "Content-Type": "application/json",
    # "X-Requested-With": "XMLHttpRequest"
}

def test_market_data():
    print("Step 1: Sending API request...🚀")
    response = requests.get(API_URL, params=PARAMS, headers=HEADERS)
    
    print("Step 2: Checking response status code...")
    assert response.status_code == 200, f"API request failed: {response.status_code}"
    print(f"✅ Status code {response.status_code} is OK.")

    print("Step 3: Parsing JSON response...")
    data = response.json()
    print("✅ JSON response parsed successfully.")

    print("Step 4: Checking if 'data' field exists in response...")
    assert "data" in data, "Response does not contain 'data' field"
    market_data = data["data"]
    print("✅ 'data' field found.")

    print("Step 5: Checking if 'high' and 'low' fields exist in market data...")
    assert "high" in market_data and "low" in market_data, "Response does not contain 'high' or 'low' fields"
    print("✅ 'high' and 'low' fields found.")

    print("Step 6: Validating market data (high > low)...")
    high = float(market_data["high"])
    low = float(market_data["low"])
    assert high > low, f"Invalid market data: High ({high}) is not greater than Low ({low})"
    print(f"✅ Market data is valid: High ({high}) > Low ({low})")