# 15-Minute 1¢ Study

*Updated Thu Nov 19, 1:52 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 4568 finished bets | 1% | $210.90 | +42% | +4.62¢ | $77.70 / $133.20 |

*Expect about **87 buys a day** (~$13.03/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 4305 | $111.10 | +24% |
| Volatility model ≥ 2%, hold to the close | 8521 | $68.40 | +7% |
| Momentum model ≥ 2%, hold to the close | 7064 | -$11.25 | -1% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 62105 | 62071 | 240 (0%) | 1.07% | -$4,191.60 (-56%) | Hold to the close: -$4,191.60 (-56%) |

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
| Volatility model | 36879 | 4.5% | 0.4% (154) | -636% | ❌ Worse |
| Momentum model | 36879 | 4.4% | 0.4% (154) | -661% | ❌ Worse |
| Mean-reversion model | 36879 | 7.9% | 0.4% (154) | -772% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 36879 | 154 | -46% | -87% | -87% | -84% |
| Volatility model ≥ 2% | 8521 | 78 | +7% | -77% | -76% | -72% |
| Volatility model ≥ 5% | 4568 | 51 | +42% | -72% | -71% | -67% |
| Volatility model ≥ 10% | 2627 | 30 | +67% | -63% | -62% | -58% |
| Momentum model ≥ 2% | 7064 | 57 | -1% | -79% | -78% | -75% |
| Momentum model ≥ 5% | 4305 | 41 | +24% | -75% | -74% | -70% |
| Momentum model ≥ 10% | 2806 | 26 | +32% | -67% | -66% | -62% |
| Mean-reversion model ≥ 2% | 15073 | 108 | -21% | -82% | -82% | -79% |
| Mean-reversion model ≥ 5% | 10491 | 89 | -6% | -80% | -79% | -77% |
| Mean-reversion model ≥ 10% | 6976 | 64 | +4% | -77% | -77% | -74% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 37085 | 5% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 14863 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 10123 | 3% | 2% | 1% | 1% | 0% | 0% |
| **All** | 62071 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 240 | 0% | -$4,191.60 | -56% | — |
| Sell at 2¢ | 2523 | 4% | -$6,601.62 | -87% | 47 sec |
| Sell at 3¢ | 1704 | 3% | -$6,593.04 | -87% | 48 sec |
| Sell at 5¢ | 1165 | 2% | -$6,472.35 | -86% | 63 sec |
| Sell at 10¢ | 713 | 1% | -$6,211.57 | -82% | 65 sec |
| Sell at 25¢ | 381 | 1% | -$5,730.49 | -76% | 80 sec |
| Sell at 50¢ | 247 | 0% | -$5,184.35 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 13 | 0 | 31% | 23% | -100% | -47% | -20% |
| 5–10 min | 3167 | 17 | 11% | 4% | -49% | -81% | -82% |
| 2–5 min | 20132 | 108 | 7% | 3% | -47% | -86% | -86% |
| 1–2 min | 15533 | 52 | 3% | 2% | -63% | -92% | -92% |
| Under 1 min | 23226 | 63 | 1% | 0% | -61% | -86% | -86% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 4147 | 19 | 5% | 2% | -39% | -88% | -87% |
| SOL | 4144 | 19 | 4% | 2% | -41% | -86% | -86% |
| HYPE | 4136 | 12 | 4% | 2% | -63% | -89% | -88% |
| DOGE | 4126 | 11 | 4% | 2% | -66% | -89% | -89% |
| BNB | 4125 | 21 | 5% | 2% | -36% | -85% | -85% |
| ETH | 4121 | 19 | 7% | 3% | -42% | -82% | -82% |
| BTC | 4102 | 21 | 5% | 2% | -31% | -86% | -88% |
| NEAR | 4100 | 18 | 5% | 2% | -43% | -85% | -86% |
| XRP | 4084 | 16 | 3% | 2% | -50% | -89% | -88% |
| GOLD | 2216 | 6 | 5% | 2% | -67% | -82% | -84% |
| WTI | 2195 | 7 | 4% | 2% | -61% | -91% | -92% |
| SILVER | 2155 | 9 | 5% | 2% | -50% | -83% | -83% |
| PLATINUM | 1963 | 5 | 3% | 1% | -76% | -95% | -95% |
| EURUSD | 1921 | 7 | 3% | 1% | -66% | -91% | -90% |
| GBPUSD | 1850 | 8 | 2% | 1% | -60% | -96% | -95% |
| COPPER | 1845 | 6 | 2% | 1% | -70% | -76% | -76% |
| USDJPY | 1806 | 6 | 2% | 1% | -69% | -96% | -96% |
| NATGAS | 1805 | 10 | 2% | 1% | -48% | -76% | -75% |
| PALLADIUM | 1765 | 4 | 1% | 0% | -79% | -93% | -93% |
| AUDUSD | 1358 | 6 | 2% | 1% | -59% | -90% | -89% |
| USDCAD | 1296 | 1 | 3% | 1% | -93% | -95% | -96% |
| BRENT | 919 | 0 | 2% | 1% | -100% | -97% | -97% |
| 10YRRATE | 477 | 2 | 3% | 1% | -61% | -75% | -73% |
| 2YRRATE | 452 | 4 | 4% | 2% | -17% | -52% | -51% |
| 30YRRATE | 439 | 0 | 3% | 1% | -100% | -96% | -93% |
| 5YRRATE | 428 | 2 | 4% | 2% | -56% | -94% | -95% |
| INX | 96 | 1 | 2% | 1% | -3% | -96% | -97% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 31642 | 123 | 4% | 2% | -55% | -88% | -88% |
| DOWN (bought NO) | 30429 | 117 | 4% | 2% | -56% | -86% | -87% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 5539 | 25 | 2% | 1% | -18% | -78% | -78% |
| 0.05–0.1% | 6024 | 24 | 3% | 2% | -38% | -91% | -91% |
| 0.1–0.2% | 9293 | 34 | 5% | 2% | -53% | -89% | -89% |
| 0.2–0.5% | 11528 | 50 | 7% | 3% | -51% | -86% | -86% |
| Over 0.5% | 4692 | 23 | 7% | 3% | -49% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 15189 | 47 | 4% | 2% | -65% | -88% | -88% |
| Morning (6am–12pm) | 14806 | 79 | 5% | 2% | -39% | -85% | -84% |
| Afternoon (12–6pm) | 15149 | 65 | 4% | 2% | -50% | -87% | -87% |
| Evening (6pm–12am) | 16927 | 49 | 4% | 2% | -67% | -89% | -89% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,997 |
| Time from buy to best bounce (bounced bets) | 50 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/19 1:44:51 PM | NEAR | DOWN | 8 sec | -0.151% | 1¢ | ❌ Lost | -$0.15 |
| 11/19 1:44:35 PM | SOL | UP | 24 sec | -0.103% | 0¢ | ❌ Lost | $0.00 |
| 11/19 1:44:35 PM | 10YRRATE | DOWN | 24 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/19 1:44:35 PM | BTC | DOWN | 24 sec | +0.083% | 1¢ | ❌ Lost | -$0.15 |
| 11/19 1:44:19 PM | ZEC | DOWN | 41 sec | +0.163% | 1¢ | ❌ Lost | -$0.15 |
| 11/19 1:44:04 PM | BNB | DOWN | 55 sec | +0.076% | 0¢ | ❌ Lost | -$0.15 |
| 11/19 1:44:04 PM | USDJPY | DOWN | 55 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/19 1:44:04 PM | DOGE | DOWN | 55 sec | +0.124% | 1¢ | ❌ Lost | -$0.15 |
| 11/19 1:43:48 PM | ETH | DOWN | 71 sec | +0.185% | 0¢ | ❌ Lost | $0.00 |
| 11/19 1:43:48 PM | 30YRRATE | DOWN | 71 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/19 1:43:48 PM | GOLD | UP | 71 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 11/19 1:43:48 PM | HYPE | DOWN | 71 sec | +0.369% | 0¢ | ❌ Lost | -$0.15 |
| 11/19 1:43:32 PM | GBPUSD | UP | 87 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/19 1:43:32 PM | NATGAS | UP | 87 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/19 1:43:16 PM | USDCAD | DOWN | 1.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/19 1:43:16 PM | PLATINUM | UP | 1.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/19 1:42:44 PM | WTI | DOWN | 2.3 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/19 1:42:44 PM | XRP | DOWN | 2.3 min | +0.271% | 1¢ | ❌ Lost | -$0.15 |
| 11/19 1:40:15 PM | BRENT | DOWN | 4.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/19 8:44:13 AM | SILVER | DOWN | 47 sec | — | 2¢ | ❌ Lost | -$0.15 |
| 11/19 8:43:56 AM | GBPUSD | DOWN | 63 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/19 8:43:41 AM | GOLD | DOWN | 78 sec | — | 2¢ | ❌ Lost | -$0.15 |
| 11/19 8:43:41 AM | AUDUSD | UP | 78 sec | — | 29¢ | ❌ Lost | -$0.15 |
| 11/19 8:43:41 AM | EURUSD | DOWN | 78 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/19 8:43:09 AM | PALLADIUM | DOWN | 1.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/19 8:43:09 AM | PLATINUM | DOWN | 1.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/19 8:41:18 AM | USDJPY | UP | 3.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/19 8:39:58 AM | BRENT | UP | 5.0 min | — | 5¢ | ❌ Lost | -$0.15 |
| 11/19 8:39:58 AM | WTI | UP | 5.0 min | — | 8¢ | ❌ Lost | -$0.15 |
| 11/19 8:39:25 AM | 30YRRATE | UP | 5.6 min | — | 4¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
