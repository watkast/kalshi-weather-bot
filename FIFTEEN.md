# 15-Minute 1¢ Study

*Updated Wed Nov 11, 10:08 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 4230 finished bets | 1% | $174.50 | +37% | +4.13¢ | $84.40 / $90.10 |

*Expect about **94 buys a day** (~$14.12/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 3964 | $102.70 | +24% |
| Volatility model ≥ 2%, hold to the close | 7776 | $44.30 | +5% |
| Momentum model ≥ 2%, hold to the close | 6459 | -$14.35 | -2% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 54353 | 54332 | 208 (0%) | 1.07% | -$3,715.90 (-56%) | Hold to the close: -$3,715.90 (-56%) |

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
| Volatility model | 32640 | 4.7% | 0.4% (132) | -669% | ❌ Worse |
| Momentum model | 32640 | 4.6% | 0.4% (132) | -694% | ❌ Worse |
| Mean-reversion model | 32640 | 8.1% | 0.4% (132) | -812% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 32640 | 132 | -48% | -87% | -87% | -84% |
| Volatility model ≥ 2% | 7776 | 70 | +5% | -77% | -76% | -72% |
| Volatility model ≥ 5% | 4230 | 46 | +37% | -72% | -70% | -67% |
| Volatility model ≥ 10% | 2444 | 28 | +64% | -62% | -61% | -57% |
| Momentum model ≥ 2% | 6459 | 52 | -2% | -78% | -77% | -74% |
| Momentum model ≥ 5% | 3964 | 38 | +24% | -74% | -73% | -69% |
| Momentum model ≥ 10% | 2598 | 25 | +35% | -66% | -65% | -61% |
| Mean-reversion model ≥ 2% | 13466 | 92 | -25% | -82% | -82% | -80% |
| Mean-reversion model ≥ 5% | 9414 | 78 | -8% | -80% | -79% | -77% |
| Mean-reversion model ≥ 10% | 6287 | 56 | +1% | -77% | -77% | -74% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 32845 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 13034 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 8453 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 54332 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 208 | 0% | -$3,715.90 | -56% | — |
| Sell at 2¢ | 2160 | 4% | -$5,772.30 | -87% | 47 sec |
| Sell at 3¢ | 1469 | 3% | -$5,760.99 | -87% | 48 sec |
| Sell at 5¢ | 1016 | 2% | -$5,645.50 | -85% | 63 sec |
| Sell at 10¢ | 614 | 1% | -$5,417.56 | -82% | 65 sec |
| Sell at 25¢ | 327 | 1% | -$5,027.53 | -76% | 82 sec |
| Sell at 50¢ | 214 | 0% | -$4,553.40 | -69% | 1.7 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 12 | 0 | 25% | 17% | -100% | -57% | -35% |
| 5–10 min | 2707 | 13 | 11% | 4% | -54% | -81% | -83% |
| 2–5 min | 17572 | 96 | 7% | 3% | -46% | -87% | -87% |
| 1–2 min | 13712 | 45 | 3% | 2% | -64% | -92% | -92% |
| Under 1 min | 20329 | 54 | 1% | 0% | -62% | -84% | -84% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 3676 | 17 | 5% | 2% | -40% | -88% | -88% |
| SOL | 3673 | 16 | 4% | 2% | -45% | -86% | -86% |
| HYPE | 3665 | 11 | 5% | 2% | -62% | -89% | -88% |
| BNB | 3657 | 19 | 5% | 2% | -35% | -86% | -85% |
| DOGE | 3653 | 8 | 4% | 2% | -72% | -90% | -90% |
| ETH | 3648 | 16 | 7% | 3% | -46% | -82% | -81% |
| NEAR | 3629 | 17 | 5% | 2% | -39% | -85% | -85% |
| BTC | 3628 | 17 | 5% | 2% | -36% | -87% | -88% |
| XRP | 3616 | 13 | 3% | 1% | -55% | -89% | -89% |
| GOLD | 1958 | 5 | 5% | 2% | -69% | -82% | -83% |
| WTI | 1949 | 6 | 4% | 2% | -63% | -91% | -92% |
| SILVER | 1910 | 9 | 5% | 2% | -44% | -83% | -82% |
| PLATINUM | 1738 | 4 | 3% | 1% | -79% | -96% | -95% |
| EURUSD | 1676 | 5 | 2% | 1% | -72% | -90% | -90% |
| COPPER | 1624 | 6 | 2% | 1% | -66% | -74% | -74% |
| GBPUSD | 1604 | 6 | 2% | 1% | -65% | -96% | -96% |
| NATGAS | 1597 | 9 | 2% | 1% | -47% | -73% | -73% |
| USDJPY | 1579 | 6 | 2% | 1% | -65% | -97% | -96% |
| PALLADIUM | 1561 | 4 | 1% | 1% | -76% | -92% | -92% |
| AUDUSD | 1133 | 6 | 2% | 1% | -51% | -88% | -88% |
| USDCAD | 1095 | 0 | 2% | 1% | -100% | -96% | -96% |
| BRENT | 697 | 0 | 2% | 1% | -100% | -97% | -97% |
| 10YRRATE | 353 | 2 | 4% | 2% | -47% | -66% | -64% |
| 2YRRATE | 338 | 4 | 4% | 2% | +10% | -38% | -36% |
| 30YRRATE | 332 | 0 | 2% | 1% | -100% | -96% | -94% |
| 5YRRATE | 311 | 2 | 4% | 2% | -40% | -93% | -95% |
| INX | 32 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 27587 | 108 | 4% | 2% | -55% | -88% | -88% |
| DOWN (bought NO) | 26745 | 100 | 4% | 2% | -57% | -86% | -86% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 5199 | 25 | 2% | 1% | -15% | -77% | -77% |
| 0.05–0.1% | 5583 | 20 | 3% | 2% | -45% | -91% | -91% |
| 0.1–0.2% | 8425 | 31 | 5% | 2% | -53% | -89% | -89% |
| 0.2–0.5% | 9886 | 41 | 6% | 3% | -54% | -87% | -86% |
| Over 0.5% | 3744 | 17 | 7% | 3% | -53% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 13236 | 43 | 4% | 2% | -63% | -88% | -88% |
| Morning (6am–12pm) | 13083 | 60 | 4% | 2% | -48% | -85% | -84% |
| Afternoon (12–6pm) | 13132 | 58 | 4% | 2% | -48% | -86% | -86% |
| Evening (6pm–12am) | 14881 | 47 | 4% | 2% | -64% | -89% | -89% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,870 |
| Time from buy to best bounce (bounced bets) | 50 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/11 9:59:49 PM | BTC | DOWN | 10 sec | +0.013% | 0¢ | ❌ Lost | -$0.15 |
| 11/11 9:59:49 PM | EURUSD | UP | 10 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/11 9:59:49 PM | ETH | UP | 10 sec | -0.016% | 0¢ | ❌ Lost | -$0.15 |
| 11/11 9:59:34 PM | GBPUSD | UP | 25 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/11 9:59:34 PM | NEAR | UP | 25 sec | -0.149% | 1¢ | ❌ Lost | -$0.15 |
| 11/11 9:59:34 PM | DOGE | UP | 25 sec | -0.018% | 0¢ | ❌ Lost | $0.00 |
| 11/11 9:59:34 PM | BNB | UP | 25 sec | -0.071% | 0¢ | ❌ Lost | $0.00 |
| 11/11 9:59:15 PM | XRP | UP | 45 sec | -0.115% | 0¢ | ❌ Lost | $0.00 |
| 11/11 9:59:15 PM | SOL | DOWN | 45 sec | +0.038% | 1¢ | ❌ Lost | -$0.15 |
| 11/11 9:58:59 PM | HYPE | UP | 61 sec | -0.099% | 0¢ | ❌ Lost | -$0.15 |
| 11/11 9:58:59 PM | ZEC | DOWN | 61 sec | +0.183% | 1¢ | ❌ Lost | -$0.15 |
| 11/11 9:57:13 PM | AUDUSD | UP | 2.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/11 9:57:13 PM | USDJPY | DOWN | 2.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/11 9:44:55 PM | XRP | UP | 5 sec | -0.067% | 0¢ | ❌ Lost | $0.00 |
| 11/11 9:44:55 PM | NEAR | UP | 5 sec | -0.079% | 1¢ | ❌ Lost | -$0.15 |
| 11/11 9:44:55 PM | DOGE | UP | 5 sec | -0.019% | 1¢ | ❌ Lost | -$0.15 |
| 11/11 9:44:39 PM | GOLD | UP | 21 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 11/11 9:44:24 PM | SILVER | DOWN | 35 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 11/11 9:44:24 PM | USDJPY | UP | 35 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/11 9:44:05 PM | GBPUSD | DOWN | 55 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/11 9:43:49 PM | NATGAS | UP | 71 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/11 9:43:33 PM | AUDUSD | DOWN | 87 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/11 9:42:59 PM | BTC | UP | 2.0 min | -0.097% | 2¢ | ❌ Lost | -$0.15 |
| 11/11 9:42:43 PM | EURUSD | DOWN | 2.3 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/11 9:42:27 PM | COPPER | UP | 2.5 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/11 9:42:12 PM | USDCAD | UP | 2.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/11 9:40:31 PM | ETH | UP | 4.5 min | -0.247% | 1¢ | ❌ Lost | -$0.15 |
| 11/11 9:40:31 PM | SOL | UP | 4.5 min | -0.317% | 1¢ | ❌ Lost | -$0.15 |
| 11/11 9:40:15 PM | HYPE | UP | 4.8 min | -0.379% | 2¢ | ❌ Lost | -$0.15 |
| 11/11 9:40:15 PM | BNB | UP | 4.8 min | -0.226% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
