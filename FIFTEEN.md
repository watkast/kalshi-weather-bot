# 15-Minute 1¢ Study

*Updated Sun Oct 25, 7:22 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 2659 finished bets | 1% | $90.20 | +30% | +3.39¢ | $36.80 / $53.40 |

*Expect about **97 buys a day** (~$14.62/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 2445 | $65.70 | +24% |
| Volatility model ≥ 2%, hold to the close | 4903 | $1.10 | +0% |
| Momentum model ≥ 2%, hold to the close | 4084 | -$17.55 | -4% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 31433 | 31425 | 119 (0%) | 1.07% | -$2,154.80 (-56%) | Hold to the close: -$2,154.80 (-56%) |

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
| Volatility model | 20218 | 4.7% | 0.4% (84) | -650% | ❌ Worse |
| Momentum model | 20218 | 4.5% | 0.4% (84) | -674% | ❌ Worse |
| Mean-reversion model | 20218 | 7.9% | 0.4% (84) | -787% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 20218 | 84 | -48% | -87% | -87% | -85% |
| Volatility model ≥ 2% | 4903 | 43 | +0% | -78% | -77% | -73% |
| Volatility model ≥ 5% | 2659 | 28 | +30% | -74% | -73% | -69% |
| Volatility model ≥ 10% | 1507 | 18 | +67% | -66% | -64% | -61% |
| Momentum model ≥ 2% | 4084 | 33 | -4% | -80% | -80% | -76% |
| Momentum model ≥ 5% | 2445 | 24 | +24% | -76% | -76% | -71% |
| Momentum model ≥ 10% | 1597 | 16 | +38% | -70% | -69% | -64% |
| Mean-reversion model ≥ 2% | 8147 | 55 | -26% | -83% | -82% | -80% |
| Mean-reversion model ≥ 5% | 5711 | 46 | -11% | -81% | -80% | -77% |
| Mean-reversion model ≥ 10% | 3808 | 33 | -2% | -78% | -78% | -76% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 20418 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 7352 | 2% | 2% | 1% | 1% | 0% | 0% |
| Financials | 3655 | 2% | 1% | 1% | 1% | 0% | 0% |
| **All** | 31425 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 119 | 0% | -$2,154.80 | -56% | — |
| Sell at 2¢ | 1163 | 4% | -$3,350.42 | -88% | 47 sec |
| Sell at 3¢ | 797 | 3% | -$3,341.97 | -87% | 48 sec |
| Sell at 5¢ | 557 | 2% | -$3,290.75 | -86% | 61 sec |
| Sell at 10¢ | 344 | 1% | -$3,160.16 | -83% | 64 sec |
| Sell at 25¢ | 188 | 1% | -$2,918.52 | -76% | 82 sec |
| Sell at 50¢ | 121 | 0% | -$2,640.05 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 1371 | 7 | 11% | 4% | -51% | -81% | -83% |
| 2–5 min | 10047 | 54 | 7% | 3% | -47% | -87% | -87% |
| 1–2 min | 7972 | 30 | 3% | 1% | -59% | -92% | -91% |
| Under 1 min | 12031 | 28 | 1% | 0% | -67% | -86% | -86% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 2288 | 12 | 5% | 2% | -34% | -89% | -89% |
| HYPE | 2282 | 8 | 5% | 3% | -57% | -88% | -87% |
| BNB | 2276 | 12 | 5% | 2% | -35% | -84% | -83% |
| SOL | 2274 | 6 | 3% | 2% | -67% | -92% | -92% |
| ETH | 2270 | 11 | 6% | 3% | -42% | -86% | -86% |
| DOGE | 2263 | 4 | 4% | 2% | -78% | -90% | -90% |
| XRP | 2260 | 9 | 3% | 1% | -51% | -88% | -88% |
| NEAR | 2257 | 12 | 5% | 2% | -31% | -81% | -81% |
| BTC | 2248 | 12 | 5% | 2% | -29% | -88% | -89% |
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
| UP (bought YES) | 15904 | 65 | 4% | 2% | -53% | -87% | -87% |
| DOWN (bought NO) | 15521 | 54 | 4% | 2% | -60% | -88% | -88% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 3414 | 18 | 2% | 1% | -11% | -80% | -79% |
| 0.05–0.1% | 3519 | 11 | 3% | 2% | -54% | -92% | -92% |
| 0.1–0.2% | 5276 | 19 | 5% | 2% | -55% | -89% | -89% |
| 0.2–0.5% | 5939 | 28 | 6% | 3% | -48% | -87% | -86% |
| Over 0.5% | 2266 | 10 | 7% | 3% | -54% | -87% | -88% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 7904 | 32 | 4% | 2% | -54% | -85% | -85% |
| Morning (6am–12pm) | 7614 | 34 | 4% | 2% | -49% | -88% | -87% |
| Afternoon (12–6pm) | 7332 | 24 | 4% | 2% | -61% | -87% | -88% |
| Evening (6pm–12am) | 8575 | 29 | 3% | 2% | -61% | -90% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,760 |
| Time from buy to best bounce (bounced bets) | 49 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/25 7:14:42 AM | SOL | DOWN | 17 sec | -0.016% | 0¢ | ❌ Lost | $0.00 |
| 10/25 7:14:42 AM | ZEC | DOWN | 17 sec | -0.057% | 0¢ | ❌ Lost | -$0.15 |
| 10/25 7:14:42 AM | NEAR | DOWN | 17 sec | -0.036% | 0¢ | ❌ Lost | -$0.15 |
| 10/25 7:14:28 AM | BTC | UP | 31 sec | -0.033% | 0¢ | ❌ Lost | $0.00 |
| 10/25 7:14:28 AM | XRP | DOWN | 31 sec | +0.015% | 1¢ | ❌ Lost | -$0.15 |
| 10/25 7:14:14 AM | ETH | DOWN | 45 sec | +0.032% | 1¢ | ❌ Lost | -$0.15 |
| 10/25 7:14:14 AM | DOGE | DOWN | 45 sec | +0.012% | 0¢ | ❌ Lost | $0.00 |
| 10/25 7:13:27 AM | HYPE | DOWN | 1.5 min | +0.112% | 1¢ | ❌ Lost | -$0.15 |
| 10/25 7:13:13 AM | BNB | UP | 1.8 min | -0.118% | 1¢ | ❌ Lost | -$0.15 |
| 10/25 6:59:25 AM | NEAR | DOWN | 35 sec | +0.139% | 0¢ | ❌ Lost | $0.00 |
| 10/25 6:59:25 AM | BNB | UP | 35 sec | -0.079% | 0¢ | ❌ Lost | -$0.15 |
| 10/25 6:59:25 AM | HYPE | DOWN | 35 sec | +0.106% | 0¢ | ❌ Lost | $0.00 |
| 10/25 6:58:53 AM | BTC | DOWN | 67 sec | +0.043% | 0¢ | ❌ Lost | $0.00 |
| 10/25 6:58:23 AM | XRP | DOWN | 1.6 min | +0.077% | 1¢ | ❌ Lost | -$0.15 |
| 10/25 6:56:50 AM | ETH | DOWN | 3.1 min | +0.128% | 0¢ | ❌ Lost | $0.00 |
| 10/25 6:56:35 AM | SOL | DOWN | 3.4 min | +0.151% | 1¢ | ❌ Lost | -$0.15 |
| 10/25 6:56:35 AM | DOGE | DOWN | 3.4 min | +0.161% | 1¢ | ❌ Lost | -$0.15 |
| 10/25 6:55:49 AM | ZEC | DOWN | 4.2 min | +0.362% | 1¢ | ❌ Lost | -$0.15 |
| 10/25 6:44:40 AM | NEAR | DOWN | 19 sec | -0.115% | 1¢ | ❌ Lost | -$0.15 |
| 10/25 6:44:10 AM | XRP | DOWN | 49 sec | +0.070% | 0¢ | ❌ Lost | -$0.15 |
| 10/25 6:42:08 AM | DOGE | DOWN | 2.9 min | +0.156% | 1¢ | ❌ Lost | -$0.15 |
| 10/25 6:41:21 AM | ETH | DOWN | 3.6 min | +0.133% | 1¢ | ❌ Lost | -$0.15 |
| 10/25 6:40:51 AM | BTC | DOWN | 4.1 min | +0.098% | 1¢ | ❌ Lost | -$0.15 |
| 10/25 6:40:20 AM | SOL | DOWN | 4.7 min | +0.237% | 1¢ | ❌ Lost | -$0.15 |
| 10/25 6:40:20 AM | HYPE | DOWN | 4.7 min | +0.268% | 1¢ | ❌ Lost | -$0.15 |
| 10/25 6:39:18 AM | ZEC | DOWN | 5.7 min | +0.658% | 1¢ | ❌ Lost | -$0.15 |
| 10/25 6:29:20 AM | HYPE | UP | 40 sec | -0.163% | 0¢ | ❌ Lost | $0.00 |
| 10/25 6:29:06 AM | XRP | UP | 54 sec | -0.116% | 1¢ | ❌ Lost | -$0.15 |
| 10/25 6:29:06 AM | DOGE | UP | 54 sec | -0.108% | 0¢ | ❌ Lost | -$0.15 |
| 10/25 6:27:49 AM | SOL | UP | 2.2 min | -0.175% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
