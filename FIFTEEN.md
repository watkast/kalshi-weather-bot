# 15-Minute 1¢ Study

*Updated Wed Sep 30, 1:55 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (5+ min left).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| 5+ min left, hold to the close | 112 finished bets | 2% | $11.35 | +68% | +10.13¢ | $19.60 / -$8.25 |

*Expect about **42 buys a day** (~$6.23/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| 5+ min left, sell at 50¢ | 112 | -$3.15 | -19% |
| 5+ min left, sell at 25¢ | 112 | -$6.72 | -40% |
| Momentum model ≥ 5%, hold to the close | 191 | -$7.15 | -34% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 3445 | 3437 | 13 (0%) | 1.07% | -$238.30 (-57%) | Hold to the close: -$238.30 (-57%) |

*In play or awaiting result: 8. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 1945 | 3.1% | 0.3% (5) | -564% | ❌ Worse |
| Momentum model | 1945 | 3.3% | 0.3% (5) | -619% | ❌ Worse |
| Mean-reversion model | 1945 | 6.1% | 0.3% (5) | -703% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 1945 | 5 | -68% | -90% | -90% | -87% |
| Volatility model ≥ 2% | 386 | 2 | -41% | -84% | -85% | -81% |
| Volatility model ≥ 5% | 183 | 0 | -100% | -78% | -77% | -71% |
| Volatility model ≥ 10% | 100 | 0 | -100% | -80% | -79% | -72% |
| Momentum model ≥ 2% | 344 | 1 | -66% | -84% | -86% | -82% |
| Momentum model ≥ 5% | 191 | 1 | -34% | -84% | -87% | -82% |
| Momentum model ≥ 10% | 124 | 0 | -100% | -89% | -87% | -84% |
| Mean-reversion model ≥ 2% | 738 | 3 | -57% | -86% | -87% | -82% |
| Mean-reversion model ≥ 5% | 484 | 3 | -34% | -84% | -83% | -77% |
| Mean-reversion model ≥ 10% | 298 | 2 | -26% | -78% | -78% | -71% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 2141 | 4% | 3% | 2% | 2% | 1% | 0% |
| Commodities | 1033 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 263 | 4% | 2% | 2% | 2% | 1% | 1% |
| **All** | 3437 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 13 | 0% | -$238.30 | -57% | — |
| Sell at 2¢ | 132 | 4% | -$385.98 | -92% | 47 sec |
| Sell at 3¢ | 84 | 2% | -$387.54 | -92% | 50 sec |
| Sell at 5¢ | 63 | 2% | -$379.35 | -90% | 64 sec |
| Sell at 10¢ | 48 | 1% | -$343.42 | -82% | 80 sec |
| Sell at 25¢ | 24 | 1% | -$326.86 | -78% | 1.6 min |
| Sell at 50¢ | 12 | 0% | -$297.30 | -71% | 2.0 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| 5–10 min | 112 | 2 | 11% | 4% | +68% | -81% | -86% |
| 2–5 min | 1146 | 6 | 7% | 3% | -49% | -88% | -89% |
| 1–2 min | 898 | 4 | 4% | 2% | -52% | -93% | -92% |
| Under 1 min | 1281 | 1 | 1% | 0% | -88% | -98% | -98% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| DOGE | 242 | 1 | 4% | 2% | -47% | -90% | -90% |
| ZEC | 240 | 1 | 5% | 2% | -50% | -89% | -92% |
| NEAR | 239 | 0 | 5% | 2% | -100% | -87% | -90% |
| ETH | 238 | 2 | 5% | 4% | +1% | -89% | -86% |
| XRP | 238 | 2 | 2% | 2% | +10% | -95% | -94% |
| BNB | 237 | 0 | 3% | 1% | -100% | -93% | -95% |
| SOL | 236 | 0 | 3% | 1% | -100% | -91% | -92% |
| HYPE | 236 | 1 | 5% | 3% | -48% | -89% | -87% |
| BTC | 235 | 0 | 6% | 3% | -100% | -85% | -88% |
| GOLD | 180 | 0 | 6% | 2% | -100% | -88% | -91% |
| SILVER | 162 | 0 | 2% | 1% | -100% | -96% | -96% |
| WTI | 159 | 1 | 4% | 1% | -33% | -93% | -94% |
| COPPER | 147 | 0 | 1% | 1% | -100% | -99% | -98% |
| NATGAS | 142 | 1 | 4% | 3% | -34% | -93% | -89% |
| PLATINUM | 124 | 0 | 0% | 0% | -100% | -100% | -100% |
| PALLADIUM | 119 | 0 | 2% | 1% | -100% | -97% | -98% |
| GBPUSD | 97 | 1 | 5% | 2% | -4% | -91% | -92% |
| EURUSD | 87 | 1 | 3% | 1% | +7% | -94% | -97% |
| USDJPY | 79 | 2 | 3% | 3% | +136% | -96% | -93% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 1774 | 8 | 4% | 2% | -48% | -92% | -92% |
| DOWN (bought NO) | 1663 | 5 | 4% | 2% | -66% | -92% | -93% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 221 | 0 | 2% | 1% | -100% | -93% | -93% |
| 0.05–0.1% | 277 | 0 | 1% | 0% | -100% | -97% | -98% |
| 0.1–0.2% | 499 | 1 | 4% | 1% | -73% | -91% | -92% |
| 0.2–0.5% | 765 | 2 | 6% | 3% | -71% | -88% | -88% |
| Over 0.5% | 378 | 4 | 6% | 3% | +9% | -88% | -88% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 888 | 2 | 4% | 2% | -74% | -91% | -93% |
| Morning (6am–12pm) | 960 | 6 | 4% | 2% | -29% | -91% | -90% |
| Afternoon (12–6pm) | 625 | 1 | 3% | 1% | -82% | -94% | -97% |
| Evening (6pm–12am) | 964 | 4 | 4% | 2% | -52% | -92% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 24 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 3,389 |
| Time from buy to best bounce (bounced bets) | 49 sec |
| Price snapshots per bet | 43 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 9/30 1:55:03 PM | ETH | UP | 4.9 min | -0.348% | — | In play | — |
| 9/30 1:53:13 PM | ZEC | UP | 6.8 min | -0.872% | — | In play | — |
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
| 9/30 1:29:34 PM | XRP | DOWN | 25 sec | +0.013% | 0¢ | ❌ Lost | -$0.15 |
| 9/30 1:29:34 PM | GBPUSD | DOWN | 25 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/30 1:29:18 PM | ZEC | DOWN | 41 sec | +0.045% | 0¢ | ❌ Lost | -$0.15 |
| 9/30 1:29:02 PM | HYPE | DOWN | 57 sec | +0.103% | 0¢ | ❌ Lost | $0.00 |
| 9/30 1:27:43 PM | NATGAS | UP | 2.3 min | — | 0¢ | ❌ Lost | -$0.15 |
| 9/30 1:27:28 PM | BNB | UP | 2.5 min | -0.125% | 2¢ | ❌ Lost | -$0.15 |
| 9/30 1:26:40 PM | COPPER | UP | 3.3 min | — | 1¢ | ❌ Lost | -$0.15 |
| 9/30 1:26:25 PM | NEAR | DOWN | 3.6 min | +1.053% | 1¢ | ❌ Lost | -$0.15 |
| 9/30 1:25:04 PM | SOL | UP | 4.9 min | -0.586% | 2¢ | ❌ Lost | -$0.15 |
| 9/30 1:14:55 PM | SILVER | DOWN | 5 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/30 1:14:55 PM | GOLD | DOWN | 5 sec | — | 0¢ | ❌ Lost | $0.00 |
| 9/30 1:14:55 PM | PLATINUM | DOWN | 5 sec | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
