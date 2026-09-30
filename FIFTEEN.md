# 15-Minute 1¢ Study

*Updated Wed Sep 30, 3:56 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (5+ min left).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| 5+ min left, hold to the close | 115 finished bets | 2% | $11.05 | +65% | +9.61¢ | $19.45 / -$8.40 |

*Expect about **41 buys a day** (~$6.15/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| 5+ min left, sell at 50¢ | 115 | -$3.45 | -20% |
| 5+ min left, sell at 25¢ | 115 | -$7.02 | -41% |
| Momentum model ≥ 5%, hold to the close | 196 | -$7.45 | -35% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 3545 | 3539 | 13 (0%) | 1.07% | -$250.15 (-58%) | Hold to the close: -$250.15 (-58%) |

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
| Volatility model | 2015 | 3.2% | 0.2% (5) | -584% | ❌ Worse |
| Momentum model | 2015 | 3.3% | 0.2% (5) | -634% | ❌ Worse |
| Mean-reversion model | 2015 | 6.3% | 0.2% (5) | -742% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 2015 | 5 | -69% | -90% | -90% | -87% |
| Volatility model ≥ 2% | 397 | 2 | -42% | -84% | -86% | -81% |
| Volatility model ≥ 5% | 192 | 0 | -100% | -79% | -78% | -72% |
| Volatility model ≥ 10% | 107 | 0 | -100% | -82% | -80% | -74% |
| Momentum model ≥ 2% | 351 | 1 | -66% | -84% | -86% | -83% |
| Momentum model ≥ 5% | 196 | 1 | -35% | -84% | -87% | -82% |
| Momentum model ≥ 10% | 129 | 0 | -100% | -89% | -87% | -84% |
| Mean-reversion model ≥ 2% | 764 | 3 | -58% | -86% | -87% | -83% |
| Mean-reversion model ≥ 5% | 504 | 3 | -37% | -83% | -84% | -77% |
| Mean-reversion model ≥ 10% | 317 | 2 | -30% | -78% | -79% | -72% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 2211 | 4% | 3% | 2% | 2% | 1% | 0% |
| Commodities | 1057 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 271 | 4% | 2% | 2% | 1% | 1% | 1% |
| **All** | 3539 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 13 | 0% | -$250.15 | -58% | — |
| Sell at 2¢ | 137 | 4% | -$396.53 | -92% | 47 sec |
| Sell at 3¢ | 85 | 2% | -$399.00 | -92% | 50 sec |
| Sell at 5¢ | 63 | 2% | -$391.20 | -91% | 64 sec |
| Sell at 10¢ | 48 | 1% | -$355.27 | -82% | 80 sec |
| Sell at 25¢ | 24 | 1% | -$338.71 | -78% | 1.6 min |
| Sell at 50¢ | 12 | 0% | -$309.15 | -72% | 2.0 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| 5–10 min | 115 | 2 | 11% | 3% | +65% | -80% | -86% |
| 2–5 min | 1173 | 6 | 7% | 3% | -50% | -88% | -89% |
| 1–2 min | 915 | 4 | 3% | 2% | -53% | -93% | -92% |
| Under 1 min | 1336 | 1 | 1% | 0% | -89% | -98% | -98% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| DOGE | 250 | 1 | 4% | 2% | -49% | -91% | -90% |
| ZEC | 248 | 1 | 5% | 2% | -52% | -88% | -92% |
| NEAR | 247 | 0 | 5% | 2% | -100% | -87% | -90% |
| ETH | 246 | 2 | 5% | 4% | -1% | -88% | -85% |
| XRP | 246 | 2 | 2% | 2% | +7% | -95% | -94% |
| BNB | 245 | 0 | 3% | 1% | -100% | -93% | -95% |
| HYPE | 244 | 1 | 5% | 3% | -50% | -90% | -87% |
| BTC | 243 | 0 | 7% | 3% | -100% | -85% | -89% |
| SOL | 242 | 0 | 3% | 1% | -100% | -92% | -92% |
| GOLD | 184 | 0 | 5% | 2% | -100% | -88% | -91% |
| SILVER | 166 | 0 | 2% | 1% | -100% | -96% | -96% |
| WTI | 161 | 1 | 4% | 1% | -34% | -93% | -94% |
| COPPER | 150 | 0 | 1% | 1% | -100% | -98% | -98% |
| NATGAS | 147 | 1 | 4% | 3% | -37% | -93% | -89% |
| PLATINUM | 128 | 0 | 0% | 0% | -100% | -100% | -100% |
| PALLADIUM | 121 | 0 | 2% | 1% | -100% | -96% | -98% |
| GBPUSD | 98 | 1 | 5% | 2% | -5% | -91% | -92% |
| EURUSD | 91 | 1 | 3% | 1% | +3% | -94% | -97% |
| USDJPY | 82 | 2 | 2% | 2% | +128% | -96% | -94% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 1824 | 8 | 4% | 2% | -50% | -92% | -92% |
| DOWN (bought NO) | 1715 | 5 | 4% | 2% | -67% | -92% | -93% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 236 | 0 | 2% | 1% | -100% | -94% | -93% |
| 0.05–0.1% | 289 | 0 | 1% | 0% | -100% | -97% | -98% |
| 0.1–0.2% | 514 | 1 | 4% | 1% | -74% | -91% | -92% |
| 0.2–0.5% | 782 | 2 | 6% | 3% | -72% | -88% | -88% |
| Over 0.5% | 389 | 4 | 6% | 3% | +7% | -88% | -88% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 888 | 2 | 4% | 2% | -74% | -91% | -93% |
| Morning (6am–12pm) | 960 | 6 | 4% | 2% | -29% | -91% | -90% |
| Afternoon (12–6pm) | 727 | 1 | 3% | 1% | -84% | -93% | -97% |
| Evening (6pm–12am) | 964 | 4 | 4% | 2% | -52% | -92% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 24 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 3,384 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 43 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 9/30 3:44:52 PM | DOGE | UP | 8 sec | -0.081% | 0¢ | ❌ Lost | $0.00 |
| 9/30 3:44:52 PM | BNB | DOWN | 8 sec | -0.016% | 0¢ | ❌ Lost | $0.00 |
| 9/30 3:44:52 PM | GOLD | DOWN | 8 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/30 3:44:37 PM | SILVER | UP | 23 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/30 3:44:37 PM | SOL | DOWN | 23 sec | +0.031% | 0¢ | ❌ Lost | $0.00 |
| 9/30 3:44:37 PM | BTC | UP | 23 sec | -0.039% | 0¢ | ❌ Lost | $0.00 |
| 9/30 3:44:37 PM | NEAR | UP | 23 sec | -0.257% | 0¢ | ❌ Lost | $0.00 |
| 9/30 3:44:37 PM | ETH | UP | 23 sec | -0.067% | 0¢ | ❌ Lost | $0.00 |
| 9/30 3:44:21 PM | XRP | UP | 39 sec | -0.094% | 0¢ | ❌ Lost | $0.00 |
| 9/30 3:42:45 PM | ZEC | DOWN | 2.2 min | +0.168% | 1¢ | ❌ Lost | -$0.15 |
| 9/30 3:37:44 PM | HYPE | DOWN | 7.3 min | +0.744% | 1¢ | ❌ Lost | -$0.15 |
| 9/30 3:29:49 PM | BTC | UP | 10 sec | -0.016% | 1¢ | ❌ Lost | -$0.15 |
| 9/30 3:29:49 PM | USDJPY | UP | 10 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/30 3:29:49 PM | BNB | UP | 10 sec | -0.027% | 0¢ | ❌ Lost | $0.00 |
| 9/30 3:29:49 PM | ETH | UP | 10 sec | -0.063% | 0¢ | ❌ Lost | $0.00 |
| 9/30 3:29:18 PM | NATGAS | UP | 41 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/30 3:28:46 PM | DOGE | UP | 73 sec | -0.152% | 1¢ | ❌ Lost | -$0.15 |
| 9/30 3:28:46 PM | XRP | UP | 73 sec | -0.168% | 1¢ | ❌ Lost | -$0.15 |
| 9/30 3:28:31 PM | ZEC | UP | 88 sec | -0.184% | 1¢ | ❌ Lost | -$0.15 |
| 9/30 3:26:39 PM | NEAR | UP | 3.4 min | -0.907% | 1¢ | ❌ Lost | $0.00 |
| 9/30 3:25:51 PM | HYPE | UP | 4.1 min | -0.776% | 1¢ | ❌ Lost | -$0.15 |
| 9/30 3:14:49 PM | SOL | DOWN | 10 sec | +0.057% | 0¢ | ❌ Lost | $0.00 |
| 9/30 3:14:49 PM | NEAR | UP | 10 sec | -0.086% | 0¢ | ❌ Lost | $0.00 |
| 9/30 3:14:34 PM | COPPER | DOWN | 25 sec | — | 2¢ | ❌ Lost | -$0.15 |
| 9/30 3:14:34 PM | XRP | DOWN | 25 sec | +0.047% | 1¢ | ❌ Lost | -$0.15 |
| 9/30 3:14:34 PM | DOGE | DOWN | 25 sec | +0.012% | 1¢ | ❌ Lost | -$0.15 |
| 9/30 3:14:34 PM | BNB | DOWN | 25 sec | +0.006% | 0¢ | ❌ Lost | $0.00 |
| 9/30 3:14:18 PM | ZEC | UP | 41 sec | -0.227% | 0¢ | ❌ Lost | -$0.15 |
| 9/30 3:14:02 PM | EURUSD | DOWN | 57 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/30 3:12:28 PM | BTC | DOWN | 2.5 min | +0.106% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
