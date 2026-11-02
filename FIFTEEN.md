# 15-Minute 1¢ Study

*Updated Mon Nov 2, 2:02 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 3482 finished bets | 1% | $128.45 | +33% | +3.69¢ | $72.95 / $55.50 |

*Expect about **99 buys a day** (~$14.88/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Volatility model ≥ 2%, hold to the close | 6429 | $61.05 | +8% |
| Momentum model ≥ 5%, hold to the close | 3208 | $56.50 | +16% |
| Momentum model ≥ 2%, hold to the close | 5297 | -$25.20 | -4% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 42333 | 42323 | 159 (0%) | 1.07% | -$2,925.15 (-57%) | Hold to the close: -$2,925.15 (-57%) |

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
| Volatility model | 26364 | 4.7% | 0.4% (106) | -672% | ❌ Worse |
| Momentum model | 26364 | 4.6% | 0.4% (106) | -694% | ❌ Worse |
| Mean-reversion model | 26364 | 8.1% | 0.4% (106) | -820% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 26364 | 106 | -49% | -88% | -87% | -85% |
| Volatility model ≥ 2% | 6429 | 60 | +8% | -79% | -77% | -73% |
| Volatility model ≥ 5% | 3482 | 37 | +33% | -76% | -74% | -70% |
| Volatility model ≥ 10% | 1972 | 22 | +59% | -70% | -68% | -65% |
| Momentum model ≥ 2% | 5297 | 42 | -4% | -81% | -80% | -77% |
| Momentum model ≥ 5% | 3208 | 29 | +16% | -79% | -78% | -74% |
| Momentum model ≥ 10% | 2094 | 19 | +27% | -74% | -73% | -68% |
| Mean-reversion model ≥ 2% | 10897 | 76 | -24% | -83% | -83% | -80% |
| Mean-reversion model ≥ 5% | 7642 | 65 | -6% | -81% | -80% | -77% |
| Mean-reversion model ≥ 10% | 5109 | 46 | +2% | -79% | -79% | -76% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 26566 | 5% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 9924 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 5833 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 42323 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 159 | 0% | -$2,925.15 | -57% | — |
| Sell at 2¢ | 1656 | 4% | -$4,496.59 | -87% | 47 sec |
| Sell at 3¢ | 1137 | 3% | -$4,483.72 | -87% | 48 sec |
| Sell at 5¢ | 791 | 2% | -$4,385.00 | -85% | 63 sec |
| Sell at 10¢ | 477 | 1% | -$4,204.28 | -82% | 65 sec |
| Sell at 25¢ | 251 | 1% | -$3,886.34 | -75% | 83 sec |
| Sell at 50¢ | 164 | 0% | -$3,526.15 | -68% | 1.8 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 11 | 0 | 27% | 18% | -100% | -53% | -29% |
| 5–10 min | 2018 | 9 | 11% | 4% | -58% | -81% | -82% |
| 2–5 min | 13599 | 75 | 7% | 3% | -46% | -87% | -86% |
| 1–2 min | 10689 | 38 | 3% | 2% | -61% | -92% | -92% |
| Under 1 min | 16006 | 37 | 1% | 0% | -67% | -85% | -85% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 2976 | 13 | 5% | 3% | -44% | -88% | -87% |
| SOL | 2967 | 11 | 4% | 2% | -53% | -91% | -91% |
| BNB | 2964 | 17 | 5% | 2% | -28% | -85% | -84% |
| HYPE | 2963 | 9 | 5% | 2% | -62% | -89% | -87% |
| DOGE | 2951 | 6 | 4% | 2% | -74% | -90% | -89% |
| ETH | 2950 | 11 | 6% | 3% | -55% | -85% | -85% |
| NEAR | 2932 | 15 | 5% | 2% | -34% | -83% | -83% |
| BTC | 2932 | 14 | 5% | 2% | -36% | -88% | -89% |
| XRP | 2931 | 12 | 3% | 1% | -49% | -89% | -89% |
| GOLD | 1547 | 5 | 5% | 2% | -61% | -82% | -84% |
| SILVER | 1508 | 7 | 5% | 2% | -45% | -82% | -82% |
| WTI | 1504 | 4 | 3% | 1% | -68% | -93% | -94% |
| PLATINUM | 1339 | 3 | 2% | 1% | -79% | -96% | -96% |
| COPPER | 1280 | 5 | 1% | 1% | -64% | -76% | -75% |
| EURUSD | 1278 | 3 | 2% | 1% | -78% | -89% | -89% |
| NATGAS | 1232 | 7 | 2% | 1% | -47% | -81% | -80% |
| GBPUSD | 1209 | 2 | 2% | 1% | -85% | -96% | -96% |
| PALLADIUM | 1203 | 2 | 1% | 0% | -84% | -90% | -91% |
| USDJPY | 1198 | 5 | 2% | 1% | -61% | -97% | -96% |
| AUDUSD | 733 | 4 | 2% | 1% | -49% | -85% | -84% |
| USDCAD | 710 | 0 | 2% | 1% | -100% | -97% | -97% |
| BRENT | 311 | 0 | 1% | 1% | -100% | -98% | -97% |
| 10YRRATE | 192 | 1 | 5% | 2% | -51% | -42% | -41% |
| 30YRRATE | 181 | 0 | 1% | 0% | -100% | -98% | -97% |
| 2YRRATE | 173 | 2 | 5% | 1% | +8% | +16% | +17% |
| 5YRRATE | 159 | 1 | 6% | 3% | -41% | -89% | -92% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 21486 | 87 | 4% | 2% | -53% | -88% | -87% |
| DOWN (bought NO) | 20837 | 72 | 4% | 2% | -60% | -87% | -87% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 4332 | 21 | 2% | 1% | -16% | -82% | -81% |
| 0.05–0.1% | 4570 | 18 | 3% | 2% | -41% | -91% | -90% |
| 0.1–0.2% | 6884 | 24 | 4% | 2% | -57% | -90% | -90% |
| 0.2–0.5% | 7833 | 33 | 7% | 3% | -53% | -87% | -86% |
| Over 0.5% | 2942 | 12 | 7% | 3% | -58% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 10463 | 37 | 4% | 2% | -60% | -86% | -86% |
| Morning (6am–12pm) | 10513 | 48 | 5% | 2% | -48% | -85% | -84% |
| Afternoon (12–6pm) | 9923 | 37 | 4% | 2% | -56% | -87% | -87% |
| Evening (6pm–12am) | 11424 | 37 | 3% | 2% | -63% | -91% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,803 |
| Time from buy to best bounce (bounced bets) | 51 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/2 1:59:54 AM | USDJPY | DOWN | 5 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/2 1:59:37 AM | GOLD | UP | 23 sec | — | 0¢ | ❌ Lost | $0.00 |
| 11/2 1:59:37 AM | ETH | UP | 23 sec | -0.072% | 0¢ | ❌ Lost | $0.00 |
| 11/2 1:59:37 AM | PALLADIUM | UP | 23 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/2 1:59:37 AM | 2YRRATE | DOWN | 23 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/2 1:59:05 AM | PLATINUM | UP | 55 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/2 1:58:50 AM | BNB | DOWN | 69 sec | +0.013% | 1¢ | ❌ Lost | -$0.15 |
| 11/2 1:58:50 AM | NEAR | DOWN | 69 sec | +0.150% | 1¢ | ❌ Lost | -$0.15 |
| 11/2 1:58:50 AM | DOGE | UP | 69 sec | -0.135% | 0¢ | ❌ Lost | $0.00 |
| 11/2 1:58:34 AM | BTC | UP | 85 sec | -0.085% | 1¢ | ❌ Lost | -$0.15 |
| 11/2 1:57:46 AM | ZEC | UP | 2.2 min | -0.271% | 1¢ | ❌ Lost | -$0.15 |
| 11/2 1:57:29 AM | SOL | UP | 2.5 min | -0.154% | 1¢ | ❌ Lost | -$0.15 |
| 11/2 1:57:29 AM | HYPE | UP | 2.5 min | -0.297% | 0¢ | ❌ Lost | $0.00 |
| 11/2 1:57:13 AM | XRP | UP | 2.8 min | -0.175% | 0¢ | ❌ Lost | -$0.15 |
| 11/2 1:56:57 AM | GBPUSD | DOWN | 3.0 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/2 1:56:57 AM | USDCAD | UP | 3.0 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/2 1:56:42 AM | EURUSD | DOWN | 3.3 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/2 1:56:09 AM | NATGAS | DOWN | 3.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/2 1:53:30 AM | COPPER | DOWN | 6.5 min | — | 0¢ | ❌ Lost | -$0.15 |
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

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
