# 15-Minute 1¢ Study

*Updated Mon Sep 28, 7:21 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (Mean-reversion model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Mean-reversion model ≥ 5%, hold to the close | 60 finished bets | 2% | $6.20 | +79% | +10.33¢ | $10.25 / -$4.05 |

*Expect **60 buys in the first 7 hours** — daily pace shows after 24 hours; max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Mean-reversion model ≥ 2%, hold to the close | 101 | $0.65 | +5% |
| Mean-reversion model ≥ 5%, sell at 50¢ | 60 | -$1.05 | -13% |
| Momentum model ≥ 2%, sell at 5¢ | 40 | -$4.00 | -86% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 664 | 658 | 3 (0%) | 1.07% | -$37.50 (-47%) | Hold to the close: -$37.50 (-47%) |

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
| Volatility model | 237 | 3.9% | 0.4% (1) | -650% | ❌ Worse |
| Momentum model | 237 | 4.4% | 0.4% (1) | -776% | ❌ Worse |
| Mean-reversion model | 237 | 6.4% | 0.4% (1) | -655% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 237 | 1 | -47% | -89% | -91% | -88% |
| Volatility model ≥ 2% | 41 | 0 | -100% | -89% | -92% | -87% |
| Volatility model ≥ 5% | 23 | 0 | -100% | -80% | -85% | -75% |
| Volatility model ≥ 10% | 12 | 0 | -100% | -78% | -68% | -46% |
| Momentum model ≥ 2% | 40 | 0 | -100% | -89% | -92% | -86% |
| Momentum model ≥ 5% | 27 | 0 | -100% | -83% | -87% | -78% |
| Momentum model ≥ 10% | 20 | 0 | -100% | -88% | -81% | -69% |
| Mean-reversion model ≥ 2% | 101 | 1 | +5% | -84% | -88% | -85% |
| Mean-reversion model ≥ 5% | 60 | 1 | +79% | -83% | -85% | -75% |
| Mean-reversion model ≥ 10% | 40 | 1 | +175% | -80% | -85% | -75% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 432 | 4% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 202 | 1% | 1% | 0% | 0% | 0% | 0% |
| Financials | 24 | 0% | 0% | 0% | 0% | 0% | 0% |
| **All** | 658 | 3% | 2% | 1% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 3 | 0% | -$37.50 | -47% | — |
| Sell at 2¢ | 22 | 3% | -$73.78 | -93% | 64 sec |
| Sell at 3¢ | 14 | 2% | -$74.04 | -93% | 74 sec |
| Sell at 5¢ | 8 | 1% | -$74.30 | -93% | 2.3 min |
| Sell at 10¢ | 7 | 1% | -$70.33 | -88% | 2.9 min |
| Sell at 25¢ | 4 | 1% | -$66.26 | -83% | 3.5 min |
| Sell at 50¢ | 3 | 0% | -$59.25 | -75% | 4.8 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| 5–10 min | 22 | 2 | 14% | 9% | +748% | -76% | -65% |
| 2–5 min | 234 | 1 | 6% | 2% | -58% | -88% | -91% |
| 1–2 min | 193 | 0 | 2% | 1% | -100% | -97% | -97% |
| Under 1 min | 209 | 0 | 0% | 0% | -100% | -99% | -98% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| XRP | 50 | 2 | 6% | 4% | +355% | -87% | -87% |
| ZEC | 50 | 0 | 6% | 0% | -100% | -87% | -100% |
| ETH | 49 | 1 | 2% | 2% | +167% | -95% | -93% |
| DOGE | 49 | 0 | 6% | 2% | -100% | -88% | -81% |
| NEAR | 48 | 0 | 0% | 0% | -100% | -100% | -100% |
| BTC | 48 | 0 | 10% | 4% | -100% | -74% | -76% |
| SOL | 48 | 0 | 4% | 2% | -100% | -90% | -85% |
| BNB | 47 | 0 | 2% | 0% | -100% | -95% | -93% |
| HYPE | 43 | 0 | 2% | 0% | -100% | -95% | -100% |
| GOLD | 36 | 0 | 0% | 0% | -100% | -100% | -100% |
| WTI | 34 | 0 | 3% | 0% | -100% | -94% | -100% |
| SILVER | 32 | 0 | 0% | 0% | -100% | -100% | -100% |
| NATGAS | 29 | 0 | 7% | 3% | -100% | -88% | -82% |
| COPPER | 25 | 0 | 0% | 0% | -100% | -100% | -100% |
| PLATINUM | 25 | 0 | 0% | 0% | -100% | -100% | -100% |
| PALLADIUM | 21 | 0 | 0% | 0% | -100% | -100% | -100% |
| GBPUSD | 11 | 0 | 0% | 0% | -100% | -100% | -100% |
| EURUSD | 8 | 0 | 0% | 0% | -100% | -100% | -100% |
| USDJPY | 5 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 349 | 3 | 4% | 2% | +3% | -92% | -90% |
| DOWN (bought NO) | 309 | 0 | 3% | 1% | -100% | -94% | -96% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 39 | 0 | 3% | 3% | -100% | -89% | -84% |
| 0.05–0.1% | 45 | 0 | 2% | 0% | -100% | -94% | -100% |
| 0.1–0.2% | 102 | 0 | 3% | 0% | -100% | -92% | -92% |
| 0.2–0.5% | 184 | 1 | 5% | 2% | -42% | -90% | -92% |
| Over 0.5% | 62 | 2 | 8% | 3% | +246% | -84% | -81% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 308 | 1 | 4% | 2% | -62% | -91% | -93% |
| Morning (6am–12pm) | 74 | 0 | 1% | 0% | -100% | -97% | -100% |
| Evening (6pm–12am) | 276 | 2 | 3% | 1% | -16% | -93% | -92% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 23 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 3,972 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 48 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 9/28 7:14:55 AM | SILVER | UP | 4 sec | — | 0¢ | ❌ Lost | $0.00 |
| 9/28 7:14:39 AM | ZEC | DOWN | 20 sec | +0.167% | 0¢ | ❌ Lost | $0.00 |
| 9/28 7:14:07 AM | PLATINUM | UP | 53 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/28 7:13:02 AM | PALLADIUM | UP | 1.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 9/28 7:12:30 AM | GOLD | UP | 2.5 min | — | 1¢ | ❌ Lost | -$0.15 |
| 9/28 7:11:08 AM | COPPER | UP | 3.9 min | — | 1¢ | ❌ Lost | -$0.15 |
| 9/28 7:10:51 AM | ETH | UP | 4.1 min | -0.359% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 7:10:35 AM | SOL | UP | 4.4 min | -0.520% | 0¢ | ❌ Lost | -$0.15 |
| 9/28 7:10:35 AM | BTC | UP | 4.4 min | -0.310% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 7:10:35 AM | XRP | UP | 4.4 min | -0.597% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 7:10:19 AM | GBPUSD | UP | 4.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 9/28 7:10:19 AM | DOGE | UP | 4.7 min | -0.652% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 7:10:19 AM | BNB | UP | 4.7 min | -0.530% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 7:08:57 AM | HYPE | UP | 6.0 min | -0.791% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 6:59:40 AM | SILVER | DOWN | 20 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/28 6:59:24 AM | COPPER | DOWN | 36 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/28 6:58:02 AM | NEAR | DOWN | 1.9 min | +1.087% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 6:57:30 AM | GOLD | DOWN | 2.5 min | — | 1¢ | ❌ Lost | -$0.15 |
| 9/28 6:57:14 AM | WTI | UP | 2.8 min | — | 1¢ | ❌ Lost | -$0.15 |
| 9/28 6:56:57 AM | DOGE | DOWN | 3.0 min | +0.480% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 6:55:37 AM | HYPE | DOWN | 4.4 min | +0.394% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 6:55:21 AM | BNB | DOWN | 4.6 min | +0.305% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 6:55:21 AM | SOL | DOWN | 4.6 min | +0.577% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 6:55:21 AM | ZEC | DOWN | 4.6 min | +0.814% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 6:55:05 AM | XRP | DOWN | 4.9 min | +0.853% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 6:55:05 AM | BTC | DOWN | 4.9 min | +0.354% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 6:53:44 AM | ETH | DOWN | 6.3 min | +0.452% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 6:44:53 AM | SOL | DOWN | 7 sec | +0.113% | 0¢ | ❌ Lost | -$0.15 |
| 9/28 6:44:53 AM | HYPE | DOWN | 7 sec | +0.065% | 0¢ | ❌ Lost | $0.00 |
| 9/28 6:44:21 AM | ZEC | DOWN | 39 sec | +0.051% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
