# 15-Minute 1¢ Study

*Updated Mon Oct 12, 9:56 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 1187 finished bets | 1% | $39.30 | +31% | +3.31¢ | $34.10 / $5.20 |

*Expect about **83 buys a day** (~$12.38/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 1136 | $18.50 | +15% |
| 5+ min left, hold to the close | 424 | -$6.70 | -11% |
| Volatility model ≥ 2%, hold to the close | 2089 | -$12.95 | -5% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 15611 | 15604 | 62 (0%) | 1.07% | -$1,014.35 (-54%) | Hold to the close: -$1,014.35 (-54%) |

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
| Volatility model | 10387 | 4.5% | 0.4% (45) | -671% | ❌ Worse |
| Momentum model | 10387 | 4.5% | 0.4% (45) | -697% | ❌ Worse |
| Mean-reversion model | 10387 | 7.2% | 0.4% (45) | -775% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 10387 | 45 | -46% | -88% | -88% | -86% |
| Volatility model ≥ 2% | 2089 | 17 | -5% | -77% | -77% | -74% |
| Volatility model ≥ 5% | 1187 | 12 | +31% | -72% | -71% | -68% |
| Volatility model ≥ 10% | 749 | 8 | +55% | -62% | -62% | -58% |
| Momentum model ≥ 2% | 1839 | 14 | -7% | -79% | -80% | -78% |
| Momentum model ≥ 5% | 1136 | 10 | +15% | -75% | -76% | -72% |
| Momentum model ≥ 10% | 786 | 7 | +27% | -68% | -68% | -64% |
| Mean-reversion model ≥ 2% | 3633 | 26 | -22% | -85% | -85% | -81% |
| Mean-reversion model ≥ 5% | 2482 | 20 | -10% | -82% | -82% | -78% |
| Mean-reversion model ≥ 10% | 1660 | 14 | -2% | -81% | -81% | -78% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 10585 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 3704 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 1315 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 15604 | 3% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 62 | 0% | -$1,014.35 | -54% | — |
| Sell at 2¢ | 534 | 3% | -$1,701.51 | -90% | 33 sec |
| Sell at 3¢ | 354 | 2% | -$1,702.29 | -90% | 46 sec |
| Sell at 5¢ | 259 | 2% | -$1,672.00 | -89% | 50 sec |
| Sell at 10¢ | 170 | 1% | -$1,589.65 | -84% | 64 sec |
| Sell at 25¢ | 96 | 1% | -$1,466.59 | -78% | 80 sec |
| Sell at 50¢ | 64 | 0% | -$1,310.35 | -70% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 420 | 4 | 11% | 3% | -10% | -81% | -86% |
| 2–5 min | 5024 | 32 | 6% | 3% | -37% | -88% | -88% |
| 1–2 min | 4120 | 16 | 3% | 2% | -58% | -94% | -94% |
| Under 1 min | 6036 | 10 | 1% | 0% | -76% | -91% | -91% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 1188 | 7 | 4% | 3% | -28% | -90% | -90% |
| HYPE | 1186 | 4 | 4% | 2% | -58% | -90% | -89% |
| DOGE | 1179 | 2 | 4% | 2% | -79% | -91% | -90% |
| BNB | 1177 | 5 | 4% | 2% | -48% | -91% | -92% |
| ETH | 1176 | 8 | 5% | 2% | -17% | -89% | -89% |
| SOL | 1176 | 2 | 3% | 1% | -79% | -93% | -92% |
| BTC | 1172 | 5 | 5% | 2% | -43% | -88% | -91% |
| NEAR | 1166 | 7 | 5% | 2% | -21% | -76% | -77% |
| XRP | 1165 | 7 | 2% | 1% | -25% | -84% | -85% |
| GOLD | 607 | 0 | 3% | 1% | -100% | -92% | -94% |
| SILVER | 593 | 1 | 3% | 1% | -81% | -94% | -94% |
| WTI | 570 | 3 | 3% | 1% | -40% | -94% | -96% |
| COPPER | 531 | 0 | 1% | 1% | -100% | -98% | -98% |
| PLATINUM | 490 | 0 | 0% | 0% | -100% | -100% | -99% |
| PALLADIUM | 457 | 1 | 1% | 0% | -80% | -98% | -98% |
| NATGAS | 456 | 3 | 3% | 2% | -39% | -95% | -94% |
| EURUSD | 441 | 3 | 3% | 2% | -37% | -74% | -73% |
| GBPUSD | 422 | 1 | 2% | 1% | -78% | -96% | -96% |
| USDJPY | 381 | 3 | 1% | 1% | -27% | -98% | -97% |
| USDCAD | 37 | 0 | 0% | 0% | -100% | -100% | -100% |
| AUDUSD | 34 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 7855 | 34 | 3% | 2% | -50% | -90% | -89% |
| DOWN (bought NO) | 7749 | 28 | 3% | 2% | -58% | -91% | -92% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 1908 | 9 | 2% | 1% | -21% | -76% | -76% |
| 0.05–0.1% | 1888 | 6 | 3% | 1% | -54% | -92% | -92% |
| 0.1–0.2% | 2718 | 9 | 4% | 2% | -59% | -91% | -92% |
| 0.2–0.5% | 2926 | 18 | 6% | 3% | -32% | -89% | -88% |
| Over 0.5% | 1142 | 5 | 6% | 2% | -55% | -88% | -90% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 4019 | 20 | 4% | 2% | -43% | -86% | -86% |
| Morning (6am–12pm) | 3651 | 20 | 4% | 2% | -37% | -91% | -91% |
| Afternoon (12–6pm) | 3575 | 9 | 3% | 1% | -70% | -90% | -91% |
| Evening (6pm–12am) | 4359 | 13 | 3% | 2% | -66% | -94% | -94% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 25 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,503 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 41 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/12 9:44:45 AM | ETH | DOWN | 14 sec | -0.023% | 0¢ | ❌ Lost | -$0.15 |
| 10/12 9:44:45 AM | SOL | UP | 14 sec | -0.114% | 0¢ | ❌ Lost | $0.00 |
| 10/12 9:44:45 AM | PALLADIUM | DOWN | 14 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/12 9:44:45 AM | NATGAS | UP | 14 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/12 9:44:45 AM | WTI | UP | 14 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/12 9:44:45 AM | GOLD | DOWN | 14 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/12 9:44:29 AM | DOGE | DOWN | 30 sec | +0.078% | 0¢ | ❌ Lost | $0.00 |
| 10/12 9:44:29 AM | XRP | UP | 30 sec | -0.065% | 0¢ | ❌ Lost | $0.00 |
| 10/12 9:44:13 AM | BNB | UP | 47 sec | -0.086% | 1¢ | ❌ Lost | -$0.15 |
| 10/12 9:43:56 AM | BTC | DOWN | 64 sec | +0.049% | 1¢ | ❌ Lost | -$0.15 |
| 10/12 9:43:24 AM | AUDUSD | UP | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/12 9:42:51 AM | GBPUSD | UP | 2.1 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/12 9:42:35 AM | USDCAD | DOWN | 2.4 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/12 9:42:03 AM | ZEC | UP | 3.0 min | -0.381% | 2¢ | ❌ Lost | $0.00 |
| 10/12 9:42:03 AM | HYPE | UP | 3.0 min | -0.254% | 1¢ | ❌ Lost | -$0.15 |
| 10/12 9:40:58 AM | EURUSD | UP | 4.0 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/12 9:40:58 AM | NEAR | UP | 4.0 min | -1.104% | 1¢ | ❌ Lost | -$0.15 |
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

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
