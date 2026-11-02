# 15-Minute 1¢ Study

*Updated Mon Nov 2, 1:52 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 3480 finished bets | 1% | $128.75 | +33% | +3.70¢ | $73.10 / $55.65 |

*Expect about **99 buys a day** (~$14.88/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Volatility model ≥ 2%, hold to the close | 6425 | $61.65 | +8% |
| Momentum model ≥ 5%, hold to the close | 3206 | $56.80 | +16% |
| Momentum model ≥ 2%, hold to the close | 5294 | -$24.75 | -4% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 42314 | 42304 | 159 (0%) | 1.07% | -$2,922.90 (-57%) | Hold to the close: -$2,922.90 (-57%) |

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
| Volatility model | 26355 | 4.7% | 0.4% (106) | -672% | ❌ Worse |
| Momentum model | 26355 | 4.6% | 0.4% (106) | -694% | ❌ Worse |
| Mean-reversion model | 26355 | 8.1% | 0.4% (106) | -820% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 26355 | 106 | -49% | -88% | -87% | -85% |
| Volatility model ≥ 2% | 6425 | 60 | +8% | -79% | -77% | -73% |
| Volatility model ≥ 5% | 3480 | 37 | +33% | -76% | -74% | -70% |
| Volatility model ≥ 10% | 1971 | 22 | +59% | -70% | -68% | -65% |
| Momentum model ≥ 2% | 5294 | 42 | -4% | -81% | -80% | -77% |
| Momentum model ≥ 5% | 3206 | 29 | +16% | -79% | -78% | -74% |
| Momentum model ≥ 10% | 2093 | 19 | +27% | -74% | -73% | -68% |
| Mean-reversion model ≥ 2% | 10891 | 76 | -24% | -83% | -83% | -80% |
| Mean-reversion model ≥ 5% | 7637 | 65 | -6% | -81% | -80% | -77% |
| Mean-reversion model ≥ 10% | 5106 | 46 | +2% | -79% | -79% | -76% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 26557 | 5% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 9919 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 5828 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 42304 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 159 | 0% | -$2,922.90 | -57% | — |
| Sell at 2¢ | 1656 | 4% | -$4,494.34 | -87% | 47 sec |
| Sell at 3¢ | 1137 | 3% | -$4,481.47 | -87% | 48 sec |
| Sell at 5¢ | 791 | 2% | -$4,382.75 | -85% | 63 sec |
| Sell at 10¢ | 477 | 1% | -$4,202.03 | -82% | 65 sec |
| Sell at 25¢ | 251 | 1% | -$3,884.09 | -75% | 83 sec |
| Sell at 50¢ | 164 | 0% | -$3,523.90 | -68% | 1.8 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 11 | 0 | 27% | 18% | -100% | -53% | -29% |
| 5–10 min | 2017 | 9 | 11% | 4% | -58% | -81% | -82% |
| 2–5 min | 13591 | 75 | 7% | 3% | -46% | -87% | -86% |
| 1–2 min | 10685 | 38 | 3% | 2% | -61% | -92% | -92% |
| Under 1 min | 16000 | 37 | 1% | 0% | -67% | -85% | -85% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 2975 | 13 | 5% | 3% | -44% | -88% | -87% |
| SOL | 2966 | 11 | 4% | 2% | -53% | -91% | -91% |
| BNB | 2963 | 17 | 5% | 2% | -28% | -85% | -84% |
| HYPE | 2962 | 9 | 5% | 2% | -62% | -89% | -87% |
| DOGE | 2950 | 6 | 4% | 2% | -74% | -90% | -89% |
| ETH | 2949 | 11 | 6% | 3% | -55% | -85% | -85% |
| NEAR | 2931 | 15 | 5% | 2% | -34% | -83% | -83% |
| BTC | 2931 | 14 | 5% | 2% | -36% | -88% | -89% |
| XRP | 2930 | 12 | 3% | 1% | -49% | -89% | -89% |
| GOLD | 1546 | 5 | 5% | 2% | -61% | -82% | -84% |
| SILVER | 1508 | 7 | 5% | 2% | -45% | -82% | -82% |
| WTI | 1504 | 4 | 3% | 1% | -68% | -93% | -94% |
| PLATINUM | 1338 | 3 | 2% | 1% | -79% | -96% | -96% |
| COPPER | 1279 | 5 | 1% | 1% | -64% | -76% | -75% |
| EURUSD | 1277 | 3 | 2% | 1% | -78% | -89% | -89% |
| NATGAS | 1231 | 7 | 2% | 1% | -47% | -81% | -80% |
| GBPUSD | 1208 | 2 | 2% | 1% | -85% | -96% | -96% |
| PALLADIUM | 1202 | 2 | 1% | 0% | -84% | -90% | -91% |
| USDJPY | 1197 | 5 | 2% | 1% | -61% | -97% | -96% |
| AUDUSD | 733 | 4 | 2% | 1% | -49% | -85% | -84% |
| USDCAD | 709 | 0 | 2% | 1% | -100% | -97% | -97% |
| BRENT | 311 | 0 | 1% | 1% | -100% | -98% | -97% |
| 10YRRATE | 192 | 1 | 5% | 2% | -51% | -42% | -41% |
| 30YRRATE | 181 | 0 | 1% | 0% | -100% | -98% | -97% |
| 2YRRATE | 172 | 2 | 5% | 1% | +9% | +17% | +18% |
| 5YRRATE | 159 | 1 | 6% | 3% | -41% | -89% | -92% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 21475 | 87 | 4% | 2% | -53% | -88% | -87% |
| DOWN (bought NO) | 20829 | 72 | 4% | 2% | -60% | -87% | -87% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 4331 | 21 | 2% | 1% | -16% | -82% | -81% |
| 0.05–0.1% | 4568 | 18 | 3% | 2% | -41% | -91% | -90% |
| 0.1–0.2% | 6880 | 24 | 4% | 2% | -57% | -90% | -90% |
| 0.2–0.5% | 7831 | 33 | 7% | 3% | -53% | -87% | -86% |
| Over 0.5% | 2942 | 12 | 7% | 3% | -58% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 10444 | 37 | 4% | 2% | -60% | -86% | -86% |
| Morning (6am–12pm) | 10513 | 48 | 5% | 2% | -48% | -85% | -84% |
| Afternoon (12–6pm) | 9923 | 37 | 4% | 2% | -56% | -87% | -87% |
| Evening (6pm–12am) | 11424 | 37 | 3% | 2% | -63% | -91% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,804 |
| Time from buy to best bounce (bounced bets) | 51 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/2 1:44:47 AM | COPPER | DOWN | 12 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/2 1:44:47 AM | USDJPY | UP | 12 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/2 1:44:31 AM | GOLD | DOWN | 28 sec | — | 0¢ | ❌ Lost | $0.00 |
| 11/2 1:44:31 AM | SILVER | DOWN | 28 sec | — | 0¢ | ❌ Lost | $0.00 |
| 11/2 1:44:31 AM | PALLADIUM | DOWN | 28 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/2 1:44:31 AM | 5YRRATE | UP | 28 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/2 1:44:31 AM | 2YRRATE | UP | 28 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/2 1:44:15 AM | AUDUSD | DOWN | 44 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/2 1:43:27 AM | 10YRRATE | UP | 1.5 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/2 1:43:27 AM | 30YRRATE | UP | 1.5 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/2 1:43:11 AM | BRENT | UP | 1.8 min | — | 11¢ | ❌ Lost | -$0.15 |
| 11/2 1:41:06 AM | BTC | DOWN | 3.9 min | +0.268% | 1¢ | ❌ Lost | -$0.15 |
| 11/2 1:41:06 AM | XRP | DOWN | 3.9 min | +0.432% | 0¢ | ❌ Lost | -$0.15 |
| 11/2 1:41:06 AM | ZEC | DOWN | 3.9 min | +0.653% | 1¢ | ❌ Lost | -$0.15 |
| 11/2 1:40:50 AM | BNB | DOWN | 4.2 min | +0.185% | 1¢ | ❌ Lost | -$0.15 |
| 11/2 1:40:50 AM | DOGE | DOWN | 4.2 min | +0.305% | 0¢ | ❌ Lost | -$0.15 |
| 11/2 1:40:34 AM | NEAR | DOWN | 4.4 min | +0.429% | 1¢ | ❌ Lost | -$0.15 |
| 11/2 1:40:02 AM | SOL | DOWN | 5.0 min | +0.298% | 1¢ | ❌ Lost | -$0.15 |
| 11/2 1:39:46 AM | ETH | DOWN | 5.2 min | +0.261% | 1¢ | ❌ Lost | -$0.15 |
| 11/2 1:39:46 AM | USDCAD | UP | 5.2 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/2 1:39:14 AM | HYPE | DOWN | 5.8 min | +0.487% | 0¢ | ❌ Lost | -$0.15 |
| 11/2 1:38:58 AM | GBPUSD | DOWN | 6.0 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/2 1:38:42 AM | EURUSD | DOWN | 6.3 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/2 1:29:29 AM | EURUSD | DOWN | 31 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/2 1:29:29 AM | 5YRRATE | UP | 31 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/2 1:29:29 AM | 30YRRATE | UP | 31 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/2 1:29:14 AM | SOL | DOWN | 46 sec | +0.048% | 0¢ | ❌ Lost | -$0.15 |
| 11/2 1:29:14 AM | ETH | DOWN | 46 sec | +0.058% | 0¢ | ❌ Lost | $0.00 |
| 11/2 1:29:14 AM | GBPUSD | DOWN | 46 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/2 1:29:14 AM | 10YRRATE | UP | 46 sec | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
