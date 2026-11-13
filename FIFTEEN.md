# 15-Minute 1¢ Study

*Updated Fri Nov 13, 6:29 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 4281 finished bets | 1% | $168.80 | +36% | +3.94¢ | $80.95 / $87.85 |

*Expect about **92 buys a day** (~$13.87/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 4023 | $95.80 | +22% |
| Volatility model ≥ 2%, hold to the close | 7905 | $28.40 | +3% |
| Momentum model ≥ 2%, hold to the close | 6562 | -$26.05 | -3% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 55948 | 55911 | 212 (0%) | 1.07% | -$3,854.90 (-56%) | Hold to the close: -$3,854.90 (-56%) |

*In play or awaiting result: 25. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 33370 | 4.7% | 0.4% (133) | -671% | ❌ Worse |
| Momentum model | 33370 | 4.6% | 0.4% (133) | -697% | ❌ Worse |
| Mean-reversion model | 33370 | 8.0% | 0.4% (133) | -813% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 33370 | 133 | -49% | -87% | -87% | -85% |
| Volatility model ≥ 2% | 7905 | 70 | +3% | -77% | -76% | -72% |
| Volatility model ≥ 5% | 4281 | 46 | +36% | -72% | -71% | -67% |
| Volatility model ≥ 10% | 2480 | 28 | +62% | -63% | -61% | -58% |
| Momentum model ≥ 2% | 6562 | 52 | -3% | -78% | -78% | -74% |
| Momentum model ≥ 5% | 4023 | 38 | +22% | -74% | -74% | -70% |
| Momentum model ≥ 10% | 2638 | 25 | +33% | -66% | -66% | -61% |
| Mean-reversion model ≥ 2% | 13738 | 93 | -26% | -82% | -82% | -79% |
| Mean-reversion model ≥ 5% | 9581 | 79 | -9% | -80% | -79% | -77% |
| Mean-reversion model ≥ 10% | 6392 | 56 | -0% | -77% | -77% | -75% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 33575 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 13484 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 8852 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 55911 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 212 | 0% | -$3,854.90 | -56% | — |
| Sell at 2¢ | 2231 | 4% | -$5,948.84 | -87% | 47 sec |
| Sell at 3¢ | 1512 | 3% | -$5,939.22 | -87% | 48 sec |
| Sell at 5¢ | 1040 | 2% | -$5,824.90 | -85% | 63 sec |
| Sell at 10¢ | 632 | 1% | -$5,588.98 | -82% | 65 sec |
| Sell at 25¢ | 330 | 1% | -$5,198.60 | -76% | 82 sec |
| Sell at 50¢ | 217 | 0% | -$4,714.15 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 13 | 0 | 31% | 23% | -100% | -47% | -20% |
| 5–10 min | 2782 | 13 | 11% | 4% | -56% | -81% | -82% |
| 2–5 min | 18035 | 97 | 7% | 3% | -47% | -87% | -87% |
| 1–2 min | 14098 | 46 | 3% | 2% | -64% | -92% | -92% |
| Under 1 min | 20983 | 56 | 1% | 0% | -62% | -85% | -85% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 3759 | 17 | 5% | 3% | -41% | -88% | -87% |
| SOL | 3754 | 16 | 4% | 2% | -46% | -87% | -87% |
| HYPE | 3749 | 11 | 5% | 2% | -63% | -89% | -88% |
| BNB | 3735 | 19 | 5% | 2% | -36% | -86% | -85% |
| DOGE | 3734 | 8 | 4% | 2% | -73% | -90% | -90% |
| ETH | 3729 | 16 | 7% | 3% | -47% | -81% | -81% |
| NEAR | 3710 | 17 | 5% | 2% | -41% | -85% | -85% |
| BTC | 3710 | 18 | 5% | 2% | -34% | -87% | -88% |
| XRP | 3695 | 13 | 3% | 1% | -56% | -89% | -89% |
| GOLD | 2026 | 5 | 5% | 2% | -70% | -82% | -84% |
| WTI | 2002 | 7 | 4% | 2% | -58% | -91% | -92% |
| SILVER | 1967 | 9 | 5% | 2% | -46% | -83% | -83% |
| PLATINUM | 1795 | 4 | 3% | 1% | -79% | -96% | -95% |
| EURUSD | 1738 | 6 | 3% | 1% | -68% | -90% | -90% |
| COPPER | 1679 | 6 | 2% | 1% | -67% | -74% | -74% |
| GBPUSD | 1664 | 6 | 2% | 1% | -66% | -96% | -96% |
| NATGAS | 1655 | 9 | 2% | 1% | -49% | -74% | -73% |
| USDJPY | 1629 | 6 | 2% | 1% | -66% | -96% | -96% |
| PALLADIUM | 1608 | 4 | 1% | 0% | -77% | -92% | -92% |
| AUDUSD | 1182 | 6 | 2% | 1% | -53% | -89% | -89% |
| USDCAD | 1148 | 1 | 3% | 1% | -92% | -96% | -96% |
| BRENT | 752 | 0 | 2% | 1% | -100% | -97% | -97% |
| 10YRRATE | 383 | 2 | 4% | 2% | -51% | -69% | -67% |
| 2YRRATE | 367 | 4 | 4% | 2% | +2% | -43% | -41% |
| 30YRRATE | 363 | 0 | 2% | 1% | -100% | -96% | -94% |
| 5YRRATE | 337 | 2 | 4% | 2% | -45% | -93% | -95% |
| INX | 41 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 28405 | 110 | 4% | 2% | -56% | -88% | -88% |
| DOWN (bought NO) | 27506 | 102 | 4% | 2% | -58% | -86% | -86% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 5270 | 25 | 2% | 1% | -16% | -77% | -77% |
| 0.05–0.1% | 5671 | 20 | 3% | 2% | -46% | -91% | -91% |
| 0.1–0.2% | 8576 | 31 | 5% | 2% | -54% | -89% | -89% |
| 0.2–0.5% | 10168 | 41 | 6% | 3% | -55% | -87% | -86% |
| Over 0.5% | 3882 | 18 | 7% | 3% | -52% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 13733 | 44 | 4% | 2% | -63% | -88% | -88% |
| Morning (6am–12pm) | 13361 | 62 | 4% | 2% | -47% | -85% | -84% |
| Afternoon (12–6pm) | 13453 | 59 | 4% | 2% | -49% | -86% | -87% |
| Evening (6pm–12am) | 15364 | 47 | 4% | 2% | -65% | -89% | -89% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,819 |
| Time from buy to best bounce (bounced bets) | 51 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/13 6:29:39 AM | AUDUSD | DOWN | 20 sec | — | — | In play | — |
| 11/13 6:29:39 AM | XRP | UP | 20 sec | -0.039% | — | In play | — |
| 11/13 6:29:22 AM | BTC | DOWN | 37 sec | +0.122% | — | In play | — |
| 11/13 6:29:22 AM | BNB | DOWN | 37 sec | +0.034% | — | In play | — |
| 11/13 6:29:06 AM | GBPUSD | DOWN | 53 sec | — | — | In play | — |
| 11/13 6:29:06 AM | GOLD | UP | 53 sec | — | — | In play | — |
| 11/13 6:29:06 AM | DOGE | DOWN | 53 sec | +0.089% | — | In play | — |
| 11/13 6:28:50 AM | EURUSD | DOWN | 69 sec | — | — | In play | — |
| 11/13 6:28:33 AM | USDCAD | UP | 86 sec | — | — | In play | — |
| 11/13 6:28:33 AM | ETH | DOWN | 86 sec | +0.162% | — | In play | — |
| 11/13 6:28:16 AM | SOL | DOWN | 1.7 min | +0.187% | — | In play | — |
| 11/13 6:28:16 AM | HYPE | DOWN | 1.7 min | +0.396% | — | In play | — |
| 11/13 6:28:00 AM | PALLADIUM | UP | 2.0 min | — | — | In play | — |
| 11/13 6:27:11 AM | COPPER | UP | 2.8 min | — | — | In play | — |
| 11/13 6:27:11 AM | SILVER | UP | 2.8 min | — | — | In play | — |
| 11/13 6:27:11 AM | ZEC | DOWN | 2.8 min | +0.574% | — | In play | — |
| 11/13 6:14:58 AM | BNB | DOWN | 2 sec | +0.014% | 0¢ | ❌ Lost | $0.00 |
| 11/13 6:14:58 AM | DOGE | DOWN | 2 sec | +0.020% | 0¢ | ❌ Lost | $0.00 |
| 11/13 6:14:42 AM | BTC | DOWN | 18 sec | +0.035% | 1¢ | ❌ Lost | -$0.15 |
| 11/13 6:14:42 AM | GBPUSD | DOWN | 18 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/13 6:14:42 AM | XRP | UP | 18 sec | -0.020% | 0¢ | ❌ Lost | $0.00 |
| 11/13 6:14:42 AM | PLATINUM | DOWN | 18 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/13 6:14:42 AM | SOL | DOWN | 18 sec | +0.021% | 0¢ | ❌ Lost | $0.00 |
| 11/13 6:14:26 AM | GOLD | UP | 34 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 11/13 6:14:11 AM | 2YRRATE | UP | 48 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/13 6:13:54 AM | 5YRRATE | UP | 65 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/13 6:13:38 AM | 10YRRATE | UP | 81 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/13 6:13:38 AM | ZEC | DOWN | 81 sec | +0.284% | 0¢ | ❌ Lost | $0.00 |
| 11/13 6:13:22 AM | 30YRRATE | UP | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/13 6:13:22 AM | ETH | UP | 1.6 min | -0.193% | 0¢ | ❌ Lost | $0.00 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
