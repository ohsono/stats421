import requests

urls = {
    "Freddie Mac (Archive)": "https://www.freddiemac.com/pmms/pmms_archives/PMMS_averages_since_1971.csv",
    "Zillow Price Cuts (Original)": "https://files.zillowstatic.com/research/public_csvs/pct_listings_price_cut/Metro_pct_listings_price_cut_uc_sfrcondo_month.csv",
    "Zillow Variation 1 (Smoothed)": "https://files.zillowstatic.com/research/public_csvs/pct_listings_price_cut/Metro_pct_listings_price_cut_uc_sfrcondo_sm_month.csv",
    "Zillow Variation 2 (SA)": "https://files.zillowstatic.com/research/public_csvs/pct_listings_price_cut/Metro_pct_listings_price_cut_uc_sfrcondo_sa_month.csv",
    "Zillow Variation 3 (SFR only)": "https://files.zillowstatic.com/research/public_csvs/pct_listings_price_cut/Metro_pct_listings_price_cut_uc_sfr_month.csv",
    "Zillow Variation 4 (Weekly)": "https://files.zillowstatic.com/research/public_csvs/pct_listings_price_cut/Metro_pct_listings_price_cut_uc_sfrcondo_week.csv"
}

for name, url in urls.items():
    try:
        print(f"Checking {name}...")
        response = requests.head(url, timeout=10, allow_redirects=True)
        print(f"  Status: {response.status_code}")
        if response.status_code == 404:
            print("  Result: BROKEN (404)")
        elif response.status_code == 200:
            print("  Result: OK")
        else:
            print(f"  Result: Other ({response.status_code})")
    except Exception as e:
        print(f"  Error: {e}")
