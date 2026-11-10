# 15-Minute 1¢ Study

*Updated Tue Nov 10, 5:46 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 4157 finished bets | 1% | $182.30 | +39% | +4.39¢ | $89.05 / $93.25 |

*Expect about **96 buys a day** (~$14.42/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 3870 | $99.50 | +24% |
| Volatility model ≥ 2%, hold to the close | 7598 | $66.05 | +7% |
| Momentum model ≥ 2%, hold to the close | 6294 | -$8.40 | -1% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 51983 | 51966 | 199 (0%) | 1.07% | -$3,544.15 (-56%) | Hold to the close: -$3,544.15 (-56%) |

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
| Volatility model | 31526 | 4.8% | 0.4% (128) | -679% | ❌ Worse |
| Momentum model | 31526 | 4.6% | 0.4% (128) | -704% | ❌ Worse |
| Mean-reversion model | 31526 | 8.1% | 0.4% (128) | -821% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 31526 | 128 | -48% | -87% | -87% | -84% |
| Volatility model ≥ 2% | 7598 | 70 | +7% | -77% | -76% | -71% |
| Volatility model ≥ 5% | 4157 | 46 | +39% | -72% | -70% | -66% |
| Volatility model ≥ 10% | 2396 | 28 | +68% | -62% | -60% | -56% |
| Momentum model ≥ 2% | 6294 | 51 | -1% | -78% | -77% | -74% |
| Momentum model ≥ 5% | 3870 | 37 | +24% | -74% | -73% | -69% |
| Momentum model ≥ 10% | 2538 | 25 | +39% | -65% | -64% | -60% |
| Mean-reversion model ≥ 2% | 13052 | 91 | -23% | -82% | -82% | -79% |
| Mean-reversion model ≥ 5% | 9147 | 78 | -5% | -79% | -79% | -76% |
| Mean-reversion model ≥ 10% | 6118 | 56 | +4% | -77% | -76% | -74% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 31731 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 12334 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 7901 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 51966 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 199 | 0% | -$3,544.15 | -56% | — |
| Sell at 2¢ | 2068 | 4% | -$5,512.47 | -87% | 47 sec |
| Sell at 3¢ | 1407 | 3% | -$5,501.42 | -87% | 48 sec |
| Sell at 5¢ | 982 | 2% | -$5,383.85 | -85% | 63 sec |
| Sell at 10¢ | 595 | 1% | -$5,158.70 | -81% | 65 sec |
| Sell at 25¢ | 314 | 1% | -$4,786.81 | -76% | 83 sec |
| Sell at 50¢ | 205 | 0% | -$4,344.40 | -69% | 1.7 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 12 | 0 | 25% | 17% | -100% | -57% | -35% |
| 5–10 min | 2592 | 12 | 11% | 4% | -56% | -81% | -82% |
| 2–5 min | 16788 | 93 | 7% | 3% | -45% | -87% | -86% |
| 1–2 min | 13126 | 44 | 3% | 2% | -63% | -92% | -92% |
| Under 1 min | 19448 | 50 | 1% | 0% | -63% | -85% | -84% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 3554 | 15 | 5% | 2% | -45% | -88% | -88% |
| SOL | 3549 | 16 | 4% | 2% | -42% | -87% | -87% |
| HYPE | 3541 | 11 | 5% | 2% | -61% | -89% | -88% |
| BNB | 3534 | 19 | 5% | 2% | -32% | -86% | -85% |
| DOGE | 3529 | 8 | 4% | 2% | -71% | -90% | -89% |
| ETH | 3525 | 15 | 7% | 3% | -47% | -81% | -81% |
| BTC | 3504 | 17 | 5% | 2% | -33% | -87% | -88% |
| NEAR | 3503 | 16 | 5% | 2% | -41% | -85% | -85% |
| XRP | 3492 | 13 | 3% | 1% | -54% | -89% | -88% |
| GOLD | 1869 | 5 | 6% | 2% | -67% | -81% | -83% |
| WTI | 1842 | 6 | 4% | 2% | -61% | -91% | -92% |
| SILVER | 1822 | 8 | 5% | 2% | -48% | -83% | -82% |
| PLATINUM | 1651 | 4 | 2% | 1% | -77% | -96% | -95% |
| EURUSD | 1585 | 5 | 2% | 1% | -71% | -90% | -89% |
| COPPER | 1548 | 6 | 2% | 1% | -64% | -73% | -73% |
| NATGAS | 1508 | 8 | 2% | 1% | -50% | -78% | -77% |
| GBPUSD | 1503 | 5 | 2% | 1% | -69% | -96% | -96% |
| PALLADIUM | 1486 | 3 | 1% | 0% | -81% | -92% | -92% |
| USDJPY | 1483 | 6 | 2% | 1% | -62% | -96% | -96% |
| AUDUSD | 1045 | 5 | 2% | 1% | -55% | -87% | -88% |
| USDCAD | 1013 | 0 | 2% | 1% | -100% | -96% | -97% |
| BRENT | 608 | 0 | 2% | 1% | -100% | -97% | -97% |
| 10YRRATE | 336 | 2 | 4% | 2% | -44% | -64% | -62% |
| 2YRRATE | 318 | 4 | 4% | 2% | +17% | -34% | -32% |
| 30YRRATE | 312 | 0 | 2% | 1% | -100% | -96% | -94% |
| 5YRRATE | 295 | 2 | 4% | 2% | -37% | -92% | -95% |
| INX | 11 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 26348 | 104 | 4% | 2% | -55% | -88% | -87% |
| DOWN (bought NO) | 25618 | 95 | 4% | 2% | -57% | -86% | -86% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 5106 | 25 | 2% | 1% | -14% | -77% | -76% |
| 0.05–0.1% | 5420 | 20 | 3% | 2% | -44% | -91% | -91% |
| 0.1–0.2% | 8164 | 30 | 5% | 2% | -54% | -89% | -89% |
| 0.2–0.5% | 9480 | 40 | 6% | 3% | -53% | -87% | -86% |
| Over 0.5% | 3553 | 15 | 7% | 3% | -56% | -87% | -88% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 12889 | 43 | 4% | 2% | -62% | -88% | -88% |
| Morning (6am–12pm) | 12425 | 56 | 4% | 2% | -49% | -84% | -84% |
| Afternoon (12–6pm) | 12535 | 57 | 4% | 2% | -47% | -86% | -86% |
| Evening (6pm–12am) | 14117 | 43 | 4% | 2% | -65% | -90% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,902 |
| Time from buy to best bounce (bounced bets) | 51 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/10 5:44:51 AM | SILVER | UP | 9 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 11/10 5:44:51 AM | SOL | DOWN | 9 sec | -0.010% | 0¢ | ❌ Lost | $0.00 |
| 11/10 5:44:51 AM | USDJPY | UP | 9 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/10 5:44:51 AM | AUDUSD | UP | 9 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/10 5:44:35 AM | GOLD | DOWN | 25 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 11/10 5:44:20 AM | ZEC | DOWN | 40 sec | +0.106% | 0¢ | ❌ Lost | $0.00 |
| 11/10 5:44:20 AM | BRENT | UP | 40 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/10 5:44:20 AM | NATGAS | UP | 40 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/10 5:44:20 AM | PALLADIUM | UP | 40 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/10 5:44:00 AM | HYPE | UP | 60 sec | -0.186% | 0¢ | ❌ Lost | -$0.15 |
| 11/10 5:44:00 AM | COPPER | UP | 60 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/10 5:44:00 AM | EURUSD | UP | 60 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/10 5:43:44 AM | PLATINUM | UP | 76 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 11/10 5:43:44 AM | DOGE | UP | 76 sec | -0.120% | 0¢ | ❌ Lost | $0.00 |
| 11/10 5:43:28 AM | BTC | UP | 1.5 min | -0.124% | 1¢ | ❌ Lost | -$0.15 |
| 11/10 5:43:28 AM | NEAR | UP | 1.5 min | -0.380% | 0¢ | ❌ Lost | $0.00 |
| 11/10 5:43:28 AM | XRP | UP | 1.5 min | -0.223% | 1¢ | ❌ Lost | -$0.15 |
| 11/10 5:42:53 AM | ETH | UP | 2.1 min | -0.169% | 1¢ | ❌ Lost | -$0.15 |
| 11/10 5:42:07 AM | BNB | UP | 2.9 min | -0.175% | 1¢ | ❌ Lost | -$0.15 |
| 11/10 2:29:44 AM | WTI | UP | 15 sec | — | 0¢ | ❌ Lost | $0.00 |
| 11/10 2:29:44 AM | USDCAD | UP | 15 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/10 2:29:44 AM | SILVER | DOWN | 15 sec | — | 0¢ | ❌ Lost | $0.00 |
| 11/10 2:29:44 AM | BRENT | UP | 15 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/10 2:29:28 AM | 5YRRATE | UP | 31 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/10 2:29:28 AM | 10YRRATE | UP | 31 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/10 2:29:28 AM | 30YRRATE | UP | 31 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/10 2:29:12 AM | 2YRRATE | UP | 47 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/10 2:29:12 AM | GOLD | UP | 47 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 11/10 2:28:56 AM | SOL | DOWN | 63 sec | +0.120% | 0¢ | ❌ Lost | $0.00 |
| 11/10 2:28:56 AM | USDJPY | UP | 63 sec | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
