# 15-Minute 1¢ Study

*Updated Thu Nov 12, 8:07 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 4261 finished bets | 1% | $171.20 | +36% | +4.02¢ | $82.45 / $88.75 |

*Expect about **93 buys a day** (~$13.94/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 4002 | $98.20 | +23% |
| Volatility model ≥ 2%, hold to the close | 7855 | $34.70 | +4% |
| Momentum model ≥ 2%, hold to the close | 6526 | -$22.00 | -3% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 55406 | 55385 | 212 (0%) | 1.07% | -$3,789.50 (-56%) | Hold to the close: -$3,789.50 (-56%) |

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
| Volatility model | 33118 | 4.7% | 0.4% (133) | -669% | ❌ Worse |
| Momentum model | 33118 | 4.6% | 0.4% (133) | -694% | ❌ Worse |
| Mean-reversion model | 33118 | 8.0% | 0.4% (133) | -810% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 33118 | 133 | -49% | -87% | -87% | -84% |
| Volatility model ≥ 2% | 7855 | 70 | +4% | -77% | -76% | -72% |
| Volatility model ≥ 5% | 4261 | 46 | +36% | -72% | -70% | -67% |
| Volatility model ≥ 10% | 2466 | 28 | +63% | -63% | -61% | -58% |
| Momentum model ≥ 2% | 6526 | 52 | -3% | -78% | -77% | -74% |
| Momentum model ≥ 5% | 4002 | 38 | +23% | -74% | -73% | -69% |
| Momentum model ≥ 10% | 2623 | 25 | +34% | -66% | -65% | -61% |
| Mean-reversion model ≥ 2% | 13637 | 93 | -25% | -82% | -82% | -79% |
| Mean-reversion model ≥ 5% | 9521 | 79 | -8% | -80% | -79% | -77% |
| Mean-reversion model ≥ 10% | 6348 | 56 | +0% | -77% | -77% | -75% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 33323 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 13332 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 8730 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 55385 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 212 | 0% | -$3,789.50 | -56% | — |
| Sell at 2¢ | 2206 | 4% | -$5,889.94 | -87% | 47 sec |
| Sell at 3¢ | 1500 | 3% | -$5,878.50 | -87% | 49 sec |
| Sell at 5¢ | 1034 | 2% | -$5,763.40 | -85% | 63 sec |
| Sell at 10¢ | 628 | 1% | -$5,528.82 | -82% | 65 sec |
| Sell at 25¢ | 330 | 1% | -$5,133.20 | -76% | 82 sec |
| Sell at 50¢ | 217 | 0% | -$4,648.75 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 13 | 0 | 31% | 23% | -100% | -47% | -20% |
| 5–10 min | 2755 | 13 | 11% | 4% | -55% | -81% | -83% |
| 2–5 min | 17881 | 97 | 7% | 3% | -47% | -87% | -86% |
| 1–2 min | 13964 | 46 | 3% | 2% | -63% | -92% | -92% |
| Under 1 min | 20772 | 56 | 1% | 0% | -62% | -85% | -85% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 3730 | 17 | 5% | 3% | -41% | -88% | -87% |
| SOL | 3725 | 16 | 4% | 2% | -45% | -87% | -87% |
| HYPE | 3720 | 11 | 5% | 2% | -63% | -89% | -88% |
| BNB | 3708 | 19 | 5% | 2% | -35% | -86% | -85% |
| DOGE | 3706 | 8 | 4% | 2% | -73% | -90% | -90% |
| ETH | 3701 | 16 | 7% | 3% | -46% | -82% | -81% |
| BTC | 3683 | 18 | 5% | 2% | -33% | -87% | -88% |
| NEAR | 3681 | 17 | 5% | 2% | -40% | -85% | -85% |
| XRP | 3669 | 13 | 3% | 1% | -56% | -89% | -89% |
| GOLD | 2002 | 5 | 5% | 2% | -69% | -82% | -84% |
| WTI | 1984 | 7 | 4% | 2% | -57% | -91% | -92% |
| SILVER | 1946 | 9 | 5% | 2% | -45% | -83% | -83% |
| PLATINUM | 1775 | 4 | 3% | 1% | -79% | -96% | -95% |
| EURUSD | 1717 | 6 | 3% | 1% | -67% | -90% | -90% |
| COPPER | 1664 | 6 | 2% | 1% | -66% | -74% | -74% |
| GBPUSD | 1644 | 6 | 2% | 1% | -66% | -96% | -96% |
| NATGAS | 1636 | 9 | 2% | 1% | -49% | -74% | -73% |
| USDJPY | 1616 | 6 | 2% | 1% | -65% | -96% | -96% |
| PALLADIUM | 1590 | 4 | 1% | 1% | -77% | -92% | -92% |
| AUDUSD | 1166 | 6 | 2% | 1% | -52% | -89% | -89% |
| USDCAD | 1125 | 1 | 3% | 1% | -92% | -96% | -96% |
| BRENT | 735 | 0 | 2% | 1% | -100% | -97% | -97% |
| 10YRRATE | 375 | 2 | 4% | 2% | -50% | -68% | -66% |
| 2YRRATE | 360 | 4 | 4% | 2% | +4% | -41% | -40% |
| 30YRRATE | 356 | 0 | 2% | 1% | -100% | -96% | -94% |
| 5YRRATE | 330 | 2 | 4% | 2% | -43% | -93% | -94% |
| INX | 41 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 28144 | 110 | 4% | 2% | -55% | -88% | -88% |
| DOWN (bought NO) | 27241 | 102 | 4% | 2% | -57% | -86% | -86% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 5248 | 25 | 2% | 1% | -15% | -77% | -77% |
| 0.05–0.1% | 5644 | 20 | 3% | 2% | -45% | -91% | -91% |
| 0.1–0.2% | 8527 | 31 | 5% | 2% | -54% | -89% | -89% |
| 0.2–0.5% | 10074 | 41 | 6% | 3% | -55% | -87% | -86% |
| Over 0.5% | 3822 | 18 | 7% | 3% | -51% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 13478 | 44 | 4% | 2% | -63% | -88% | -88% |
| Morning (6am–12pm) | 13343 | 62 | 4% | 2% | -47% | -85% | -84% |
| Afternoon (12–6pm) | 13453 | 59 | 4% | 2% | -49% | -86% | -87% |
| Evening (6pm–12am) | 15111 | 47 | 4% | 2% | -64% | -89% | -89% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,830 |
| Time from buy to best bounce (bounced bets) | 51 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/12 7:59:46 PM | SILVER | DOWN | 14 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/12 7:59:46 PM | NATGAS | UP | 14 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/12 7:59:14 PM | AUDUSD | DOWN | 46 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/12 7:59:14 PM | NEAR | DOWN | 46 sec | +0.323% | 0¢ | ❌ Lost | $0.00 |
| 11/12 7:58:58 PM | PALLADIUM | DOWN | 62 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/12 7:58:58 PM | XRP | DOWN | 62 sec | +0.255% | 0¢ | ❌ Lost | $0.00 |
| 11/12 7:58:58 PM | GOLD | DOWN | 62 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/12 7:58:58 PM | USDCAD | UP | 62 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/12 7:58:58 PM | ZEC | DOWN | 62 sec | +0.498% | 0¢ | ❌ Lost | -$0.15 |
| 11/12 7:58:43 PM | GBPUSD | DOWN | 77 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/12 7:58:43 PM | PLATINUM | DOWN | 77 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/12 7:58:27 PM | BTC | DOWN | 1.6 min | +0.199% | 1¢ | ❌ Lost | -$0.15 |
| 11/12 7:58:11 PM | ETH | DOWN | 1.8 min | +0.315% | 1¢ | ❌ Lost | -$0.15 |
| 11/12 7:58:11 PM | BNB | DOWN | 1.8 min | +0.252% | 1¢ | ❌ Lost | -$0.15 |
| 11/12 7:58:11 PM | SOL | DOWN | 1.8 min | +0.322% | 4¢ | ❌ Lost | -$0.15 |
| 11/12 7:58:11 PM | HYPE | DOWN | 1.8 min | +0.566% | 1¢ | ❌ Lost | -$0.15 |
| 11/12 7:57:55 PM | DOGE | DOWN | 2.1 min | +0.445% | 1¢ | ❌ Lost | -$0.15 |
| 11/12 7:57:23 PM | COPPER | UP | 2.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/12 7:57:23 PM | BRENT | UP | 2.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/12 7:57:23 PM | EURUSD | DOWN | 2.6 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/12 7:57:23 PM | WTI | UP | 2.6 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/12 7:44:54 PM | AUDUSD | UP | 5 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/12 7:44:54 PM | EURUSD | UP | 5 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/12 7:44:39 PM | WTI | DOWN | 21 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 11/12 7:44:23 PM | BRENT | DOWN | 37 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/12 7:44:23 PM | USDCAD | DOWN | 37 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/12 7:44:07 PM | NATGAS | UP | 53 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/12 7:43:35 PM | COPPER | UP | 84 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/12 7:43:35 PM | ZEC | UP | 84 sec | -0.734% | 0¢ | ❌ Lost | $0.00 |
| 11/12 7:43:03 PM | USDJPY | DOWN | 1.9 min | — | 3¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
