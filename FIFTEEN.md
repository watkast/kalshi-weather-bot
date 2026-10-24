# 15-Minute 1¢ Study

*Updated Sat Oct 24, 6:59 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 2571 finished bets | 1% | $100.40 | +34% | +3.91¢ | $41.30 / $59.10 |

*Expect about **98 buys a day** (~$14.68/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 2372 | $73.20 | +28% |
| Volatility model ≥ 2%, hold to the close | 4753 | $19.55 | +3% |
| Momentum model ≥ 2%, hold to the close | 3955 | -$2.85 | -1% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 30887 | 30873 | 119 (0%) | 1.07% | -$2,094.20 (-56%) | Hold to the close: -$2,094.20 (-56%) |

*In play or awaiting result: 13. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 19666 | 4.7% | 0.4% (84) | -634% | ❌ Worse |
| Momentum model | 19666 | 4.6% | 0.4% (84) | -659% | ❌ Worse |
| Mean-reversion model | 19666 | 7.9% | 0.4% (84) | -767% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 19666 | 84 | -46% | -87% | -87% | -85% |
| Volatility model ≥ 2% | 4753 | 43 | +3% | -78% | -77% | -73% |
| Volatility model ≥ 5% | 2571 | 28 | +34% | -73% | -72% | -69% |
| Volatility model ≥ 10% | 1465 | 18 | +72% | -65% | -63% | -60% |
| Momentum model ≥ 2% | 3955 | 33 | -1% | -79% | -79% | -76% |
| Momentum model ≥ 5% | 2372 | 24 | +28% | -76% | -75% | -71% |
| Momentum model ≥ 10% | 1552 | 16 | +41% | -69% | -68% | -63% |
| Mean-reversion model ≥ 2% | 7907 | 55 | -24% | -83% | -82% | -80% |
| Mean-reversion model ≥ 5% | 5533 | 46 | -8% | -81% | -80% | -77% |
| Mean-reversion model ≥ 10% | 3681 | 33 | +2% | -78% | -77% | -75% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 19866 | 5% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 7352 | 2% | 2% | 1% | 1% | 0% | 0% |
| Financials | 3655 | 2% | 1% | 1% | 1% | 0% | 0% |
| **All** | 30873 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 119 | 0% | -$2,094.20 | -56% | — |
| Sell at 2¢ | 1151 | 4% | -$3,292.94 | -88% | 47 sec |
| Sell at 3¢ | 789 | 3% | -$3,284.49 | -87% | 48 sec |
| Sell at 5¢ | 553 | 2% | -$3,232.75 | -86% | 61 sec |
| Sell at 10¢ | 340 | 1% | -$3,104.80 | -83% | 64 sec |
| Sell at 25¢ | 187 | 1% | -$2,861.23 | -76% | 82 sec |
| Sell at 50¢ | 121 | 0% | -$2,579.45 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 1325 | 7 | 11% | 4% | -50% | -80% | -82% |
| 2–5 min | 9861 | 54 | 7% | 3% | -46% | -87% | -87% |
| 1–2 min | 7841 | 30 | 3% | 1% | -58% | -92% | -91% |
| Under 1 min | 11842 | 28 | 1% | 0% | -66% | -86% | -86% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 2227 | 12 | 5% | 2% | -32% | -89% | -89% |
| HYPE | 2219 | 8 | 5% | 3% | -55% | -88% | -86% |
| BNB | 2216 | 12 | 5% | 2% | -33% | -83% | -82% |
| SOL | 2211 | 6 | 4% | 2% | -66% | -92% | -92% |
| ETH | 2208 | 11 | 6% | 3% | -40% | -86% | -85% |
| DOGE | 2202 | 4 | 4% | 2% | -77% | -90% | -90% |
| XRP | 2199 | 9 | 3% | 1% | -49% | -88% | -88% |
| NEAR | 2195 | 12 | 5% | 3% | -29% | -81% | -81% |
| BTC | 2189 | 12 | 5% | 2% | -27% | -88% | -89% |
| GOLD | 1190 | 4 | 4% | 2% | -60% | -81% | -83% |
| SILVER | 1156 | 5 | 4% | 1% | -50% | -82% | -82% |
| WTI | 1143 | 3 | 3% | 1% | -69% | -94% | -95% |
| PLATINUM | 1010 | 0 | 1% | 1% | -100% | -98% | -98% |
| COPPER | 987 | 4 | 1% | 1% | -62% | -69% | -69% |
| EURUSD | 938 | 3 | 2% | 1% | -70% | -86% | -86% |
| NATGAS | 933 | 5 | 2% | 1% | -50% | -86% | -86% |
| PALLADIUM | 897 | 2 | 1% | 0% | -79% | -88% | -88% |
| GBPUSD | 884 | 1 | 2% | 1% | -89% | -96% | -96% |
| USDJPY | 866 | 5 | 1% | 1% | -46% | -98% | -97% |
| AUDUSD | 428 | 0 | 1% | 0% | -100% | -98% | -98% |
| USDCAD | 387 | 0 | 1% | 0% | -100% | -98% | -99% |
| 10YRRATE | 43 | 0 | 0% | 0% | -100% | -100% | -100% |
| 2YRRATE | 40 | 1 | 2% | 0% | +133% | +138% | +133% |
| 30YRRATE | 39 | 0 | 0% | 0% | -100% | -100% | -100% |
| BRENT | 36 | 0 | 0% | 0% | -100% | -100% | -100% |
| 5YRRATE | 30 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 15615 | 65 | 4% | 2% | -52% | -87% | -86% |
| DOWN (bought NO) | 15258 | 54 | 4% | 2% | -59% | -88% | -88% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 3308 | 18 | 2% | 1% | -8% | -79% | -79% |
| 0.05–0.1% | 3424 | 11 | 3% | 1% | -53% | -92% | -92% |
| 0.1–0.2% | 5123 | 19 | 5% | 2% | -54% | -89% | -89% |
| 0.2–0.5% | 5791 | 28 | 6% | 3% | -47% | -87% | -86% |
| Over 0.5% | 2216 | 10 | 7% | 3% | -53% | -87% | -88% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 7739 | 32 | 4% | 2% | -53% | -85% | -85% |
| Morning (6am–12pm) | 7451 | 34 | 4% | 2% | -48% | -88% | -87% |
| Afternoon (12–6pm) | 7298 | 24 | 4% | 2% | -61% | -87% | -88% |
| Evening (6pm–12am) | 8385 | 29 | 3% | 2% | -60% | -90% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,658 |
| Time from buy to best bounce (bounced bets) | 49 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/24 6:59:26 AM | XRP | UP | 34 sec | -0.039% | — | In play | — |
| 10/24 6:59:26 AM | SOL | DOWN | 34 sec | +0.025% | — | In play | — |
| 10/24 6:59:26 AM | BTC | DOWN | 34 sec | +0.023% | — | In play | — |
| 10/24 6:57:49 AM | NEAR | UP | 2.2 min | -0.536% | — | In play | — |
| 10/24 6:57:17 AM | HYPE | DOWN | 2.7 min | +0.204% | — | In play | — |
| 10/24 6:54:33 AM | ZEC | DOWN | 5.5 min | +0.486% | — | In play | — |
| 10/24 6:44:56 AM | BNB | UP | 3 sec | -0.018% | 0¢ | ❌ Lost | $0.00 |
| 10/24 6:44:40 AM | DOGE | UP | 19 sec | -0.062% | 0¢ | ❌ Lost | $0.00 |
| 10/24 6:44:24 AM | ETH | UP | 35 sec | -0.039% | 0¢ | ❌ Lost | $0.00 |
| 10/24 6:44:24 AM | HYPE | UP | 35 sec | -0.131% | 0¢ | ❌ Lost | $0.00 |
| 10/24 6:44:08 AM | ZEC | UP | 52 sec | -0.136% | 0¢ | ❌ Lost | $0.00 |
| 10/24 6:44:08 AM | XRP | UP | 52 sec | -0.086% | 1¢ | ❌ Lost | -$0.15 |
| 10/24 6:42:31 AM | SOL | UP | 2.5 min | -0.160% | 1¢ | ❌ Lost | -$0.15 |
| 10/24 6:42:31 AM | NEAR | UP | 2.5 min | -0.389% | 1¢ | ❌ Lost | -$0.15 |
| 10/24 6:26:36 AM | BNB | DOWN | 3.4 min | +0.133% | 1¢ | ❌ Lost | -$0.15 |
| 10/24 6:25:46 AM | NEAR | DOWN | 4.2 min | +0.503% | 1¢ | ❌ Lost | -$0.15 |
| 10/24 6:25:30 AM | ZEC | DOWN | 4.5 min | +0.524% | 1¢ | ❌ Lost | -$0.15 |
| 10/24 6:25:14 AM | HYPE | DOWN | 4.8 min | +0.351% | 1¢ | ❌ Lost | -$0.15 |
| 10/24 6:25:14 AM | DOGE | DOWN | 4.8 min | +0.244% | 1¢ | ❌ Lost | -$0.15 |
| 10/24 6:24:59 AM | BTC | DOWN | 5.0 min | +0.157% | 1¢ | ❌ Lost | -$0.15 |
| 10/24 6:24:59 AM | ETH | DOWN | 5.0 min | +0.192% | 1¢ | ❌ Lost | -$0.15 |
| 10/24 6:24:42 AM | SOL | DOWN | 5.3 min | +0.251% | 1¢ | ❌ Lost | -$0.15 |
| 10/24 6:24:10 AM | XRP | DOWN | 5.8 min | +0.344% | 1¢ | ❌ Lost | -$0.15 |
| 10/24 6:14:39 AM | ETH | UP | 21 sec | -0.023% | 1¢ | ❌ Lost | -$0.15 |
| 10/24 6:14:08 AM | BTC | DOWN | 51 sec | +0.037% | 1¢ | ❌ Lost | -$0.15 |
| 10/24 6:13:52 AM | ZEC | UP | 67 sec | -0.117% | 1¢ | ❌ Lost | -$0.15 |
| 10/24 6:13:20 AM | XRP | UP | 1.6 min | -0.109% | 1¢ | ❌ Lost | -$0.15 |
| 10/24 6:11:59 AM | BNB | UP | 3.0 min | -0.105% | 5¢ | ❌ Lost | -$0.15 |
| 10/24 6:11:26 AM | DOGE | UP | 3.5 min | -0.199% | 2¢ | ❌ Lost | -$0.15 |
| 10/24 6:10:53 AM | HYPE | UP | 4.1 min | -0.324% | 4¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
