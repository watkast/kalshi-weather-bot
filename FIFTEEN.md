# 15-Minute 1¢ Study

*Updated Thu Nov 19, 10:46 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 4587 finished bets | 1% | $209.40 | +41% | +4.57¢ | $76.80 / $132.60 |

*Expect about **87 buys a day** (~$13.00/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 4328 | $109.15 | +23% |
| Volatility model ≥ 2%, hold to the close | 8567 | $64.05 | +6% |
| Momentum model ≥ 2%, hold to the close | 7110 | -$16.05 | -2% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 62673 | 62622 | 242 (0%) | 1.07% | -$4,228.25 (-56%) | Hold to the close: -$4,228.25 (-56%) |

*In play or awaiting result: 23. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 37159 | 4.5% | 0.4% (155) | -636% | ❌ Worse |
| Momentum model | 37159 | 4.4% | 0.4% (155) | -662% | ❌ Worse |
| Mean-reversion model | 37159 | 7.9% | 0.4% (155) | -772% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 37159 | 155 | -46% | -87% | -87% | -85% |
| Volatility model ≥ 2% | 8567 | 78 | +6% | -77% | -76% | -72% |
| Volatility model ≥ 5% | 4587 | 51 | +41% | -72% | -71% | -68% |
| Volatility model ≥ 10% | 2637 | 30 | +66% | -63% | -62% | -59% |
| Momentum model ≥ 2% | 7110 | 57 | -2% | -79% | -78% | -75% |
| Momentum model ≥ 5% | 4328 | 41 | +23% | -75% | -74% | -70% |
| Momentum model ≥ 10% | 2823 | 26 | +32% | -67% | -66% | -62% |
| Mean-reversion model ≥ 2% | 15176 | 109 | -21% | -82% | -82% | -79% |
| Mean-reversion model ≥ 5% | 10558 | 89 | -6% | -80% | -79% | -77% |
| Mean-reversion model ≥ 10% | 7016 | 64 | +4% | -77% | -77% | -74% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 37365 | 5% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 15017 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 10240 | 3% | 2% | 1% | 1% | 0% | 0% |
| **All** | 62622 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 242 | 0% | -$4,228.25 | -56% | — |
| Sell at 2¢ | 2540 | 4% | -$6,661.85 | -87% | 47 sec |
| Sell at 3¢ | 1712 | 3% | -$6,654.57 | -87% | 48 sec |
| Sell at 5¢ | 1170 | 2% | -$6,533.75 | -86% | 63 sec |
| Sell at 10¢ | 717 | 1% | -$6,270.98 | -82% | 65 sec |
| Sell at 25¢ | 383 | 1% | -$5,788.52 | -76% | 80 sec |
| Sell at 50¢ | 248 | 0% | -$5,228.25 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 13 | 0 | 31% | 23% | -100% | -47% | -20% |
| 5–10 min | 3203 | 17 | 11% | 4% | -50% | -81% | -82% |
| 2–5 min | 20290 | 109 | 7% | 3% | -47% | -86% | -87% |
| 1–2 min | 15672 | 53 | 3% | 2% | -62% | -92% | -92% |
| Under 1 min | 23444 | 63 | 1% | 0% | -62% | -86% | -86% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 4178 | 19 | 5% | 2% | -40% | -88% | -87% |
| SOL | 4175 | 19 | 4% | 2% | -41% | -86% | -86% |
| HYPE | 4166 | 12 | 4% | 2% | -63% | -89% | -88% |
| DOGE | 4158 | 11 | 4% | 2% | -66% | -89% | -89% |
| BNB | 4155 | 21 | 5% | 2% | -36% | -85% | -85% |
| ETH | 4152 | 19 | 7% | 3% | -43% | -82% | -82% |
| BTC | 4135 | 22 | 5% | 2% | -28% | -86% | -88% |
| NEAR | 4131 | 18 | 5% | 2% | -43% | -85% | -86% |
| XRP | 4115 | 16 | 3% | 2% | -51% | -89% | -88% |
| GOLD | 2236 | 7 | 5% | 2% | -62% | -82% | -84% |
| WTI | 2216 | 7 | 4% | 1% | -62% | -91% | -92% |
| SILVER | 2177 | 9 | 5% | 2% | -51% | -83% | -83% |
| PLATINUM | 1980 | 5 | 3% | 1% | -76% | -95% | -95% |
| EURUSD | 1941 | 7 | 3% | 1% | -66% | -91% | -90% |
| GBPUSD | 1873 | 8 | 2% | 1% | -60% | -96% | -95% |
| COPPER | 1864 | 6 | 2% | 1% | -70% | -77% | -77% |
| USDJPY | 1826 | 6 | 2% | 1% | -69% | -96% | -96% |
| NATGAS | 1823 | 10 | 2% | 1% | -49% | -76% | -76% |
| PALLADIUM | 1783 | 4 | 1% | 1% | -79% | -93% | -93% |
| AUDUSD | 1378 | 6 | 2% | 1% | -59% | -90% | -90% |
| USDCAD | 1317 | 1 | 3% | 1% | -93% | -95% | -96% |
| BRENT | 938 | 0 | 2% | 1% | -100% | -97% | -98% |
| 10YRRATE | 480 | 2 | 3% | 1% | -61% | -75% | -73% |
| 2YRRATE | 456 | 4 | 4% | 2% | -18% | -52% | -51% |
| 30YRRATE | 441 | 0 | 2% | 1% | -100% | -96% | -94% |
| 5YRRATE | 431 | 2 | 4% | 2% | -57% | -94% | -95% |
| INX | 97 | 1 | 2% | 1% | -4% | -96% | -97% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 31983 | 124 | 4% | 2% | -55% | -88% | -88% |
| DOWN (bought NO) | 30639 | 118 | 4% | 2% | -56% | -87% | -87% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 5558 | 25 | 2% | 1% | -19% | -78% | -78% |
| 0.05–0.1% | 6055 | 24 | 3% | 2% | -38% | -91% | -91% |
| 0.1–0.2% | 9353 | 34 | 5% | 2% | -53% | -89% | -89% |
| 0.2–0.5% | 11631 | 51 | 7% | 3% | -50% | -86% | -86% |
| Over 0.5% | 4759 | 23 | 7% | 3% | -49% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 15189 | 47 | 4% | 2% | -65% | -88% | -88% |
| Morning (6am–12pm) | 14806 | 79 | 5% | 2% | -39% | -85% | -84% |
| Afternoon (12–6pm) | 15444 | 66 | 4% | 2% | -50% | -87% | -87% |
| Evening (6pm–12am) | 17183 | 50 | 4% | 2% | -67% | -90% | -89% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 5,010 |
| Time from buy to best bounce (bounced bets) | 51 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/19 10:44:58 PM | BTC | UP | 2 sec | -0.020% | 1¢ | ❌ Lost | -$0.15 |
| 11/19 10:44:58 PM | SILVER | UP | 2 sec | — | 0¢ | In play | — |
| 11/19 10:44:58 PM | PALLADIUM | UP | 2 sec | — | 0¢ | In play | — |
| 11/19 10:44:58 PM | EURUSD | UP | 2 sec | — | 0¢ | In play | — |
| 11/19 10:44:58 PM | ETH | UP | 2 sec | -0.029% | 0¢ | In play | — |
| 11/19 10:44:42 PM | BRENT | UP | 18 sec | — | 0¢ | In play | — |
| 11/19 10:44:26 PM | DOGE | DOWN | 34 sec | +0.070% | 0¢ | ❌ Lost | -$0.15 |
| 11/19 10:44:26 PM | BNB | DOWN | 34 sec | -0.046% | 0¢ | In play | — |
| 11/19 10:44:10 PM | WTI | UP | 50 sec | — | 1¢ | In play | — |
| 11/19 10:44:10 PM | SOL | DOWN | 50 sec | +0.175% | 0¢ | In play | — |
| 11/19 10:44:10 PM | XRP | UP | 50 sec | -0.114% | 0¢ | In play | — |
| 11/19 10:43:39 PM | PLATINUM | UP | 80 sec | — | 0¢ | In play | — |
| 11/19 10:43:23 PM | AUDUSD | UP | 1.6 min | — | 0¢ | In play | — |
| 11/19 10:42:51 PM | USDJPY | UP | 2.1 min | — | 0¢ | In play | — |
| 11/19 10:42:19 PM | USDCAD | DOWN | 2.7 min | — | 0¢ | In play | — |
| 11/19 10:42:19 PM | COPPER | UP | 2.7 min | — | 0¢ | In play | — |
| 11/19 10:42:19 PM | HYPE | DOWN | 2.7 min | +0.547% | 0¢ | In play | — |
| 11/19 10:42:03 PM | NEAR | DOWN | 3.0 min | +0.484% | 1¢ | ❌ Lost | -$0.15 |
| 11/19 10:42:03 PM | ZEC | DOWN | 3.0 min | +0.552% | 1¢ | In play | — |
| 11/19 10:40:45 PM | GBPUSD | UP | 4.2 min | — | 0¢ | In play | — |
| 11/19 10:29:57 PM | COPPER | UP | 2 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/19 10:29:57 PM | GBPUSD | UP | 2 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/19 10:29:41 PM | BRENT | DOWN | 18 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/19 10:29:41 PM | NATGAS | DOWN | 18 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/19 10:29:41 PM | USDCAD | DOWN | 18 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/19 10:29:25 PM | WTI | DOWN | 34 sec | — | 0¢ | ❌ Lost | $0.00 |
| 11/19 10:29:25 PM | AUDUSD | UP | 34 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/19 10:28:53 PM | GOLD | DOWN | 67 sec | — | 3¢ | ❌ Lost | -$0.15 |
| 11/19 10:28:53 PM | PALLADIUM | DOWN | 67 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/19 10:28:53 PM | ZEC | DOWN | 67 sec | +0.260% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
