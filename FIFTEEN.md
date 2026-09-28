# 15-Minute 1¢ Study

*Updated Mon Sep 28, 4:01 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Mean-reversion model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Mean-reversion model ≥ 5%, hold to the close | 133 finished bets | 2% | $24.90 | +146% | +18.72¢ | $5.45 / $19.45 |

*Expect **133 buys in the first 15 hours** — daily pace shows after 24 hours; max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| 5+ min left, hold to the close | 45 | $21.25 | +315% |
| Mean-reversion model ≥ 2%, hold to the close | 210 | $15.15 | +56% |
| 2–5 min left, hold to the close | 387 | $14.65 | +26% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 1147 | 1141 | 7 (1%) | 1.07% | -$40.00 (-29%) | Hold to the close: -$40.00 (-29%) |

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
| Volatility model | 532 | 3.1% | 0.8% (4) | -316% | ❌ Worse |
| Momentum model | 532 | 3.3% | 0.8% (4) | -393% | ❌ Worse |
| Mean-reversion model | 532 | 6.2% | 0.8% (4) | -344% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 532 | 4 | -4% | -90% | -91% | -88% |
| Volatility model ≥ 2% | 102 | 1 | +15% | -85% | -84% | -79% |
| Volatility model ≥ 5% | 51 | 0 | -100% | -73% | -73% | -66% |
| Volatility model ≥ 10% | 26 | 0 | -100% | -69% | -69% | -49% |
| Momentum model ≥ 2% | 89 | 0 | -100% | -85% | -89% | -87% |
| Momentum model ≥ 5% | 51 | 0 | -100% | -77% | -86% | -77% |
| Momentum model ≥ 10% | 34 | 0 | -100% | -84% | -76% | -61% |
| Mean-reversion model ≥ 2% | 210 | 3 | +56% | -85% | -87% | -83% |
| Mean-reversion model ≥ 5% | 133 | 3 | +146% | -82% | -82% | -73% |
| Mean-reversion model ≥ 10% | 84 | 2 | +171% | -77% | -77% | -69% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 727 | 4% | 3% | 2% | 2% | 1% | 1% |
| Commodities | 357 | 1% | 1% | 0% | 0% | 0% | 0% |
| Financials | 57 | 2% | 2% | 2% | 2% | 2% | 2% |
| **All** | 1141 | 3% | 2% | 1% | 1% | 1% | 1% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 7 | 1% | -$40.00 | -29% | — |
| Sell at 2¢ | 36 | 3% | -$128.64 | -93% | 62 sec |
| Sell at 3¢ | 22 | 2% | -$129.42 | -94% | 65 sec |
| Sell at 5¢ | 15 | 1% | -$128.25 | -93% | 81 sec |
| Sell at 10¢ | 14 | 1% | -$119.66 | -87% | 1.8 min |
| Sell at 25¢ | 10 | 1% | -$104.90 | -76% | 2.1 min |
| Sell at 50¢ | 7 | 1% | -$90.75 | -66% | 2.4 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| 5–10 min | 45 | 2 | 7% | 4% | +315% | -88% | -83% |
| 2–5 min | 387 | 5 | 6% | 3% | +26% | -88% | -90% |
| 1–2 min | 342 | 0 | 2% | 0% | -100% | -96% | -97% |
| Under 1 min | 367 | 0 | 1% | 1% | -100% | -98% | -98% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ETH | 83 | 2 | 5% | 2% | +196% | -89% | -88% |
| DOGE | 83 | 1 | 5% | 2% | +39% | -90% | -84% |
| ZEC | 82 | 1 | 5% | 1% | +53% | -89% | -96% |
| NEAR | 81 | 0 | 1% | 0% | -100% | -97% | -100% |
| BTC | 81 | 0 | 9% | 2% | -100% | -78% | -86% |
| XRP | 81 | 2 | 5% | 4% | +206% | -89% | -87% |
| SOL | 80 | 0 | 4% | 2% | -100% | -90% | -86% |
| BNB | 80 | 0 | 1% | 0% | -100% | -97% | -96% |
| HYPE | 76 | 0 | 3% | 1% | -100% | -94% | -96% |
| GOLD | 63 | 0 | 3% | 0% | -100% | -93% | -100% |
| WTI | 59 | 0 | 2% | 0% | -100% | -97% | -100% |
| SILVER | 58 | 0 | 0% | 0% | -100% | -100% | -100% |
| NATGAS | 49 | 0 | 4% | 2% | -100% | -93% | -89% |
| COPPER | 47 | 0 | 0% | 0% | -100% | -100% | -100% |
| PLATINUM | 44 | 0 | 0% | 0% | -100% | -100% | -100% |
| PALLADIUM | 37 | 0 | 0% | 0% | -100% | -100% | -100% |
| GBPUSD | 23 | 0 | 0% | 0% | -100% | -100% | -100% |
| EURUSD | 19 | 0 | 0% | 0% | -100% | -100% | -100% |
| USDJPY | 15 | 1 | 7% | 7% | +522% | -88% | -83% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 626 | 5 | 3% | 1% | -6% | -93% | -93% |
| DOWN (bought NO) | 515 | 2 | 3% | 1% | -56% | -93% | -94% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 67 | 0 | 4% | 3% | -100% | -83% | -83% |
| 0.05–0.1% | 69 | 0 | 1% | 0% | -100% | -96% | -100% |
| 0.1–0.2% | 159 | 0 | 3% | 0% | -100% | -91% | -92% |
| 0.2–0.5% | 297 | 2 | 4% | 2% | -26% | -92% | -93% |
| Over 0.5% | 135 | 4 | 7% | 4% | +225% | -86% | -84% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 308 | 1 | 4% | 2% | -62% | -91% | -93% |
| Morning (6am–12pm) | 338 | 4 | 3% | 1% | +36% | -94% | -94% |
| Afternoon (12–6pm) | 219 | 0 | 2% | 1% | -100% | -95% | -97% |
| Evening (6pm–12am) | 276 | 2 | 3% | 1% | -16% | -93% | -92% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 23 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 3,838 |
| Time from buy to best bounce (bounced bets) | 47 sec |
| Price snapshots per bet | 48 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 9/28 3:59:47 PM | SILVER | UP | 13 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/28 3:59:32 PM | ZEC | DOWN | 27 sec | +0.127% | 0¢ | ❌ Lost | $0.00 |
| 9/28 3:58:44 PM | NEAR | UP | 76 sec | -0.372% | 0¢ | ❌ Lost | -$0.15 |
| 9/28 3:58:44 PM | XRP | UP | 76 sec | -0.215% | 1¢ | ❌ Lost | $0.00 |
| 9/28 3:58:13 PM | HYPE | UP | 1.8 min | -0.145% | 0¢ | ❌ Lost | -$0.15 |
| 9/28 3:57:57 PM | DOGE | UP | 2.0 min | -0.278% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 3:57:41 PM | SOL | UP | 2.3 min | -0.300% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 3:56:54 PM | BNB | UP | 3.1 min | -0.122% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 3:56:07 PM | BTC | UP | 3.9 min | -0.183% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 3:55:51 PM | ETH | UP | 4.1 min | -0.244% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 3:44:57 PM | EURUSD | DOWN | 2 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/28 3:44:40 PM | NATGAS | UP | 19 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/28 3:44:40 PM | NEAR | UP | 19 sec | -0.089% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 3:43:52 PM | ETH | UP | 67 sec | -0.032% | 2¢ | ❌ Lost | -$0.15 |
| 9/28 3:43:52 PM | BTC | UP | 67 sec | -0.042% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 3:43:19 PM | HYPE | UP | 1.7 min | -0.245% | 0¢ | ❌ Lost | -$0.15 |
| 9/28 3:43:19 PM | SOL | UP | 1.7 min | -0.168% | 0¢ | ❌ Lost | -$0.15 |
| 9/28 3:43:03 PM | XRP | UP | 1.9 min | -0.301% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 3:42:47 PM | WTI | DOWN | 2.2 min | — | 0¢ | ❌ Lost | -$0.15 |
| 9/28 3:42:31 PM | DOGE | UP | 2.5 min | -0.299% | 0¢ | ❌ Lost | -$0.15 |
| 9/28 3:42:15 PM | ZEC | DOWN | 2.8 min | +0.590% | 0¢ | ❌ Lost | -$0.15 |
| 9/28 3:41:59 PM | BNB | UP | 3.0 min | -0.160% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 3:29:51 PM | SILVER | UP | 8 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/28 3:29:05 PM | NEAR | UP | 55 sec | -0.346% | 0¢ | ❌ Lost | -$0.15 |
| 9/28 3:28:49 PM | NATGAS | DOWN | 71 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/28 3:28:34 PM | ZEC | UP | 86 sec | -0.475% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 3:28:18 PM | COPPER | UP | 1.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 9/28 3:27:15 PM | XRP | UP | 2.7 min | -0.321% | 14¢ | ❌ Lost | -$0.15 |
| 9/28 3:27:15 PM | DOGE | UP | 2.7 min | -0.427% | 0¢ | ❌ Lost | $0.00 |
| 9/28 3:26:59 PM | HYPE | UP | 3.0 min | -0.404% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
