from usta_scrapers import scrape_uaid

def main():
    player_name = "Lucy%20Sanders"
    uaid = scrape_uaid(player_name)
    print(uaid)

if __name__ == "__main__":
    main()