# 15-Minute 1¢ Study

*Updated Tue Oct 13, 2:47 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 1248 finished bets | 1% | $45.35 | +33% | +3.63¢ | $30.95 / $14.40 |

*Expect about **83 buys a day** (~$12.41/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 1191 | $25.60 | +20% |
| 5+ min left, hold to the close | 455 | -$11.35 | -17% |
| Volatility model ≥ 5%, sell at 50¢ | 1248 | -$13.65 | -10% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 16400 | 16393 | 63 (0%) | 1.07% | -$1,102.35 (-56%) | Hold to the close: -$1,102.35 (-56%) |

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
| Volatility model | 10824 | 4.5% | 0.4% (46) | -659% | ❌ Worse |
| Momentum model | 10824 | 4.5% | 0.4% (46) | -686% | ❌ Worse |
| Mean-reversion model | 10824 | 7.2% | 0.4% (46) | -770% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 10824 | 46 | -47% | -88% | -88% | -86% |
| Volatility model ≥ 2% | 2213 | 18 | -6% | -78% | -78% | -75% |
| Volatility model ≥ 5% | 1248 | 13 | +33% | -73% | -71% | -69% |
| Volatility model ≥ 10% | 780 | 9 | +65% | -63% | -63% | -59% |
| Momentum model ≥ 2% | 1940 | 15 | -6% | -79% | -80% | -78% |
| Momentum model ≥ 5% | 1191 | 11 | +20% | -76% | -76% | -73% |
| Momentum model ≥ 10% | 816 | 8 | +39% | -69% | -69% | -64% |
| Mean-reversion model ≥ 2% | 3857 | 27 | -24% | -85% | -85% | -82% |
| Mean-reversion model ≥ 5% | 2638 | 20 | -16% | -83% | -83% | -79% |
| Mean-reversion model ≥ 10% | 1745 | 14 | -7% | -81% | -81% | -78% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 11022 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 3944 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 1427 | 2% | 1% | 1% | 1% | 0% | 0% |
| **All** | 16393 | 3% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 63 | 0% | -$1,102.35 | -56% | — |
| Sell at 2¢ | 553 | 3% | -$1,798.57 | -91% | 33 sec |
| Sell at 3¢ | 365 | 2% | -$1,800.00 | -91% | 46 sec |
| Sell at 5¢ | 264 | 2% | -$1,770.75 | -89% | 49 sec |
| Sell at 10¢ | 174 | 1% | -$1,686.41 | -85% | 63 sec |
| Sell at 25¢ | 99 | 1% | -$1,558.66 | -79% | 79 sec |
| Sell at 50¢ | 64 | 0% | -$1,398.35 | -70% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 451 | 4 | 11% | 3% | -16% | -81% | -87% |
| 2–5 min | 5296 | 32 | 6% | 3% | -41% | -88% | -89% |
| 1–2 min | 4324 | 16 | 3% | 2% | -60% | -94% | -94% |
| Under 1 min | 6318 | 11 | 1% | 0% | -75% | -91% | -91% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 1237 | 7 | 4% | 2% | -30% | -90% | -90% |
| HYPE | 1234 | 4 | 4% | 2% | -60% | -90% | -89% |
| DOGE | 1228 | 2 | 4% | 2% | -80% | -91% | -91% |
| BNB | 1227 | 5 | 4% | 1% | -50% | -91% | -91% |
| ETH | 1226 | 8 | 5% | 2% | -20% | -90% | -89% |
| SOL | 1226 | 2 | 3% | 1% | -80% | -93% | -92% |
| BTC | 1218 | 6 | 5% | 2% | -35% | -88% | -91% |
| NEAR | 1213 | 7 | 5% | 2% | -25% | -77% | -77% |
| XRP | 1213 | 7 | 2% | 1% | -29% | -85% | -85% |
| GOLD | 648 | 0 | 3% | 1% | -100% | -93% | -94% |
| SILVER | 631 | 1 | 3% | 1% | -82% | -94% | -94% |
| WTI | 603 | 3 | 3% | 1% | -43% | -94% | -96% |
| COPPER | 565 | 0 | 1% | 1% | -100% | -98% | -97% |
| PLATINUM | 523 | 0 | 0% | 0% | -100% | -100% | -100% |
| PALLADIUM | 490 | 1 | 1% | 0% | -81% | -98% | -98% |
| NATGAS | 484 | 3 | 2% | 2% | -42% | -96% | -94% |
| EURUSD | 470 | 3 | 3% | 2% | -40% | -75% | -75% |
| GBPUSD | 446 | 1 | 2% | 1% | -79% | -96% | -96% |
| USDJPY | 405 | 3 | 1% | 1% | -31% | -98% | -97% |
| USDCAD | 53 | 0 | 0% | 0% | -100% | -100% | -100% |
| AUDUSD | 53 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 8254 | 34 | 3% | 2% | -52% | -90% | -89% |
| DOWN (bought NO) | 8139 | 29 | 3% | 1% | -59% | -91% | -92% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 1952 | 10 | 2% | 1% | -15% | -77% | -76% |
| 0.05–0.1% | 1954 | 6 | 3% | 1% | -56% | -92% | -92% |
| 0.1–0.2% | 2811 | 9 | 4% | 2% | -61% | -91% | -92% |
| 0.2–0.5% | 3093 | 18 | 5% | 3% | -36% | -89% | -89% |
| Over 0.5% | 1209 | 5 | 6% | 2% | -57% | -88% | -90% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 4145 | 20 | 4% | 2% | -45% | -87% | -87% |
| Morning (6am–12pm) | 3780 | 20 | 4% | 2% | -39% | -91% | -91% |
| Afternoon (12–6pm) | 3818 | 9 | 3% | 1% | -72% | -91% | -91% |
| Evening (6pm–12am) | 4650 | 14 | 3% | 1% | -66% | -94% | -94% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 25 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,516 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/13 2:44:53 AM | USDCAD | DOWN | 6 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/13 2:44:38 AM | PLATINUM | UP | 22 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/13 2:44:38 AM | DOGE | UP | 22 sec | -0.009% | 1¢ | ❌ Lost | -$0.15 |
| 10/13 2:44:06 AM | EURUSD | UP | 54 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/13 2:44:06 AM | ZEC | DOWN | 54 sec | +0.202% | 0¢ | ❌ Lost | -$0.15 |
| 10/13 2:44:06 AM | USDJPY | UP | 54 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/13 2:44:06 AM | HYPE | UP | 54 sec | -0.107% | 1¢ | ❌ Lost | -$0.15 |
| 10/13 2:43:50 AM | NATGAS | UP | 70 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/13 2:42:17 AM | SOL | UP | 2.7 min | -0.257% | 1¢ | ❌ Lost | -$0.15 |
| 10/13 2:42:01 AM | GOLD | UP | 3.0 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/13 2:42:01 AM | SILVER | UP | 3.0 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/13 2:41:45 AM | ETH | UP | 3.2 min | -0.169% | 1¢ | ❌ Lost | -$0.15 |
| 10/13 2:41:30 AM | BNB | UP | 3.5 min | -0.134% | 1¢ | ❌ Lost | -$0.15 |
| 10/13 2:41:14 AM | BTC | UP | 3.8 min | -0.181% | 1¢ | ❌ Lost | -$0.15 |
| 10/13 2:40:58 AM | NEAR | DOWN | 4.0 min | +0.707% | 1¢ | ❌ Lost | -$0.15 |
| 10/13 2:29:46 AM | PLATINUM | DOWN | 13 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/13 2:29:30 AM | GOLD | DOWN | 29 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/13 2:29:30 AM | NATGAS | UP | 29 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/13 2:29:14 AM | COPPER | UP | 45 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/13 2:29:14 AM | USDJPY | UP | 45 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/13 2:29:14 AM | HYPE | UP | 45 sec | -0.117% | 0¢ | ❌ Lost | $0.00 |
| 10/13 2:28:58 AM | WTI | DOWN | 61 sec | — | 2¢ | ❌ Lost | -$0.15 |
| 10/13 2:28:27 AM | PALLADIUM | DOWN | 1.5 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/13 2:28:11 AM | SILVER | DOWN | 1.8 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/13 2:27:40 AM | SOL | UP | 2.3 min | -0.216% | 0¢ | ❌ Lost | -$0.15 |
| 10/13 2:27:24 AM | ZEC | UP | 2.6 min | -0.454% | 0¢ | ❌ Lost | $0.00 |
| 10/13 2:26:36 AM | ETH | UP | 3.4 min | -0.180% | 1¢ | ❌ Lost | -$0.15 |
| 10/13 2:26:20 AM | XRP | UP | 3.6 min | -0.282% | 1¢ | ❌ Lost | -$0.15 |
| 10/13 2:25:33 AM | NEAR | UP | 4.5 min | -0.761% | 1¢ | ❌ Lost | -$0.15 |
| 10/13 2:25:17 AM | BTC | UP | 4.7 min | -0.220% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
