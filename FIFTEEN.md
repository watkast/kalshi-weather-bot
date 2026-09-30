# 15-Minute 1¢ Study

*Updated Wed Sep 30, 2:05 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (5+ min left).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| 5+ min left, hold to the close | 113 finished bets | 2% | $11.20 | +67% | +9.91¢ | $19.60 / -$8.40 |

*Expect about **41 buys a day** (~$6.22/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| 5+ min left, sell at 50¢ | 113 | -$3.30 | -20% |
| 5+ min left, sell at 25¢ | 113 | -$6.87 | -41% |
| Momentum model ≥ 5%, hold to the close | 191 | -$7.15 | -34% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 3457 | 3451 | 13 (0%) | 1.07% | -$240.40 (-57%) | Hold to the close: -$240.40 (-57%) |

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
| Volatility model | 1954 | 3.1% | 0.3% (5) | -562% | ❌ Worse |
| Momentum model | 1954 | 3.2% | 0.3% (5) | -618% | ❌ Worse |
| Mean-reversion model | 1954 | 6.2% | 0.3% (5) | -705% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 1954 | 5 | -68% | -89% | -90% | -87% |
| Volatility model ≥ 2% | 386 | 2 | -41% | -84% | -85% | -81% |
| Volatility model ≥ 5% | 183 | 0 | -100% | -78% | -77% | -71% |
| Volatility model ≥ 10% | 100 | 0 | -100% | -80% | -79% | -72% |
| Momentum model ≥ 2% | 344 | 1 | -66% | -84% | -86% | -82% |
| Momentum model ≥ 5% | 191 | 1 | -34% | -84% | -87% | -82% |
| Momentum model ≥ 10% | 124 | 0 | -100% | -89% | -87% | -84% |
| Mean-reversion model ≥ 2% | 742 | 3 | -57% | -85% | -87% | -82% |
| Mean-reversion model ≥ 5% | 486 | 3 | -34% | -83% | -84% | -77% |
| Mean-reversion model ≥ 10% | 300 | 2 | -26% | -77% | -78% | -71% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 2150 | 5% | 3% | 2% | 2% | 1% | 0% |
| Commodities | 1038 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 263 | 4% | 2% | 2% | 2% | 1% | 1% |
| **All** | 3451 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 13 | 0% | -$240.40 | -57% | — |
| Sell at 2¢ | 135 | 4% | -$387.30 | -92% | 47 sec |
| Sell at 3¢ | 85 | 2% | -$389.25 | -92% | 50 sec |
| Sell at 5¢ | 63 | 2% | -$381.45 | -90% | 64 sec |
| Sell at 10¢ | 48 | 1% | -$345.52 | -82% | 80 sec |
| Sell at 25¢ | 24 | 1% | -$328.96 | -78% | 1.6 min |
| Sell at 50¢ | 12 | 0% | -$299.40 | -71% | 2.0 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| 5–10 min | 113 | 2 | 12% | 4% | +67% | -80% | -86% |
| 2–5 min | 1153 | 6 | 7% | 3% | -50% | -87% | -89% |
| 1–2 min | 899 | 4 | 4% | 2% | -52% | -93% | -92% |
| Under 1 min | 1286 | 1 | 1% | 0% | -89% | -98% | -98% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| DOGE | 243 | 1 | 4% | 2% | -48% | -90% | -90% |
| ZEC | 241 | 1 | 5% | 2% | -50% | -88% | -92% |
| NEAR | 240 | 0 | 5% | 2% | -100% | -87% | -90% |
| ETH | 239 | 2 | 5% | 4% | +1% | -88% | -85% |
| XRP | 239 | 2 | 2% | 2% | +10% | -95% | -94% |
| BNB | 238 | 0 | 3% | 1% | -100% | -93% | -95% |
| SOL | 237 | 0 | 3% | 1% | -100% | -91% | -92% |
| HYPE | 237 | 1 | 5% | 3% | -48% | -89% | -87% |
| BTC | 236 | 0 | 7% | 3% | -100% | -84% | -88% |
| GOLD | 181 | 0 | 6% | 2% | -100% | -88% | -91% |
| SILVER | 163 | 0 | 2% | 1% | -100% | -96% | -96% |
| WTI | 159 | 1 | 4% | 1% | -33% | -93% | -94% |
| COPPER | 147 | 0 | 1% | 1% | -100% | -99% | -98% |
| NATGAS | 143 | 1 | 4% | 3% | -35% | -93% | -89% |
| PLATINUM | 125 | 0 | 0% | 0% | -100% | -100% | -100% |
| PALLADIUM | 120 | 0 | 2% | 1% | -100% | -97% | -98% |
| GBPUSD | 97 | 1 | 5% | 2% | -4% | -91% | -92% |
| EURUSD | 87 | 1 | 3% | 1% | +7% | -94% | -97% |
| USDJPY | 79 | 2 | 3% | 3% | +136% | -96% | -93% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 1785 | 8 | 4% | 2% | -49% | -92% | -92% |
| DOWN (bought NO) | 1666 | 5 | 4% | 2% | -66% | -92% | -93% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 221 | 0 | 2% | 1% | -100% | -93% | -93% |
| 0.05–0.1% | 277 | 0 | 1% | 0% | -100% | -97% | -98% |
| 0.1–0.2% | 499 | 1 | 4% | 1% | -73% | -91% | -92% |
| 0.2–0.5% | 769 | 2 | 6% | 3% | -71% | -88% | -88% |
| Over 0.5% | 383 | 4 | 7% | 3% | +8% | -87% | -88% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 888 | 2 | 4% | 2% | -74% | -91% | -93% |
| Morning (6am–12pm) | 960 | 6 | 4% | 2% | -29% | -91% | -90% |
| Afternoon (12–6pm) | 639 | 1 | 3% | 1% | -82% | -93% | -97% |
| Evening (6pm–12am) | 964 | 4 | 4% | 2% | -52% | -92% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 24 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 3,399 |
| Time from buy to best bounce (bounced bets) | 49 sec |
| Price snapshots per bet | 43 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 9/30 1:59:48 PM | NATGAS | DOWN | 11 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/30 1:59:48 PM | SILVER | DOWN | 11 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/30 1:59:33 PM | GOLD | DOWN | 26 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/30 1:59:33 PM | PALLADIUM | UP | 26 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/30 1:59:33 PM | PLATINUM | UP | 26 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/30 1:58:14 PM | DOGE | UP | 1.8 min | -0.341% | 1¢ | ❌ Lost | -$0.15 |
| 9/30 1:57:58 PM | NEAR | UP | 2.0 min | -1.050% | 1¢ | ❌ Lost | -$0.15 |
| 9/30 1:57:27 PM | HYPE | UP | 2.5 min | -0.641% | 0¢ | ❌ Lost | -$0.15 |
| 9/30 1:56:55 PM | XRP | UP | 3.1 min | -0.502% | 1¢ | ❌ Lost | -$0.15 |
| 9/30 1:55:50 PM | SOL | UP | 4.2 min | -0.509% | 1¢ | ❌ Lost | -$0.15 |
| 9/30 1:55:19 PM | BNB | UP | 4.7 min | -0.304% | 1¢ | ❌ Lost | -$0.15 |
| 9/30 1:55:19 PM | BTC | UP | 4.7 min | -0.365% | 2¢ | ❌ Lost | -$0.15 |
| 9/30 1:55:03 PM | ETH | UP | 4.9 min | -0.348% | 5¢ | ❌ Lost | -$0.15 |
| 9/30 1:53:13 PM | ZEC | UP | 6.8 min | -0.872% | 2¢ | ❌ Lost | -$0.15 |
| 9/30 1:44:17 PM | BTC | DOWN | 43 sec | +0.048% | 0¢ | ❌ Lost | $0.00 |
| 9/30 1:44:17 PM | WTI | UP | 43 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 9/30 1:44:17 PM | SOL | DOWN | 43 sec | +0.017% | 1¢ | ❌ Lost | -$0.15 |
| 9/30 1:44:17 PM | USDJPY | DOWN | 43 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/30 1:44:01 PM | XRP | DOWN | 59 sec | +0.188% | 0¢ | ❌ Lost | $0.00 |
| 9/30 1:44:01 PM | ETH | DOWN | 59 sec | +0.066% | 1¢ | ❌ Lost | -$0.15 |
| 9/30 1:43:30 PM | GBPUSD | UP | 1.5 min | — | 0¢ | ❌ Lost | -$0.15 |
| 9/30 1:43:14 PM | BNB | DOWN | 1.8 min | +0.042% | 0¢ | ❌ Lost | -$0.15 |
| 9/30 1:43:14 PM | PLATINUM | UP | 1.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 9/30 1:42:27 PM | DOGE | DOWN | 2.5 min | +0.294% | 0¢ | ❌ Lost | -$0.15 |
| 9/30 1:42:11 PM | HYPE | UP | 2.8 min | -0.445% | 1¢ | ❌ Lost | -$0.15 |
| 9/30 1:41:55 PM | EURUSD | UP | 3.1 min | — | 0¢ | ❌ Lost | -$0.15 |
| 9/30 1:40:04 PM | ZEC | DOWN | 4.9 min | +0.705% | 1¢ | ❌ Lost | -$0.15 |
| 9/30 1:29:49 PM | EURUSD | DOWN | 10 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/30 1:29:49 PM | ETH | UP | 10 sec | -0.063% | 0¢ | ❌ Lost | $0.00 |
| 9/30 1:29:49 PM | DOGE | DOWN | 10 sec | -0.013% | 0¢ | ❌ Lost | $0.00 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
