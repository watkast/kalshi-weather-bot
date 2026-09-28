# 15-Minute 1¢ Study

*Updated Mon Sep 28, 8:12 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

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
| Momentum model ≥ 2%, sell at 5¢ | 43 | -$4.30 | -87% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 715 | 701 | 3 (0%) | 1.07% | -$42.75 (-50%) | Hold to the close: -$42.75 (-50%) |

*In play or awaiting result: 14. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 264 | 3.6% | 0.4% (1) | -629% | ❌ Worse |
| Momentum model | 264 | 4.0% | 0.4% (1) | -747% | ❌ Worse |
| Mean-reversion model | 264 | 6.5% | 0.4% (1) | -671% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 264 | 1 | -52% | -90% | -92% | -89% |
| Volatility model ≥ 2% | 42 | 0 | -100% | -90% | -92% | -87% |
| Volatility model ≥ 5% | 24 | 0 | -100% | -81% | -86% | -76% |
| Volatility model ≥ 10% | 13 | 0 | -100% | -81% | -71% | -52% |
| Momentum model ≥ 2% | 43 | 0 | -100% | -89% | -92% | -87% |
| Momentum model ≥ 5% | 29 | 0 | -100% | -83% | -88% | -79% |
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
| Crypto | 459 | 4% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 215 | 2% | 1% | 0% | 0% | 0% | 0% |
| Financials | 27 | 0% | 0% | 0% | 0% | 0% | 0% |
| **All** | 701 | 3% | 2% | 1% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 3 | 0% | -$42.75 | -50% | — |
| Sell at 2¢ | 23 | 3% | -$78.77 | -93% | 63 sec |
| Sell at 3¢ | 14 | 2% | -$79.29 | -94% | 74 sec |
| Sell at 5¢ | 8 | 1% | -$79.55 | -94% | 2.3 min |
| Sell at 10¢ | 7 | 1% | -$75.58 | -89% | 2.9 min |
| Sell at 25¢ | 4 | 1% | -$71.51 | -84% | 3.5 min |
| Sell at 50¢ | 3 | 0% | -$64.50 | -76% | 4.8 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| 5–10 min | 22 | 2 | 14% | 9% | +748% | -76% | -65% |
| 2–5 min | 241 | 1 | 6% | 2% | -59% | -89% | -91% |
| 1–2 min | 216 | 0 | 2% | 0% | -100% | -96% | -97% |
| Under 1 min | 222 | 0 | 0% | 0% | -100% | -99% | -98% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| XRP | 53 | 2 | 6% | 4% | +324% | -88% | -88% |
| ZEC | 53 | 0 | 6% | 0% | -100% | -87% | -100% |
| ETH | 52 | 1 | 2% | 2% | +152% | -95% | -93% |
| DOGE | 52 | 0 | 6% | 2% | -100% | -88% | -82% |
| NEAR | 51 | 0 | 0% | 0% | -100% | -100% | -100% |
| BTC | 51 | 0 | 10% | 4% | -100% | -75% | -78% |
| SOL | 51 | 0 | 4% | 2% | -100% | -90% | -86% |
| BNB | 50 | 0 | 2% | 0% | -100% | -96% | -93% |
| HYPE | 46 | 0 | 2% | 0% | -100% | -95% | -100% |
| GOLD | 39 | 0 | 3% | 0% | -100% | -95% | -100% |
| WTI | 35 | 0 | 3% | 0% | -100% | -94% | -100% |
| SILVER | 34 | 0 | 0% | 0% | -100% | -100% | -100% |
| NATGAS | 31 | 0 | 6% | 3% | -100% | -89% | -83% |
| PLATINUM | 27 | 0 | 0% | 0% | -100% | -100% | -100% |
| COPPER | 26 | 0 | 0% | 0% | -100% | -100% | -100% |
| PALLADIUM | 23 | 0 | 0% | 0% | -100% | -100% | -100% |
| GBPUSD | 11 | 0 | 0% | 0% | -100% | -100% | -100% |
| EURUSD | 10 | 0 | 0% | 0% | -100% | -100% | -100% |
| USDJPY | 6 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 367 | 3 | 4% | 2% | -2% | -92% | -91% |
| DOWN (bought NO) | 334 | 0 | 3% | 1% | -100% | -94% | -96% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 42 | 0 | 2% | 2% | -100% | -90% | -86% |
| 0.05–0.1% | 47 | 0 | 2% | 0% | -100% | -94% | -100% |
| 0.1–0.2% | 110 | 0 | 3% | 0% | -100% | -93% | -93% |
| 0.2–0.5% | 196 | 1 | 5% | 2% | -46% | -91% | -92% |
| Over 0.5% | 64 | 2 | 8% | 3% | +239% | -84% | -81% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 308 | 1 | 4% | 2% | -62% | -91% | -93% |
| Morning (6am–12pm) | 117 | 0 | 2% | 0% | -100% | -97% | -100% |
| Evening (6pm–12am) | 276 | 2 | 3% | 1% | -16% | -93% | -92% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 23 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 3,971 |
| Time from buy to best bounce (bounced bets) | 47 sec |
| Price snapshots per bet | 46 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 9/28 8:12:18 AM | BNB | UP | 2.7 min | -0.239% | — | In play | — |
| 9/28 8:12:18 AM | DOGE | UP | 2.7 min | -0.437% | — | In play | — |
| 9/28 8:11:44 AM | HYPE | UP | 3.3 min | -0.355% | — | In play | — |
| 9/28 8:11:28 AM | XRP | UP | 3.5 min | -0.795% | — | In play | — |
| 9/28 8:11:28 AM | BTC | UP | 3.5 min | -0.267% | — | In play | — |
| 9/28 8:10:57 AM | NEAR | UP | 4.0 min | -1.409% | — | In play | — |
| 9/28 8:08:48 AM | SILVER | UP | 6.2 min | — | — | In play | — |
| 9/28 8:08:48 AM | GOLD | UP | 6.2 min | — | — | In play | — |
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
| 9/28 7:58:21 AM | DOGE | UP | 1.6 min | -0.309% | 0¢ | ❌ Lost | -$0.15 |
| 9/28 7:58:05 AM | PALLADIUM | DOWN | 1.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 9/28 7:57:47 AM | PLATINUM | DOWN | 2.2 min | — | 0¢ | ❌ Lost | -$0.15 |
| 9/28 7:57:47 AM | SILVER | DOWN | 2.2 min | — | 1¢ | ❌ Lost | -$0.15 |
| 9/28 7:57:00 AM | HYPE | UP | 3.0 min | -0.488% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 7:44:39 AM | NEAR | DOWN | 20 sec | +0.011% | 0¢ | ❌ Lost | -$0.15 |
| 9/28 7:44:23 AM | SOL | DOWN | 36 sec | +0.064% | 0¢ | ❌ Lost | -$0.15 |
| 9/28 7:44:23 AM | ZEC | UP | 36 sec | -0.253% | 0¢ | ❌ Lost | -$0.15 |
| 9/28 7:43:49 AM | PLATINUM | DOWN | 71 sec | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
