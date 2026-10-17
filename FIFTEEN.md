# 15-Minute 1¢ Study

*Updated Sat Oct 17, 6:54 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 1752 finished bets | 1% | $71.45 | +37% | +4.08¢ | $30.75 / $40.70 |

*Expect about **91 buys a day** (~$13.65/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 1621 | $33.75 | +19% |
| Momentum model ≥ 2%, hold to the close | 2726 | -$22.65 | -7% |
| Volatility model ≥ 5%, sell at 50¢ | 1752 | -$31.05 | -16% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 21834 | 21823 | 82 (0%) | 1.07% | -$1,504.75 (-57%) | Hold to the close: -$1,504.75 (-57%) |

*In play or awaiting result: 10. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 14099 | 4.5% | 0.4% (56) | -658% | ❌ Worse |
| Momentum model | 14099 | 4.5% | 0.4% (56) | -680% | ❌ Worse |
| Mean-reversion model | 14099 | 7.5% | 0.4% (56) | -790% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 14099 | 56 | -50% | -88% | -88% | -86% |
| Volatility model ≥ 2% | 3179 | 24 | -13% | -79% | -78% | -75% |
| Volatility model ≥ 5% | 1752 | 19 | +37% | -74% | -73% | -70% |
| Volatility model ≥ 10% | 1026 | 11 | +52% | -67% | -66% | -64% |
| Momentum model ≥ 2% | 2726 | 21 | -7% | -81% | -81% | -78% |
| Momentum model ≥ 5% | 1621 | 15 | +19% | -78% | -78% | -74% |
| Momentum model ≥ 10% | 1077 | 10 | +30% | -74% | -73% | -68% |
| Mean-reversion model ≥ 2% | 5359 | 35 | -29% | -84% | -84% | -81% |
| Mean-reversion model ≥ 5% | 3697 | 27 | -19% | -82% | -82% | -78% |
| Mean-reversion model ≥ 10% | 2435 | 16 | -25% | -80% | -80% | -78% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 14297 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 5309 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 2217 | 1% | 1% | 1% | 1% | 0% | 0% |
| **All** | 21823 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 82 | 0% | -$1,504.75 | -57% | — |
| Sell at 2¢ | 787 | 4% | -$2,350.13 | -89% | 37 sec |
| Sell at 3¢ | 528 | 2% | -$2,348.83 | -89% | 47 sec |
| Sell at 5¢ | 380 | 2% | -$2,307.75 | -87% | 50 sec |
| Sell at 10¢ | 229 | 1% | -$2,226.76 | -84% | 63 sec |
| Sell at 25¢ | 129 | 1% | -$2,057.76 | -78% | 79 sec |
| Sell at 50¢ | 85 | 0% | -$1,841.00 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 749 | 5 | 10% | 3% | -37% | -82% | -85% |
| 2–5 min | 7050 | 38 | 7% | 3% | -47% | -88% | -87% |
| 1–2 min | 5672 | 20 | 3% | 2% | -62% | -92% | -92% |
| Under 1 min | 8348 | 19 | 1% | 0% | -67% | -88% | -88% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 1607 | 11 | 4% | 2% | -15% | -90% | -90% |
| HYPE | 1602 | 6 | 4% | 2% | -54% | -90% | -88% |
| ETH | 1592 | 8 | 6% | 3% | -39% | -87% | -86% |
| DOGE | 1591 | 2 | 4% | 2% | -84% | -90% | -90% |
| BNB | 1591 | 6 | 5% | 2% | -54% | -89% | -89% |
| SOL | 1585 | 2 | 4% | 2% | -84% | -92% | -91% |
| XRP | 1579 | 7 | 3% | 1% | -45% | -86% | -87% |
| NEAR | 1576 | 8 | 6% | 3% | -34% | -78% | -78% |
| BTC | 1574 | 8 | 5% | 2% | -32% | -88% | -91% |
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
| UP (bought YES) | 11017 | 41 | 4% | 2% | -57% | -89% | -88% |
| DOWN (bought NO) | 10806 | 41 | 4% | 2% | -56% | -88% | -89% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 2424 | 12 | 2% | 1% | -17% | -81% | -80% |
| 0.05–0.1% | 2478 | 7 | 3% | 1% | -59% | -91% | -91% |
| 0.1–0.2% | 3594 | 12 | 5% | 2% | -59% | -90% | -89% |
| 0.2–0.5% | 4159 | 21 | 6% | 3% | -44% | -88% | -88% |
| Over 0.5% | 1639 | 6 | 6% | 3% | -62% | -88% | -89% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 5566 | 22 | 4% | 2% | -55% | -87% | -88% |
| Morning (6am–12pm) | 5130 | 27 | 4% | 2% | -40% | -87% | -86% |
| Afternoon (12–6pm) | 5104 | 16 | 3% | 1% | -63% | -88% | -89% |
| Evening (6pm–12am) | 6023 | 17 | 3% | 2% | -68% | -92% | -91% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,531 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/17 6:54:52 AM | XRP | UP | 5.1 min | -0.416% | — | In play | — |
| 10/17 6:54:19 AM | BNB | UP | 5.7 min | -0.175% | — | In play | — |
| 10/17 6:54:19 AM | DOGE | UP | 5.7 min | -0.615% | — | In play | — |
| 10/17 6:53:30 AM | ZEC | UP | 6.5 min | -0.754% | — | In play | — |
| 10/17 6:44:41 AM | DOGE | UP | 19 sec | -0.050% | 0¢ | ❌ Lost | $0.00 |
| 10/17 6:44:25 AM | XRP | UP | 35 sec | -0.077% | 0¢ | ❌ Lost | $0.00 |
| 10/17 6:44:25 AM | HYPE | UP | 35 sec | -0.025% | 0¢ | ❌ Lost | -$0.15 |
| 10/17 6:44:25 AM | BTC | UP | 35 sec | -0.024% | 1¢ | ❌ Lost | -$0.15 |
| 10/17 6:44:10 AM | NEAR | UP | 49 sec | -0.253% | 0¢ | ❌ Lost | -$0.15 |
| 10/17 6:43:37 AM | BNB | UP | 82 sec | -0.071% | 8¢ | ❌ Lost | $0.00 |
| 10/17 6:43:05 AM | ETH | UP | 1.9 min | -0.088% | 1¢ | ❌ Lost | -$0.15 |
| 10/17 6:42:48 AM | SOL | UP | 2.2 min | -0.126% | 1¢ | ❌ Lost | -$0.15 |
| 10/17 6:42:32 AM | ZEC | UP | 2.5 min | -0.343% | 1¢ | ❌ Lost | -$0.15 |
| 10/17 6:29:30 AM | ZEC | UP | 30 sec | -0.038% | 0¢ | ❌ Lost | -$0.15 |
| 10/17 6:29:30 AM | NEAR | UP | 30 sec | -0.124% | 0¢ | ❌ Lost | $0.00 |
| 10/17 6:29:30 AM | BTC | UP | 30 sec | -0.017% | 0¢ | ❌ Lost | -$0.15 |
| 10/17 6:29:30 AM | BNB | UP | 30 sec | -0.092% | 0¢ | ❌ Lost | $0.00 |
| 10/17 6:27:34 AM | XRP | UP | 2.4 min | -0.223% | 1¢ | ❌ Lost | -$0.15 |
| 10/17 6:27:03 AM | HYPE | DOWN | 2.9 min | +0.213% | 2¢ | ❌ Lost | -$0.15 |
| 10/17 6:25:09 AM | DOGE | UP | 4.8 min | -0.305% | 8¢ | ❌ Lost | -$0.15 |
| 10/17 6:23:47 AM | ETH | UP | 6.2 min | -0.157% | 33¢ | ❌ Lost | -$0.15 |
| 10/17 6:14:27 AM | BTC | UP | 33 sec | -0.028% | 1¢ | ❌ Lost | -$0.15 |
| 10/17 6:14:10 AM | ETH | UP | 49 sec | -0.056% | 0¢ | ❌ Lost | $0.00 |
| 10/17 6:13:03 AM | BNB | UP | 1.9 min | -0.140% | 1¢ | ❌ Lost | -$0.15 |
| 10/17 6:12:14 AM | ZEC | UP | 2.8 min | -0.303% | 1¢ | ❌ Lost | -$0.15 |
| 10/17 6:12:14 AM | HYPE | UP | 2.8 min | -0.242% | 1¢ | ❌ Lost | -$0.15 |
| 10/17 6:11:40 AM | DOGE | UP | 3.3 min | -0.206% | 1¢ | ❌ Lost | -$0.15 |
| 10/17 6:10:20 AM | NEAR | UP | 4.7 min | -0.960% | 1¢ | ❌ Lost | -$0.15 |
| 10/17 6:10:04 AM | XRP | UP | 4.9 min | -0.207% | 3¢ | ❌ Lost | -$0.15 |
| 10/17 6:08:27 AM | SOL | UP | 6.5 min | -0.289% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
