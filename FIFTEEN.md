# 15-Minute 1¢ Study

*Updated Tue Nov 17, 4:54 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 4486 finished bets | 1% | $218.40 | +44% | +4.87¢ | $82.65 / $135.75 |

*Expect about **88 buys a day** (~$13.27/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 4220 | $118.90 | +26% |
| Volatility model ≥ 2%, hold to the close | 8366 | $85.95 | +9% |
| Momentum model ≥ 2%, hold to the close | 6933 | $3.00 | +0% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 60038 | 60004 | 235 (0%) | 1.07% | -$4,011.40 (-55%) | Hold to the close: -$4,011.40 (-55%) |

*In play or awaiting result: 6. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 35979 | 4.5% | 0.4% (154) | -622% | ❌ Worse |
| Momentum model | 35979 | 4.4% | 0.4% (154) | -647% | ❌ Worse |
| Mean-reversion model | 35979 | 7.9% | 0.4% (154) | -754% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 35979 | 154 | -45% | -87% | -87% | -84% |
| Volatility model ≥ 2% | 8366 | 78 | +9% | -77% | -76% | -72% |
| Volatility model ≥ 5% | 4486 | 51 | +44% | -72% | -70% | -67% |
| Volatility model ≥ 10% | 2576 | 30 | +69% | -63% | -61% | -58% |
| Momentum model ≥ 2% | 6933 | 57 | +0% | -79% | -78% | -74% |
| Momentum model ≥ 5% | 4220 | 41 | +26% | -74% | -74% | -70% |
| Momentum model ≥ 10% | 2749 | 26 | +34% | -66% | -66% | -62% |
| Mean-reversion model ≥ 2% | 14753 | 108 | -20% | -82% | -82% | -79% |
| Mean-reversion model ≥ 5% | 10265 | 89 | -4% | -80% | -79% | -77% |
| Mean-reversion model ≥ 10% | 6819 | 64 | +7% | -77% | -77% | -74% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 36185 | 5% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 14252 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 9567 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 60004 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 235 | 0% | -$4,011.40 | -55% | — |
| Sell at 2¢ | 2422 | 4% | -$6,377.68 | -87% | 47 sec |
| Sell at 3¢ | 1635 | 3% | -$6,369.75 | -87% | 48 sec |
| Sell at 5¢ | 1119 | 2% | -$6,252.05 | -86% | 63 sec |
| Sell at 10¢ | 682 | 1% | -$6,001.98 | -82% | 65 sec |
| Sell at 25¢ | 365 | 1% | -$5,561.25 | -76% | 80 sec |
| Sell at 50¢ | 242 | 0% | -$5,009.90 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 13 | 0 | 31% | 23% | -100% | -47% | -20% |
| 5–10 min | 3033 | 17 | 11% | 4% | -47% | -81% | -82% |
| 2–5 min | 19443 | 107 | 7% | 3% | -46% | -86% | -87% |
| 1–2 min | 15051 | 51 | 3% | 2% | -62% | -92% | -92% |
| Under 1 min | 22464 | 60 | 1% | 0% | -62% | -86% | -85% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 4047 | 19 | 5% | 3% | -38% | -88% | -87% |
| SOL | 4045 | 19 | 4% | 2% | -40% | -86% | -86% |
| HYPE | 4037 | 12 | 5% | 2% | -62% | -89% | -88% |
| DOGE | 4026 | 11 | 4% | 2% | -65% | -90% | -89% |
| BNB | 4026 | 21 | 5% | 2% | -34% | -85% | -85% |
| ETH | 4020 | 19 | 7% | 3% | -41% | -82% | -82% |
| NEAR | 4000 | 18 | 5% | 2% | -41% | -85% | -86% |
| BTC | 4000 | 21 | 5% | 2% | -29% | -86% | -88% |
| XRP | 3984 | 16 | 3% | 2% | -49% | -89% | -88% |
| GOLD | 2133 | 5 | 5% | 2% | -71% | -83% | -84% |
| WTI | 2113 | 7 | 4% | 1% | -60% | -91% | -92% |
| SILVER | 2070 | 9 | 5% | 2% | -48% | -83% | -83% |
| PLATINUM | 1884 | 4 | 3% | 1% | -80% | -95% | -95% |
| EURUSD | 1838 | 6 | 2% | 1% | -70% | -91% | -90% |
| COPPER | 1768 | 6 | 2% | 1% | -68% | -76% | -76% |
| GBPUSD | 1765 | 6 | 2% | 1% | -68% | -96% | -96% |
| NATGAS | 1743 | 10 | 2% | 1% | -46% | -75% | -75% |
| USDJPY | 1725 | 6 | 2% | 1% | -68% | -96% | -96% |
| PALLADIUM | 1696 | 4 | 1% | 0% | -78% | -93% | -93% |
| AUDUSD | 1281 | 6 | 2% | 1% | -56% | -89% | -89% |
| USDCAD | 1228 | 1 | 3% | 1% | -92% | -95% | -96% |
| BRENT | 845 | 0 | 2% | 1% | -100% | -97% | -98% |
| 10YRRATE | 435 | 2 | 3% | 1% | -57% | -73% | -71% |
| 2YRRATE | 420 | 4 | 4% | 2% | -11% | -49% | -48% |
| 30YRRATE | 403 | 0 | 2% | 1% | -100% | -96% | -94% |
| 5YRRATE | 391 | 2 | 4% | 2% | -52% | -93% | -95% |
| INX | 81 | 1 | 2% | 1% | +15% | -96% | -97% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 30536 | 121 | 4% | 2% | -54% | -88% | -88% |
| DOWN (bought NO) | 29468 | 114 | 4% | 2% | -55% | -86% | -87% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 5449 | 25 | 2% | 1% | -17% | -78% | -77% |
| 0.05–0.1% | 5903 | 24 | 3% | 2% | -37% | -91% | -91% |
| 0.1–0.2% | 9064 | 34 | 5% | 2% | -52% | -89% | -89% |
| 0.2–0.5% | 11195 | 50 | 7% | 3% | -50% | -86% | -86% |
| Over 0.5% | 4565 | 23 | 7% | 3% | -47% | -86% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 14507 | 45 | 4% | 2% | -65% | -88% | -88% |
| Morning (6am–12pm) | 14416 | 78 | 5% | 2% | -38% | -85% | -84% |
| Afternoon (12–6pm) | 14721 | 63 | 4% | 2% | -50% | -87% | -87% |
| Evening (6pm–12am) | 16360 | 49 | 4% | 2% | -66% | -89% | -89% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 5,070 |
| Time from buy to best bounce (bounced bets) | 50 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/17 4:44:47 PM | BNB | DOWN | 12 sec | +0.005% | 0¢ | ❌ Lost | $0.00 |
| 11/17 4:44:47 PM | BTC | UP | 12 sec | -0.026% | 0¢ | ❌ Lost | $0.00 |
| 11/17 4:44:47 PM | AUDUSD | DOWN | 12 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/17 4:44:47 PM | DOGE | UP | 12 sec | -0.042% | 0¢ | ❌ Lost | $0.00 |
| 11/17 4:44:31 PM | COPPER | DOWN | 28 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/17 4:44:31 PM | ZEC | DOWN | 28 sec | -0.001% | 0¢ | ❌ Lost | -$0.15 |
| 11/17 4:44:15 PM | ETH | DOWN | 45 sec | +0.096% | 0¢ | ❌ Lost | $0.00 |
| 11/17 4:44:15 PM | SILVER | DOWN | 45 sec | — | 0¢ | ❌ Lost | $0.00 |
| 11/17 4:44:15 PM | WTI | UP | 45 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 11/17 4:44:15 PM | XRP | UP | 45 sec | -0.112% | 0¢ | ❌ Lost | $0.00 |
| 11/17 4:44:15 PM | SOL | UP | 45 sec | -0.055% | 1¢ | ❌ Lost | -$0.15 |
| 11/17 4:43:26 PM | NEAR | DOWN | 1.6 min | +0.261% | 1¢ | ❌ Lost | -$0.15 |
| 11/17 4:43:26 PM | USDJPY | DOWN | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/17 4:43:26 PM | EURUSD | UP | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/17 4:43:10 PM | BRENT | UP | 1.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/17 4:42:26 PM | GBPUSD | UP | 2.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/17 4:40:45 PM | GOLD | UP | 4.2 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/17 4:40:28 PM | HYPE | DOWN | 4.5 min | +0.438% | 3¢ | ❌ Lost | -$0.15 |
| 11/17 4:29:48 PM | USDJPY | UP | 12 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/17 4:29:48 PM | NATGAS | DOWN | 12 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/17 4:29:48 PM | EURUSD | DOWN | 12 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/17 4:29:32 PM | BRENT | DOWN | 28 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/17 4:29:32 PM | XRP | UP | 28 sec | -0.193% | 0¢ | ❌ Lost | $0.00 |
| 11/17 4:29:32 PM | USDCAD | UP | 28 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/17 4:29:16 PM | SILVER | UP | 44 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 11/17 4:29:16 PM | PALLADIUM | UP | 44 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/17 4:29:16 PM | GBPUSD | DOWN | 44 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/17 4:28:59 PM | NEAR | UP | 60 sec | -0.382% | 1¢ | ❌ Lost | -$0.15 |
| 11/17 4:28:28 PM | DOGE | UP | 1.5 min | -0.256% | 1¢ | ❌ Lost | -$0.15 |
| 11/17 4:28:12 PM | GOLD | DOWN | 1.8 min | — | 3¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
