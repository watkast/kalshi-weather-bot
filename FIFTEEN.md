# 15-Minute 1¢ Study

*Updated Sat Oct 17, 9:32 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 1767 finished bets | 1% | $69.35 | +35% | +3.92¢ | $30.00 / $39.35 |

*Expect about **91 buys a day** (~$13.68/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 1630 | $32.55 | +18% |
| Momentum model ≥ 2%, hold to the close | 2740 | -$24.60 | -8% |
| Volatility model ≥ 5%, sell at 50¢ | 1767 | -$33.15 | -17% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 21927 | 21920 | 82 (0%) | 1.07% | -$1,516.90 (-57%) | Hold to the close: -$1,516.90 (-57%) |

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
| Volatility model | 14196 | 4.5% | 0.4% (56) | -657% | ❌ Worse |
| Momentum model | 14196 | 4.4% | 0.4% (56) | -679% | ❌ Worse |
| Mean-reversion model | 14196 | 7.5% | 0.4% (56) | -791% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 14196 | 56 | -51% | -88% | -88% | -86% |
| Volatility model ≥ 2% | 3203 | 24 | -14% | -79% | -79% | -75% |
| Volatility model ≥ 5% | 1767 | 19 | +35% | -75% | -74% | -70% |
| Volatility model ≥ 10% | 1032 | 11 | +51% | -67% | -67% | -64% |
| Momentum model ≥ 2% | 2740 | 21 | -8% | -81% | -81% | -78% |
| Momentum model ≥ 5% | 1630 | 15 | +18% | -78% | -78% | -74% |
| Momentum model ≥ 10% | 1081 | 10 | +29% | -74% | -73% | -68% |
| Mean-reversion model ≥ 2% | 5411 | 35 | -29% | -84% | -84% | -81% |
| Mean-reversion model ≥ 5% | 3736 | 27 | -20% | -82% | -82% | -79% |
| Mean-reversion model ≥ 10% | 2461 | 16 | -26% | -80% | -81% | -78% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 14394 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 5309 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 2217 | 1% | 1% | 1% | 1% | 0% | 0% |
| **All** | 21920 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 82 | 0% | -$1,516.90 | -57% | — |
| Sell at 2¢ | 790 | 4% | -$2,361.50 | -89% | 37 sec |
| Sell at 3¢ | 531 | 2% | -$2,359.81 | -89% | 47 sec |
| Sell at 5¢ | 382 | 2% | -$2,318.60 | -87% | 50 sec |
| Sell at 10¢ | 231 | 1% | -$2,236.29 | -84% | 63 sec |
| Sell at 25¢ | 130 | 1% | -$2,066.60 | -78% | 80 sec |
| Sell at 50¢ | 85 | 0% | -$1,853.15 | -70% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 760 | 5 | 10% | 3% | -38% | -82% | -85% |
| 2–5 min | 7096 | 38 | 7% | 3% | -47% | -88% | -88% |
| 1–2 min | 5690 | 20 | 3% | 2% | -62% | -92% | -92% |
| Under 1 min | 8370 | 19 | 1% | 0% | -67% | -88% | -88% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 1618 | 11 | 4% | 2% | -15% | -90% | -90% |
| HYPE | 1612 | 6 | 5% | 2% | -54% | -90% | -88% |
| ETH | 1603 | 8 | 6% | 3% | -40% | -87% | -86% |
| BNB | 1602 | 6 | 5% | 2% | -54% | -89% | -89% |
| DOGE | 1601 | 2 | 4% | 2% | -84% | -91% | -90% |
| SOL | 1596 | 2 | 4% | 2% | -85% | -92% | -91% |
| XRP | 1590 | 7 | 3% | 1% | -46% | -86% | -87% |
| NEAR | 1587 | 8 | 6% | 3% | -34% | -78% | -78% |
| BTC | 1585 | 8 | 5% | 2% | -32% | -88% | -91% |
| GOLD | 864 | 1 | 3% | 1% | -86% | -92% | -94% |
| SILVER | 841 | 4 | 3% | 1% | -45% | -80% | -80% |
| WTI | 821 | 3 | 3% | 1% | -57% | -94% | -95% |
| COPPER | 735 | 2 | 2% | 1% | -75% | -84% | -84% |
| PLATINUM | 722 | 0 | 1% | 0% | -100% | -99% | -99% |
| NATGAS | 667 | 5 | 2% | 2% | -30% | -82% | -81% |
| PALLADIUM | 659 | 2 | 1% | 0% | -72% | -84% | -84% |
| EURUSD | 659 | 3 | 3% | 1% | -58% | -81% | -81% |
| GBPUSD | 615 | 1 | 2% | 1% | -85% | -97% | -97% |
| USDJPY | 574 | 3 | 1% | 1% | -51% | -99% | -98% |
| AUDUSD | 200 | 0 | 0% | 0% | -100% | -99% | -99% |
| USDCAD | 169 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 11070 | 41 | 4% | 2% | -57% | -89% | -88% |
| DOWN (bought NO) | 10850 | 41 | 4% | 2% | -56% | -88% | -89% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 2444 | 12 | 2% | 1% | -18% | -81% | -80% |
| 0.05–0.1% | 2491 | 7 | 3% | 1% | -59% | -91% | -91% |
| 0.1–0.2% | 3622 | 12 | 5% | 2% | -59% | -90% | -89% |
| 0.2–0.5% | 4182 | 21 | 6% | 3% | -45% | -88% | -88% |
| Over 0.5% | 1652 | 6 | 6% | 3% | -62% | -88% | -89% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 5566 | 22 | 4% | 2% | -55% | -87% | -88% |
| Morning (6am–12pm) | 5227 | 27 | 4% | 2% | -41% | -87% | -86% |
| Afternoon (12–6pm) | 5104 | 16 | 3% | 1% | -63% | -88% | -89% |
| Evening (6pm–12am) | 6023 | 17 | 3% | 2% | -68% | -92% | -91% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,560 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/17 9:27:54 AM | BTC | UP | 2.1 min | -0.119% | 1¢ | ❌ Lost | -$0.15 |
| 10/17 9:26:34 AM | HYPE | UP | 3.4 min | -0.346% | 1¢ | ❌ Lost | -$0.15 |
| 10/17 9:25:46 AM | XRP | UP | 4.2 min | -0.300% | 1¢ | ❌ Lost | -$0.15 |
| 10/17 9:25:46 AM | BNB | UP | 4.2 min | -0.348% | 1¢ | ❌ Lost | -$0.15 |
| 10/17 9:25:30 AM | NEAR | UP | 4.5 min | -1.185% | 1¢ | ❌ Lost | -$0.15 |
| 10/17 9:25:14 AM | SOL | UP | 4.8 min | -0.344% | 1¢ | ❌ Lost | -$0.15 |
| 10/17 9:24:42 AM | DOGE | UP | 5.3 min | -0.491% | 1¢ | ❌ Lost | -$0.15 |
| 10/17 9:24:10 AM | ZEC | UP | 5.8 min | -1.171% | 1¢ | ❌ Lost | -$0.15 |
| 10/17 9:23:54 AM | ETH | UP | 6.1 min | -0.296% | 1¢ | ❌ Lost | -$0.15 |
| 10/17 9:14:54 AM | BTC | DOWN | 5 sec | +0.013% | 0¢ | ❌ Lost | $0.00 |
| 10/17 9:14:54 AM | NEAR | UP | 5 sec | -0.092% | 0¢ | ❌ Lost | $0.00 |
| 10/17 9:12:11 AM | ZEC | UP | 2.8 min | -0.425% | 0¢ | ❌ Lost | $0.00 |
| 10/17 9:10:36 AM | SOL | UP | 4.4 min | -0.239% | 1¢ | ❌ Lost | -$0.15 |
| 10/17 9:10:20 AM | DOGE | UP | 4.7 min | -0.305% | 1¢ | ❌ Lost | -$0.15 |
| 10/17 9:10:20 AM | ETH | UP | 4.7 min | -0.174% | 1¢ | ❌ Lost | -$0.15 |
| 10/17 9:10:20 AM | BNB | UP | 4.7 min | -0.172% | 1¢ | ❌ Lost | -$0.15 |
| 10/17 9:08:28 AM | XRP | UP | 6.5 min | -0.323% | 1¢ | ❌ Lost | -$0.15 |
| 10/17 8:59:44 AM | BTC | DOWN | 16 sec | +0.015% | 0¢ | ❌ Lost | $0.00 |
| 10/17 8:59:28 AM | ETH | DOWN | 32 sec | +0.031% | 0¢ | ❌ Lost | $0.00 |
| 10/17 8:59:12 AM | DOGE | UP | 48 sec | -0.075% | 1¢ | ❌ Lost | -$0.15 |
| 10/17 8:58:56 AM | ZEC | UP | 64 sec | -0.269% | 0¢ | ❌ Lost | $0.00 |
| 10/17 8:58:40 AM | HYPE | DOWN | 80 sec | +0.057% | 0¢ | ❌ Lost | -$0.15 |
| 10/17 8:58:24 AM | SOL | DOWN | 1.6 min | +0.069% | 1¢ | ❌ Lost | -$0.15 |
| 10/17 8:58:24 AM | XRP | DOWN | 1.6 min | +0.069% | 1¢ | ❌ Lost | -$0.15 |
| 10/17 8:57:20 AM | NEAR | UP | 2.6 min | -0.594% | 1¢ | ❌ Lost | -$0.15 |
| 10/17 8:56:32 AM | BNB | UP | 3.5 min | -0.157% | 1¢ | ❌ Lost | -$0.15 |
| 10/17 8:44:46 AM | XRP | UP | 14 sec | -0.046% | 0¢ | ❌ Lost | -$0.15 |
| 10/17 8:44:30 AM | BTC | DOWN | 30 sec | +0.017% | 0¢ | ❌ Lost | $0.00 |
| 10/17 8:44:14 AM | HYPE | UP | 46 sec | -0.098% | 0¢ | ❌ Lost | -$0.15 |
| 10/17 8:43:24 AM | SOL | UP | 1.6 min | -0.103% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
