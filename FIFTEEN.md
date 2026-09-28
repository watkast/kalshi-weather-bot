# 15-Minute 1¢ Study

*Updated Mon Sep 28, 1:49 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Mean-reversion model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Mean-reversion model ≥ 5%, hold to the close | 113 finished bets | 3% | $27.45 | +189% | +24.29¢ | $6.80 / $20.65 |

*Expect **113 buys in the first 13 hours** — daily pace shows after 24 hours; max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| 5+ min left, hold to the close | 42 | $21.70 | +344% |
| 2–5 min left, hold to the close | 353 | $19.60 | +39% |
| Mean-reversion model ≥ 2%, hold to the close | 176 | $19.50 | +87% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 1027 | 1021 | 7 (1%) | 1.07% | -$25.00 (-20%) | Hold to the close: -$25.00 (-20%) |

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
| Volatility model | 454 | 3.1% | 0.9% (4) | -283% | ❌ Worse |
| Momentum model | 454 | 3.3% | 0.9% (4) | -363% | ❌ Worse |
| Mean-reversion model | 454 | 6.0% | 0.9% (4) | -292% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 454 | 4 | +13% | -90% | -91% | -88% |
| Volatility model ≥ 2% | 83 | 1 | +44% | -87% | -84% | -80% |
| Volatility model ≥ 5% | 41 | 0 | -100% | -78% | -75% | -72% |
| Volatility model ≥ 10% | 21 | 0 | -100% | -88% | -81% | -69% |
| Momentum model ≥ 2% | 74 | 0 | -100% | -88% | -91% | -92% |
| Momentum model ≥ 5% | 42 | 0 | -100% | -83% | -91% | -86% |
| Momentum model ≥ 10% | 29 | 0 | -100% | -91% | -86% | -77% |
| Mean-reversion model ≥ 2% | 176 | 3 | +87% | -85% | -86% | -83% |
| Mean-reversion model ≥ 5% | 113 | 3 | +189% | -82% | -81% | -73% |
| Mean-reversion model ≥ 10% | 72 | 2 | +211% | -80% | -78% | -71% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 649 | 4% | 3% | 2% | 2% | 1% | 1% |
| Commodities | 323 | 1% | 1% | 0% | 0% | 0% | 0% |
| Financials | 49 | 2% | 2% | 2% | 2% | 2% | 2% |
| **All** | 1021 | 3% | 2% | 1% | 1% | 1% | 1% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 7 | 1% | -$25.00 | -20% | — |
| Sell at 2¢ | 32 | 3% | -$114.68 | -93% | 62 sec |
| Sell at 3¢ | 20 | 2% | -$115.20 | -94% | 72 sec |
| Sell at 5¢ | 13 | 1% | -$114.55 | -93% | 1.6 min |
| Sell at 10¢ | 12 | 1% | -$107.28 | -87% | 2.0 min |
| Sell at 25¢ | 9 | 1% | -$93.21 | -76% | 2.1 min |
| Sell at 50¢ | 7 | 1% | -$75.75 | -62% | 2.4 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| 5–10 min | 42 | 2 | 7% | 5% | +344% | -88% | -81% |
| 2–5 min | 353 | 5 | 7% | 3% | +39% | -88% | -90% |
| 1–2 min | 312 | 0 | 2% | 0% | -100% | -97% | -97% |
| Under 1 min | 314 | 0 | 0% | 0% | -100% | -99% | -99% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ETH | 74 | 2 | 4% | 3% | +246% | -90% | -86% |
| DOGE | 74 | 1 | 5% | 3% | +53% | -89% | -83% |
| ZEC | 74 | 1 | 5% | 1% | +70% | -87% | -95% |
| XRP | 73 | 2 | 4% | 3% | +233% | -91% | -91% |
| NEAR | 72 | 0 | 1% | 0% | -100% | -96% | -100% |
| BTC | 72 | 0 | 10% | 3% | -100% | -74% | -83% |
| SOL | 72 | 0 | 3% | 1% | -100% | -93% | -89% |
| BNB | 71 | 0 | 1% | 0% | -100% | -97% | -96% |
| HYPE | 67 | 0 | 3% | 1% | -100% | -93% | -95% |
| GOLD | 58 | 0 | 2% | 0% | -100% | -96% | -100% |
| WTI | 54 | 0 | 2% | 0% | -100% | -96% | -100% |
| SILVER | 51 | 0 | 0% | 0% | -100% | -100% | -100% |
| NATGAS | 45 | 0 | 4% | 2% | -100% | -92% | -88% |
| COPPER | 41 | 0 | 0% | 0% | -100% | -100% | -100% |
| PLATINUM | 40 | 0 | 0% | 0% | -100% | -100% | -100% |
| PALLADIUM | 34 | 0 | 0% | 0% | -100% | -100% | -100% |
| GBPUSD | 20 | 0 | 0% | 0% | -100% | -100% | -100% |
| EURUSD | 17 | 0 | 0% | 0% | -100% | -100% | -100% |
| USDJPY | 12 | 1 | 8% | 8% | +678% | -86% | -78% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 550 | 5 | 3% | 1% | +8% | -93% | -93% |
| DOWN (bought NO) | 471 | 2 | 3% | 1% | -52% | -93% | -95% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 50 | 0 | 2% | 2% | -100% | -91% | -87% |
| 0.05–0.1% | 62 | 0 | 2% | 0% | -100% | -95% | -100% |
| 0.1–0.2% | 143 | 0 | 3% | 0% | -100% | -90% | -91% |
| 0.2–0.5% | 267 | 2 | 4% | 2% | -19% | -92% | -93% |
| Over 0.5% | 127 | 4 | 7% | 4% | +249% | -85% | -83% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 308 | 1 | 4% | 2% | -62% | -91% | -93% |
| Morning (6am–12pm) | 338 | 4 | 3% | 1% | +36% | -94% | -94% |
| Afternoon (12–6pm) | 99 | 0 | 1% | 0% | -100% | -98% | -100% |
| Evening (6pm–12am) | 276 | 2 | 3% | 1% | -16% | -93% | -92% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 23 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 3,838 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 49 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 9/28 1:44:33 PM | EURUSD | UP | 26 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/28 1:44:17 PM | WTI | UP | 42 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 9/28 1:44:01 PM | PLATINUM | UP | 58 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/28 1:43:45 PM | HYPE | UP | 75 sec | -0.247% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 1:43:14 PM | COPPER | UP | 1.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 9/28 1:42:58 PM | NATGAS | UP | 2.0 min | — | 0¢ | ❌ Lost | -$0.15 |
| 9/28 1:42:58 PM | GOLD | UP | 2.0 min | — | 1¢ | ❌ Lost | -$0.15 |
| 9/28 1:42:25 PM | ZEC | UP | 2.6 min | -0.813% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 1:42:25 PM | SILVER | UP | 2.6 min | — | 1¢ | ❌ Lost | -$0.15 |
| 9/28 1:40:50 PM | SOL | UP | 4.2 min | -0.651% | 0¢ | ❌ Lost | -$0.15 |
| 9/28 1:40:34 PM | XRP | UP | 4.4 min | -0.957% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 1:39:46 PM | DOGE | UP | 5.2 min | -0.790% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 1:39:46 PM | BTC | UP | 5.2 min | -0.537% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 1:39:30 PM | ETH | UP | 5.5 min | -0.508% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 1:38:59 PM | NEAR | UP | 6.0 min | -2.564% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 1:38:59 PM | BNB | UP | 6.0 min | -0.487% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 1:29:49 PM | NEAR | DOWN | 10 sec | +0.043% | 0¢ | ❌ Lost | $0.00 |
| 9/28 1:29:34 PM | USDJPY | UP | 25 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/28 1:29:18 PM | XRP | UP | 41 sec | -0.287% | 0¢ | ❌ Lost | $0.00 |
| 9/28 1:29:02 PM | HYPE | UP | 57 sec | -0.197% | 0¢ | ❌ Lost | -$0.15 |
| 9/28 1:29:02 PM | BTC | UP | 57 sec | -0.077% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 1:28:46 PM | SILVER | DOWN | 73 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 9/28 1:28:31 PM | WTI | DOWN | 88 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 9/28 1:28:15 PM | NATGAS | DOWN | 1.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 9/28 1:28:15 PM | DOGE | UP | 1.7 min | -0.244% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 1:28:15 PM | ETH | UP | 1.7 min | -0.137% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 1:28:15 PM | SOL | UP | 1.7 min | -0.203% | 0¢ | ❌ Lost | $0.00 |
| 9/28 1:27:59 PM | BNB | UP | 2.0 min | -0.122% | 0¢ | ❌ Lost | -$0.15 |
| 9/28 1:27:28 PM | ZEC | UP | 2.5 min | -0.815% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 1:27:12 PM | GBPUSD | DOWN | 2.8 min | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
