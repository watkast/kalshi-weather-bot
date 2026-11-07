# 15-Minute 1¢ Study

*Updated Sat Nov 7, 2:55 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 3921 finished bets | 1% | $152.70 | +35% | +3.89¢ | $74.55 / $78.15 |

*Expect about **96 buys a day** (~$14.47/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 3646 | $82.25 | +21% |
| Volatility model ≥ 2%, hold to the close | 7208 | $43.00 | +5% |
| Momentum model ≥ 2%, hold to the close | 5952 | -$25.25 | -4% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 49029 | 49012 | 178 (0%) | 1.07% | -$3,475.15 (-58%) | Hold to the close: -$3,475.15 (-58%) |

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
| Volatility model | 29769 | 4.8% | 0.4% (114) | -705% | ❌ Worse |
| Momentum model | 29769 | 4.7% | 0.4% (114) | -731% | ❌ Worse |
| Mean-reversion model | 29769 | 8.1% | 0.4% (114) | -854% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 29769 | 114 | -51% | -87% | -87% | -84% |
| Volatility model ≥ 2% | 7208 | 65 | +5% | -76% | -75% | -71% |
| Volatility model ≥ 5% | 3921 | 42 | +35% | -71% | -69% | -66% |
| Volatility model ≥ 10% | 2258 | 27 | +72% | -60% | -58% | -55% |
| Momentum model ≥ 2% | 5952 | 47 | -4% | -78% | -77% | -74% |
| Momentum model ≥ 5% | 3646 | 34 | +21% | -73% | -72% | -69% |
| Momentum model ≥ 10% | 2390 | 23 | +36% | -64% | -63% | -59% |
| Mean-reversion model ≥ 2% | 12313 | 83 | -26% | -82% | -82% | -79% |
| Mean-reversion model ≥ 5% | 8633 | 72 | -7% | -79% | -78% | -76% |
| Mean-reversion model ≥ 10% | 5771 | 52 | +3% | -76% | -76% | -73% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 29974 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 11670 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 7368 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 49012 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 178 | 0% | -$3,475.15 | -58% | — |
| Sell at 2¢ | 1915 | 4% | -$5,189.25 | -87% | 47 sec |
| Sell at 3¢ | 1301 | 3% | -$5,179.76 | -87% | 48 sec |
| Sell at 5¢ | 903 | 2% | -$5,072.20 | -85% | 63 sec |
| Sell at 10¢ | 544 | 1% | -$4,862.51 | -81% | 65 sec |
| Sell at 25¢ | 284 | 1% | -$4,523.11 | -76% | 83 sec |
| Sell at 50¢ | 182 | 0% | -$4,136.65 | -69% | 1.8 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 12 | 0 | 25% | 17% | -100% | -57% | -35% |
| 5–10 min | 2418 | 10 | 11% | 4% | -61% | -81% | -83% |
| 2–5 min | 15755 | 83 | 7% | 3% | -48% | -87% | -87% |
| 1–2 min | 12368 | 40 | 3% | 1% | -64% | -92% | -92% |
| Under 1 min | 18459 | 45 | 1% | 0% | -65% | -84% | -84% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 3361 | 13 | 5% | 2% | -50% | -88% | -88% |
| SOL | 3354 | 14 | 4% | 2% | -47% | -87% | -87% |
| HYPE | 3344 | 10 | 5% | 2% | -63% | -89% | -88% |
| BNB | 3341 | 17 | 5% | 2% | -36% | -85% | -85% |
| DOGE | 3331 | 6 | 4% | 2% | -77% | -90% | -90% |
| ETH | 3330 | 13 | 7% | 3% | -52% | -81% | -81% |
| NEAR | 3309 | 16 | 5% | 2% | -37% | -84% | -85% |
| BTC | 3304 | 15 | 5% | 2% | -38% | -88% | -89% |
| XRP | 3300 | 12 | 3% | 1% | -55% | -90% | -89% |
| GOLD | 1783 | 5 | 5% | 2% | -66% | -81% | -83% |
| WTI | 1751 | 6 | 4% | 1% | -59% | -92% | -92% |
| SILVER | 1733 | 8 | 5% | 2% | -45% | -82% | -81% |
| PLATINUM | 1567 | 4 | 2% | 1% | -76% | -96% | -96% |
| EURUSD | 1503 | 4 | 2% | 1% | -75% | -90% | -89% |
| COPPER | 1471 | 6 | 2% | 1% | -62% | -72% | -71% |
| NATGAS | 1433 | 8 | 2% | 1% | -48% | -77% | -76% |
| GBPUSD | 1426 | 4 | 2% | 1% | -74% | -96% | -96% |
| PALLADIUM | 1408 | 3 | 1% | 0% | -80% | -91% | -92% |
| USDJPY | 1406 | 5 | 2% | 1% | -67% | -97% | -96% |
| AUDUSD | 960 | 4 | 2% | 1% | -61% | -87% | -87% |
| USDCAD | 929 | 0 | 2% | 1% | -100% | -97% | -97% |
| BRENT | 524 | 0 | 2% | 1% | -100% | -97% | -97% |
| 10YRRATE | 303 | 1 | 4% | 1% | -69% | -62% | -60% |
| 2YRRATE | 287 | 3 | 4% | 1% | -2% | -28% | -27% |
| 30YRRATE | 285 | 0 | 2% | 1% | -100% | -96% | -95% |
| 5YRRATE | 262 | 1 | 4% | 2% | -64% | -93% | -95% |
| INX | 7 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 24852 | 94 | 4% | 2% | -56% | -88% | -87% |
| DOWN (bought NO) | 24160 | 84 | 4% | 2% | -60% | -86% | -86% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 4863 | 25 | 2% | 1% | -10% | -76% | -76% |
| 0.05–0.1% | 5118 | 18 | 3% | 2% | -46% | -91% | -91% |
| 0.1–0.2% | 7713 | 26 | 4% | 2% | -57% | -90% | -89% |
| 0.2–0.5% | 8914 | 34 | 6% | 3% | -57% | -87% | -87% |
| Over 0.5% | 3358 | 13 | 7% | 3% | -60% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 11973 | 41 | 4% | 2% | -61% | -87% | -87% |
| Morning (6am–12pm) | 12086 | 54 | 4% | 2% | -49% | -84% | -84% |
| Afternoon (12–6pm) | 11786 | 42 | 4% | 2% | -58% | -86% | -86% |
| Evening (6pm–12am) | 13167 | 41 | 3% | 2% | -64% | -90% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,772 |
| Time from buy to best bounce (bounced bets) | 51 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/7 2:44:25 PM | HYPE | DOWN | 34 sec | +0.034% | 0¢ | ❌ Lost | -$0.15 |
| 11/7 2:44:08 PM | NEAR | DOWN | 51 sec | +0.096% | 1¢ | ❌ Lost | -$0.15 |
| 11/7 2:43:52 PM | DOGE | DOWN | 67 sec | +0.086% | 1¢ | ❌ Lost | -$0.15 |
| 11/7 2:43:52 PM | BTC | DOWN | 67 sec | +0.046% | 0¢ | ❌ Lost | $0.00 |
| 11/7 2:43:04 PM | ETH | DOWN | 1.9 min | +0.090% | 1¢ | ❌ Lost | -$0.15 |
| 11/7 2:42:30 PM | SOL | DOWN | 2.5 min | +0.171% | 1¢ | ❌ Lost | -$0.15 |
| 11/7 2:42:30 PM | BNB | DOWN | 2.5 min | +0.030% | 1¢ | ❌ Lost | -$0.15 |
| 11/7 2:40:54 PM | ZEC | DOWN | 4.1 min | +0.511% | 1¢ | ❌ Lost | -$0.15 |
| 11/7 2:40:37 PM | XRP | DOWN | 4.4 min | +0.269% | 1¢ | ❌ Lost | -$0.15 |
| 11/7 2:29:57 PM | NEAR | UP | 2 sec | -0.179% | 0¢ | ❌ Lost | $0.00 |
| 11/7 2:29:41 PM | ETH | DOWN | 18 sec | +0.004% | 0¢ | ❌ Lost | $0.00 |
| 11/7 2:29:41 PM | BTC | DOWN | 18 sec | +0.005% | 1¢ | ❌ Lost | -$0.15 |
| 11/7 2:29:25 PM | HYPE | UP | 34 sec | -0.056% | 0¢ | ❌ Lost | -$0.15 |
| 11/7 2:29:09 PM | XRP | DOWN | 51 sec | +0.070% | 0¢ | ❌ Lost | $0.00 |
| 11/7 2:28:36 PM | SOL | DOWN | 83 sec | +0.083% | 1¢ | ❌ Lost | -$0.15 |
| 11/7 2:28:36 PM | BNB | UP | 83 sec | -0.050% | 1¢ | ❌ Lost | -$0.15 |
| 11/7 2:28:04 PM | DOGE | UP | 1.9 min | -0.209% | 1¢ | ❌ Lost | -$0.15 |
| 11/7 2:26:59 PM | ZEC | DOWN | 3.0 min | +0.378% | 1¢ | ❌ Lost | -$0.15 |
| 11/7 2:14:23 PM | HYPE | UP | 37 sec | -0.195% | 0¢ | ❌ Lost | $0.00 |
| 11/7 2:14:23 PM | ETH | UP | 37 sec | -0.136% | 0¢ | ❌ Lost | $0.00 |
| 11/7 2:14:23 PM | DOGE | UP | 37 sec | -0.213% | 0¢ | ❌ Lost | $0.00 |
| 11/7 2:14:23 PM | BTC | UP | 37 sec | -0.082% | 0¢ | ❌ Lost | $0.00 |
| 11/7 2:13:50 PM | XRP | UP | 70 sec | -0.165% | 1¢ | ❌ Lost | -$0.15 |
| 11/7 2:13:50 PM | BNB | UP | 70 sec | -0.065% | 0¢ | ❌ Lost | -$0.15 |
| 11/7 2:13:34 PM | NEAR | DOWN | 86 sec | +0.226% | 1¢ | ❌ Lost | -$0.15 |
| 11/7 2:13:34 PM | ZEC | UP | 86 sec | -0.275% | 0¢ | ❌ Lost | -$0.15 |
| 11/7 2:13:34 PM | SOL | UP | 86 sec | -0.164% | 0¢ | ❌ Lost | -$0.15 |
| 11/7 1:59:00 PM | HYPE | UP | 59 sec | -0.060% | 1¢ | ❌ Lost | -$0.15 |
| 11/7 1:56:35 PM | NEAR | UP | 3.4 min | -0.668% | 0¢ | ❌ Lost | -$0.15 |
| 11/7 1:54:59 PM | DOGE | UP | 5.0 min | -0.425% | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
