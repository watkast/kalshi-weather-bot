# 15-Minute 1¢ Study

*Updated Tue Nov 17, 5:35 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 4488 finished bets | 1% | $218.25 | +44% | +4.86¢ | $82.50 / $135.75 |

*Expect about **88 buys a day** (~$13.27/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 4224 | $118.60 | +26% |
| Volatility model ≥ 2%, hold to the close | 8371 | $85.35 | +8% |
| Momentum model ≥ 2%, hold to the close | 6941 | $2.10 | +0% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 60093 | 60059 | 237 (0%) | 1.07% | -$3,990.00 (-55%) | Hold to the close: -$3,990.00 (-55%) |

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
| Volatility model | 36005 | 4.5% | 0.4% (154) | -622% | ❌ Worse |
| Momentum model | 36005 | 4.4% | 0.4% (154) | -647% | ❌ Worse |
| Mean-reversion model | 36005 | 7.9% | 0.4% (154) | -754% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 36005 | 154 | -45% | -87% | -87% | -84% |
| Volatility model ≥ 2% | 8371 | 78 | +8% | -77% | -76% | -72% |
| Volatility model ≥ 5% | 4488 | 51 | +44% | -72% | -70% | -67% |
| Volatility model ≥ 10% | 2577 | 30 | +69% | -63% | -61% | -58% |
| Momentum model ≥ 2% | 6941 | 57 | +0% | -79% | -78% | -74% |
| Momentum model ≥ 5% | 4224 | 41 | +26% | -74% | -74% | -70% |
| Momentum model ≥ 10% | 2751 | 26 | +34% | -66% | -66% | -62% |
| Mean-reversion model ≥ 2% | 14760 | 108 | -20% | -82% | -82% | -79% |
| Mean-reversion model ≥ 5% | 10267 | 89 | -4% | -80% | -79% | -77% |
| Mean-reversion model ≥ 10% | 6821 | 64 | +7% | -77% | -77% | -74% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 36211 | 5% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 14272 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 9576 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 60059 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 237 | 0% | -$3,990.00 | -55% | — |
| Sell at 2¢ | 2426 | 4% | -$6,383.24 | -87% | 47 sec |
| Sell at 3¢ | 1639 | 3% | -$6,374.79 | -87% | 48 sec |
| Sell at 5¢ | 1122 | 2% | -$6,256.70 | -86% | 63 sec |
| Sell at 10¢ | 684 | 1% | -$6,005.96 | -82% | 65 sec |
| Sell at 25¢ | 366 | 1% | -$5,550.54 | -76% | 80 sec |
| Sell at 50¢ | 243 | 0% | -$4,995.75 | -68% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 13 | 0 | 31% | 23% | -100% | -47% | -20% |
| 5–10 min | 3036 | 17 | 11% | 4% | -47% | -81% | -82% |
| 2–5 min | 19461 | 108 | 7% | 3% | -45% | -86% | -87% |
| 1–2 min | 15068 | 51 | 3% | 2% | -62% | -92% | -92% |
| Under 1 min | 22481 | 61 | 1% | 0% | -61% | -86% | -85% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 4050 | 19 | 5% | 3% | -38% | -88% | -87% |
| SOL | 4048 | 19 | 4% | 2% | -40% | -86% | -86% |
| HYPE | 4040 | 12 | 5% | 2% | -62% | -89% | -88% |
| DOGE | 4029 | 11 | 4% | 2% | -65% | -90% | -89% |
| BNB | 4028 | 21 | 5% | 2% | -34% | -85% | -85% |
| ETH | 4023 | 19 | 7% | 3% | -41% | -82% | -82% |
| NEAR | 4003 | 18 | 5% | 2% | -41% | -85% | -86% |
| BTC | 4003 | 21 | 5% | 2% | -29% | -86% | -88% |
| XRP | 3987 | 16 | 3% | 2% | -49% | -89% | -88% |
| GOLD | 2136 | 6 | 5% | 2% | -66% | -82% | -84% |
| WTI | 2115 | 7 | 4% | 1% | -60% | -91% | -92% |
| SILVER | 2073 | 9 | 5% | 2% | -48% | -83% | -83% |
| PLATINUM | 1887 | 4 | 3% | 1% | -80% | -95% | -95% |
| EURUSD | 1840 | 7 | 2% | 1% | -64% | -91% | -90% |
| COPPER | 1771 | 6 | 2% | 1% | -68% | -76% | -76% |
| GBPUSD | 1767 | 6 | 2% | 1% | -68% | -96% | -96% |
| NATGAS | 1745 | 10 | 2% | 1% | -47% | -75% | -75% |
| USDJPY | 1726 | 6 | 2% | 1% | -68% | -96% | -96% |
| PALLADIUM | 1698 | 4 | 1% | 0% | -78% | -93% | -93% |
| AUDUSD | 1283 | 6 | 2% | 1% | -56% | -89% | -89% |
| USDCAD | 1230 | 1 | 3% | 1% | -92% | -95% | -96% |
| BRENT | 847 | 0 | 2% | 1% | -100% | -97% | -98% |
| 10YRRATE | 435 | 2 | 3% | 1% | -57% | -73% | -71% |
| 2YRRATE | 420 | 4 | 4% | 2% | -11% | -49% | -48% |
| 30YRRATE | 403 | 0 | 2% | 1% | -100% | -96% | -94% |
| 5YRRATE | 391 | 2 | 4% | 2% | -52% | -93% | -95% |
| INX | 81 | 1 | 2% | 1% | +15% | -96% | -97% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 30573 | 121 | 4% | 2% | -54% | -88% | -88% |
| DOWN (bought NO) | 29486 | 116 | 4% | 2% | -55% | -86% | -87% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 5449 | 25 | 2% | 1% | -17% | -78% | -77% |
| 0.05–0.1% | 5908 | 24 | 3% | 2% | -37% | -91% | -91% |
| 0.1–0.2% | 9073 | 34 | 5% | 2% | -52% | -89% | -89% |
| 0.2–0.5% | 11204 | 50 | 7% | 3% | -50% | -86% | -86% |
| Over 0.5% | 4568 | 23 | 7% | 3% | -47% | -86% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 14507 | 45 | 4% | 2% | -65% | -88% | -88% |
| Morning (6am–12pm) | 14416 | 78 | 5% | 2% | -38% | -85% | -84% |
| Afternoon (12–6pm) | 14776 | 65 | 4% | 2% | -48% | -87% | -87% |
| Evening (6pm–12am) | 16360 | 49 | 4% | 2% | -66% | -89% | -89% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 5,072 |
| Time from buy to best bounce (bounced bets) | 50 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/17 5:29:44 PM | GBPUSD | DOWN | 15 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/17 5:29:12 PM | DOGE | UP | 48 sec | -0.088% | 0¢ | ❌ Lost | $0.00 |
| 11/17 5:28:52 PM | NEAR | DOWN | 68 sec | +0.225% | 0¢ | ❌ Lost | $0.00 |
| 11/17 5:28:52 PM | PLATINUM | UP | 68 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/17 5:28:52 PM | USDCAD | DOWN | 68 sec | — | 8¢ | ❌ Lost | -$0.15 |
| 11/17 5:28:52 PM | XRP | DOWN | 68 sec | +0.173% | 0¢ | ❌ Lost | $0.00 |
| 11/17 5:28:52 PM | BNB | UP | 68 sec | -0.111% | 0¢ | ❌ Lost | -$0.15 |
| 11/17 5:28:52 PM | ZEC | DOWN | 68 sec | +0.173% | 0¢ | ❌ Lost | -$0.15 |
| 11/17 5:28:52 PM | HYPE | UP | 68 sec | -0.188% | 1¢ | ❌ Lost | -$0.15 |
| 11/17 5:28:20 PM | PALLADIUM | UP | 1.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/17 5:28:20 PM | SOL | DOWN | 1.7 min | +0.243% | 1¢ | ❌ Lost | -$0.15 |
| 11/17 5:28:07 PM | BTC | UP | 1.9 min | -0.190% | 1¢ | ❌ Lost | -$0.15 |
| 11/17 5:27:50 PM | ETH | UP | 2.2 min | -0.206% | 1¢ | ❌ Lost | -$0.15 |
| 11/17 5:27:34 PM | GOLD | UP | 2.4 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/17 5:27:34 PM | SILVER | UP | 2.4 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/17 5:27:04 PM | COPPER | UP | 2.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/17 5:26:46 PM | NATGAS | UP | 3.2 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/17 5:14:31 PM | GBPUSD | UP | 28 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/17 5:14:15 PM | ETH | UP | 44 sec | -0.177% | 0¢ | ❌ Lost | $0.00 |
| 11/17 5:14:03 PM | BTC | UP | 56 sec | -0.117% | 0¢ | ❌ Lost | $0.00 |
| 11/17 5:14:03 PM | EURUSD | UP | 56 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/17 5:13:15 PM | BRENT | UP | 1.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/17 5:13:05 PM | USDCAD | DOWN | 1.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/17 5:13:05 PM | DOGE | UP | 1.9 min | -0.300% | 1¢ | ❌ Lost | -$0.15 |
| 11/17 5:12:49 PM | XRP | UP | 2.2 min | -0.285% | 1¢ | ❌ Lost | -$0.15 |
| 11/17 5:12:49 PM | SOL | UP | 2.2 min | -0.321% | 0¢ | ❌ Lost | -$0.15 |
| 11/17 5:12:33 PM | ZEC | UP | 2.5 min | -0.605% | 0¢ | ❌ Lost | $0.00 |
| 11/17 5:12:17 PM | NEAR | UP | 2.7 min | -0.524% | 1¢ | ❌ Lost | -$0.15 |
| 11/17 5:12:17 PM | COPPER | UP | 2.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/17 5:12:17 PM | HYPE | UP | 2.7 min | -0.389% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
