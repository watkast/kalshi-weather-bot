# 15-Minute 1¢ Study

*Updated Thu Oct 29, 10:54 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 3139 finished bets | 1% | $82.10 | +23% | +2.62¢ | $77.85 / $4.25 |

*Expect about **98 buys a day** (~$14.75/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 2906 | $31.25 | +10% |
| Volatility model ≥ 2%, hold to the close | 5812 | -$5.75 | -1% |
| Volatility model ≥ 5%, sell at 50¢ | 3139 | -$72.15 | -21% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 38806 | 38795 | 143 (0%) | 1.07% | -$2,736.65 (-58%) | Hold to the close: -$2,736.65 (-58%) |

*In play or awaiting result: 10. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 23858 | 4.7% | 0.4% (93) | -680% | ❌ Worse |
| Momentum model | 23858 | 4.5% | 0.4% (93) | -703% | ❌ Worse |
| Mean-reversion model | 23858 | 8.0% | 0.4% (93) | -828% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 23858 | 93 | -51% | -88% | -87% | -85% |
| Volatility model ≥ 2% | 5812 | 50 | -1% | -79% | -77% | -74% |
| Volatility model ≥ 5% | 3139 | 31 | +23% | -75% | -74% | -70% |
| Volatility model ≥ 10% | 1770 | 19 | +52% | -68% | -67% | -64% |
| Momentum model ≥ 2% | 4797 | 34 | -15% | -81% | -80% | -77% |
| Momentum model ≥ 5% | 2906 | 25 | +10% | -78% | -78% | -73% |
| Momentum model ≥ 10% | 1893 | 17 | +24% | -73% | -72% | -68% |
| Mean-reversion model ≥ 2% | 9785 | 64 | -29% | -83% | -83% | -80% |
| Mean-reversion model ≥ 5% | 6857 | 54 | -13% | -81% | -80% | -77% |
| Mean-reversion model ≥ 10% | 4572 | 39 | -3% | -79% | -78% | -76% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 24059 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 9352 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 5384 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 38795 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 143 | 0% | -$2,736.65 | -58% | — |
| Sell at 2¢ | 1492 | 4% | -$4,154.73 | -88% | 47 sec |
| Sell at 3¢ | 1028 | 3% | -$4,141.73 | -87% | 49 sec |
| Sell at 5¢ | 715 | 2% | -$4,063.90 | -86% | 63 sec |
| Sell at 10¢ | 432 | 1% | -$3,892.73 | -82% | 65 sec |
| Sell at 25¢ | 226 | 1% | -$3,598.59 | -76% | 83 sec |
| Sell at 50¢ | 146 | 0% | -$3,277.15 | -69% | 1.9 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 9 | 0 | 33% | 22% | -100% | -42% | -13% |
| 5–10 min | 1807 | 8 | 11% | 4% | -58% | -80% | -81% |
| 2–5 min | 12369 | 68 | 7% | 3% | -46% | -87% | -86% |
| 1–2 min | 9813 | 34 | 3% | 1% | -62% | -92% | -92% |
| Under 1 min | 14797 | 33 | 1% | 0% | -68% | -86% | -86% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 2692 | 12 | 5% | 3% | -43% | -88% | -88% |
| HYPE | 2688 | 8 | 5% | 3% | -63% | -89% | -87% |
| BNB | 2685 | 15 | 5% | 2% | -30% | -85% | -84% |
| SOL | 2680 | 7 | 4% | 2% | -67% | -91% | -91% |
| ETH | 2673 | 11 | 6% | 3% | -50% | -86% | -85% |
| DOGE | 2673 | 6 | 4% | 2% | -72% | -90% | -89% |
| BTC | 2657 | 13 | 5% | 2% | -34% | -88% | -89% |
| XRP | 2656 | 11 | 3% | 1% | -49% | -89% | -89% |
| NEAR | 2655 | 12 | 5% | 2% | -41% | -83% | -83% |
| GOLD | 1468 | 5 | 4% | 2% | -59% | -82% | -84% |
| SILVER | 1436 | 7 | 4% | 2% | -42% | -82% | -81% |
| WTI | 1421 | 4 | 3% | 1% | -66% | -93% | -94% |
| PLATINUM | 1271 | 2 | 2% | 1% | -85% | -97% | -96% |
| COPPER | 1209 | 5 | 1% | 1% | -61% | -75% | -74% |
| EURUSD | 1208 | 3 | 2% | 1% | -77% | -88% | -88% |
| NATGAS | 1169 | 7 | 2% | 1% | -44% | -80% | -80% |
| GBPUSD | 1141 | 2 | 2% | 1% | -84% | -96% | -96% |
| PALLADIUM | 1139 | 2 | 1% | 0% | -84% | -90% | -90% |
| USDJPY | 1128 | 5 | 2% | 1% | -59% | -97% | -96% |
| AUDUSD | 677 | 4 | 2% | 1% | -45% | -83% | -82% |
| USDCAD | 638 | 0 | 2% | 0% | -100% | -97% | -98% |
| BRENT | 239 | 0 | 0% | 0% | -100% | -99% | -99% |
| 10YRRATE | 158 | 0 | 4% | 1% | -100% | -92% | -90% |
| 30YRRATE | 152 | 0 | 1% | 0% | -100% | -98% | -97% |
| 2YRRATE | 146 | 1 | 5% | 1% | -36% | -28% | -27% |
| 5YRRATE | 136 | 1 | 7% | 3% | -31% | -89% | -90% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 19696 | 78 | 4% | 2% | -55% | -88% | -87% |
| DOWN (bought NO) | 19099 | 65 | 4% | 2% | -61% | -88% | -88% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 3883 | 19 | 2% | 1% | -15% | -81% | -81% |
| 0.05–0.1% | 4101 | 14 | 3% | 2% | -49% | -92% | -92% |
| 0.1–0.2% | 6203 | 22 | 4% | 2% | -56% | -90% | -89% |
| 0.2–0.5% | 7128 | 30 | 6% | 3% | -53% | -87% | -86% |
| Over 0.5% | 2740 | 10 | 7% | 3% | -62% | -86% | -86% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 9458 | 35 | 4% | 2% | -58% | -86% | -86% |
| Morning (6am–12pm) | 9668 | 43 | 4% | 2% | -50% | -86% | -85% |
| Afternoon (12–6pm) | 9178 | 31 | 4% | 2% | -60% | -88% | -88% |
| Evening (6pm–12am) | 10491 | 34 | 3% | 2% | -63% | -91% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,497 |
| Time from buy to best bounce (bounced bets) | 51 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/29 10:54:48 PM | GOLD | DOWN | 5.2 min | — | — | In play | — |
| 10/29 10:44:44 PM | SOL | UP | 16 sec | -0.109% | 0¢ | ❌ Lost | $0.00 |
| 10/29 10:44:44 PM | NEAR | DOWN | 16 sec | -0.074% | 0¢ | ❌ Lost | $0.00 |
| 10/29 10:44:44 PM | ZEC | UP | 16 sec | -0.051% | 0¢ | ❌ Lost | $0.00 |
| 10/29 10:44:44 PM | BRENT | DOWN | 16 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/29 10:44:11 PM | ETH | DOWN | 49 sec | +0.051% | 0¢ | ❌ Lost | $0.00 |
| 10/29 10:44:11 PM | PLATINUM | UP | 49 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/29 10:43:53 PM | BNB | UP | 67 sec | -0.153% | 0¢ | ❌ Lost | $0.00 |
| 10/29 10:43:53 PM | BTC | UP | 67 sec | -0.074% | 1¢ | ❌ Lost | -$0.15 |
| 10/29 10:43:53 PM | DOGE | DOWN | 67 sec | +0.071% | 1¢ | ❌ Lost | -$0.15 |
| 10/29 10:43:53 PM | HYPE | UP | 67 sec | -0.146% | 0¢ | ❌ Lost | $0.00 |
| 10/29 10:43:06 PM | EURUSD | UP | 1.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/29 10:42:34 PM | PALLADIUM | UP | 2.4 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/29 10:42:01 PM | GOLD | UP | 3.0 min | — | 2¢ | ❌ Lost | -$0.15 |
| 10/29 10:40:07 PM | SILVER | UP | 4.9 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/29 10:29:57 PM | USDJPY | UP | 2 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/29 10:29:41 PM | PLATINUM | DOWN | 18 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/29 10:29:25 PM | BNB | UP | 34 sec | -0.102% | 1¢ | ❌ Lost | $0.00 |
| 10/29 10:29:25 PM | WTI | UP | 34 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/29 10:29:25 PM | XRP | DOWN | 34 sec | +0.032% | 0¢ | ❌ Lost | -$0.15 |
| 10/29 10:29:08 PM | SOL | DOWN | 51 sec | +0.128% | 0¢ | ❌ Lost | -$0.15 |
| 10/29 10:28:36 PM | DOGE | DOWN | 83 sec | +0.124% | 1¢ | ❌ Lost | -$0.15 |
| 10/29 10:28:36 PM | HYPE | DOWN | 83 sec | +0.387% | 0¢ | ❌ Lost | -$0.15 |
| 10/29 10:28:20 PM | EURUSD | UP | 1.6 min | — | 3¢ | ❌ Lost | -$0.15 |
| 10/29 10:28:04 PM | PALLADIUM | DOWN | 1.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/29 10:27:45 PM | SILVER | DOWN | 2.2 min | — | 0¢ | ❌ Lost | $0.00 |
| 10/29 10:27:45 PM | ETH | DOWN | 2.2 min | +0.222% | 1¢ | ❌ Lost | -$0.15 |
| 10/29 10:27:45 PM | ZEC | DOWN | 2.2 min | +0.442% | 1¢ | ❌ Lost | -$0.15 |
| 10/29 10:27:29 PM | COPPER | DOWN | 2.5 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/29 10:27:13 PM | NEAR | DOWN | 2.8 min | +0.375% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
