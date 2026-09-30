# 15-Minute 1¢ Study

*Updated Tue Sep 29, 6:36 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (5+ min left).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| 5+ min left, hold to the close | 78 finished bets | 3% | $16.30 | +139% | +20.90¢ | $22.15 / -$5.85 |

*Expect about **41 buys a day** (~$6.11/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| 5+ min left, sell at 50¢ | 78 | $1.80 | +15% |
| Mean-reversion model ≥ 5%, hold to the close | 326 | -$1.05 | -2% |
| Volatility model ≥ 5%, sell at 25¢ | 116 | -$2.22 | -18% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 2431 | 2425 | 10 (0%) | 1.07% | -$155.20 (-53%) | Hold to the close: -$155.20 (-53%) |

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
| Volatility model | 1336 | 2.7% | 0.3% (4) | -430% | ❌ Worse |
| Momentum model | 1336 | 2.9% | 0.3% (4) | -506% | ❌ Worse |
| Mean-reversion model | 1336 | 5.7% | 0.3% (4) | -528% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 1336 | 4 | -62% | -90% | -92% | -89% |
| Volatility model ≥ 2% | 261 | 1 | -56% | -85% | -88% | -86% |
| Volatility model ≥ 5% | 116 | 0 | -100% | -74% | -74% | -68% |
| Volatility model ≥ 10% | 61 | 0 | -100% | -72% | -72% | -65% |
| Momentum model ≥ 2% | 221 | 0 | -100% | -86% | -90% | -90% |
| Momentum model ≥ 5% | 124 | 0 | -100% | -83% | -89% | -86% |
| Momentum model ≥ 10% | 79 | 0 | -100% | -86% | -85% | -83% |
| Mean-reversion model ≥ 2% | 499 | 3 | -36% | -86% | -88% | -84% |
| Mean-reversion model ≥ 5% | 326 | 3 | -2% | -84% | -85% | -79% |
| Mean-reversion model ≥ 10% | 201 | 2 | +10% | -78% | -82% | -77% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 1532 | 4% | 2% | 2% | 2% | 1% | 0% |
| Commodities | 739 | 2% | 1% | 1% | 0% | 0% | 0% |
| Financials | 154 | 5% | 3% | 3% | 2% | 2% | 1% |
| **All** | 2425 | 4% | 2% | 1% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 10 | 0% | -$155.20 | -53% | — |
| Sell at 2¢ | 86 | 4% | -$272.84 | -92% | 40 sec |
| Sell at 3¢ | 51 | 2% | -$275.31 | -93% | 47 sec |
| Sell at 5¢ | 36 | 1% | -$271.80 | -92% | 66 sec |
| Sell at 10¢ | 30 | 1% | -$241.90 | -82% | 1.6 min |
| Sell at 25¢ | 15 | 1% | -$231.55 | -78% | 2.1 min |
| Sell at 50¢ | 9 | 0% | -$206.45 | -70% | 2.4 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| 5–10 min | 78 | 2 | 12% | 3% | +139% | -80% | -87% |
| 2–5 min | 828 | 5 | 6% | 3% | -41% | -89% | -91% |
| 1–2 min | 650 | 2 | 3% | 1% | -67% | -94% | -94% |
| Under 1 min | 869 | 1 | 1% | 0% | -82% | -97% | -98% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ETH | 174 | 2 | 5% | 3% | +40% | -90% | -86% |
| DOGE | 173 | 1 | 4% | 2% | -24% | -90% | -89% |
| ZEC | 173 | 1 | 5% | 2% | -31% | -90% | -94% |
| NEAR | 170 | 0 | 5% | 1% | -100% | -87% | -91% |
| XRP | 170 | 2 | 2% | 2% | +51% | -94% | -94% |
| BTC | 169 | 0 | 7% | 2% | -100% | -83% | -90% |
| SOL | 169 | 0 | 4% | 2% | -100% | -91% | -88% |
| HYPE | 167 | 0 | 4% | 2% | -100% | -92% | -92% |
| BNB | 167 | 0 | 2% | 1% | -100% | -96% | -96% |
| GOLD | 132 | 0 | 3% | 0% | -100% | -93% | -97% |
| SILVER | 118 | 0 | 3% | 1% | -100% | -94% | -94% |
| WTI | 117 | 0 | 3% | 1% | -100% | -95% | -97% |
| COPPER | 108 | 0 | 1% | 1% | -100% | -98% | -98% |
| NATGAS | 100 | 0 | 3% | 1% | -100% | -95% | -92% |
| PLATINUM | 86 | 0 | 0% | 0% | -100% | -100% | -100% |
| PALLADIUM | 78 | 0 | 1% | 0% | -100% | -98% | -100% |
| GBPUSD | 59 | 1 | 5% | 2% | +58% | -91% | -91% |
| EURUSD | 51 | 1 | 6% | 2% | +83% | -90% | -95% |
| USDJPY | 44 | 2 | 5% | 5% | +324% | -92% | -88% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 1271 | 7 | 4% | 2% | -37% | -92% | -92% |
| DOWN (bought NO) | 1154 | 3 | 3% | 1% | -70% | -93% | -94% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 154 | 0 | 2% | 1% | -100% | -93% | -93% |
| 0.05–0.1% | 188 | 0 | 1% | 0% | -100% | -97% | -97% |
| 0.1–0.2% | 355 | 0 | 4% | 1% | -100% | -91% | -92% |
| 0.2–0.5% | 573 | 2 | 5% | 3% | -62% | -90% | -91% |
| Over 0.5% | 261 | 4 | 6% | 3% | +60% | -88% | -88% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 577 | 1 | 3% | 1% | -80% | -93% | -96% |
| Morning (6am–12pm) | 647 | 6 | 4% | 2% | +7% | -91% | -90% |
| Afternoon (12–6pm) | 583 | 1 | 3% | 1% | -81% | -94% | -97% |
| Evening (6pm–12am) | 618 | 2 | 4% | 2% | -62% | -92% | -91% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 23 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 3,832 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 45 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 9/29 6:29:44 PM | SOL | DOWN | 15 sec | +0.041% | 0¢ | ❌ Lost | $0.00 |
| 9/29 6:29:44 PM | WTI | UP | 15 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 9/29 6:29:44 PM | PALLADIUM | UP | 15 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/29 6:29:28 PM | EURUSD | DOWN | 31 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/29 6:29:12 PM | ETH | DOWN | 47 sec | +0.067% | 0¢ | ❌ Lost | $0.00 |
| 9/29 6:29:12 PM | DOGE | DOWN | 47 sec | +0.193% | 0¢ | ❌ Lost | $0.00 |
| 9/29 6:29:12 PM | BTC | DOWN | 47 sec | +0.049% | 0¢ | ❌ Lost | $0.00 |
| 9/29 6:28:56 PM | USDJPY | UP | 63 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/29 6:28:39 PM | BNB | DOWN | 81 sec | +0.091% | 0¢ | ❌ Lost | -$0.15 |
| 9/29 6:28:39 PM | HYPE | DOWN | 81 sec | +0.236% | 0¢ | ❌ Lost | $0.00 |
| 9/29 6:28:39 PM | XRP | DOWN | 81 sec | +0.215% | 0¢ | ❌ Lost | $0.00 |
| 9/29 6:28:23 PM | NATGAS | UP | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 9/29 6:28:23 PM | SILVER | UP | 1.6 min | — | 1¢ | ❌ Lost | -$0.15 |
| 9/29 6:27:52 PM | ZEC | DOWN | 2.1 min | +0.325% | 0¢ | ❌ Lost | -$0.15 |
| 9/29 6:27:19 PM | NEAR | DOWN | 2.7 min | +0.999% | 0¢ | ❌ Lost | -$0.15 |
| 9/29 6:14:46 PM | COPPER | UP | 13 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/29 6:14:46 PM | GOLD | UP | 13 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 9/29 6:14:30 PM | ZEC | UP | 29 sec | -0.117% | 0¢ | ❌ Lost | $0.00 |
| 9/29 6:14:30 PM | PLATINUM | UP | 29 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/29 6:13:42 PM | SILVER | UP | 77 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 9/29 6:13:42 PM | NEAR | DOWN | 77 sec | +0.431% | 0¢ | ❌ Lost | -$0.15 |
| 9/29 6:13:26 PM | XRP | UP | 1.6 min | -0.201% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 6:13:26 PM | BTC | UP | 1.6 min | -0.136% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 6:12:54 PM | HYPE | UP | 2.1 min | -0.293% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 6:12:06 PM | SOL | UP | 2.9 min | -0.242% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 6:12:06 PM | BNB | UP | 2.9 min | -0.152% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 6:11:50 PM | ETH | UP | 3.2 min | -0.248% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 6:11:50 PM | DOGE | UP | 3.2 min | -0.394% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 6:11:18 PM | WTI | DOWN | 3.7 min | — | 1¢ | ❌ Lost | -$0.15 |
| 9/29 5:59:51 PM | BTC | DOWN | 9 sec | +0.005% | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
