# 15-Minute 1¢ Study

*Updated Mon Nov 9, 11:21 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 4140 finished bets | 1% | $183.80 | +40% | +4.44¢ | $89.80 / $94.00 |

*Expect about **96 buys a day** (~$14.45/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 3847 | $101.60 | +24% |
| Volatility model ≥ 2%, hold to the close | 7571 | $68.75 | +8% |
| Momentum model ≥ 2%, hold to the close | 6266 | -$5.55 | -1% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 51707 | 51690 | 199 (0%) | 1.07% | -$3,509.50 (-56%) | Hold to the close: -$3,509.50 (-56%) |

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
| Volatility model | 31405 | 4.8% | 0.4% (128) | -677% | ❌ Worse |
| Momentum model | 31405 | 4.6% | 0.4% (128) | -701% | ❌ Worse |
| Mean-reversion model | 31405 | 8.1% | 0.4% (128) | -819% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 31405 | 128 | -48% | -87% | -87% | -84% |
| Volatility model ≥ 2% | 7571 | 70 | +8% | -77% | -75% | -71% |
| Volatility model ≥ 5% | 4140 | 46 | +40% | -71% | -70% | -66% |
| Volatility model ≥ 10% | 2385 | 28 | +68% | -62% | -60% | -56% |
| Momentum model ≥ 2% | 6266 | 51 | -1% | -78% | -77% | -74% |
| Momentum model ≥ 5% | 3847 | 37 | +24% | -73% | -73% | -68% |
| Momentum model ≥ 10% | 2524 | 25 | +39% | -65% | -64% | -60% |
| Mean-reversion model ≥ 2% | 12999 | 91 | -23% | -82% | -82% | -79% |
| Mean-reversion model ≥ 5% | 9119 | 78 | -5% | -79% | -79% | -76% |
| Mean-reversion model ≥ 10% | 6095 | 56 | +5% | -77% | -76% | -74% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 31610 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 12248 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 7832 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 51690 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 199 | 0% | -$3,509.50 | -56% | — |
| Sell at 2¢ | 2063 | 4% | -$5,479.12 | -87% | 47 sec |
| Sell at 3¢ | 1405 | 3% | -$5,467.55 | -87% | 48 sec |
| Sell at 5¢ | 982 | 2% | -$5,349.20 | -85% | 63 sec |
| Sell at 10¢ | 595 | 1% | -$5,124.05 | -81% | 65 sec |
| Sell at 25¢ | 314 | 1% | -$4,752.16 | -75% | 83 sec |
| Sell at 50¢ | 205 | 0% | -$4,309.75 | -68% | 1.7 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 12 | 0 | 25% | 17% | -100% | -57% | -35% |
| 5–10 min | 2572 | 12 | 11% | 4% | -56% | -81% | -82% |
| 2–5 min | 16707 | 93 | 7% | 3% | -45% | -87% | -86% |
| 1–2 min | 13061 | 44 | 3% | 2% | -63% | -92% | -92% |
| Under 1 min | 19338 | 50 | 1% | 0% | -63% | -84% | -84% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 3540 | 15 | 5% | 2% | -45% | -88% | -88% |
| SOL | 3536 | 16 | 4% | 2% | -42% | -87% | -87% |
| HYPE | 3527 | 11 | 5% | 2% | -61% | -89% | -88% |
| BNB | 3520 | 19 | 5% | 2% | -32% | -86% | -85% |
| DOGE | 3516 | 8 | 4% | 2% | -71% | -90% | -89% |
| ETH | 3511 | 15 | 7% | 3% | -47% | -81% | -81% |
| BTC | 3491 | 17 | 5% | 2% | -33% | -87% | -88% |
| NEAR | 3490 | 16 | 5% | 2% | -41% | -85% | -85% |
| XRP | 3479 | 13 | 3% | 1% | -53% | -89% | -88% |
| GOLD | 1859 | 5 | 6% | 2% | -67% | -81% | -83% |
| WTI | 1831 | 6 | 4% | 2% | -61% | -91% | -92% |
| SILVER | 1809 | 8 | 5% | 2% | -48% | -82% | -82% |
| PLATINUM | 1639 | 4 | 2% | 1% | -77% | -96% | -95% |
| EURUSD | 1574 | 5 | 2% | 1% | -70% | -90% | -89% |
| COPPER | 1538 | 6 | 2% | 1% | -64% | -73% | -72% |
| NATGAS | 1500 | 8 | 2% | 1% | -50% | -78% | -77% |
| GBPUSD | 1494 | 5 | 2% | 1% | -69% | -96% | -96% |
| PALLADIUM | 1475 | 3 | 1% | 0% | -81% | -92% | -92% |
| USDJPY | 1472 | 6 | 2% | 1% | -62% | -96% | -96% |
| AUDUSD | 1034 | 5 | 2% | 1% | -55% | -87% | -87% |
| USDCAD | 1002 | 0 | 2% | 1% | -100% | -96% | -97% |
| BRENT | 597 | 0 | 2% | 1% | -100% | -97% | -97% |
| 10YRRATE | 331 | 2 | 5% | 2% | -44% | -64% | -62% |
| 2YRRATE | 314 | 4 | 4% | 2% | +19% | -33% | -31% |
| 30YRRATE | 309 | 0 | 2% | 1% | -100% | -96% | -94% |
| 5YRRATE | 291 | 2 | 4% | 2% | -36% | -92% | -95% |
| INX | 11 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 26198 | 104 | 4% | 2% | -54% | -88% | -87% |
| DOWN (bought NO) | 25492 | 95 | 4% | 2% | -57% | -86% | -86% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 5084 | 25 | 2% | 1% | -13% | -77% | -76% |
| 0.05–0.1% | 5403 | 20 | 3% | 2% | -44% | -91% | -91% |
| 0.1–0.2% | 8124 | 30 | 5% | 2% | -53% | -89% | -89% |
| 0.2–0.5% | 9450 | 40 | 6% | 3% | -53% | -87% | -86% |
| Over 0.5% | 3541 | 15 | 7% | 3% | -56% | -87% | -88% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 12671 | 43 | 4% | 2% | -61% | -87% | -87% |
| Morning (6am–12pm) | 12425 | 56 | 4% | 2% | -49% | -84% | -84% |
| Afternoon (12–6pm) | 12535 | 57 | 4% | 2% | -47% | -86% | -86% |
| Evening (6pm–12am) | 14059 | 43 | 4% | 2% | -65% | -90% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,915 |
| Time from buy to best bounce (bounced bets) | 51 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/9 11:14:47 PM | WTI | UP | 12 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/9 11:14:31 PM | COPPER | UP | 28 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/9 11:14:15 PM | NATGAS | DOWN | 44 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/9 11:13:28 PM | NEAR | UP | 1.5 min | -0.575% | 0¢ | ❌ Lost | $0.00 |
| 11/9 11:13:28 PM | XRP | UP | 1.5 min | -0.264% | 0¢ | ❌ Lost | -$0.15 |
| 11/9 11:13:12 PM | HYPE | UP | 1.8 min | -0.366% | 1¢ | ❌ Lost | -$0.15 |
| 11/9 11:13:12 PM | AUDUSD | DOWN | 1.8 min | — | 17¢ | ❌ Lost | -$0.15 |
| 11/9 11:12:23 PM | USDCAD | UP | 2.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/9 11:12:23 PM | BTC | UP | 2.6 min | -0.152% | 1¢ | ❌ Lost | -$0.15 |
| 11/9 11:11:20 PM | USDJPY | UP | 3.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/9 11:11:04 PM | BNB | UP | 3.9 min | -0.182% | 1¢ | ❌ Lost | -$0.15 |
| 11/9 11:11:04 PM | ETH | UP | 3.9 min | -0.279% | 1¢ | ❌ Lost | -$0.15 |
| 11/9 11:10:44 PM | GBPUSD | DOWN | 4.3 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/9 11:10:12 PM | DOGE | UP | 4.8 min | -0.308% | 3¢ | ❌ Lost | -$0.15 |
| 11/9 11:10:12 PM | ZEC | UP | 4.8 min | -0.696% | 1¢ | ❌ Lost | -$0.15 |
| 11/9 11:10:12 PM | EURUSD | DOWN | 4.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/9 11:10:12 PM | SOL | UP | 4.8 min | -0.352% | 1¢ | ❌ Lost | -$0.15 |
| 11/9 10:59:43 PM | USDJPY | DOWN | 17 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/9 10:59:43 PM | EURUSD | DOWN | 17 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/9 10:59:27 PM | ZEC | UP | 33 sec | -0.205% | 0¢ | ❌ Lost | $0.00 |
| 11/9 10:59:27 PM | PALLADIUM | UP | 33 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/9 10:59:27 PM | HYPE | UP | 33 sec | -0.087% | 0¢ | ❌ Lost | $0.00 |
| 11/9 10:59:27 PM | ETH | UP | 33 sec | -0.067% | 0¢ | ❌ Lost | $0.00 |
| 11/9 10:59:27 PM | AUDUSD | DOWN | 33 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/9 10:59:11 PM | BTC | UP | 49 sec | -0.060% | 0¢ | ❌ Lost | $0.00 |
| 11/9 10:58:39 PM | GOLD | UP | 80 sec | — | 3¢ | ❌ Lost | -$0.15 |
| 11/9 10:58:23 PM | PLATINUM | UP | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/9 10:58:07 PM | DOGE | DOWN | 1.9 min | +0.117% | 1¢ | ❌ Lost | -$0.15 |
| 11/9 10:57:51 PM | SILVER | UP | 2.1 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/9 10:57:35 PM | NATGAS | UP | 2.4 min | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
