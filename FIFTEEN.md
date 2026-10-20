# 15-Minute 1¢ Study

*Updated Tue Oct 20, 10:33 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 2148 finished bets | 1% | $79.90 | +33% | +3.72¢ | $22.55 / $57.35 |

*Expect about **96 buys a day** (~$14.38/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 1976 | $61.60 | +28% |
| Momentum model ≥ 2%, hold to the close | 3299 | -$24.50 | -6% |
| Volatility model ≥ 5%, sell at 50¢ | 2148 | -$37.10 | -15% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 25350 | 25343 | 92 (0%) | 1.07% | -$1,796.60 (-58%) | Hold to the close: -$1,796.60 (-58%) |

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
| Volatility model | 16532 | 4.6% | 0.4% (65) | -672% | ❌ Worse |
| Momentum model | 16532 | 4.5% | 0.4% (65) | -695% | ❌ Worse |
| Mean-reversion model | 16532 | 7.8% | 0.4% (65) | -811% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 16532 | 65 | -51% | -87% | -87% | -85% |
| Volatility model ≥ 2% | 3901 | 31 | -9% | -77% | -76% | -73% |
| Volatility model ≥ 5% | 2148 | 23 | +33% | -71% | -70% | -67% |
| Volatility model ≥ 10% | 1240 | 15 | +69% | -60% | -58% | -55% |
| Momentum model ≥ 2% | 3299 | 26 | -6% | -79% | -78% | -75% |
| Momentum model ≥ 5% | 1976 | 20 | +28% | -74% | -74% | -70% |
| Momentum model ≥ 10% | 1304 | 13 | +36% | -67% | -66% | -61% |
| Mean-reversion model ≥ 2% | 6488 | 42 | -30% | -83% | -82% | -80% |
| Mean-reversion model ≥ 5% | 4516 | 34 | -17% | -80% | -80% | -77% |
| Mean-reversion model ≥ 10% | 2988 | 22 | -16% | -77% | -77% | -75% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 16730 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 5986 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 2627 | 1% | 1% | 1% | 1% | 0% | 0% |
| **All** | 25343 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 92 | 0% | -$1,796.60 | -58% | — |
| Sell at 2¢ | 917 | 4% | -$2,720.18 | -88% | 46 sec |
| Sell at 3¢ | 622 | 2% | -$2,716.02 | -88% | 47 sec |
| Sell at 5¢ | 441 | 2% | -$2,671.95 | -87% | 51 sec |
| Sell at 10¢ | 269 | 1% | -$2,578.21 | -84% | 64 sec |
| Sell at 25¢ | 147 | 1% | -$2,388.03 | -77% | 80 sec |
| Sell at 50¢ | 95 | 0% | -$2,163.35 | -70% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 1005 | 5 | 10% | 3% | -53% | -81% | -84% |
| 2–5 min | 8205 | 41 | 7% | 3% | -51% | -88% | -87% |
| 1–2 min | 6473 | 24 | 3% | 2% | -60% | -93% | -92% |
| Under 1 min | 9656 | 22 | 1% | 0% | -67% | -86% | -86% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 1881 | 11 | 4% | 2% | -27% | -90% | -90% |
| HYPE | 1870 | 6 | 5% | 3% | -61% | -89% | -87% |
| BNB | 1869 | 9 | 5% | 2% | -41% | -83% | -82% |
| ETH | 1858 | 9 | 6% | 3% | -42% | -87% | -87% |
| DOGE | 1858 | 3 | 4% | 2% | -80% | -91% | -90% |
| SOL | 1856 | 2 | 3% | 2% | -87% | -92% | -92% |
| XRP | 1849 | 7 | 3% | 1% | -54% | -87% | -88% |
| NEAR | 1845 | 10 | 6% | 3% | -30% | -79% | -79% |
| BTC | 1844 | 10 | 5% | 2% | -27% | -88% | -90% |
| GOLD | 981 | 1 | 3% | 1% | -88% | -92% | -95% |
| SILVER | 946 | 4 | 3% | 1% | -51% | -81% | -81% |
| WTI | 923 | 3 | 3% | 1% | -62% | -94% | -95% |
| COPPER | 822 | 3 | 2% | 1% | -66% | -75% | -74% |
| PLATINUM | 816 | 0 | 1% | 0% | -100% | -99% | -98% |
| NATGAS | 755 | 5 | 2% | 1% | -38% | -84% | -83% |
| EURUSD | 752 | 3 | 2% | 1% | -63% | -83% | -83% |
| PALLADIUM | 743 | 2 | 1% | 0% | -75% | -86% | -86% |
| GBPUSD | 709 | 1 | 2% | 1% | -87% | -97% | -97% |
| USDJPY | 661 | 3 | 1% | 1% | -58% | -99% | -98% |
| AUDUSD | 277 | 0 | 0% | 0% | -100% | -99% | -99% |
| USDCAD | 228 | 0 | 0% | 0% | -100% | -99% | -99% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 12774 | 45 | 4% | 2% | -60% | -88% | -87% |
| DOWN (bought NO) | 12569 | 47 | 3% | 1% | -57% | -88% | -89% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 2811 | 15 | 2% | 1% | -11% | -77% | -76% |
| 0.05–0.1% | 2901 | 10 | 3% | 2% | -50% | -92% | -91% |
| 0.1–0.2% | 4232 | 13 | 5% | 2% | -62% | -90% | -89% |
| 0.2–0.5% | 4885 | 23 | 6% | 3% | -48% | -88% | -87% |
| Over 0.5% | 1898 | 6 | 7% | 3% | -67% | -88% | -88% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 6450 | 26 | 4% | 2% | -54% | -85% | -85% |
| Morning (6am–12pm) | 6124 | 29 | 4% | 2% | -46% | -87% | -87% |
| Afternoon (12–6pm) | 5807 | 19 | 3% | 1% | -61% | -89% | -89% |
| Evening (6pm–12am) | 6962 | 18 | 3% | 2% | -70% | -92% | -92% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,767 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/20 10:29:53 AM | NATGAS | DOWN | 6 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/20 10:29:38 AM | SOL | UP | 22 sec | -0.041% | 1¢ | ❌ Lost | -$0.15 |
| 10/20 10:29:22 AM | BTC | UP | 38 sec | -0.040% | 1¢ | ❌ Lost | -$0.15 |
| 10/20 10:29:22 AM | NEAR | DOWN | 38 sec | +0.182% | 0¢ | ❌ Lost | -$0.15 |
| 10/20 10:29:22 AM | ZEC | DOWN | 38 sec | +0.165% | 0¢ | ❌ Lost | $0.00 |
| 10/20 10:29:06 AM | GOLD | UP | 54 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/20 10:28:50 AM | DOGE | DOWN | 70 sec | +0.154% | 0¢ | ❌ Lost | -$0.15 |
| 10/20 10:27:31 AM | PALLADIUM | UP | 2.5 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/20 10:27:15 AM | BNB | UP | 2.8 min | -0.147% | 4¢ | ❌ Lost | -$0.15 |
| 10/20 10:26:59 AM | HYPE | UP | 3.0 min | -0.356% | 11¢ | ❌ Lost | -$0.15 |
| 10/20 10:14:20 AM | SILVER | UP | 39 sec | — | 4¢ | ❌ Lost | -$0.15 |
| 10/20 10:14:20 AM | USDJPY | DOWN | 39 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/20 10:14:04 AM | BNB | DOWN | 55 sec | +0.112% | 1¢ | ❌ Lost | -$0.15 |
| 10/20 10:14:04 AM | EURUSD | UP | 55 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/20 10:13:47 AM | GOLD | UP | 73 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/20 10:13:47 AM | AUDUSD | UP | 73 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/20 10:13:47 AM | GBPUSD | UP | 73 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/20 10:13:47 AM | PLATINUM | UP | 73 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/20 10:13:31 AM | COPPER | UP | 89 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/20 10:13:31 AM | ZEC | UP | 89 sec | -0.274% | 47¢ | ❌ Lost | -$0.15 |
| 10/20 10:13:15 AM | WTI | DOWN | 1.8 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/20 10:13:00 AM | NEAR | UP | 2.0 min | -0.762% | 2¢ | ❌ Lost | -$0.15 |
| 10/20 10:13:00 AM | XRP | UP | 2.0 min | -0.288% | 1¢ | ❌ Lost | -$0.15 |
| 10/20 10:12:45 AM | NATGAS | UP | 2.2 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/20 10:12:45 AM | SOL | UP | 2.2 min | -0.412% | 0¢ | ❌ Lost | $0.00 |
| 10/20 10:12:29 AM | BTC | UP | 2.5 min | -0.228% | 1¢ | ❌ Lost | -$0.15 |
| 10/20 10:12:13 AM | ETH | UP | 2.8 min | -0.268% | 1¢ | ❌ Lost | -$0.15 |
| 10/20 10:11:09 AM | HYPE | UP | 3.8 min | -0.463% | 1¢ | ❌ Lost | -$0.15 |
| 10/20 9:59:56 AM | NATGAS | DOWN | 4 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/20 9:59:56 AM | USDJPY | DOWN | 4 sec | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
