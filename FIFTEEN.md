# 15-Minute 1¢ Study

*Updated Mon Oct 12, 3:48 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 1179 finished bets | 1% | $40.05 | +31% | +3.40¢ | $34.70 / $5.35 |

*Expect about **83 buys a day** (~$12.52/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 1132 | $18.95 | +16% |
| 5+ min left, hold to the close | 423 | -$6.55 | -10% |
| Volatility model ≥ 2%, hold to the close | 2076 | -$11.45 | -5% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 15486 | 15479 | 62 (0%) | 1.07% | -$999.35 (-54%) | Hold to the close: -$999.35 (-54%) |

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
| Volatility model | 10317 | 4.5% | 0.4% (45) | -663% | ❌ Worse |
| Momentum model | 10317 | 4.5% | 0.4% (45) | -690% | ❌ Worse |
| Mean-reversion model | 10317 | 7.2% | 0.4% (45) | -767% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 10317 | 45 | -45% | -88% | -88% | -86% |
| Volatility model ≥ 2% | 2076 | 17 | -5% | -77% | -77% | -74% |
| Volatility model ≥ 5% | 1179 | 12 | +31% | -72% | -70% | -68% |
| Volatility model ≥ 10% | 746 | 8 | +56% | -62% | -62% | -58% |
| Momentum model ≥ 2% | 1827 | 14 | -7% | -79% | -80% | -78% |
| Momentum model ≥ 5% | 1132 | 10 | +16% | -75% | -76% | -72% |
| Momentum model ≥ 10% | 783 | 7 | +28% | -68% | -68% | -64% |
| Mean-reversion model ≥ 2% | 3614 | 26 | -21% | -85% | -85% | -81% |
| Mean-reversion model ≥ 5% | 2467 | 20 | -10% | -82% | -82% | -78% |
| Mean-reversion model ≥ 10% | 1649 | 14 | -1% | -81% | -81% | -77% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 10515 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 3666 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 1298 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 15479 | 3% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 62 | 0% | -$999.35 | -54% | — |
| Sell at 2¢ | 531 | 3% | -$1,687.29 | -90% | 33 sec |
| Sell at 3¢ | 353 | 2% | -$1,687.68 | -90% | 46 sec |
| Sell at 5¢ | 258 | 2% | -$1,657.65 | -89% | 50 sec |
| Sell at 10¢ | 170 | 1% | -$1,574.65 | -84% | 64 sec |
| Sell at 25¢ | 96 | 1% | -$1,451.59 | -78% | 80 sec |
| Sell at 50¢ | 64 | 0% | -$1,295.35 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 419 | 4 | 11% | 3% | -10% | -82% | -86% |
| 2–5 min | 4981 | 32 | 6% | 3% | -37% | -88% | -88% |
| 1–2 min | 4092 | 16 | 3% | 2% | -58% | -94% | -94% |
| Under 1 min | 5983 | 10 | 1% | 0% | -75% | -91% | -90% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 1180 | 7 | 4% | 3% | -27% | -90% | -90% |
| HYPE | 1179 | 4 | 4% | 2% | -58% | -90% | -89% |
| DOGE | 1171 | 2 | 4% | 2% | -78% | -91% | -90% |
| BNB | 1169 | 5 | 4% | 2% | -48% | -91% | -92% |
| ETH | 1168 | 8 | 5% | 2% | -17% | -89% | -89% |
| SOL | 1168 | 2 | 3% | 1% | -79% | -93% | -92% |
| BTC | 1164 | 5 | 5% | 2% | -43% | -88% | -91% |
| NEAR | 1158 | 7 | 5% | 3% | -21% | -76% | -76% |
| XRP | 1158 | 7 | 2% | 1% | -25% | -84% | -84% |
| GOLD | 600 | 0 | 4% | 1% | -100% | -92% | -94% |
| SILVER | 588 | 1 | 3% | 1% | -80% | -94% | -94% |
| WTI | 565 | 3 | 3% | 1% | -40% | -94% | -96% |
| COPPER | 525 | 0 | 1% | 1% | -100% | -98% | -98% |
| PLATINUM | 486 | 0 | 0% | 0% | -100% | -100% | -99% |
| NATGAS | 451 | 3 | 3% | 2% | -38% | -95% | -94% |
| PALLADIUM | 451 | 1 | 1% | 0% | -79% | -98% | -98% |
| EURUSD | 435 | 3 | 3% | 2% | -36% | -74% | -73% |
| GBPUSD | 418 | 1 | 2% | 1% | -78% | -96% | -96% |
| USDJPY | 378 | 3 | 1% | 1% | -26% | -98% | -97% |
| USDCAD | 35 | 0 | 0% | 0% | -100% | -100% | -100% |
| AUDUSD | 32 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 7777 | 34 | 3% | 2% | -49% | -90% | -89% |
| DOWN (bought NO) | 7702 | 28 | 3% | 2% | -58% | -91% | -92% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 1899 | 9 | 2% | 1% | -21% | -76% | -76% |
| 0.05–0.1% | 1873 | 6 | 3% | 1% | -54% | -92% | -92% |
| 0.1–0.2% | 2702 | 9 | 4% | 2% | -59% | -91% | -92% |
| 0.2–0.5% | 2899 | 18 | 6% | 3% | -32% | -89% | -88% |
| Over 0.5% | 1139 | 5 | 6% | 2% | -55% | -88% | -90% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 3930 | 20 | 4% | 2% | -41% | -86% | -86% |
| Morning (6am–12pm) | 3615 | 20 | 4% | 2% | -36% | -91% | -90% |
| Afternoon (12–6pm) | 3575 | 9 | 3% | 1% | -70% | -90% | -91% |
| Evening (6pm–12am) | 4359 | 13 | 3% | 2% | -66% | -94% | -94% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 25 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,523 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 41 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/12 3:44:59 AM | ETH | UP | 1 sec | -0.080% | 0¢ | ❌ Lost | $0.00 |
| 10/12 3:44:59 AM | USDCAD | UP | 1 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/12 3:44:28 AM | GBPUSD | DOWN | 32 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/12 3:44:28 AM | HYPE | UP | 32 sec | -0.065% | 0¢ | ❌ Lost | -$0.15 |
| 10/12 3:44:12 AM | USDJPY | DOWN | 48 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/12 3:43:41 AM | BTC | UP | 79 sec | -0.072% | 0¢ | ❌ Lost | $0.00 |
| 10/12 3:43:41 AM | SOL | UP | 79 sec | -0.139% | 1¢ | ❌ Lost | -$0.15 |
| 10/12 3:43:41 AM | ZEC | UP | 79 sec | -0.203% | 1¢ | ❌ Lost | -$0.15 |
| 10/12 3:43:41 AM | NATGAS | DOWN | 79 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/12 3:43:25 AM | DOGE | UP | 1.6 min | -0.148% | 1¢ | ❌ Lost | -$0.15 |
| 10/12 3:43:09 AM | BNB | UP | 1.9 min | -0.151% | 1¢ | ❌ Lost | -$0.15 |
| 10/12 3:43:09 AM | COPPER | UP | 1.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/12 3:43:09 AM | XRP | UP | 1.9 min | -0.192% | 1¢ | ❌ Lost | -$0.15 |
| 10/12 3:42:53 AM | SILVER | UP | 2.1 min | — | 2¢ | ❌ Lost | -$0.15 |
| 10/12 3:42:22 AM | WTI | DOWN | 2.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/12 3:41:35 AM | PALLADIUM | UP | 3.4 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/12 3:41:03 AM | GOLD | UP | 4.0 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/12 3:40:15 AM | NEAR | UP | 4.7 min | -0.654% | 1¢ | ❌ Lost | -$0.15 |
| 10/12 3:29:56 AM | SILVER | DOWN | 3 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/12 3:29:56 AM | PALLADIUM | DOWN | 3 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/12 3:29:25 AM | GOLD | UP | 34 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/12 3:29:09 AM | USDJPY | DOWN | 50 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/12 3:29:09 AM | GBPUSD | UP | 50 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/12 3:29:09 AM | WTI | UP | 50 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/12 3:28:53 AM | SOL | UP | 66 sec | -0.169% | 1¢ | ❌ Lost | -$0.15 |
| 10/12 3:28:53 AM | ETH | UP | 66 sec | -0.087% | 1¢ | ❌ Lost | -$0.15 |
| 10/12 3:28:38 AM | ZEC | UP | 81 sec | -0.269% | 1¢ | ❌ Lost | -$0.15 |
| 10/12 3:28:38 AM | DOGE | UP | 81 sec | -0.102% | 1¢ | ❌ Lost | -$0.15 |
| 10/12 3:28:22 AM | BNB | UP | 1.6 min | -0.152% | 1¢ | ❌ Lost | -$0.15 |
| 10/12 3:28:22 AM | XRP | UP | 1.6 min | -0.206% | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
