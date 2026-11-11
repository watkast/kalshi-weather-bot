# 15-Minute 1¢ Study

*Updated Wed Nov 11, 2:41 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 4198 finished bets | 1% | $177.80 | +38% | +4.24¢ | $86.80 / $91.00 |

*Expect about **95 buys a day** (~$14.27/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 3919 | $93.65 | +22% |
| Volatility model ≥ 2%, hold to the close | 7700 | $53.30 | +6% |
| Momentum model ≥ 2%, hold to the close | 6385 | -$19.65 | -3% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 53287 | 53265 | 203 (0%) | 1.07% | -$3,653.60 (-56%) | Hold to the close: -$3,653.60 (-56%) |

*In play or awaiting result: 14. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 32108 | 4.7% | 0.4% (130) | -675% | ❌ Worse |
| Momentum model | 32108 | 4.6% | 0.4% (130) | -699% | ❌ Worse |
| Mean-reversion model | 32108 | 8.1% | 0.4% (130) | -817% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 32108 | 130 | -48% | -87% | -87% | -84% |
| Volatility model ≥ 2% | 7700 | 70 | +6% | -77% | -76% | -72% |
| Volatility model ≥ 5% | 4198 | 46 | +38% | -72% | -70% | -67% |
| Volatility model ≥ 10% | 2422 | 28 | +66% | -62% | -60% | -57% |
| Momentum model ≥ 2% | 6385 | 51 | -3% | -78% | -77% | -74% |
| Momentum model ≥ 5% | 3919 | 37 | +22% | -74% | -73% | -69% |
| Momentum model ≥ 10% | 2573 | 25 | +37% | -66% | -65% | -61% |
| Mean-reversion model ≥ 2% | 13295 | 92 | -24% | -82% | -82% | -79% |
| Mean-reversion model ≥ 5% | 9305 | 78 | -7% | -80% | -79% | -76% |
| Mean-reversion model ≥ 10% | 6221 | 56 | +2% | -77% | -76% | -74% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 32313 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 12709 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 8243 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 53265 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 203 | 0% | -$3,653.60 | -56% | — |
| Sell at 2¢ | 2122 | 4% | -$5,663.88 | -87% | 47 sec |
| Sell at 3¢ | 1443 | 3% | -$5,652.83 | -87% | 48 sec |
| Sell at 5¢ | 1003 | 2% | -$5,535.65 | -85% | 63 sec |
| Sell at 10¢ | 605 | 1% | -$5,311.05 | -82% | 65 sec |
| Sell at 25¢ | 320 | 1% | -$4,932.40 | -76% | 83 sec |
| Sell at 50¢ | 211 | 0% | -$4,469.35 | -69% | 1.7 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 12 | 0 | 25% | 17% | -100% | -57% | -35% |
| 5–10 min | 2668 | 13 | 11% | 4% | -54% | -81% | -82% |
| 2–5 min | 17246 | 94 | 7% | 3% | -46% | -87% | -87% |
| 1–2 min | 13428 | 44 | 3% | 2% | -64% | -92% | -92% |
| Under 1 min | 19911 | 52 | 1% | 0% | -63% | -85% | -85% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 3617 | 16 | 5% | 2% | -43% | -88% | -88% |
| SOL | 3613 | 16 | 4% | 2% | -43% | -87% | -87% |
| HYPE | 3606 | 11 | 5% | 2% | -62% | -89% | -88% |
| BNB | 3598 | 19 | 5% | 2% | -34% | -86% | -85% |
| DOGE | 3595 | 8 | 4% | 2% | -72% | -90% | -90% |
| ETH | 3588 | 15 | 7% | 3% | -48% | -81% | -81% |
| BTC | 3570 | 17 | 5% | 2% | -35% | -87% | -88% |
| NEAR | 3569 | 17 | 5% | 2% | -38% | -85% | -85% |
| XRP | 3557 | 13 | 3% | 1% | -54% | -89% | -88% |
| GOLD | 1918 | 5 | 5% | 2% | -68% | -81% | -83% |
| WTI | 1897 | 6 | 4% | 2% | -62% | -91% | -92% |
| SILVER | 1870 | 8 | 5% | 2% | -50% | -83% | -82% |
| PLATINUM | 1698 | 4 | 2% | 1% | -78% | -96% | -95% |
| EURUSD | 1635 | 5 | 3% | 1% | -71% | -90% | -89% |
| COPPER | 1590 | 6 | 2% | 1% | -65% | -73% | -73% |
| NATGAS | 1556 | 8 | 2% | 1% | -52% | -78% | -78% |
| GBPUSD | 1554 | 5 | 2% | 1% | -70% | -96% | -96% |
| USDJPY | 1535 | 6 | 2% | 1% | -64% | -97% | -96% |
| PALLADIUM | 1525 | 4 | 1% | 1% | -76% | -92% | -92% |
| AUDUSD | 1098 | 6 | 2% | 1% | -49% | -88% | -88% |
| USDCAD | 1064 | 0 | 2% | 1% | -100% | -96% | -97% |
| BRENT | 655 | 0 | 2% | 1% | -100% | -97% | -97% |
| 10YRRATE | 353 | 2 | 4% | 2% | -47% | -66% | -64% |
| 2YRRATE | 338 | 4 | 4% | 2% | +10% | -38% | -36% |
| 30YRRATE | 332 | 0 | 2% | 1% | -100% | -96% | -94% |
| 5YRRATE | 311 | 2 | 4% | 2% | -40% | -93% | -95% |
| INX | 23 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 26991 | 107 | 4% | 2% | -54% | -88% | -87% |
| DOWN (bought NO) | 26274 | 96 | 4% | 2% | -58% | -86% | -87% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 5151 | 25 | 2% | 1% | -14% | -77% | -76% |
| 0.05–0.1% | 5489 | 20 | 3% | 2% | -44% | -91% | -91% |
| 0.1–0.2% | 8299 | 30 | 5% | 2% | -54% | -89% | -89% |
| 0.2–0.5% | 9684 | 40 | 6% | 3% | -54% | -87% | -86% |
| Over 0.5% | 3682 | 17 | 7% | 3% | -52% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 12984 | 43 | 4% | 2% | -62% | -88% | -88% |
| Morning (6am–12pm) | 12871 | 58 | 4% | 2% | -49% | -85% | -84% |
| Afternoon (12–6pm) | 12822 | 57 | 4% | 2% | -48% | -86% | -86% |
| Evening (6pm–12am) | 14588 | 45 | 4% | 2% | -65% | -90% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,875 |
| Time from buy to best bounce (bounced bets) | 51 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/11 2:40:38 AM | EURUSD | UP | 4.4 min | — | — | In play | — |
| 11/11 2:40:22 AM | USDCAD | DOWN | 4.6 min | — | — | In play | — |
| 11/11 2:40:06 AM | ETH | UP | 4.9 min | -0.387% | — | In play | — |
| 11/11 2:40:06 AM | HYPE | UP | 4.9 min | -0.534% | — | In play | — |
| 11/11 2:40:06 AM | BNB | UP | 4.9 min | -0.196% | — | In play | — |
| 11/11 2:29:53 AM | BTC | DOWN | 6 sec | +0.061% | 0¢ | ❌ Lost | $0.00 |
| 11/11 2:29:53 AM | XRP | UP | 6 sec | -0.019% | 0¢ | ❌ Lost | $0.00 |
| 11/11 2:29:37 AM | SILVER | DOWN | 22 sec | — | 0¢ | ❌ Lost | $0.00 |
| 11/11 2:29:37 AM | ETH | DOWN | 22 sec | +0.080% | 0¢ | ❌ Lost | $0.00 |
| 11/11 2:29:04 AM | EURUSD | UP | 55 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/11 2:28:48 AM | NEAR | DOWN | 71 sec | +0.173% | 0¢ | ❌ Lost | $0.00 |
| 11/11 2:28:48 AM | AUDUSD | UP | 71 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/11 2:28:48 AM | BNB | DOWN | 71 sec | -0.012% | 1¢ | ❌ Lost | -$0.15 |
| 11/11 2:28:16 AM | COPPER | UP | 1.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/11 2:27:58 AM | GOLD | UP | 2.0 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/11 2:27:58 AM | DOGE | DOWN | 2.0 min | +0.236% | 1¢ | ❌ Lost | -$0.15 |
| 11/11 2:27:42 AM | USDJPY | DOWN | 2.3 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/11 2:27:42 AM | ZEC | DOWN | 2.3 min | +0.566% | 1¢ | ❌ Lost | -$0.15 |
| 11/11 2:27:42 AM | SOL | DOWN | 2.3 min | +0.255% | 1¢ | ❌ Lost | -$0.15 |
| 11/11 2:27:26 AM | PLATINUM | DOWN | 2.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/11 2:26:53 AM | PALLADIUM | DOWN | 3.1 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/11 2:26:21 AM | HYPE | DOWN | 3.6 min | +0.372% | 1¢ | ❌ Lost | -$0.15 |
| 11/11 2:24:12 AM | BRENT | DOWN | 5.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/11 2:23:57 AM | WTI | DOWN | 6.0 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/11 12:44:49 AM | EURUSD | UP | 11 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/11 12:44:32 AM | USDJPY | UP | 28 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/11 12:44:16 AM | BTC | UP | 44 sec | -0.068% | 0¢ | ❌ Lost | $0.00 |
| 11/11 12:44:16 AM | BRENT | DOWN | 44 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/11 12:44:00 AM | SOL | UP | 60 sec | -0.161% | 0¢ | ❌ Lost | -$0.15 |
| 11/11 12:43:45 AM | NEAR | UP | 74 sec | -0.341% | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
