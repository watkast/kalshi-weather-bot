# 15-Minute 1¢ Study

*Updated Mon Sep 28, 9:23 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade small.** Profitable in both halves of the data; sample still modest.

1. **Watch** every 15-minute up/down market (Mean-reversion model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Mean-reversion model ≥ 5%, hold to the close | 72 finished bets | 3% | $18.70 | +201% | +25.97¢ | $9.35 / $9.35 |

*Expect **72 buys in the first 9 hours** — daily pace shows after 24 hours; max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Mean-reversion model ≥ 2%, hold to the close | 118 | $12.40 | +79% |
| Volatility model ≥ 2%, hold to the close | 47 | $8.15 | +139% |
| Mean-reversion model ≥ 5%, sell at 50¢ | 72 | $4.20 | +45% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 782 | 776 | 4 (1%) | 1.07% | -$36.70 (-40%) | Hold to the close: -$36.70 (-40%) |

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
| Volatility model | 309 | 3.5% | 0.6% (2) | -437% | ❌ Worse |
| Momentum model | 309 | 3.9% | 0.6% (2) | -552% | ❌ Worse |
| Mean-reversion model | 309 | 6.3% | 0.6% (2) | -441% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 309 | 2 | -16% | -87% | -89% | -86% |
| Volatility model ≥ 2% | 47 | 1 | +139% | -78% | -73% | -67% |
| Volatility model ≥ 5% | 27 | 0 | -100% | -67% | -63% | -59% |
| Volatility model ≥ 10% | 14 | 0 | -100% | -83% | -74% | -57% |
| Momentum model ≥ 2% | 51 | 0 | -100% | -83% | -87% | -89% |
| Momentum model ≥ 5% | 33 | 0 | -100% | -79% | -90% | -83% |
| Momentum model ≥ 10% | 22 | 0 | -100% | -88% | -83% | -71% |
| Mean-reversion model ≥ 2% | 118 | 2 | +79% | -82% | -82% | -79% |
| Mean-reversion model ≥ 5% | 72 | 2 | +201% | -78% | -75% | -65% |
| Mean-reversion model ≥ 10% | 49 | 2 | +344% | -71% | -69% | -59% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 504 | 5% | 3% | 2% | 2% | 1% | 1% |
| Commodities | 240 | 2% | 1% | 0% | 0% | 0% | 0% |
| Financials | 32 | 0% | 0% | 0% | 0% | 0% | 0% |
| **All** | 776 | 4% | 2% | 1% | 1% | 1% | 1% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 4 | 1% | -$36.70 | -40% | — |
| Sell at 2¢ | 28 | 4% | -$85.42 | -92% | 62 sec |
| Sell at 3¢ | 17 | 2% | -$86.07 | -93% | 67 sec |
| Sell at 5¢ | 10 | 1% | -$86.20 | -93% | 1.9 min |
| Sell at 10¢ | 9 | 1% | -$80.91 | -87% | 2.4 min |
| Sell at 25¢ | 6 | 1% | -$72.84 | -79% | 2.8 min |
| Sell at 50¢ | 4 | 1% | -$65.70 | -71% | 4.7 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| 5–10 min | 25 | 2 | 12% | 8% | +647% | -79% | -69% |
| 2–5 min | 263 | 2 | 7% | 2% | -25% | -87% | -90% |
| 1–2 min | 240 | 0 | 2% | 0% | -100% | -96% | -96% |
| Under 1 min | 248 | 0 | 0% | 0% | -100% | -99% | -98% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ETH | 58 | 2 | 5% | 3% | +355% | -87% | -81% |
| XRP | 58 | 2 | 5% | 3% | +315% | -88% | -88% |
| DOGE | 57 | 0 | 5% | 2% | -100% | -89% | -83% |
| ZEC | 57 | 0 | 5% | 0% | -100% | -88% | -100% |
| NEAR | 56 | 0 | 2% | 0% | -100% | -96% | -100% |
| BTC | 56 | 0 | 11% | 4% | -100% | -71% | -78% |
| SOL | 56 | 0 | 4% | 2% | -100% | -91% | -86% |
| BNB | 55 | 0 | 2% | 0% | -100% | -96% | -94% |
| HYPE | 51 | 0 | 4% | 2% | -100% | -91% | -93% |
| GOLD | 44 | 0 | 2% | 0% | -100% | -95% | -100% |
| WTI | 40 | 0 | 2% | 0% | -100% | -95% | -100% |
| SILVER | 37 | 0 | 0% | 0% | -100% | -100% | -100% |
| NATGAS | 34 | 0 | 6% | 3% | -100% | -90% | -85% |
| PLATINUM | 32 | 0 | 0% | 0% | -100% | -100% | -100% |
| COPPER | 29 | 0 | 0% | 0% | -100% | -100% | -100% |
| PALLADIUM | 24 | 0 | 0% | 0% | -100% | -100% | -100% |
| GBPUSD | 14 | 0 | 0% | 0% | -100% | -100% | -100% |
| EURUSD | 12 | 0 | 0% | 0% | -100% | -100% | -100% |
| USDJPY | 6 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 418 | 3 | 4% | 1% | -13% | -92% | -92% |
| DOWN (bought NO) | 358 | 1 | 4% | 1% | -69% | -92% | -94% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 44 | 0 | 2% | 2% | -100% | -90% | -86% |
| 0.05–0.1% | 51 | 0 | 2% | 0% | -100% | -94% | -100% |
| 0.1–0.2% | 119 | 0 | 3% | 0% | -100% | -91% | -89% |
| 0.2–0.5% | 211 | 2 | 5% | 2% | +3% | -90% | -91% |
| Over 0.5% | 79 | 2 | 9% | 4% | +179% | -82% | -81% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 308 | 1 | 4% | 2% | -62% | -91% | -93% |
| Morning (6am–12pm) | 192 | 1 | 4% | 1% | -39% | -92% | -95% |
| Evening (6pm–12am) | 276 | 2 | 3% | 1% | -16% | -93% | -92% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 23 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 3,886 |
| Time from buy to best bounce (bounced bets) | 47 sec |
| Price snapshots per bet | 46 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 9/28 9:14:56 AM | BTC | DOWN | 3 sec | +0.004% | 0¢ | ❌ Lost | $0.00 |
| 9/28 9:14:56 AM | GOLD | DOWN | 3 sec | — | 0¢ | ❌ Lost | $0.00 |
| 9/28 9:14:56 AM | ETH | UP | 3 sec | -0.022% | 0¢ | ❌ Lost | $0.00 |
| 9/28 9:14:56 AM | BNB | DOWN | 3 sec | -0.062% | 0¢ | ❌ Lost | -$0.15 |
| 9/28 9:14:40 AM | XRP | UP | 19 sec | -0.202% | 0¢ | ❌ Lost | $0.00 |
| 9/28 9:14:40 AM | SOL | UP | 19 sec | -0.104% | 0¢ | ❌ Lost | $0.00 |
| 9/28 9:14:24 AM | DOGE | DOWN | 35 sec | +0.192% | 0¢ | ❌ Lost | $0.00 |
| 9/28 9:13:49 AM | SILVER | DOWN | 70 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 9/28 9:13:33 AM | WTI | UP | 86 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/28 9:13:17 AM | PLATINUM | DOWN | 1.7 min | — | 1¢ | ❌ Lost | -$0.15 |
| 9/28 9:12:45 AM | NATGAS | UP | 2.2 min | — | 0¢ | ❌ Lost | -$0.15 |
| 9/28 9:12:13 AM | NEAR | UP | 2.8 min | -3.165% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 9:10:20 AM | HYPE | DOWN | 4.7 min | +0.602% | 26¢ | ❌ Lost | -$0.15 |
| 9/28 8:59:39 AM | XRP | UP | 20 sec | -0.094% | 0¢ | ❌ Lost | $0.00 |
| 9/28 8:59:39 AM | BTC | DOWN | 20 sec | +0.095% | 0¢ | ❌ Lost | $0.00 |
| 9/28 8:59:39 AM | SOL | UP | 20 sec | -0.130% | 0¢ | ❌ Lost | $0.00 |
| 9/28 8:59:23 AM | BNB | UP | 36 sec | -0.145% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 8:59:23 AM | HYPE | DOWN | 36 sec | +0.157% | 0¢ | ❌ Lost | $0.00 |
| 9/28 8:58:33 AM | NATGAS | UP | 87 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/28 8:58:33 AM | EURUSD | DOWN | 87 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 9/28 8:58:33 AM | ETH | DOWN | 87 sec | +0.145% | 4¢ | ❌ Lost | -$0.15 |
| 9/28 8:58:02 AM | DOGE | DOWN | 1.9 min | +0.414% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 8:58:02 AM | PLATINUM | UP | 1.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 9/28 8:57:46 AM | NEAR | DOWN | 2.2 min | +0.956% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 8:57:30 AM | GOLD | UP | 2.5 min | — | 1¢ | ❌ Lost | -$0.15 |
| 9/28 8:55:03 AM | WTI | DOWN | 5.0 min | — | 1¢ | ❌ Lost | -$0.15 |
| 9/28 8:53:26 AM | ZEC | UP | 6.6 min | -2.161% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 8:44:37 AM | ZEC | UP | 23 sec | -0.114% | 0¢ | ❌ Lost | $0.00 |
| 9/28 8:44:21 AM | BNB | UP | 39 sec | -0.111% | 0¢ | ❌ Lost | $0.00 |
| 9/28 8:44:06 AM | XRP | UP | 54 sec | -0.729% | 0¢ | ❌ Lost | $0.00 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
