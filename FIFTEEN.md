# 15-Minute 1¢ Study

*Updated Tue Oct 20, 6:11 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 2114 finished bets | 1% | $84.55 | +36% | +4.00¢ | $24.05 / $60.50 |

*Expect about **95 buys a day** (~$14.27/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 1946 | $65.80 | +31% |
| Momentum model ≥ 2%, hold to the close | 3243 | -$16.70 | -4% |
| Volatility model ≥ 5%, sell at 50¢ | 2114 | -$32.45 | -14% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 25043 | 25033 | 92 (0%) | 1.07% | -$1,755.20 (-58%) | Hold to the close: -$1,755.20 (-58%) |

*In play or awaiting result: 9. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 16375 | 4.6% | 0.4% (65) | -673% | ❌ Worse |
| Momentum model | 16375 | 4.6% | 0.4% (65) | -696% | ❌ Worse |
| Mean-reversion model | 16375 | 7.8% | 0.4% (65) | -812% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 16375 | 65 | -50% | -87% | -87% | -85% |
| Volatility model ≥ 2% | 3832 | 31 | -7% | -77% | -76% | -73% |
| Volatility model ≥ 5% | 2114 | 23 | +36% | -71% | -70% | -67% |
| Volatility model ≥ 10% | 1229 | 15 | +71% | -60% | -58% | -55% |
| Momentum model ≥ 2% | 3243 | 26 | -4% | -78% | -78% | -75% |
| Momentum model ≥ 5% | 1946 | 20 | +31% | -74% | -74% | -69% |
| Momentum model ≥ 10% | 1289 | 13 | +38% | -66% | -66% | -61% |
| Mean-reversion model ≥ 2% | 6392 | 42 | -28% | -83% | -83% | -80% |
| Mean-reversion model ≥ 5% | 4447 | 34 | -16% | -80% | -80% | -77% |
| Mean-reversion model ≥ 10% | 2941 | 22 | -15% | -77% | -77% | -75% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 16573 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 5893 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 2567 | 1% | 1% | 1% | 1% | 0% | 0% |
| **All** | 25033 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 92 | 0% | -$1,755.20 | -58% | — |
| Sell at 2¢ | 902 | 4% | -$2,682.68 | -88% | 46 sec |
| Sell at 3¢ | 613 | 2% | -$2,678.13 | -88% | 47 sec |
| Sell at 5¢ | 435 | 2% | -$2,634.45 | -87% | 51 sec |
| Sell at 10¢ | 265 | 1% | -$2,542.05 | -84% | 64 sec |
| Sell at 25¢ | 146 | 1% | -$2,349.94 | -77% | 80 sec |
| Sell at 50¢ | 95 | 0% | -$2,121.95 | -70% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 972 | 5 | 10% | 3% | -51% | -82% | -84% |
| 2–5 min | 8120 | 41 | 7% | 3% | -50% | -88% | -87% |
| 1–2 min | 6394 | 24 | 3% | 2% | -59% | -93% | -92% |
| Under 1 min | 9543 | 22 | 1% | 0% | -67% | -86% | -86% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 1863 | 11 | 4% | 2% | -26% | -90% | -90% |
| HYPE | 1852 | 6 | 5% | 2% | -60% | -89% | -88% |
| BNB | 1851 | 9 | 5% | 2% | -40% | -83% | -82% |
| ETH | 1842 | 9 | 6% | 3% | -41% | -87% | -86% |
| DOGE | 1841 | 3 | 4% | 2% | -80% | -91% | -90% |
| SOL | 1838 | 2 | 3% | 2% | -87% | -92% | -92% |
| XRP | 1832 | 7 | 3% | 1% | -53% | -87% | -88% |
| NEAR | 1827 | 10 | 6% | 3% | -29% | -79% | -79% |
| BTC | 1827 | 10 | 5% | 2% | -27% | -88% | -90% |
| GOLD | 967 | 1 | 3% | 1% | -88% | -93% | -95% |
| SILVER | 933 | 4 | 3% | 1% | -50% | -81% | -81% |
| WTI | 909 | 3 | 3% | 1% | -61% | -94% | -95% |
| COPPER | 810 | 3 | 2% | 1% | -65% | -74% | -74% |
| PLATINUM | 801 | 0 | 0% | 0% | -100% | -99% | -99% |
| NATGAS | 743 | 5 | 2% | 1% | -37% | -84% | -83% |
| EURUSD | 738 | 3 | 2% | 1% | -62% | -83% | -83% |
| PALLADIUM | 730 | 2 | 1% | 0% | -74% | -85% | -85% |
| GBPUSD | 696 | 1 | 2% | 1% | -87% | -97% | -97% |
| USDJPY | 646 | 3 | 1% | 1% | -57% | -99% | -98% |
| AUDUSD | 269 | 0 | 0% | 0% | -100% | -99% | -99% |
| USDCAD | 218 | 0 | 0% | 0% | -100% | -99% | -99% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 12641 | 45 | 4% | 2% | -59% | -88% | -87% |
| DOWN (bought NO) | 12392 | 47 | 3% | 1% | -56% | -88% | -89% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 2802 | 15 | 2% | 1% | -11% | -77% | -76% |
| 0.05–0.1% | 2881 | 10 | 3% | 2% | -50% | -92% | -91% |
| 0.1–0.2% | 4195 | 13 | 5% | 2% | -62% | -90% | -89% |
| 0.2–0.5% | 4829 | 23 | 6% | 3% | -48% | -88% | -87% |
| Over 0.5% | 1863 | 6 | 6% | 3% | -67% | -88% | -88% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 6450 | 26 | 4% | 2% | -54% | -85% | -85% |
| Morning (6am–12pm) | 5814 | 29 | 4% | 2% | -43% | -87% | -86% |
| Afternoon (12–6pm) | 5807 | 19 | 3% | 1% | -61% | -89% | -89% |
| Evening (6pm–12am) | 6962 | 18 | 3% | 2% | -70% | -92% | -92% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,794 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/20 6:11:08 AM | BTC | UP | 3.9 min | -0.203% | — | In play | — |
| 10/20 6:09:47 AM | GOLD | UP | 5.2 min | — | — | In play | — |
| 10/20 6:09:47 AM | SILVER | UP | 5.2 min | — | — | In play | — |
| 10/20 5:59:51 AM | NATGAS | UP | 9 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/20 5:58:30 AM | USDCAD | DOWN | 89 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/20 5:58:30 AM | GOLD | DOWN | 89 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/20 5:58:14 AM | COPPER | UP | 1.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/20 5:58:14 AM | USDJPY | UP | 1.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/20 5:58:14 AM | XRP | UP | 1.8 min | -0.177% | 1¢ | ❌ Lost | -$0.15 |
| 10/20 5:58:14 AM | AUDUSD | UP | 1.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/20 5:57:40 AM | WTI | UP | 2.3 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/20 5:57:24 AM | SOL | UP | 2.6 min | -0.208% | 1¢ | ❌ Lost | -$0.15 |
| 10/20 5:57:09 AM | HYPE | UP | 2.8 min | -0.174% | 2¢ | ❌ Lost | -$0.15 |
| 10/20 5:56:52 AM | ETH | UP | 3.1 min | -0.166% | 1¢ | ❌ Lost | -$0.15 |
| 10/20 5:56:52 AM | BTC | UP | 3.1 min | -0.127% | 1¢ | ❌ Lost | -$0.15 |
| 10/20 5:56:04 AM | DOGE | UP | 3.9 min | -0.227% | 1¢ | ❌ Lost | -$0.15 |
| 10/20 5:55:30 AM | BNB | UP | 4.5 min | -0.152% | 1¢ | ❌ Lost | -$0.15 |
| 10/20 5:54:59 AM | ZEC | UP | 5.0 min | -0.538% | 1¢ | ❌ Lost | -$0.15 |
| 10/20 5:52:01 AM | NEAR | UP | 8.0 min | -0.796% | 4¢ | ❌ Lost | -$0.15 |
| 10/20 5:44:51 AM | USDJPY | DOWN | 8 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/20 5:44:51 AM | WTI | DOWN | 8 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/20 5:44:51 AM | SILVER | UP | 8 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/20 5:44:51 AM | ZEC | DOWN | 8 sec | -0.064% | 0¢ | ❌ Lost | -$0.15 |
| 10/20 5:44:51 AM | NATGAS | DOWN | 8 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/20 5:44:51 AM | GBPUSD | DOWN | 8 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/20 5:44:35 AM | PLATINUM | UP | 24 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/20 5:44:19 AM | GOLD | UP | 40 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/20 5:44:03 AM | SOL | DOWN | 57 sec | +0.041% | 1¢ | ❌ Lost | -$0.15 |
| 10/20 5:43:47 AM | USDCAD | DOWN | 73 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/20 5:43:47 AM | NEAR | DOWN | 73 sec | +0.336% | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
