# 15-Minute 1¢ Study

*Updated Wed Sep 30, 12:34 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (5+ min left).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| 5+ min left, hold to the close | 82 finished bets | 2% | $15.70 | +128% | +19.15¢ | $21.85 / -$6.15 |

*Expect about **38 buys a day** (~$5.69/day at risk); max loss per buy **15¢**.*

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
| 2808 | 2802 | 13 (0%) | 1.07% | -$159.70 (-47%) | Hold to the close: -$159.70 (-47%) |

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
| Volatility model | 1544 | 2.8% | 0.3% (5) | -443% | ❌ Worse |
| Momentum model | 1544 | 2.9% | 0.3% (5) | -492% | ❌ Worse |
| Mean-reversion model | 1544 | 5.7% | 0.3% (5) | -549% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 1544 | 5 | -59% | -90% | -91% | -87% |
| Volatility model ≥ 2% | 289 | 2 | -20% | -86% | -88% | -85% |
| Volatility model ≥ 5% | 130 | 0 | -100% | -77% | -77% | -71% |
| Volatility model ≥ 10% | 70 | 0 | -100% | -75% | -75% | -69% |
| Momentum model ≥ 2% | 253 | 1 | -53% | -87% | -90% | -89% |
| Momentum model ≥ 5% | 142 | 1 | -11% | -83% | -88% | -83% |
| Momentum model ≥ 10% | 90 | 0 | -100% | -88% | -87% | -85% |
| Mean-reversion model ≥ 2% | 569 | 3 | -44% | -86% | -87% | -83% |
| Mean-reversion model ≥ 5% | 369 | 3 | -13% | -83% | -83% | -76% |
| Mean-reversion model ≥ 10% | 225 | 2 | -1% | -78% | -79% | -72% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 1740 | 4% | 3% | 2% | 2% | 1% | 0% |
| Commodities | 856 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 206 | 4% | 3% | 2% | 2% | 1% | 1% |
| **All** | 2802 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 13 | 0% | -$159.70 | -47% | — |
| Sell at 2¢ | 102 | 4% | -$315.18 | -92% | 46 sec |
| Sell at 3¢ | 66 | 2% | -$315.96 | -92% | 48 sec |
| Sell at 5¢ | 48 | 2% | -$310.50 | -91% | 64 sec |
| Sell at 10¢ | 40 | 1% | -$275.30 | -81% | 82 sec |
| Sell at 25¢ | 20 | 1% | -$261.50 | -77% | 1.7 min |
| Sell at 50¢ | 11 | 0% | -$225.45 | -66% | 2.1 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| 5–10 min | 82 | 2 | 11% | 2% | +128% | -81% | -87% |
| 2–5 min | 925 | 6 | 6% | 3% | -37% | -89% | -89% |
| 1–2 min | 754 | 4 | 4% | 2% | -43% | -93% | -92% |
| Under 1 min | 1041 | 1 | 1% | 0% | -86% | -98% | -98% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| DOGE | 197 | 1 | 4% | 2% | -34% | -91% | -91% |
| ZEC | 196 | 1 | 6% | 3% | -39% | -88% | -90% |
| ETH | 194 | 2 | 4% | 3% | +24% | -91% | -88% |
| NEAR | 193 | 0 | 5% | 1% | -100% | -87% | -90% |
| XRP | 193 | 2 | 3% | 2% | +33% | -94% | -93% |
| SOL | 193 | 0 | 3% | 2% | -100% | -92% | -90% |
| BTC | 192 | 0 | 6% | 2% | -100% | -85% | -91% |
| HYPE | 191 | 1 | 5% | 3% | -34% | -89% | -87% |
| BNB | 191 | 0 | 2% | 1% | -100% | -97% | -97% |
| GOLD | 152 | 0 | 5% | 1% | -100% | -88% | -91% |
| WTI | 136 | 1 | 4% | 1% | -22% | -93% | -93% |
| SILVER | 134 | 0 | 2% | 1% | -100% | -95% | -95% |
| COPPER | 124 | 0 | 1% | 1% | -100% | -99% | -98% |
| NATGAS | 116 | 1 | 3% | 2% | -20% | -94% | -91% |
| PLATINUM | 100 | 0 | 0% | 0% | -100% | -100% | -100% |
| PALLADIUM | 94 | 0 | 1% | 0% | -100% | -98% | -100% |
| GBPUSD | 75 | 1 | 5% | 3% | +24% | -91% | -90% |
| EURUSD | 69 | 1 | 4% | 1% | +35% | -92% | -96% |
| USDJPY | 62 | 2 | 3% | 3% | +201% | -94% | -92% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 1470 | 8 | 4% | 2% | -38% | -92% | -92% |
| DOWN (bought NO) | 1332 | 5 | 4% | 2% | -57% | -92% | -93% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 181 | 0 | 2% | 1% | -100% | -94% | -94% |
| 0.05–0.1% | 232 | 0 | 1% | 0% | -100% | -97% | -98% |
| 0.1–0.2% | 413 | 1 | 3% | 1% | -67% | -92% | -93% |
| 0.2–0.5% | 637 | 2 | 5% | 3% | -66% | -89% | -89% |
| Over 0.5% | 276 | 4 | 6% | 3% | +51% | -88% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 608 | 2 | 4% | 1% | -62% | -92% | -94% |
| Morning (6am–12pm) | 647 | 6 | 4% | 2% | +7% | -91% | -90% |
| Afternoon (12–6pm) | 583 | 1 | 3% | 1% | -81% | -94% | -97% |
| Evening (6pm–12am) | 964 | 4 | 4% | 2% | -52% | -92% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 23 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 3,634 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 43 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 9/30 12:29:38 AM | SOL | UP | 21 sec | -0.044% | 0¢ | ❌ Lost | -$0.15 |
| 9/30 12:29:38 AM | XRP | UP | 21 sec | -0.047% | 1¢ | ❌ Lost | -$0.15 |
| 9/30 12:29:38 AM | ETH | UP | 21 sec | -0.053% | 1¢ | ❌ Lost | -$0.15 |
| 9/30 12:29:38 AM | PALLADIUM | UP | 21 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/30 12:29:38 AM | COPPER | DOWN | 21 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/30 12:29:23 AM | SILVER | UP | 36 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/30 12:29:23 AM | GBPUSD | DOWN | 36 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/30 12:29:07 AM | GOLD | UP | 52 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 9/30 12:28:51 AM | WTI | DOWN | 68 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 9/30 12:28:51 AM | EURUSD | DOWN | 68 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/30 12:28:51 AM | NEAR | DOWN | 68 sec | +0.458% | 0¢ | ❌ Lost | $0.00 |
| 9/30 12:28:03 AM | NATGAS | DOWN | 1.9 min | — | 49¢ | ✅ Won | $13.85 |
| 9/30 12:27:47 AM | USDJPY | UP | 2.2 min | — | 0¢ | ❌ Lost | -$0.15 |
| 9/30 12:27:47 AM | DOGE | UP | 2.2 min | -0.348% | 0¢ | ❌ Lost | -$0.15 |
| 9/30 12:27:31 AM | ZEC | UP | 2.5 min | -0.373% | 7¢ | ❌ Lost | -$0.15 |
| 9/30 12:27:15 AM | BNB | UP | 2.7 min | -0.252% | 0¢ | ❌ Lost | $0.00 |
| 9/30 12:26:59 AM | HYPE | UP | 3.0 min | -0.209% | 13¢ | ❌ Lost | -$0.15 |
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

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
