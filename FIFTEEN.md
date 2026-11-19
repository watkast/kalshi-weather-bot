# 15-Minute 1¢ Study

*Updated Thu Nov 19, 7:35 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 4566 finished bets | 1% | $211.05 | +42% | +4.62¢ | $77.70 / $133.35 |

*Expect about **87 buys a day** (~$13.09/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 4301 | $111.55 | +24% |
| Volatility model ≥ 2%, hold to the close | 8517 | $68.85 | +7% |
| Momentum model ≥ 2%, hold to the close | 7059 | -$10.65 | -1% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 61977 | 61943 | 239 (0%) | 1.07% | -$4,188.50 (-56%) | Hold to the close: -$4,188.50 (-56%) |

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
| Volatility model | 36826 | 4.5% | 0.4% (154) | -635% | ❌ Worse |
| Momentum model | 36826 | 4.4% | 0.4% (154) | -660% | ❌ Worse |
| Mean-reversion model | 36826 | 7.9% | 0.4% (154) | -771% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 36826 | 154 | -46% | -87% | -87% | -84% |
| Volatility model ≥ 2% | 8517 | 78 | +7% | -77% | -76% | -72% |
| Volatility model ≥ 5% | 4566 | 51 | +42% | -72% | -71% | -67% |
| Volatility model ≥ 10% | 2625 | 30 | +67% | -63% | -62% | -58% |
| Momentum model ≥ 2% | 7059 | 57 | -1% | -79% | -78% | -75% |
| Momentum model ≥ 5% | 4301 | 41 | +24% | -75% | -74% | -70% |
| Momentum model ≥ 10% | 2804 | 26 | +32% | -67% | -66% | -62% |
| Mean-reversion model ≥ 2% | 15058 | 108 | -21% | -82% | -82% | -79% |
| Mean-reversion model ≥ 5% | 10480 | 89 | -6% | -80% | -79% | -77% |
| Mean-reversion model ≥ 10% | 6968 | 64 | +5% | -77% | -77% | -74% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 37032 | 5% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 14831 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 10080 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 61943 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 239 | 0% | -$4,188.50 | -56% | — |
| Sell at 2¢ | 2512 | 4% | -$6,587.38 | -87% | 47 sec |
| Sell at 3¢ | 1694 | 3% | -$6,579.84 | -87% | 48 sec |
| Sell at 5¢ | 1156 | 2% | -$6,461.10 | -86% | 63 sec |
| Sell at 10¢ | 706 | 1% | -$6,203.64 | -82% | 65 sec |
| Sell at 25¢ | 378 | 1% | -$5,737.32 | -76% | 80 sec |
| Sell at 50¢ | 246 | 0% | -$5,188.00 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 13 | 0 | 31% | 23% | -100% | -47% | -20% |
| 5–10 min | 3147 | 17 | 10% | 4% | -49% | -82% | -83% |
| 2–5 min | 20093 | 108 | 7% | 3% | -47% | -86% | -86% |
| 1–2 min | 15495 | 52 | 3% | 2% | -63% | -92% | -92% |
| Under 1 min | 23195 | 62 | 1% | 0% | -62% | -86% | -86% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 4141 | 19 | 5% | 2% | -39% | -88% | -87% |
| SOL | 4138 | 19 | 4% | 2% | -41% | -86% | -86% |
| HYPE | 4130 | 12 | 4% | 2% | -63% | -90% | -88% |
| DOGE | 4120 | 11 | 4% | 2% | -66% | -89% | -89% |
| BNB | 4120 | 21 | 5% | 2% | -35% | -85% | -85% |
| ETH | 4115 | 19 | 7% | 3% | -42% | -82% | -82% |
| BTC | 4096 | 21 | 5% | 2% | -30% | -86% | -88% |
| NEAR | 4094 | 18 | 5% | 2% | -42% | -85% | -86% |
| XRP | 4078 | 16 | 3% | 2% | -50% | -89% | -88% |
| GOLD | 2211 | 6 | 5% | 2% | -67% | -82% | -84% |
| WTI | 2190 | 7 | 4% | 1% | -61% | -91% | -92% |
| SILVER | 2150 | 9 | 5% | 2% | -50% | -83% | -83% |
| PLATINUM | 1958 | 4 | 3% | 1% | -81% | -95% | -95% |
| EURUSD | 1916 | 7 | 3% | 1% | -66% | -91% | -90% |
| GBPUSD | 1844 | 8 | 2% | 1% | -60% | -96% | -95% |
| COPPER | 1843 | 6 | 2% | 1% | -70% | -76% | -76% |
| NATGAS | 1802 | 10 | 2% | 1% | -48% | -76% | -75% |
| USDJPY | 1800 | 6 | 2% | 1% | -69% | -96% | -96% |
| PALLADIUM | 1762 | 4 | 1% | 0% | -79% | -93% | -93% |
| AUDUSD | 1353 | 6 | 2% | 1% | -59% | -90% | -90% |
| USDCAD | 1293 | 1 | 3% | 1% | -93% | -95% | -96% |
| BRENT | 915 | 0 | 2% | 1% | -100% | -97% | -98% |
| 10YRRATE | 473 | 2 | 3% | 1% | -61% | -75% | -73% |
| 2YRRATE | 449 | 4 | 4% | 2% | -17% | -52% | -51% |
| 30YRRATE | 435 | 0 | 2% | 1% | -100% | -96% | -94% |
| 5YRRATE | 425 | 2 | 4% | 1% | -56% | -94% | -96% |
| INX | 92 | 1 | 2% | 1% | +1% | -96% | -97% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 31563 | 123 | 4% | 2% | -55% | -88% | -88% |
| DOWN (bought NO) | 30380 | 116 | 4% | 2% | -56% | -86% | -87% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 5537 | 25 | 2% | 1% | -18% | -78% | -78% |
| 0.05–0.1% | 6022 | 24 | 3% | 2% | -38% | -91% | -91% |
| 0.1–0.2% | 9282 | 34 | 5% | 2% | -53% | -89% | -89% |
| 0.2–0.5% | 11513 | 50 | 7% | 3% | -51% | -86% | -86% |
| Over 0.5% | 4669 | 23 | 7% | 3% | -48% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 15189 | 47 | 4% | 2% | -65% | -88% | -88% |
| Morning (6am–12pm) | 14697 | 78 | 5% | 2% | -40% | -85% | -85% |
| Afternoon (12–6pm) | 15130 | 65 | 4% | 2% | -49% | -87% | -87% |
| Evening (6pm–12am) | 16927 | 49 | 4% | 2% | -67% | -89% | -89% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 5,003 |
| Time from buy to best bounce (bounced bets) | 50 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/19 7:29:51 AM | USDCAD | DOWN | 8 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/19 7:29:51 AM | BNB | UP | 8 sec | -0.032% | 0¢ | ❌ Lost | $0.00 |
| 11/19 7:29:51 AM | BTC | UP | 8 sec | -0.060% | 1¢ | ❌ Lost | -$0.15 |
| 11/19 7:29:35 AM | WTI | UP | 24 sec | — | 0¢ | ❌ Lost | $0.00 |
| 11/19 7:29:35 AM | 30YRRATE | UP | 24 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/19 7:29:35 AM | NEAR | UP | 24 sec | -0.177% | 0¢ | ❌ Lost | $0.00 |
| 11/19 7:29:35 AM | DOGE | UP | 24 sec | -0.116% | 0¢ | ❌ Lost | $0.00 |
| 11/19 7:29:35 AM | USDJPY | UP | 24 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/19 7:29:19 AM | NATGAS | UP | 40 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/19 7:29:19 AM | BRENT | UP | 40 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/19 7:28:48 AM | XRP | DOWN | 72 sec | +0.111% | 1¢ | ❌ Lost | -$0.15 |
| 11/19 7:28:48 AM | PLATINUM | UP | 72 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/19 7:28:32 AM | ZEC | UP | 88 sec | -0.311% | 0¢ | ❌ Lost | $0.00 |
| 11/19 7:28:32 AM | SILVER | UP | 88 sec | — | 0¢ | ❌ Lost | $0.00 |
| 11/19 7:28:32 AM | 2YRRATE | UP | 88 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/19 7:28:16 AM | 5YRRATE | UP | 1.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/19 7:27:44 AM | ETH | UP | 2.2 min | -0.198% | 6¢ | ❌ Lost | -$0.15 |
| 11/19 7:27:44 AM | EURUSD | UP | 2.2 min | — | 44¢ | ❌ Lost | -$0.15 |
| 11/19 7:27:28 AM | PALLADIUM | UP | 2.5 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/19 7:27:12 AM | GBPUSD | UP | 2.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/19 7:26:40 AM | HYPE | UP | 3.3 min | -0.365% | 1¢ | ❌ Lost | -$0.15 |
| 11/19 7:26:40 AM | AUDUSD | UP | 3.3 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/19 7:24:21 AM | COPPER | UP | 5.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/19 7:14:48 AM | SOL | UP | 11 sec | -0.108% | 0¢ | ❌ Lost | $0.00 |
| 11/19 7:14:32 AM | SILVER | DOWN | 27 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/19 7:14:18 AM | ETH | UP | 41 sec | -0.104% | 0¢ | ❌ Lost | $0.00 |
| 11/19 7:14:02 AM | ZEC | UP | 57 sec | -0.183% | 0¢ | ❌ Lost | $0.00 |
| 11/19 7:14:02 AM | BTC | UP | 57 sec | -0.149% | 0¢ | ❌ Lost | $0.00 |
| 11/19 7:14:02 AM | PALLADIUM | UP | 57 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/19 7:14:02 AM | BNB | UP | 57 sec | -0.098% | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
