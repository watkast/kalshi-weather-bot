# 15-Minute 1¢ Study

*Updated Sun Oct 25, 7:38 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 2706 finished bets | 1% | $84.35 | +27% | +3.12¢ | $33.65 / $50.70 |

*Expect about **97 buys a day** (~$14.61/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 2500 | $59.25 | +21% |
| Volatility model ≥ 2%, hold to the close | 4999 | -$10.90 | -2% |
| Momentum model ≥ 2%, hold to the close | 4159 | -$25.95 | -5% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 31973 | 31965 | 120 (0%) | 1.07% | -$2,202.90 (-57%) | Hold to the close: -$2,202.90 (-57%) |

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
| Volatility model | 20646 | 4.7% | 0.4% (85) | -656% | ❌ Worse |
| Momentum model | 20646 | 4.6% | 0.4% (85) | -680% | ❌ Worse |
| Mean-reversion model | 20646 | 7.9% | 0.4% (85) | -794% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 20646 | 85 | -48% | -88% | -87% | -85% |
| Volatility model ≥ 2% | 4999 | 43 | -2% | -78% | -77% | -74% |
| Volatility model ≥ 5% | 2706 | 28 | +27% | -75% | -73% | -70% |
| Volatility model ≥ 10% | 1532 | 18 | +64% | -66% | -65% | -61% |
| Momentum model ≥ 2% | 4159 | 33 | -5% | -80% | -80% | -77% |
| Momentum model ≥ 5% | 2500 | 24 | +21% | -77% | -76% | -72% |
| Momentum model ≥ 10% | 1631 | 16 | +34% | -71% | -70% | -65% |
| Mean-reversion model ≥ 2% | 8324 | 56 | -27% | -83% | -83% | -80% |
| Mean-reversion model ≥ 5% | 5834 | 47 | -11% | -81% | -80% | -78% |
| Mean-reversion model ≥ 10% | 3887 | 33 | -4% | -78% | -78% | -76% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 20846 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 7412 | 2% | 2% | 1% | 1% | 0% | 0% |
| Financials | 3707 | 2% | 1% | 1% | 1% | 0% | 0% |
| **All** | 31965 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 120 | 0% | -$2,202.90 | -57% | — |
| Sell at 2¢ | 1188 | 4% | -$3,406.02 | -88% | 47 sec |
| Sell at 3¢ | 816 | 3% | -$3,396.66 | -87% | 48 sec |
| Sell at 5¢ | 570 | 2% | -$3,344.40 | -86% | 61 sec |
| Sell at 10¢ | 352 | 1% | -$3,211.78 | -83% | 65 sec |
| Sell at 25¢ | 191 | 1% | -$2,970.69 | -77% | 82 sec |
| Sell at 50¢ | 122 | 0% | -$2,695.40 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 1404 | 7 | 11% | 4% | -52% | -81% | -83% |
| 2–5 min | 10239 | 55 | 7% | 3% | -47% | -87% | -87% |
| 1–2 min | 8087 | 30 | 3% | 1% | -59% | -92% | -91% |
| Under 1 min | 12231 | 28 | 1% | 0% | -67% | -86% | -86% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 2335 | 12 | 5% | 2% | -35% | -89% | -89% |
| HYPE | 2329 | 8 | 5% | 3% | -58% | -89% | -87% |
| BNB | 2325 | 13 | 5% | 3% | -31% | -84% | -83% |
| SOL | 2321 | 6 | 3% | 2% | -68% | -92% | -92% |
| ETH | 2317 | 11 | 6% | 3% | -43% | -86% | -85% |
| DOGE | 2310 | 4 | 4% | 2% | -78% | -91% | -90% |
| NEAR | 2306 | 12 | 5% | 2% | -32% | -81% | -81% |
| XRP | 2306 | 9 | 3% | 1% | -52% | -89% | -88% |
| BTC | 2297 | 12 | 5% | 2% | -30% | -88% | -89% |
| GOLD | 1199 | 4 | 4% | 2% | -60% | -81% | -83% |
| SILVER | 1165 | 5 | 4% | 2% | -50% | -82% | -82% |
| WTI | 1150 | 3 | 3% | 1% | -69% | -94% | -95% |
| PLATINUM | 1019 | 0 | 1% | 1% | -100% | -98% | -97% |
| COPPER | 993 | 4 | 1% | 1% | -62% | -69% | -69% |
| EURUSD | 950 | 3 | 2% | 1% | -71% | -86% | -86% |
| NATGAS | 943 | 5 | 2% | 1% | -51% | -87% | -86% |
| PALLADIUM | 904 | 2 | 1% | 0% | -79% | -88% | -88% |
| GBPUSD | 895 | 1 | 2% | 1% | -90% | -96% | -97% |
| USDJPY | 877 | 5 | 1% | 1% | -47% | -98% | -97% |
| AUDUSD | 436 | 0 | 1% | 0% | -100% | -98% | -98% |
| USDCAD | 397 | 0 | 2% | 0% | -100% | -97% | -99% |
| 10YRRATE | 43 | 0 | 0% | 0% | -100% | -100% | -100% |
| 2YRRATE | 40 | 1 | 2% | 0% | +133% | +138% | +133% |
| 30YRRATE | 39 | 0 | 0% | 0% | -100% | -100% | -100% |
| BRENT | 39 | 0 | 0% | 0% | -100% | -100% | -100% |
| 5YRRATE | 30 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 16200 | 66 | 4% | 2% | -53% | -87% | -87% |
| DOWN (bought NO) | 15765 | 54 | 4% | 2% | -61% | -88% | -88% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 3491 | 18 | 2% | 1% | -13% | -80% | -80% |
| 0.05–0.1% | 3593 | 11 | 3% | 2% | -55% | -92% | -92% |
| 0.1–0.2% | 5398 | 20 | 5% | 2% | -54% | -89% | -89% |
| 0.2–0.5% | 6052 | 28 | 6% | 3% | -49% | -87% | -86% |
| Over 0.5% | 2308 | 10 | 7% | 3% | -55% | -87% | -88% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 7904 | 32 | 4% | 2% | -54% | -85% | -85% |
| Morning (6am–12pm) | 7781 | 35 | 4% | 2% | -49% | -88% | -87% |
| Afternoon (12–6pm) | 7607 | 24 | 4% | 2% | -63% | -87% | -88% |
| Evening (6pm–12am) | 8673 | 29 | 3% | 2% | -62% | -90% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,820 |
| Time from buy to best bounce (bounced bets) | 49 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/25 7:29:45 PM | DOGE | UP | 14 sec | -0.095% | 0¢ | ❌ Lost | $0.00 |
| 10/25 7:29:45 PM | SOL | UP | 14 sec | -0.026% | 0¢ | ❌ Lost | $0.00 |
| 10/25 7:29:45 PM | HYPE | UP | 14 sec | -0.052% | 0¢ | ❌ Lost | $0.00 |
| 10/25 7:29:45 PM | NATGAS | DOWN | 14 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/25 7:29:29 PM | BTC | UP | 30 sec | -0.066% | 0¢ | ❌ Lost | $0.00 |
| 10/25 7:29:29 PM | EURUSD | UP | 30 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/25 7:29:29 PM | SILVER | UP | 30 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/25 7:29:29 PM | XRP | DOWN | 30 sec | +0.124% | 0¢ | ❌ Lost | $0.00 |
| 10/25 7:28:57 PM | NEAR | UP | 62 sec | -0.583% | 0¢ | ❌ Lost | $0.00 |
| 10/25 7:28:57 PM | GBPUSD | UP | 62 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/25 7:28:42 PM | GOLD | UP | 77 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/25 7:28:26 PM | PALLADIUM | UP | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/25 7:27:16 PM | PLATINUM | UP | 2.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/25 7:27:00 PM | BNB | DOWN | 3.0 min | +0.150% | 26¢ | ❌ Lost | -$0.15 |
| 10/25 7:25:23 PM | ETH | DOWN | 4.6 min | +0.451% | 41¢ | ❌ Lost | -$0.15 |
| 10/25 7:14:53 PM | PLATINUM | DOWN | 6 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/25 7:14:38 PM | BNB | DOWN | 22 sec | +0.030% | 0¢ | ❌ Lost | $0.00 |
| 10/25 7:14:38 PM | SILVER | DOWN | 22 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/25 7:14:22 PM | COPPER | DOWN | 38 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/25 7:14:22 PM | NATGAS | DOWN | 38 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/25 7:14:06 PM | USDJPY | UP | 54 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/25 7:14:06 PM | EURUSD | DOWN | 54 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/25 7:14:06 PM | WTI | UP | 54 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/25 7:14:06 PM | GBPUSD | DOWN | 54 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/25 7:13:50 PM | ZEC | UP | 70 sec | -0.376% | 1¢ | ❌ Lost | -$0.15 |
| 10/25 7:13:35 PM | BTC | UP | 85 sec | -0.137% | 1¢ | ❌ Lost | -$0.15 |
| 10/25 7:13:03 PM | USDCAD | UP | 1.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/25 7:12:47 PM | HYPE | UP | 2.2 min | -0.271% | 1¢ | ❌ Lost | -$0.15 |
| 10/25 7:12:47 PM | XRP | UP | 2.2 min | -0.363% | 1¢ | ❌ Lost | -$0.15 |
| 10/25 7:12:31 PM | GOLD | DOWN | 2.5 min | — | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
