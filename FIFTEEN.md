# 15-Minute 1¢ Study

*Updated Tue Sep 29, 2:03 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (5+ min left).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| 5+ min left, hold to the close | 73 finished bets | 3% | $17.05 | +156% | +23.36¢ | $22.60 / -$5.55 |

*Expect about **42 buys a day** (~$6.35/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Mean-reversion model ≥ 5%, hold to the close | 295 | $3.45 | +9% |
| 5+ min left, sell at 50¢ | 73 | $2.55 | +23% |
| Volatility model ≥ 5%, sell at 25¢ | 106 | -$1.02 | -9% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 2207 | 2201 | 10 (0%) | 1.07% | -$126.55 (-47%) | Hold to the close: -$126.55 (-47%) |

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
| Volatility model | 1183 | 2.9% | 0.3% (4) | -448% | ❌ Worse |
| Momentum model | 1183 | 3.0% | 0.3% (4) | -528% | ❌ Worse |
| Mean-reversion model | 1183 | 5.9% | 0.3% (4) | -537% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 1183 | 4 | -57% | -90% | -91% | -88% |
| Volatility model ≥ 2% | 231 | 1 | -50% | -85% | -86% | -84% |
| Volatility model ≥ 5% | 106 | 0 | -100% | -74% | -72% | -64% |
| Volatility model ≥ 10% | 54 | 0 | -100% | -72% | -66% | -58% |
| Momentum model ≥ 2% | 192 | 0 | -100% | -86% | -88% | -88% |
| Momentum model ≥ 5% | 111 | 0 | -100% | -83% | -87% | -84% |
| Momentum model ≥ 10% | 69 | 0 | -100% | -88% | -81% | -79% |
| Mean-reversion model ≥ 2% | 453 | 3 | -29% | -86% | -87% | -84% |
| Mean-reversion model ≥ 5% | 295 | 3 | +9% | -84% | -84% | -78% |
| Mean-reversion model ≥ 10% | 181 | 2 | +24% | -78% | -79% | -74% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 1378 | 4% | 3% | 2% | 2% | 1% | 1% |
| Commodities | 680 | 2% | 1% | 1% | 0% | 0% | 0% |
| Financials | 143 | 5% | 3% | 3% | 2% | 2% | 1% |
| **All** | 2201 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 10 | 0% | -$126.55 | -47% | — |
| Sell at 2¢ | 80 | 4% | -$245.75 | -92% | 47 sec |
| Sell at 3¢ | 50 | 2% | -$247.05 | -93% | 47 sec |
| Sell at 5¢ | 35 | 2% | -$243.80 | -91% | 67 sec |
| Sell at 10¢ | 30 | 1% | -$213.25 | -80% | 1.6 min |
| Sell at 25¢ | 15 | 1% | -$202.90 | -76% | 2.1 min |
| Sell at 50¢ | 9 | 0% | -$177.80 | -67% | 2.4 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| 5–10 min | 73 | 2 | 12% | 3% | +156% | -79% | -86% |
| 2–5 min | 740 | 5 | 6% | 3% | -34% | -89% | -90% |
| 1–2 min | 596 | 2 | 3% | 1% | -64% | -94% | -94% |
| Under 1 min | 792 | 1 | 1% | 1% | -80% | -97% | -97% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ETH | 157 | 2 | 5% | 4% | +57% | -88% | -85% |
| DOGE | 155 | 1 | 4% | 2% | -18% | -91% | -89% |
| ZEC | 155 | 1 | 5% | 2% | -21% | -88% | -93% |
| XRP | 154 | 2 | 3% | 2% | +65% | -94% | -93% |
| BTC | 153 | 0 | 8% | 3% | -100% | -81% | -88% |
| NEAR | 152 | 0 | 5% | 1% | -100% | -87% | -90% |
| SOL | 152 | 0 | 4% | 2% | -100% | -90% | -87% |
| BNB | 151 | 0 | 2% | 1% | -100% | -96% | -96% |
| HYPE | 149 | 0 | 3% | 1% | -100% | -94% | -93% |
| GOLD | 120 | 0 | 2% | 0% | -100% | -94% | -97% |
| WTI | 107 | 0 | 3% | 1% | -100% | -94% | -97% |
| SILVER | 107 | 0 | 3% | 1% | -100% | -94% | -94% |
| COPPER | 99 | 0 | 1% | 1% | -100% | -98% | -97% |
| NATGAS | 94 | 0 | 3% | 1% | -100% | -94% | -92% |
| PLATINUM | 82 | 0 | 0% | 0% | -100% | -100% | -100% |
| PALLADIUM | 71 | 0 | 1% | 0% | -100% | -98% | -100% |
| GBPUSD | 54 | 1 | 6% | 2% | +73% | -90% | -90% |
| EURUSD | 47 | 1 | 4% | 2% | +99% | -93% | -94% |
| USDJPY | 42 | 2 | 5% | 5% | +344% | -92% | -88% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 1171 | 7 | 4% | 2% | -31% | -92% | -92% |
| DOWN (bought NO) | 1030 | 3 | 3% | 1% | -66% | -92% | -94% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 134 | 0 | 2% | 1% | -100% | -91% | -91% |
| 0.05–0.1% | 167 | 0 | 1% | 0% | -100% | -96% | -97% |
| 0.1–0.2% | 313 | 0 | 4% | 1% | -100% | -91% | -92% |
| 0.2–0.5% | 519 | 2 | 5% | 3% | -58% | -89% | -90% |
| Over 0.5% | 245 | 4 | 7% | 3% | +71% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 577 | 1 | 3% | 1% | -80% | -93% | -96% |
| Morning (6am–12pm) | 647 | 6 | 4% | 2% | +7% | -91% | -90% |
| Afternoon (12–6pm) | 388 | 1 | 3% | 1% | -70% | -95% | -96% |
| Evening (6pm–12am) | 589 | 2 | 4% | 2% | -60% | -92% | -91% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 23 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 3,771 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 45 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 9/29 1:59:56 PM | COPPER | DOWN | 3 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/29 1:59:40 PM | XRP | UP | 19 sec | -0.060% | 0¢ | ❌ Lost | $0.00 |
| 9/29 1:59:40 PM | SILVER | DOWN | 19 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/29 1:59:40 PM | GOLD | DOWN | 19 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/29 1:59:09 PM | DOGE | UP | 50 sec | -0.122% | 0¢ | ❌ Lost | -$0.15 |
| 9/29 1:59:09 PM | ETH | UP | 50 sec | -0.047% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 1:59:09 PM | SOL | UP | 50 sec | -0.130% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 1:58:22 PM | BNB | DOWN | 1.6 min | +0.054% | 0¢ | ❌ Lost | -$0.15 |
| 9/29 1:58:22 PM | NATGAS | DOWN | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 9/29 1:57:34 PM | BTC | DOWN | 2.4 min | +0.147% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 1:57:18 PM | ZEC | UP | 2.7 min | -0.815% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 1:56:46 PM | HYPE | UP | 3.2 min | -0.432% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 1:55:58 PM | NEAR | UP | 4.0 min | -1.142% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 1:44:59 PM | SILVER | DOWN | 0 sec | — | 0¢ | ❌ Lost | $0.00 |
| 9/29 1:44:59 PM | GOLD | DOWN | 0 sec | — | 0¢ | ❌ Lost | $0.00 |
| 9/29 1:44:26 PM | EURUSD | UP | 34 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/29 1:44:10 PM | NEAR | UP | 50 sec | -0.365% | 0¢ | ❌ Lost | -$0.15 |
| 9/29 1:44:10 PM | WTI | UP | 50 sec | — | 13¢ | ❌ Lost | -$0.15 |
| 9/29 1:43:55 PM | NATGAS | UP | 64 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/29 1:43:55 PM | DOGE | UP | 64 sec | -0.181% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 1:43:55 PM | USDJPY | DOWN | 64 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/29 1:43:55 PM | ETH | UP | 64 sec | -0.080% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 1:43:55 PM | BTC | UP | 64 sec | -0.061% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 1:43:24 PM | XRP | UP | 1.6 min | -0.227% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 1:43:24 PM | SOL | UP | 1.6 min | -0.127% | 0¢ | ❌ Lost | -$0.15 |
| 9/29 1:42:51 PM | BNB | UP | 2.1 min | -0.159% | 0¢ | ❌ Lost | -$0.15 |
| 9/29 1:41:32 PM | ZEC | UP | 3.5 min | -0.551% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 1:40:44 PM | HYPE | UP | 4.3 min | -0.462% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 1:29:48 PM | XRP | DOWN | 11 sec | +0.013% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 1:29:48 PM | BNB | DOWN | 11 sec | -0.001% | 0¢ | ❌ Lost | $0.00 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
