# 15-Minute 1¢ Study

*Updated Mon Oct 5, 2:52 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 578 finished bets | 1% | $35.60 | +57% | +6.16¢ | -$17.80 / $53.40 |

*Expect about **82 buys a day** (~$12.23/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Volatility model ≥ 2%, hold to the close | 1074 | $24.25 | +19% |
| Momentum model ≥ 5%, hold to the close | 582 | $21.90 | +35% |
| 5+ min left, hold to the close | 210 | $10.95 | +35% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 8257 | 8251 | 37 (0%) | 1.07% | -$472.90 (-48%) | Hold to the close: -$472.90 (-48%) |

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
| Volatility model | 5465 | 4.2% | 0.5% (25) | -589% | ❌ Worse |
| Momentum model | 5465 | 4.2% | 0.5% (25) | -618% | ❌ Worse |
| Mean-reversion model | 5465 | 6.8% | 0.5% (25) | -688% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 5465 | 25 | -42% | -85% | -85% | -82% |
| Volatility model ≥ 2% | 1074 | 11 | +19% | -69% | -69% | -64% |
| Volatility model ≥ 5% | 578 | 7 | +57% | -55% | -54% | -49% |
| Volatility model ≥ 10% | 361 | 5 | +103% | -36% | -37% | -31% |
| Momentum model ≥ 2% | 945 | 8 | +2% | -69% | -72% | -69% |
| Momentum model ≥ 5% | 582 | 6 | +35% | -61% | -63% | -60% |
| Momentum model ≥ 10% | 405 | 5 | +76% | -48% | -48% | -45% |
| Mean-reversion model ≥ 2% | 1902 | 14 | -20% | -82% | -83% | -78% |
| Mean-reversion model ≥ 5% | 1274 | 12 | +4% | -79% | -79% | -72% |
| Mean-reversion model ≥ 10% | 845 | 9 | +23% | -77% | -78% | -71% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 5662 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 1964 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 625 | 4% | 3% | 2% | 2% | 1% | 0% |
| **All** | 8251 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 37 | 0% | -$472.90 | -48% | — |
| Sell at 2¢ | 327 | 4% | -$877.88 | -89% | 33 sec |
| Sell at 3¢ | 212 | 3% | -$880.22 | -89% | 48 sec |
| Sell at 5¢ | 157 | 2% | -$860.85 | -87% | 61 sec |
| Sell at 10¢ | 105 | 1% | -$811.35 | -82% | 66 sec |
| Sell at 25¢ | 58 | 1% | -$728.92 | -74% | 1.5 min |
| Sell at 50¢ | 36 | 0% | -$635.90 | -64% | 1.8 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 3 | 0 | 100% | 67% | -100% | +73% | +160% |
| 5–10 min | 207 | 3 | 12% | 3% | +37% | -80% | -87% |
| 2–5 min | 2663 | 20 | 8% | 4% | -27% | -86% | -86% |
| 1–2 min | 2176 | 9 | 3% | 2% | -55% | -93% | -93% |
| Under 1 min | 3202 | 5 | 1% | 0% | -76% | -89% | -89% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 640 | 5 | 5% | 3% | -7% | -89% | -89% |
| ETH | 633 | 5 | 6% | 3% | -0% | -86% | -86% |
| DOGE | 633 | 2 | 4% | 2% | -59% | -90% | -90% |
| HYPE | 630 | 3 | 5% | 3% | -42% | -88% | -86% |
| BNB | 629 | 2 | 4% | 2% | -62% | -91% | -93% |
| SOL | 627 | 0 | 3% | 1% | -100% | -92% | -91% |
| XRP | 625 | 4 | 2% | 1% | -18% | -76% | -76% |
| BTC | 624 | 3 | 6% | 2% | -37% | -86% | -89% |
| NEAR | 621 | 3 | 7% | 3% | -37% | -63% | -64% |
| GOLD | 334 | 0 | 4% | 1% | -100% | -91% | -93% |
| SILVER | 320 | 0 | 2% | 1% | -100% | -96% | -96% |
| WTI | 301 | 2 | 3% | 1% | -29% | -95% | -96% |
| COPPER | 279 | 0 | 1% | 0% | -100% | -99% | -99% |
| PLATINUM | 247 | 0 | 0% | 0% | -100% | -100% | -100% |
| NATGAS | 244 | 2 | 3% | 2% | -23% | -94% | -93% |
| PALLADIUM | 239 | 1 | 2% | 1% | -61% | -96% | -98% |
| EURUSD | 224 | 1 | 5% | 3% | -58% | -91% | -90% |
| GBPUSD | 213 | 1 | 4% | 2% | -56% | -93% | -94% |
| USDJPY | 188 | 3 | 2% | 2% | +49% | -96% | -94% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 4154 | 20 | 4% | 2% | -43% | -88% | -88% |
| DOWN (bought NO) | 4097 | 17 | 4% | 2% | -52% | -89% | -90% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 948 | 7 | 2% | 1% | +25% | -58% | -57% |
| 0.05–0.1% | 950 | 2 | 3% | 1% | -69% | -90% | -92% |
| 0.1–0.2% | 1410 | 6 | 4% | 2% | -46% | -90% | -91% |
| 0.2–0.5% | 1660 | 8 | 6% | 3% | -47% | -88% | -87% |
| Over 0.5% | 692 | 4 | 7% | 3% | -41% | -86% | -88% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 2048 | 9 | 4% | 2% | -49% | -85% | -86% |
| Morning (6am–12pm) | 2058 | 17 | 5% | 3% | -5% | -89% | -87% |
| Afternoon (12–6pm) | 1751 | 4 | 3% | 1% | -73% | -86% | -87% |
| Evening (6pm–12am) | 2394 | 7 | 3% | 2% | -66% | -94% | -94% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 25 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,195 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 41 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/5 2:44:54 AM | ZEC | UP | 6 sec | -0.123% | 0¢ | ❌ Lost | $0.00 |
| 10/5 2:44:36 AM | USDJPY | DOWN | 23 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/5 2:44:36 AM | GBPUSD | DOWN | 23 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/5 2:44:36 AM | GOLD | UP | 23 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/5 2:43:19 AM | XRP | UP | 1.7 min | -0.184% | 1¢ | ❌ Lost | -$0.15 |
| 10/5 2:43:19 AM | COPPER | UP | 1.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/5 2:42:47 AM | BTC | UP | 2.2 min | -0.191% | 1¢ | ❌ Lost | -$0.15 |
| 10/5 2:42:47 AM | SOL | UP | 2.2 min | -0.181% | 1¢ | ❌ Lost | -$0.15 |
| 10/5 2:42:47 AM | HYPE | UP | 2.2 min | -0.337% | 0¢ | ❌ Lost | $0.00 |
| 10/5 2:42:47 AM | SILVER | UP | 2.2 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/5 2:42:47 AM | WTI | DOWN | 2.2 min | — | 0¢ | ❌ Lost | $0.00 |
| 10/5 2:42:30 AM | ETH | UP | 2.5 min | -0.164% | 1¢ | ❌ Lost | -$0.15 |
| 10/5 2:42:30 AM | PLATINUM | UP | 2.5 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/5 2:42:14 AM | NATGAS | DOWN | 2.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/5 2:41:58 AM | PALLADIUM | UP | 3.0 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/5 2:41:25 AM | DOGE | DOWN | 3.6 min | +0.630% | 1¢ | ❌ Lost | -$0.15 |
| 10/5 2:40:53 AM | BNB | UP | 4.1 min | -0.208% | 1¢ | ❌ Lost | -$0.15 |
| 10/5 2:40:53 AM | NEAR | UP | 4.1 min | -0.998% | 1¢ | ❌ Lost | -$0.15 |
| 10/5 2:29:53 AM | BTC | DOWN | 7 sec | +0.011% | 1¢ | ❌ Lost | -$0.15 |
| 10/5 2:29:53 AM | WTI | DOWN | 7 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/5 2:28:34 AM | ZEC | DOWN | 85 sec | +0.212% | 1¢ | ❌ Lost | -$0.15 |
| 10/5 2:28:34 AM | PALLADIUM | DOWN | 85 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/5 2:28:34 AM | PLATINUM | DOWN | 85 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/5 2:27:29 AM | USDJPY | DOWN | 2.5 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/5 2:27:29 AM | XRP | UP | 2.5 min | -0.263% | 1¢ | ❌ Lost | -$0.15 |
| 10/5 2:27:13 AM | NEAR | UP | 2.8 min | -0.862% | 1¢ | ❌ Lost | -$0.15 |
| 10/5 2:26:57 AM | HYPE | UP | 3.0 min | -0.380% | 1¢ | ❌ Lost | -$0.15 |
| 10/5 2:26:42 AM | ETH | UP | 3.3 min | -0.179% | 1¢ | ❌ Lost | -$0.15 |
| 10/5 2:26:27 AM | SOL | UP | 3.5 min | -0.319% | 1¢ | ❌ Lost | -$0.15 |
| 10/5 2:26:27 AM | DOGE | UP | 3.5 min | -0.369% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
