# 15-Minute 1¢ Study

*Updated Tue Sep 29, 10:59 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (5+ min left).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| 5+ min left, hold to the close | 68 finished bets | 3% | $17.80 | +175% | +26.18¢ | $22.90 / -$5.10 |

*Expect about **43 buys a day** (~$6.48/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Mean-reversion model ≥ 5%, hold to the close | 278 | $5.70 | +16% |
| 5+ min left, sell at 50¢ | 68 | $3.30 | +32% |
| Volatility model ≥ 5%, sell at 25¢ | 100 | -$0.57 | -5% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 2092 | 2075 | 8 (0%) | 1.07% | -$139.10 (-55%) | Hold to the close: -$139.10 (-55%) |

*In play or awaiting result: 17. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 1107 | 2.7% | 0.4% (4) | -394% | ❌ Worse |
| Momentum model | 1107 | 2.8% | 0.4% (4) | -458% | ❌ Worse |
| Mean-reversion model | 1107 | 5.9% | 0.4% (4) | -498% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 1107 | 4 | -54% | -90% | -91% | -87% |
| Volatility model ≥ 2% | 219 | 1 | -47% | -85% | -87% | -83% |
| Volatility model ≥ 5% | 100 | 0 | -100% | -73% | -70% | -63% |
| Volatility model ≥ 10% | 50 | 0 | -100% | -70% | -64% | -55% |
| Momentum model ≥ 2% | 176 | 0 | -100% | -86% | -89% | -87% |
| Momentum model ≥ 5% | 103 | 0 | -100% | -82% | -86% | -83% |
| Momentum model ≥ 10% | 64 | 0 | -100% | -87% | -80% | -78% |
| Mean-reversion model ≥ 2% | 427 | 3 | -25% | -86% | -87% | -82% |
| Mean-reversion model ≥ 5% | 278 | 3 | +16% | -83% | -83% | -77% |
| Mean-reversion model ≥ 10% | 173 | 2 | +30% | -77% | -78% | -73% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 1302 | 4% | 3% | 2% | 2% | 1% | 1% |
| Commodities | 644 | 2% | 1% | 0% | 0% | 0% | 0% |
| Financials | 129 | 3% | 2% | 2% | 2% | 2% | 2% |
| **All** | 2075 | 3% | 2% | 1% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 8 | 0% | -$139.10 | -55% | — |
| Sell at 2¢ | 72 | 3% | -$232.38 | -93% | 40 sec |
| Sell at 3¢ | 43 | 2% | -$234.33 | -93% | 47 sec |
| Sell at 5¢ | 31 | 1% | -$230.95 | -92% | 78 sec |
| Sell at 10¢ | 27 | 1% | -$215.73 | -86% | 1.6 min |
| Sell at 25¢ | 13 | 1% | -$208.07 | -83% | 2.1 min |
| Sell at 50¢ | 9 | 0% | -$190.35 | -76% | 2.4 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| 5–10 min | 68 | 2 | 10% | 3% | +175% | -82% | -89% |
| 2–5 min | 703 | 5 | 6% | 3% | -31% | -89% | -90% |
| 1–2 min | 565 | 1 | 3% | 1% | -81% | -94% | -94% |
| Under 1 min | 739 | 0 | 1% | 0% | -100% | -98% | -98% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ETH | 148 | 2 | 5% | 4% | +67% | -88% | -84% |
| ZEC | 147 | 1 | 5% | 2% | -17% | -88% | -93% |
| DOGE | 146 | 1 | 4% | 2% | -12% | -90% | -88% |
| NEAR | 145 | 0 | 4% | 1% | -100% | -89% | -95% |
| BTC | 145 | 0 | 8% | 3% | -100% | -80% | -88% |
| XRP | 145 | 2 | 3% | 2% | +74% | -94% | -93% |
| SOL | 143 | 0 | 3% | 1% | -100% | -91% | -89% |
| BNB | 142 | 0 | 2% | 1% | -100% | -96% | -96% |
| HYPE | 141 | 0 | 3% | 1% | -100% | -94% | -93% |
| GOLD | 112 | 0 | 2% | 0% | -100% | -96% | -100% |
| SILVER | 102 | 0 | 3% | 1% | -100% | -94% | -94% |
| WTI | 101 | 0 | 2% | 0% | -100% | -96% | -100% |
| COPPER | 94 | 0 | 1% | 1% | -100% | -98% | -97% |
| NATGAS | 89 | 0 | 3% | 1% | -100% | -94% | -91% |
| PLATINUM | 79 | 0 | 0% | 0% | -100% | -100% | -100% |
| PALLADIUM | 67 | 0 | 1% | 0% | -100% | -97% | -100% |
| GBPUSD | 49 | 0 | 2% | 0% | -100% | -96% | -95% |
| EURUSD | 42 | 0 | 2% | 0% | -100% | -96% | -100% |
| USDJPY | 38 | 2 | 5% | 5% | +391% | -91% | -86% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 1100 | 5 | 3% | 1% | -47% | -93% | -93% |
| DOWN (bought NO) | 975 | 3 | 3% | 2% | -64% | -93% | -94% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 122 | 0 | 2% | 2% | -100% | -91% | -91% |
| 0.05–0.1% | 153 | 0 | 1% | 0% | -100% | -96% | -97% |
| 0.1–0.2% | 296 | 0 | 4% | 1% | -100% | -90% | -92% |
| 0.2–0.5% | 498 | 2 | 5% | 3% | -56% | -89% | -90% |
| Over 0.5% | 233 | 4 | 6% | 3% | +80% | -88% | -89% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 577 | 1 | 3% | 1% | -80% | -93% | -96% |
| Morning (6am–12pm) | 579 | 4 | 4% | 2% | -21% | -92% | -92% |
| Afternoon (12–6pm) | 330 | 1 | 2% | 1% | -65% | -95% | -96% |
| Evening (6pm–12am) | 589 | 2 | 4% | 2% | -60% | -92% | -91% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 23 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 3,764 |
| Time from buy to best bounce (bounced bets) | 47 sec |
| Price snapshots per bet | 45 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 9/29 10:59:24 AM | PALLADIUM | UP | 36 sec | — | — | In play | — |
| 9/29 10:59:09 AM | ETH | DOWN | 50 sec | +0.063% | — | In play | — |
| 9/29 10:59:09 AM | SILVER | UP | 50 sec | — | — | In play | — |
| 9/29 10:59:09 AM | COPPER | UP | 50 sec | — | — | In play | — |
| 9/29 10:59:09 AM | WTI | UP | 50 sec | — | — | In play | — |
| 9/29 10:59:09 AM | GOLD | UP | 50 sec | — | — | In play | — |
| 9/29 10:57:48 AM | XRP | UP | 2.2 min | -0.457% | — | In play | — |
| 9/29 10:56:43 AM | SOL | UP | 3.3 min | -0.456% | — | In play | — |
| 9/29 10:56:43 AM | GBPUSD | UP | 3.3 min | — | — | In play | — |
| 9/29 10:56:11 AM | DOGE | UP | 3.8 min | -0.700% | — | In play | — |
| 9/29 10:54:50 AM | EURUSD | UP | 5.2 min | — | — | In play | — |
| 9/29 10:44:56 AM | COPPER | UP | 3 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/29 10:44:56 AM | EURUSD | UP | 3 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/29 10:44:40 AM | GBPUSD | UP | 19 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/29 10:44:24 AM | SILVER | UP | 35 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 9/29 10:44:08 AM | NEAR | UP | 51 sec | -0.522% | 0¢ | ❌ Lost | -$0.15 |
| 9/29 10:43:52 AM | ZEC | UP | 68 sec | -0.269% | 0¢ | ❌ Lost | -$0.15 |
| 9/29 10:43:52 AM | GOLD | UP | 68 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 9/29 10:43:36 AM | WTI | DOWN | 84 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 9/29 10:43:20 AM | NATGAS | UP | 1.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 9/29 10:43:04 AM | PALLADIUM | DOWN | 1.9 min | — | 1¢ | ❌ Lost | -$0.15 |
| 9/29 10:42:13 AM | ETH | UP | 2.8 min | -0.313% | 0¢ | ❌ Lost | $0.00 |
| 9/29 10:42:13 AM | BTC | UP | 2.8 min | -0.204% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 10:42:13 AM | SOL | UP | 2.8 min | -0.369% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 10:41:58 AM | DOGE | UP | 3.0 min | -0.590% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 10:41:42 AM | BNB | UP | 3.3 min | -0.233% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 10:41:42 AM | XRP | UP | 3.3 min | -0.706% | 0¢ | ❌ Lost | -$0.15 |
| 9/29 10:41:10 AM | HYPE | UP | 3.8 min | -0.581% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 10:29:52 AM | EURUSD | DOWN | 8 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/29 10:29:36 AM | COPPER | DOWN | 24 sec | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
