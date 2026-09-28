# 15-Minute 1¢ Study

*Updated Mon Sep 28, 8:22 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (Mean-reversion model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Mean-reversion model ≥ 5%, hold to the close | 66 finished bets | 2% | $5.45 | +64% | +8.26¢ | $9.80 / -$4.35 |

*Expect **66 buys in the first 8 hours** — daily pace shows after 24 hours; max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Mean-reversion model ≥ 2%, hold to the close | 110 | -$0.55 | -4% |
| Mean-reversion model ≥ 5%, sell at 50¢ | 66 | -$1.80 | -21% |
| Momentum model ≥ 5%, sell at 2¢ | 32 | -$2.82 | -78% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 724 | 718 | 3 (0%) | 1.07% | -$44.70 (-52%) | Hold to the close: -$44.70 (-52%) |

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
| Volatility model | 273 | 3.5% | 0.4% (1) | -621% | ❌ Worse |
| Momentum model | 273 | 4.0% | 0.4% (1) | -739% | ❌ Worse |
| Mean-reversion model | 273 | 6.2% | 0.4% (1) | -662% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 273 | 1 | -54% | -89% | -92% | -89% |
| Volatility model ≥ 2% | 42 | 0 | -100% | -90% | -92% | -87% |
| Volatility model ≥ 5% | 24 | 0 | -100% | -81% | -86% | -76% |
| Volatility model ≥ 10% | 13 | 0 | -100% | -81% | -71% | -52% |
| Momentum model ≥ 2% | 47 | 0 | -100% | -86% | -93% | -88% |
| Momentum model ≥ 5% | 32 | 0 | -100% | -78% | -89% | -82% |
| Momentum model ≥ 10% | 21 | 0 | -100% | -88% | -81% | -69% |
| Mean-reversion model ≥ 2% | 110 | 1 | -4% | -86% | -89% | -87% |
| Mean-reversion model ≥ 5% | 66 | 1 | +64% | -85% | -86% | -77% |
| Mean-reversion model ≥ 10% | 44 | 1 | +146% | -82% | -86% | -77% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 468 | 4% | 3% | 1% | 1% | 1% | 1% |
| Commodities | 221 | 2% | 1% | 0% | 0% | 0% | 0% |
| Financials | 29 | 0% | 0% | 0% | 0% | 0% | 0% |
| **All** | 718 | 3% | 2% | 1% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 3 | 0% | -$44.70 | -52% | — |
| Sell at 2¢ | 25 | 3% | -$80.20 | -93% | 63 sec |
| Sell at 3¢ | 14 | 2% | -$81.24 | -94% | 74 sec |
| Sell at 5¢ | 8 | 1% | -$81.50 | -94% | 2.3 min |
| Sell at 10¢ | 7 | 1% | -$77.53 | -89% | 2.9 min |
| Sell at 25¢ | 4 | 1% | -$73.46 | -85% | 3.5 min |
| Sell at 50¢ | 3 | 0% | -$66.45 | -77% | 4.8 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| 5–10 min | 24 | 2 | 12% | 8% | +678% | -78% | -68% |
| 2–5 min | 250 | 1 | 7% | 2% | -60% | -88% | -91% |
| 1–2 min | 220 | 0 | 2% | 0% | -100% | -96% | -97% |
| Under 1 min | 224 | 0 | 0% | 0% | -100% | -99% | -98% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| XRP | 54 | 2 | 6% | 4% | +324% | -88% | -88% |
| ZEC | 54 | 0 | 6% | 0% | -100% | -87% | -100% |
| ETH | 53 | 1 | 2% | 2% | +146% | -95% | -93% |
| DOGE | 53 | 0 | 6% | 2% | -100% | -88% | -83% |
| NEAR | 52 | 0 | 2% | 0% | -100% | -95% | -100% |
| BTC | 52 | 0 | 12% | 4% | -100% | -71% | -78% |
| SOL | 52 | 0 | 4% | 2% | -100% | -90% | -86% |
| BNB | 51 | 0 | 2% | 0% | -100% | -96% | -94% |
| HYPE | 47 | 0 | 2% | 0% | -100% | -95% | -100% |
| GOLD | 40 | 0 | 2% | 0% | -100% | -95% | -100% |
| WTI | 36 | 0 | 3% | 0% | -100% | -94% | -100% |
| SILVER | 35 | 0 | 0% | 0% | -100% | -100% | -100% |
| NATGAS | 31 | 0 | 6% | 3% | -100% | -89% | -83% |
| PLATINUM | 28 | 0 | 0% | 0% | -100% | -100% | -100% |
| COPPER | 27 | 0 | 0% | 0% | -100% | -100% | -100% |
| PALLADIUM | 24 | 0 | 0% | 0% | -100% | -100% | -100% |
| GBPUSD | 12 | 0 | 0% | 0% | -100% | -100% | -100% |
| EURUSD | 11 | 0 | 0% | 0% | -100% | -100% | -100% |
| USDJPY | 6 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 381 | 3 | 4% | 2% | -5% | -91% | -91% |
| DOWN (bought NO) | 337 | 0 | 3% | 1% | -100% | -94% | -96% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 42 | 0 | 2% | 2% | -100% | -90% | -86% |
| 0.05–0.1% | 48 | 0 | 2% | 0% | -100% | -94% | -100% |
| 0.1–0.2% | 110 | 0 | 3% | 0% | -100% | -93% | -93% |
| 0.2–0.5% | 202 | 1 | 5% | 2% | -47% | -90% | -93% |
| Over 0.5% | 66 | 2 | 9% | 3% | +233% | -81% | -81% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 308 | 1 | 4% | 2% | -62% | -91% | -93% |
| Morning (6am–12pm) | 134 | 0 | 3% | 0% | -100% | -94% | -100% |
| Evening (6pm–12am) | 276 | 2 | 3% | 1% | -16% | -93% | -92% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 23 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 3,964 |
| Time from buy to best bounce (bounced bets) | 47 sec |
| Price snapshots per bet | 48 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 9/28 8:14:43 AM | WTI | DOWN | 16 sec | — | 0¢ | ❌ Lost | $0.00 |
| 9/28 8:14:43 AM | ZEC | UP | 16 sec | -0.092% | 0¢ | ❌ Lost | $0.00 |
| 9/28 8:13:37 AM | SOL | UP | 83 sec | -0.306% | 0¢ | ❌ Lost | $0.00 |
| 9/28 8:13:06 AM | COPPER | UP | 1.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 9/28 8:13:06 AM | EURUSD | DOWN | 1.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 9/28 8:13:06 AM | ETH | UP | 1.9 min | -0.249% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 8:12:50 AM | PLATINUM | UP | 2.1 min | — | 0¢ | ❌ Lost | -$0.15 |
| 9/28 8:12:34 AM | PALLADIUM | UP | 2.4 min | — | 0¢ | ❌ Lost | -$0.15 |
| 9/28 8:12:34 AM | GBPUSD | DOWN | 2.4 min | — | 0¢ | ❌ Lost | -$0.15 |
| 9/28 8:12:18 AM | BNB | UP | 2.7 min | -0.239% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 8:12:18 AM | DOGE | UP | 2.7 min | -0.437% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 8:11:44 AM | HYPE | UP | 3.3 min | -0.355% | 2¢ | ❌ Lost | -$0.15 |
| 9/28 8:11:28 AM | XRP | UP | 3.5 min | -0.795% | 0¢ | ❌ Lost | $0.00 |
| 9/28 8:11:28 AM | BTC | UP | 3.5 min | -0.267% | 2¢ | ❌ Lost | -$0.15 |
| 9/28 8:10:57 AM | NEAR | UP | 4.0 min | -1.409% | 2¢ | ❌ Lost | -$0.15 |
| 9/28 8:08:48 AM | SILVER | UP | 6.2 min | — | 1¢ | ❌ Lost | -$0.15 |
| 9/28 8:08:48 AM | GOLD | UP | 6.2 min | — | 1¢ | ❌ Lost | -$0.15 |
| 9/28 7:59:58 AM | EURUSD | UP | 1 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/28 7:59:26 AM | COPPER | DOWN | 33 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 9/28 7:59:09 AM | NEAR | UP | 50 sec | -0.571% | 0¢ | ❌ Lost | $0.00 |
| 9/28 7:59:09 AM | BNB | UP | 50 sec | -0.105% | 0¢ | ❌ Lost | -$0.15 |
| 9/28 7:58:53 AM | USDJPY | DOWN | 66 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/28 7:58:53 AM | SOL | UP | 66 sec | -0.135% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 7:58:53 AM | BTC | UP | 66 sec | -0.107% | 0¢ | ❌ Lost | $0.00 |
| 9/28 7:58:53 AM | XRP | UP | 66 sec | -0.315% | 0¢ | ❌ Lost | -$0.15 |
| 9/28 7:58:53 AM | GOLD | DOWN | 66 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 9/28 7:58:53 AM | ETH | UP | 66 sec | -0.174% | 0¢ | ❌ Lost | $0.00 |
| 9/28 7:58:37 AM | WTI | UP | 82 sec | — | 0¢ | ❌ Lost | $0.00 |
| 9/28 7:58:37 AM | ZEC | UP | 82 sec | -0.398% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 7:58:21 AM | NATGAS | UP | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
