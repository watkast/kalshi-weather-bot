# 15-Minute 1¢ Study

*Updated Wed Nov 11, 7:21 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 4209 finished bets | 1% | $176.75 | +38% | +4.20¢ | $86.05 / $90.70 |

*Expect about **95 buys a day** (~$14.25/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 3931 | $92.45 | +22% |
| Volatility model ≥ 2%, hold to the close | 7720 | $51.05 | +5% |
| Momentum model ≥ 2%, hold to the close | 6408 | -$22.05 | -3% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 53635 | 53618 | 205 (0%) | 1.07% | -$3,669.25 (-56%) | Hold to the close: -$3,669.25 (-56%) |

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
| Volatility model | 32277 | 4.7% | 0.4% (131) | -672% | ❌ Worse |
| Momentum model | 32277 | 4.6% | 0.4% (131) | -697% | ❌ Worse |
| Mean-reversion model | 32277 | 8.1% | 0.4% (131) | -815% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 32277 | 131 | -48% | -87% | -87% | -84% |
| Volatility model ≥ 2% | 7720 | 70 | +5% | -77% | -76% | -72% |
| Volatility model ≥ 5% | 4209 | 46 | +38% | -72% | -70% | -67% |
| Volatility model ≥ 10% | 2432 | 28 | +65% | -62% | -61% | -57% |
| Momentum model ≥ 2% | 6408 | 51 | -3% | -78% | -77% | -74% |
| Momentum model ≥ 5% | 3931 | 37 | +22% | -74% | -73% | -69% |
| Momentum model ≥ 10% | 2580 | 25 | +36% | -66% | -65% | -61% |
| Mean-reversion model ≥ 2% | 13348 | 92 | -24% | -82% | -82% | -79% |
| Mean-reversion model ≥ 5% | 9339 | 78 | -7% | -80% | -79% | -76% |
| Mean-reversion model ≥ 10% | 6243 | 56 | +2% | -77% | -77% | -74% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 32482 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 12824 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 8312 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 53618 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 205 | 0% | -$3,669.25 | -56% | — |
| Sell at 2¢ | 2137 | 4% | -$5,703.63 | -87% | 47 sec |
| Sell at 3¢ | 1455 | 3% | -$5,691.80 | -87% | 48 sec |
| Sell at 5¢ | 1012 | 2% | -$5,573.45 | -85% | 63 sec |
| Sell at 10¢ | 611 | 1% | -$5,346.84 | -82% | 65 sec |
| Sell at 25¢ | 325 | 1% | -$4,959.50 | -76% | 82 sec |
| Sell at 50¢ | 212 | 0% | -$4,492.25 | -69% | 1.7 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 12 | 0 | 25% | 17% | -100% | -57% | -35% |
| 5–10 min | 2686 | 13 | 11% | 4% | -54% | -81% | -83% |
| 2–5 min | 17354 | 94 | 7% | 3% | -47% | -87% | -87% |
| 1–2 min | 13531 | 45 | 3% | 2% | -63% | -92% | -92% |
| Under 1 min | 20035 | 53 | 1% | 0% | -62% | -85% | -85% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 3636 | 17 | 5% | 3% | -39% | -88% | -87% |
| SOL | 3632 | 16 | 4% | 2% | -44% | -87% | -86% |
| HYPE | 3625 | 11 | 5% | 2% | -62% | -89% | -88% |
| BNB | 3617 | 19 | 5% | 2% | -34% | -86% | -85% |
| DOGE | 3613 | 8 | 4% | 2% | -72% | -90% | -90% |
| ETH | 3607 | 15 | 7% | 3% | -48% | -82% | -81% |
| NEAR | 3588 | 17 | 5% | 2% | -39% | -85% | -85% |
| BTC | 3588 | 17 | 5% | 2% | -35% | -87% | -88% |
| XRP | 3576 | 13 | 3% | 1% | -55% | -89% | -89% |
| GOLD | 1933 | 5 | 5% | 2% | -68% | -81% | -83% |
| WTI | 1914 | 6 | 4% | 2% | -62% | -91% | -92% |
| SILVER | 1884 | 8 | 5% | 2% | -50% | -83% | -83% |
| PLATINUM | 1713 | 4 | 3% | 1% | -78% | -96% | -95% |
| EURUSD | 1649 | 5 | 2% | 1% | -72% | -90% | -89% |
| COPPER | 1602 | 6 | 2% | 1% | -65% | -74% | -73% |
| GBPUSD | 1570 | 6 | 2% | 1% | -64% | -96% | -96% |
| NATGAS | 1568 | 8 | 2% | 1% | -52% | -79% | -78% |
| USDJPY | 1553 | 6 | 2% | 1% | -64% | -97% | -96% |
| PALLADIUM | 1540 | 4 | 1% | 1% | -76% | -92% | -92% |
| AUDUSD | 1107 | 6 | 2% | 1% | -49% | -88% | -88% |
| USDCAD | 1076 | 0 | 3% | 1% | -100% | -96% | -96% |
| BRENT | 670 | 0 | 2% | 1% | -100% | -97% | -97% |
| 10YRRATE | 353 | 2 | 4% | 2% | -47% | -66% | -64% |
| 2YRRATE | 338 | 4 | 4% | 2% | +10% | -38% | -36% |
| 30YRRATE | 332 | 0 | 2% | 1% | -100% | -96% | -94% |
| 5YRRATE | 311 | 2 | 4% | 2% | -40% | -93% | -95% |
| INX | 23 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 27163 | 108 | 4% | 2% | -54% | -88% | -87% |
| DOWN (bought NO) | 26455 | 97 | 4% | 2% | -58% | -86% | -87% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 5169 | 25 | 2% | 1% | -14% | -77% | -76% |
| 0.05–0.1% | 5518 | 20 | 3% | 2% | -45% | -91% | -91% |
| 0.1–0.2% | 8345 | 30 | 5% | 2% | -55% | -89% | -89% |
| 0.2–0.5% | 9742 | 41 | 6% | 3% | -53% | -87% | -86% |
| Over 0.5% | 3700 | 17 | 7% | 3% | -52% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 13236 | 43 | 4% | 2% | -63% | -88% | -88% |
| Morning (6am–12pm) | 12972 | 60 | 4% | 2% | -47% | -85% | -84% |
| Afternoon (12–6pm) | 12822 | 57 | 4% | 2% | -48% | -86% | -86% |
| Evening (6pm–12am) | 14588 | 45 | 4% | 2% | -65% | -90% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,863 |
| Time from buy to best bounce (bounced bets) | 51 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/11 7:14:41 AM | USDJPY | UP | 18 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/11 7:14:09 AM | BRENT | DOWN | 51 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/11 7:14:09 AM | XRP | UP | 51 sec | -0.179% | 0¢ | ❌ Lost | $0.00 |
| 11/11 7:13:52 AM | BNB | UP | 67 sec | -0.126% | 0¢ | ❌ Lost | -$0.15 |
| 11/11 7:13:52 AM | DOGE | UP | 67 sec | -0.131% | 0¢ | ❌ Lost | -$0.15 |
| 11/11 7:13:20 AM | WTI | DOWN | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/11 7:13:20 AM | NATGAS | DOWN | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/11 7:13:20 AM | USDCAD | DOWN | 1.6 min | — | 38¢ | ❌ Lost | -$0.15 |
| 11/11 7:13:03 AM | BTC | UP | 1.9 min | -0.165% | 1¢ | ❌ Lost | -$0.15 |
| 11/11 7:12:15 AM | EURUSD | UP | 2.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/11 7:12:15 AM | HYPE | UP | 2.7 min | -0.400% | 1¢ | ❌ Lost | -$0.15 |
| 11/11 7:11:59 AM | NEAR | UP | 3.0 min | -0.832% | 1¢ | ❌ Lost | -$0.15 |
| 11/11 7:11:59 AM | GBPUSD | UP | 3.0 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/11 7:11:12 AM | SOL | UP | 3.8 min | -0.421% | 2¢ | ❌ Lost | -$0.15 |
| 11/11 7:11:12 AM | ZEC | UP | 3.8 min | -0.977% | 1¢ | ❌ Lost | -$0.15 |
| 11/11 7:11:12 AM | COPPER | UP | 3.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/11 7:10:52 AM | ETH | UP | 4.1 min | -0.440% | 1¢ | ❌ Lost | -$0.15 |
| 11/11 7:10:36 AM | PALLADIUM | UP | 4.4 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/11 7:10:04 AM | GOLD | UP | 4.9 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/11 7:10:04 AM | SILVER | UP | 4.9 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/11 7:09:15 AM | PLATINUM | UP | 5.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/11 6:59:58 AM | PLATINUM | DOWN | 2 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/11 6:59:26 AM | NATGAS | DOWN | 34 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/11 6:59:26 AM | AUDUSD | DOWN | 34 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/11 6:59:11 AM | BTC | DOWN | 48 sec | +0.060% | 1¢ | ❌ Lost | -$0.15 |
| 11/11 6:58:55 AM | SILVER | DOWN | 64 sec | — | 0¢ | ❌ Lost | $0.00 |
| 11/11 6:58:39 AM | PALLADIUM | DOWN | 80 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/11 6:58:39 AM | USDCAD | DOWN | 80 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/11 6:58:23 AM | COPPER | DOWN | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/11 6:58:07 AM | GOLD | DOWN | 1.9 min | — | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
