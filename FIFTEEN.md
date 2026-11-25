# 15-Minute 1¢ Study

*Updated Wed Nov 25, 10:35 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 4887 finished bets | 1% | $209.50 | +39% | +4.29¢ | $87.70 / $121.80 |

*Expect about **84 buys a day** (~$12.54/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 4629 | $108.80 | +22% |
| Volatility model ≥ 2%, hold to the close | 9105 | $49.05 | +5% |
| Momentum model ≥ 2%, hold to the close | 7572 | -$33.80 | -4% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 67563 | 67529 | 256 (0%) | 1.07% | -$4,591.60 (-56%) | Hold to the close: -$4,591.60 (-56%) |

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
| Volatility model | 40057 | 4.5% | 0.4% (165) | -646% | ❌ Worse |
| Momentum model | 40057 | 4.4% | 0.4% (165) | -668% | ❌ Worse |
| Mean-reversion model | 40057 | 7.9% | 0.4% (165) | -785% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 40057 | 165 | -46% | -87% | -86% | -84% |
| Volatility model ≥ 2% | 9105 | 81 | +5% | -77% | -76% | -72% |
| Volatility model ≥ 5% | 4887 | 53 | +39% | -73% | -71% | -68% |
| Volatility model ≥ 10% | 2829 | 32 | +67% | -65% | -63% | -59% |
| Momentum model ≥ 2% | 7572 | 59 | -4% | -79% | -79% | -75% |
| Momentum model ≥ 5% | 4629 | 43 | +22% | -75% | -75% | -71% |
| Momentum model ≥ 10% | 3020 | 28 | +34% | -68% | -68% | -63% |
| Mean-reversion model ≥ 2% | 16303 | 113 | -24% | -82% | -82% | -80% |
| Mean-reversion model ≥ 5% | 11350 | 93 | -9% | -80% | -79% | -77% |
| Mean-reversion model ≥ 10% | 7539 | 66 | +0% | -78% | -77% | -75% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 40263 | 5% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 16066 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 11200 | 3% | 2% | 1% | 1% | 0% | 0% |
| **All** | 67529 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 256 | 0% | -$4,591.60 | -56% | — |
| Sell at 2¢ | 2769 | 4% | -$7,161.66 | -88% | 47 sec |
| Sell at 3¢ | 1861 | 3% | -$7,155.81 | -88% | 48 sec |
| Sell at 5¢ | 1260 | 2% | -$7,034.60 | -86% | 62 sec |
| Sell at 10¢ | 769 | 1% | -$6,762.21 | -83% | 65 sec |
| Sell at 25¢ | 415 | 1% | -$6,241.95 | -76% | 79 sec |
| Sell at 50¢ | 266 | 0% | -$5,638.10 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 13 | 0 | 31% | 23% | -100% | -47% | -20% |
| 5–10 min | 3495 | 17 | 11% | 4% | -54% | -81% | -83% |
| 2–5 min | 21896 | 116 | 7% | 3% | -48% | -86% | -86% |
| 1–2 min | 16856 | 58 | 3% | 2% | -61% | -92% | -92% |
| Under 1 min | 25269 | 65 | 1% | 0% | -63% | -87% | -87% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 4502 | 20 | 5% | 2% | -41% | -88% | -87% |
| HYPE | 4496 | 16 | 5% | 2% | -54% | -89% | -88% |
| SOL | 4490 | 20 | 4% | 2% | -42% | -86% | -86% |
| BNB | 4483 | 22 | 5% | 2% | -37% | -86% | -85% |
| DOGE | 4480 | 12 | 4% | 2% | -65% | -89% | -89% |
| ETH | 4474 | 19 | 7% | 3% | -47% | -82% | -82% |
| BTC | 4453 | 24 | 6% | 2% | -26% | -86% | -87% |
| NEAR | 4448 | 18 | 5% | 2% | -47% | -85% | -86% |
| XRP | 4437 | 16 | 4% | 2% | -54% | -89% | -88% |
| GOLD | 2378 | 8 | 5% | 2% | -59% | -82% | -84% |
| WTI | 2365 | 8 | 4% | 2% | -59% | -91% | -92% |
| SILVER | 2319 | 9 | 5% | 2% | -53% | -83% | -84% |
| PLATINUM | 2105 | 5 | 3% | 1% | -78% | -95% | -95% |
| EURUSD | 2059 | 7 | 3% | 1% | -68% | -91% | -90% |
| GBPUSD | 1999 | 8 | 2% | 1% | -63% | -96% | -96% |
| COPPER | 1995 | 6 | 2% | 1% | -72% | -78% | -78% |
| USDJPY | 1959 | 6 | 2% | 1% | -71% | -96% | -96% |
| NATGAS | 1952 | 10 | 2% | 1% | -52% | -77% | -77% |
| PALLADIUM | 1891 | 4 | 1% | 1% | -80% | -93% | -93% |
| AUDUSD | 1520 | 7 | 2% | 1% | -57% | -90% | -90% |
| USDCAD | 1431 | 1 | 3% | 1% | -93% | -96% | -96% |
| BRENT | 1061 | 1 | 2% | 1% | -91% | -96% | -97% |
| 10YRRATE | 550 | 2 | 3% | 1% | -66% | -77% | -76% |
| 2YRRATE | 510 | 4 | 4% | 2% | -27% | -57% | -56% |
| 30YRRATE | 510 | 0 | 3% | 1% | -100% | -95% | -93% |
| 5YRRATE | 500 | 2 | 4% | 2% | -63% | -94% | -95% |
| INX | 132 | 1 | 2% | 2% | -29% | -96% | -96% |
| USDMXN | 30 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 34541 | 132 | 4% | 2% | -56% | -88% | -88% |
| DOWN (bought NO) | 32988 | 124 | 4% | 2% | -57% | -87% | -87% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 5845 | 25 | 2% | 1% | -21% | -79% | -78% |
| 0.05–0.1% | 6393 | 26 | 3% | 2% | -35% | -91% | -91% |
| 0.1–0.2% | 9992 | 36 | 5% | 2% | -52% | -89% | -89% |
| 0.2–0.5% | 12694 | 56 | 7% | 3% | -50% | -86% | -86% |
| Over 0.5% | 5330 | 24 | 7% | 3% | -53% | -86% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 16330 | 50 | 4% | 2% | -65% | -88% | -88% |
| Morning (6am–12pm) | 16000 | 82 | 4% | 2% | -41% | -85% | -85% |
| Afternoon (12–6pm) | 16634 | 73 | 4% | 2% | -48% | -87% | -87% |
| Evening (6pm–12am) | 18565 | 51 | 4% | 2% | -68% | -89% | -89% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 5,102 |
| Time from buy to best bounce (bounced bets) | 51 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/25 10:29:49 AM | 30YRRATE | UP | 11 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/25 10:29:49 AM | ETH | UP | 11 sec | +0.013% | 1¢ | ❌ Lost | -$0.15 |
| 11/25 10:29:49 AM | BNB | UP | 11 sec | -0.094% | 0¢ | ❌ Lost | $0.00 |
| 11/25 10:29:34 AM | WTI | DOWN | 25 sec | — | 0¢ | ❌ Lost | $0.00 |
| 11/25 10:29:34 AM | SOL | DOWN | 25 sec | +0.068% | 0¢ | ❌ Lost | $0.00 |
| 11/25 10:29:34 AM | XRP | DOWN | 25 sec | +0.022% | 0¢ | ❌ Lost | $0.00 |
| 11/25 10:29:14 AM | HYPE | DOWN | 46 sec | +0.323% | 0¢ | ❌ Lost | $0.00 |
| 11/25 10:29:14 AM | AUDUSD | DOWN | 46 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/25 10:29:14 AM | SILVER | DOWN | 46 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 11/25 10:29:14 AM | DOGE | DOWN | 46 sec | +0.203% | 0¢ | ❌ Lost | $0.00 |
| 11/25 10:28:58 AM | ZEC | DOWN | 62 sec | +0.790% | 0¢ | ❌ Lost | $0.00 |
| 11/25 10:28:58 AM | GOLD | DOWN | 62 sec | — | 0¢ | ❌ Lost | $0.00 |
| 11/25 10:28:58 AM | BRENT | DOWN | 62 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/25 10:28:42 AM | NEAR | DOWN | 78 sec | +0.526% | 1¢ | ❌ Lost | -$0.15 |
| 11/25 10:28:27 AM | GBPUSD | DOWN | 1.5 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/25 10:28:11 AM | BTC | UP | 1.8 min | -0.277% | 6¢ | ❌ Lost | -$0.15 |
| 11/25 10:27:39 AM | 2YRRATE | UP | 2.3 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/25 10:26:35 AM | 5YRRATE | UP | 3.4 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/25 10:26:19 AM | 10YRRATE | UP | 3.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/25 10:14:05 AM | EURUSD | DOWN | 54 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/25 10:13:49 AM | USDCAD | UP | 70 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/25 10:12:59 AM | GBPUSD | DOWN | 2.0 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/25 10:11:36 AM | USDJPY | DOWN | 3.4 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/25 10:11:02 AM | BRENT | DOWN | 4.0 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/25 10:10:46 AM | COPPER | DOWN | 4.2 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/25 10:10:14 AM | AUDUSD | DOWN | 4.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/25 10:10:14 AM | NATGAS | DOWN | 4.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/25 10:09:37 AM | WTI | DOWN | 5.4 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/25 10:09:21 AM | 30YRRATE | DOWN | 5.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/25 10:09:21 AM | ETH | DOWN | 5.6 min | +0.969% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
