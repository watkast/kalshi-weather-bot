# 15-Minute 1¢ Study

*Updated Thu Nov 19, 4:19 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 4573 finished bets | 1% | $210.60 | +42% | +4.61¢ | $77.40 / $133.20 |

*Expect about **87 buys a day** (~$13.02/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 4312 | $110.50 | +24% |
| Volatility model ≥ 2%, hold to the close | 8537 | $66.60 | +6% |
| Momentum model ≥ 2%, hold to the close | 7080 | -$13.20 | -2% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 62264 | 62230 | 240 (0%) | 1.07% | -$4,211.10 (-56%) | Hold to the close: -$4,211.10 (-56%) |

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
| Volatility model | 36969 | 4.5% | 0.4% (154) | -638% | ❌ Worse |
| Momentum model | 36969 | 4.4% | 0.4% (154) | -663% | ❌ Worse |
| Mean-reversion model | 36969 | 7.9% | 0.4% (154) | -774% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 36969 | 154 | -46% | -87% | -87% | -84% |
| Volatility model ≥ 2% | 8537 | 78 | +6% | -77% | -76% | -72% |
| Volatility model ≥ 5% | 4573 | 51 | +42% | -72% | -71% | -67% |
| Volatility model ≥ 10% | 2631 | 30 | +67% | -63% | -62% | -58% |
| Momentum model ≥ 2% | 7080 | 57 | -2% | -79% | -78% | -75% |
| Momentum model ≥ 5% | 4312 | 41 | +24% | -75% | -74% | -70% |
| Momentum model ≥ 10% | 2811 | 26 | +32% | -67% | -66% | -62% |
| Mean-reversion model ≥ 2% | 15108 | 108 | -22% | -82% | -82% | -79% |
| Mean-reversion model ≥ 5% | 10510 | 89 | -6% | -80% | -79% | -77% |
| Mean-reversion model ≥ 10% | 6988 | 64 | +4% | -77% | -77% | -74% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 37175 | 5% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 14891 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 10164 | 3% | 2% | 1% | 1% | 0% | 0% |
| **All** | 62230 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 240 | 0% | -$4,211.10 | -56% | — |
| Sell at 2¢ | 2527 | 4% | -$6,620.08 | -87% | 47 sec |
| Sell at 3¢ | 1705 | 3% | -$6,612.15 | -87% | 48 sec |
| Sell at 5¢ | 1166 | 2% | -$6,491.20 | -86% | 63 sec |
| Sell at 10¢ | 713 | 1% | -$6,231.07 | -82% | 65 sec |
| Sell at 25¢ | 381 | 1% | -$5,749.99 | -76% | 80 sec |
| Sell at 50¢ | 247 | 0% | -$5,203.85 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 13 | 0 | 31% | 23% | -100% | -47% | -20% |
| 5–10 min | 3183 | 17 | 11% | 4% | -49% | -81% | -82% |
| 2–5 min | 20172 | 108 | 7% | 3% | -47% | -86% | -86% |
| 1–2 min | 15574 | 52 | 3% | 2% | -63% | -92% | -92% |
| Under 1 min | 23288 | 63 | 1% | 0% | -61% | -86% | -86% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 4157 | 19 | 5% | 2% | -40% | -88% | -87% |
| SOL | 4154 | 19 | 4% | 2% | -41% | -86% | -86% |
| HYPE | 4146 | 12 | 4% | 2% | -63% | -89% | -88% |
| DOGE | 4136 | 11 | 4% | 2% | -66% | -89% | -89% |
| BNB | 4135 | 21 | 5% | 2% | -36% | -85% | -85% |
| ETH | 4131 | 19 | 7% | 3% | -43% | -82% | -82% |
| BTC | 4112 | 21 | 5% | 2% | -31% | -86% | -88% |
| NEAR | 4110 | 18 | 5% | 2% | -43% | -85% | -86% |
| XRP | 4094 | 16 | 3% | 2% | -50% | -89% | -88% |
| GOLD | 2219 | 6 | 5% | 2% | -67% | -82% | -84% |
| WTI | 2198 | 7 | 4% | 2% | -61% | -91% | -92% |
| SILVER | 2159 | 9 | 5% | 2% | -50% | -83% | -83% |
| PLATINUM | 1967 | 5 | 3% | 1% | -76% | -95% | -95% |
| EURUSD | 1927 | 7 | 3% | 1% | -66% | -91% | -90% |
| GBPUSD | 1858 | 8 | 2% | 1% | -60% | -96% | -95% |
| COPPER | 1849 | 6 | 2% | 1% | -70% | -76% | -76% |
| USDJPY | 1811 | 6 | 2% | 1% | -69% | -96% | -96% |
| NATGAS | 1810 | 10 | 2% | 1% | -48% | -76% | -75% |
| PALLADIUM | 1767 | 4 | 1% | 0% | -79% | -93% | -93% |
| AUDUSD | 1362 | 6 | 2% | 1% | -59% | -90% | -90% |
| USDCAD | 1301 | 1 | 3% | 1% | -93% | -95% | -96% |
| BRENT | 922 | 0 | 2% | 1% | -100% | -97% | -97% |
| 10YRRATE | 480 | 2 | 3% | 1% | -61% | -75% | -73% |
| 2YRRATE | 456 | 4 | 4% | 2% | -18% | -52% | -51% |
| 30YRRATE | 441 | 0 | 2% | 1% | -100% | -96% | -94% |
| 5YRRATE | 431 | 2 | 4% | 2% | -57% | -94% | -95% |
| INX | 97 | 1 | 2% | 1% | -4% | -96% | -97% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 31744 | 123 | 4% | 2% | -55% | -88% | -88% |
| DOWN (bought NO) | 30486 | 117 | 4% | 2% | -56% | -86% | -87% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 5543 | 25 | 2% | 1% | -18% | -78% | -78% |
| 0.05–0.1% | 6033 | 24 | 3% | 2% | -38% | -91% | -91% |
| 0.1–0.2% | 9312 | 34 | 5% | 2% | -53% | -89% | -89% |
| 0.2–0.5% | 11566 | 50 | 7% | 3% | -51% | -86% | -86% |
| Over 0.5% | 4712 | 23 | 7% | 3% | -49% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 15189 | 47 | 4% | 2% | -65% | -88% | -88% |
| Morning (6am–12pm) | 14806 | 79 | 5% | 2% | -39% | -85% | -84% |
| Afternoon (12–6pm) | 15308 | 65 | 4% | 2% | -50% | -87% | -87% |
| Evening (6pm–12am) | 16927 | 49 | 4% | 2% | -67% | -89% | -89% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 5,004 |
| Time from buy to best bounce (bounced bets) | 50 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/19 4:14:15 PM | XRP | UP | 45 sec | -0.125% | 3¢ | ❌ Lost | -$0.15 |
| 11/19 4:14:15 PM | BRENT | UP | 45 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/19 4:13:59 PM | WTI | UP | 61 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 11/19 4:13:27 PM | GBPUSD | UP | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/19 4:13:09 PM | BNB | UP | 1.9 min | -0.233% | 1¢ | ❌ Lost | -$0.15 |
| 11/19 4:12:53 PM | USDCAD | UP | 2.1 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/19 4:12:22 PM | AUDUSD | UP | 2.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/19 4:12:04 PM | ZEC | UP | 2.9 min | -0.445% | 1¢ | ❌ Lost | -$0.15 |
| 11/19 4:12:04 PM | SOL | UP | 2.9 min | -0.465% | 1¢ | ❌ Lost | -$0.15 |
| 11/19 4:12:04 PM | NEAR | UP | 2.9 min | -0.678% | 1¢ | ❌ Lost | -$0.15 |
| 11/19 4:11:48 PM | DOGE | UP | 3.2 min | -0.364% | 1¢ | ❌ Lost | -$0.15 |
| 11/19 4:11:32 PM | BTC | UP | 3.5 min | -0.322% | 1¢ | ❌ Lost | -$0.15 |
| 11/19 4:11:17 PM | HYPE | UP | 3.7 min | -0.554% | 1¢ | ❌ Lost | -$0.15 |
| 11/19 4:11:17 PM | ETH | UP | 3.7 min | -0.443% | 1¢ | ❌ Lost | -$0.15 |
| 11/19 3:59:56 PM | SOL | DOWN | 4 sec | +0.062% | 0¢ | ❌ Lost | $0.00 |
| 11/19 3:59:56 PM | BRENT | UP | 4 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/19 3:59:56 PM | NEAR | DOWN | 4 sec | +0.094% | 0¢ | ❌ Lost | $0.00 |
| 11/19 3:59:40 PM | NATGAS | UP | 20 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/19 3:59:40 PM | BNB | UP | 20 sec | -0.093% | 0¢ | ❌ Lost | $0.00 |
| 11/19 3:59:24 PM | DOGE | UP | 36 sec | -0.194% | 0¢ | ❌ Lost | $0.00 |
| 11/19 3:59:24 PM | XRP | UP | 36 sec | -0.114% | 0¢ | ❌ Lost | -$0.15 |
| 11/19 3:59:24 PM | WTI | DOWN | 36 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/19 3:59:09 PM | GBPUSD | DOWN | 50 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/19 3:59:09 PM | BTC | UP | 50 sec | -0.116% | 1¢ | ❌ Lost | -$0.15 |
| 11/19 3:58:53 PM | HYPE | DOWN | 66 sec | +0.116% | 1¢ | ❌ Lost | -$0.15 |
| 11/19 3:58:53 PM | ETH | UP | 66 sec | -0.149% | 1¢ | ❌ Lost | -$0.15 |
| 11/19 3:58:04 PM | AUDUSD | UP | 1.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/19 3:57:47 PM | ZEC | DOWN | 2.2 min | +0.412% | 0¢ | ❌ Lost | $0.00 |
| 11/19 3:57:15 PM | USDJPY | UP | 2.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/19 3:44:48 PM | BNB | UP | 12 sec | -0.052% | 0¢ | ❌ Lost | $0.00 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
