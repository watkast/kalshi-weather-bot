# 15-Minute 1¢ Study

*Updated Wed Nov 25, 8:40 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 4873 finished bets | 1% | $211.15 | +40% | +4.33¢ | $88.60 / $122.55 |

*Expect about **83 buys a day** (~$12.52/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 4622 | $109.55 | +22% |
| Volatility model ≥ 2%, hold to the close | 9080 | $38.35 | +4% |
| Momentum model ≥ 2%, hold to the close | 7558 | -$32.15 | -4% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 67386 | 67346 | 255 (0%) | 1.07% | -$4,582.65 (-56%) | Hold to the close: -$4,582.65 (-56%) |

*In play or awaiting result: 12. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 39985 | 4.5% | 0.4% (164) | -649% | ❌ Worse |
| Momentum model | 39985 | 4.4% | 0.4% (164) | -671% | ❌ Worse |
| Mean-reversion model | 39985 | 7.9% | 0.4% (164) | -788% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 39985 | 164 | -47% | -87% | -86% | -84% |
| Volatility model ≥ 2% | 9080 | 80 | +4% | -77% | -76% | -73% |
| Volatility model ≥ 5% | 4873 | 53 | +40% | -73% | -71% | -68% |
| Volatility model ≥ 10% | 2825 | 32 | +68% | -64% | -63% | -59% |
| Momentum model ≥ 2% | 7558 | 59 | -4% | -79% | -79% | -75% |
| Momentum model ≥ 5% | 4622 | 43 | +22% | -75% | -75% | -71% |
| Momentum model ≥ 10% | 3016 | 28 | +34% | -68% | -67% | -63% |
| Mean-reversion model ≥ 2% | 16259 | 112 | -24% | -82% | -82% | -80% |
| Mean-reversion model ≥ 5% | 11315 | 92 | -9% | -80% | -79% | -77% |
| Mean-reversion model ≥ 10% | 7518 | 66 | +0% | -78% | -77% | -75% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 40191 | 5% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 16017 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 11138 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 67346 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 255 | 0% | -$4,582.65 | -56% | — |
| Sell at 2¢ | 2754 | 4% | -$7,142.61 | -88% | 47 sec |
| Sell at 3¢ | 1852 | 3% | -$7,136.37 | -88% | 48 sec |
| Sell at 5¢ | 1255 | 2% | -$7,014.90 | -86% | 62 sec |
| Sell at 10¢ | 768 | 1% | -$6,740.57 | -83% | 65 sec |
| Sell at 25¢ | 414 | 1% | -$6,222.31 | -76% | 80 sec |
| Sell at 50¢ | 265 | 0% | -$5,621.90 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 13 | 0 | 31% | 23% | -100% | -47% | -20% |
| 5–10 min | 3468 | 17 | 11% | 4% | -54% | -81% | -83% |
| 2–5 min | 21834 | 116 | 7% | 3% | -48% | -86% | -86% |
| 1–2 min | 16818 | 57 | 3% | 2% | -62% | -92% | -92% |
| Under 1 min | 25213 | 65 | 1% | 0% | -63% | -87% | -86% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 4494 | 19 | 5% | 2% | -43% | -88% | -87% |
| HYPE | 4488 | 16 | 5% | 2% | -54% | -89% | -88% |
| SOL | 4482 | 20 | 4% | 2% | -42% | -86% | -86% |
| BNB | 4475 | 22 | 5% | 2% | -37% | -86% | -85% |
| DOGE | 4472 | 12 | 4% | 2% | -65% | -89% | -89% |
| ETH | 4466 | 19 | 7% | 3% | -46% | -82% | -82% |
| BTC | 4445 | 24 | 5% | 2% | -26% | -86% | -88% |
| NEAR | 4440 | 18 | 5% | 2% | -47% | -85% | -86% |
| XRP | 4429 | 16 | 4% | 2% | -54% | -89% | -88% |
| GOLD | 2371 | 8 | 5% | 2% | -59% | -83% | -84% |
| WTI | 2357 | 8 | 4% | 2% | -59% | -91% | -92% |
| SILVER | 2311 | 9 | 5% | 2% | -53% | -83% | -84% |
| PLATINUM | 2100 | 5 | 3% | 1% | -78% | -95% | -95% |
| EURUSD | 2054 | 7 | 3% | 1% | -68% | -91% | -90% |
| COPPER | 1992 | 6 | 2% | 1% | -72% | -78% | -78% |
| GBPUSD | 1992 | 8 | 2% | 1% | -63% | -96% | -96% |
| USDJPY | 1955 | 6 | 2% | 1% | -71% | -96% | -96% |
| NATGAS | 1947 | 10 | 2% | 1% | -52% | -77% | -77% |
| PALLADIUM | 1885 | 4 | 1% | 1% | -80% | -93% | -93% |
| AUDUSD | 1512 | 7 | 2% | 1% | -57% | -90% | -90% |
| USDCAD | 1425 | 1 | 3% | 1% | -93% | -96% | -96% |
| BRENT | 1054 | 1 | 2% | 1% | -91% | -96% | -97% |
| 10YRRATE | 544 | 2 | 3% | 1% | -66% | -77% | -76% |
| 2YRRATE | 505 | 4 | 4% | 2% | -26% | -57% | -56% |
| 30YRRATE | 504 | 0 | 3% | 1% | -100% | -96% | -93% |
| 5YRRATE | 494 | 2 | 4% | 2% | -62% | -94% | -95% |
| INX | 127 | 1 | 2% | 1% | -27% | -97% | -98% |
| USDMXN | 26 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 34483 | 131 | 4% | 2% | -56% | -88% | -88% |
| DOWN (bought NO) | 32863 | 124 | 4% | 2% | -56% | -87% | -87% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 5842 | 25 | 2% | 1% | -21% | -79% | -78% |
| 0.05–0.1% | 6387 | 26 | 3% | 2% | -35% | -91% | -91% |
| 0.1–0.2% | 9990 | 36 | 5% | 2% | -52% | -89% | -89% |
| 0.2–0.5% | 12675 | 56 | 7% | 3% | -50% | -86% | -86% |
| Over 0.5% | 5288 | 23 | 7% | 3% | -54% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 16330 | 50 | 4% | 2% | -65% | -88% | -88% |
| Morning (6am–12pm) | 15817 | 81 | 4% | 2% | -41% | -86% | -85% |
| Afternoon (12–6pm) | 16634 | 73 | 4% | 2% | -48% | -87% | -87% |
| Evening (6pm–12am) | 18565 | 51 | 4% | 2% | -68% | -89% | -89% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 5,111 |
| Time from buy to best bounce (bounced bets) | 51 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/25 8:40:24 AM | AUDUSD | DOWN | 4.6 min | — | — | In play | — |
| 11/25 8:38:27 AM | BNB | DOWN | 6.5 min | +1.155% | — | In play | — |
| 11/25 8:38:11 AM | BTC | DOWN | 6.8 min | +1.171% | — | In play | — |
| 11/25 8:37:55 AM | DOGE | DOWN | 7.1 min | +1.126% | — | In play | — |
| 11/25 8:37:37 AM | ETH | DOWN | 7.4 min | +1.391% | — | In play | — |
| 11/25 8:37:21 AM | HYPE | DOWN | 7.7 min | +1.833% | — | In play | — |
| 11/25 8:29:51 AM | USDCAD | UP | 8 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/25 8:29:35 AM | BTC | UP | 25 sec | -0.102% | 0¢ | ❌ Lost | $0.00 |
| 11/25 8:29:35 AM | GBPUSD | UP | 25 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/25 8:29:35 AM | SOL | UP | 25 sec | -0.131% | 0¢ | ❌ Lost | $0.00 |
| 11/25 8:29:35 AM | 30YRRATE | UP | 25 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/25 8:29:35 AM | USDMXN | DOWN | 25 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/25 8:29:16 AM | DOGE | UP | 43 sec | -0.196% | 0¢ | ❌ Lost | $0.00 |
| 11/25 8:29:16 AM | BNB | UP | 43 sec | -0.206% | 0¢ | ❌ Lost | $0.00 |
| 11/25 8:29:16 AM | ETH | UP | 43 sec | -0.330% | 0¢ | ❌ Lost | $0.00 |
| 11/25 8:29:00 AM | XRP | UP | 59 sec | -0.290% | 0¢ | ❌ Lost | -$0.15 |
| 11/25 8:29:00 AM | ZEC | UP | 59 sec | -0.592% | 0¢ | ❌ Lost | $0.00 |
| 11/25 8:28:44 AM | AUDUSD | UP | 75 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/25 8:28:44 AM | COPPER | UP | 75 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/25 8:28:28 AM | NATGAS | DOWN | 1.5 min | — | 2¢ | ❌ Lost | -$0.15 |
| 11/25 8:27:54 AM | HYPE | UP | 2.1 min | -0.688% | 0¢ | ❌ Lost | -$0.15 |
| 11/25 8:27:54 AM | 10YRRATE | UP | 2.1 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/25 8:27:54 AM | 2YRRATE | UP | 2.1 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/25 8:27:38 AM | NEAR | UP | 2.4 min | -1.109% | 0¢ | ❌ Lost | $0.00 |
| 11/25 8:27:22 AM | 5YRRATE | UP | 2.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/25 8:27:03 AM | BRENT | UP | 2.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/25 8:26:15 AM | WTI | UP | 3.7 min | — | 2¢ | ❌ Lost | -$0.15 |
| 11/25 8:25:57 AM | INX | UP | 4.0 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/25 8:25:25 AM | SILVER | UP | 4.6 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/25 8:25:25 AM | GOLD | UP | 4.6 min | — | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
