# 15-Minute 1¢ Study

*Updated Wed Nov 18, 2:44 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 4503 finished bets | 1% | $216.45 | +44% | +4.81¢ | $81.75 / $134.70 |

*Expect about **88 buys a day** (~$13.22/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 4241 | $116.50 | +25% |
| Volatility model ≥ 2%, hold to the close | 8401 | $81.30 | +8% |
| Momentum model ≥ 2%, hold to the close | 6972 | -$2.10 | -0% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 60522 | 60469 | 237 (0%) | 1.07% | -$4,042.20 (-55%) | Hold to the close: -$4,042.20 (-55%) |

*In play or awaiting result: 25. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 36195 | 4.5% | 0.4% (154) | -623% | ❌ Worse |
| Momentum model | 36195 | 4.4% | 0.4% (154) | -648% | ❌ Worse |
| Mean-reversion model | 36195 | 7.9% | 0.4% (154) | -756% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 36195 | 154 | -45% | -87% | -87% | -84% |
| Volatility model ≥ 2% | 8401 | 78 | +8% | -77% | -76% | -72% |
| Volatility model ≥ 5% | 4503 | 51 | +44% | -72% | -70% | -67% |
| Volatility model ≥ 10% | 2586 | 30 | +68% | -63% | -61% | -58% |
| Momentum model ≥ 2% | 6972 | 57 | -0% | -79% | -78% | -74% |
| Momentum model ≥ 5% | 4241 | 41 | +25% | -74% | -74% | -70% |
| Momentum model ≥ 10% | 2762 | 26 | +34% | -67% | -66% | -62% |
| Mean-reversion model ≥ 2% | 14835 | 108 | -20% | -82% | -82% | -79% |
| Mean-reversion model ≥ 5% | 10317 | 89 | -4% | -80% | -79% | -77% |
| Mean-reversion model ≥ 10% | 6853 | 64 | +6% | -77% | -77% | -74% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 36401 | 5% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 14396 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 9672 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 60469 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 237 | 0% | -$4,042.20 | -55% | — |
| Sell at 2¢ | 2442 | 4% | -$6,431.28 | -87% | 47 sec |
| Sell at 3¢ | 1651 | 3% | -$6,422.31 | -87% | 48 sec |
| Sell at 5¢ | 1128 | 2% | -$6,305.00 | -86% | 63 sec |
| Sell at 10¢ | 687 | 1% | -$6,054.23 | -82% | 65 sec |
| Sell at 25¢ | 368 | 1% | -$5,596.12 | -76% | 80 sec |
| Sell at 50¢ | 244 | 0% | -$5,041.20 | -68% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 13 | 0 | 31% | 23% | -100% | -47% | -20% |
| 5–10 min | 3060 | 17 | 11% | 4% | -47% | -81% | -82% |
| 2–5 min | 19612 | 108 | 7% | 3% | -46% | -87% | -86% |
| 1–2 min | 15158 | 51 | 3% | 2% | -62% | -92% | -92% |
| Under 1 min | 22626 | 61 | 1% | 0% | -61% | -86% | -85% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 4070 | 19 | 5% | 3% | -39% | -88% | -87% |
| SOL | 4068 | 19 | 4% | 2% | -40% | -86% | -86% |
| HYPE | 4062 | 12 | 5% | 2% | -63% | -89% | -88% |
| DOGE | 4051 | 11 | 4% | 2% | -66% | -90% | -89% |
| BNB | 4050 | 21 | 5% | 2% | -34% | -85% | -85% |
| ETH | 4043 | 19 | 7% | 3% | -41% | -82% | -82% |
| BTC | 4025 | 21 | 5% | 2% | -29% | -86% | -88% |
| NEAR | 4024 | 18 | 5% | 2% | -42% | -85% | -86% |
| XRP | 4008 | 16 | 3% | 2% | -49% | -89% | -88% |
| GOLD | 2152 | 6 | 5% | 2% | -66% | -82% | -84% |
| WTI | 2134 | 7 | 4% | 1% | -60% | -91% | -92% |
| SILVER | 2088 | 9 | 5% | 2% | -49% | -83% | -83% |
| PLATINUM | 1903 | 4 | 3% | 1% | -80% | -95% | -95% |
| EURUSD | 1856 | 7 | 2% | 1% | -65% | -91% | -90% |
| COPPER | 1790 | 6 | 2% | 1% | -69% | -76% | -76% |
| GBPUSD | 1783 | 6 | 2% | 1% | -69% | -96% | -96% |
| NATGAS | 1753 | 10 | 2% | 1% | -47% | -75% | -75% |
| USDJPY | 1744 | 6 | 2% | 1% | -68% | -97% | -96% |
| PALLADIUM | 1711 | 4 | 1% | 0% | -78% | -93% | -93% |
| AUDUSD | 1297 | 6 | 2% | 1% | -57% | -89% | -89% |
| USDCAD | 1240 | 1 | 3% | 1% | -92% | -95% | -96% |
| BRENT | 865 | 0 | 2% | 1% | -100% | -97% | -98% |
| 10YRRATE | 441 | 2 | 3% | 1% | -58% | -73% | -71% |
| 2YRRATE | 425 | 4 | 4% | 2% | -12% | -50% | -48% |
| 30YRRATE | 409 | 0 | 2% | 1% | -100% | -96% | -94% |
| 5YRRATE | 396 | 2 | 4% | 2% | -53% | -93% | -95% |
| INX | 81 | 1 | 2% | 1% | +15% | -96% | -97% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 30817 | 121 | 4% | 2% | -55% | -88% | -88% |
| DOWN (bought NO) | 29652 | 116 | 4% | 2% | -55% | -86% | -87% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 5469 | 25 | 2% | 1% | -18% | -78% | -77% |
| 0.05–0.1% | 5923 | 24 | 3% | 2% | -37% | -91% | -91% |
| 0.1–0.2% | 9122 | 34 | 5% | 2% | -52% | -89% | -89% |
| 0.2–0.5% | 11289 | 50 | 7% | 3% | -50% | -86% | -86% |
| Over 0.5% | 4589 | 23 | 7% | 3% | -48% | -86% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 14682 | 45 | 4% | 2% | -65% | -88% | -88% |
| Morning (6am–12pm) | 14416 | 78 | 5% | 2% | -38% | -85% | -84% |
| Afternoon (12–6pm) | 14813 | 65 | 4% | 2% | -48% | -87% | -87% |
| Evening (6pm–12am) | 16558 | 49 | 4% | 2% | -66% | -90% | -89% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 5,066 |
| Time from buy to best bounce (bounced bets) | 50 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/18 2:44:34 AM | AUDUSD | DOWN | 26 sec | — | — | In play | — |
| 11/18 2:44:34 AM | XRP | UP | 26 sec | -0.110% | — | In play | — |
| 11/18 2:44:34 AM | HYPE | DOWN | 26 sec | -0.009% | — | In play | — |
| 11/18 2:44:34 AM | ZEC | DOWN | 26 sec | +0.006% | — | In play | — |
| 11/18 2:44:34 AM | COPPER | UP | 26 sec | — | — | In play | — |
| 11/18 2:44:18 AM | 5YRRATE | UP | 42 sec | — | — | In play | — |
| 11/18 2:44:18 AM | SILVER | DOWN | 42 sec | — | — | In play | — |
| 11/18 2:44:03 AM | BNB | UP | 56 sec | -0.142% | — | In play | — |
| 11/18 2:44:03 AM | 10YRRATE | UP | 56 sec | — | — | In play | — |
| 11/18 2:44:03 AM | 30YRRATE | UP | 56 sec | — | — | In play | — |
| 11/18 2:44:03 AM | PALLADIUM | DOWN | 56 sec | — | — | In play | — |
| 11/18 2:43:47 AM | USDCAD | UP | 72 sec | — | — | In play | — |
| 11/18 2:43:47 AM | SOL | DOWN | 72 sec | +0.097% | — | In play | — |
| 11/18 2:43:31 AM | DOGE | UP | 88 sec | -0.219% | — | In play | — |
| 11/18 2:43:31 AM | EURUSD | DOWN | 88 sec | — | — | In play | — |
| 11/18 2:43:15 AM | NATGAS | DOWN | 1.7 min | — | — | In play | — |
| 11/18 2:41:38 AM | GBPUSD | DOWN | 3.4 min | — | — | In play | — |
| 11/18 2:41:06 AM | GOLD | DOWN | 3.9 min | — | — | In play | — |
| 11/18 2:40:18 AM | NEAR | UP | 4.7 min | -0.702% | — | In play | — |
| 11/18 2:29:54 AM | 5YRRATE | UP | 5 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/18 2:29:54 AM | XRP | DOWN | 5 sec | -0.040% | 0¢ | ❌ Lost | $0.00 |
| 11/18 2:29:38 AM | BTC | UP | 21 sec | -0.033% | 0¢ | ❌ Lost | -$0.15 |
| 11/18 2:29:22 AM | BNB | DOWN | 37 sec | -0.010% | 1¢ | ❌ Lost | -$0.15 |
| 11/18 2:29:22 AM | WTI | DOWN | 37 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/18 2:29:22 AM | USDJPY | DOWN | 37 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/18 2:29:22 AM | DOGE | DOWN | 37 sec | +0.050% | 0¢ | ❌ Lost | $0.00 |
| 11/18 2:29:22 AM | COPPER | DOWN | 37 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/18 2:29:06 AM | AUDUSD | DOWN | 53 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/18 2:29:06 AM | PALLADIUM | DOWN | 53 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/18 2:29:06 AM | ETH | DOWN | 53 sec | +0.061% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
