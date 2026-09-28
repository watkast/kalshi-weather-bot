# 15-Minute 1¢ Study

*Updated Mon Sep 28, 4:25 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (Mean-reversion model ≥ 2%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Mean-reversion model ≥ 2%, hold to the close | 47 finished bets | 2% | $8.00 | +133% | +17.02¢ | -$3.00 / $11.00 |

*Expect **47 buys in the first 4 hours** — daily pace shows after 24 hours; max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Mean-reversion model ≥ 2%, sell at 50¢ | 47 | $0.75 | +12% |
| Mean-reversion model ≥ 2%, sell at 25¢ | 47 | -$2.69 | -45% |
| Mean-reversion model ≥ 2%, sell at 10¢ | 47 | -$3.38 | -56% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 391 | 381 | 1 (0%) | 1.07% | -$30.85 (-69%) | Hold to the close: -$30.85 (-69%) |

*In play or awaiting result: 0. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 131 | 2.7% | 0.8% (1) | -131% | ❌ Worse |
| Momentum model | 131 | 3.8% | 0.8% (1) | -284% | ❌ Worse |
| Mean-reversion model | 131 | 4.1% | 0.8% (1) | -51% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 131 | 1 | +4% | -90% | -91% | -86% |
| Volatility model ≥ 2% | 21 | 0 | -100% | -90% | -100% | -100% |
| Volatility model ≥ 5% | 12 | 0 | -100% | -83% | -100% | -100% |
| Volatility model ≥ 10% | 5 | 0 | -100% | -100% | -100% | -100% |
| Momentum model ≥ 2% | 25 | 0 | -100% | -91% | -100% | -100% |
| Momentum model ≥ 5% | 16 | 0 | -100% | -87% | -100% | -100% |
| Momentum model ≥ 10% | 12 | 0 | -100% | -100% | -100% | -100% |
| Mean-reversion model ≥ 2% | 47 | 1 | +133% | -83% | -87% | -78% |
| Mean-reversion model ≥ 5% | 27 | 1 | +324% | -76% | -76% | -61% |
| Mean-reversion model ≥ 10% | 17 | 1 | +567% | -75% | -81% | -69% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 251 | 3% | 2% | 1% | 1% | 1% | 0% |
| Commodities | 119 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 11 | 0% | 0% | 0% | 0% | 0% | 0% |
| **All** | 381 | 2% | 2% | 1% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 1 | 0% | -$30.85 | -69% | — |
| Sell at 2¢ | 9 | 2% | -$42.51 | -95% | 32 sec |
| Sell at 3¢ | 6 | 2% | -$42.51 | -95% | 72 sec |
| Sell at 5¢ | 4 | 1% | -$42.25 | -94% | 2.7 min |
| Sell at 10¢ | 4 | 1% | -$39.61 | -88% | 2.8 min |
| Sell at 25¢ | 2 | 1% | -$38.23 | -85% | 3.5 min |
| Sell at 50¢ | 1 | 0% | -$38.10 | -85% | 4.8 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| 5–10 min | 8 | 1 | 12% | 12% | +1067% | -78% | -68% |
| 2–5 min | 131 | 0 | 5% | 2% | -100% | -91% | -91% |
| 1–2 min | 118 | 0 | 2% | 1% | -100% | -96% | -97% |
| Under 1 min | 124 | 0 | 0% | 0% | -100% | -100% | -100% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| BTC | 29 | 0 | 10% | 3% | -100% | -75% | -75% |
| ETH | 29 | 0 | 0% | 0% | -100% | -100% | -100% |
| DOGE | 29 | 0 | 3% | 0% | -100% | -92% | -88% |
| XRP | 29 | 1 | 3% | 3% | +306% | -92% | -89% |
| ZEC | 29 | 0 | 3% | 0% | -100% | -92% | -100% |
| NEAR | 28 | 0 | 0% | 0% | -100% | -100% | -100% |
| SOL | 28 | 0 | 4% | 4% | -100% | -91% | -87% |
| BNB | 27 | 0 | 0% | 0% | -100% | -100% | -100% |
| HYPE | 23 | 0 | 0% | 0% | -100% | -100% | -100% |
| WTI | 22 | 0 | 5% | 0% | -100% | -91% | -100% |
| GOLD | 21 | 0 | 0% | 0% | -100% | -100% | -100% |
| SILVER | 18 | 0 | 0% | 0% | -100% | -100% | -100% |
| COPPER | 16 | 0 | 0% | 0% | -100% | -100% | -100% |
| PLATINUM | 16 | 0 | 0% | 0% | -100% | -100% | -100% |
| NATGAS | 13 | 0 | 8% | 8% | -100% | -87% | -80% |
| PALLADIUM | 13 | 0 | 0% | 0% | -100% | -100% | -100% |
| GBPUSD | 5 | 0 | 0% | 0% | -100% | -100% | -100% |
| EURUSD | 4 | 0 | 0% | 0% | -100% | -100% | -100% |
| USDJPY | 2 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 221 | 1 | 2% | 1% | -44% | -95% | -92% |
| DOWN (bought NO) | 160 | 0 | 2% | 1% | -100% | -95% | -98% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 21 | 0 | 0% | 0% | -100% | -100% | -100% |
| 0.05–0.1% | 25 | 0 | 4% | 0% | -100% | -88% | -100% |
| 0.1–0.2% | 63 | 0 | 2% | 0% | -100% | -96% | -93% |
| 0.2–0.5% | 114 | 0 | 3% | 2% | -100% | -95% | -95% |
| Over 0.5% | 28 | 1 | 7% | 4% | +306% | -85% | -77% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 196 | 1 | 3% | 2% | -39% | -93% | -95% |
| Evening (6pm–12am) | 185 | 0 | 2% | 1% | -100% | -96% | -95% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 23 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,720 |
| Time from buy to best bounce (bounced bets) | 40 sec |
| Price snapshots per bet | 46 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 9/28 4:14:15 AM | NEAR | UP | 45 sec | -0.522% | 0¢ | ❌ Lost | $0.00 |
| 9/28 4:14:15 AM | HYPE | DOWN | 45 sec | +0.054% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 4:13:59 AM | ZEC | DOWN | 61 sec | +0.244% | 0¢ | ❌ Lost | $0.00 |
| 9/28 4:13:59 AM | BTC | DOWN | 61 sec | +0.040% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 4:13:59 AM | SOL | DOWN | 61 sec | +0.160% | 0¢ | ❌ Lost | $0.00 |
| 9/28 4:13:43 AM | BNB | DOWN | 77 sec | +0.057% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 4:13:43 AM | XRP | DOWN | 77 sec | +0.257% | 0¢ | ❌ Lost | $0.00 |
| 9/28 4:13:10 AM | GBPUSD | UP | 1.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 9/28 4:12:38 AM | WTI | DOWN | 2.4 min | — | 2¢ | ❌ Lost | -$0.15 |
| 9/28 4:12:06 AM | ETH | DOWN | 2.9 min | +0.182% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 4:12:06 AM | DOGE | DOWN | 2.9 min | +0.377% | 0¢ | ❌ Lost | -$0.15 |
| 9/28 3:59:50 AM | SOL | UP | 9 sec | -0.017% | 0¢ | ❌ Lost | $0.00 |
| 9/28 3:59:34 AM | ETH | DOWN | 25 sec | +0.030% | 0¢ | ❌ Lost | $0.00 |
| 9/28 3:59:34 AM | DOGE | DOWN | 25 sec | +0.011% | 0¢ | ❌ Lost | -$0.15 |
| 9/28 3:59:34 AM | BTC | DOWN | 25 sec | -0.007% | 0¢ | ❌ Lost | $0.00 |
| 9/28 3:59:34 AM | USDJPY | UP | 25 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/28 3:59:18 AM | PLATINUM | DOWN | 41 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/28 3:59:18 AM | XRP | DOWN | 41 sec | +0.081% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 3:59:02 AM | BNB | DOWN | 57 sec | +0.053% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 3:59:02 AM | ZEC | DOWN | 57 sec | +0.132% | 0¢ | ❌ Lost | -$0.15 |
| 9/28 3:58:46 AM | SILVER | DOWN | 73 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 9/28 3:58:46 AM | NEAR | DOWN | 73 sec | +0.427% | 0¢ | ❌ Lost | $0.00 |
| 9/28 3:58:30 AM | COPPER | DOWN | 89 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/28 3:58:14 AM | EURUSD | UP | 1.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 9/28 3:58:14 AM | GOLD | DOWN | 1.8 min | — | 1¢ | ❌ Lost | -$0.15 |
| 9/28 3:57:10 AM | WTI | DOWN | 2.8 min | — | 1¢ | ❌ Lost | -$0.15 |
| 9/28 3:44:38 AM | HYPE | DOWN | 21 sec | +0.047% | 0¢ | ❌ Lost | $0.00 |
| 9/28 3:44:22 AM | PLATINUM | DOWN | 37 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/28 3:43:49 AM | GOLD | DOWN | 70 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 9/28 3:43:49 AM | XRP | UP | 70 sec | -0.162% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
