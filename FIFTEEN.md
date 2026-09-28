# 15-Minute 1¢ Study

*Updated Mon Sep 28, 10:24 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade small.** Profitable in both halves of the data; sample still modest.

1. **Watch** every 15-minute up/down market (Mean-reversion model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Mean-reversion model ≥ 5%, hold to the close | 91 finished bets | 2% | $16.45 | +142% | +18.08¢ | $8.30 / $8.15 |

*Expect **91 buys in the first 10 hours** — daily pace shows after 24 hours; max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Mean-reversion model ≥ 2%, hold to the close | 141 | $10.15 | +57% |
| Volatility model ≥ 2%, hold to the close | 69 | $5.75 | +70% |
| Mean-reversion model ≥ 5%, sell at 50¢ | 91 | $1.95 | +17% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 841 | 834 | 4 (0%) | 1.07% | -$43.15 (-44%) | Hold to the close: -$43.15 (-44%) |

*In play or awaiting result: 7. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 344 | 3.8% | 0.6% (2) | -505% | ❌ Worse |
| Momentum model | 344 | 4.0% | 0.6% (2) | -613% | ❌ Worse |
| Mean-reversion model | 344 | 6.9% | 0.6% (2) | -529% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 344 | 2 | -23% | -89% | -90% | -87% |
| Volatility model ≥ 2% | 69 | 1 | +70% | -84% | -81% | -76% |
| Volatility model ≥ 5% | 35 | 0 | -100% | -74% | -71% | -68% |
| Volatility model ≥ 10% | 20 | 0 | -100% | -88% | -81% | -69% |
| Momentum model ≥ 2% | 62 | 0 | -100% | -86% | -89% | -91% |
| Momentum model ≥ 5% | 37 | 0 | -100% | -81% | -90% | -84% |
| Momentum model ≥ 10% | 25 | 0 | -100% | -90% | -85% | -75% |
| Mean-reversion model ≥ 2% | 141 | 2 | +57% | -84% | -85% | -82% |
| Mean-reversion model ≥ 5% | 91 | 2 | +142% | -82% | -80% | -72% |
| Mean-reversion model ≥ 10% | 60 | 2 | +273% | -76% | -74% | -65% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 539 | 4% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 260 | 2% | 1% | 0% | 0% | 0% | 0% |
| Financials | 35 | 0% | 0% | 0% | 0% | 0% | 0% |
| **All** | 834 | 3% | 2% | 1% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 4 | 0% | -$43.15 | -44% | — |
| Sell at 2¢ | 28 | 3% | -$91.87 | -93% | 62 sec |
| Sell at 3¢ | 17 | 2% | -$92.52 | -93% | 67 sec |
| Sell at 5¢ | 10 | 1% | -$92.65 | -93% | 1.9 min |
| Sell at 10¢ | 9 | 1% | -$87.36 | -88% | 2.4 min |
| Sell at 25¢ | 6 | 1% | -$79.29 | -80% | 2.8 min |
| Sell at 50¢ | 4 | 0% | -$72.15 | -73% | 4.7 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| 5–10 min | 25 | 2 | 12% | 8% | +647% | -79% | -69% |
| 2–5 min | 278 | 2 | 7% | 2% | -29% | -87% | -90% |
| 1–2 min | 262 | 0 | 2% | 0% | -100% | -96% | -96% |
| Under 1 min | 269 | 0 | 0% | 0% | -100% | -99% | -98% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ETH | 62 | 2 | 5% | 3% | +324% | -88% | -82% |
| DOGE | 61 | 0 | 5% | 2% | -100% | -89% | -84% |
| XRP | 61 | 2 | 5% | 3% | +297% | -89% | -89% |
| ZEC | 61 | 0 | 5% | 0% | -100% | -89% | -100% |
| NEAR | 60 | 0 | 2% | 0% | -100% | -96% | -100% |
| BTC | 60 | 0 | 10% | 3% | -100% | -73% | -79% |
| SOL | 60 | 0 | 3% | 2% | -100% | -91% | -87% |
| BNB | 59 | 0 | 2% | 0% | -100% | -96% | -94% |
| HYPE | 55 | 0 | 4% | 2% | -100% | -92% | -94% |
| GOLD | 48 | 0 | 2% | 0% | -100% | -96% | -100% |
| WTI | 43 | 0 | 2% | 0% | -100% | -95% | -100% |
| SILVER | 41 | 0 | 0% | 0% | -100% | -100% | -100% |
| NATGAS | 36 | 0 | 6% | 3% | -100% | -90% | -86% |
| PLATINUM | 33 | 0 | 0% | 0% | -100% | -100% | -100% |
| COPPER | 32 | 0 | 0% | 0% | -100% | -100% | -100% |
| PALLADIUM | 27 | 0 | 0% | 0% | -100% | -100% | -100% |
| GBPUSD | 15 | 0 | 0% | 0% | -100% | -100% | -100% |
| EURUSD | 13 | 0 | 0% | 0% | -100% | -100% | -100% |
| USDJPY | 7 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 437 | 3 | 3% | 1% | -16% | -92% | -92% |
| DOWN (bought NO) | 397 | 1 | 3% | 1% | -72% | -93% | -94% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 46 | 0 | 2% | 2% | -100% | -91% | -86% |
| 0.05–0.1% | 53 | 0 | 2% | 0% | -100% | -94% | -100% |
| 0.1–0.2% | 128 | 0 | 3% | 0% | -100% | -91% | -90% |
| 0.2–0.5% | 229 | 2 | 5% | 2% | -4% | -90% | -92% |
| Over 0.5% | 83 | 2 | 8% | 4% | +171% | -82% | -81% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 308 | 1 | 4% | 2% | -62% | -91% | -93% |
| Morning (6am–12pm) | 250 | 1 | 3% | 1% | -53% | -94% | -96% |
| Evening (6pm–12am) | 276 | 2 | 3% | 1% | -16% | -93% | -92% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 23 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 3,660 |
| Time from buy to best bounce (bounced bets) | 47 sec |
| Price snapshots per bet | 45 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 9/28 10:20:44 AM | SILVER | DOWN | 9.3 min | — | — | In play | — |
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
| 9/28 9:59:34 AM | PLATINUM | DOWN | 25 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/28 9:59:18 AM | NEAR | DOWN | 42 sec | +0.151% | 0¢ | ❌ Lost | $0.00 |
| 9/28 9:59:18 AM | PALLADIUM | DOWN | 42 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/28 9:59:18 AM | GOLD | DOWN | 42 sec | — | 0¢ | ❌ Lost | $0.00 |
| 9/28 9:59:18 AM | SILVER | DOWN | 42 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/28 9:58:45 AM | ZEC | DOWN | 74 sec | +0.368% | 0¢ | ❌ Lost | -$0.15 |
| 9/28 9:58:45 AM | ETH | DOWN | 74 sec | +0.124% | 0¢ | ❌ Lost | $0.00 |
| 9/28 9:58:29 AM | NATGAS | UP | 1.5 min | — | 0¢ | ❌ Lost | -$0.15 |
| 9/28 9:58:29 AM | XRP | DOWN | 1.5 min | +0.215% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 9:58:13 AM | DOGE | DOWN | 1.8 min | +0.320% | 0¢ | ❌ Lost | -$0.15 |
| 9/28 9:57:55 AM | BNB | DOWN | 2.1 min | +0.133% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 9:57:39 AM | BTC | DOWN | 2.4 min | +0.205% | 0¢ | ❌ Lost | $0.00 |
| 9/28 9:57:39 AM | SOL | DOWN | 2.4 min | +0.347% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 9:57:08 AM | WTI | UP | 2.9 min | — | 1¢ | ❌ Lost | -$0.15 |
| 9/28 9:57:08 AM | HYPE | DOWN | 2.9 min | +0.442% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
