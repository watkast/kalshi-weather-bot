# 15-Minute 1¢ Study

*Updated Wed Nov 4, 10:05 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 3644 finished bets | 1% | $125.50 | +31% | +3.44¢ | $77.95 / $47.55 |

*Expect about **97 buys a day** (~$14.60/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 3381 | $52.80 | +14% |
| Volatility model ≥ 2%, hold to the close | 6758 | $37.40 | +5% |
| Momentum model ≥ 2%, hold to the close | 5568 | -$40.30 | -6% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 45490 | 45480 | 169 (0%) | 1.07% | -$3,177.25 (-57%) | Hold to the close: -$3,177.25 (-57%) |

*In play or awaiting result: 9. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 27784 | 4.7% | 0.4% (109) | -676% | ❌ Worse |
| Momentum model | 27784 | 4.6% | 0.4% (109) | -702% | ❌ Worse |
| Mean-reversion model | 27784 | 8.1% | 0.4% (109) | -823% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 27784 | 109 | -50% | -88% | -87% | -85% |
| Volatility model ≥ 2% | 6758 | 61 | +5% | -79% | -78% | -74% |
| Volatility model ≥ 5% | 3644 | 38 | +31% | -76% | -75% | -71% |
| Volatility model ≥ 10% | 2071 | 23 | +59% | -71% | -69% | -66% |
| Momentum model ≥ 2% | 5568 | 43 | -6% | -81% | -81% | -78% |
| Momentum model ≥ 5% | 3381 | 30 | +14% | -79% | -79% | -75% |
| Momentum model ≥ 10% | 2204 | 19 | +21% | -75% | -74% | -70% |
| Mean-reversion model ≥ 2% | 11504 | 79 | -25% | -83% | -83% | -81% |
| Mean-reversion model ≥ 5% | 8082 | 68 | -7% | -81% | -80% | -78% |
| Mean-reversion model ≥ 10% | 5415 | 48 | +1% | -80% | -79% | -77% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 27989 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 10814 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 6677 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 45480 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 169 | 0% | -$3,177.25 | -57% | — |
| Sell at 2¢ | 1785 | 4% | -$4,827.15 | -87% | 47 sec |
| Sell at 3¢ | 1221 | 3% | -$4,815.06 | -87% | 49 sec |
| Sell at 5¢ | 845 | 2% | -$4,714.00 | -85% | 63 sec |
| Sell at 10¢ | 511 | 1% | -$4,509.84 | -81% | 65 sec |
| Sell at 25¢ | 268 | 1% | -$4,180.17 | -75% | 83 sec |
| Sell at 50¢ | 172 | 0% | -$3,808.25 | -69% | 1.8 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 11 | 0 | 27% | 18% | -100% | -53% | -29% |
| 5–10 min | 2249 | 10 | 11% | 4% | -58% | -81% | -83% |
| 2–5 min | 14637 | 79 | 7% | 3% | -47% | -87% | -86% |
| 1–2 min | 11465 | 39 | 3% | 2% | -62% | -92% | -92% |
| Under 1 min | 17118 | 41 | 1% | 0% | -66% | -85% | -84% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 3135 | 13 | 5% | 2% | -47% | -88% | -88% |
| SOL | 3130 | 12 | 4% | 2% | -51% | -90% | -90% |
| HYPE | 3122 | 9 | 5% | 2% | -64% | -89% | -87% |
| BNB | 3122 | 17 | 5% | 2% | -32% | -85% | -84% |
| DOGE | 3110 | 6 | 4% | 2% | -76% | -90% | -90% |
| ETH | 3104 | 12 | 7% | 3% | -53% | -85% | -85% |
| BTC | 3093 | 15 | 5% | 2% | -34% | -87% | -89% |
| NEAR | 3090 | 15 | 5% | 2% | -37% | -84% | -84% |
| XRP | 3083 | 12 | 3% | 1% | -52% | -89% | -89% |
| GOLD | 1675 | 5 | 5% | 2% | -64% | -81% | -83% |
| WTI | 1629 | 5 | 4% | 1% | -63% | -92% | -93% |
| SILVER | 1627 | 8 | 5% | 2% | -42% | -82% | -81% |
| PLATINUM | 1458 | 4 | 2% | 1% | -74% | -96% | -96% |
| EURUSD | 1403 | 3 | 2% | 1% | -80% | -89% | -89% |
| COPPER | 1376 | 6 | 2% | 1% | -59% | -70% | -70% |
| GBPUSD | 1329 | 3 | 2% | 1% | -79% | -96% | -96% |
| NATGAS | 1323 | 8 | 2% | 1% | -44% | -75% | -75% |
| USDJPY | 1310 | 5 | 2% | 1% | -64% | -97% | -97% |
| PALLADIUM | 1307 | 3 | 1% | 1% | -79% | -91% | -91% |
| AUDUSD | 859 | 4 | 2% | 1% | -57% | -86% | -86% |
| USDCAD | 827 | 0 | 2% | 0% | -100% | -97% | -98% |
| BRENT | 419 | 0 | 1% | 1% | -100% | -98% | -97% |
| 10YRRATE | 257 | 1 | 5% | 2% | -64% | -56% | -54% |
| 30YRRATE | 237 | 0 | 1% | 0% | -100% | -98% | -97% |
| 2YRRATE | 236 | 2 | 3% | 0% | -21% | -15% | -14% |
| 5YRRATE | 219 | 1 | 5% | 2% | -57% | -92% | -94% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 23098 | 90 | 4% | 2% | -55% | -88% | -87% |
| DOWN (bought NO) | 22382 | 79 | 4% | 2% | -60% | -86% | -87% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 4512 | 22 | 2% | 1% | -15% | -83% | -82% |
| 0.05–0.1% | 4765 | 18 | 3% | 2% | -43% | -91% | -90% |
| 0.1–0.2% | 7215 | 25 | 4% | 2% | -57% | -90% | -89% |
| 0.2–0.5% | 8326 | 33 | 6% | 3% | -56% | -87% | -86% |
| Over 0.5% | 3163 | 13 | 7% | 3% | -58% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 11276 | 40 | 4% | 2% | -60% | -87% | -87% |
| Morning (6am–12pm) | 11403 | 50 | 4% | 2% | -50% | -86% | -85% |
| Afternoon (12–6pm) | 10598 | 39 | 4% | 2% | -57% | -86% | -86% |
| Evening (6pm–12am) | 12203 | 40 | 3% | 2% | -62% | -90% | -89% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,685 |
| Time from buy to best bounce (bounced bets) | 51 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/4 9:59:53 AM | 5YRRATE | UP | 7 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/4 9:59:53 AM | NATGAS | DOWN | 7 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/4 9:59:53 AM | GBPUSD | UP | 7 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/4 9:59:53 AM | COPPER | DOWN | 7 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/4 9:59:53 AM | 30YRRATE | DOWN | 7 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/4 9:59:35 AM | 2YRRATE | UP | 24 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/4 9:59:19 AM | DOGE | DOWN | 40 sec | +0.012% | 0¢ | ❌ Lost | $0.00 |
| 11/4 9:59:19 AM | ETH | UP | 40 sec | -0.068% | 0¢ | ❌ Lost | -$0.15 |
| 11/4 9:58:49 AM | PALLADIUM | UP | 70 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/4 9:58:34 AM | XRP | DOWN | 85 sec | +0.175% | 1¢ | ❌ Lost | -$0.15 |
| 11/4 9:58:34 AM | GOLD | DOWN | 85 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 11/4 9:58:34 AM | SOL | UP | 85 sec | -0.263% | 0¢ | ❌ Lost | $0.00 |
| 11/4 9:58:18 AM | PLATINUM | UP | 1.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/4 9:58:18 AM | NEAR | UP | 1.7 min | -0.633% | 1¢ | ❌ Lost | -$0.15 |
| 11/4 9:58:18 AM | BTC | UP | 1.7 min | -0.198% | 1¢ | ❌ Lost | -$0.15 |
| 11/4 9:58:02 AM | BNB | UP | 1.9 min | -0.168% | 1¢ | ❌ Lost | -$0.15 |
| 11/4 9:57:46 AM | HYPE | UP | 2.2 min | -0.531% | 1¢ | ❌ Lost | -$0.15 |
| 11/4 9:56:42 AM | WTI | UP | 3.3 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/4 9:56:42 AM | USDCAD | DOWN | 3.3 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/4 9:55:24 AM | BRENT | UP | 4.6 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/4 9:44:41 AM | XRP | DOWN | 18 sec | +0.084% | 0¢ | ❌ Lost | $0.00 |
| 11/4 9:44:25 AM | BTC | DOWN | 34 sec | +0.098% | 0¢ | ❌ Lost | $0.00 |
| 11/4 9:44:09 AM | HYPE | DOWN | 50 sec | +0.225% | 1¢ | ❌ Lost | -$0.15 |
| 11/4 9:43:53 AM | NATGAS | DOWN | 66 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/4 9:43:53 AM | SOL | DOWN | 66 sec | +0.192% | 0¢ | ❌ Lost | $0.00 |
| 11/4 9:43:06 AM | USDCAD | DOWN | 1.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/4 9:43:06 AM | GBPUSD | UP | 1.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/4 9:43:06 AM | EURUSD | UP | 1.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/4 9:43:06 AM | ETH | DOWN | 1.9 min | +0.301% | 1¢ | ❌ Lost | -$0.15 |
| 11/4 9:42:35 AM | DOGE | DOWN | 2.4 min | +0.333% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
