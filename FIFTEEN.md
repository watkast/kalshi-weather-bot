# 15-Minute 1¢ Study

*Updated Mon Nov 16, 12:54 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 4416 finished bets | 1% | $224.85 | +46% | +5.09¢ | $86.25 / $138.60 |

*Expect about **90 buys a day** (~$13.50/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 4165 | $123.40 | +27% |
| Volatility model ≥ 2%, hold to the close | 8218 | $88.90 | +9% |
| Momentum model ≥ 2%, hold to the close | 6830 | $13.80 | +2% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 58361 | 58340 | 227 (0%) | 1.07% | -$3,915.05 (-55%) | Hold to the close: -$3,915.05 (-55%) |

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
| Volatility model | 35212 | 4.6% | 0.4% (148) | -631% | ❌ Worse |
| Momentum model | 35212 | 4.5% | 0.4% (148) | -656% | ❌ Worse |
| Mean-reversion model | 35212 | 7.9% | 0.4% (148) | -766% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 35212 | 148 | -46% | -87% | -87% | -84% |
| Volatility model ≥ 2% | 8218 | 77 | +9% | -77% | -76% | -72% |
| Volatility model ≥ 5% | 4416 | 51 | +46% | -72% | -70% | -67% |
| Volatility model ≥ 10% | 2538 | 30 | +71% | -63% | -61% | -57% |
| Momentum model ≥ 2% | 6830 | 57 | +2% | -78% | -78% | -74% |
| Momentum model ≥ 5% | 4165 | 41 | +27% | -74% | -74% | -70% |
| Momentum model ≥ 10% | 2712 | 26 | +36% | -66% | -66% | -61% |
| Mean-reversion model ≥ 2% | 14420 | 103 | -22% | -82% | -82% | -80% |
| Mean-reversion model ≥ 5% | 10032 | 85 | -6% | -80% | -79% | -77% |
| Mean-reversion model ≥ 10% | 6653 | 61 | +4% | -77% | -77% | -74% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 35418 | 5% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 13806 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 9116 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 58340 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 227 | 0% | -$3,915.05 | -55% | — |
| Sell at 2¢ | 2348 | 4% | -$6,188.57 | -87% | 47 sec |
| Sell at 3¢ | 1587 | 3% | -$6,180.12 | -87% | 48 sec |
| Sell at 5¢ | 1088 | 2% | -$6,063.85 | -85% | 62 sec |
| Sell at 10¢ | 665 | 1% | -$5,815.90 | -82% | 65 sec |
| Sell at 25¢ | 351 | 1% | -$5,399.24 | -76% | 80 sec |
| Sell at 50¢ | 234 | 0% | -$4,855.55 | -68% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 13 | 0 | 31% | 23% | -100% | -47% | -20% |
| 5–10 min | 2917 | 13 | 11% | 4% | -58% | -81% | -82% |
| 2–5 min | 18852 | 104 | 7% | 3% | -46% | -87% | -87% |
| 1–2 min | 14719 | 51 | 3% | 2% | -61% | -92% | -92% |
| Under 1 min | 21839 | 59 | 1% | 0% | -61% | -85% | -85% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 3964 | 19 | 5% | 2% | -37% | -88% | -87% |
| SOL | 3959 | 18 | 4% | 2% | -42% | -86% | -86% |
| HYPE | 3953 | 12 | 5% | 2% | -62% | -89% | -88% |
| DOGE | 3943 | 11 | 4% | 2% | -65% | -90% | -89% |
| BNB | 3940 | 20 | 5% | 2% | -36% | -85% | -85% |
| ETH | 3932 | 17 | 6% | 3% | -46% | -82% | -82% |
| BTC | 3914 | 21 | 5% | 2% | -27% | -86% | -88% |
| NEAR | 3913 | 17 | 5% | 2% | -43% | -85% | -86% |
| XRP | 3900 | 15 | 3% | 2% | -52% | -89% | -88% |
| GOLD | 2066 | 5 | 5% | 2% | -70% | -83% | -84% |
| WTI | 2053 | 7 | 4% | 2% | -59% | -91% | -92% |
| SILVER | 2011 | 9 | 5% | 2% | -47% | -83% | -83% |
| PLATINUM | 1830 | 4 | 3% | 1% | -80% | -95% | -95% |
| EURUSD | 1777 | 6 | 2% | 1% | -68% | -90% | -90% |
| COPPER | 1715 | 6 | 2% | 1% | -67% | -75% | -75% |
| GBPUSD | 1702 | 6 | 2% | 1% | -67% | -96% | -96% |
| NATGAS | 1689 | 9 | 2% | 1% | -50% | -74% | -74% |
| USDJPY | 1668 | 6 | 2% | 1% | -66% | -97% | -96% |
| PALLADIUM | 1644 | 4 | 1% | 0% | -77% | -92% | -93% |
| AUDUSD | 1223 | 6 | 2% | 1% | -54% | -89% | -89% |
| USDCAD | 1176 | 1 | 3% | 1% | -92% | -96% | -96% |
| BRENT | 798 | 0 | 2% | 1% | -100% | -97% | -97% |
| 10YRRATE | 401 | 2 | 4% | 1% | -53% | -70% | -68% |
| 2YRRATE | 384 | 4 | 4% | 2% | -3% | -45% | -43% |
| 30YRRATE | 376 | 0 | 2% | 1% | -100% | -96% | -94% |
| 5YRRATE | 355 | 2 | 4% | 2% | -47% | -93% | -95% |
| INX | 54 | 0 | 2% | 0% | -100% | -97% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 29703 | 113 | 4% | 2% | -56% | -88% | -88% |
| DOWN (bought NO) | 28637 | 114 | 4% | 2% | -54% | -86% | -86% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 5387 | 25 | 2% | 1% | -17% | -78% | -77% |
| 0.05–0.1% | 5832 | 24 | 3% | 2% | -36% | -91% | -91% |
| 0.1–0.2% | 8902 | 34 | 5% | 2% | -51% | -89% | -89% |
| 0.2–0.5% | 10902 | 48 | 7% | 3% | -50% | -86% | -86% |
| Over 0.5% | 4386 | 19 | 7% | 3% | -55% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 14108 | 45 | 4% | 2% | -64% | -88% | -88% |
| Morning (6am–12pm) | 13903 | 70 | 4% | 2% | -43% | -85% | -84% |
| Afternoon (12–6pm) | 14272 | 63 | 4% | 2% | -48% | -87% | -87% |
| Evening (6pm–12am) | 16057 | 49 | 4% | 2% | -65% | -89% | -89% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 5,099 |
| Time from buy to best bounce (bounced bets) | 50 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/16 12:44:56 AM | PLATINUM | UP | 3 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/16 12:44:56 AM | SILVER | UP | 3 sec | — | 0¢ | ❌ Lost | $0.00 |
| 11/16 12:44:56 AM | USDCAD | DOWN | 3 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/16 12:44:56 AM | NATGAS | DOWN | 3 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/16 12:44:37 AM | SOL | UP | 23 sec | -0.156% | 0¢ | ❌ Lost | $0.00 |
| 11/16 12:44:37 AM | DOGE | UP | 23 sec | -0.058% | 0¢ | ❌ Lost | -$0.15 |
| 11/16 12:44:37 AM | BNB | UP | 23 sec | -0.132% | 0¢ | ❌ Lost | $0.00 |
| 11/16 12:44:37 AM | NEAR | DOWN | 23 sec | -0.025% | 0¢ | ❌ Lost | $0.00 |
| 11/16 12:44:00 AM | ETH | DOWN | 60 sec | +0.136% | 1¢ | ❌ Lost | -$0.15 |
| 11/16 12:43:44 AM | GOLD | UP | 75 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 11/16 12:43:28 AM | BRENT | UP | 1.5 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/16 12:42:40 AM | AUDUSD | UP | 2.3 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/16 12:42:40 AM | WTI | UP | 2.3 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/16 12:41:52 AM | ZEC | DOWN | 3.1 min | +0.825% | 2¢ | ❌ Lost | -$0.15 |
| 11/16 12:41:52 AM | SOL | DOWN | 3.1 min | +0.391% | 100¢ | ✅ Won | $14.00 |
| 11/16 12:41:52 AM | HYPE | DOWN | 3.1 min | +0.399% | 7¢ | ❌ Lost | -$0.15 |
| 11/16 12:41:52 AM | XRP | DOWN | 3.1 min | +0.376% | 26¢ | ❌ Lost | -$0.15 |
| 11/16 12:40:33 AM | BTC | DOWN | 4.4 min | +0.327% | 1¢ | ❌ Lost | -$0.15 |
| 11/16 12:29:54 AM | NATGAS | DOWN | 5 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/16 12:29:38 AM | WTI | UP | 21 sec | — | 0¢ | ❌ Lost | $0.00 |
| 11/16 12:29:38 AM | PALLADIUM | DOWN | 21 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/16 12:29:38 AM | EURUSD | DOWN | 21 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/16 12:29:38 AM | GBPUSD | DOWN | 21 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/16 12:29:06 AM | SILVER | DOWN | 54 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 11/16 12:28:50 AM | AUDUSD | DOWN | 69 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/16 12:28:50 AM | GOLD | DOWN | 69 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 11/16 12:28:50 AM | BRENT | UP | 69 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/16 12:28:02 AM | DOGE | DOWN | 1.9 min | +0.304% | 0¢ | ❌ Lost | -$0.15 |
| 11/16 12:28:02 AM | USDJPY | UP | 1.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/16 12:26:43 AM | SOL | DOWN | 3.3 min | +0.496% | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
