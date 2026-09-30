# 15-Minute 1¢ Study

*Updated Wed Sep 30, 4:27 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (5+ min left).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| 5+ min left, hold to the close | 116 finished bets | 2% | $10.90 | +64% | +9.40¢ | $19.30 / -$8.40 |

*Expect about **42 buys a day** (~$6.32/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| 5+ min left, sell at 50¢ | 116 | -$3.60 | -21% |
| 5+ min left, sell at 25¢ | 116 | -$7.17 | -42% |
| Momentum model ≥ 5%, hold to the close | 198 | -$7.75 | -36% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 3573 | 3560 | 13 (0%) | 1.07% | -$253.00 (-58%) | Hold to the close: -$253.00 (-58%) |

*In play or awaiting result: 13. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 2031 | 3.2% | 0.2% (5) | -582% | ❌ Worse |
| Momentum model | 2031 | 3.3% | 0.2% (5) | -632% | ❌ Worse |
| Mean-reversion model | 2031 | 6.3% | 0.2% (5) | -742% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 2031 | 5 | -69% | -90% | -91% | -87% |
| Volatility model ≥ 2% | 400 | 2 | -43% | -85% | -86% | -81% |
| Volatility model ≥ 5% | 193 | 0 | -100% | -79% | -78% | -72% |
| Volatility model ≥ 10% | 107 | 0 | -100% | -82% | -80% | -74% |
| Momentum model ≥ 2% | 354 | 1 | -67% | -84% | -86% | -83% |
| Momentum model ≥ 5% | 198 | 1 | -36% | -84% | -87% | -82% |
| Momentum model ≥ 10% | 129 | 0 | -100% | -89% | -87% | -84% |
| Mean-reversion model ≥ 2% | 770 | 3 | -59% | -86% | -87% | -83% |
| Mean-reversion model ≥ 5% | 509 | 3 | -37% | -83% | -84% | -78% |
| Mean-reversion model ≥ 10% | 320 | 2 | -31% | -77% | -80% | -73% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 2227 | 4% | 3% | 2% | 2% | 1% | 0% |
| Commodities | 1060 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 273 | 4% | 2% | 2% | 1% | 1% | 1% |
| **All** | 3560 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 13 | 0% | -$253.00 | -58% | — |
| Sell at 2¢ | 138 | 4% | -$399.12 | -92% | 47 sec |
| Sell at 3¢ | 85 | 2% | -$401.85 | -92% | 50 sec |
| Sell at 5¢ | 63 | 2% | -$394.05 | -91% | 64 sec |
| Sell at 10¢ | 48 | 1% | -$358.12 | -82% | 80 sec |
| Sell at 25¢ | 24 | 1% | -$341.56 | -79% | 1.6 min |
| Sell at 50¢ | 12 | 0% | -$312.00 | -72% | 2.0 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| 5–10 min | 116 | 2 | 12% | 3% | +64% | -79% | -86% |
| 2–5 min | 1179 | 6 | 7% | 3% | -51% | -88% | -89% |
| 1–2 min | 918 | 4 | 3% | 2% | -53% | -93% | -92% |
| Under 1 min | 1347 | 1 | 1% | 0% | -89% | -98% | -98% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| DOGE | 252 | 1 | 4% | 2% | -50% | -91% | -90% |
| ZEC | 250 | 1 | 6% | 2% | -52% | -88% | -92% |
| NEAR | 248 | 0 | 5% | 2% | -100% | -87% | -90% |
| ETH | 248 | 2 | 5% | 4% | -2% | -88% | -85% |
| XRP | 247 | 2 | 2% | 2% | +7% | -95% | -94% |
| BNB | 247 | 0 | 3% | 1% | -100% | -93% | -95% |
| HYPE | 246 | 1 | 4% | 3% | -50% | -90% | -87% |
| BTC | 245 | 0 | 7% | 3% | -100% | -85% | -89% |
| SOL | 244 | 0 | 3% | 1% | -100% | -92% | -92% |
| GOLD | 184 | 0 | 5% | 2% | -100% | -88% | -91% |
| SILVER | 167 | 0 | 2% | 1% | -100% | -96% | -96% |
| WTI | 162 | 1 | 4% | 1% | -34% | -93% | -95% |
| COPPER | 151 | 0 | 1% | 1% | -100% | -98% | -98% |
| NATGAS | 147 | 1 | 4% | 3% | -37% | -93% | -89% |
| PLATINUM | 128 | 0 | 0% | 0% | -100% | -100% | -100% |
| PALLADIUM | 121 | 0 | 2% | 1% | -100% | -96% | -98% |
| GBPUSD | 99 | 1 | 5% | 2% | -6% | -91% | -92% |
| EURUSD | 91 | 1 | 3% | 1% | +3% | -94% | -97% |
| USDJPY | 83 | 2 | 2% | 2% | +125% | -96% | -94% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 1843 | 8 | 4% | 2% | -50% | -92% | -92% |
| DOWN (bought NO) | 1717 | 5 | 4% | 2% | -67% | -92% | -93% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 239 | 0 | 2% | 1% | -100% | -94% | -93% |
| 0.05–0.1% | 292 | 0 | 1% | 0% | -100% | -97% | -98% |
| 0.1–0.2% | 520 | 1 | 4% | 1% | -75% | -91% | -92% |
| 0.2–0.5% | 785 | 2 | 6% | 3% | -72% | -88% | -88% |
| Over 0.5% | 390 | 4 | 7% | 3% | +6% | -87% | -88% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 888 | 2 | 4% | 2% | -74% | -91% | -93% |
| Morning (6am–12pm) | 960 | 6 | 4% | 2% | -29% | -91% | -90% |
| Afternoon (12–6pm) | 748 | 1 | 3% | 1% | -85% | -93% | -97% |
| Evening (6pm–12am) | 964 | 4 | 4% | 2% | -52% | -92% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 24 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 3,384 |
| Time from buy to best bounce (bounced bets) | 49 sec |
| Price snapshots per bet | 43 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 9/30 4:26:54 PM | XRP | DOWN | 3.1 min | +0.229% | — | In play | — |
| 9/30 4:26:23 PM | SOL | DOWN | 3.6 min | +0.294% | — | In play | — |
| 9/30 4:25:35 PM | HYPE | DOWN | 4.4 min | +0.515% | — | In play | — |
| 9/30 4:25:20 PM | BNB | DOWN | 4.7 min | +0.115% | — | In play | — |
| 9/30 4:24:32 PM | ETH | DOWN | 5.5 min | +0.157% | — | In play | — |
| 9/30 4:23:11 PM | NEAR | DOWN | 6.8 min | +1.395% | — | In play | — |
| 9/30 4:22:55 PM | ZEC | DOWN | 7.1 min | +0.788% | — | In play | — |
| 9/30 4:14:46 PM | SILVER | UP | 13 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/30 4:14:36 PM | USDJPY | DOWN | 24 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/30 4:14:36 PM | WTI | UP | 24 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/30 4:14:20 PM | XRP | UP | 40 sec | -0.054% | 1¢ | ❌ Lost | -$0.15 |
| 9/30 4:14:04 PM | BTC | UP | 56 sec | -0.070% | 1¢ | ❌ Lost | -$0.15 |
| 9/30 4:14:04 PM | DOGE | UP | 56 sec | -0.165% | 0¢ | ❌ Lost | $0.00 |
| 9/30 4:14:04 PM | NEAR | UP | 56 sec | -0.350% | 0¢ | ❌ Lost | -$0.15 |
| 9/30 4:13:01 PM | SOL | UP | 2.0 min | -0.133% | 1¢ | ❌ Lost | -$0.15 |
| 9/30 4:11:58 PM | HYPE | UP | 3.0 min | -0.268% | 1¢ | ❌ Lost | -$0.15 |
| 9/30 4:11:58 PM | ETH | UP | 3.0 min | -0.159% | 1¢ | ❌ Lost | -$0.15 |
| 9/30 4:11:42 PM | COPPER | UP | 3.3 min | — | 1¢ | ❌ Lost | -$0.15 |
| 9/30 4:11:11 PM | BNB | UP | 3.8 min | -0.145% | 1¢ | ❌ Lost | -$0.15 |
| 9/30 4:07:30 PM | ZEC | UP | 7.5 min | -1.010% | 3¢ | ❌ Lost | -$0.15 |
| 9/30 3:59:33 PM | SOL | UP | 27 sec | -0.049% | 0¢ | ❌ Lost | $0.00 |
| 9/30 3:59:33 PM | ETH | UP | 27 sec | -0.034% | 1¢ | ❌ Lost | -$0.15 |
| 9/30 3:59:17 PM | BTC | DOWN | 43 sec | +0.030% | 0¢ | ❌ Lost | -$0.15 |
| 9/30 3:59:01 PM | DOGE | UP | 59 sec | -0.127% | 1¢ | ❌ Lost | -$0.15 |
| 9/30 3:58:12 PM | ZEC | UP | 1.8 min | -0.178% | 0¢ | ❌ Lost | -$0.15 |
| 9/30 3:58:12 PM | GBPUSD | UP | 1.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 9/30 3:57:41 PM | BNB | UP | 2.3 min | -0.094% | 0¢ | ❌ Lost | -$0.15 |
| 9/30 3:57:09 PM | HYPE | UP | 2.9 min | -0.411% | 1¢ | ❌ Lost | -$0.15 |
| 9/30 3:44:52 PM | DOGE | UP | 8 sec | -0.081% | 0¢ | ❌ Lost | $0.00 |
| 9/30 3:44:52 PM | BNB | DOWN | 8 sec | -0.016% | 0¢ | ❌ Lost | $0.00 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
