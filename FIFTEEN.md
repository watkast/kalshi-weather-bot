# 15-Minute 1¢ Study

*Updated Fri Nov 20, 6:42 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

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
| Momentum model ≥ 2%, hold to the close | 7123 | -$17.10 | -2% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 62953 | 62911 | 243 (0%) | 1.07% | -$4,247.70 (-56%) | Hold to the close: -$4,247.70 (-56%) |

*In play or awaiting result: 14. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 37284 | 4.5% | 0.4% (156) | -636% | ❌ Worse |
| Momentum model | 37284 | 4.4% | 0.4% (156) | -661% | ❌ Worse |
| Mean-reversion model | 37284 | 7.9% | 0.4% (156) | -771% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 37284 | 156 | -46% | -87% | -87% | -84% |
| Volatility model ≥ 2% | 8582 | 78 | +6% | -77% | -76% | -72% |
| Volatility model ≥ 5% | 4595 | 51 | +41% | -72% | -71% | -68% |
| Volatility model ≥ 10% | 2644 | 30 | +66% | -63% | -62% | -59% |
| Momentum model ≥ 2% | 7123 | 57 | -2% | -79% | -78% | -75% |
| Momentum model ≥ 5% | 4337 | 41 | +23% | -75% | -74% | -70% |
| Momentum model ≥ 10% | 2830 | 26 | +31% | -67% | -67% | -62% |
| Mean-reversion model ≥ 2% | 15223 | 109 | -21% | -82% | -82% | -79% |
| Mean-reversion model ≥ 5% | 10589 | 89 | -7% | -80% | -79% | -77% |
| Mean-reversion model ≥ 10% | 7036 | 64 | +4% | -77% | -77% | -74% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 37490 | 5% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 15116 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 10305 | 3% | 2% | 1% | 1% | 0% | 0% |
| **All** | 62911 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 243 | 0% | -$4,247.70 | -56% | — |
| Sell at 2¢ | 2555 | 4% | -$6,691.40 | -87% | 47 sec |
| Sell at 3¢ | 1722 | 3% | -$6,684.12 | -87% | 48 sec |
| Sell at 5¢ | 1175 | 2% | -$6,563.95 | -86% | 63 sec |
| Sell at 10¢ | 719 | 1% | -$6,301.81 | -82% | 65 sec |
| Sell at 25¢ | 385 | 1% | -$5,815.35 | -76% | 80 sec |
| Sell at 50¢ | 249 | 0% | -$5,254.95 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 13 | 0 | 31% | 23% | -100% | -47% | -20% |
| 5–10 min | 3228 | 17 | 11% | 4% | -50% | -81% | -82% |
| 2–5 min | 20382 | 109 | 7% | 3% | -47% | -86% | -86% |
| 1–2 min | 15736 | 54 | 3% | 2% | -62% | -92% | -92% |
| Under 1 min | 23552 | 63 | 1% | 0% | -62% | -86% | -86% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 4191 | 19 | 5% | 2% | -40% | -88% | -87% |
| SOL | 4189 | 19 | 4% | 2% | -42% | -86% | -86% |
| HYPE | 4181 | 13 | 4% | 2% | -60% | -89% | -88% |
| DOGE | 4172 | 11 | 4% | 2% | -66% | -90% | -89% |
| BNB | 4170 | 21 | 5% | 2% | -36% | -85% | -85% |
| ETH | 4166 | 19 | 7% | 3% | -43% | -82% | -82% |
| BTC | 4148 | 22 | 5% | 2% | -28% | -86% | -88% |
| NEAR | 4144 | 18 | 5% | 2% | -43% | -85% | -86% |
| XRP | 4129 | 16 | 3% | 2% | -51% | -89% | -88% |
| GOLD | 2247 | 7 | 5% | 2% | -62% | -82% | -84% |
| WTI | 2228 | 7 | 4% | 1% | -62% | -91% | -92% |
| SILVER | 2191 | 9 | 5% | 2% | -51% | -83% | -83% |
| PLATINUM | 1994 | 5 | 3% | 1% | -77% | -95% | -95% |
| EURUSD | 1950 | 7 | 3% | 1% | -66% | -91% | -90% |
| GBPUSD | 1885 | 8 | 2% | 1% | -60% | -96% | -95% |
| COPPER | 1878 | 6 | 2% | 1% | -70% | -77% | -77% |
| USDJPY | 1837 | 6 | 2% | 1% | -70% | -96% | -96% |
| NATGAS | 1835 | 10 | 2% | 1% | -49% | -76% | -76% |
| PALLADIUM | 1795 | 4 | 1% | 1% | -79% | -92% | -93% |
| AUDUSD | 1387 | 6 | 2% | 1% | -60% | -90% | -90% |
| USDCAD | 1326 | 1 | 3% | 1% | -93% | -95% | -96% |
| BRENT | 948 | 0 | 2% | 1% | -100% | -97% | -98% |
| 10YRRATE | 484 | 2 | 3% | 1% | -61% | -75% | -73% |
| 2YRRATE | 460 | 4 | 4% | 2% | -19% | -53% | -52% |
| 30YRRATE | 445 | 0 | 2% | 1% | -100% | -96% | -94% |
| 5YRRATE | 434 | 2 | 4% | 2% | -57% | -94% | -95% |
| INX | 97 | 1 | 2% | 1% | -4% | -96% | -97% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 32125 | 125 | 4% | 2% | -55% | -88% | -88% |
| DOWN (bought NO) | 30786 | 118 | 4% | 2% | -56% | -87% | -87% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 5572 | 25 | 2% | 1% | -19% | -78% | -78% |
| 0.05–0.1% | 6072 | 24 | 3% | 2% | -38% | -91% | -91% |
| 0.1–0.2% | 9382 | 34 | 5% | 2% | -53% | -89% | -89% |
| 0.2–0.5% | 11678 | 52 | 7% | 3% | -50% | -86% | -86% |
| Over 0.5% | 4777 | 23 | 7% | 3% | -50% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 15327 | 48 | 4% | 2% | -64% | -88% | -88% |
| Morning (6am–12pm) | 14844 | 79 | 5% | 2% | -39% | -85% | -84% |
| Afternoon (12–6pm) | 15444 | 66 | 4% | 2% | -50% | -87% | -87% |
| Evening (6pm–12am) | 17296 | 50 | 4% | 2% | -67% | -89% | -89% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,992 |
| Time from buy to best bounce (bounced bets) | 50 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/20 6:42:46 AM | 5YRRATE | UP | 2.2 min | — | — | In play | — |
| 11/20 6:42:30 AM | PALLADIUM | UP | 2.5 min | — | — | In play | — |
| 11/20 6:42:30 AM | COPPER | DOWN | 2.5 min | — | — | In play | — |
| 11/20 6:42:30 AM | DOGE | UP | 2.5 min | -0.552% | — | In play | — |
| 11/20 6:42:30 AM | XRP | UP | 2.5 min | -0.533% | — | In play | — |
| 11/20 6:41:58 AM | NEAR | UP | 3.0 min | -0.597% | — | In play | — |
| 11/20 6:41:58 AM | SILVER | DOWN | 3.0 min | — | — | In play | — |
| 11/20 6:37:59 AM | 2YRRATE | UP | 7.0 min | — | — | In play | — |
| 11/20 6:29:38 AM | SOL | UP | 21 sec | -0.179% | 1¢ | ❌ Lost | -$0.15 |
| 11/20 6:29:22 AM | 5YRRATE | DOWN | 37 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/20 6:29:06 AM | 10YRRATE | DOWN | 54 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/20 6:29:06 AM | 30YRRATE | DOWN | 54 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/20 6:29:06 AM | BRENT | DOWN | 54 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/20 6:29:06 AM | 2YRRATE | DOWN | 54 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/20 6:29:06 AM | ZEC | UP | 54 sec | -0.177% | 0¢ | ❌ Lost | $0.00 |
| 11/20 6:28:32 AM | NEAR | UP | 88 sec | -0.301% | 1¢ | ❌ Lost | -$0.15 |
| 11/20 6:28:32 AM | BNB | UP | 88 sec | -0.249% | 0¢ | ❌ Lost | -$0.15 |
| 11/20 6:28:16 AM | NATGAS | DOWN | 1.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/20 6:27:45 AM | DOGE | UP | 2.2 min | -0.353% | 1¢ | ❌ Lost | -$0.15 |
| 11/20 6:26:57 AM | EURUSD | DOWN | 3.0 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/20 6:26:41 AM | COPPER | UP | 3.3 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/20 6:26:25 AM | WTI | DOWN | 3.6 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/20 6:26:09 AM | XRP | UP | 3.9 min | -0.668% | 1¢ | ❌ Lost | -$0.15 |
| 11/20 6:25:52 AM | SILVER | UP | 4.1 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/20 6:25:52 AM | GOLD | UP | 4.1 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/20 6:25:04 AM | HYPE | UP | 4.9 min | -0.795% | 1¢ | ❌ Lost | -$0.15 |
| 11/20 6:14:55 AM | AUDUSD | UP | 4 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/20 6:14:39 AM | COPPER | UP | 20 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/20 6:14:39 AM | PLATINUM | UP | 20 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/20 6:14:23 AM | NEAR | DOWN | 36 sec | +0.088% | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
