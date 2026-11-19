# 15-Minute 1¢ Study

*Updated Thu Nov 19, 2:13 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 4569 finished bets | 1% | $210.90 | +42% | +4.62¢ | $77.70 / $133.20 |

*Expect about **87 buys a day** (~$13.03/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 4306 | $111.10 | +24% |
| Volatility model ≥ 2%, hold to the close | 8522 | $68.40 | +7% |
| Momentum model ≥ 2%, hold to the close | 7065 | -$11.25 | -1% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 62134 | 62092 | 240 (0%) | 1.07% | -$4,194.15 (-56%) | Hold to the close: -$4,194.15 (-56%) |

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
| Volatility model | 36888 | 4.5% | 0.4% (154) | -637% | ❌ Worse |
| Momentum model | 36888 | 4.4% | 0.4% (154) | -662% | ❌ Worse |
| Mean-reversion model | 36888 | 7.9% | 0.4% (154) | -773% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 36888 | 154 | -46% | -87% | -87% | -84% |
| Volatility model ≥ 2% | 8522 | 78 | +7% | -77% | -76% | -72% |
| Volatility model ≥ 5% | 4569 | 51 | +42% | -72% | -71% | -67% |
| Volatility model ≥ 10% | 2628 | 30 | +67% | -63% | -62% | -58% |
| Momentum model ≥ 2% | 7065 | 57 | -1% | -79% | -78% | -75% |
| Momentum model ≥ 5% | 4306 | 41 | +24% | -75% | -74% | -70% |
| Momentum model ≥ 10% | 2807 | 26 | +32% | -67% | -66% | -62% |
| Mean-reversion model ≥ 2% | 15076 | 108 | -21% | -82% | -82% | -79% |
| Mean-reversion model ≥ 5% | 10493 | 89 | -6% | -80% | -79% | -77% |
| Mean-reversion model ≥ 10% | 6977 | 64 | +4% | -77% | -77% | -74% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 37094 | 5% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 14869 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 10129 | 3% | 2% | 1% | 1% | 0% | 0% |
| **All** | 62092 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 240 | 0% | -$4,194.15 | -56% | — |
| Sell at 2¢ | 2523 | 4% | -$6,604.17 | -87% | 47 sec |
| Sell at 3¢ | 1704 | 3% | -$6,595.59 | -87% | 48 sec |
| Sell at 5¢ | 1165 | 2% | -$6,474.90 | -86% | 63 sec |
| Sell at 10¢ | 713 | 1% | -$6,214.12 | -82% | 65 sec |
| Sell at 25¢ | 381 | 1% | -$5,733.04 | -76% | 80 sec |
| Sell at 50¢ | 247 | 0% | -$5,186.90 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 13 | 0 | 31% | 23% | -100% | -47% | -20% |
| 5–10 min | 3167 | 17 | 11% | 4% | -49% | -81% | -82% |
| 2–5 min | 20134 | 108 | 7% | 3% | -47% | -86% | -86% |
| 1–2 min | 15540 | 52 | 3% | 2% | -63% | -92% | -92% |
| Under 1 min | 23238 | 63 | 1% | 0% | -61% | -86% | -86% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 4148 | 19 | 5% | 2% | -39% | -88% | -87% |
| SOL | 4145 | 19 | 4% | 2% | -41% | -86% | -86% |
| HYPE | 4137 | 12 | 4% | 2% | -63% | -89% | -88% |
| DOGE | 4127 | 11 | 4% | 2% | -66% | -89% | -89% |
| BNB | 4126 | 21 | 5% | 2% | -36% | -85% | -85% |
| ETH | 4122 | 19 | 7% | 3% | -42% | -82% | -82% |
| BTC | 4103 | 21 | 5% | 2% | -31% | -86% | -88% |
| NEAR | 4101 | 18 | 5% | 2% | -43% | -85% | -86% |
| XRP | 4085 | 16 | 3% | 2% | -50% | -89% | -88% |
| GOLD | 2217 | 6 | 5% | 2% | -67% | -82% | -84% |
| WTI | 2195 | 7 | 4% | 2% | -61% | -91% | -92% |
| SILVER | 2156 | 9 | 5% | 2% | -50% | -83% | -83% |
| PLATINUM | 1964 | 5 | 3% | 1% | -76% | -95% | -95% |
| EURUSD | 1922 | 7 | 3% | 1% | -66% | -91% | -90% |
| GBPUSD | 1851 | 8 | 2% | 1% | -60% | -96% | -95% |
| COPPER | 1846 | 6 | 2% | 1% | -70% | -76% | -76% |
| USDJPY | 1807 | 6 | 2% | 1% | -69% | -96% | -96% |
| NATGAS | 1806 | 10 | 2% | 1% | -48% | -76% | -75% |
| PALLADIUM | 1766 | 4 | 1% | 0% | -79% | -93% | -93% |
| AUDUSD | 1358 | 6 | 2% | 1% | -59% | -90% | -89% |
| USDCAD | 1297 | 1 | 3% | 1% | -93% | -95% | -96% |
| BRENT | 919 | 0 | 2% | 1% | -100% | -97% | -97% |
| 10YRRATE | 477 | 2 | 3% | 1% | -61% | -75% | -73% |
| 2YRRATE | 453 | 4 | 4% | 2% | -18% | -52% | -51% |
| 30YRRATE | 439 | 0 | 3% | 1% | -100% | -96% | -93% |
| 5YRRATE | 428 | 2 | 4% | 2% | -56% | -94% | -95% |
| INX | 97 | 1 | 2% | 1% | -4% | -96% | -97% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 31658 | 123 | 4% | 2% | -55% | -88% | -88% |
| DOWN (bought NO) | 30434 | 117 | 4% | 2% | -56% | -86% | -87% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 5540 | 25 | 2% | 1% | -18% | -78% | -78% |
| 0.05–0.1% | 6024 | 24 | 3% | 2% | -38% | -91% | -91% |
| 0.1–0.2% | 9295 | 34 | 5% | 2% | -53% | -89% | -89% |
| 0.2–0.5% | 11533 | 50 | 7% | 3% | -51% | -86% | -86% |
| Over 0.5% | 4693 | 23 | 7% | 3% | -49% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 15189 | 47 | 4% | 2% | -65% | -88% | -88% |
| Morning (6am–12pm) | 14806 | 79 | 5% | 2% | -39% | -85% | -84% |
| Afternoon (12–6pm) | 15170 | 65 | 4% | 2% | -50% | -87% | -87% |
| Evening (6pm–12am) | 16927 | 49 | 4% | 2% | -67% | -89% | -89% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,996 |
| Time from buy to best bounce (bounced bets) | 50 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/19 2:13:29 PM | GBPUSD | UP | 1.5 min | — | — | In play | — |
| 11/19 2:13:29 PM | HYPE | UP | 1.5 min | -0.532% | — | In play | — |
| 11/19 2:13:12 PM | NEAR | UP | 1.8 min | -0.611% | — | In play | — |
| 11/19 2:13:12 PM | XRP | UP | 1.8 min | -0.291% | — | In play | — |
| 11/19 2:12:24 PM | SOL | UP | 2.6 min | -0.386% | — | In play | — |
| 11/19 2:11:51 PM | BNB | UP | 3.1 min | -0.329% | — | In play | — |
| 11/19 2:11:51 PM | DOGE | UP | 3.1 min | -0.426% | — | In play | — |
| 11/19 2:11:19 PM | EURUSD | UP | 3.7 min | — | — | In play | — |
| 11/19 1:59:53 PM | BTC | UP | 7 sec | +0.023% | 0¢ | ❌ Lost | $0.00 |
| 11/19 1:59:37 PM | EURUSD | DOWN | 23 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/19 1:59:37 PM | 2YRRATE | UP | 23 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/19 1:59:37 PM | USDJPY | UP | 23 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/19 1:59:37 PM | SOL | DOWN | 23 sec | +0.135% | 0¢ | ❌ Lost | -$0.15 |
| 11/19 1:59:37 PM | INX | UP | 23 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/19 1:59:21 PM | COPPER | UP | 39 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/19 1:59:21 PM | NATGAS | UP | 39 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/19 1:59:06 PM | BNB | UP | 54 sec | -0.138% | 1¢ | ❌ Lost | -$0.15 |
| 11/19 1:59:06 PM | GBPUSD | DOWN | 54 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/19 1:59:06 PM | DOGE | UP | 54 sec | -0.218% | 0¢ | ❌ Lost | $0.00 |
| 11/19 1:59:06 PM | XRP | UP | 54 sec | -0.249% | 0¢ | ❌ Lost | $0.00 |
| 11/19 1:58:50 PM | ETH | UP | 69 sec | -0.220% | 1¢ | ❌ Lost | -$0.15 |
| 11/19 1:58:50 PM | ZEC | UP | 69 sec | -0.344% | 1¢ | ❌ Lost | -$0.15 |
| 11/19 1:58:50 PM | USDCAD | DOWN | 69 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/19 1:58:34 PM | PALLADIUM | UP | 85 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/19 1:58:34 PM | SILVER | UP | 85 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 11/19 1:58:34 PM | GOLD | UP | 85 sec | — | 0¢ | ❌ Lost | $0.00 |
| 11/19 1:58:18 PM | NEAR | UP | 1.7 min | -0.470% | 1¢ | ❌ Lost | -$0.15 |
| 11/19 1:57:44 PM | PLATINUM | UP | 2.3 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/19 1:55:35 PM | HYPE | DOWN | 4.4 min | +1.000% | 1¢ | ❌ Lost | -$0.15 |
| 11/19 1:44:51 PM | NEAR | DOWN | 8 sec | -0.151% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
