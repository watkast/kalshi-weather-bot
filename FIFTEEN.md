# 15-Minute 1¢ Study

*Updated Mon Oct 12, 9:35 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 1185 finished bets | 1% | $39.45 | +31% | +3.33¢ | $34.25 / $5.20 |

*Expect about **82 buys a day** (~$12.37/day at risk); max loss per buy **15¢**.*

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
| 15594 | 15587 | 62 (0%) | 1.07% | -$1,012.70 (-54%) | Hold to the close: -$1,012.70 (-54%) |

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
| Volatility model | 10378 | 4.5% | 0.4% (45) | -668% | ❌ Worse |
| Momentum model | 10378 | 4.5% | 0.4% (45) | -694% | ❌ Worse |
| Mean-reversion model | 10378 | 7.2% | 0.4% (45) | -773% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 10378 | 45 | -46% | -88% | -88% | -86% |
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
| Crypto | 10576 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 3700 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 1311 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 15587 | 3% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 62 | 0% | -$1,012.70 | -54% | — |
| Sell at 2¢ | 533 | 3% | -$1,700.12 | -90% | 33 sec |
| Sell at 3¢ | 354 | 2% | -$1,700.64 | -90% | 46 sec |
| Sell at 5¢ | 259 | 2% | -$1,670.35 | -89% | 50 sec |
| Sell at 10¢ | 170 | 1% | -$1,588.00 | -84% | 64 sec |
| Sell at 25¢ | 96 | 1% | -$1,464.94 | -78% | 80 sec |
| Sell at 50¢ | 64 | 0% | -$1,308.70 | -70% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 420 | 4 | 11% | 3% | -10% | -81% | -86% |
| 2–5 min | 5018 | 32 | 6% | 3% | -37% | -88% | -88% |
| 1–2 min | 4118 | 16 | 3% | 2% | -58% | -94% | -94% |
| Under 1 min | 6027 | 10 | 1% | 0% | -76% | -91% | -91% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 1187 | 7 | 4% | 3% | -28% | -90% | -90% |
| HYPE | 1185 | 4 | 4% | 2% | -58% | -90% | -89% |
| DOGE | 1178 | 2 | 4% | 2% | -79% | -91% | -90% |
| BNB | 1176 | 5 | 4% | 2% | -48% | -91% | -92% |
| ETH | 1175 | 8 | 5% | 2% | -17% | -89% | -89% |
| SOL | 1175 | 2 | 3% | 1% | -79% | -93% | -92% |
| BTC | 1171 | 5 | 5% | 2% | -43% | -88% | -90% |
| NEAR | 1165 | 7 | 5% | 2% | -21% | -76% | -77% |
| XRP | 1164 | 7 | 2% | 1% | -25% | -84% | -85% |
| GOLD | 606 | 0 | 3% | 1% | -100% | -92% | -94% |
| SILVER | 593 | 1 | 3% | 1% | -81% | -94% | -94% |
| WTI | 569 | 3 | 3% | 1% | -40% | -94% | -96% |
| COPPER | 531 | 0 | 1% | 1% | -100% | -98% | -98% |
| PLATINUM | 490 | 0 | 0% | 0% | -100% | -100% | -99% |
| PALLADIUM | 456 | 1 | 1% | 0% | -80% | -98% | -98% |
| NATGAS | 455 | 3 | 3% | 2% | -38% | -95% | -94% |
| EURUSD | 440 | 3 | 3% | 2% | -36% | -74% | -73% |
| GBPUSD | 421 | 1 | 2% | 1% | -78% | -96% | -96% |
| USDJPY | 381 | 3 | 1% | 1% | -27% | -98% | -97% |
| USDCAD | 36 | 0 | 0% | 0% | -100% | -100% | -100% |
| AUDUSD | 33 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 7844 | 34 | 3% | 2% | -50% | -90% | -89% |
| DOWN (bought NO) | 7743 | 28 | 3% | 2% | -58% | -91% | -92% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 1906 | 9 | 2% | 1% | -21% | -76% | -76% |
| 0.05–0.1% | 1885 | 6 | 3% | 1% | -54% | -92% | -92% |
| 0.1–0.2% | 2717 | 9 | 4% | 2% | -59% | -91% | -92% |
| 0.2–0.5% | 2924 | 18 | 6% | 3% | -32% | -89% | -88% |
| Over 0.5% | 1141 | 5 | 6% | 2% | -55% | -88% | -90% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 4019 | 20 | 4% | 2% | -43% | -86% | -86% |
| Morning (6am–12pm) | 3634 | 20 | 4% | 2% | -36% | -91% | -91% |
| Afternoon (12–6pm) | 3575 | 9 | 3% | 1% | -70% | -90% | -91% |
| Evening (6pm–12am) | 4359 | 13 | 3% | 2% | -66% | -94% | -94% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 25 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,506 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 41 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/12 9:29:45 AM | WTI | DOWN | 15 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/12 9:29:28 AM | ETH | UP | 31 sec | -0.064% | 0¢ | ❌ Lost | $0.00 |
| 10/12 9:29:28 AM | ZEC | UP | 31 sec | -0.129% | 1¢ | ❌ Lost | -$0.15 |
| 10/12 9:29:28 AM | BTC | UP | 31 sec | -0.047% | 0¢ | ❌ Lost | $0.00 |
| 10/12 9:29:12 AM | SOL | UP | 47 sec | -0.125% | 0¢ | ❌ Lost | $0.00 |
| 10/12 9:29:12 AM | DOGE | UP | 47 sec | -0.169% | 0¢ | ❌ Lost | -$0.15 |
| 10/12 9:28:56 AM | BNB | UP | 63 sec | -0.088% | 0¢ | ❌ Lost | $0.00 |
| 10/12 9:28:56 AM | NEAR | UP | 63 sec | -0.495% | 0¢ | ❌ Lost | -$0.15 |
| 10/12 9:28:56 AM | GOLD | UP | 63 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/12 9:28:40 AM | USDCAD | DOWN | 79 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/12 9:28:08 AM | GBPUSD | UP | 1.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/12 9:28:08 AM | NATGAS | DOWN | 1.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/12 9:28:08 AM | AUDUSD | UP | 1.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/12 9:27:52 AM | EURUSD | UP | 2.1 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/12 9:27:52 AM | USDJPY | DOWN | 2.1 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/12 9:27:36 AM | SILVER | UP | 2.4 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/12 9:27:02 AM | PALLADIUM | UP | 3.0 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/12 9:26:46 AM | PLATINUM | UP | 3.2 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/12 9:26:15 AM | COPPER | UP | 3.7 min | — | 0¢ | ❌ Lost | -$0.15 |
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

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
