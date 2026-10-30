# 15-Minute 1¢ Study

*Updated Fri Oct 30, 6:58 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 3165 finished bets | 1% | $80.15 | +23% | +2.53¢ | $76.35 / $3.80 |

*Expect about **98 buys a day** (~$14.72/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 2926 | $30.20 | +9% |
| Volatility model ≥ 2%, hold to the close | 5859 | -$10.10 | -1% |
| Volatility model ≥ 5%, sell at 50¢ | 3165 | -$74.10 | -21% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 39386 | 39367 | 144 (0%) | 1.07% | -$2,793.30 (-58%) | Hold to the close: -$2,793.30 (-58%) |

*In play or awaiting result: 18. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 24124 | 4.6% | 0.4% (93) | -685% | ❌ Worse |
| Momentum model | 24124 | 4.5% | 0.4% (93) | -708% | ❌ Worse |
| Mean-reversion model | 24124 | 8.0% | 0.4% (93) | -835% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 24124 | 93 | -51% | -88% | -87% | -85% |
| Volatility model ≥ 2% | 5859 | 50 | -1% | -79% | -77% | -74% |
| Volatility model ≥ 5% | 3165 | 31 | +23% | -76% | -74% | -70% |
| Volatility model ≥ 10% | 1786 | 19 | +52% | -68% | -67% | -64% |
| Momentum model ≥ 2% | 4831 | 34 | -15% | -81% | -80% | -77% |
| Momentum model ≥ 5% | 2926 | 25 | +9% | -78% | -78% | -74% |
| Momentum model ≥ 10% | 1908 | 17 | +24% | -73% | -72% | -68% |
| Mean-reversion model ≥ 2% | 9911 | 64 | -29% | -83% | -83% | -80% |
| Mean-reversion model ≥ 5% | 6939 | 54 | -14% | -81% | -80% | -77% |
| Mean-reversion model ≥ 10% | 4620 | 39 | -4% | -79% | -78% | -76% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 24325 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 9521 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 5521 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 39367 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 144 | 0% | -$2,793.30 | -58% | — |
| Sell at 2¢ | 1516 | 4% | -$4,219.14 | -88% | 47 sec |
| Sell at 3¢ | 1045 | 3% | -$4,205.75 | -87% | 49 sec |
| Sell at 5¢ | 729 | 2% | -$4,125.45 | -86% | 63 sec |
| Sell at 10¢ | 440 | 1% | -$3,952.90 | -82% | 65 sec |
| Sell at 25¢ | 228 | 1% | -$3,662.62 | -76% | 86 sec |
| Sell at 50¢ | 147 | 0% | -$3,341.05 | -69% | 1.9 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 9 | 0 | 33% | 22% | -100% | -42% | -13% |
| 5–10 min | 1832 | 8 | 11% | 4% | -58% | -80% | -81% |
| 2–5 min | 12550 | 69 | 7% | 3% | -46% | -87% | -86% |
| 1–2 min | 9968 | 34 | 3% | 2% | -63% | -92% | -92% |
| Under 1 min | 15008 | 33 | 1% | 0% | -69% | -87% | -86% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 2721 | 12 | 5% | 3% | -44% | -88% | -88% |
| HYPE | 2718 | 8 | 5% | 3% | -64% | -89% | -87% |
| BNB | 2714 | 15 | 5% | 3% | -31% | -85% | -84% |
| SOL | 2710 | 7 | 4% | 2% | -67% | -91% | -91% |
| ETH | 2703 | 11 | 6% | 3% | -51% | -86% | -85% |
| DOGE | 2703 | 6 | 4% | 2% | -72% | -90% | -89% |
| BTC | 2686 | 13 | 5% | 2% | -35% | -88% | -89% |
| NEAR | 2685 | 12 | 5% | 2% | -42% | -83% | -83% |
| XRP | 2685 | 11 | 3% | 1% | -50% | -89% | -89% |
| GOLD | 1492 | 5 | 4% | 2% | -60% | -82% | -84% |
| SILVER | 1457 | 7 | 4% | 2% | -43% | -82% | -81% |
| WTI | 1441 | 4 | 3% | 1% | -67% | -92% | -93% |
| PLATINUM | 1294 | 3 | 2% | 1% | -78% | -96% | -96% |
| COPPER | 1232 | 5 | 1% | 1% | -62% | -75% | -75% |
| EURUSD | 1231 | 3 | 2% | 1% | -77% | -88% | -88% |
| NATGAS | 1187 | 7 | 2% | 1% | -45% | -80% | -80% |
| GBPUSD | 1164 | 2 | 2% | 1% | -84% | -96% | -96% |
| PALLADIUM | 1159 | 2 | 1% | 0% | -84% | -90% | -90% |
| USDJPY | 1150 | 5 | 2% | 1% | -59% | -97% | -96% |
| AUDUSD | 691 | 4 | 2% | 1% | -46% | -84% | -83% |
| USDCAD | 661 | 0 | 2% | 0% | -100% | -97% | -98% |
| BRENT | 259 | 0 | 1% | 0% | -100% | -99% | -98% |
| 10YRRATE | 167 | 0 | 4% | 1% | -100% | -93% | -91% |
| 30YRRATE | 161 | 0 | 1% | 0% | -100% | -98% | -97% |
| 2YRRATE | 156 | 1 | 4% | 1% | -40% | -32% | -32% |
| 5YRRATE | 140 | 1 | 6% | 3% | -33% | -89% | -91% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 20001 | 79 | 4% | 2% | -55% | -88% | -87% |
| DOWN (bought NO) | 19366 | 65 | 4% | 2% | -62% | -88% | -88% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 3901 | 19 | 2% | 1% | -16% | -81% | -81% |
| 0.05–0.1% | 4131 | 14 | 3% | 2% | -49% | -92% | -92% |
| 0.1–0.2% | 6259 | 22 | 4% | 2% | -56% | -90% | -89% |
| 0.2–0.5% | 7250 | 30 | 6% | 3% | -54% | -87% | -86% |
| Over 0.5% | 2780 | 10 | 7% | 3% | -63% | -86% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 9916 | 36 | 4% | 2% | -59% | -86% | -86% |
| Morning (6am–12pm) | 9693 | 43 | 4% | 2% | -50% | -86% | -85% |
| Afternoon (12–6pm) | 9178 | 31 | 4% | 2% | -60% | -88% | -88% |
| Evening (6pm–12am) | 10580 | 34 | 3% | 2% | -63% | -91% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,472 |
| Time from buy to best bounce (bounced bets) | 51 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/30 6:58:24 AM | ETH | DOWN | 1.6 min | +0.132% | — | In play | — |
| 10/30 6:58:24 AM | HYPE | UP | 1.6 min | -0.278% | — | In play | — |
| 10/30 6:58:06 AM | DOGE | DOWN | 1.9 min | +0.176% | — | In play | — |
| 10/30 6:58:06 AM | USDJPY | UP | 1.9 min | — | — | In play | — |
| 10/30 6:58:06 AM | BTC | DOWN | 1.9 min | +0.111% | — | In play | — |
| 10/30 6:57:50 AM | BRENT | UP | 2.2 min | — | — | In play | — |
| 10/30 6:57:34 AM | WTI | UP | 2.4 min | — | — | In play | — |
| 10/30 6:57:19 AM | SOL | DOWN | 2.7 min | +0.253% | — | In play | — |
| 10/30 6:55:23 AM | BNB | DOWN | 4.6 min | +0.201% | — | In play | — |
| 10/30 6:14:57 AM | PALLADIUM | UP | 3 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/30 6:14:41 AM | XRP | UP | 19 sec | -0.104% | 0¢ | ❌ Lost | -$0.15 |
| 10/30 6:14:41 AM | GBPUSD | UP | 19 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/30 6:14:25 AM | EURUSD | UP | 35 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/30 6:14:25 AM | NEAR | DOWN | 35 sec | +0.130% | 0¢ | ❌ Lost | $0.00 |
| 10/30 6:14:10 AM | GOLD | UP | 49 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/30 6:13:51 AM | SILVER | UP | 68 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/30 6:13:51 AM | USDCAD | UP | 68 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/30 6:13:51 AM | HYPE | DOWN | 68 sec | +0.327% | 0¢ | ❌ Lost | $0.00 |
| 10/30 6:13:35 AM | ETH | DOWN | 84 sec | +0.149% | 0¢ | ❌ Lost | -$0.15 |
| 10/30 6:13:19 AM | 5YRRATE | DOWN | 1.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/30 6:13:19 AM | 2YRRATE | DOWN | 1.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/30 6:13:19 AM | BRENT | UP | 1.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/30 6:13:19 AM | NATGAS | DOWN | 1.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/30 6:13:19 AM | WTI | UP | 1.7 min | — | 8¢ | ❌ Lost | -$0.15 |
| 10/30 6:13:19 AM | 30YRRATE | DOWN | 1.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/30 6:13:19 AM | 10YRRATE | DOWN | 1.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/30 6:12:31 AM | COPPER | DOWN | 2.5 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/30 6:12:15 AM | SOL | DOWN | 2.8 min | +0.284% | 1¢ | ❌ Lost | $0.00 |
| 10/30 6:12:15 AM | ZEC | DOWN | 2.8 min | +0.696% | 1¢ | ❌ Lost | -$0.15 |
| 10/30 6:12:15 AM | BTC | DOWN | 2.8 min | +0.177% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
