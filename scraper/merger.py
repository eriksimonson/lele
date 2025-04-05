import requests
import json
import time
import os
import difflib

INPUT_FILE = "input.json"
OUTPUT_FILE = "output.json"
MAX_RETRIES = 3
FAILURE_LOG = "failures.log"

USER_INPUT_KEYWORDS = {
    "Word": ["word", "guess", "letters", "anagram", "spelling", "unscramble"],
    "Number": ["number", "math", "digits", "equation", "add", "subtract"],
    "Letter": ["letter", "alphabet", "char", "character"],
    "Multiple Choice": ["multiple choice", "options", "pick one", "select"],
    "Pick": ["choose", "pick", "click", "select"],
    "Mixed": ["mixed", "combo", "variety"],
}
FUZZY_THRESHOLD = 0.8  # 80% similarity

def infer_user_input_type(tags, description):
    combined = " ".join(tags).lower() + " " + description.lower()

    # Step 1: Exact keyword match
    for input_type, keywords in USER_INPUT_KEYWORDS.items():
        for kw in keywords:
            if kw in combined:
                return input_type

    # Step 2: Fuzzy match
    words = combined.split()
    all_keywords = [(kw, input_type) for input_type, kws in USER_INPUT_KEYWORDS.items() for kw in kws]

    for word in words:
        close_matches = difflib.get_close_matches(word, [kw for kw, _ in all_keywords], n=1, cutoff=FUZZY_THRESHOLD)
        if close_matches:
            match = close_matches[0]
            for kw, input_type in all_keywords:
                if kw == match:
                    return input_type

    return "Unknown"

def get_first_year_from_wayback(url):
    cdx_api = "http://web.archive.org/cdx/search/cdx"
    params = {
        'url': url,
        'output': 'json',
        'fl': 'timestamp',
        'limit': 1,
        'from': '2000',
        'collapse': 'timestamp:8',
        'filter': 'statuscode:200',
        'sort': 'ascending'
    }

    try:
        response = requests.get(cdx_api, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()
        if len(data) > 1:
            timestamp = data[1][0]
            return timestamp[:4]
    except Exception as e:
        print(f"[!] Error fetching year for {url}: {e}")
    return "Unknown"

def update_unknown_years(data):
    updated = data.copy()

    for name, game in data.items():

        current_year = game.get("releaseYear", "Unknown")
        if current_year == "Unknown":
            url = game.get("website")
            retries = 0
            new_year = "Unknown"

            while retries < MAX_RETRIES:
                new_year = get_first_year_from_wayback(url)
                if new_year != "Unknown":
                    break
                retries += 1
                print(f"[!] Retry {retries}/{MAX_RETRIES} for {name} in 20s...")
                time.sleep(20)

            if new_year == "Unknown":
                print(f"❌ Failed to fetch year for {name} after {MAX_RETRIES} retries.")
                with open(FAILURE_LOG, "a", encoding="utf-8") as log:
                    log.write(f"{name} | {url}\n")
            else:
                print(f"🔄 Updated {name}: {new_year}")

            game["releaseYear"] = new_year
            updated[name] = game

            # Save after every attempt
            with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
                json.dump(updated, f, indent=2)

            time.sleep(1)  # Be nice to Wayback

        else:
            print(f"✅ Skipped {name}: already has year {current_year}")
            updated[name] = game

    return updated

def update_unknown_user_input(data):
    updated = data.copy()

    for name, game in data.items():
        if game.get("userInput") == "Unknown" or not game.get("userInput"):
            tags = game.get("tags", [])
            desc = game.get("description", "")
            inferred = infer_user_input_type(tags, desc)
            game["userInput"] = inferred
            print(f"🔍 {name} → {inferred}")
            
            # Save after every attempt
            with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
                json.dump(updated, f, indent=2)
            # time.sleep(1)  # Respectful delay

    return updated

def main():
    if not os.path.exists(INPUT_FILE):
        print(f"❌ Input file '{INPUT_FILE}' not found.")
        return

    with open(INPUT_FILE, "r", encoding="utf-8") as infile:
        data = json.load(infile)

    # First update the years
    updated_data = update_unknown_years(data)
    
    # Then update the user input types
    updated_data = update_unknown_user_input(updated_data)

    with open(OUTPUT_FILE, "w", encoding="utf-8") as outfile:
        json.dump(updated_data, outfile, indent=2)
        print(f"\n✅ Updated data written to '{OUTPUT_FILE}'")

if __name__ == "__main__":
    main()
