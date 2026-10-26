# 15-Minute 1¢ Study

*Updated Sun Oct 25, 10:06 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 2710 finished bets | 1% | $84.35 | +27% | +3.11¢ | $33.35 / $51.00 |

*Expect about **97 buys a day** (~$14.57/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 2511 | $58.50 | +21% |
| Volatility model ≥ 2%, hold to the close | 5013 | -$12.25 | -2% |
| Momentum model ≥ 2%, hold to the close | 4178 | -$27.75 | -6% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 32138 | 32130 | 120 (0%) | 1.07% | -$2,222.70 (-57%) | Hold to the close: -$2,222.70 (-57%) |

*In play or awaiting result: 7. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 20732 | 4.6% | 0.4% (85) | -658% | ❌ Worse |
| Momentum model | 20732 | 4.6% | 0.4% (85) | -682% | ❌ Worse |
| Mean-reversion model | 20732 | 7.9% | 0.4% (85) | -796% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 20732 | 85 | -48% | -88% | -87% | -85% |
| Volatility model ≥ 2% | 5013 | 43 | -2% | -78% | -77% | -74% |
| Volatility model ≥ 5% | 2710 | 28 | +27% | -75% | -73% | -70% |
| Volatility model ≥ 10% | 1535 | 18 | +64% | -66% | -65% | -61% |
| Momentum model ≥ 2% | 4178 | 33 | -6% | -80% | -80% | -77% |
| Momentum model ≥ 5% | 2511 | 24 | +21% | -77% | -76% | -72% |
| Momentum model ≥ 10% | 1637 | 16 | +34% | -71% | -70% | -65% |
| Mean-reversion model ≥ 2% | 8356 | 56 | -27% | -83% | -82% | -80% |
| Mean-reversion model ≥ 5% | 5855 | 47 | -12% | -81% | -80% | -78% |
| Mean-reversion model ≥ 10% | 3896 | 33 | -4% | -78% | -78% | -75% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 20932 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 7462 | 2% | 2% | 1% | 1% | 0% | 0% |
| Financials | 3736 | 2% | 1% | 1% | 1% | 0% | 0% |
| **All** | 32130 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 120 | 0% | -$2,222.70 | -57% | — |
| Sell at 2¢ | 1197 | 4% | -$3,423.48 | -88% | 47 sec |
| Sell at 3¢ | 822 | 3% | -$3,414.12 | -87% | 48 sec |
| Sell at 5¢ | 572 | 2% | -$3,362.90 | -86% | 61 sec |
| Sell at 10¢ | 354 | 1% | -$3,228.96 | -83% | 65 sec |
| Sell at 25¢ | 191 | 1% | -$2,990.49 | -77% | 82 sec |
| Sell at 50¢ | 122 | 0% | -$2,715.20 | -70% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 1407 | 7 | 11% | 4% | -53% | -81% | -83% |
| 2–5 min | 10297 | 55 | 7% | 3% | -47% | -87% | -87% |
| 1–2 min | 8125 | 30 | 3% | 1% | -60% | -92% | -91% |
| Under 1 min | 12297 | 28 | 1% | 0% | -67% | -86% | -86% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 2345 | 12 | 5% | 2% | -35% | -89% | -89% |
| HYPE | 2339 | 8 | 5% | 3% | -58% | -89% | -87% |
| BNB | 2335 | 13 | 5% | 3% | -31% | -84% | -83% |
| SOL | 2331 | 6 | 3% | 2% | -68% | -92% | -92% |
| ETH | 2327 | 11 | 6% | 3% | -43% | -86% | -85% |
| DOGE | 2319 | 4 | 4% | 2% | -78% | -91% | -90% |
| NEAR | 2315 | 12 | 5% | 2% | -33% | -82% | -81% |
| XRP | 2315 | 9 | 3% | 1% | -52% | -89% | -88% |
| BTC | 2306 | 12 | 5% | 2% | -30% | -88% | -89% |
| GOLD | 1209 | 4 | 4% | 1% | -61% | -81% | -83% |
| SILVER | 1174 | 5 | 4% | 2% | -51% | -82% | -82% |
| WTI | 1155 | 3 | 3% | 1% | -69% | -94% | -95% |
| PLATINUM | 1024 | 0 | 1% | 1% | -100% | -98% | -97% |
| COPPER | 1000 | 4 | 1% | 1% | -63% | -70% | -69% |
| EURUSD | 955 | 3 | 2% | 1% | -71% | -86% | -86% |
| NATGAS | 948 | 5 | 2% | 1% | -51% | -87% | -86% |
| PALLADIUM | 911 | 2 | 1% | 0% | -80% | -88% | -88% |
| GBPUSD | 900 | 1 | 2% | 1% | -90% | -96% | -97% |
| USDJPY | 884 | 5 | 1% | 1% | -47% | -98% | -97% |
| AUDUSD | 441 | 0 | 1% | 0% | -100% | -98% | -98% |
| USDCAD | 404 | 0 | 1% | 0% | -100% | -97% | -99% |
| 10YRRATE | 43 | 0 | 0% | 0% | -100% | -100% | -100% |
| BRENT | 41 | 0 | 0% | 0% | -100% | -100% | -100% |
| 2YRRATE | 40 | 1 | 2% | 0% | +133% | +138% | +133% |
| 30YRRATE | 39 | 0 | 0% | 0% | -100% | -100% | -100% |
| 5YRRATE | 30 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 16294 | 66 | 4% | 2% | -53% | -87% | -87% |
| DOWN (bought NO) | 15836 | 54 | 4% | 1% | -61% | -88% | -88% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 3499 | 18 | 2% | 1% | -13% | -80% | -80% |
| 0.05–0.1% | 3603 | 11 | 3% | 1% | -55% | -92% | -92% |
| 0.1–0.2% | 5412 | 20 | 5% | 2% | -54% | -89% | -89% |
| 0.2–0.5% | 6091 | 28 | 6% | 3% | -49% | -87% | -86% |
| Over 0.5% | 2323 | 10 | 7% | 3% | -56% | -87% | -88% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 7904 | 32 | 4% | 2% | -54% | -85% | -85% |
| Morning (6am–12pm) | 7781 | 35 | 4% | 2% | -49% | -88% | -87% |
| Afternoon (12–6pm) | 7607 | 24 | 4% | 2% | -63% | -87% | -88% |
| Evening (6pm–12am) | 8838 | 29 | 3% | 2% | -62% | -90% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,822 |
| Time from buy to best bounce (bounced bets) | 50 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/25 9:59:43 PM | SOL | UP | 16 sec | -0.083% | 0¢ | ❌ Lost | $0.00 |
| 10/25 9:59:27 PM | WTI | DOWN | 33 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/25 9:59:27 PM | HYPE | DOWN | 33 sec | +0.189% | 0¢ | ❌ Lost | $0.00 |
| 10/25 9:58:55 PM | ZEC | DOWN | 65 sec | +0.285% | 1¢ | ❌ Lost | -$0.15 |
| 10/25 9:58:55 PM | NEAR | DOWN | 65 sec | +0.353% | 0¢ | ❌ Lost | $0.00 |
| 10/25 9:58:55 PM | BRENT | DOWN | 65 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/25 9:58:55 PM | GOLD | UP | 65 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/25 9:58:22 PM | USDJPY | DOWN | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/25 9:57:17 PM | SILVER | UP | 2.7 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/25 9:56:11 PM | USDCAD | DOWN | 3.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/25 9:56:11 PM | PALLADIUM | UP | 3.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/25 9:56:11 PM | XRP | UP | 3.8 min | -0.407% | 1¢ | ❌ Lost | -$0.15 |
| 10/25 9:56:11 PM | PLATINUM | UP | 3.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/25 9:56:11 PM | BNB | UP | 3.8 min | -0.367% | 12¢ | ❌ Lost | -$0.15 |
| 10/25 9:56:11 PM | ETH | UP | 3.8 min | -0.332% | 17¢ | ❌ Lost | -$0.15 |
| 10/25 9:44:13 PM | PLATINUM | UP | 46 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/25 9:44:13 PM | BNB | UP | 46 sec | -0.080% | 0¢ | ❌ Lost | $0.00 |
| 10/25 9:43:57 PM | ZEC | UP | 62 sec | -0.356% | 0¢ | ❌ Lost | $0.00 |
| 10/25 9:43:57 PM | GOLD | UP | 62 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/25 9:43:57 PM | DOGE | UP | 62 sec | -0.092% | 1¢ | ❌ Lost | -$0.15 |
| 10/25 9:43:57 PM | BTC | UP | 62 sec | -0.121% | 0¢ | ❌ Lost | $0.00 |
| 10/25 9:43:57 PM | COPPER | UP | 62 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/25 9:43:26 PM | NATGAS | UP | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/25 9:43:26 PM | SILVER | UP | 1.6 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/25 9:43:10 PM | HYPE | UP | 1.8 min | -0.247% | 1¢ | ❌ Lost | -$0.15 |
| 10/25 9:43:10 PM | ETH | UP | 1.8 min | -0.192% | 1¢ | ❌ Lost | -$0.15 |
| 10/25 9:43:10 PM | SOL | UP | 1.8 min | -0.281% | 0¢ | ❌ Lost | $0.00 |
| 10/25 9:29:53 PM | EURUSD | DOWN | 6 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/25 9:29:53 PM | ETH | UP | 6 sec | -0.043% | 0¢ | ❌ Lost | $0.00 |
| 10/25 9:29:53 PM | USDJPY | UP | 6 sec | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
