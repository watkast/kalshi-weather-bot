# 15-Minute 1¢ Study

*Updated Wed Nov 4, 1:05 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 3644 finished bets | 1% | $125.50 | +31% | +3.44¢ | $77.95 / $47.55 |

*Expect about **97 buys a day** (~$14.55/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 3381 | $52.80 | +14% |
| Volatility model ≥ 2%, hold to the close | 6758 | $37.40 | +5% |
| Momentum model ≥ 2%, hold to the close | 5570 | -$40.45 | -6% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 45531 | 45520 | 169 (0%) | 1.07% | -$3,182.65 (-57%) | Hold to the close: -$3,182.65 (-57%) |

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
| Volatility model | 27802 | 4.7% | 0.4% (109) | -675% | ❌ Worse |
| Momentum model | 27802 | 4.6% | 0.4% (109) | -702% | ❌ Worse |
| Mean-reversion model | 27802 | 8.1% | 0.4% (109) | -823% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 27802 | 109 | -50% | -88% | -87% | -85% |
| Volatility model ≥ 2% | 6758 | 61 | +5% | -79% | -78% | -74% |
| Volatility model ≥ 5% | 3644 | 38 | +31% | -76% | -75% | -71% |
| Volatility model ≥ 10% | 2071 | 23 | +59% | -71% | -69% | -66% |
| Momentum model ≥ 2% | 5570 | 43 | -6% | -81% | -81% | -78% |
| Momentum model ≥ 5% | 3381 | 30 | +14% | -79% | -79% | -75% |
| Momentum model ≥ 10% | 2204 | 19 | +21% | -75% | -74% | -70% |
| Mean-reversion model ≥ 2% | 11509 | 79 | -25% | -83% | -83% | -81% |
| Mean-reversion model ≥ 5% | 8085 | 68 | -7% | -81% | -80% | -78% |
| Mean-reversion model ≥ 10% | 5417 | 48 | +1% | -80% | -79% | -77% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 28007 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 10824 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 6689 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 45520 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 169 | 0% | -$3,182.65 | -57% | — |
| Sell at 2¢ | 1786 | 4% | -$4,832.29 | -87% | 47 sec |
| Sell at 3¢ | 1221 | 3% | -$4,820.46 | -87% | 49 sec |
| Sell at 5¢ | 845 | 2% | -$4,719.40 | -85% | 63 sec |
| Sell at 10¢ | 511 | 1% | -$4,515.24 | -81% | 65 sec |
| Sell at 25¢ | 268 | 1% | -$4,185.57 | -75% | 83 sec |
| Sell at 50¢ | 172 | 0% | -$3,813.65 | -69% | 1.8 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 11 | 0 | 27% | 18% | -100% | -53% | -29% |
| 5–10 min | 2253 | 10 | 11% | 4% | -58% | -81% | -83% |
| 2–5 min | 14656 | 79 | 7% | 3% | -47% | -87% | -86% |
| 1–2 min | 11471 | 39 | 3% | 1% | -62% | -92% | -92% |
| Under 1 min | 17129 | 41 | 1% | 0% | -66% | -85% | -84% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 3137 | 13 | 5% | 2% | -47% | -88% | -88% |
| SOL | 3132 | 12 | 4% | 2% | -51% | -90% | -90% |
| HYPE | 3124 | 9 | 5% | 2% | -64% | -89% | -87% |
| BNB | 3124 | 17 | 5% | 2% | -32% | -85% | -84% |
| DOGE | 3112 | 6 | 4% | 2% | -76% | -90% | -90% |
| ETH | 3106 | 12 | 7% | 3% | -53% | -85% | -85% |
| BTC | 3095 | 15 | 5% | 2% | -34% | -87% | -89% |
| NEAR | 3092 | 15 | 5% | 2% | -37% | -84% | -84% |
| XRP | 3085 | 12 | 3% | 1% | -52% | -89% | -89% |
| GOLD | 1676 | 5 | 5% | 2% | -64% | -81% | -83% |
| WTI | 1630 | 5 | 4% | 1% | -63% | -92% | -93% |
| SILVER | 1628 | 8 | 5% | 2% | -42% | -82% | -81% |
| PLATINUM | 1460 | 4 | 2% | 1% | -74% | -96% | -96% |
| EURUSD | 1405 | 3 | 2% | 1% | -80% | -89% | -89% |
| COPPER | 1377 | 6 | 2% | 1% | -59% | -70% | -70% |
| GBPUSD | 1331 | 3 | 2% | 1% | -79% | -96% | -96% |
| NATGAS | 1324 | 8 | 2% | 1% | -44% | -75% | -75% |
| USDJPY | 1312 | 5 | 2% | 1% | -64% | -97% | -97% |
| PALLADIUM | 1308 | 3 | 1% | 1% | -79% | -91% | -91% |
| AUDUSD | 861 | 4 | 2% | 1% | -57% | -86% | -86% |
| USDCAD | 829 | 0 | 2% | 0% | -100% | -97% | -98% |
| BRENT | 421 | 0 | 1% | 1% | -100% | -98% | -97% |
| 10YRRATE | 257 | 1 | 5% | 2% | -64% | -56% | -54% |
| 2YRRATE | 237 | 2 | 3% | 0% | -21% | -15% | -15% |
| 30YRRATE | 237 | 0 | 1% | 0% | -100% | -98% | -97% |
| 5YRRATE | 220 | 1 | 5% | 2% | -58% | -92% | -94% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 23119 | 90 | 4% | 2% | -55% | -88% | -87% |
| DOWN (bought NO) | 22401 | 79 | 4% | 2% | -60% | -86% | -87% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 4512 | 22 | 2% | 1% | -15% | -83% | -82% |
| 0.05–0.1% | 4765 | 18 | 3% | 2% | -43% | -91% | -90% |
| 0.1–0.2% | 7216 | 25 | 4% | 2% | -57% | -90% | -89% |
| 0.2–0.5% | 8334 | 33 | 6% | 3% | -56% | -87% | -86% |
| Over 0.5% | 3172 | 13 | 7% | 3% | -58% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 11276 | 40 | 4% | 2% | -60% | -87% | -87% |
| Morning (6am–12pm) | 11422 | 50 | 4% | 2% | -50% | -86% | -85% |
| Afternoon (12–6pm) | 10619 | 39 | 4% | 2% | -57% | -86% | -86% |
| Evening (6pm–12am) | 12203 | 40 | 3% | 2% | -62% | -90% | -89% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,684 |
| Time from buy to best bounce (bounced bets) | 51 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/4 12:59:58 PM | 2YRRATE | DOWN | 2 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/4 12:59:58 PM | GOLD | DOWN | 2 sec | — | 0¢ | ❌ Lost | $0.00 |
| 11/4 12:59:58 PM | USDJPY | DOWN | 2 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/4 12:59:58 PM | NATGAS | DOWN | 2 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/4 12:59:58 PM | AUDUSD | DOWN | 2 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/4 12:59:58 PM | 5YRRATE | DOWN | 2 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/4 12:59:42 PM | PLATINUM | DOWN | 18 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/4 12:59:42 PM | USDCAD | UP | 18 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/4 12:59:26 PM | BRENT | DOWN | 34 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/4 12:58:39 PM | WTI | DOWN | 80 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 11/4 12:58:39 PM | GBPUSD | DOWN | 80 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/4 12:58:23 PM | EURUSD | DOWN | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/4 12:58:07 PM | BTC | UP | 1.9 min | -0.149% | 1¢ | ❌ Lost | -$0.15 |
| 11/4 12:57:35 PM | HYPE | UP | 2.4 min | -0.600% | 0¢ | ❌ Lost | $0.00 |
| 11/4 12:57:19 PM | DOGE | UP | 2.7 min | -0.318% | 1¢ | ❌ Lost | -$0.15 |
| 11/4 12:56:47 PM | XRP | UP | 3.2 min | -0.330% | 0¢ | ❌ Lost | $0.00 |
| 11/4 12:56:15 PM | ZEC | UP | 3.8 min | -0.613% | 1¢ | ❌ Lost | -$0.15 |
| 11/4 12:56:15 PM | NEAR | UP | 3.8 min | -0.726% | 1¢ | ❌ Lost | -$0.15 |
| 11/4 12:55:59 PM | ETH | UP | 4.0 min | -0.388% | 1¢ | ❌ Lost | -$0.15 |
| 11/4 12:53:16 PM | SOL | UP | 6.7 min | -0.725% | 2¢ | ❌ Lost | -$0.15 |
| 11/4 12:53:00 PM | BNB | UP | 7.0 min | -0.337% | 1¢ | ❌ Lost | -$0.15 |
| 11/4 10:25:43 AM | EURUSD | DOWN | 4.3 min | — | — | ❌ Lost | -$0.15 |
| 11/4 10:14:35 AM | SILVER | DOWN | 24 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/4 10:14:35 AM | BRENT | DOWN | 24 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/4 10:13:47 AM | PALLADIUM | DOWN | 72 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/4 10:13:00 AM | BTC | UP | 2.0 min | -0.253% | 1¢ | ❌ Lost | -$0.15 |
| 11/4 10:12:44 AM | HYPE | UP | 2.3 min | -0.748% | 0¢ | ❌ Lost | $0.00 |
| 11/4 10:12:29 AM | ETH | UP | 2.5 min | -0.360% | 1¢ | ❌ Lost | -$0.15 |
| 11/4 10:12:29 AM | NEAR | UP | 2.5 min | -1.167% | 0¢ | ❌ Lost | -$0.15 |
| 11/4 10:12:13 AM | BNB | UP | 2.8 min | -0.342% | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
