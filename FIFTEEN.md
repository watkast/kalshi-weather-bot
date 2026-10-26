# 15-Minute 1¢ Study

*Updated Sun Oct 25, 7:07 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 2705 finished bets | 1% | $84.50 | +27% | +3.12¢ | $33.80 / $50.70 |

*Expect about **97 buys a day** (~$14.61/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 2500 | $59.25 | +21% |
| Volatility model ≥ 2%, hold to the close | 4998 | -$10.75 | -2% |
| Momentum model ≥ 2%, hold to the close | 4159 | -$25.95 | -5% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 31939 | 31931 | 120 (0%) | 1.07% | -$2,199.00 (-57%) | Hold to the close: -$2,199.00 (-57%) |

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
| Volatility model | 20629 | 4.7% | 0.4% (85) | -656% | ❌ Worse |
| Momentum model | 20629 | 4.6% | 0.4% (85) | -680% | ❌ Worse |
| Mean-reversion model | 20629 | 7.9% | 0.4% (85) | -794% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 20629 | 85 | -48% | -88% | -87% | -85% |
| Volatility model ≥ 2% | 4998 | 43 | -2% | -78% | -77% | -74% |
| Volatility model ≥ 5% | 2705 | 28 | +27% | -75% | -74% | -70% |
| Volatility model ≥ 10% | 1532 | 18 | +64% | -66% | -65% | -61% |
| Momentum model ≥ 2% | 4159 | 33 | -5% | -80% | -80% | -77% |
| Momentum model ≥ 5% | 2500 | 24 | +21% | -77% | -76% | -72% |
| Momentum model ≥ 10% | 1631 | 16 | +34% | -71% | -70% | -65% |
| Mean-reversion model ≥ 2% | 8316 | 56 | -27% | -83% | -83% | -80% |
| Mean-reversion model ≥ 5% | 5830 | 47 | -11% | -81% | -80% | -78% |
| Mean-reversion model ≥ 10% | 3883 | 33 | -4% | -78% | -78% | -76% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 20829 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 7401 | 2% | 2% | 1% | 1% | 0% | 0% |
| Financials | 3701 | 2% | 1% | 1% | 1% | 0% | 0% |
| **All** | 31931 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 120 | 0% | -$2,199.00 | -57% | — |
| Sell at 2¢ | 1185 | 4% | -$3,402.90 | -88% | 47 sec |
| Sell at 3¢ | 813 | 3% | -$3,393.93 | -87% | 48 sec |
| Sell at 5¢ | 568 | 2% | -$3,341.80 | -86% | 61 sec |
| Sell at 10¢ | 350 | 1% | -$3,210.50 | -83% | 65 sec |
| Sell at 25¢ | 189 | 1% | -$2,973.41 | -77% | 82 sec |
| Sell at 50¢ | 122 | 0% | -$2,691.50 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 1404 | 7 | 11% | 4% | -52% | -81% | -83% |
| 2–5 min | 10229 | 55 | 7% | 3% | -47% | -87% | -87% |
| 1–2 min | 8080 | 30 | 3% | 1% | -59% | -92% | -91% |
| Under 1 min | 12214 | 28 | 1% | 0% | -67% | -86% | -86% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 2334 | 12 | 5% | 2% | -35% | -89% | -89% |
| HYPE | 2327 | 8 | 5% | 3% | -57% | -89% | -87% |
| BNB | 2323 | 13 | 5% | 2% | -31% | -84% | -83% |
| SOL | 2319 | 6 | 3% | 2% | -68% | -92% | -92% |
| ETH | 2315 | 11 | 6% | 3% | -43% | -86% | -86% |
| DOGE | 2308 | 4 | 4% | 2% | -78% | -91% | -90% |
| NEAR | 2304 | 12 | 5% | 2% | -32% | -81% | -81% |
| XRP | 2304 | 9 | 3% | 1% | -52% | -89% | -88% |
| BTC | 2295 | 12 | 5% | 2% | -30% | -88% | -89% |
| GOLD | 1197 | 4 | 4% | 2% | -60% | -81% | -83% |
| SILVER | 1163 | 5 | 4% | 2% | -50% | -82% | -82% |
| WTI | 1149 | 3 | 3% | 1% | -69% | -94% | -95% |
| PLATINUM | 1017 | 0 | 1% | 1% | -100% | -98% | -97% |
| COPPER | 992 | 4 | 1% | 1% | -62% | -69% | -69% |
| EURUSD | 948 | 3 | 2% | 1% | -70% | -86% | -86% |
| NATGAS | 941 | 5 | 2% | 1% | -50% | -87% | -86% |
| PALLADIUM | 903 | 2 | 1% | 0% | -79% | -88% | -88% |
| GBPUSD | 893 | 1 | 2% | 1% | -90% | -96% | -97% |
| USDJPY | 876 | 5 | 1% | 1% | -47% | -98% | -97% |
| AUDUSD | 436 | 0 | 1% | 0% | -100% | -98% | -98% |
| USDCAD | 396 | 0 | 2% | 0% | -100% | -97% | -99% |
| 10YRRATE | 43 | 0 | 0% | 0% | -100% | -100% | -100% |
| 2YRRATE | 40 | 1 | 2% | 0% | +133% | +138% | +133% |
| 30YRRATE | 39 | 0 | 0% | 0% | -100% | -100% | -100% |
| BRENT | 39 | 0 | 0% | 0% | -100% | -100% | -100% |
| 5YRRATE | 30 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 16178 | 66 | 4% | 2% | -53% | -87% | -87% |
| DOWN (bought NO) | 15753 | 54 | 4% | 1% | -60% | -88% | -88% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 3489 | 18 | 2% | 1% | -13% | -80% | -80% |
| 0.05–0.1% | 3590 | 11 | 3% | 2% | -55% | -92% | -92% |
| 0.1–0.2% | 5395 | 20 | 5% | 2% | -54% | -89% | -89% |
| 0.2–0.5% | 6045 | 28 | 6% | 3% | -49% | -87% | -86% |
| Over 0.5% | 2306 | 10 | 7% | 3% | -55% | -87% | -88% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 7904 | 32 | 4% | 2% | -54% | -85% | -85% |
| Morning (6am–12pm) | 7781 | 35 | 4% | 2% | -49% | -88% | -87% |
| Afternoon (12–6pm) | 7607 | 24 | 4% | 2% | -63% | -87% | -88% |
| Evening (6pm–12am) | 8639 | 29 | 3% | 2% | -61% | -90% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,821 |
| Time from buy to best bounce (bounced bets) | 49 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/25 6:59:59 PM | USDJPY | DOWN | 0 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/25 6:59:59 PM | COPPER | UP | 0 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/25 6:59:59 PM | ZEC | DOWN | 0 sec | +0.060% | 0¢ | ❌ Lost | -$0.15 |
| 10/25 6:59:59 PM | SOL | DOWN | 0 sec | +0.070% | 0¢ | ❌ Lost | $0.00 |
| 10/25 6:59:44 PM | BNB | UP | 15 sec | +0.028% | 0¢ | ❌ Lost | $0.00 |
| 10/25 6:59:44 PM | DOGE | UP | 15 sec | -0.091% | 0¢ | ❌ Lost | $0.00 |
| 10/25 6:59:28 PM | HYPE | UP | 31 sec | -0.057% | 0¢ | ❌ Lost | $0.00 |
| 10/25 6:59:28 PM | PALLADIUM | UP | 31 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/25 6:59:28 PM | GOLD | UP | 31 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/25 6:59:28 PM | AUDUSD | DOWN | 31 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/25 6:59:12 PM | BTC | UP | 47 sec | -0.084% | 0¢ | ❌ Lost | $0.00 |
| 10/25 6:58:56 PM | XRP | UP | 64 sec | -0.185% | 1¢ | ❌ Lost | -$0.15 |
| 10/25 6:58:56 PM | NEAR | UP | 64 sec | -0.417% | 0¢ | ❌ Lost | $0.00 |
| 10/25 6:58:56 PM | SILVER | UP | 64 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/25 6:58:56 PM | NATGAS | UP | 64 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/25 6:58:56 PM | PLATINUM | UP | 64 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/25 6:58:07 PM | USDCAD | UP | 1.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/25 6:57:05 PM | GBPUSD | DOWN | 2.9 min | — | 2¢ | ❌ Lost | -$0.15 |
| 10/25 6:55:14 PM | ETH | UP | 4.8 min | -0.430% | 20¢ | ❌ Lost | -$0.15 |
| 10/25 6:44:49 PM | ZEC | UP | 10 sec | -0.176% | 0¢ | ❌ Lost | $0.00 |
| 10/25 6:44:49 PM | DOGE | UP | 10 sec | -0.096% | 0¢ | ❌ Lost | -$0.15 |
| 10/25 6:44:34 PM | XRP | UP | 25 sec | -0.062% | 0¢ | ❌ Lost | -$0.15 |
| 10/25 6:44:34 PM | BNB | DOWN | 25 sec | -0.001% | 0¢ | ❌ Lost | -$0.15 |
| 10/25 6:44:34 PM | NEAR | UP | 25 sec | -0.324% | 0¢ | ❌ Lost | $0.00 |
| 10/25 6:44:34 PM | NATGAS | UP | 25 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/25 6:44:34 PM | SOL | UP | 25 sec | -0.084% | 0¢ | ❌ Lost | $0.00 |
| 10/25 6:44:18 PM | USDCAD | UP | 41 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/25 6:44:02 PM | EURUSD | UP | 57 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/25 6:43:46 PM | PLATINUM | UP | 73 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/25 6:43:31 PM | BTC | UP | 88 sec | -0.135% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
