# Housing Market Data Analysis: CA to TX Migration & Investment Opportunities

Complete data pipeline for analyzing housing market trends, migration patterns, and identifying investment opportunities for 2026.

> [!NOTE]
> **Development Status:** Check [DEV_LOG.md](DEV_LOG.md) for the latest findings, debug logs, and current focus.

## 📊 Project Overview

This project provides tools to:

- Download housing market datasets from multiple authoritative sources
- Analyze CA to TX migration patterns and ROI opportunities
- Identify emerging hot housing markets for 2026 investment
- Clean, merge, and prepare data for advanced analytics

## 🎯 Key Features

- **Automated data downloads** from Zillow, Census Bureau, BLS, and FHFA
- **Comprehensive metro coverage** including CA, TX, and emerging markets
- **Time series data** from 2020-2025 for trend analysis
- **Employment & salary data** to correlate with housing demand
- **Migration flow tracking** to identify population movements
- **ROI calculation framework** for investment decision-making

## 📁 Project Structure

```
housing-market-analysis/
├── housing_data_downloader.py    # Main data download script
├── bls_api_downloader.py         # BLS API-specific downloader
├── data_cleaner.py               # Data cleaning & merging script
├── ca_county_cleaner.py          # CA county-specific cleaner
├── tx_county_cleaner.py          # TX county-specific cleaner
├── feature_engineer.py           # Feature engineering script
├── requirements.txt               # Python dependencies
├── README.md                      # This file
└── housing_market_data/           # Downloaded data (created on first run)
    ├── zillow/                    # Zillow Research Data
    ├── census/                    # Census Bureau data
    ├── bls/                       # BLS employment & wage data
    ├── other/                     # FHFA, Freddie Mac, etc.
    └── metro_reference.csv        # Metro area reference codes
```

## 🚀 Quick Start

### 1. Install Dependencies

```bash
# Create virtual environment (recommended)
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install required packages
pip install -r requirements.txt
```

### 2. Download Data

```bash
# Run main downloader (downloads most datasets automatically)
python housing_data_downloader.py
```

This will download:

- ✅ Zillow ZHVI (Home Values) - Metro, County, ZIP levels
- ✅ Zillow Rental Index (ZORI)
- ✅ Inventory metrics
- ✅ Days on market
- ✅ Sales counts
- ✅ FHFA House Price Index
- ✅ Census population estimates

**Manual Downloads Required:**

- **Zillow Price Cuts**: Download `Metro_perc_listings_price_cut_uc_sfrcondo_month.csv` manually (URL in script output) and save to `housing_market_data/zillow/price_cuts_metro.csv`.
- **Freddie Mac Rates**: Download `PMMS_averages_since_1971.csv` manually (URL in script output) and save to `housing_market_data/other/freddie_mac_rates.csv`.
- **Census Migration Flows**: Download `county-to-county-migration-flows.csv` manually and save to `housing_market_data/census/migration_flows.csv`.

### 3. Verify Data Quality

```bash
# Run verification script
python verify_data.py
```

This script checks for missing files, validates CSV formats, and reports data completeness.

### 4. Clean and Merge Data

```bash
# Run data cleaner
python data_cleaner.py
```

This script:

- Standardizes Zillow, Census, and BLS data formats
- Merges datasets into a master file
- Handles missing values and aligns dates

### 5. Download BLS Data (Optional but Recommended)

**Option A: Manual Download (No API Key Required)**

1. Visit <https://www.bls.gov/cew/downloadable-data-files.htm>
2. Download County High-Level CSVs for recent quarters
3. Save to `housing_market_data/bls/qcew/`

**Option B: API Access (Recommended)**

1. Register for free API key: <https://www.bls.gov/developers/home.htm>
2. Set environment variable:

   ```bash
   export BLS_API_KEY='your-api-key-here'
   ```

3. Run BLS downloader:

   ```bash
   python bls_api_downloader.py
   ```

## 📊 Data Sources

### Zillow Research Data

- **URL**: <https://www.zillow.com/research/data/>
- **Coverage**: National, Metro, County, ZIP
- **Frequency**: Monthly updates
- **Metrics**: Home values, rents, inventory, sales

### U.S. Census Bureau

- **URL**: <https://www.census.gov/data.html>
- **Coverage**: National, State, County
- **Frequency**: Annual (ACS), Quarterly (Population)
- **Metrics**: Population, migration flows, demographics, building permits

### Bureau of Labor Statistics (BLS)

- **URL**: <https://www.bls.gov/data/>
- **Coverage**: National, State, Metro, County
- **Frequency**: Monthly/Quarterly
- **Metrics**: Employment, wages, unemployment rates

### FHFA (Federal Housing Finance Agency)

- **URL**: <https://www.fhfa.gov/data>
- **Coverage**: National, State, Metro
- **Frequency**: Quarterly (some metros) & Monthly (others)
- **Metrics**: House Price Index (HPI)

### Freddie Mac

- **URL**: <https://www.freddiemac.com/pmms>
- **Coverage**: National
- **Frequency**: Weekly
- **Metrics**: Mortgage rates

## 🎯 Key Metros Included

### California (Outbound Focus)

- Los Angeles-Long Beach-Anaheim (CBSA: 31080)
- San Francisco-Oakland-Berkeley (CBSA: 41860)
- San Diego-Chula Vista-Carlsbad (CBSA: 41740)
- San Jose-Sunnyvale-Santa Clara (CBSA: 41940)
- Sacramento-Roseville-Folsom (CBSA: 40900)

### Texas (Inbound Focus)

