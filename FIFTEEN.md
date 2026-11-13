# 15-Minute 1¢ Study

*Updated Fri Nov 13, 11:46 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 4287 finished bets | 1% | $168.20 | +35% | +3.92¢ | $80.50 / $87.70 |

*Expect about **92 buys a day** (~$13.83/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 4030 | $95.20 | +22% |
| Volatility model ≥ 2%, hold to the close | 7920 | $26.75 | +3% |
| Momentum model ≥ 2%, hold to the close | 6576 | -$27.70 | -4% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 56190 | 56169 | 213 (0%) | 1.07% | -$3,872.85 (-56%) | Hold to the close: -$3,872.85 (-56%) |

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
| Volatility model | 33474 | 4.7% | 0.4% (134) | -667% | ❌ Worse |
| Momentum model | 33474 | 4.6% | 0.4% (134) | -693% | ❌ Worse |
| Mean-reversion model | 33474 | 8.0% | 0.4% (134) | -809% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 33474 | 134 | -49% | -87% | -87% | -85% |
| Volatility model ≥ 2% | 7920 | 70 | +3% | -77% | -76% | -72% |
| Volatility model ≥ 5% | 4287 | 46 | +35% | -72% | -71% | -67% |
| Volatility model ≥ 10% | 2484 | 28 | +62% | -63% | -61% | -58% |
| Momentum model ≥ 2% | 6576 | 52 | -4% | -78% | -78% | -74% |
| Momentum model ≥ 5% | 4030 | 38 | +22% | -74% | -74% | -70% |
| Momentum model ≥ 10% | 2644 | 25 | +33% | -66% | -66% | -61% |
| Mean-reversion model ≥ 2% | 13780 | 94 | -25% | -82% | -82% | -79% |
| Mean-reversion model ≥ 5% | 9610 | 79 | -9% | -80% | -79% | -77% |
| Mean-reversion model ≥ 10% | 6404 | 56 | -1% | -77% | -77% | -74% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 33679 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 13551 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 8939 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 56169 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 213 | 0% | -$3,872.85 | -56% | — |
| Sell at 2¢ | 2237 | 4% | -$5,979.23 | -87% | 47 sec |
| Sell at 3¢ | 1515 | 3% | -$5,970.00 | -87% | 48 sec |
| Sell at 5¢ | 1042 | 2% | -$5,855.55 | -85% | 63 sec |
| Sell at 10¢ | 633 | 1% | -$5,619.62 | -82% | 65 sec |
| Sell at 25¢ | 331 | 1% | -$5,227.24 | -76% | 82 sec |
| Sell at 50¢ | 218 | 0% | -$4,739.35 | -69% | 1.7 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 13 | 0 | 31% | 23% | -100% | -47% | -20% |
| 5–10 min | 2801 | 13 | 11% | 4% | -56% | -81% | -82% |
| 2–5 min | 18097 | 98 | 7% | 3% | -47% | -87% | -87% |
| 1–2 min | 14169 | 46 | 3% | 2% | -64% | -92% | -92% |
| Under 1 min | 21089 | 56 | 1% | 0% | -62% | -85% | -85% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 3770 | 17 | 5% | 2% | -41% | -88% | -87% |
| SOL | 3766 | 16 | 4% | 2% | -46% | -87% | -87% |
| HYPE | 3760 | 11 | 5% | 2% | -63% | -89% | -88% |
| DOGE | 3746 | 8 | 4% | 2% | -73% | -90% | -90% |
| BNB | 3746 | 19 | 5% | 2% | -36% | -86% | -85% |
| ETH | 3741 | 16 | 7% | 3% | -47% | -81% | -81% |
| NEAR | 3721 | 17 | 5% | 2% | -41% | -85% | -85% |
| BTC | 3721 | 18 | 5% | 2% | -34% | -87% | -88% |
| XRP | 3708 | 14 | 3% | 1% | -53% | -89% | -89% |
| GOLD | 2037 | 5 | 5% | 2% | -70% | -82% | -84% |
| WTI | 2010 | 7 | 4% | 2% | -58% | -91% | -92% |
| SILVER | 1977 | 9 | 5% | 2% | -46% | -83% | -83% |
| PLATINUM | 1802 | 4 | 3% | 1% | -79% | -95% | -95% |
| EURUSD | 1748 | 6 | 3% | 1% | -68% | -90% | -90% |
| COPPER | 1689 | 6 | 2% | 1% | -67% | -75% | -75% |
| GBPUSD | 1674 | 6 | 2% | 1% | -67% | -96% | -96% |
| NATGAS | 1661 | 9 | 2% | 1% | -49% | -74% | -73% |
| USDJPY | 1637 | 6 | 2% | 1% | -66% | -97% | -96% |
| PALLADIUM | 1617 | 4 | 1% | 0% | -77% | -92% | -92% |
| AUDUSD | 1192 | 6 | 2% | 1% | -53% | -89% | -89% |
| USDCAD | 1157 | 1 | 3% | 1% | -92% | -96% | -96% |
| BRENT | 758 | 0 | 2% | 1% | -100% | -97% | -97% |
| 10YRRATE | 393 | 2 | 4% | 2% | -53% | -70% | -68% |
| 2YRRATE | 374 | 4 | 4% | 2% | -0% | -44% | -42% |
| 30YRRATE | 372 | 0 | 2% | 1% | -100% | -96% | -94% |
| 5YRRATE | 346 | 2 | 4% | 2% | -46% | -93% | -95% |
| INX | 46 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 28536 | 110 | 4% | 2% | -56% | -88% | -88% |
| DOWN (bought NO) | 27633 | 103 | 4% | 2% | -57% | -86% | -86% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 5280 | 25 | 2% | 1% | -16% | -77% | -77% |
| 0.05–0.1% | 5676 | 20 | 3% | 2% | -46% | -91% | -91% |
| 0.1–0.2% | 8590 | 31 | 5% | 2% | -54% | -89% | -89% |
| 0.2–0.5% | 10209 | 42 | 6% | 3% | -54% | -87% | -86% |
| Over 0.5% | 3916 | 18 | 7% | 3% | -52% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 13733 | 44 | 4% | 2% | -63% | -88% | -88% |
| Morning (6am–12pm) | 13619 | 63 | 4% | 2% | -47% | -85% | -85% |
| Afternoon (12–6pm) | 13453 | 59 | 4% | 2% | -49% | -86% | -87% |
| Evening (6pm–12am) | 15364 | 47 | 4% | 2% | -65% | -89% | -89% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,806 |
| Time from buy to best bounce (bounced bets) | 50 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/13 11:44:58 AM | 2YRRATE | DOWN | 1 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/13 11:44:58 AM | 30YRRATE | DOWN | 1 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/13 11:44:58 AM | HYPE | DOWN | 1 sec | +0.006% | 0¢ | ❌ Lost | $0.00 |
| 11/13 11:44:42 AM | AUDUSD | UP | 17 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/13 11:44:42 AM | 10YRRATE | DOWN | 17 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/13 11:44:42 AM | PALLADIUM | UP | 17 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/13 11:44:27 AM | ZEC | DOWN | 32 sec | +0.031% | 0¢ | ❌ Lost | $0.00 |
| 11/13 11:44:27 AM | 5YRRATE | DOWN | 32 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/13 11:44:08 AM | DOGE | UP | 51 sec | -0.131% | 1¢ | ❌ Lost | -$0.15 |
| 11/13 11:44:08 AM | XRP | DOWN | 51 sec | +0.088% | 1¢ | ❌ Lost | -$0.15 |
| 11/13 11:43:52 AM | GOLD | UP | 67 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 11/13 11:43:52 AM | COPPER | UP | 67 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/13 11:43:52 AM | INX | DOWN | 67 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/13 11:43:21 AM | NEAR | DOWN | 1.6 min | +0.309% | 1¢ | ❌ Lost | -$0.15 |
| 11/13 11:43:21 AM | ETH | UP | 1.6 min | -0.108% | 2¢ | ❌ Lost | -$0.15 |
| 11/13 11:42:46 AM | SILVER | UP | 2.2 min | — | 0¢ | ❌ Lost | $0.00 |
| 11/13 11:42:30 AM | SOL | UP | 2.5 min | -0.238% | 1¢ | ❌ Lost | -$0.15 |
| 11/13 11:42:15 AM | WTI | DOWN | 2.7 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/13 11:42:15 AM | BTC | UP | 2.7 min | -0.173% | 1¢ | ❌ Lost | -$0.15 |
| 11/13 11:42:15 AM | USDCAD | DOWN | 2.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/13 11:41:56 AM | GBPUSD | UP | 3.1 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/13 11:41:56 AM | BNB | UP | 3.1 min | -0.212% | 1¢ | ❌ Lost | -$0.15 |
| 11/13 11:40:20 AM | EURUSD | UP | 4.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/13 11:40:20 AM | USDJPY | DOWN | 4.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/13 11:40:03 AM | BRENT | DOWN | 5.0 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/13 11:29:49 AM | 10YRRATE | UP | 10 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/13 11:29:49 AM | GBPUSD | DOWN | 10 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/13 11:29:49 AM | XRP | UP | 10 sec | -0.127% | 0¢ | ❌ Lost | $0.00 |
| 11/13 11:29:49 AM | GOLD | UP | 10 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/13 11:29:49 AM | PALLADIUM | UP | 10 sec | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
