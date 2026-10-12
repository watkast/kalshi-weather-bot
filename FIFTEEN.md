# 15-Minute 1¢ Study

*Updated Mon Oct 12, 5:20 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 1185 finished bets | 1% | $39.45 | +31% | +3.33¢ | $34.25 / $5.20 |

*Expect about **83 buys a day** (~$12.52/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 1134 | $18.80 | +16% |
| 5+ min left, hold to the close | 424 | -$6.70 | -11% |
| Volatility model ≥ 2%, hold to the close | 2085 | -$12.50 | -5% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 15575 | 15568 | 62 (0%) | 1.07% | -$1,010.60 (-54%) | Hold to the close: -$1,010.60 (-54%) |

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
| Volatility model | 10371 | 4.5% | 0.4% (45) | -668% | ❌ Worse |
| Momentum model | 10371 | 4.5% | 0.4% (45) | -694% | ❌ Worse |
| Mean-reversion model | 10371 | 7.2% | 0.4% (45) | -773% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 10371 | 45 | -46% | -88% | -88% | -86% |
| Volatility model ≥ 2% | 2085 | 17 | -5% | -77% | -77% | -74% |
| Volatility model ≥ 5% | 1185 | 12 | +31% | -72% | -71% | -68% |
| Volatility model ≥ 10% | 748 | 8 | +55% | -62% | -62% | -58% |
| Momentum model ≥ 2% | 1835 | 14 | -7% | -79% | -80% | -78% |
| Momentum model ≥ 5% | 1134 | 10 | +16% | -75% | -76% | -72% |
| Momentum model ≥ 10% | 785 | 7 | +28% | -68% | -68% | -64% |
| Mean-reversion model ≥ 2% | 3630 | 26 | -22% | -85% | -85% | -81% |
| Mean-reversion model ≥ 5% | 2480 | 20 | -10% | -82% | -82% | -78% |
| Mean-reversion model ≥ 10% | 1659 | 14 | -2% | -81% | -81% | -78% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 10569 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 3693 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 1306 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 15568 | 3% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 62 | 0% | -$1,010.60 | -54% | — |
| Sell at 2¢ | 533 | 3% | -$1,698.02 | -90% | 33 sec |
| Sell at 3¢ | 354 | 2% | -$1,698.54 | -90% | 46 sec |
| Sell at 5¢ | 259 | 2% | -$1,668.25 | -89% | 50 sec |
| Sell at 10¢ | 170 | 1% | -$1,585.90 | -84% | 64 sec |
| Sell at 25¢ | 96 | 1% | -$1,462.84 | -78% | 80 sec |
| Sell at 50¢ | 64 | 0% | -$1,306.60 | -70% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 420 | 4 | 11% | 3% | -10% | -81% | -86% |
| 2–5 min | 5012 | 32 | 6% | 3% | -37% | -88% | -88% |
| 1–2 min | 4111 | 16 | 3% | 2% | -58% | -94% | -94% |
| Under 1 min | 6021 | 10 | 1% | 0% | -76% | -91% | -91% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 1186 | 7 | 4% | 3% | -27% | -90% | -90% |
| HYPE | 1185 | 4 | 4% | 2% | -58% | -90% | -89% |
| DOGE | 1177 | 2 | 4% | 2% | -79% | -91% | -90% |
| BNB | 1175 | 5 | 4% | 2% | -48% | -91% | -92% |
| ETH | 1174 | 8 | 5% | 2% | -17% | -89% | -89% |
| SOL | 1174 | 2 | 3% | 1% | -79% | -93% | -92% |
| BTC | 1170 | 5 | 5% | 2% | -43% | -88% | -90% |
| NEAR | 1164 | 7 | 5% | 2% | -21% | -76% | -77% |
| XRP | 1164 | 7 | 2% | 1% | -25% | -84% | -85% |
| GOLD | 605 | 0 | 3% | 1% | -100% | -92% | -94% |
| SILVER | 592 | 1 | 3% | 1% | -81% | -94% | -94% |
| WTI | 568 | 3 | 3% | 1% | -40% | -94% | -96% |
| COPPER | 530 | 0 | 1% | 1% | -100% | -98% | -98% |
| PLATINUM | 489 | 0 | 0% | 0% | -100% | -100% | -99% |
| PALLADIUM | 455 | 1 | 1% | 0% | -79% | -98% | -98% |
| NATGAS | 454 | 3 | 3% | 2% | -38% | -95% | -94% |
| EURUSD | 439 | 3 | 3% | 2% | -36% | -74% | -73% |
| GBPUSD | 420 | 1 | 2% | 1% | -78% | -96% | -96% |
| USDJPY | 380 | 3 | 1% | 1% | -26% | -98% | -97% |
| USDCAD | 35 | 0 | 0% | 0% | -100% | -100% | -100% |
| AUDUSD | 32 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 7829 | 34 | 3% | 2% | -50% | -90% | -89% |
| DOWN (bought NO) | 7739 | 28 | 3% | 2% | -58% | -91% | -92% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 1905 | 9 | 2% | 1% | -21% | -76% | -76% |
| 0.05–0.1% | 1883 | 6 | 3% | 1% | -54% | -92% | -92% |
| 0.1–0.2% | 2714 | 9 | 4% | 2% | -59% | -91% | -92% |
| 0.2–0.5% | 2923 | 18 | 6% | 3% | -32% | -89% | -88% |
| Over 0.5% | 1141 | 5 | 6% | 2% | -55% | -88% | -90% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 4019 | 20 | 4% | 2% | -43% | -86% | -86% |
| Morning (6am–12pm) | 3615 | 20 | 4% | 2% | -36% | -91% | -90% |
| Afternoon (12–6pm) | 3575 | 9 | 3% | 1% | -70% | -90% | -91% |
| Evening (6pm–12am) | 4359 | 13 | 3% | 2% | -66% | -94% | -94% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 25 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,515 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 41 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/12 5:14:33 AM | SILVER | UP | 27 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/12 5:14:33 AM | USDJPY | DOWN | 27 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/12 5:14:33 AM | PALLADIUM | UP | 27 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/12 5:13:46 AM | COPPER | DOWN | 74 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/12 5:13:46 AM | BNB | UP | 74 sec | -0.104% | 1¢ | ❌ Lost | -$0.15 |
| 10/12 5:13:46 AM | ZEC | UP | 74 sec | -0.289% | 0¢ | ❌ Lost | $0.00 |
| 10/12 5:13:14 AM | EURUSD | UP | 1.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/12 5:12:11 AM | NEAR | UP | 2.8 min | -0.791% | 1¢ | ❌ Lost | -$0.15 |
| 10/12 5:12:11 AM | DOGE | UP | 2.8 min | -0.219% | 1¢ | ❌ Lost | -$0.15 |
| 10/12 5:11:55 AM | XRP | UP | 3.1 min | -0.249% | 1¢ | ❌ Lost | -$0.15 |
| 10/12 5:11:55 AM | HYPE | UP | 3.1 min | -0.222% | 1¢ | ❌ Lost | -$0.15 |
| 10/12 5:11:24 AM | BTC | UP | 3.6 min | -0.122% | 1¢ | ❌ Lost | -$0.15 |
| 10/12 5:10:36 AM | SOL | UP | 4.4 min | -0.351% | 1¢ | ❌ Lost | -$0.15 |
| 10/12 5:10:36 AM | ETH | UP | 4.4 min | -0.216% | 1¢ | ❌ Lost | -$0.15 |
| 10/12 5:10:04 AM | GOLD | UP | 4.9 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/12 5:09:46 AM | WTI | DOWN | 5.2 min | — | 3¢ | ❌ Lost | -$0.15 |
| 10/12 4:59:54 AM | XRP | DOWN | 5 sec | +0.007% | 1¢ | ❌ Lost | -$0.15 |
| 10/12 4:59:54 AM | BTC | UP | 5 sec | +0.002% | 0¢ | ❌ Lost | -$0.15 |
| 10/12 4:59:54 AM | COPPER | UP | 5 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/12 4:59:54 AM | BNB | UP | 5 sec | -0.047% | 0¢ | ❌ Lost | $0.00 |
| 10/12 4:59:54 AM | PLATINUM | UP | 5 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/12 4:59:16 AM | GOLD | UP | 44 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/12 4:59:16 AM | SOL | UP | 44 sec | -0.048% | 0¢ | ❌ Lost | -$0.15 |
| 10/12 4:59:16 AM | NATGAS | UP | 44 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/12 4:59:16 AM | ETH | UP | 44 sec | -0.061% | 0¢ | ❌ Lost | $0.00 |
| 10/12 4:59:00 AM | DOGE | UP | 60 sec | -0.136% | 1¢ | ❌ Lost | -$0.15 |
| 10/12 4:58:13 AM | NEAR | UP | 1.8 min | -0.406% | 1¢ | ❌ Lost | -$0.15 |
| 10/12 4:57:42 AM | ZEC | DOWN | 2.3 min | +0.264% | 1¢ | ❌ Lost | -$0.15 |
| 10/12 4:57:27 AM | HYPE | UP | 2.5 min | -0.199% | 1¢ | ❌ Lost | -$0.15 |
| 10/12 4:44:45 AM | EURUSD | UP | 15 sec | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
