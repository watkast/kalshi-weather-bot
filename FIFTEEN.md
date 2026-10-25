# 15-Minute 1¢ Study

*Updated Sun Oct 25, 8:55 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 2659 finished bets | 1% | $90.20 | +30% | +3.39¢ | $36.80 / $53.40 |

*Expect about **97 buys a day** (~$14.59/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 2447 | $65.40 | +24% |
| Volatility model ≥ 2%, hold to the close | 4911 | -$0.10 | -0% |
| Momentum model ≥ 2%, hold to the close | 4088 | -$18.15 | -4% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 31491 | 31479 | 119 (0%) | 1.07% | -$2,160.65 (-56%) | Hold to the close: -$2,160.65 (-56%) |

*In play or awaiting result: 11. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 20272 | 4.6% | 0.4% (84) | -649% | ❌ Worse |
| Momentum model | 20272 | 4.5% | 0.4% (84) | -673% | ❌ Worse |
| Mean-reversion model | 20272 | 7.9% | 0.4% (84) | -786% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 20272 | 84 | -48% | -88% | -87% | -85% |
| Volatility model ≥ 2% | 4911 | 43 | -0% | -78% | -77% | -73% |
| Volatility model ≥ 5% | 2659 | 28 | +30% | -74% | -73% | -69% |
| Volatility model ≥ 10% | 1507 | 18 | +67% | -66% | -64% | -61% |
| Momentum model ≥ 2% | 4088 | 33 | -4% | -80% | -80% | -76% |
| Momentum model ≥ 5% | 2447 | 24 | +24% | -76% | -76% | -71% |
| Momentum model ≥ 10% | 1597 | 16 | +38% | -70% | -69% | -64% |
| Mean-reversion model ≥ 2% | 8167 | 55 | -27% | -83% | -83% | -80% |
| Mean-reversion model ≥ 5% | 5723 | 46 | -12% | -81% | -80% | -78% |
| Mean-reversion model ≥ 10% | 3813 | 33 | -2% | -78% | -78% | -76% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 20472 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 7352 | 2% | 2% | 1% | 1% | 0% | 0% |
| Financials | 3655 | 2% | 1% | 1% | 1% | 0% | 0% |
| **All** | 31479 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 119 | 0% | -$2,160.65 | -56% | — |
| Sell at 2¢ | 1164 | 4% | -$3,356.01 | -88% | 47 sec |
| Sell at 3¢ | 797 | 3% | -$3,347.82 | -87% | 48 sec |
| Sell at 5¢ | 557 | 2% | -$3,296.60 | -86% | 61 sec |
| Sell at 10¢ | 344 | 1% | -$3,166.01 | -83% | 64 sec |
| Sell at 25¢ | 188 | 1% | -$2,924.37 | -76% | 82 sec |
| Sell at 50¢ | 121 | 0% | -$2,645.90 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 1372 | 7 | 11% | 4% | -51% | -81% | -83% |
| 2–5 min | 10077 | 54 | 7% | 3% | -47% | -87% | -87% |
| 1–2 min | 7982 | 30 | 3% | 1% | -59% | -92% | -91% |
| Under 1 min | 12044 | 28 | 1% | 0% | -67% | -86% | -86% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 2294 | 12 | 5% | 2% | -34% | -89% | -89% |
| HYPE | 2288 | 8 | 5% | 3% | -57% | -89% | -87% |
| BNB | 2282 | 12 | 5% | 2% | -35% | -84% | -83% |
| SOL | 2280 | 6 | 3% | 2% | -67% | -92% | -92% |
| ETH | 2276 | 11 | 6% | 3% | -42% | -86% | -86% |
| DOGE | 2269 | 4 | 4% | 2% | -78% | -90% | -90% |
| XRP | 2266 | 9 | 3% | 1% | -51% | -88% | -88% |
| NEAR | 2263 | 12 | 5% | 2% | -31% | -81% | -81% |
| BTC | 2254 | 12 | 5% | 2% | -29% | -88% | -89% |
| GOLD | 1190 | 4 | 4% | 2% | -60% | -81% | -83% |
| SILVER | 1156 | 5 | 4% | 1% | -50% | -82% | -82% |
| WTI | 1143 | 3 | 3% | 1% | -69% | -94% | -95% |
| PLATINUM | 1010 | 0 | 1% | 1% | -100% | -98% | -98% |
| COPPER | 987 | 4 | 1% | 1% | -62% | -69% | -69% |
| EURUSD | 938 | 3 | 2% | 1% | -70% | -86% | -86% |
| NATGAS | 933 | 5 | 2% | 1% | -50% | -86% | -86% |
| PALLADIUM | 897 | 2 | 1% | 0% | -79% | -88% | -88% |
| GBPUSD | 884 | 1 | 2% | 1% | -89% | -96% | -96% |
| USDJPY | 866 | 5 | 1% | 1% | -46% | -98% | -97% |
| AUDUSD | 428 | 0 | 1% | 0% | -100% | -98% | -98% |
| USDCAD | 387 | 0 | 1% | 0% | -100% | -98% | -99% |
| 10YRRATE | 43 | 0 | 0% | 0% | -100% | -100% | -100% |
| 2YRRATE | 40 | 1 | 2% | 0% | +133% | +138% | +133% |
| 30YRRATE | 39 | 0 | 0% | 0% | -100% | -100% | -100% |
| BRENT | 36 | 0 | 0% | 0% | -100% | -100% | -100% |
| 5YRRATE | 30 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 15934 | 65 | 4% | 2% | -53% | -87% | -87% |
| DOWN (bought NO) | 15545 | 54 | 4% | 1% | -60% | -88% | -88% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 3419 | 18 | 2% | 1% | -11% | -80% | -79% |
| 0.05–0.1% | 3524 | 11 | 3% | 2% | -54% | -92% | -92% |
| 0.1–0.2% | 5298 | 19 | 5% | 2% | -56% | -89% | -89% |
| 0.2–0.5% | 5958 | 28 | 6% | 3% | -48% | -87% | -86% |
| Over 0.5% | 2269 | 10 | 7% | 3% | -55% | -87% | -88% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 7904 | 32 | 4% | 2% | -54% | -85% | -85% |
| Morning (6am–12pm) | 7668 | 34 | 4% | 2% | -49% | -88% | -87% |
| Afternoon (12–6pm) | 7332 | 24 | 4% | 2% | -61% | -87% | -88% |
| Evening (6pm–12am) | 8575 | 29 | 3% | 2% | -61% | -90% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,767 |
| Time from buy to best bounce (bounced bets) | 49 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/25 8:55:38 AM | NEAR | DOWN | 4.4 min | +0.581% | — | In play | — |
| 10/25 8:55:38 AM | SOL | DOWN | 4.4 min | +0.296% | — | In play | — |
| 10/25 8:54:17 AM | HYPE | DOWN | 5.7 min | +0.473% | — | In play | — |
| 10/25 8:53:45 AM | BNB | DOWN | 6.2 min | +0.293% | — | In play | — |
| 10/25 8:42:11 AM | NEAR | DOWN | 2.8 min | +0.405% | 0¢ | ❌ Lost | $0.00 |
| 10/25 8:42:11 AM | ZEC | DOWN | 2.8 min | +0.368% | 1¢ | ❌ Lost | -$0.15 |
| 10/25 8:41:57 AM | HYPE | DOWN | 3.0 min | +0.188% | 1¢ | ❌ Lost | -$0.15 |
| 10/25 8:41:57 AM | XRP | DOWN | 3.0 min | +0.194% | 1¢ | ❌ Lost | -$0.15 |
| 10/25 8:41:57 AM | SOL | DOWN | 3.0 min | +0.216% | 1¢ | ❌ Lost | -$0.15 |
| 10/25 8:41:57 AM | BTC | DOWN | 3.0 min | +0.124% | 1¢ | ❌ Lost | -$0.15 |
| 10/25 8:41:41 AM | BNB | DOWN | 3.3 min | +0.110% | 1¢ | ❌ Lost | -$0.15 |
| 10/25 8:41:25 AM | ETH | DOWN | 3.6 min | +0.162% | 0¢ | ❌ Lost | -$0.15 |
| 10/25 8:40:53 AM | DOGE | DOWN | 4.1 min | +0.196% | 1¢ | ❌ Lost | -$0.15 |
| 10/25 8:28:47 AM | HYPE | UP | 72 sec | -0.121% | 1¢ | ❌ Lost | -$0.15 |
| 10/25 8:28:33 AM | BNB | UP | 86 sec | -0.054% | 1¢ | ❌ Lost | -$0.15 |
| 10/25 8:28:33 AM | ZEC | UP | 86 sec | -0.329% | 0¢ | ❌ Lost | $0.00 |
| 10/25 8:27:46 AM | SOL | UP | 2.2 min | -0.169% | 1¢ | ❌ Lost | -$0.15 |
| 10/25 8:27:46 AM | BTC | UP | 2.2 min | -0.079% | 1¢ | ❌ Lost | -$0.15 |
| 10/25 8:27:01 AM | NEAR | UP | 3.0 min | -0.472% | 1¢ | ❌ Lost | -$0.15 |
| 10/25 8:26:42 AM | DOGE | UP | 3.3 min | -0.220% | 1¢ | ❌ Lost | -$0.15 |
| 10/25 8:26:28 AM | ETH | UP | 3.5 min | -0.173% | 1¢ | ❌ Lost | -$0.15 |
| 10/25 8:26:28 AM | XRP | UP | 3.5 min | -0.224% | 1¢ | ❌ Lost | -$0.15 |
| 10/25 8:14:51 AM | BTC | DOWN | 9 sec | +0.046% | 0¢ | ❌ Lost | -$0.15 |
| 10/25 8:14:51 AM | ETH | DOWN | 9 sec | +0.085% | 0¢ | ❌ Lost | $0.00 |
| 10/25 8:14:35 AM | SOL | DOWN | 25 sec | +0.200% | 0¢ | ❌ Lost | $0.00 |
| 10/25 8:14:35 AM | NEAR | DOWN | 25 sec | +0.221% | 0¢ | ❌ Lost | $0.00 |
| 10/25 8:14:35 AM | HYPE | UP | 25 sec | -0.024% | 0¢ | ❌ Lost | $0.00 |
| 10/25 8:14:11 AM | DOGE | UP | 48 sec | -0.137% | 0¢ | ❌ Lost | $0.00 |
| 10/25 8:13:40 AM | BNB | DOWN | 79 sec | +0.080% | 1¢ | ❌ Lost | -$0.15 |
| 10/25 8:13:24 AM | XRP | UP | 1.6 min | -0.147% | 2¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
