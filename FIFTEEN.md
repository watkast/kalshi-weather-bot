# 15-Minute 1¢ Study

*Updated Wed Sep 30, 12:16 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (5+ min left).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| 5+ min left, hold to the close | 82 finished bets | 2% | $15.70 | +128% | +19.15¢ | $21.85 / -$6.15 |

*Expect about **38 buys a day** (~$5.72/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| 5+ min left, sell at 50¢ | 82 | $1.20 | +10% |
| Momentum model ≥ 5%, hold to the close | 142 | -$1.75 | -11% |
| Volatility model ≥ 5%, sell at 25¢ | 130 | -$3.72 | -27% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 2791 | 2785 | 12 (0%) | 1.07% | -$171.45 (-51%) | Hold to the close: -$171.45 (-51%) |

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
| Volatility model | 1536 | 2.8% | 0.3% (5) | -444% | ❌ Worse |
| Momentum model | 1536 | 2.9% | 0.3% (5) | -493% | ❌ Worse |
| Mean-reversion model | 1536 | 5.7% | 0.3% (5) | -550% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 1536 | 5 | -59% | -91% | -91% | -88% |
| Volatility model ≥ 2% | 289 | 2 | -20% | -86% | -88% | -85% |
| Volatility model ≥ 5% | 130 | 0 | -100% | -77% | -77% | -71% |
| Volatility model ≥ 10% | 70 | 0 | -100% | -75% | -75% | -69% |
| Momentum model ≥ 2% | 253 | 1 | -53% | -87% | -90% | -89% |
| Momentum model ≥ 5% | 142 | 1 | -11% | -83% | -88% | -83% |
| Momentum model ≥ 10% | 90 | 0 | -100% | -88% | -87% | -85% |
| Mean-reversion model ≥ 2% | 567 | 3 | -43% | -87% | -88% | -84% |
| Mean-reversion model ≥ 5% | 367 | 3 | -13% | -84% | -85% | -78% |
| Mean-reversion model ≥ 10% | 223 | 2 | -0% | -80% | -82% | -77% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 1732 | 4% | 3% | 2% | 2% | 1% | 0% |
| Commodities | 850 | 2% | 2% | 1% | 1% | 0% | 0% |
| Financials | 203 | 4% | 3% | 2% | 2% | 1% | 1% |
| **All** | 2785 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 12 | 0% | -$171.45 | -51% | — |
| Sell at 2¢ | 99 | 4% | -$313.71 | -92% | 34 sec |
| Sell at 3¢ | 63 | 2% | -$314.88 | -93% | 47 sec |
| Sell at 5¢ | 45 | 2% | -$310.20 | -91% | 64 sec |
| Sell at 10¢ | 38 | 1% | -$275.67 | -81% | 82 sec |
| Sell at 25¢ | 19 | 1% | -$262.56 | -77% | 1.6 min |
| Sell at 50¢ | 11 | 0% | -$237.20 | -70% | 2.1 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| 5–10 min | 82 | 2 | 11% | 2% | +128% | -81% | -87% |
| 2–5 min | 920 | 6 | 6% | 3% | -37% | -89% | -90% |
| 1–2 min | 750 | 3 | 3% | 2% | -57% | -93% | -92% |
| Under 1 min | 1033 | 1 | 1% | 0% | -86% | -98% | -98% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| DOGE | 196 | 1 | 4% | 2% | -33% | -91% | -91% |
| ZEC | 195 | 1 | 5% | 3% | -39% | -89% | -92% |
| ETH | 193 | 2 | 4% | 3% | +25% | -91% | -88% |
| NEAR | 192 | 0 | 5% | 1% | -100% | -87% | -90% |
| BTC | 192 | 0 | 6% | 2% | -100% | -85% | -91% |
| XRP | 192 | 2 | 3% | 2% | +34% | -94% | -93% |
| SOL | 192 | 0 | 3% | 2% | -100% | -92% | -90% |
| HYPE | 190 | 1 | 4% | 3% | -33% | -90% | -89% |
| BNB | 190 | 0 | 2% | 1% | -100% | -97% | -97% |
| GOLD | 151 | 0 | 5% | 1% | -100% | -88% | -91% |
| WTI | 135 | 1 | 4% | 1% | -21% | -93% | -93% |
| SILVER | 133 | 0 | 2% | 1% | -100% | -95% | -95% |
| COPPER | 123 | 0 | 1% | 1% | -100% | -99% | -98% |
| NATGAS | 115 | 0 | 3% | 1% | -100% | -95% | -93% |
| PLATINUM | 100 | 0 | 0% | 0% | -100% | -100% | -100% |
| PALLADIUM | 93 | 0 | 1% | 0% | -100% | -98% | -100% |
| GBPUSD | 74 | 1 | 5% | 3% | +26% | -91% | -89% |
| EURUSD | 68 | 1 | 4% | 1% | +37% | -92% | -96% |
| USDJPY | 61 | 2 | 3% | 3% | +206% | -94% | -91% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 1459 | 8 | 4% | 2% | -37% | -92% | -92% |
| DOWN (bought NO) | 1326 | 4 | 4% | 2% | -65% | -92% | -93% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 179 | 0 | 2% | 1% | -100% | -94% | -94% |
| 0.05–0.1% | 231 | 0 | 1% | 0% | -100% | -97% | -98% |
| 0.1–0.2% | 413 | 1 | 3% | 1% | -67% | -92% | -93% |
| 0.2–0.5% | 632 | 2 | 5% | 3% | -65% | -89% | -90% |
| Over 0.5% | 276 | 4 | 6% | 3% | +51% | -88% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 591 | 1 | 4% | 1% | -81% | -92% | -96% |
| Morning (6am–12pm) | 647 | 6 | 4% | 2% | +7% | -91% | -90% |
| Afternoon (12–6pm) | 583 | 1 | 3% | 1% | -81% | -94% | -97% |
| Evening (6pm–12am) | 964 | 4 | 4% | 2% | -52% | -92% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 23 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 3,650 |
| Time from buy to best bounce (bounced bets) | 47 sec |
| Price snapshots per bet | 43 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 9/30 12:14:37 AM | PALLADIUM | DOWN | 23 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/30 12:14:37 AM | WTI | UP | 23 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/30 12:13:00 AM | DOGE | UP | 2.0 min | -0.296% | 1¢ | ❌ Lost | -$0.15 |
| 9/30 12:13:00 AM | XRP | UP | 2.0 min | -0.273% | 1¢ | ❌ Lost | -$0.15 |
| 9/30 12:12:45 AM | HYPE | UP | 2.2 min | -0.308% | 1¢ | ❌ Lost | -$0.15 |
| 9/30 12:12:45 AM | SILVER | DOWN | 2.2 min | — | 1¢ | ❌ Lost | -$0.15 |
| 9/30 12:12:30 AM | PLATINUM | DOWN | 2.5 min | — | 0¢ | ❌ Lost | -$0.15 |
| 9/30 12:12:14 AM | ETH | UP | 2.8 min | -0.247% | 0¢ | ❌ Lost | -$0.15 |
| 9/30 12:12:14 AM | GOLD | DOWN | 2.8 min | — | 2¢ | ❌ Lost | -$0.15 |
| 9/30 12:11:58 AM | BNB | UP | 3.0 min | -0.218% | 1¢ | ❌ Lost | -$0.15 |
| 9/30 12:11:58 AM | SOL | UP | 3.0 min | -0.382% | 1¢ | ❌ Lost | -$0.15 |
| 9/30 12:11:42 AM | BTC | UP | 3.3 min | -0.177% | 1¢ | ❌ Lost | -$0.15 |
| 9/30 12:10:23 AM | ZEC | UP | 4.6 min | -0.618% | 1¢ | ❌ Lost | -$0.15 |
| 9/30 12:10:23 AM | NEAR | UP | 4.6 min | -1.202% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 11:59:38 PM | NATGAS | DOWN | 22 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/29 11:59:06 PM | COPPER | DOWN | 54 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/29 11:58:33 PM | WTI | DOWN | 87 sec | — | 78¢ | ✅ Won | $13.85 |
| 9/29 11:58:33 PM | GBPUSD | DOWN | 87 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/29 11:58:18 PM | XRP | UP | 1.7 min | -0.246% | 17¢ | ❌ Lost | $0.00 |
| 9/29 11:58:02 PM | HYPE | UP | 1.9 min | -0.225% | 13¢ | ❌ Lost | -$0.15 |
| 9/29 11:58:02 PM | DOGE | UP | 1.9 min | -0.234% | 1¢ | ❌ Lost | $0.00 |
| 9/29 11:57:29 PM | USDJPY | UP | 2.5 min | — | 0¢ | ❌ Lost | -$0.15 |
| 9/29 11:57:13 PM | BNB | UP | 2.8 min | -0.149% | 2¢ | ❌ Lost | -$0.15 |
| 9/29 11:56:27 PM | ETH | UP | 3.5 min | -0.218% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 11:55:55 PM | BTC | UP | 4.1 min | -0.166% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 11:55:24 PM | ZEC | UP | 4.6 min | -0.463% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 11:55:24 PM | SOL | UP | 4.6 min | -0.417% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 11:44:39 PM | GOLD | DOWN | 20 sec | — | 1¢ | ❌ Lost | $0.00 |
| 9/29 11:44:39 PM | EURUSD | DOWN | 20 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/29 11:44:23 PM | BNB | DOWN | 36 sec | +0.090% | 0¢ | ❌ Lost | $0.00 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