- Dallas-Fort Worth-Arlington (CBSA: 19100)
- Houston-The Woodlands-Sugar Land (CBSA: 26420)
- Austin-Round Rock-Georgetown (CBSA: 12420)
- San Antonio-New Braunfels (CBSA: 41700)

### Emerging Hot Markets (2024-2025 Data)

- Phoenix-Mesa-Chandler, AZ (CBSA: 38060) - Only major metro with positive migration
- Charlotte-Concord-Gastonia, NC-SC (CBSA: 16740)
- Raleigh-Cary, NC (CBSA: 39580)
- Nashville-Davidson-Murfreesboro, TN (CBSA: 34980)
- Greenville-Anderson, SC (CBSA: 24860) - Highest migration rate
- Charleston-North Charleston, SC (CBSA: 16700)
- Buffalo-Cheektowaga, NY (CBSA: 15380) - #1 Zillow hot market
- Virginia Beach-Norfolk-Newport News, VA-NC (CBSA: 47260)

## 📈 Key Findings from 2024-2025 Data

### Migration Trends

- **CA to TX corridor**: 102,000+ people annually (largest interstate route)
- **TX/FL cooling**: Near-zero net migration in 2024 (was positive 2021-2023)
- **South Carolina**: +3.6% net migration (highest rate)
- **Idaho**: +3.4% net migration
- **Phoenix**: Only major metro maintaining positive migration (+0.2%)

### Housing Market Trends

- **National**: Projected +1.2% home value growth through Oct 2026
- **Northeast gaining**: NY, NJ, IL, PA seeing value increases
- **Sun Belt cooling**: FL (-$109B), CA (-$106B), TX (-$32B) annual losses
- **Buffalo, NY**: #1 competitive market for 2025
- **Miami**: Bubble risk (1.73 index score)

### Investment Implications

- **Avoid**: Major TX metros (Dallas, Houston showing price declines)
- **Watch**: Carolinas, Phoenix, upstate NY, Virginia markets
- **Risk**: South Florida (Miami bubble risk + insurance costs)

## 🔄 Next Steps

After downloading data:

1. **Data Cleaning & Merging** (Run `data_cleaner.py`)
   - ✅ Standardize Zillow data
   - ✅ Standardize Census data
   - ✅ Standardize BLS data
   - 🔄 Merge datasets into a master file
   - 🔄 Run `ca_county_cleaner.py` for CA specific analysis
   - 🔄 Run `tx_county_cleaner.py` for TX specific analysis

2. **Feature Engineering** (Run `feature_engineer.py`)
   - Calculate rental yields
   - Compute price momentum (YoY, MoM)
   - Analyze rent growth
   - Derive inventory dynamics

3. **Correlation Analysis**
   - Migration vs. price growth
   - Employment vs. housing demand
   - Supply pipeline vs. appreciation

4. **Predictive Modeling**
   - Random Forest for market scoring
   - Time series forecasting
   - ROI projections

5. **Visualization & Reporting**
   - Interactive dashboards
   - Metro comparison charts
   - Investment recommendation reports

## 💡 Tips for Success

### Data Quality

- Always verify download completion (check file sizes)
- Compare data ranges across sources for consistency
- Document any manual adjustments or exclusions

### Rate Limiting

- Zillow: Be respectful, add delays between requests
- BLS API: 500 requests/day limit (with key), 25 without
- Census: No strict limits but use reasonable delays

### Data Updates

- Zillow: Updates monthly (typically first week of month)
- Census: Annual updates (ACS in September)
- BLS: Monthly employment data, quarterly wages
- Re-run downloads quarterly for fresh data

### Storage

- Full dataset: ~500MB-1GB compressed
- Keep raw downloads separate from processed data
- Use version control for scripts, not data

## 🔧 Troubleshooting

### Download Failures

```bash
# Check internet connection
ping zillow.com

# Verify URLs are still valid (they occasionally change)
# Check Zillow Research page for updated links

# Try manual download if automated fails
```

### Missing Data

- Some smaller metros may not have all metrics
- Rural areas often excluded from certain datasets
- Use metro_reference.csv to verify coverage

### API Issues

```bash
# BLS API not working?
# 1. Verify API key is correct
echo $BLS_API_KEY

# 2. Check daily request limit
# 3. Try manual download as backup
```

## 📚 Resources

### Documentation

- [Zillow Research Methodology](https://www.zillow.com/research/methodology/)
- [Census Migration Data Guide](https://www.census.gov/topics/population/migration/guidance.html)
- [BLS API Documentation](https://www.bls.gov/developers/api_signature_v2.htm)
- [FHFA HPI Documentation](https://www.fhfa.gov/DataTools/Downloads/Pages/House-Price-Index.aspx)

### Analysis References

- [Zillow 2025 Market Predictions](https://www.zillow.com/research/2025-housing-predictions-34620/)
- [Census County-to-County Flows](https://www.census.gov/data/tables/time-series/demo/geographic-mobility/county-to-county-migration.html)

## 🤝 Contributing

This is a personal investment research project. Feel free to adapt and extend for your own analysis.

## ⚠️ Disclaimer

This project is for research and educational purposes only. Not financial advice. Always:

- Conduct your own due diligence
- Consult with licensed professionals
- Consider your personal financial situation
- Verify data accuracy and timeliness
- Understand market risks

## 📧 Questions?

This is part of a larger housing market investment analysis pipeline. Additional scripts for data cleaning, analysis, and visualization will follow.

---

**Last Updated**: November 2025
**Data Coverage**: 2020-2025
**Target Investment Year**: 2026
