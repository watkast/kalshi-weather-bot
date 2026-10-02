# 15-Minute 1¢ Study

*Updated Fri Oct 2, 3:06 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (5+ min left).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| 5+ min left, hold to the close | 171 finished bets | 1% | $2.80 | +11% | +1.64¢ | $15.40 / -$12.60 |

*Expect about **36 buys a day** (~$5.38/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 374 | $2.25 | +6% |
| Momentum model ≥ 5%, sell at 50¢ | 374 | -$5.00 | -13% |
| Volatility model ≥ 5%, sell at 25¢ | 369 | -$9.05 | -23% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 5971 | 5965 | 23 (0%) | 1.07% | -$403.25 (-56%) | Hold to the close: -$403.25 (-56%) |

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
| Volatility model | 3439 | 3.8% | 0.3% (11) | -621% | ❌ Worse |
| Momentum model | 3439 | 3.9% | 0.3% (11) | -662% | ❌ Worse |
| Mean-reversion model | 3439 | 6.8% | 0.3% (11) | -772% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 3439 | 11 | -59% | -85% | -86% | -83% |
| Volatility model ≥ 2% | 736 | 5 | -22% | -65% | -65% | -60% |
| Volatility model ≥ 5% | 369 | 2 | -29% | -42% | -42% | -37% |
| Volatility model ≥ 10% | 212 | 2 | +42% | -5% | -7% | +1% |
| Momentum model ≥ 2% | 647 | 4 | -25% | -63% | -66% | -62% |
| Momentum model ≥ 5% | 374 | 3 | +6% | -48% | -51% | -45% |
| Momentum model ≥ 10% | 250 | 2 | +16% | -28% | -29% | -23% |
| Mean-reversion model ≥ 2% | 1317 | 7 | -42% | -84% | -86% | -81% |
| Mean-reversion model ≥ 5% | 875 | 6 | -25% | -80% | -82% | -75% |
| Mean-reversion model ≥ 10% | 563 | 4 | -19% | -77% | -80% | -74% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 3635 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 1775 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 555 | 4% | 3% | 2% | 2% | 1% | 1% |
| **All** | 5965 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 23 | 0% | -$403.25 | -56% | — |
| Sell at 2¢ | 238 | 4% | -$649.37 | -90% | 44 sec |
| Sell at 3¢ | 149 | 2% | -$653.14 | -90% | 48 sec |
| Sell at 5¢ | 110 | 2% | -$639.75 | -88% | 64 sec |
| Sell at 10¢ | 74 | 1% | -$600.31 | -83% | 81 sec |
| Sell at 25¢ | 39 | 1% | -$554.16 | -76% | 1.6 min |
| Sell at 50¢ | 21 | 0% | -$499.50 | -69% | 1.9 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 3 | 0 | 100% | 67% | -100% | +73% | +160% |
| 5–10 min | 168 | 2 | 12% | 3% | +13% | -79% | -89% |
| 2–5 min | 1943 | 12 | 8% | 3% | -40% | -86% | -87% |
| 1–2 min | 1547 | 6 | 3% | 2% | -58% | -94% | -93% |
| Under 1 min | 2304 | 3 | 1% | 0% | -81% | -92% | -92% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| DOGE | 411 | 2 | 4% | 1% | -36% | -89% | -90% |
| ZEC | 406 | 2 | 5% | 3% | -41% | -88% | -90% |
| BNB | 406 | 0 | 4% | 1% | -100% | -91% | -93% |
| BTC | 405 | 1 | 7% | 3% | -68% | -83% | -88% |
| ETH | 405 | 2 | 6% | 3% | -39% | -86% | -85% |
| HYPE | 404 | 2 | 5% | 3% | -39% | -88% | -86% |
| XRP | 401 | 3 | 1% | 1% | -2% | -64% | -64% |
| SOL | 399 | 0 | 3% | 1% | -100% | -92% | -91% |
| NEAR | 398 | 1 | 6% | 2% | -66% | -85% | -88% |
| GOLD | 304 | 0 | 5% | 1% | -100% | -90% | -92% |
| SILVER | 285 | 0 | 2% | 1% | -100% | -95% | -95% |
| WTI | 267 | 2 | 3% | 1% | -21% | -94% | -96% |
| COPPER | 254 | 0 | 1% | 0% | -100% | -99% | -99% |
| PLATINUM | 226 | 0 | 0% | 0% | -100% | -100% | -100% |
| NATGAS | 223 | 2 | 4% | 2% | -16% | -94% | -92% |
| PALLADIUM | 216 | 1 | 2% | 1% | -57% | -96% | -98% |
| GBPUSD | 195 | 1 | 4% | 2% | -52% | -93% | -93% |
| EURUSD | 195 | 1 | 5% | 3% | -52% | -91% | -89% |
| USDJPY | 165 | 3 | 2% | 2% | +70% | -96% | -94% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 3065 | 14 | 4% | 2% | -47% | -91% | -91% |
| DOWN (bought NO) | 2900 | 9 | 4% | 2% | -65% | -88% | -89% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 440 | 2 | 1% | 1% | -15% | -53% | -53% |
| 0.05–0.1% | 501 | 0 | 3% | 1% | -100% | -89% | -92% |
| 0.1–0.2% | 886 | 2 | 4% | 1% | -70% | -91% | -91% |
| 0.2–0.5% | 1237 | 5 | 6% | 3% | -55% | -87% | -87% |
| Over 0.5% | 570 | 4 | 7% | 3% | -27% | -86% | -88% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 1474 | 5 | 4% | 1% | -61% | -91% | -94% |
| Morning (6am–12pm) | 1640 | 9 | 5% | 3% | -38% | -90% | -88% |
| Afternoon (12–6pm) | 1201 | 3 | 4% | 1% | -71% | -83% | -85% |
| Evening (6pm–12am) | 1650 | 6 | 3% | 2% | -58% | -93% | -93% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 25 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 3,084 |
| Time from buy to best bounce (bounced bets) | 49 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/2 2:59:51 PM | EURUSD | DOWN | 8 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/2 2:59:51 PM | ETH | UP | 8 sec | -0.048% | 0¢ | ❌ Lost | $0.00 |
| 10/2 2:59:35 PM | GOLD | DOWN | 24 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/2 2:59:35 PM | WTI | UP | 24 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/2 2:59:35 PM | SOL | DOWN | 24 sec | +0.016% | 0¢ | ❌ Lost | -$0.15 |
| 10/2 2:59:19 PM | NATGAS | UP | 40 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/2 2:59:19 PM | DOGE | UP | 40 sec | -0.037% | 0¢ | ❌ Lost | $0.00 |
| 10/2 2:59:19 PM | XRP | DOWN | 40 sec | +0.048% | 1¢ | ❌ Lost | -$0.15 |
| 10/2 2:59:03 PM | NEAR | UP | 57 sec | -0.293% | 0¢ | ❌ Lost | $0.00 |
| 10/2 2:58:45 PM | ZEC | UP | 75 sec | -0.353% | 0¢ | ❌ Lost | -$0.15 |
| 10/2 2:57:58 PM | BNB | UP | 2.0 min | -0.094% | 9¢ | ❌ Lost | -$0.15 |
| 10/2 2:57:40 PM | HYPE | DOWN | 2.3 min | +0.241% | 0¢ | ❌ Lost | -$0.15 |
| 10/2 2:57:24 PM | BTC | DOWN | 2.6 min | +0.167% | 1¢ | ❌ Lost | -$0.15 |
| 10/2 2:44:51 PM | PALLADIUM | UP | 8 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/2 2:44:35 PM | PLATINUM | UP | 24 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/2 2:44:03 PM | USDJPY | DOWN | 56 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/2 2:43:44 PM | BTC | UP | 75 sec | -0.155% | 1¢ | ❌ Lost | -$0.15 |
| 10/2 2:43:44 PM | XRP | UP | 75 sec | -0.190% | 0¢ | ❌ Lost | -$0.15 |
| 10/2 2:43:28 PM | COPPER | UP | 1.5 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/2 2:43:12 PM | GOLD | UP | 1.8 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/2 2:43:12 PM | DOGE | UP | 1.8 min | -0.281% | 1¢ | ❌ Lost | -$0.15 |
| 10/2 2:43:12 PM | ZEC | UP | 1.8 min | -0.293% | 1¢ | ❌ Lost | -$0.15 |
| 10/2 2:43:12 PM | ETH | UP | 1.8 min | -0.151% | 1¢ | ❌ Lost | -$0.15 |
| 10/2 2:42:58 PM | BNB | UP | 2.0 min | -0.172% | 0¢ | ❌ Lost | $0.00 |
| 10/2 2:42:58 PM | HYPE | UP | 2.0 min | -0.317% | 0¢ | ❌ Lost | -$0.15 |
| 10/2 2:42:58 PM | GBPUSD | UP | 2.0 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/2 2:42:58 PM | SOL | UP | 2.0 min | -0.225% | 1¢ | ❌ Lost | -$0.15 |
| 10/2 2:41:20 PM | EURUSD | UP | 3.7 min | — | 6¢ | ❌ Lost | -$0.15 |
| 10/2 2:40:17 PM | SILVER | UP | 4.7 min | — | 3¢ | ❌ Lost | -$0.15 |
| 10/2 2:29:47 PM | BNB | DOWN | 13 sec | -0.020% | 0¢ | ❌ Lost | $0.00 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
