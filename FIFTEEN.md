# 15-Minute 1¢ Study

*Updated Wed Nov 11, 5:26 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 4207 finished bets | 1% | $176.90 | +38% | +4.20¢ | $86.20 / $90.70 |

*Expect about **95 buys a day** (~$14.26/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 3927 | $92.75 | +22% |
| Volatility model ≥ 2%, hold to the close | 7717 | $51.35 | +6% |
| Momentum model ≥ 2%, hold to the close | 6400 | -$21.30 | -3% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 53484 | 53465 | 203 (0%) | 1.07% | -$3,678.65 (-56%) | Hold to the close: -$3,678.65 (-56%) |

*In play or awaiting result: 11. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 32204 | 4.7% | 0.4% (130) | -676% | ❌ Worse |
| Momentum model | 32204 | 4.6% | 0.4% (130) | -701% | ❌ Worse |
| Mean-reversion model | 32204 | 8.1% | 0.4% (130) | -819% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 32204 | 130 | -48% | -87% | -87% | -84% |
| Volatility model ≥ 2% | 7717 | 70 | +6% | -77% | -76% | -72% |
| Volatility model ≥ 5% | 4207 | 46 | +38% | -72% | -70% | -67% |
| Volatility model ≥ 10% | 2430 | 28 | +65% | -62% | -61% | -57% |
| Momentum model ≥ 2% | 6400 | 51 | -3% | -78% | -77% | -74% |
| Momentum model ≥ 5% | 3927 | 37 | +22% | -74% | -73% | -69% |
| Momentum model ≥ 10% | 2578 | 25 | +36% | -66% | -65% | -61% |
| Mean-reversion model ≥ 2% | 13326 | 92 | -24% | -82% | -82% | -79% |
| Mean-reversion model ≥ 5% | 9327 | 78 | -7% | -80% | -79% | -76% |
| Mean-reversion model ≥ 10% | 6238 | 56 | +2% | -77% | -76% | -74% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 32409 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 12774 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 8282 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 53465 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 203 | 0% | -$3,678.65 | -56% | — |
| Sell at 2¢ | 2128 | 4% | -$5,687.37 | -87% | 47 sec |
| Sell at 3¢ | 1447 | 3% | -$5,676.32 | -87% | 48 sec |
| Sell at 5¢ | 1005 | 2% | -$5,559.40 | -85% | 63 sec |
| Sell at 10¢ | 605 | 1% | -$5,336.10 | -82% | 65 sec |
| Sell at 25¢ | 320 | 1% | -$4,957.45 | -76% | 83 sec |
| Sell at 50¢ | 211 | 0% | -$4,494.40 | -69% | 1.7 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 12 | 0 | 25% | 17% | -100% | -57% | -35% |
| 5–10 min | 2675 | 13 | 11% | 4% | -54% | -81% | -83% |
| 2–5 min | 17305 | 94 | 7% | 3% | -47% | -87% | -87% |
| 1–2 min | 13486 | 44 | 3% | 2% | -64% | -92% | -92% |
| Under 1 min | 19987 | 52 | 1% | 0% | -63% | -85% | -85% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 3627 | 16 | 5% | 2% | -43% | -88% | -88% |
| SOL | 3624 | 16 | 4% | 2% | -44% | -87% | -86% |
| HYPE | 3617 | 11 | 5% | 2% | -62% | -89% | -88% |
| BNB | 3609 | 19 | 5% | 2% | -34% | -86% | -85% |
| DOGE | 3605 | 8 | 4% | 2% | -72% | -90% | -90% |
| ETH | 3599 | 15 | 7% | 3% | -48% | -82% | -81% |
| NEAR | 3580 | 17 | 5% | 2% | -39% | -85% | -85% |
| BTC | 3580 | 17 | 5% | 2% | -35% | -87% | -88% |
| XRP | 3568 | 13 | 3% | 1% | -55% | -89% | -89% |
| GOLD | 1926 | 5 | 5% | 2% | -68% | -81% | -83% |
| WTI | 1907 | 6 | 4% | 2% | -62% | -91% | -92% |
| SILVER | 1878 | 8 | 5% | 2% | -50% | -83% | -83% |
| PLATINUM | 1705 | 4 | 2% | 1% | -78% | -96% | -95% |
| EURUSD | 1643 | 5 | 2% | 1% | -72% | -90% | -89% |
| COPPER | 1598 | 6 | 2% | 1% | -65% | -73% | -73% |
| NATGAS | 1563 | 8 | 2% | 1% | -52% | -79% | -78% |
| GBPUSD | 1563 | 5 | 2% | 1% | -70% | -96% | -96% |
| USDJPY | 1546 | 6 | 2% | 1% | -64% | -97% | -96% |
| PALLADIUM | 1534 | 4 | 1% | 1% | -76% | -92% | -92% |
| AUDUSD | 1104 | 6 | 2% | 1% | -49% | -88% | -88% |
| USDCAD | 1069 | 0 | 2% | 1% | -100% | -96% | -96% |
| BRENT | 663 | 0 | 2% | 1% | -100% | -97% | -97% |
| 10YRRATE | 353 | 2 | 4% | 2% | -47% | -66% | -64% |
| 2YRRATE | 338 | 4 | 4% | 2% | +10% | -38% | -36% |
| 30YRRATE | 332 | 0 | 2% | 1% | -100% | -96% | -94% |
| 5YRRATE | 311 | 2 | 4% | 2% | -40% | -93% | -95% |
| INX | 23 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 27087 | 107 | 4% | 2% | -55% | -88% | -88% |
| DOWN (bought NO) | 26378 | 96 | 4% | 2% | -58% | -86% | -87% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 5163 | 25 | 2% | 1% | -14% | -77% | -76% |
| 0.05–0.1% | 5508 | 20 | 3% | 2% | -44% | -91% | -91% |
| 0.1–0.2% | 8325 | 30 | 5% | 2% | -54% | -89% | -89% |
| 0.2–0.5% | 9716 | 40 | 6% | 3% | -54% | -87% | -86% |
| Over 0.5% | 3689 | 17 | 7% | 3% | -52% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 13184 | 43 | 4% | 2% | -63% | -88% | -88% |
| Morning (6am–12pm) | 12871 | 58 | 4% | 2% | -49% | -85% | -84% |
| Afternoon (12–6pm) | 12822 | 57 | 4% | 2% | -48% | -86% | -86% |
| Evening (6pm–12am) | 14588 | 45 | 4% | 2% | -65% | -90% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,865 |
| Time from buy to best bounce (bounced bets) | 51 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/11 5:26:40 AM | WTI | DOWN | 3.3 min | — | — | In play | — |
| 11/11 5:26:08 AM | DOGE | UP | 3.9 min | -0.292% | — | In play | — |
| 11/11 5:14:54 AM | PALLADIUM | DOWN | 6 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/11 5:14:54 AM | NATGAS | UP | 6 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/11 5:14:38 AM | GOLD | DOWN | 22 sec | — | 0¢ | ❌ Lost | $0.00 |
| 11/11 5:14:38 AM | NEAR | DOWN | 22 sec | +0.096% | 0¢ | ❌ Lost | $0.00 |
| 11/11 5:14:38 AM | AUDUSD | DOWN | 22 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/11 5:14:38 AM | EURUSD | DOWN | 22 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/11 5:14:07 AM | COPPER | DOWN | 53 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/11 5:14:07 AM | GBPUSD | DOWN | 53 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/11 5:14:07 AM | ZEC | UP | 53 sec | -0.228% | 1¢ | ❌ Lost | -$0.15 |
| 11/11 5:13:51 AM | BTC | UP | 69 sec | -0.120% | 0¢ | ❌ Lost | $0.00 |
| 11/11 5:13:51 AM | BRENT | DOWN | 69 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/11 5:13:51 AM | DOGE | UP | 69 sec | -0.158% | 0¢ | ❌ Lost | -$0.15 |
| 11/11 5:13:35 AM | HYPE | UP | 85 sec | -0.220% | 0¢ | ❌ Lost | -$0.15 |
| 11/11 5:13:19 AM | ETH | UP | 1.7 min | -0.158% | 0¢ | ❌ Lost | -$0.15 |
| 11/11 5:13:19 AM | SILVER | DOWN | 1.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/11 5:13:19 AM | BNB | UP | 1.7 min | -0.050% | 0¢ | ❌ Lost | -$0.15 |
| 11/11 5:12:48 AM | WTI | DOWN | 2.2 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/11 5:12:48 AM | XRP | UP | 2.2 min | -0.255% | 1¢ | ❌ Lost | -$0.15 |
| 11/11 5:12:32 AM | SOL | UP | 2.5 min | -0.252% | 1¢ | ❌ Lost | -$0.15 |
| 11/11 5:12:16 AM | USDJPY | DOWN | 2.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/11 5:11:27 AM | PLATINUM | DOWN | 3.5 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/11 4:59:59 AM | WTI | DOWN | 1 sec | — | 0¢ | ❌ Lost | $0.00 |
| 11/11 4:59:59 AM | BNB | DOWN | 1 sec | +0.003% | 0¢ | ❌ Lost | -$0.15 |
| 11/11 4:59:59 AM | EURUSD | UP | 1 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/11 4:59:43 AM | GOLD | UP | 17 sec | — | 0¢ | ❌ Lost | $0.00 |
| 11/11 4:59:43 AM | BTC | UP | 17 sec | -0.051% | 0¢ | ❌ Lost | $0.00 |
| 11/11 4:59:43 AM | XRP | UP | 17 sec | -0.085% | 0¢ | ❌ Lost | $0.00 |
| 11/11 4:59:43 AM | NATGAS | DOWN | 17 sec | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
