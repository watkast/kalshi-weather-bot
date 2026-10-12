# 15-Minute 1¢ Study

*Updated Mon Oct 12, 11:07 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 1191 finished bets | 1% | $38.85 | +30% | +3.26¢ | $33.80 / $5.05 |

*Expect about **83 buys a day** (~$12.38/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 1140 | $18.05 | +15% |
| 5+ min left, hold to the close | 428 | -$7.30 | -12% |
| Volatility model ≥ 2%, hold to the close | 2094 | -$13.55 | -5% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 15683 | 15676 | 62 (0%) | 1.07% | -$1,022.30 (-54%) | Hold to the close: -$1,022.30 (-54%) |

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
| Volatility model | 10430 | 4.5% | 0.4% (45) | -671% | ❌ Worse |
| Momentum model | 10430 | 4.5% | 0.4% (45) | -697% | ❌ Worse |
| Mean-reversion model | 10430 | 7.2% | 0.4% (45) | -776% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 10430 | 45 | -46% | -88% | -88% | -86% |
| Volatility model ≥ 2% | 2094 | 17 | -5% | -77% | -77% | -74% |
| Volatility model ≥ 5% | 1191 | 12 | +30% | -72% | -71% | -68% |
| Volatility model ≥ 10% | 751 | 8 | +55% | -62% | -62% | -58% |
| Momentum model ≥ 2% | 1844 | 14 | -8% | -79% | -80% | -78% |
| Momentum model ≥ 5% | 1140 | 10 | +15% | -75% | -76% | -73% |
| Momentum model ≥ 10% | 788 | 7 | +27% | -68% | -68% | -64% |
| Mean-reversion model ≥ 2% | 3647 | 26 | -22% | -85% | -85% | -81% |
| Mean-reversion model ≥ 5% | 2493 | 20 | -11% | -82% | -82% | -78% |
| Mean-reversion model ≥ 10% | 1665 | 14 | -2% | -81% | -81% | -77% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 10628 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 3724 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 1324 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 15676 | 3% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 62 | 0% | -$1,022.30 | -54% | — |
| Sell at 2¢ | 535 | 3% | -$1,709.20 | -90% | 33 sec |
| Sell at 3¢ | 355 | 2% | -$1,709.85 | -90% | 47 sec |
| Sell at 5¢ | 260 | 2% | -$1,679.30 | -89% | 50 sec |
| Sell at 10¢ | 170 | 1% | -$1,597.60 | -85% | 64 sec |
| Sell at 25¢ | 96 | 1% | -$1,474.54 | -78% | 80 sec |
| Sell at 50¢ | 64 | 0% | -$1,318.30 | -70% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 424 | 4 | 11% | 3% | -11% | -81% | -86% |
| 2–5 min | 5036 | 32 | 6% | 3% | -38% | -88% | -88% |
| 1–2 min | 4142 | 16 | 3% | 2% | -58% | -94% | -94% |
| Under 1 min | 6070 | 10 | 1% | 0% | -76% | -91% | -91% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 1193 | 7 | 4% | 3% | -28% | -90% | -90% |
| HYPE | 1191 | 4 | 4% | 2% | -58% | -90% | -89% |
| DOGE | 1184 | 2 | 4% | 2% | -79% | -91% | -90% |
| BNB | 1182 | 5 | 4% | 2% | -48% | -91% | -92% |
| ETH | 1181 | 8 | 5% | 2% | -17% | -89% | -89% |
| SOL | 1181 | 2 | 3% | 1% | -79% | -93% | -92% |
| BTC | 1176 | 5 | 5% | 2% | -43% | -88% | -91% |
| NEAR | 1171 | 7 | 5% | 2% | -21% | -76% | -77% |
| XRP | 1169 | 7 | 2% | 1% | -25% | -84% | -85% |
| GOLD | 610 | 0 | 3% | 1% | -100% | -92% | -94% |
| SILVER | 597 | 1 | 3% | 1% | -81% | -94% | -94% |
| WTI | 573 | 3 | 3% | 1% | -40% | -94% | -96% |
| COPPER | 533 | 0 | 1% | 1% | -100% | -98% | -98% |
| PLATINUM | 492 | 0 | 0% | 0% | -100% | -100% | -99% |
| PALLADIUM | 461 | 1 | 1% | 0% | -80% | -98% | -98% |
| NATGAS | 458 | 3 | 3% | 2% | -39% | -95% | -94% |
| EURUSD | 443 | 3 | 3% | 2% | -37% | -74% | -73% |
| GBPUSD | 422 | 1 | 2% | 1% | -78% | -96% | -96% |
| USDJPY | 383 | 3 | 1% | 1% | -27% | -98% | -97% |
| USDCAD | 39 | 0 | 0% | 0% | -100% | -100% | -100% |
| AUDUSD | 37 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 7906 | 34 | 3% | 2% | -50% | -90% | -89% |
| DOWN (bought NO) | 7770 | 28 | 3% | 2% | -58% | -91% | -92% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 1912 | 9 | 2% | 1% | -21% | -77% | -76% |
| 0.05–0.1% | 1899 | 6 | 3% | 1% | -54% | -92% | -92% |
| 0.1–0.2% | 2723 | 9 | 4% | 2% | -59% | -91% | -92% |
| 0.2–0.5% | 2944 | 18 | 6% | 3% | -33% | -89% | -88% |
| Over 0.5% | 1147 | 5 | 6% | 2% | -55% | -88% | -90% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 4019 | 20 | 4% | 2% | -43% | -86% | -86% |
| Morning (6am–12pm) | 3723 | 20 | 4% | 2% | -38% | -91% | -91% |
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
| 10/12 10:59:53 AM | AUDUSD | DOWN | 6 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/12 10:59:53 AM | WTI | DOWN | 6 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/12 10:59:53 AM | PALLADIUM | UP | 6 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/12 10:59:21 AM | USDJPY | UP | 39 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/12 10:58:15 AM | GOLD | DOWN | 1.7 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/12 10:56:05 AM | SOL | UP | 3.9 min | -0.323% | 1¢ | ❌ Lost | -$0.15 |
| 10/12 10:55:30 AM | HYPE | UP | 4.5 min | -0.386% | 1¢ | ❌ Lost | -$0.15 |
| 10/12 10:55:30 AM | BNB | UP | 4.5 min | -0.237% | 0¢ | ❌ Lost | -$0.15 |
| 10/12 10:55:14 AM | NEAR | UP | 4.8 min | -1.797% | 1¢ | ❌ Lost | -$0.15 |
| 10/12 10:55:14 AM | XRP | UP | 4.8 min | -0.772% | 1¢ | ❌ Lost | -$0.15 |
| 10/12 10:54:59 AM | BTC | UP | 5.0 min | -0.242% | 1¢ | ❌ Lost | -$0.15 |
| 10/12 10:54:59 AM | DOGE | UP | 5.0 min | -0.597% | 1¢ | ❌ Lost | -$0.15 |
| 10/12 10:54:42 AM | ZEC | UP | 5.3 min | -1.151% | 1¢ | ❌ Lost | -$0.15 |
| 10/12 10:54:10 AM | ETH | UP | 5.8 min | -0.380% | 1¢ | ❌ Lost | -$0.15 |
| 10/12 10:44:43 AM | PALLADIUM | UP | 16 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/12 10:44:43 AM | DOGE | UP | 16 sec | -0.101% | 0¢ | ❌ Lost | $0.00 |
| 10/12 10:44:27 AM | BTC | UP | 32 sec | -0.053% | 0¢ | ❌ Lost | $0.00 |
| 10/12 10:44:27 AM | ETH | UP | 32 sec | -0.056% | 0¢ | ❌ Lost | $0.00 |
| 10/12 10:44:11 AM | PLATINUM | UP | 49 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/12 10:44:11 AM | BNB | UP | 49 sec | -0.082% | 0¢ | ❌ Lost | -$0.15 |
| 10/12 10:43:38 AM | ZEC | UP | 81 sec | -0.223% | 1¢ | ❌ Lost | -$0.15 |
| 10/12 10:43:38 AM | NEAR | UP | 81 sec | -0.516% | 0¢ | ❌ Lost | $0.00 |
| 10/12 10:43:38 AM | SILVER | UP | 81 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/12 10:43:22 AM | HYPE | UP | 1.6 min | -0.237% | 0¢ | ❌ Lost | -$0.15 |
| 10/12 10:43:22 AM | XRP | UP | 1.6 min | -0.203% | 1¢ | ❌ Lost | -$0.15 |
| 10/12 10:43:22 AM | COPPER | UP | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/12 10:43:06 AM | SOL | UP | 1.9 min | -0.246% | 0¢ | ❌ Lost | $0.00 |
| 10/12 10:29:59 AM | SILVER | UP | 1 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/12 10:29:59 AM | WTI | UP | 1 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/12 10:29:59 AM | EURUSD | UP | 1 sec | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
