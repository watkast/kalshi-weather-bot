# 15-Minute 1¢ Study

*Updated Thu Oct 1, 8:01 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (5+ min left).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| 5+ min left, hold to the close | 147 finished bets | 1% | $6.40 | +30% | +4.35¢ | $17.05 / -$10.65 |

*Expect about **37 buys a day** (~$5.55/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 300 | -$4.70 | -14% |
| Volatility model ≥ 5%, sell at 25¢ | 291 | -$7.87 | -25% |
| 5+ min left, sell at 50¢ | 147 | -$8.10 | -38% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 4928 | 4922 | 15 (0%) | 1.07% | -$390.90 (-65%) | Hold to the close: -$390.90 (-65%) |

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
| Volatility model | 2831 | 3.5% | 0.2% (6) | -702% | ❌ Worse |
| Momentum model | 2831 | 3.7% | 0.2% (6) | -757% | ❌ Worse |
| Mean-reversion model | 2831 | 6.6% | 0.2% (6) | -894% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 2831 | 6 | -73% | -86% | -87% | -85% |
| Volatility model ≥ 2% | 579 | 3 | -41% | -64% | -66% | -63% |
| Volatility model ≥ 5% | 291 | 1 | -56% | -37% | -38% | -36% |
| Volatility model ≥ 10% | 165 | 1 | -10% | +6% | +5% | +11% |
| Momentum model ≥ 2% | 519 | 2 | -54% | -62% | -65% | -63% |
| Momentum model ≥ 5% | 300 | 2 | -14% | -43% | -45% | -41% |
| Momentum model ≥ 10% | 202 | 1 | -29% | -20% | -19% | -16% |
| Mean-reversion model ≥ 2% | 1068 | 3 | -70% | -86% | -88% | -85% |
| Mean-reversion model ≥ 5% | 704 | 3 | -54% | -83% | -85% | -80% |
| Mean-reversion model ≥ 10% | 445 | 2 | -49% | -78% | -81% | -75% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 3027 | 4% | 2% | 2% | 1% | 1% | 0% |
| Commodities | 1452 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 443 | 4% | 3% | 2% | 2% | 1% | 1% |
| **All** | 4922 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 15 | 0% | -$390.90 | -65% | — |
| Sell at 2¢ | 177 | 4% | -$540.88 | -90% | 45 sec |
| Sell at 3¢ | 106 | 2% | -$545.56 | -91% | 49 sec |
| Sell at 5¢ | 77 | 2% | -$536.85 | -89% | 66 sec |
| Sell at 10¢ | 56 | 1% | -$499.54 | -83% | 81 sec |
| Sell at 25¢ | 26 | 1% | -$472.84 | -79% | 1.6 min |
| Sell at 50¢ | 13 | 0% | -$443.15 | -74% | 2.1 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 3 | 0 | 100% | 67% | -100% | +73% | +160% |
| 5–10 min | 144 | 2 | 12% | 3% | +32% | -78% | -89% |
| 2–5 min | 1619 | 7 | 7% | 3% | -58% | -88% | -89% |
| 1–2 min | 1291 | 4 | 3% | 2% | -67% | -94% | -93% |
| Under 1 min | 1865 | 2 | 1% | 0% | -84% | -91% | -91% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| DOGE | 342 | 1 | 4% | 1% | -62% | -91% | -93% |
| ZEC | 338 | 1 | 5% | 2% | -65% | -89% | -94% |
| BNB | 338 | 0 | 4% | 1% | -100% | -92% | -94% |
| ETH | 337 | 2 | 5% | 3% | -27% | -88% | -86% |
| BTC | 336 | 0 | 6% | 3% | -100% | -85% | -88% |
| HYPE | 336 | 1 | 4% | 3% | -64% | -90% | -88% |
| NEAR | 335 | 0 | 5% | 1% | -100% | -87% | -91% |
| XRP | 333 | 3 | 2% | 1% | +17% | -58% | -57% |
| SOL | 332 | 0 | 3% | 1% | -100% | -92% | -92% |
| GOLD | 250 | 0 | 4% | 1% | -100% | -91% | -93% |
| SILVER | 233 | 0 | 2% | 1% | -100% | -96% | -96% |
| WTI | 221 | 1 | 3% | 1% | -53% | -95% | -96% |
| COPPER | 208 | 0 | 1% | 0% | -100% | -98% | -99% |
| NATGAS | 188 | 1 | 4% | 2% | -50% | -94% | -92% |
| PLATINUM | 181 | 0 | 0% | 0% | -100% | -100% | -100% |
| PALLADIUM | 171 | 0 | 2% | 1% | -100% | -97% | -98% |
| GBPUSD | 157 | 1 | 4% | 2% | -41% | -92% | -93% |
| EURUSD | 156 | 1 | 4% | 2% | -40% | -93% | -93% |
| USDJPY | 130 | 3 | 3% | 2% | +115% | -95% | -92% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 2511 | 9 | 4% | 2% | -59% | -92% | -92% |
| DOWN (bought NO) | 2411 | 6 | 4% | 1% | -71% | -88% | -89% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 359 | 1 | 1% | 1% | -47% | -43% | -43% |
| 0.05–0.1% | 429 | 0 | 2% | 0% | -100% | -93% | -96% |
| 0.1–0.2% | 736 | 1 | 4% | 1% | -82% | -91% | -92% |
| 0.2–0.5% | 1016 | 2 | 6% | 3% | -78% | -88% | -89% |
| Over 0.5% | 486 | 4 | 7% | 2% | -15% | -87% | -91% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 1116 | 2 | 4% | 1% | -80% | -92% | -94% |
| Morning (6am–12pm) | 1285 | 7 | 4% | 2% | -38% | -91% | -91% |
| Afternoon (12–6pm) | 1097 | 2 | 3% | 1% | -79% | -83% | -86% |
| Evening (6pm–12am) | 1424 | 4 | 3% | 2% | -67% | -93% | -92% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 24 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 3,192 |
| Time from buy to best bounce (bounced bets) | 50 sec |
| Price snapshots per bet | 43 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/1 7:59:59 PM | GOLD | DOWN | 1 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/1 7:59:59 PM | EURUSD | DOWN | 1 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/1 7:59:43 PM | GBPUSD | DOWN | 17 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/1 7:59:27 PM | USDJPY | UP | 33 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/1 7:59:27 PM | COPPER | DOWN | 33 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/1 7:57:35 PM | PALLADIUM | DOWN | 2.4 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/1 7:57:19 PM | PLATINUM | DOWN | 2.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/1 7:57:19 PM | SILVER | DOWN | 2.7 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/1 7:56:31 PM | BNB | DOWN | 3.5 min | +0.322% | 0¢ | ❌ Lost | $0.00 |
| 10/1 7:56:15 PM | XRP | DOWN | 3.8 min | +0.740% | 1¢ | ❌ Lost | -$0.15 |
| 10/1 7:56:15 PM | DOGE | DOWN | 3.8 min | +0.691% | 1¢ | ❌ Lost | -$0.15 |
| 10/1 7:55:59 PM | HYPE | DOWN | 4.0 min | +0.650% | 0¢ | ❌ Lost | $0.00 |
| 10/1 7:55:44 PM | BTC | DOWN | 4.2 min | +0.369% | 1¢ | ❌ Lost | -$0.15 |
| 10/1 7:55:28 PM | NEAR | DOWN | 4.5 min | +0.747% | 1¢ | ❌ Lost | -$0.15 |
| 10/1 7:53:48 PM | SOL | DOWN | 6.2 min | +0.749% | 2¢ | ❌ Lost | -$0.15 |
| 10/1 7:53:27 PM | ETH | DOWN | 6.5 min | +0.607% | 2¢ | ❌ Lost | -$0.15 |
| 10/1 7:53:11 PM | ZEC | DOWN | 6.8 min | +1.249% | 1¢ | ❌ Lost | -$0.15 |
| 10/1 7:44:54 PM | GBPUSD | DOWN | 5 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/1 7:44:38 PM | NEAR | UP | 21 sec | -0.227% | 0¢ | ❌ Lost | $0.00 |
| 10/1 7:44:22 PM | SOL | UP | 37 sec | -0.142% | 0¢ | ❌ Lost | $0.00 |
| 10/1 7:44:22 PM | BTC | UP | 37 sec | -0.043% | 0¢ | ❌ Lost | $0.00 |
| 10/1 7:44:08 PM | HYPE | DOWN | 52 sec | +0.053% | 0¢ | ❌ Lost | $0.00 |
| 10/1 7:44:08 PM | DOGE | UP | 52 sec | -0.170% | 0¢ | ❌ Lost | -$0.15 |
| 10/1 7:43:52 PM | BNB | UP | 67 sec | -0.093% | 1¢ | ❌ Lost | -$0.15 |
| 10/1 7:43:20 PM | SILVER | UP | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/1 7:43:04 PM | PLATINUM | UP | 1.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/1 7:43:04 PM | XRP | UP | 1.9 min | -0.255% | 0¢ | ❌ Lost | -$0.15 |
| 10/1 7:43:04 PM | PALLADIUM | UP | 1.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/1 7:42:46 PM | ZEC | UP | 2.2 min | -0.493% | 1¢ | ❌ Lost | -$0.15 |
| 10/1 7:42:30 PM | COPPER | UP | 2.5 min | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
