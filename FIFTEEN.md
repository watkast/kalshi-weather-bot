# 15-Minute 1¢ Study

*Updated Thu Nov 12, 1:00 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 4252 finished bets | 1% | $172.25 | +37% | +4.05¢ | $83.05 / $89.20 |

*Expect about **93 buys a day** (~$14.00/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 3991 | $99.55 | +23% |
| Volatility model ≥ 2%, hold to the close | 7827 | $38.45 | +4% |
| Momentum model ≥ 2%, hold to the close | 6503 | -$19.30 | -3% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 55015 | 54974 | 211 (0%) | 1.07% | -$3,753.55 (-56%) | Hold to the close: -$3,753.55 (-56%) |

*In play or awaiting result: 29. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 32915 | 4.7% | 0.4% (133) | -668% | ❌ Worse |
| Momentum model | 32915 | 4.6% | 0.4% (133) | -694% | ❌ Worse |
| Mean-reversion model | 32915 | 8.0% | 0.4% (133) | -809% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 32915 | 133 | -48% | -87% | -87% | -84% |
| Volatility model ≥ 2% | 7827 | 70 | +4% | -77% | -76% | -72% |
| Volatility model ≥ 5% | 4252 | 46 | +37% | -72% | -70% | -67% |
| Volatility model ≥ 10% | 2459 | 28 | +64% | -62% | -61% | -57% |
| Momentum model ≥ 2% | 6503 | 52 | -3% | -78% | -77% | -74% |
| Momentum model ≥ 5% | 3991 | 38 | +23% | -74% | -73% | -69% |
| Momentum model ≥ 10% | 2615 | 25 | +34% | -66% | -65% | -61% |
| Mean-reversion model ≥ 2% | 13580 | 93 | -25% | -82% | -82% | -79% |
| Mean-reversion model ≥ 5% | 9484 | 79 | -8% | -80% | -79% | -77% |
| Mean-reversion model ≥ 10% | 6328 | 56 | +1% | -77% | -77% | -75% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 33120 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 13218 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 8636 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 54974 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 211 | 0% | -$3,753.55 | -56% | — |
| Sell at 2¢ | 2192 | 4% | -$5,843.63 | -87% | 47 sec |
| Sell at 3¢ | 1492 | 3% | -$5,831.67 | -87% | 49 sec |
| Sell at 5¢ | 1030 | 2% | -$5,716.05 | -85% | 63 sec |
| Sell at 10¢ | 625 | 1% | -$5,482.80 | -82% | 65 sec |
| Sell at 25¢ | 329 | 1% | -$5,086.56 | -76% | 82 sec |
| Sell at 50¢ | 216 | 0% | -$4,605.55 | -69% | 1.7 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 13 | 0 | 31% | 23% | -100% | -47% | -20% |
| 5–10 min | 2743 | 13 | 11% | 4% | -55% | -81% | -83% |
| 2–5 min | 17762 | 97 | 7% | 3% | -46% | -87% | -86% |
| 1–2 min | 13862 | 46 | 3% | 2% | -63% | -92% | -92% |
| Under 1 min | 20594 | 55 | 1% | 0% | -62% | -85% | -84% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 3707 | 17 | 5% | 3% | -40% | -88% | -87% |
| SOL | 3703 | 16 | 4% | 2% | -45% | -87% | -87% |
| HYPE | 3696 | 11 | 5% | 2% | -63% | -89% | -88% |
| BNB | 3687 | 19 | 5% | 2% | -35% | -86% | -85% |
| DOGE | 3683 | 8 | 4% | 2% | -73% | -90% | -90% |
| ETH | 3678 | 16 | 7% | 3% | -46% | -82% | -81% |
| BTC | 3660 | 18 | 5% | 2% | -33% | -87% | -88% |
| NEAR | 3659 | 17 | 5% | 2% | -40% | -85% | -85% |
| XRP | 3647 | 13 | 3% | 1% | -55% | -89% | -89% |
| GOLD | 1986 | 5 | 5% | 2% | -69% | -82% | -84% |
| WTI | 1970 | 7 | 4% | 2% | -57% | -91% | -92% |
| SILVER | 1934 | 9 | 5% | 2% | -45% | -83% | -82% |
| PLATINUM | 1763 | 4 | 3% | 1% | -79% | -96% | -95% |
| EURUSD | 1703 | 6 | 3% | 1% | -67% | -90% | -89% |
| COPPER | 1649 | 6 | 2% | 1% | -66% | -74% | -74% |
| GBPUSD | 1631 | 6 | 2% | 1% | -66% | -96% | -96% |
| NATGAS | 1618 | 9 | 2% | 1% | -48% | -73% | -73% |
| USDJPY | 1602 | 6 | 2% | 1% | -65% | -97% | -96% |
| PALLADIUM | 1580 | 4 | 1% | 1% | -76% | -92% | -92% |
| AUDUSD | 1155 | 6 | 2% | 1% | -52% | -88% | -89% |
| USDCAD | 1111 | 0 | 3% | 1% | -100% | -96% | -96% |
| BRENT | 718 | 0 | 2% | 1% | -100% | -97% | -97% |
| 10YRRATE | 369 | 2 | 4% | 2% | -49% | -68% | -66% |
| 2YRRATE | 353 | 4 | 4% | 2% | +6% | -40% | -39% |
| 30YRRATE | 349 | 0 | 2% | 1% | -100% | -96% | -94% |
| 5YRRATE | 324 | 2 | 4% | 2% | -42% | -93% | -94% |
| INX | 39 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 27950 | 109 | 4% | 2% | -55% | -88% | -88% |
| DOWN (bought NO) | 27024 | 102 | 4% | 2% | -57% | -86% | -86% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 5223 | 25 | 2% | 1% | -15% | -77% | -77% |
| 0.05–0.1% | 5621 | 20 | 3% | 2% | -45% | -91% | -91% |
| 0.1–0.2% | 8482 | 31 | 5% | 2% | -54% | -89% | -89% |
| 0.2–0.5% | 9984 | 41 | 6% | 3% | -54% | -87% | -86% |
| Over 0.5% | 3802 | 18 | 7% | 3% | -51% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 13478 | 44 | 4% | 2% | -63% | -88% | -88% |
| Morning (6am–12pm) | 13343 | 62 | 4% | 2% | -47% | -85% | -84% |
| Afternoon (12–6pm) | 13192 | 58 | 4% | 2% | -49% | -86% | -86% |
| Evening (6pm–12am) | 14961 | 47 | 4% | 2% | -64% | -89% | -89% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,832 |
| Time from buy to best bounce (bounced bets) | 51 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/12 12:59:55 PM | 30YRRATE | UP | 5 sec | — | 0¢ | In play | — |
| 11/12 12:59:55 PM | SILVER | DOWN | 5 sec | — | 0¢ | In play | — |
| 11/12 12:59:55 PM | USDCAD | DOWN | 5 sec | — | 0¢ | In play | — |
| 11/12 12:59:39 PM | GOLD | DOWN | 21 sec | — | 0¢ | In play | — |
| 11/12 12:59:39 PM | WTI | UP | 21 sec | — | 0¢ | In play | — |
| 11/12 12:59:39 PM | AUDUSD | DOWN | 21 sec | — | 0¢ | In play | — |
| 11/12 12:59:23 PM | USDJPY | UP | 37 sec | — | 0¢ | In play | — |
| 11/12 12:59:23 PM | BRENT | UP | 37 sec | — | 0¢ | In play | — |
| 11/12 12:59:08 PM | PLATINUM | DOWN | 51 sec | — | 0¢ | In play | — |
| 11/12 12:59:08 PM | COPPER | DOWN | 51 sec | — | 0¢ | In play | — |
| 11/12 12:58:52 PM | EURUSD | DOWN | 67 sec | — | 0¢ | In play | — |
| 11/12 12:58:52 PM | SOL | DOWN | 67 sec | +0.104% | 0¢ | In play | — |
| 11/12 12:57:14 PM | GBPUSD | DOWN | 2.8 min | — | 0¢ | In play | — |
| 11/12 12:56:27 PM | HYPE | DOWN | 3.5 min | +0.484% | 0¢ | In play | — |
| 11/12 12:56:11 PM | BNB | DOWN | 3.8 min | +0.161% | 0¢ | In play | — |
| 11/12 12:56:11 PM | BTC | DOWN | 3.8 min | +0.210% | 1¢ | In play | — |
| 11/12 12:55:37 PM | NEAR | DOWN | 4.4 min | +0.490% | 1¢ | ❌ Lost | -$0.15 |
| 11/12 12:55:37 PM | XRP | DOWN | 4.4 min | +0.282% | 1¢ | In play | — |
| 11/12 12:55:21 PM | ETH | DOWN | 4.7 min | +0.262% | 1¢ | In play | — |
| 11/12 12:54:50 PM | ZEC | DOWN | 5.2 min | +0.996% | 1¢ | In play | — |
| 11/12 12:53:46 PM | DOGE | DOWN | 6.2 min | +0.334% | 1¢ | In play | — |
| 11/12 12:44:44 PM | 2YRRATE | UP | 15 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/12 12:44:28 PM | GBPUSD | UP | 31 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/12 12:44:28 PM | HYPE | DOWN | 31 sec | +0.119% | 0¢ | ❌ Lost | $0.00 |
| 11/12 12:44:28 PM | NATGAS | DOWN | 31 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/12 12:43:54 PM | XRP | DOWN | 66 sec | +0.205% | 0¢ | ❌ Lost | $0.00 |
| 11/12 12:43:54 PM | BTC | UP | 66 sec | -0.084% | 1¢ | ❌ Lost | -$0.15 |
| 11/12 12:43:54 PM | BRENT | DOWN | 66 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/12 12:43:38 PM | ZEC | DOWN | 82 sec | +0.276% | 1¢ | ❌ Lost | $0.00 |
| 11/12 12:43:38 PM | WTI | DOWN | 82 sec | — | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
