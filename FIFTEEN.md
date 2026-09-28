# 15-Minute 1¢ Study

*Updated Mon Sep 28, 5:57 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (Mean-reversion model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Mean-reversion model ≥ 5%, hold to the close | 45 finished bets | 2% | $8.30 | +146% | +18.44¢ | $11.30 / -$3.00 |

*Expect **45 buys in the first 5 hours** — daily pace shows after 24 hours; max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Mean-reversion model ≥ 2%, hold to the close | 76 | $4.25 | +44% |
| Mean-reversion model ≥ 5%, sell at 50¢ | 45 | $1.05 | +18% |
| crypto only, hold to the close | 380 | -$0.30 | -1% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 580 | 572 | 3 (1%) | 1.07% | -$26.40 (-39%) | Hold to the close: -$26.40 (-39%) |

*In play or awaiting result: 8. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 185 | 3.6% | 0.5% (1) | -419% | ❌ Worse |
| Momentum model | 185 | 4.3% | 0.5% (1) | -553% | ❌ Worse |
| Mean-reversion model | 185 | 5.6% | 0.5% (1) | -382% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 185 | 1 | -29% | -88% | -90% | -87% |
| Volatility model ≥ 2% | 34 | 0 | -100% | -87% | -90% | -84% |
| Volatility model ≥ 5% | 18 | 0 | -100% | -73% | -80% | -67% |
| Volatility model ≥ 10% | 9 | 0 | -100% | -71% | -57% | -28% |
| Momentum model ≥ 2% | 34 | 0 | -100% | -87% | -90% | -83% |
| Momentum model ≥ 5% | 24 | 0 | -100% | -81% | -86% | -76% |
| Momentum model ≥ 10% | 17 | 0 | -100% | -86% | -78% | -64% |
| Mean-reversion model ≥ 2% | 76 | 1 | +44% | -81% | -84% | -80% |
| Mean-reversion model ≥ 5% | 45 | 1 | +146% | -82% | -79% | -66% |
| Mean-reversion model ≥ 10% | 28 | 1 | +306% | -77% | -77% | -62% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 380 | 4% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 173 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 19 | 0% | 0% | 0% | 0% | 0% | 0% |
| **All** | 572 | 3% | 2% | 1% | 1% | 1% | 1% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 3 | 1% | -$26.40 | -39% | — |
| Sell at 2¢ | 20 | 3% | -$63.20 | -92% | 64 sec |
| Sell at 3¢ | 13 | 2% | -$63.33 | -93% | 67 sec |
| Sell at 5¢ | 7 | 1% | -$63.85 | -93% | 2.4 min |
| Sell at 10¢ | 6 | 1% | -$60.54 | -89% | 3.1 min |
| Sell at 25¢ | 4 | 1% | -$55.16 | -81% | 3.5 min |
| Sell at 50¢ | 3 | 1% | -$48.15 | -70% | 4.8 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| 5–10 min | 14 | 2 | 21% | 14% | +1233% | -63% | -44% |
| 2–5 min | 198 | 1 | 7% | 2% | -50% | -88% | -90% |
| 1–2 min | 175 | 0 | 2% | 1% | -100% | -96% | -96% |
| Under 1 min | 185 | 0 | 1% | 1% | -100% | -98% | -98% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| XRP | 44 | 2 | 7% | 5% | +433% | -85% | -85% |
| ZEC | 44 | 0 | 7% | 0% | -100% | -85% | -100% |
| NEAR | 43 | 0 | 0% | 0% | -100% | -100% | -100% |
| ETH | 43 | 1 | 2% | 2% | +211% | -94% | -91% |
| DOGE | 43 | 0 | 5% | 0% | -100% | -90% | -86% |
| SOL | 43 | 0 | 5% | 2% | -100% | -88% | -83% |
| BTC | 42 | 0 | 12% | 5% | -100% | -70% | -73% |
| BNB | 41 | 0 | 2% | 0% | -100% | -94% | -92% |
| HYPE | 37 | 0 | 0% | 0% | -100% | -100% | -100% |
| WTI | 30 | 0 | 3% | 0% | -100% | -94% | -100% |
| GOLD | 30 | 0 | 0% | 0% | -100% | -100% | -100% |
| SILVER | 27 | 0 | 0% | 0% | -100% | -100% | -100% |
| NATGAS | 26 | 0 | 8% | 4% | -100% | -87% | -80% |
| COPPER | 22 | 0 | 0% | 0% | -100% | -100% | -100% |
| PLATINUM | 21 | 0 | 0% | 0% | -100% | -100% | -100% |
| PALLADIUM | 17 | 0 | 0% | 0% | -100% | -100% | -100% |
| GBPUSD | 8 | 0 | 0% | 0% | -100% | -100% | -100% |
| EURUSD | 6 | 0 | 0% | 0% | -100% | -100% | -100% |
| USDJPY | 5 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 307 | 3 | 4% | 2% | +19% | -91% | -90% |
| DOWN (bought NO) | 265 | 0 | 3% | 1% | -100% | -94% | -95% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 34 | 0 | 3% | 3% | -100% | -88% | -81% |
| 0.05–0.1% | 39 | 0 | 3% | 0% | -100% | -92% | -100% |
| 0.1–0.2% | 98 | 0 | 3% | 0% | -100% | -92% | -92% |
| 0.2–0.5% | 166 | 1 | 4% | 2% | -35% | -92% | -93% |
| Over 0.5% | 43 | 2 | 12% | 5% | +433% | -75% | -70% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 296 | 1 | 4% | 1% | -60% | -92% | -93% |
| Evening (6pm–12am) | 276 | 2 | 3% | 1% | -16% | -93% | -92% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 23 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,168 |
| Time from buy to best bounce (bounced bets) | 47 sec |
| Price snapshots per bet | 45 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 9/28 5:55:38 AM | DOGE | UP | 4.4 min | -0.320% | — | In play | — |
| 9/28 5:53:45 AM | HYPE | UP | 6.2 min | -0.690% | — | In play | — |
| 9/28 5:44:57 AM | WTI | UP | 2 sec | — | 0¢ | ❌ Lost | $0.00 |
| 9/28 5:44:25 AM | COPPER | DOWN | 34 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 9/28 5:43:51 AM | ZEC | DOWN | 69 sec | +0.167% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 5:43:51 AM | NATGAS | DOWN | 69 sec | — | 3¢ | ❌ Lost | -$0.15 |
| 9/28 5:43:35 AM | DOGE | DOWN | 85 sec | +0.173% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 5:43:35 AM | SOL | DOWN | 85 sec | +0.094% | 2¢ | ❌ Lost | -$0.15 |
| 9/28 5:43:35 AM | BTC | DOWN | 85 sec | +0.104% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 5:43:19 AM | NEAR | UP | 1.7 min | -0.536% | 1¢ | ❌ Lost | $0.00 |
| 9/28 5:43:19 AM | BNB | DOWN | 1.7 min | +0.046% | 0¢ | ❌ Lost | -$0.15 |
| 9/28 5:43:19 AM | GOLD | UP | 1.7 min | — | 1¢ | ❌ Lost | -$0.15 |
| 9/28 5:43:04 AM | SILVER | UP | 1.9 min | — | 1¢ | ❌ Lost | -$0.15 |
| 9/28 5:42:16 AM | ETH | DOWN | 2.7 min | +0.168% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 5:41:11 AM | XRP | DOWN | 3.8 min | +0.302% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 5:40:38 AM | HYPE | DOWN | 4.3 min | +0.319% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 5:29:53 AM | BNB | DOWN | 6 sec | -0.014% | 0¢ | ❌ Lost | $0.00 |
| 9/28 5:29:37 AM | ZEC | DOWN | 22 sec | +0.151% | 0¢ | ❌ Lost | -$0.15 |
| 9/28 5:29:21 AM | BTC | DOWN | 38 sec | +0.044% | 0¢ | ❌ Lost | $0.00 |
| 9/28 5:29:07 AM | ETH | DOWN | 53 sec | +0.064% | 0¢ | ❌ Lost | $0.00 |
| 9/28 5:29:07 AM | SOL | DOWN | 53 sec | +0.097% | 0¢ | ❌ Lost | -$0.15 |
| 9/28 5:28:49 AM | GOLD | DOWN | 71 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/28 5:28:33 AM | DOGE | DOWN | 87 sec | +0.141% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 5:28:33 AM | NATGAS | DOWN | 87 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/28 5:27:46 AM | XRP | DOWN | 2.2 min | +0.209% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 5:27:30 AM | WTI | UP | 2.5 min | — | 1¢ | ❌ Lost | -$0.15 |
| 9/28 5:25:52 AM | EURUSD | DOWN | 4.1 min | — | 0¢ | ❌ Lost | -$0.15 |
| 9/28 5:25:19 AM | HYPE | DOWN | 4.7 min | +0.276% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 5:25:03 AM | NEAR | DOWN | 4.9 min | +0.859% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 5:14:56 AM | SOL | DOWN | 3 sec | +0.015% | 0¢ | ❌ Lost | $0.00 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
