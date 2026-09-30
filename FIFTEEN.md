# 15-Minute 1¢ Study

*Updated Wed Sep 30, 3:26 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (5+ min left).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| 5+ min left, hold to the close | 114 finished bets | 2% | $11.20 | +67% | +9.82¢ | $19.45 / -$8.25 |

*Expect about **41 buys a day** (~$6.15/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| 5+ min left, sell at 50¢ | 114 | -$3.30 | -20% |
| 5+ min left, sell at 25¢ | 114 | -$6.87 | -41% |
| Momentum model ≥ 5%, hold to the close | 195 | -$7.45 | -35% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 3525 | 3518 | 13 (0%) | 1.07% | -$248.50 (-58%) | Hold to the close: -$248.50 (-58%) |

*In play or awaiting result: 7. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 1998 | 3.2% | 0.3% (5) | -565% | ❌ Worse |
| Momentum model | 1998 | 3.3% | 0.3% (5) | -616% | ❌ Worse |
| Mean-reversion model | 1998 | 6.3% | 0.3% (5) | -722% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 1998 | 5 | -69% | -90% | -90% | -87% |
| Volatility model ≥ 2% | 394 | 2 | -42% | -84% | -85% | -81% |
| Volatility model ≥ 5% | 190 | 0 | -100% | -79% | -77% | -72% |
| Volatility model ≥ 10% | 105 | 0 | -100% | -81% | -80% | -73% |
| Momentum model ≥ 2% | 349 | 1 | -66% | -84% | -86% | -83% |
| Momentum model ≥ 5% | 195 | 1 | -35% | -84% | -87% | -82% |
| Momentum model ≥ 10% | 128 | 0 | -100% | -89% | -87% | -84% |
| Mean-reversion model ≥ 2% | 759 | 3 | -58% | -86% | -87% | -82% |
| Mean-reversion model ≥ 5% | 500 | 3 | -36% | -83% | -84% | -77% |
| Mean-reversion model ≥ 10% | 313 | 2 | -29% | -78% | -79% | -72% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 2194 | 4% | 3% | 2% | 2% | 1% | 0% |
| Commodities | 1054 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 270 | 4% | 2% | 2% | 1% | 1% | 1% |
| **All** | 3518 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 13 | 0% | -$248.50 | -58% | — |
| Sell at 2¢ | 137 | 4% | -$394.88 | -92% | 47 sec |
| Sell at 3¢ | 85 | 2% | -$397.35 | -92% | 50 sec |
| Sell at 5¢ | 63 | 2% | -$389.55 | -90% | 64 sec |
| Sell at 10¢ | 48 | 1% | -$353.62 | -82% | 80 sec |
| Sell at 25¢ | 24 | 1% | -$337.06 | -78% | 1.6 min |
| Sell at 50¢ | 12 | 0% | -$307.50 | -71% | 2.0 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| 5–10 min | 114 | 2 | 11% | 4% | +67% | -80% | -86% |
| 2–5 min | 1170 | 6 | 7% | 3% | -50% | -88% | -89% |
| 1–2 min | 912 | 4 | 4% | 2% | -53% | -93% | -92% |
| Under 1 min | 1322 | 1 | 1% | 0% | -89% | -98% | -98% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| DOGE | 248 | 1 | 4% | 2% | -49% | -91% | -90% |
| ZEC | 246 | 1 | 5% | 2% | -51% | -88% | -92% |
| NEAR | 245 | 0 | 5% | 2% | -100% | -87% | -90% |
| ETH | 244 | 2 | 5% | 4% | -1% | -88% | -85% |
| XRP | 244 | 2 | 2% | 2% | +8% | -95% | -94% |
| BNB | 243 | 0 | 3% | 1% | -100% | -93% | -95% |
| HYPE | 242 | 1 | 5% | 3% | -49% | -90% | -87% |
| BTC | 241 | 0 | 7% | 3% | -100% | -85% | -88% |
| SOL | 241 | 0 | 3% | 1% | -100% | -92% | -92% |
| GOLD | 183 | 0 | 5% | 2% | -100% | -88% | -91% |
| SILVER | 165 | 0 | 2% | 1% | -100% | -96% | -96% |
| WTI | 161 | 1 | 4% | 1% | -34% | -93% | -94% |
| COPPER | 150 | 0 | 1% | 1% | -100% | -98% | -98% |
| NATGAS | 146 | 1 | 4% | 3% | -36% | -93% | -89% |
| PLATINUM | 128 | 0 | 0% | 0% | -100% | -100% | -100% |
| PALLADIUM | 121 | 0 | 2% | 1% | -100% | -96% | -98% |
| GBPUSD | 98 | 1 | 5% | 2% | -5% | -91% | -92% |
| EURUSD | 91 | 1 | 3% | 1% | +3% | -94% | -97% |
| USDJPY | 81 | 2 | 2% | 2% | +130% | -96% | -94% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 1808 | 8 | 4% | 2% | -49% | -92% | -92% |
| DOWN (bought NO) | 1710 | 5 | 4% | 2% | -67% | -92% | -93% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 231 | 0 | 2% | 1% | -100% | -94% | -93% |
| 0.05–0.1% | 285 | 0 | 1% | 0% | -100% | -97% | -98% |
| 0.1–0.2% | 510 | 1 | 4% | 1% | -74% | -91% | -92% |
| 0.2–0.5% | 781 | 2 | 6% | 3% | -72% | -88% | -88% |
| Over 0.5% | 386 | 4 | 6% | 3% | +7% | -88% | -88% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 888 | 2 | 4% | 2% | -74% | -91% | -93% |
| Morning (6am–12pm) | 960 | 6 | 4% | 2% | -29% | -91% | -90% |
| Afternoon (12–6pm) | 706 | 1 | 3% | 1% | -84% | -93% | -97% |
| Evening (6pm–12am) | 964 | 4 | 4% | 2% | -52% | -92% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 24 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 3,386 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 43 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 9/30 3:25:51 PM | HYPE | UP | 4.1 min | -0.776% | — | In play | — |
| 9/30 3:14:49 PM | SOL | DOWN | 10 sec | +0.057% | 0¢ | ❌ Lost | $0.00 |
| 9/30 3:14:49 PM | NEAR | UP | 10 sec | -0.086% | 0¢ | ❌ Lost | $0.00 |
| 9/30 3:14:34 PM | COPPER | DOWN | 25 sec | — | 2¢ | ❌ Lost | -$0.15 |
| 9/30 3:14:34 PM | XRP | DOWN | 25 sec | +0.047% | 1¢ | ❌ Lost | -$0.15 |
| 9/30 3:14:34 PM | DOGE | DOWN | 25 sec | +0.012% | 1¢ | ❌ Lost | -$0.15 |
| 9/30 3:14:34 PM | BNB | DOWN | 25 sec | +0.006% | 0¢ | ❌ Lost | $0.00 |
| 9/30 3:14:18 PM | ZEC | UP | 41 sec | -0.227% | 0¢ | ❌ Lost | -$0.15 |
| 9/30 3:14:02 PM | EURUSD | DOWN | 57 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/30 3:12:28 PM | BTC | DOWN | 2.5 min | +0.106% | 1¢ | ❌ Lost | -$0.15 |
| 9/30 3:11:40 PM | ETH | DOWN | 3.3 min | +0.097% | 1¢ | ❌ Lost | -$0.15 |
| 9/30 3:11:25 PM | HYPE | DOWN | 3.6 min | +0.702% | 1¢ | ❌ Lost | -$0.15 |
| 9/30 2:59:48 PM | NEAR | UP | 11 sec | -0.139% | 0¢ | ❌ Lost | $0.00 |
| 9/30 2:59:48 PM | NATGAS | DOWN | 11 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/30 2:59:32 PM | ETH | DOWN | 28 sec | +0.022% | 0¢ | ❌ Lost | $0.00 |
| 9/30 2:59:32 PM | BNB | DOWN | 28 sec | -0.006% | 1¢ | ❌ Lost | -$0.15 |
| 9/30 2:59:16 PM | HYPE | UP | 44 sec | -0.178% | 0¢ | ❌ Lost | -$0.15 |
| 9/30 2:59:16 PM | XRP | UP | 44 sec | -0.087% | 0¢ | ❌ Lost | $0.00 |
| 9/30 2:59:16 PM | SOL | UP | 44 sec | -0.098% | 0¢ | ❌ Lost | $0.00 |
| 9/30 2:59:00 PM | BTC | UP | 60 sec | -0.049% | 1¢ | ❌ Lost | -$0.15 |
| 9/30 2:58:45 PM | PLATINUM | DOWN | 74 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/30 2:57:57 PM | DOGE | UP | 2.0 min | -0.254% | 1¢ | ❌ Lost | -$0.15 |
| 9/30 2:57:10 PM | ZEC | UP | 2.8 min | -0.352% | 1¢ | ❌ Lost | -$0.15 |
| 9/30 2:44:50 PM | HYPE | DOWN | 10 sec | +0.029% | 0¢ | ❌ Lost | -$0.15 |
| 9/30 2:44:35 PM | NEAR | UP | 24 sec | -0.206% | 0¢ | ❌ Lost | $0.00 |
| 9/30 2:44:35 PM | EURUSD | DOWN | 24 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/30 2:44:35 PM | NATGAS | UP | 24 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/30 2:44:19 PM | ZEC | UP | 40 sec | -0.142% | 0¢ | ❌ Lost | $0.00 |
| 9/30 2:44:19 PM | ETH | UP | 40 sec | -0.065% | 0¢ | ❌ Lost | -$0.15 |
| 9/30 2:44:03 PM | WTI | UP | 56 sec | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
