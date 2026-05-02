#!/usr/bin/env python3
import requests
import os
from pathlib import Path

SESSION = "53616c7465645f5fe10776a8740560a6b947277cc239a30299a016bd5421a6169629b7c374daeb1ea2d75b7c7ecc0c26dcd29a30b73c67764904ad0fdbc29965"
YEAR = 2024
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:148.0) Gecko/20100101 Firefox/148.0",
    "Cookie": f"session={SESSION}"
}

for day in range(1, 26):
    dir_name = f"{day}_day"
    Path(dir_name).mkdir(exist_ok=True)
    
    # Scrape problem HTML
    problem_url = f"https://adventofcode.com/{YEAR}/day/{day}"
    resp = requests.get(problem_url, headers=HEADERS)
    if resp.status_code == 200:
        with open(f"{dir_name}/problem.html", "w") as f:
            f.write(resp.text)
        print(f"Day {day}: problem saved")
    else:
        print(f"Day {day}: problem failed ({resp.status_code})")
    
    # Scrape input
    input_url = f"https://adventofcode.com/{YEAR}/day/{day}/input"
    resp = requests.get(input_url, headers=HEADERS)
    if resp.status_code == 200:
        with open(f"{dir_name}/input.txt", "w") as f:
            f.write(resp.text)
        print(f"Day {day}: input saved")
    else:
        print(f"Day {day}: input failed ({resp.status_code})")
