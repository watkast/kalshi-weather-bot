# 15-Minute 1¢ Study

*Updated Mon Sep 28, 10:34 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade small.** Profitable in both halves of the data; sample still modest.

1. **Watch** every 15-minute up/down market (Mean-reversion model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Mean-reversion model ≥ 5%, hold to the close | 95 finished bets | 2% | $16.00 | +133% | +16.84¢ | $8.00 / $8.00 |

*Expect **95 buys in the first 10 hours** — daily pace shows after 24 hours; max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Mean-reversion model ≥ 2%, hold to the close | 146 | $9.55 | +52% |
| Volatility model ≥ 2%, hold to the close | 69 | $5.75 | +70% |
| Mean-reversion model ≥ 5%, sell at 50¢ | 95 | $1.50 | +12% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 856 | 850 | 4 (0%) | 1.07% | -$45.40 (-45%) | Hold to the close: -$45.40 (-45%) |

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
| Volatility model | 353 | 3.7% | 0.6% (2) | -501% | ❌ Worse |
| Momentum model | 353 | 3.9% | 0.6% (2) | -608% | ❌ Worse |
| Mean-reversion model | 353 | 6.9% | 0.6% (2) | -530% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 353 | 2 | -25% | -89% | -91% | -88% |
| Volatility model ≥ 2% | 69 | 1 | +70% | -84% | -81% | -76% |
| Volatility model ≥ 5% | 35 | 0 | -100% | -74% | -71% | -68% |
| Volatility model ≥ 10% | 20 | 0 | -100% | -88% | -81% | -69% |
| Momentum model ≥ 2% | 62 | 0 | -100% | -86% | -89% | -91% |
| Momentum model ≥ 5% | 37 | 0 | -100% | -81% | -90% | -84% |
| Momentum model ≥ 10% | 25 | 0 | -100% | -90% | -85% | -75% |
| Mean-reversion model ≥ 2% | 146 | 2 | +52% | -84% | -85% | -82% |
| Mean-reversion model ≥ 5% | 95 | 2 | +133% | -83% | -80% | -73% |
| Mean-reversion model ≥ 10% | 63 | 2 | +259% | -77% | -75% | -67% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 548 | 4% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 266 | 2% | 1% | 0% | 0% | 0% | 0% |
| Financials | 36 | 0% | 0% | 0% | 0% | 0% | 0% |
| **All** | 850 | 3% | 2% | 1% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 4 | 0% | -$45.40 | -45% | — |
| Sell at 2¢ | 28 | 3% | -$94.12 | -93% | 62 sec |
| Sell at 3¢ | 17 | 2% | -$94.77 | -93% | 67 sec |
| Sell at 5¢ | 10 | 1% | -$94.90 | -94% | 1.9 min |
| Sell at 10¢ | 9 | 1% | -$89.61 | -88% | 2.4 min |
| Sell at 25¢ | 6 | 1% | -$81.54 | -80% | 2.8 min |
| Sell at 50¢ | 4 | 0% | -$74.40 | -73% | 4.7 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| 5–10 min | 28 | 2 | 11% | 7% | +567% | -81% | -72% |
| 2–5 min | 290 | 2 | 7% | 2% | -32% | -88% | -91% |
| 1–2 min | 263 | 0 | 2% | 0% | -100% | -96% | -97% |
| Under 1 min | 269 | 0 | 0% | 0% | -100% | -99% | -98% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ETH | 63 | 2 | 5% | 3% | +315% | -88% | -83% |
| DOGE | 62 | 0 | 5% | 2% | -100% | -90% | -84% |
| XRP | 62 | 2 | 5% | 3% | +289% | -89% | -89% |
| ZEC | 62 | 0 | 5% | 0% | -100% | -89% | -100% |
| NEAR | 61 | 0 | 2% | 0% | -100% | -96% | -100% |
| BTC | 61 | 0 | 10% | 3% | -100% | -73% | -80% |
| SOL | 61 | 0 | 3% | 2% | -100% | -91% | -87% |
| BNB | 60 | 0 | 2% | 0% | -100% | -96% | -95% |
| HYPE | 56 | 0 | 4% | 2% | -100% | -92% | -94% |
| GOLD | 49 | 0 | 2% | 0% | -100% | -96% | -100% |
| WTI | 44 | 0 | 2% | 0% | -100% | -95% | -100% |
| SILVER | 42 | 0 | 0% | 0% | -100% | -100% | -100% |
| NATGAS | 36 | 0 | 6% | 3% | -100% | -90% | -86% |
| PLATINUM | 34 | 0 | 0% | 0% | -100% | -100% | -100% |
| COPPER | 33 | 0 | 0% | 0% | -100% | -100% | -100% |
| PALLADIUM | 28 | 0 | 0% | 0% | -100% | -100% | -100% |
| GBPUSD | 16 | 0 | 0% | 0% | -100% | -100% | -100% |
| EURUSD | 13 | 0 | 0% | 0% | -100% | -100% | -100% |
| USDJPY | 7 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 438 | 3 | 3% | 1% | -16% | -92% | -92% |
| DOWN (bought NO) | 412 | 1 | 3% | 1% | -73% | -93% | -95% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 46 | 0 | 2% | 2% | -100% | -91% | -86% |
| 0.05–0.1% | 53 | 0 | 2% | 0% | -100% | -94% | -100% |
| 0.1–0.2% | 128 | 0 | 3% | 0% | -100% | -91% | -90% |
| 0.2–0.5% | 229 | 2 | 5% | 2% | -4% | -90% | -92% |
| Over 0.5% | 92 | 2 | 8% | 3% | +142% | -84% | -83% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 308 | 1 | 4% | 2% | -62% | -91% | -93% |
| Morning (6am–12pm) | 266 | 1 | 3% | 1% | -56% | -94% | -96% |
| Evening (6pm–12am) | 276 | 2 | 3% | 1% | -16% | -93% | -92% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 23 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 3,813 |
| Time from buy to best bounce (bounced bets) | 47 sec |
| Price snapshots per bet | 46 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 9/28 10:28:17 AM | GBPUSD | DOWN | 1.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 9/28 10:27:45 AM | PALLADIUM | DOWN | 2.2 min | — | 0¢ | ❌ Lost | -$0.15 |
| 9/28 10:26:42 AM | COPPER | DOWN | 3.3 min | — | 1¢ | ❌ Lost | -$0.15 |
| 9/28 10:26:26 AM | ZEC | DOWN | 3.5 min | +1.059% | 0¢ | ❌ Lost | $0.00 |
| 9/28 10:26:10 AM | NEAR | DOWN | 3.8 min | +1.639% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 10:26:10 AM | ETH | DOWN | 3.8 min | +0.721% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 10:26:10 AM | GOLD | DOWN | 3.8 min | — | 1¢ | ❌ Lost | -$0.15 |
| 9/28 10:25:54 AM | WTI | UP | 4.1 min | — | 1¢ | ❌ Lost | -$0.15 |
| 9/28 10:25:54 AM | XRP | DOWN | 4.1 min | +1.271% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 10:25:22 AM | DOGE | DOWN | 4.6 min | +1.290% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 10:25:22 AM | HYPE | DOWN | 4.6 min | +0.773% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 10:25:22 AM | BNB | DOWN | 4.6 min | +0.515% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 10:25:06 AM | PLATINUM | DOWN | 4.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 9/28 10:24:50 AM | SOL | DOWN | 5.2 min | +1.086% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 10:24:33 AM | BTC | DOWN | 5.4 min | +0.549% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 10:20:44 AM | SILVER | DOWN | 9.3 min | — | 1¢ | ❌ Lost | -$0.15 |
| 9/28 10:14:37 AM | NEAR | UP | 23 sec | -0.224% | 0¢ | ❌ Lost | $0.00 |
| 9/28 10:14:37 AM | SOL | UP | 23 sec | -0.067% | 0¢ | ❌ Lost | $0.00 |
| 9/28 10:14:21 AM | BTC | DOWN | 39 sec | +0.021% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 10:14:21 AM | DOGE | DOWN | 39 sec | +0.129% | 0¢ | ❌ Lost | $0.00 |
| 9/28 10:13:49 AM | ETH | UP | 71 sec | -0.136% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 10:13:49 AM | ZEC | UP | 71 sec | -0.397% | 0¢ | ❌ Lost | -$0.15 |
| 9/28 10:13:33 AM | NATGAS | UP | 87 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/28 10:13:33 AM | HYPE | DOWN | 87 sec | +0.211% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 10:13:33 AM | BNB | DOWN | 87 sec | +0.088% | 0¢ | ❌ Lost | -$0.15 |
| 9/28 10:13:00 AM | GOLD | UP | 2.0 min | — | 1¢ | ❌ Lost | -$0.15 |
| 9/28 10:12:44 AM | SILVER | UP | 2.2 min | — | 1¢ | ❌ Lost | -$0.15 |
| 9/28 10:12:44 AM | COPPER | UP | 2.2 min | — | 1¢ | ❌ Lost | -$0.15 |
| 9/28 10:10:03 AM | WTI | UP | 4.9 min | — | 1¢ | ❌ Lost | -$0.15 |
| 9/28 9:59:34 AM | COPPER | DOWN | 25 sec | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
