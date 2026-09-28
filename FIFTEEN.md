# 15-Minute 1¢ Study

*Updated Mon Sep 28, 5:06 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (Mean-reversion model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Mean-reversion model ≥ 5%, hold to the close | 37 finished bets | 3% | $9.35 | +201% | +25.27¢ | $11.75 / -$2.40 |

*Expect **37 buys in the first 4 hours** — daily pace shows after 24 hours; max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Mean-reversion model ≥ 2%, hold to the close | 64 | $5.90 | +73% |
| crypto only, hold to the close | 353 | $2.85 | +7% |
| Mean-reversion model ≥ 5%, sell at 50¢ | 37 | $2.10 | +45% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 537 | 531 | 3 (1%) | 1.07% | -$21.30 (-34%) | Hold to the close: -$21.30 (-34%) |

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
| Volatility model | 158 | 3.4% | 0.6% (1) | -286% | ❌ Worse |
| Momentum model | 158 | 4.1% | 0.6% (1) | -426% | ❌ Worse |
| Mean-reversion model | 158 | 5.2% | 0.6% (1) | -234% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 158 | 1 | -16% | -88% | -88% | -84% |
| Volatility model ≥ 2% | 27 | 0 | -100% | -83% | -88% | -79% |
| Volatility model ≥ 5% | 16 | 0 | -100% | -71% | -78% | -64% |
| Volatility model ≥ 10% | 7 | 0 | -100% | -65% | -48% | -13% |
| Momentum model ≥ 2% | 30 | 0 | -100% | -85% | -89% | -81% |
| Momentum model ≥ 5% | 20 | 0 | -100% | -77% | -83% | -71% |
| Momentum model ≥ 10% | 15 | 0 | -100% | -84% | -76% | -61% |
| Mean-reversion model ≥ 2% | 64 | 1 | +73% | -78% | -81% | -76% |
| Mean-reversion model ≥ 5% | 37 | 1 | +201% | -78% | -75% | -58% |
| Mean-reversion model ≥ 10% | 23 | 1 | +391% | -73% | -73% | -54% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 353 | 5% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 162 | 1% | 1% | 1% | 1% | 0% | 0% |
| Financials | 16 | 0% | 0% | 0% | 0% | 0% | 0% |
| **All** | 531 | 3% | 2% | 1% | 1% | 1% | 1% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 3 | 1% | -$21.30 | -34% | — |
| Sell at 2¢ | 18 | 3% | -$58.62 | -93% | 64 sec |
| Sell at 3¢ | 12 | 2% | -$58.62 | -93% | 80 sec |
| Sell at 5¢ | 7 | 1% | -$58.75 | -93% | 2.4 min |
| Sell at 10¢ | 6 | 1% | -$55.44 | -88% | 3.1 min |
| Sell at 25¢ | 4 | 1% | -$50.06 | -79% | 3.5 min |
| Sell at 50¢ | 3 | 1% | -$43.05 | -68% | 4.8 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| 5–10 min | 13 | 2 | 23% | 15% | +1336% | -60% | -40% |
| 2–5 min | 182 | 1 | 7% | 2% | -45% | -88% | -89% |
| 1–2 min | 162 | 0 | 1% | 1% | -100% | -97% | -98% |
| Under 1 min | 174 | 0 | 1% | 1% | -100% | -98% | -98% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| XRP | 41 | 2 | 5% | 5% | +483% | -89% | -84% |
| ZEC | 41 | 0 | 7% | 0% | -100% | -83% | -100% |
| NEAR | 40 | 0 | 0% | 0% | -100% | -100% | -100% |
| ETH | 40 | 1 | 2% | 2% | +233% | -94% | -91% |
| DOGE | 40 | 0 | 5% | 0% | -100% | -89% | -84% |
| SOL | 40 | 0 | 5% | 2% | -100% | -88% | -81% |
| BTC | 39 | 0 | 13% | 5% | -100% | -69% | -72% |
| BNB | 38 | 0 | 3% | 0% | -100% | -94% | -91% |
| HYPE | 34 | 0 | 0% | 0% | -100% | -100% | -100% |
| WTI | 28 | 0 | 4% | 0% | -100% | -93% | -100% |
| GOLD | 27 | 0 | 0% | 0% | -100% | -100% | -100% |
| SILVER | 26 | 0 | 0% | 0% | -100% | -100% | -100% |
| NATGAS | 23 | 0 | 4% | 4% | -100% | -92% | -89% |
| COPPER | 21 | 0 | 0% | 0% | -100% | -100% | -100% |
| PLATINUM | 20 | 0 | 0% | 0% | -100% | -100% | -100% |
| PALLADIUM | 17 | 0 | 0% | 0% | -100% | -100% | -100% |
| GBPUSD | 7 | 0 | 0% | 0% | -100% | -100% | -100% |
| USDJPY | 5 | 0 | 0% | 0% | -100% | -100% | -100% |
| EURUSD | 4 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 297 | 3 | 4% | 2% | +23% | -92% | -90% |
| DOWN (bought NO) | 234 | 0 | 3% | 1% | -100% | -94% | -96% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 28 | 0 | 4% | 4% | -100% | -86% | -78% |
| 0.05–0.1% | 36 | 0 | 3% | 0% | -100% | -92% | -100% |
| 0.1–0.2% | 89 | 0 | 3% | 0% | -100% | -91% | -91% |
| 0.2–0.5% | 159 | 1 | 4% | 2% | -32% | -92% | -92% |
| Over 0.5% | 41 | 2 | 12% | 5% | +449% | -75% | -69% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 255 | 1 | 4% | 2% | -54% | -92% | -94% |
| Evening (6pm–12am) | 276 | 2 | 3% | 1% | -16% | -93% | -92% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 23 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,365 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 45 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 9/28 4:59:55 AM | ETH | DOWN | 5 sec | -0.013% | 0¢ | ❌ Lost | $0.00 |
| 9/28 4:59:55 AM | SILVER | UP | 5 sec | — | 0¢ | ❌ Lost | $0.00 |
| 9/28 4:59:23 AM | ZEC | UP | 37 sec | -0.172% | 0¢ | ❌ Lost | $0.00 |
| 9/28 4:59:23 AM | NATGAS | UP | 37 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/28 4:59:23 AM | XRP | UP | 37 sec | -0.154% | 0¢ | ❌ Lost | $0.00 |
| 9/28 4:59:23 AM | NEAR | UP | 37 sec | -0.117% | 0¢ | ❌ Lost | -$0.15 |
| 9/28 4:59:23 AM | SOL | UP | 37 sec | -0.104% | 0¢ | ❌ Lost | $0.00 |
| 9/28 4:59:23 AM | BTC | DOWN | 37 sec | +0.001% | 6¢ | ❌ Lost | -$0.15 |
| 9/28 4:58:50 AM | COPPER | DOWN | 69 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/28 4:58:01 AM | DOGE | UP | 2.0 min | -0.280% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 4:58:01 AM | HYPE | UP | 2.0 min | -0.245% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 4:58:01 AM | BNB | UP | 2.0 min | -0.143% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 4:44:24 AM | GOLD | UP | 35 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 9/28 4:41:59 AM | BNB | DOWN | 3.0 min | +0.159% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 4:41:11 AM | BTC | DOWN | 3.8 min | +0.157% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 4:40:55 AM | ZEC | DOWN | 4.1 min | +0.468% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 4:40:38 AM | NEAR | DOWN | 4.3 min | +0.868% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 4:40:22 AM | HYPE | DOWN | 4.6 min | +0.313% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 4:40:22 AM | ETH | DOWN | 4.6 min | +0.205% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 4:40:22 AM | XRP | DOWN | 4.6 min | +0.559% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 4:39:50 AM | DOGE | DOWN | 5.2 min | +0.499% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 4:39:50 AM | SOL | DOWN | 5.2 min | +0.333% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 4:29:56 AM | GBPUSD | DOWN | 4 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/28 4:29:40 AM | WTI | DOWN | 20 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/28 4:29:24 AM | GOLD | DOWN | 36 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 9/28 4:29:07 AM | SILVER | DOWN | 52 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 9/28 4:29:07 AM | NATGAS | UP | 52 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/28 4:29:07 AM | PLATINUM | DOWN | 52 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/28 4:29:07 AM | XRP | DOWN | 52 sec | +0.101% | 0¢ | ❌ Lost | -$0.15 |
| 9/28 4:28:51 AM | ETH | DOWN | 68 sec | +0.078% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
