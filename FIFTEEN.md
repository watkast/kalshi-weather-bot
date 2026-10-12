# 15-Minute 1¢ Study

*Updated Sun Oct 11, 11:47 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 1168 finished bets | 1% | $41.55 | +33% | +3.56¢ | $35.30 / $6.25 |

*Expect about **84 buys a day** (~$12.55/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 1121 | $20.45 | +17% |
| 5+ min left, hold to the close | 411 | -$4.75 | -8% |
| Volatility model ≥ 2%, hold to the close | 2049 | -$7.55 | -3% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 15240 | 15233 | 62 (0%) | 1.07% | -$966.50 (-53%) | Hold to the close: -$966.50 (-53%) |

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
| Volatility model | 10177 | 4.5% | 0.4% (45) | -660% | ❌ Worse |
| Momentum model | 10177 | 4.5% | 0.4% (45) | -687% | ❌ Worse |
| Mean-reversion model | 10177 | 7.2% | 0.4% (45) | -762% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 10177 | 45 | -44% | -88% | -88% | -86% |
| Volatility model ≥ 2% | 2049 | 17 | -3% | -77% | -77% | -74% |
| Volatility model ≥ 5% | 1168 | 12 | +33% | -71% | -70% | -68% |
| Volatility model ≥ 10% | 740 | 8 | +57% | -61% | -61% | -58% |
| Momentum model ≥ 2% | 1805 | 14 | -5% | -79% | -80% | -78% |
| Momentum model ≥ 5% | 1121 | 10 | +17% | -75% | -76% | -73% |
| Momentum model ≥ 10% | 776 | 7 | +29% | -68% | -68% | -64% |
| Mean-reversion model ≥ 2% | 3564 | 26 | -20% | -85% | -85% | -81% |
| Mean-reversion model ≥ 5% | 2431 | 20 | -8% | -83% | -82% | -78% |
| Mean-reversion model ≥ 10% | 1631 | 14 | -0% | -81% | -81% | -77% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 10375 | 4% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 3584 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 1274 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 15233 | 3% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 62 | 0% | -$966.50 | -53% | — |
| Sell at 2¢ | 522 | 3% | -$1,656.78 | -90% | 33 sec |
| Sell at 3¢ | 346 | 2% | -$1,657.56 | -90% | 46 sec |
| Sell at 5¢ | 255 | 2% | -$1,626.75 | -89% | 49 sec |
| Sell at 10¢ | 169 | 1% | -$1,543.11 | -84% | 64 sec |
| Sell at 25¢ | 96 | 1% | -$1,418.74 | -77% | 80 sec |
| Sell at 50¢ | 64 | 0% | -$1,262.50 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 407 | 4 | 10% | 3% | -7% | -82% | -86% |
| 2–5 min | 4895 | 32 | 6% | 3% | -36% | -88% | -88% |
| 1–2 min | 4023 | 16 | 3% | 2% | -57% | -94% | -94% |
| Under 1 min | 5904 | 10 | 1% | 0% | -75% | -90% | -90% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 1165 | 7 | 4% | 3% | -26% | -90% | -90% |
| HYPE | 1163 | 4 | 4% | 2% | -57% | -90% | -89% |
| DOGE | 1156 | 2 | 4% | 2% | -78% | -90% | -90% |
| BNB | 1154 | 5 | 4% | 2% | -47% | -91% | -92% |
| ETH | 1152 | 8 | 5% | 2% | -15% | -90% | -89% |
| SOL | 1152 | 2 | 3% | 1% | -78% | -93% | -92% |
| BTC | 1148 | 5 | 5% | 2% | -42% | -88% | -91% |
| NEAR | 1143 | 7 | 5% | 3% | -20% | -75% | -76% |
| XRP | 1142 | 7 | 2% | 1% | -23% | -84% | -85% |
| GOLD | 590 | 0 | 4% | 1% | -100% | -92% | -94% |
| SILVER | 576 | 1 | 3% | 1% | -80% | -94% | -94% |
| WTI | 550 | 3 | 3% | 1% | -38% | -94% | -96% |
| COPPER | 512 | 0 | 1% | 1% | -100% | -98% | -98% |
| PLATINUM | 474 | 0 | 0% | 0% | -100% | -100% | -99% |
| NATGAS | 444 | 3 | 3% | 2% | -37% | -95% | -94% |
| PALLADIUM | 438 | 1 | 1% | 0% | -79% | -98% | -99% |
| EURUSD | 432 | 3 | 3% | 2% | -35% | -74% | -72% |
| GBPUSD | 409 | 1 | 2% | 1% | -77% | -96% | -96% |
| USDJPY | 371 | 3 | 1% | 1% | -25% | -98% | -97% |
| USDCAD | 31 | 0 | 0% | 0% | -100% | -100% | -100% |
| AUDUSD | 31 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 7633 | 34 | 3% | 2% | -48% | -90% | -89% |
| DOWN (bought NO) | 7600 | 28 | 3% | 2% | -57% | -91% | -92% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 1890 | 9 | 2% | 1% | -20% | -76% | -76% |
| 0.05–0.1% | 1851 | 6 | 3% | 1% | -54% | -92% | -92% |
| 0.1–0.2% | 2660 | 9 | 4% | 2% | -58% | -91% | -92% |
| 0.2–0.5% | 2839 | 18 | 6% | 3% | -30% | -89% | -88% |
| Over 0.5% | 1132 | 5 | 6% | 2% | -54% | -88% | -90% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 3699 | 20 | 4% | 2% | -37% | -85% | -86% |
| Morning (6am–12pm) | 3615 | 20 | 4% | 2% | -36% | -91% | -90% |
| Afternoon (12–6pm) | 3575 | 9 | 3% | 1% | -70% | -90% | -91% |
| Evening (6pm–12am) | 4344 | 13 | 3% | 1% | -66% | -94% | -94% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 25 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,540 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 41 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/11 11:44:49 PM | NATGAS | DOWN | 10 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/11 11:44:34 PM | GOLD | DOWN | 25 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/11 11:44:34 PM | ZEC | UP | 25 sec | -0.090% | 0¢ | ❌ Lost | -$0.15 |
| 10/11 11:44:18 PM | EURUSD | DOWN | 41 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/11 11:43:31 PM | SOL | UP | 88 sec | -0.201% | 0¢ | ❌ Lost | -$0.15 |
| 10/11 11:43:31 PM | XRP | UP | 88 sec | -0.205% | 0¢ | ❌ Lost | -$0.15 |
| 10/11 11:43:31 PM | BTC | UP | 88 sec | -0.117% | 1¢ | ❌ Lost | -$0.15 |
| 10/11 11:43:15 PM | HYPE | UP | 1.7 min | -0.201% | 0¢ | ❌ Lost | -$0.15 |
| 10/11 11:43:15 PM | SILVER | DOWN | 1.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/11 11:42:59 PM | WTI | DOWN | 2.0 min | — | 2¢ | ❌ Lost | -$0.15 |
| 10/11 11:42:43 PM | ETH | UP | 2.3 min | -0.186% | 2¢ | ❌ Lost | -$0.15 |
| 10/11 11:42:12 PM | NEAR | UP | 2.8 min | -1.115% | 1¢ | ❌ Lost | -$0.15 |
| 10/11 11:42:12 PM | BNB | UP | 2.8 min | -0.178% | 1¢ | ❌ Lost | -$0.15 |
| 10/11 11:41:56 PM | PLATINUM | DOWN | 3.1 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/11 11:41:56 PM | DOGE | UP | 3.1 min | -0.373% | 1¢ | ❌ Lost | -$0.15 |
| 10/11 11:29:23 PM | SILVER | UP | 36 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/11 11:29:07 PM | PALLADIUM | UP | 52 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/11 11:28:51 PM | GOLD | UP | 68 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/11 11:28:51 PM | PLATINUM | UP | 68 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/11 11:28:36 PM | WTI | DOWN | 84 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/11 11:28:36 PM | HYPE | UP | 84 sec | -0.169% | 1¢ | ❌ Lost | -$0.15 |
| 10/11 11:28:36 PM | ZEC | UP | 84 sec | -0.345% | 0¢ | ❌ Lost | -$0.15 |
| 10/11 11:28:20 PM | EURUSD | UP | 1.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/11 11:27:48 PM | COPPER | UP | 2.2 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/11 11:27:48 PM | GBPUSD | UP | 2.2 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/11 11:27:13 PM | DOGE | UP | 2.8 min | -0.214% | 1¢ | ❌ Lost | -$0.15 |
| 10/11 11:26:41 PM | SOL | UP | 3.3 min | -0.325% | 1¢ | ❌ Lost | -$0.15 |
| 10/11 11:26:41 PM | NEAR | DOWN | 3.3 min | +0.800% | 1¢ | ❌ Lost | -$0.15 |
| 10/11 11:26:26 PM | XRP | UP | 3.5 min | -0.317% | 1¢ | ❌ Lost | -$0.15 |
| 10/11 11:26:10 PM | ETH | UP | 3.8 min | -0.255% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
