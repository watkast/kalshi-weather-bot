# 15-Minute 1¢ Study

*Updated Thu Nov 12, 7:27 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 4248 finished bets | 1% | $172.70 | +37% | +4.07¢ | $83.35 / $89.35 |

*Expect about **94 buys a day** (~$14.06/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 3984 | $100.45 | +23% |
| Volatility model ≥ 2%, hold to the close | 7820 | $39.35 | +4% |
| Momentum model ≥ 2%, hold to the close | 6493 | -$18.10 | -2% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 54791 | 54759 | 209 (0%) | 1.07% | -$3,756.20 (-56%) | Hold to the close: -$3,756.20 (-56%) |

*In play or awaiting result: 20. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 32827 | 4.7% | 0.4% (132) | -670% | ❌ Worse |
| Momentum model | 32827 | 4.6% | 0.4% (132) | -695% | ❌ Worse |
| Mean-reversion model | 32827 | 8.0% | 0.4% (132) | -812% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 32827 | 132 | -49% | -87% | -87% | -84% |
| Volatility model ≥ 2% | 7820 | 70 | +4% | -77% | -76% | -72% |
| Volatility model ≥ 5% | 4248 | 46 | +37% | -72% | -70% | -67% |
| Volatility model ≥ 10% | 2456 | 28 | +64% | -62% | -61% | -57% |
| Momentum model ≥ 2% | 6493 | 52 | -2% | -78% | -77% | -74% |
| Momentum model ≥ 5% | 3984 | 38 | +23% | -74% | -73% | -69% |
| Momentum model ≥ 10% | 2611 | 25 | +35% | -66% | -65% | -61% |
| Mean-reversion model ≥ 2% | 13550 | 92 | -26% | -82% | -82% | -79% |
| Mean-reversion model ≥ 5% | 9469 | 78 | -9% | -80% | -79% | -77% |
| Mean-reversion model ≥ 10% | 6320 | 56 | +1% | -77% | -77% | -75% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 33032 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 13157 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 8570 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 54759 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 209 | 0% | -$3,756.20 | -56% | — |
| Sell at 2¢ | 2183 | 4% | -$5,820.62 | -87% | 47 sec |
| Sell at 3¢ | 1487 | 3% | -$5,808.27 | -87% | 49 sec |
| Sell at 5¢ | 1026 | 2% | -$5,693.30 | -85% | 63 sec |
| Sell at 10¢ | 621 | 1% | -$5,462.69 | -82% | 65 sec |
| Sell at 25¢ | 328 | 1% | -$5,078.52 | -76% | 82 sec |
| Sell at 50¢ | 215 | 0% | -$4,600.95 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 13 | 0 | 31% | 23% | -100% | -47% | -20% |
| 5–10 min | 2733 | 13 | 11% | 4% | -55% | -81% | -82% |
| 2–5 min | 17708 | 96 | 7% | 3% | -47% | -87% | -86% |
| 1–2 min | 13809 | 45 | 3% | 2% | -64% | -92% | -92% |
| Under 1 min | 20496 | 55 | 1% | 0% | -62% | -85% | -84% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 3697 | 17 | 5% | 3% | -40% | -88% | -87% |
| SOL | 3693 | 16 | 4% | 2% | -45% | -87% | -87% |
| HYPE | 3686 | 11 | 5% | 2% | -63% | -89% | -88% |
| BNB | 3678 | 19 | 5% | 2% | -35% | -86% | -85% |
| DOGE | 3674 | 8 | 4% | 2% | -73% | -90% | -90% |
| ETH | 3669 | 16 | 7% | 3% | -46% | -82% | -81% |
| NEAR | 3649 | 17 | 5% | 2% | -40% | -85% | -85% |
| BTC | 3649 | 17 | 5% | 2% | -36% | -87% | -88% |
| XRP | 3637 | 13 | 3% | 1% | -55% | -89% | -89% |
| GOLD | 1976 | 5 | 5% | 2% | -69% | -82% | -84% |
| WTI | 1962 | 6 | 4% | 2% | -63% | -91% | -92% |
| SILVER | 1926 | 9 | 5% | 2% | -45% | -83% | -82% |
| PLATINUM | 1757 | 4 | 3% | 1% | -79% | -96% | -95% |
| EURUSD | 1695 | 6 | 3% | 1% | -67% | -90% | -89% |
| COPPER | 1642 | 6 | 2% | 1% | -66% | -74% | -74% |
| GBPUSD | 1623 | 6 | 2% | 1% | -65% | -96% | -96% |
| NATGAS | 1611 | 9 | 2% | 1% | -48% | -73% | -73% |
| USDJPY | 1596 | 6 | 2% | 1% | -65% | -97% | -96% |
| PALLADIUM | 1573 | 4 | 1% | 1% | -76% | -92% | -92% |
| AUDUSD | 1151 | 6 | 2% | 1% | -51% | -88% | -89% |
| USDCAD | 1107 | 0 | 3% | 1% | -100% | -96% | -96% |
| BRENT | 710 | 0 | 2% | 1% | -100% | -97% | -97% |
| 10YRRATE | 362 | 2 | 4% | 2% | -48% | -67% | -65% |
| 2YRRATE | 344 | 4 | 4% | 2% | +9% | -39% | -37% |
| 30YRRATE | 342 | 0 | 2% | 1% | -100% | -96% | -94% |
| 5YRRATE | 318 | 2 | 4% | 2% | -41% | -92% | -94% |
| INX | 32 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 27838 | 109 | 4% | 2% | -55% | -88% | -88% |
| DOWN (bought NO) | 26921 | 100 | 4% | 2% | -57% | -86% | -86% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 5216 | 25 | 2% | 1% | -15% | -77% | -77% |
| 0.05–0.1% | 5609 | 20 | 3% | 2% | -45% | -91% | -91% |
| 0.1–0.2% | 8460 | 31 | 5% | 2% | -54% | -89% | -89% |
| 0.2–0.5% | 9960 | 41 | 6% | 3% | -54% | -87% | -86% |
| Over 0.5% | 3779 | 17 | 7% | 3% | -53% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 13478 | 44 | 4% | 2% | -63% | -88% | -88% |
| Morning (6am–12pm) | 13188 | 60 | 4% | 2% | -48% | -85% | -84% |
| Afternoon (12–6pm) | 13132 | 58 | 4% | 2% | -48% | -86% | -86% |
| Evening (6pm–12am) | 14961 | 47 | 4% | 2% | -64% | -89% | -89% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,846 |
| Time from buy to best bounce (bounced bets) | 51 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/12 7:27:40 AM | WTI | DOWN | 2.3 min | — | — | In play | — |
| 11/12 7:27:40 AM | HYPE | UP | 2.3 min | -0.427% | — | In play | — |
| 11/12 7:27:24 AM | BRENT | DOWN | 2.6 min | — | — | In play | — |
| 11/12 7:26:36 AM | SOL | UP | 3.4 min | -0.600% | — | In play | — |
| 11/12 7:26:36 AM | GOLD | DOWN | 3.4 min | — | — | In play | — |
| 11/12 7:26:04 AM | XRP | UP | 3.9 min | -0.642% | — | In play | — |
| 11/12 7:25:17 AM | ETH | UP | 4.7 min | -0.817% | — | In play | — |
| 11/12 7:25:17 AM | ZEC | UP | 4.7 min | -1.321% | — | In play | — |
| 11/12 7:25:17 AM | DOGE | UP | 4.7 min | -0.701% | — | In play | — |
| 11/12 7:25:01 AM | BTC | UP | 5.0 min | -0.614% | — | In play | — |
| 11/12 7:24:14 AM | BNB | UP | 5.8 min | -0.653% | — | In play | — |
| 11/12 7:14:49 AM | USDJPY | UP | 10 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/12 7:14:49 AM | EURUSD | DOWN | 10 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/12 7:14:49 AM | 5YRRATE | UP | 10 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/12 7:14:34 AM | PLATINUM | DOWN | 26 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/12 7:14:18 AM | GBPUSD | UP | 42 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/12 7:13:46 AM | BRENT | UP | 74 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/12 7:13:31 AM | 30YRRATE | UP | 89 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/12 7:13:15 AM | 10YRRATE | UP | 1.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/12 7:12:43 AM | ZEC | DOWN | 2.3 min | +0.878% | 1¢ | ❌ Lost | -$0.15 |
| 11/12 7:12:43 AM | NEAR | UP | 2.3 min | -0.769% | 0¢ | ❌ Lost | -$0.15 |
| 11/12 7:12:27 AM | WTI | UP | 2.5 min | — | 0¢ | ❌ Lost | $0.00 |
| 11/12 7:12:11 AM | USDCAD | DOWN | 2.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/12 7:11:55 AM | SOL | UP | 3.1 min | -0.478% | 1¢ | ❌ Lost | -$0.15 |
| 11/12 7:11:55 AM | ETH | UP | 3.1 min | -0.352% | 5¢ | ❌ Lost | -$0.15 |
| 11/12 7:11:55 AM | BNB | UP | 3.1 min | -0.319% | 11¢ | ❌ Lost | -$0.15 |
| 11/12 7:11:24 AM | DOGE | UP | 3.6 min | -0.455% | 1¢ | ❌ Lost | -$0.15 |
| 11/12 7:11:24 AM | BTC | UP | 3.6 min | -0.311% | 14¢ | ❌ Lost | -$0.15 |
| 11/12 7:11:08 AM | XRP | UP | 3.9 min | -0.591% | 1¢ | ❌ Lost | -$0.15 |
| 11/12 7:10:52 AM | HYPE | UP | 4.1 min | -0.601% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
