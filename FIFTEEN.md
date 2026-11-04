# 15-Minute 1¢ Study

*Updated Wed Nov 4, 12:08 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 3621 finished bets | 1% | $113.90 | +28% | +3.15¢ | $79.00 / $34.90 |

*Expect about **98 buys a day** (~$14.67/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 3355 | $41.65 | +11% |
| Volatility model ≥ 2%, hold to the close | 6706 | $29.25 | +4% |
| Momentum model ≥ 2%, hold to the close | 5528 | -$50.10 | -8% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 44913 | 44903 | 167 (0%) | 1.07% | -$3,130.70 (-57%) | Hold to the close: -$3,130.70 (-57%) |

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
| Volatility model | 27548 | 4.7% | 0.4% (108) | -676% | ❌ Worse |
| Momentum model | 27548 | 4.6% | 0.4% (108) | -702% | ❌ Worse |
| Mean-reversion model | 27548 | 8.1% | 0.4% (108) | -825% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 27548 | 108 | -50% | -88% | -87% | -85% |
| Volatility model ≥ 2% | 6706 | 60 | +4% | -79% | -78% | -74% |
| Volatility model ≥ 5% | 3621 | 37 | +28% | -76% | -75% | -71% |
| Volatility model ≥ 10% | 2054 | 22 | +53% | -71% | -69% | -66% |
| Momentum model ≥ 2% | 5528 | 42 | -8% | -81% | -81% | -78% |
| Momentum model ≥ 5% | 3355 | 29 | +11% | -79% | -79% | -75% |
| Momentum model ≥ 10% | 2187 | 19 | +22% | -74% | -74% | -70% |
| Mean-reversion model ≥ 2% | 11402 | 78 | -25% | -83% | -83% | -80% |
| Mean-reversion model ≥ 5% | 8009 | 67 | -7% | -81% | -80% | -78% |
| Mean-reversion model ≥ 10% | 5361 | 47 | -1% | -80% | -79% | -77% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 27753 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 10656 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 6494 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 44903 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 167 | 0% | -$3,130.70 | -57% | — |
| Sell at 2¢ | 1765 | 4% | -$4,757.80 | -87% | 47 sec |
| Sell at 3¢ | 1210 | 3% | -$4,744.80 | -87% | 49 sec |
| Sell at 5¢ | 838 | 2% | -$4,644.00 | -85% | 63 sec |
| Sell at 10¢ | 506 | 1% | -$4,441.84 | -81% | 66 sec |
| Sell at 25¢ | 266 | 1% | -$4,112.24 | -75% | 83 sec |
| Sell at 50¢ | 170 | 0% | -$3,747.20 | -69% | 1.8 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 11 | 0 | 27% | 18% | -100% | -53% | -29% |
| 5–10 min | 2200 | 10 | 11% | 4% | -57% | -81% | -82% |
| 2–5 min | 14441 | 79 | 7% | 3% | -46% | -87% | -86% |
| 1–2 min | 11329 | 39 | 3% | 1% | -62% | -92% | -92% |
| Under 1 min | 16922 | 39 | 1% | 0% | -67% | -84% | -84% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 3109 | 13 | 5% | 3% | -46% | -88% | -88% |
| SOL | 3103 | 12 | 4% | 2% | -51% | -90% | -90% |
| BNB | 3096 | 17 | 5% | 2% | -31% | -85% | -84% |
| HYPE | 3095 | 9 | 5% | 2% | -64% | -89% | -87% |
| DOGE | 3083 | 6 | 4% | 2% | -76% | -90% | -90% |
| ETH | 3078 | 12 | 7% | 3% | -52% | -85% | -85% |
| NEAR | 3066 | 15 | 5% | 2% | -37% | -84% | -84% |
| BTC | 3066 | 14 | 5% | 2% | -38% | -88% | -89% |
| XRP | 3057 | 12 | 3% | 1% | -51% | -89% | -89% |
| GOLD | 1651 | 5 | 5% | 2% | -63% | -81% | -83% |
| SILVER | 1608 | 7 | 5% | 2% | -48% | -82% | -82% |
| WTI | 1607 | 5 | 3% | 1% | -62% | -92% | -93% |
| PLATINUM | 1438 | 4 | 2% | 1% | -74% | -96% | -96% |
| EURUSD | 1379 | 3 | 3% | 1% | -80% | -89% | -89% |
| COPPER | 1359 | 6 | 2% | 1% | -59% | -70% | -69% |
| NATGAS | 1308 | 8 | 2% | 1% | -43% | -75% | -74% |
| GBPUSD | 1307 | 3 | 2% | 1% | -79% | -96% | -96% |
| USDJPY | 1290 | 5 | 2% | 1% | -64% | -97% | -97% |
| PALLADIUM | 1287 | 3 | 1% | 1% | -78% | -91% | -91% |
| AUDUSD | 837 | 4 | 2% | 1% | -55% | -86% | -85% |
| USDCAD | 804 | 0 | 2% | 0% | -100% | -97% | -98% |
| BRENT | 398 | 0 | 1% | 1% | -100% | -98% | -97% |
| 10YRRATE | 240 | 1 | 5% | 2% | -61% | -52% | -50% |
| 30YRRATE | 223 | 0 | 1% | 0% | -100% | -98% | -97% |
| 2YRRATE | 215 | 2 | 4% | 0% | -13% | -7% | -6% |
| 5YRRATE | 199 | 1 | 5% | 2% | -53% | -91% | -93% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 22804 | 89 | 4% | 2% | -55% | -88% | -87% |
| DOWN (bought NO) | 22099 | 78 | 4% | 2% | -59% | -86% | -87% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 4487 | 21 | 2% | 1% | -18% | -83% | -82% |
| 0.05–0.1% | 4731 | 18 | 3% | 2% | -42% | -91% | -90% |
| 0.1–0.2% | 7183 | 25 | 4% | 2% | -56% | -90% | -89% |
| 0.2–0.5% | 8241 | 33 | 6% | 3% | -55% | -87% | -86% |
| Over 0.5% | 3103 | 13 | 7% | 3% | -57% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 11048 | 40 | 4% | 2% | -59% | -87% | -87% |
| Morning (6am–12pm) | 11054 | 48 | 4% | 2% | -51% | -85% | -85% |
| Afternoon (12–6pm) | 10598 | 39 | 4% | 2% | -57% | -86% | -86% |
| Evening (6pm–12am) | 12203 | 40 | 3% | 2% | -62% | -90% | -89% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,725 |
| Time from buy to best bounce (bounced bets) | 51 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/3 11:59:52 PM | USDCAD | UP | 8 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/3 11:59:52 PM | USDJPY | DOWN | 8 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/3 11:59:52 PM | EURUSD | UP | 8 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/3 11:59:36 PM | AUDUSD | DOWN | 24 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/3 11:59:36 PM | BRENT | DOWN | 24 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/3 11:59:36 PM | NEAR | DOWN | 24 sec | +0.066% | 0¢ | ❌ Lost | $0.00 |
| 11/3 11:59:20 PM | XRP | DOWN | 40 sec | +0.000% | 0¢ | ❌ Lost | $0.00 |
| 11/3 11:59:05 PM | SILVER | DOWN | 54 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/3 11:58:45 PM | ZEC | DOWN | 74 sec | +0.333% | 1¢ | ❌ Lost | -$0.15 |
| 11/3 11:58:45 PM | NATGAS | DOWN | 74 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/3 11:58:45 PM | BNB | DOWN | 74 sec | +0.046% | 1¢ | ❌ Lost | -$0.15 |
| 11/3 11:58:29 PM | SOL | DOWN | 1.5 min | +0.141% | 1¢ | ❌ Lost | -$0.15 |
| 11/3 11:58:29 PM | DOGE | DOWN | 1.5 min | +0.091% | 1¢ | ❌ Lost | -$0.15 |
| 11/3 11:58:14 PM | COPPER | DOWN | 1.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/3 11:58:14 PM | WTI | DOWN | 1.8 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/3 11:57:43 PM | BTC | DOWN | 2.3 min | +0.138% | 1¢ | ❌ Lost | -$0.15 |
| 11/3 11:57:11 PM | ETH | DOWN | 2.8 min | +0.176% | 1¢ | ❌ Lost | -$0.15 |
| 11/3 11:57:11 PM | PALLADIUM | DOWN | 2.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/3 11:56:55 PM | GOLD | DOWN | 3.1 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/3 11:55:06 PM | HYPE | DOWN | 4.9 min | +0.577% | 1¢ | ❌ Lost | -$0.15 |
| 11/3 11:44:42 PM | COPPER | UP | 17 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/3 11:44:09 PM | AUDUSD | DOWN | 50 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/3 11:44:09 PM | BRENT | UP | 50 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/3 11:44:09 PM | NEAR | UP | 50 sec | -0.352% | 0¢ | ❌ Lost | -$0.15 |
| 11/3 11:44:09 PM | BTC | UP | 50 sec | -0.083% | 0¢ | ❌ Lost | $0.00 |
| 11/3 11:44:09 PM | XRP | UP | 50 sec | -0.157% | 0¢ | ❌ Lost | $0.00 |
| 11/3 11:43:53 PM | NATGAS | DOWN | 66 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/3 11:43:53 PM | DOGE | UP | 66 sec | -0.163% | 0¢ | ❌ Lost | -$0.15 |
| 11/3 11:43:53 PM | USDJPY | UP | 66 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/3 11:43:53 PM | SILVER | UP | 66 sec | — | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
