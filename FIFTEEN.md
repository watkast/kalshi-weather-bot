# 15-Minute 1¢ Study

*Updated Fri Oct 23, 4:09 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 2490 finished bets | 1% | $96.45 | +34% | +3.87¢ | $45.80 / $50.65 |

*Expect about **97 buys a day** (~$14.56/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 2305 | $53.15 | +21% |
| Volatility model ≥ 2%, hold to the close | 4623 | $8.20 | +1% |
| Momentum model ≥ 2%, hold to the close | 3853 | -$19.00 | -4% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 30351 | 30343 | 117 (0%) | 1.07% | -$2,064.60 (-56%) | Hold to the close: -$2,064.60 (-56%) |

*In play or awaiting result: 7. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 19160 | 4.6% | 0.4% (82) | -635% | ❌ Worse |
| Momentum model | 19160 | 4.6% | 0.4% (82) | -661% | ❌ Worse |
| Mean-reversion model | 19160 | 7.9% | 0.4% (82) | -765% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 19160 | 82 | -46% | -87% | -87% | -85% |
| Volatility model ≥ 2% | 4623 | 41 | +1% | -77% | -76% | -73% |
| Volatility model ≥ 5% | 2490 | 27 | +34% | -73% | -72% | -68% |
| Volatility model ≥ 10% | 1418 | 17 | +69% | -64% | -62% | -59% |
| Momentum model ≥ 2% | 3853 | 31 | -4% | -79% | -79% | -76% |
| Momentum model ≥ 5% | 2305 | 22 | +21% | -75% | -75% | -71% |
| Momentum model ≥ 10% | 1513 | 15 | +37% | -69% | -68% | -64% |
| Mean-reversion model ≥ 2% | 7691 | 54 | -23% | -83% | -82% | -80% |
| Mean-reversion model ≥ 5% | 5369 | 45 | -8% | -80% | -79% | -77% |
| Mean-reversion model ≥ 10% | 3570 | 32 | +2% | -77% | -77% | -75% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 19360 | 5% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 7328 | 2% | 2% | 1% | 1% | 0% | 0% |
| Financials | 3655 | 2% | 1% | 1% | 1% | 0% | 0% |
| **All** | 30343 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 117 | 0% | -$2,064.60 | -56% | — |
| Sell at 2¢ | 1132 | 4% | -$3,240.28 | -88% | 47 sec |
| Sell at 3¢ | 776 | 3% | -$3,231.96 | -87% | 48 sec |
| Sell at 5¢ | 544 | 2% | -$3,181.00 | -86% | 61 sec |
| Sell at 10¢ | 332 | 1% | -$3,057.68 | -83% | 64 sec |
| Sell at 25¢ | 185 | 1% | -$2,810.25 | -76% | 82 sec |
| Sell at 50¢ | 119 | 0% | -$2,535.35 | -68% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 1276 | 7 | 11% | 4% | -48% | -80% | -82% |
| 2–5 min | 9715 | 53 | 7% | 3% | -46% | -87% | -87% |
| 1–2 min | 7730 | 29 | 3% | 1% | -59% | -91% | -91% |
| Under 1 min | 11618 | 28 | 1% | 0% | -66% | -86% | -85% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 2170 | 12 | 5% | 2% | -31% | -89% | -89% |
| BNB | 2163 | 12 | 5% | 2% | -31% | -83% | -82% |
| HYPE | 2160 | 8 | 5% | 3% | -54% | -88% | -86% |
| SOL | 2153 | 5 | 4% | 2% | -71% | -92% | -92% |
| ETH | 2151 | 10 | 6% | 3% | -44% | -86% | -85% |
| DOGE | 2147 | 4 | 4% | 2% | -77% | -90% | -89% |
| XRP | 2141 | 9 | 3% | 1% | -48% | -88% | -88% |
| NEAR | 2138 | 12 | 5% | 3% | -27% | -81% | -81% |
| BTC | 2137 | 12 | 5% | 2% | -25% | -88% | -89% |
| GOLD | 1190 | 4 | 4% | 2% | -60% | -81% | -83% |
| SILVER | 1156 | 5 | 4% | 1% | -50% | -82% | -82% |
| WTI | 1130 | 3 | 3% | 1% | -69% | -94% | -95% |
| PLATINUM | 1010 | 0 | 1% | 1% | -100% | -98% | -98% |
| COPPER | 987 | 4 | 1% | 1% | -62% | -69% | -69% |
| EURUSD | 938 | 3 | 2% | 1% | -70% | -86% | -86% |
| NATGAS | 928 | 5 | 2% | 1% | -50% | -86% | -86% |
| PALLADIUM | 897 | 2 | 1% | 0% | -79% | -88% | -88% |
| GBPUSD | 884 | 1 | 2% | 1% | -89% | -96% | -96% |
| USDJPY | 866 | 5 | 1% | 1% | -46% | -98% | -97% |
| AUDUSD | 428 | 0 | 1% | 0% | -100% | -98% | -98% |
| USDCAD | 387 | 0 | 1% | 0% | -100% | -98% | -99% |
| 10YRRATE | 43 | 0 | 0% | 0% | -100% | -100% | -100% |
| 2YRRATE | 40 | 1 | 2% | 0% | +133% | +138% | +133% |
| 30YRRATE | 39 | 0 | 0% | 0% | -100% | -100% | -100% |
| 5YRRATE | 30 | 0 | 0% | 0% | -100% | -100% | -100% |
| BRENT | 30 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 15314 | 64 | 4% | 2% | -52% | -87% | -86% |
| DOWN (bought NO) | 15029 | 53 | 4% | 2% | -59% | -88% | -88% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 3186 | 17 | 2% | 1% | -10% | -79% | -78% |
| 0.05–0.1% | 3330 | 11 | 3% | 2% | -51% | -92% | -91% |
| 0.1–0.2% | 4999 | 18 | 5% | 2% | -55% | -89% | -89% |
| 0.2–0.5% | 5671 | 28 | 6% | 3% | -46% | -87% | -86% |
| Over 0.5% | 2170 | 10 | 7% | 3% | -52% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 7532 | 31 | 4% | 2% | -53% | -84% | -84% |
| Morning (6am–12pm) | 7425 | 34 | 4% | 2% | -48% | -88% | -87% |
| Afternoon (12–6pm) | 7224 | 24 | 4% | 2% | -61% | -87% | -88% |
| Evening (6pm–12am) | 8162 | 28 | 3% | 2% | -61% | -90% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,581 |
| Time from buy to best bounce (bounced bets) | 49 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/23 3:59:53 PM | XRP | UP | 6 sec | -0.023% | 0¢ | ❌ Lost | $0.00 |
| 10/23 3:59:37 PM | BRENT | DOWN | 22 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/23 3:59:37 PM | BTC | DOWN | 22 sec | +0.028% | 0¢ | ❌ Lost | $0.00 |
| 10/23 3:59:21 PM | ZEC | DOWN | 38 sec | +0.167% | 0¢ | ❌ Lost | -$0.15 |
| 10/23 3:59:21 PM | DOGE | DOWN | 38 sec | +0.032% | 0¢ | ❌ Lost | $0.00 |
| 10/23 3:59:05 PM | BNB | DOWN | 55 sec | +0.013% | 0¢ | ❌ Lost | $0.00 |
| 10/23 3:58:47 PM | NEAR | UP | 73 sec | -0.320% | 0¢ | ❌ Lost | $0.00 |
| 10/23 3:58:47 PM | HYPE | DOWN | 73 sec | +0.171% | 1¢ | ❌ Lost | -$0.15 |
| 10/23 3:58:00 PM | SOL | UP | 2.0 min | -0.181% | 0¢ | ❌ Lost | -$0.15 |
| 10/23 3:44:38 PM | XRP | UP | 22 sec | -0.084% | 0¢ | ❌ Lost | $0.00 |
| 10/23 3:44:22 PM | HYPE | DOWN | 38 sec | +0.045% | 0¢ | ❌ Lost | -$0.15 |
| 10/23 3:44:22 PM | DOGE | UP | 38 sec | -0.097% | 0¢ | ❌ Lost | $0.00 |
| 10/23 3:44:22 PM | ZEC | UP | 38 sec | -0.242% | 0¢ | ❌ Lost | $0.00 |
| 10/23 3:44:22 PM | SOL | UP | 38 sec | -0.089% | 0¢ | ❌ Lost | $0.00 |
| 10/23 3:44:06 PM | WTI | DOWN | 54 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/23 3:43:48 PM | NEAR | UP | 72 sec | -0.394% | 0¢ | ❌ Lost | $0.00 |
| 10/23 3:43:32 PM | BTC | UP | 88 sec | -0.064% | 1¢ | ❌ Lost | -$0.15 |
| 10/23 3:43:16 PM | ETH | UP | 1.7 min | -0.055% | 0¢ | ❌ Lost | -$0.15 |
| 10/23 3:42:45 PM | BNB | UP | 2.2 min | -0.127% | 0¢ | ❌ Lost | -$0.15 |
| 10/23 3:29:47 PM | HYPE | UP | 12 sec | -0.069% | 0¢ | ❌ Lost | $0.00 |
| 10/23 3:29:47 PM | WTI | DOWN | 12 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/23 3:29:47 PM | BTC | UP | 12 sec | -0.034% | 0¢ | ❌ Lost | $0.00 |
| 10/23 3:29:31 PM | DOGE | UP | 28 sec | -0.138% | 0¢ | ❌ Lost | $0.00 |
| 10/23 3:29:31 PM | ETH | UP | 28 sec | -0.053% | 0¢ | ❌ Lost | -$0.15 |
| 10/23 3:29:15 PM | BNB | UP | 44 sec | -0.080% | 1¢ | ❌ Lost | -$0.15 |
| 10/23 3:29:15 PM | XRP | UP | 44 sec | -0.138% | 0¢ | ❌ Lost | $0.00 |
| 10/23 3:29:01 PM | NEAR | UP | 59 sec | -0.197% | 1¢ | ❌ Lost | -$0.15 |
| 10/23 3:29:01 PM | SOL | UP | 59 sec | -0.105% | 0¢ | ❌ Lost | $0.00 |
| 10/23 3:28:36 PM | ZEC | UP | 84 sec | -0.218% | 0¢ | ❌ Lost | $0.00 |
| 10/23 3:27:01 PM | BRENT | UP | 3.0 min | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
