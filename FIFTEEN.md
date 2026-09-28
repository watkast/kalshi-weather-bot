# 15-Minute 1¢ Study

*Updated Mon Sep 28, 4:36 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (Mean-reversion model ≥ 2%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Mean-reversion model ≥ 2%, hold to the close | 54 finished bets | 2% | $7.25 | +107% | +13.43¢ | -$3.30 / $10.55 |

*Expect **54 buys in the first 4 hours** — daily pace shows after 24 hours; max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Mean-reversion model ≥ 2%, sell at 50¢ | 54 | -$0.00 | -0% |
| Mean-reversion model ≥ 2%, sell at 25¢ | 54 | -$3.44 | -51% |
| Mean-reversion model ≥ 2%, sell at 10¢ | 54 | -$4.13 | -61% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 407 | 397 | 1 (0%) | 1.07% | -$32.95 (-70%) | Hold to the close: -$32.95 (-70%) |

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
| Volatility model | 140 | 2.6% | 0.7% (1) | -129% | ❌ Worse |
| Momentum model | 140 | 3.6% | 0.7% (1) | -281% | ❌ Worse |
| Mean-reversion model | 140 | 4.0% | 0.7% (1) | -54% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 140 | 1 | -4% | -87% | -89% | -87% |
| Volatility model ≥ 2% | 22 | 0 | -100% | -90% | -100% | -100% |
| Volatility model ≥ 5% | 13 | 0 | -100% | -83% | -100% | -100% |
| Volatility model ≥ 10% | 5 | 0 | -100% | -100% | -100% | -100% |
| Momentum model ≥ 2% | 26 | 0 | -100% | -91% | -100% | -100% |
| Momentum model ≥ 5% | 17 | 0 | -100% | -87% | -100% | -100% |
| Momentum model ≥ 10% | 13 | 0 | -100% | -100% | -100% | -100% |
| Mean-reversion model ≥ 2% | 54 | 1 | +107% | -77% | -83% | -81% |
| Mean-reversion model ≥ 5% | 29 | 1 | +289% | -78% | -78% | -64% |
| Mean-reversion model ≥ 10% | 17 | 1 | +567% | -75% | -81% | -69% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 260 | 3% | 2% | 1% | 1% | 1% | 0% |
| Commodities | 125 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 12 | 0% | 0% | 0% | 0% | 0% | 0% |
| **All** | 397 | 3% | 2% | 1% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 1 | 0% | -$32.95 | -70% | — |
| Sell at 2¢ | 11 | 3% | -$44.09 | -94% | 47 sec |
| Sell at 3¢ | 7 | 2% | -$44.22 | -94% | 47 sec |
| Sell at 5¢ | 4 | 1% | -$44.35 | -94% | 2.7 min |
| Sell at 10¢ | 4 | 1% | -$41.71 | -89% | 2.8 min |
| Sell at 25¢ | 2 | 1% | -$40.33 | -86% | 3.5 min |
| Sell at 50¢ | 1 | 0% | -$40.20 | -86% | 4.8 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| 5–10 min | 8 | 1 | 12% | 12% | +1067% | -78% | -68% |
| 2–5 min | 136 | 0 | 6% | 1% | -100% | -89% | -90% |
| 1–2 min | 122 | 0 | 2% | 1% | -100% | -97% | -97% |
| Under 1 min | 131 | 0 | 0% | 0% | -100% | -100% | -100% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| BTC | 30 | 0 | 10% | 3% | -100% | -76% | -76% |
| ETH | 30 | 0 | 0% | 0% | -100% | -100% | -100% |
| DOGE | 30 | 0 | 7% | 0% | -100% | -85% | -77% |
| XRP | 30 | 1 | 3% | 3% | +289% | -93% | -89% |
| ZEC | 30 | 0 | 7% | 0% | -100% | -84% | -100% |
| NEAR | 29 | 0 | 0% | 0% | -100% | -100% | -100% |
| SOL | 29 | 0 | 3% | 3% | -100% | -91% | -87% |
| BNB | 28 | 0 | 0% | 0% | -100% | -100% | -100% |
| HYPE | 24 | 0 | 0% | 0% | -100% | -100% | -100% |
| WTI | 23 | 0 | 4% | 0% | -100% | -92% | -100% |
| GOLD | 22 | 0 | 0% | 0% | -100% | -100% | -100% |
| SILVER | 19 | 0 | 0% | 0% | -100% | -100% | -100% |
| COPPER | 17 | 0 | 0% | 0% | -100% | -100% | -100% |
| PLATINUM | 17 | 0 | 0% | 0% | -100% | -100% | -100% |
| NATGAS | 14 | 0 | 7% | 7% | -100% | -88% | -81% |
| PALLADIUM | 13 | 0 | 0% | 0% | -100% | -100% | -100% |
| GBPUSD | 6 | 0 | 0% | 0% | -100% | -100% | -100% |
| EURUSD | 4 | 0 | 0% | 0% | -100% | -100% | -100% |
| USDJPY | 2 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 223 | 1 | 2% | 1% | -45% | -95% | -92% |
| DOWN (bought NO) | 174 | 0 | 3% | 1% | -100% | -93% | -96% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 21 | 0 | 0% | 0% | -100% | -100% | -100% |
| 0.05–0.1% | 27 | 0 | 4% | 0% | -100% | -88% | -100% |
| 0.1–0.2% | 65 | 0 | 2% | 0% | -100% | -96% | -94% |
| 0.2–0.5% | 118 | 0 | 4% | 2% | -100% | -91% | -92% |
| Over 0.5% | 29 | 1 | 7% | 3% | +289% | -86% | -78% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 212 | 1 | 4% | 1% | -44% | -92% | -94% |
| Evening (6pm–12am) | 185 | 0 | 2% | 1% | -100% | -96% | -95% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 23 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,361 |
| Time from buy to best bounce (bounced bets) | 47 sec |
| Price snapshots per bet | 46 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 9/28 4:29:56 AM | GBPUSD | DOWN | 4 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/28 4:29:40 AM | WTI | DOWN | 20 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/28 4:29:24 AM | GOLD | DOWN | 36 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 9/28 4:29:07 AM | SILVER | DOWN | 52 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 9/28 4:29:07 AM | NATGAS | UP | 52 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/28 4:29:07 AM | PLATINUM | DOWN | 52 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/28 4:29:07 AM | XRP | DOWN | 52 sec | +0.101% | 0¢ | ❌ Lost | -$0.15 |
| 9/28 4:28:51 AM | ETH | DOWN | 68 sec | +0.078% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 4:28:51 AM | COPPER | UP | 68 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 9/28 4:28:51 AM | BNB | DOWN | 68 sec | +0.070% | 0¢ | ❌ Lost | $0.00 |
| 9/28 4:28:19 AM | BTC | DOWN | 1.7 min | +0.129% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 4:27:45 AM | NEAR | DOWN | 2.2 min | +0.763% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 4:26:42 AM | DOGE | DOWN | 3.3 min | +0.326% | 5¢ | ❌ Lost | -$0.15 |
| 9/28 4:26:42 AM | SOL | DOWN | 3.3 min | +0.370% | 2¢ | ❌ Lost | $0.00 |
| 9/28 4:26:26 AM | HYPE | DOWN | 3.5 min | +0.469% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 4:26:26 AM | ZEC | DOWN | 3.5 min | +0.364% | 2¢ | ❌ Lost | -$0.15 |
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

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
