# 15-Minute 1¢ Study

*Updated Fri Nov 20, 6:01 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 4595 finished bets | 1% | $209.10 | +41% | +4.55¢ | $76.65 / $132.45 |

*Expect about **86 buys a day** (~$12.94/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 4337 | $108.55 | +23% |
| Volatility model ≥ 2%, hold to the close | 8582 | $62.85 | +6% |
| Momentum model ≥ 2%, hold to the close | 7122 | -$17.10 | -2% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 62907 | 62873 | 243 (0%) | 1.07% | -$4,242.60 (-55%) | Hold to the close: -$4,242.60 (-55%) |

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
| Volatility model | 37268 | 4.5% | 0.4% (156) | -636% | ❌ Worse |
| Momentum model | 37268 | 4.4% | 0.4% (156) | -661% | ❌ Worse |
| Mean-reversion model | 37268 | 7.9% | 0.4% (156) | -771% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 37268 | 156 | -46% | -87% | -87% | -84% |
| Volatility model ≥ 2% | 8582 | 78 | +6% | -77% | -76% | -72% |
| Volatility model ≥ 5% | 4595 | 51 | +41% | -72% | -71% | -68% |
| Volatility model ≥ 10% | 2644 | 30 | +66% | -63% | -62% | -59% |
| Momentum model ≥ 2% | 7122 | 57 | -2% | -79% | -78% | -75% |
| Momentum model ≥ 5% | 4337 | 41 | +23% | -75% | -74% | -70% |
| Momentum model ≥ 10% | 2830 | 26 | +31% | -67% | -67% | -62% |
| Mean-reversion model ≥ 2% | 15217 | 109 | -21% | -82% | -82% | -79% |
| Mean-reversion model ≥ 5% | 10586 | 89 | -7% | -80% | -79% | -77% |
| Mean-reversion model ≥ 10% | 7033 | 64 | +4% | -77% | -77% | -74% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 37474 | 5% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 15103 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 10296 | 3% | 2% | 1% | 1% | 0% | 0% |
| **All** | 62873 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 243 | 0% | -$4,242.60 | -55% | — |
| Sell at 2¢ | 2553 | 4% | -$6,686.82 | -87% | 47 sec |
| Sell at 3¢ | 1721 | 3% | -$6,679.41 | -87% | 48 sec |
| Sell at 5¢ | 1175 | 2% | -$6,558.85 | -86% | 63 sec |
| Sell at 10¢ | 719 | 1% | -$6,296.71 | -82% | 65 sec |
| Sell at 25¢ | 385 | 1% | -$5,810.25 | -76% | 80 sec |
| Sell at 50¢ | 249 | 0% | -$5,249.85 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 13 | 0 | 31% | 23% | -100% | -47% | -20% |
| 5–10 min | 3225 | 17 | 11% | 4% | -50% | -81% | -82% |
| 2–5 min | 20366 | 109 | 7% | 3% | -47% | -86% | -86% |
| 1–2 min | 15729 | 54 | 3% | 2% | -62% | -92% | -92% |
| Under 1 min | 23540 | 63 | 1% | 0% | -62% | -86% | -86% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 4189 | 19 | 5% | 2% | -40% | -88% | -87% |
| SOL | 4187 | 19 | 4% | 2% | -42% | -86% | -86% |
| HYPE | 4179 | 13 | 4% | 2% | -60% | -89% | -88% |
| DOGE | 4170 | 11 | 4% | 2% | -66% | -90% | -89% |
| BNB | 4168 | 21 | 5% | 2% | -36% | -85% | -85% |
| ETH | 4165 | 19 | 7% | 3% | -43% | -82% | -82% |
| BTC | 4147 | 22 | 5% | 2% | -28% | -86% | -88% |
| NEAR | 4142 | 18 | 5% | 2% | -43% | -85% | -86% |
| XRP | 4127 | 16 | 3% | 2% | -51% | -89% | -88% |
| GOLD | 2246 | 7 | 5% | 2% | -62% | -82% | -84% |
| WTI | 2226 | 7 | 4% | 1% | -62% | -91% | -92% |
| SILVER | 2189 | 9 | 5% | 2% | -51% | -83% | -83% |
| PLATINUM | 1993 | 5 | 3% | 1% | -77% | -95% | -95% |
| EURUSD | 1948 | 7 | 3% | 1% | -66% | -91% | -90% |
| GBPUSD | 1884 | 8 | 2% | 1% | -60% | -96% | -95% |
| COPPER | 1876 | 6 | 2% | 1% | -70% | -77% | -77% |
| USDJPY | 1836 | 6 | 2% | 1% | -69% | -96% | -96% |
| NATGAS | 1833 | 10 | 2% | 1% | -49% | -76% | -76% |
| PALLADIUM | 1794 | 4 | 1% | 1% | -79% | -92% | -93% |
| AUDUSD | 1386 | 6 | 2% | 1% | -60% | -90% | -90% |
| USDCAD | 1326 | 1 | 3% | 1% | -93% | -95% | -96% |
| BRENT | 946 | 0 | 2% | 1% | -100% | -97% | -98% |
| 10YRRATE | 483 | 2 | 3% | 1% | -61% | -75% | -73% |
| 2YRRATE | 459 | 4 | 4% | 2% | -19% | -53% | -51% |
| 30YRRATE | 444 | 0 | 2% | 1% | -100% | -96% | -94% |
| 5YRRATE | 433 | 2 | 4% | 2% | -57% | -94% | -95% |
| INX | 97 | 1 | 2% | 1% | -4% | -96% | -97% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 32098 | 125 | 4% | 2% | -55% | -88% | -88% |
| DOWN (bought NO) | 30775 | 118 | 4% | 2% | -56% | -87% | -87% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 5572 | 25 | 2% | 1% | -19% | -78% | -78% |
| 0.05–0.1% | 6071 | 24 | 3% | 2% | -38% | -91% | -91% |
| 0.1–0.2% | 9379 | 34 | 5% | 2% | -53% | -89% | -89% |
| 0.2–0.5% | 11669 | 52 | 7% | 3% | -49% | -86% | -86% |
| Over 0.5% | 4774 | 23 | 7% | 3% | -50% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 15327 | 48 | 4% | 2% | -64% | -88% | -88% |
| Morning (6am–12pm) | 14806 | 79 | 5% | 2% | -39% | -85% | -84% |
| Afternoon (12–6pm) | 15444 | 66 | 4% | 2% | -50% | -87% | -87% |
| Evening (6pm–12am) | 17296 | 50 | 4% | 2% | -67% | -89% | -89% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,993 |
| Time from buy to best bounce (bounced bets) | 51 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/20 5:59:59 AM | ETH | UP | 0 sec | -0.085% | 0¢ | ❌ Lost | $0.00 |
| 11/20 5:59:59 AM | SILVER | DOWN | 0 sec | — | 0¢ | ❌ Lost | $0.00 |
| 11/20 5:59:59 AM | GOLD | DOWN | 0 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/20 5:59:59 AM | BTC | UP | 0 sec | -0.046% | 0¢ | ❌ Lost | $0.00 |
| 11/20 5:59:43 AM | 10YRRATE | DOWN | 16 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/20 5:59:43 AM | GBPUSD | DOWN | 16 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/20 5:59:43 AM | 30YRRATE | DOWN | 16 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/20 5:59:43 AM | PALLADIUM | DOWN | 16 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/20 5:59:43 AM | BNB | UP | 16 sec | -0.092% | 0¢ | ❌ Lost | $0.00 |
| 11/20 5:59:27 AM | ZEC | UP | 32 sec | -0.102% | 1¢ | ❌ Lost | -$0.15 |
| 11/20 5:59:27 AM | XRP | UP | 32 sec | -0.095% | 0¢ | ❌ Lost | $0.00 |
| 11/20 5:58:55 AM | HYPE | UP | 65 sec | -0.236% | 1¢ | ❌ Lost | -$0.15 |
| 11/20 5:58:39 AM | SOL | DOWN | 81 sec | +0.171% | 1¢ | ❌ Lost | -$0.15 |
| 11/20 5:58:39 AM | EURUSD | UP | 81 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 11/20 5:58:07 AM | NATGAS | DOWN | 1.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/20 5:56:46 AM | NEAR | DOWN | 3.2 min | +0.479% | 1¢ | ❌ Lost | -$0.15 |
| 11/20 5:56:30 AM | DOGE | DOWN | 3.5 min | +0.388% | 1¢ | ❌ Lost | -$0.15 |
| 11/20 5:56:14 AM | PLATINUM | DOWN | 3.8 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/20 1:29:44 AM | USDCAD | DOWN | 15 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/20 1:29:44 AM | NEAR | DOWN | 15 sec | -0.063% | 0¢ | ❌ Lost | -$0.15 |
| 11/20 1:29:44 AM | ZEC | UP | 15 sec | -0.034% | 0¢ | ❌ Lost | $0.00 |
| 11/20 1:29:28 AM | HYPE | DOWN | 32 sec | +0.062% | 0¢ | ❌ Lost | $0.00 |
| 11/20 1:29:28 AM | ETH | DOWN | 32 sec | +0.037% | 0¢ | ❌ Lost | -$0.15 |
| 11/20 1:29:11 AM | XRP | DOWN | 48 sec | +0.145% | 0¢ | ❌ Lost | $0.00 |
| 11/20 1:29:11 AM | SOL | DOWN | 48 sec | +0.141% | 0¢ | ❌ Lost | $0.00 |
| 11/20 1:28:55 AM | GBPUSD | DOWN | 64 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/20 1:28:55 AM | AUDUSD | DOWN | 64 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/20 1:28:39 AM | WTI | UP | 80 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 11/20 1:28:39 AM | BRENT | UP | 80 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/20 1:28:23 AM | COPPER | DOWN | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
