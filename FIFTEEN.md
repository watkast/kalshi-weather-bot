# 15-Minute 1¢ Study

*Updated Wed Nov 25, 9:32 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 4884 finished bets | 1% | $209.80 | +39% | +4.30¢ | $87.85 / $121.95 |

*Expect about **84 buys a day** (~$12.54/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 4627 | $108.95 | +22% |
| Volatility model ≥ 2%, hold to the close | 9097 | $50.10 | +5% |
| Momentum model ≥ 2%, hold to the close | 7568 | -$33.50 | -4% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 67465 | 67431 | 256 (0%) | 1.07% | -$4,578.85 (-56%) | Hold to the close: -$4,578.85 (-56%) |

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
| Volatility model | 40021 | 4.5% | 0.4% (165) | -646% | ❌ Worse |
| Momentum model | 40021 | 4.4% | 0.4% (165) | -669% | ❌ Worse |
| Mean-reversion model | 40021 | 7.9% | 0.4% (165) | -785% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 40021 | 165 | -46% | -87% | -86% | -84% |
| Volatility model ≥ 2% | 9097 | 81 | +5% | -77% | -76% | -73% |
| Volatility model ≥ 5% | 4884 | 53 | +39% | -73% | -72% | -68% |
| Volatility model ≥ 10% | 2827 | 32 | +67% | -65% | -63% | -59% |
| Momentum model ≥ 2% | 7568 | 59 | -4% | -79% | -79% | -75% |
| Momentum model ≥ 5% | 4627 | 43 | +22% | -75% | -75% | -71% |
| Momentum model ≥ 10% | 3018 | 28 | +34% | -68% | -68% | -63% |
| Mean-reversion model ≥ 2% | 16281 | 113 | -23% | -82% | -82% | -80% |
| Mean-reversion model ≥ 5% | 11333 | 93 | -9% | -80% | -79% | -77% |
| Mean-reversion model ≥ 10% | 7531 | 66 | +0% | -78% | -77% | -75% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 40227 | 5% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 16040 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 11164 | 3% | 2% | 1% | 1% | 0% | 0% |
| **All** | 67431 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 256 | 0% | -$4,578.85 | -56% | — |
| Sell at 2¢ | 2766 | 4% | -$7,149.69 | -88% | 47 sec |
| Sell at 3¢ | 1860 | 3% | -$7,143.45 | -88% | 48 sec |
| Sell at 5¢ | 1259 | 2% | -$7,022.50 | -86% | 62 sec |
| Sell at 10¢ | 769 | 1% | -$6,749.46 | -83% | 65 sec |
| Sell at 25¢ | 415 | 1% | -$6,229.20 | -76% | 79 sec |
| Sell at 50¢ | 266 | 0% | -$5,625.35 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 13 | 0 | 31% | 23% | -100% | -47% | -20% |
| 5–10 min | 3475 | 17 | 11% | 4% | -54% | -81% | -82% |
| 2–5 min | 21857 | 116 | 7% | 3% | -48% | -86% | -86% |
| 1–2 min | 16837 | 58 | 3% | 2% | -61% | -92% | -92% |
| Under 1 min | 25249 | 65 | 1% | 0% | -63% | -87% | -87% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 4498 | 20 | 5% | 2% | -41% | -88% | -87% |
| HYPE | 4492 | 16 | 5% | 2% | -54% | -89% | -88% |
| SOL | 4486 | 20 | 4% | 2% | -42% | -86% | -86% |
| BNB | 4479 | 22 | 5% | 2% | -37% | -86% | -85% |
| DOGE | 4476 | 12 | 4% | 2% | -65% | -89% | -89% |
| ETH | 4470 | 19 | 7% | 3% | -46% | -82% | -82% |
| BTC | 4449 | 24 | 6% | 2% | -26% | -86% | -87% |
| NEAR | 4444 | 18 | 5% | 2% | -47% | -85% | -86% |
| XRP | 4433 | 16 | 4% | 2% | -54% | -89% | -88% |
| GOLD | 2374 | 8 | 5% | 2% | -59% | -82% | -84% |
| WTI | 2361 | 8 | 4% | 2% | -59% | -91% | -92% |
| SILVER | 2315 | 9 | 5% | 2% | -53% | -83% | -84% |
| PLATINUM | 2102 | 5 | 3% | 1% | -78% | -95% | -95% |
| EURUSD | 2056 | 7 | 3% | 1% | -68% | -91% | -90% |
| GBPUSD | 1995 | 8 | 2% | 1% | -63% | -96% | -96% |
| COPPER | 1993 | 6 | 2% | 1% | -72% | -78% | -78% |
| USDJPY | 1957 | 6 | 2% | 1% | -71% | -96% | -96% |
| NATGAS | 1950 | 10 | 2% | 1% | -52% | -77% | -77% |
| PALLADIUM | 1888 | 4 | 1% | 1% | -80% | -93% | -93% |
| AUDUSD | 1516 | 7 | 2% | 1% | -57% | -90% | -90% |
| USDCAD | 1428 | 1 | 3% | 1% | -93% | -96% | -96% |
| BRENT | 1057 | 1 | 2% | 1% | -91% | -96% | -97% |
| 10YRRATE | 546 | 2 | 3% | 1% | -66% | -77% | -76% |
| 30YRRATE | 507 | 0 | 3% | 1% | -100% | -95% | -93% |
| 2YRRATE | 506 | 4 | 4% | 2% | -26% | -57% | -56% |
| 5YRRATE | 496 | 2 | 4% | 2% | -62% | -94% | -95% |
| INX | 129 | 1 | 2% | 2% | -28% | -96% | -96% |
| USDMXN | 28 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 34508 | 132 | 4% | 2% | -56% | -88% | -88% |
| DOWN (bought NO) | 32923 | 124 | 4% | 2% | -56% | -87% | -87% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 5843 | 25 | 2% | 1% | -21% | -79% | -78% |
| 0.05–0.1% | 6391 | 26 | 3% | 2% | -35% | -91% | -91% |
| 0.1–0.2% | 9992 | 36 | 5% | 2% | -52% | -89% | -89% |
| 0.2–0.5% | 12688 | 56 | 7% | 3% | -50% | -86% | -86% |
| Over 0.5% | 5304 | 24 | 7% | 3% | -53% | -86% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 16330 | 50 | 4% | 2% | -65% | -88% | -88% |
| Morning (6am–12pm) | 15902 | 82 | 4% | 2% | -41% | -85% | -85% |
| Afternoon (12–6pm) | 16634 | 73 | 4% | 2% | -48% | -87% | -87% |
| Evening (6pm–12am) | 18565 | 51 | 4% | 2% | -68% | -89% | -89% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 5,109 |
| Time from buy to best bounce (bounced bets) | 51 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/25 9:29:49 AM | BNB | UP | 11 sec | -0.098% | 0¢ | ❌ Lost | $0.00 |
| 11/25 9:29:49 AM | SILVER | DOWN | 11 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/25 9:29:34 AM | XRP | DOWN | 25 sec | +0.122% | 0¢ | ❌ Lost | $0.00 |
| 11/25 9:29:34 AM | SOL | UP | 25 sec | -0.073% | 0¢ | ❌ Lost | $0.00 |
| 11/25 9:29:34 AM | BTC | DOWN | 25 sec | +0.093% | 1¢ | ❌ Lost | -$0.15 |
| 11/25 9:29:16 AM | NEAR | UP | 43 sec | -0.455% | 0¢ | ❌ Lost | $0.00 |
| 11/25 9:29:16 AM | DOGE | UP | 43 sec | -0.235% | 0¢ | ❌ Lost | $0.00 |
| 11/25 9:29:16 AM | ZEC | UP | 43 sec | -0.528% | 0¢ | ❌ Lost | $0.00 |
| 11/25 9:29:00 AM | ETH | UP | 59 sec | -0.313% | 0¢ | ❌ Lost | $0.00 |
| 11/25 9:28:44 AM | BRENT | UP | 75 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/25 9:28:28 AM | WTI | UP | 1.5 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/25 9:28:28 AM | USDJPY | UP | 1.5 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/25 9:28:28 AM | INX | DOWN | 1.5 min | — | 5¢ | ❌ Lost | -$0.15 |
| 11/25 9:28:28 AM | HYPE | DOWN | 1.5 min | +0.578% | 0¢ | ❌ Lost | $0.00 |
| 11/25 9:28:08 AM | GBPUSD | DOWN | 1.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/25 9:28:08 AM | GOLD | DOWN | 1.9 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/25 9:27:21 AM | AUDUSD | DOWN | 2.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/25 9:27:03 AM | PLATINUM | DOWN | 3.0 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/25 9:25:40 AM | 2YRRATE | DOWN | 4.3 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/25 9:25:24 AM | 5YRRATE | DOWN | 4.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/25 9:25:08 AM | 30YRRATE | DOWN | 4.8 min | — | 2¢ | ❌ Lost | -$0.15 |
| 11/25 9:25:08 AM | 10YRRATE | DOWN | 4.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/25 9:14:55 AM | USDCAD | UP | 5 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/25 9:14:55 AM | AUDUSD | DOWN | 5 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/25 9:14:55 AM | WTI | DOWN | 5 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 11/25 9:14:55 AM | BRENT | UP | 5 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/25 9:14:22 AM | XRP | DOWN | 37 sec | +0.044% | 1¢ | ❌ Lost | -$0.15 |
| 11/25 9:14:22 AM | PLATINUM | DOWN | 37 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/25 9:14:22 AM | HYPE | DOWN | 37 sec | +0.242% | 0¢ | ❌ Lost | $0.00 |
| 11/25 9:14:06 AM | SILVER | DOWN | 53 sec | — | 0¢ | ❌ Lost | $0.00 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
