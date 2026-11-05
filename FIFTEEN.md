# 15-Minute 1¢ Study

*Updated Thu Nov 5, 3:30 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 3721 finished bets | 1% | $132.60 | +32% | +3.56¢ | $87.30 / $45.30 |

*Expect about **96 buys a day** (~$14.44/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 3460 | $59.90 | +16% |
| Volatility model ≥ 2%, hold to the close | 6887 | $38.20 | +5% |
| Momentum model ≥ 2%, hold to the close | 5685 | -$37.70 | -6% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 47025 | 47008 | 173 (0%) | 1.07% | -$3,311.00 (-58%) | Hold to the close: -$3,311.00 (-58%) |

*In play or awaiting result: 15. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 28488 | 4.7% | 0.4% (111) | -685% | ❌ Worse |
| Momentum model | 28488 | 4.6% | 0.4% (111) | -712% | ❌ Worse |
| Mean-reversion model | 28488 | 8.1% | 0.4% (111) | -833% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 28488 | 111 | -50% | -88% | -87% | -85% |
| Volatility model ≥ 2% | 6887 | 62 | +5% | -79% | -78% | -74% |
| Volatility model ≥ 5% | 3721 | 39 | +32% | -77% | -75% | -71% |
| Volatility model ≥ 10% | 2127 | 24 | +62% | -71% | -70% | -66% |
| Momentum model ≥ 2% | 5685 | 44 | -6% | -82% | -81% | -78% |
| Momentum model ≥ 5% | 3460 | 31 | +16% | -79% | -79% | -75% |
| Momentum model ≥ 10% | 2262 | 20 | +24% | -75% | -74% | -70% |
| Mean-reversion model ≥ 2% | 11781 | 80 | -25% | -83% | -83% | -81% |
| Mean-reversion model ≥ 5% | 8263 | 69 | -7% | -82% | -81% | -78% |
| Mean-reversion model ≥ 10% | 5534 | 49 | +1% | -80% | -79% | -77% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 28693 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 11267 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 7048 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 47008 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 173 | 0% | -$3,311.00 | -58% | — |
| Sell at 2¢ | 1841 | 4% | -$5,002.34 | -87% | 47 sec |
| Sell at 3¢ | 1255 | 3% | -$4,991.55 | -87% | 49 sec |
| Sell at 5¢ | 866 | 2% | -$4,890.10 | -85% | 63 sec |
| Sell at 10¢ | 525 | 1% | -$4,681.25 | -82% | 65 sec |
| Sell at 25¢ | 273 | 1% | -$4,353.37 | -76% | 83 sec |
| Sell at 50¢ | 176 | 0% | -$3,971.00 | -69% | 1.8 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 12 | 0 | 25% | 17% | -100% | -57% | -35% |
| 5–10 min | 2323 | 10 | 10% | 4% | -59% | -82% | -83% |
| 2–5 min | 15142 | 81 | 7% | 3% | -47% | -87% | -86% |
| 1–2 min | 11820 | 40 | 3% | 2% | -63% | -92% | -92% |
| Under 1 min | 17711 | 42 | 1% | 0% | -66% | -85% | -85% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 3214 | 13 | 5% | 2% | -48% | -88% | -88% |
| SOL | 3208 | 12 | 4% | 2% | -53% | -90% | -90% |
| BNB | 3203 | 17 | 5% | 2% | -33% | -85% | -84% |
| HYPE | 3202 | 10 | 5% | 2% | -61% | -89% | -87% |
| DOGE | 3188 | 6 | 4% | 2% | -76% | -90% | -90% |
| ETH | 3186 | 12 | 7% | 3% | -54% | -85% | -85% |
| NEAR | 3168 | 16 | 5% | 2% | -34% | -84% | -84% |
| BTC | 3167 | 15 | 5% | 2% | -35% | -88% | -89% |
| XRP | 3157 | 12 | 3% | 1% | -53% | -89% | -89% |
| GOLD | 1737 | 5 | 5% | 2% | -65% | -81% | -83% |
| WTI | 1688 | 5 | 4% | 1% | -64% | -92% | -92% |
| SILVER | 1683 | 8 | 5% | 2% | -44% | -82% | -81% |
| PLATINUM | 1517 | 4 | 2% | 1% | -75% | -96% | -96% |
| EURUSD | 1456 | 3 | 2% | 1% | -81% | -89% | -89% |
| COPPER | 1433 | 6 | 2% | 1% | -61% | -71% | -71% |
| GBPUSD | 1385 | 4 | 2% | 1% | -73% | -96% | -96% |
| NATGAS | 1373 | 8 | 2% | 1% | -46% | -76% | -75% |
| PALLADIUM | 1364 | 3 | 1% | 1% | -79% | -91% | -91% |
| USDJPY | 1362 | 5 | 2% | 1% | -66% | -97% | -97% |
| AUDUSD | 910 | 4 | 2% | 1% | -59% | -87% | -87% |
| USDCAD | 888 | 0 | 2% | 1% | -100% | -97% | -98% |
| BRENT | 472 | 0 | 1% | 1% | -100% | -97% | -97% |
| 10YRRATE | 280 | 1 | 4% | 1% | -67% | -59% | -57% |
| 30YRRATE | 265 | 0 | 2% | 1% | -100% | -97% | -95% |
| 2YRRATE | 261 | 3 | 4% | 1% | +7% | -22% | -21% |
| 5YRRATE | 240 | 1 | 5% | 2% | -61% | -92% | -95% |
| INX | 1 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 23854 | 92 | 4% | 2% | -56% | -88% | -87% |
| DOWN (bought NO) | 23154 | 81 | 4% | 2% | -60% | -87% | -87% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 4597 | 22 | 2% | 1% | -16% | -83% | -82% |
| 0.05–0.1% | 4871 | 18 | 3% | 2% | -44% | -91% | -90% |
| 0.1–0.2% | 7389 | 26 | 5% | 2% | -56% | -89% | -89% |
| 0.2–0.5% | 8571 | 34 | 6% | 3% | -56% | -87% | -86% |
| Over 0.5% | 3257 | 13 | 7% | 3% | -59% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 11506 | 40 | 4% | 2% | -60% | -87% | -87% |
| Morning (6am–12pm) | 11661 | 51 | 4% | 2% | -50% | -86% | -85% |
| Afternoon (12–6pm) | 11215 | 41 | 4% | 2% | -57% | -86% | -86% |
| Evening (6pm–12am) | 12626 | 41 | 3% | 2% | -63% | -90% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,647 |
| Time from buy to best bounce (bounced bets) | 51 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/5 3:29:48 PM | NATGAS | UP | 11 sec | — | 0¢ | In play | — |
| 11/5 3:29:48 PM | GBPUSD | UP | 11 sec | — | 0¢ | In play | — |
| 11/5 3:29:16 PM | ZEC | DOWN | 43 sec | +0.424% | 0¢ | ❌ Lost | $0.00 |
| 11/5 3:29:16 PM | WTI | UP | 43 sec | — | 1¢ | In play | — |
| 11/5 3:28:29 PM | NEAR | UP | 1.5 min | -0.494% | 1¢ | In play | — |
| 11/5 3:27:42 PM | BNB | UP | 2.3 min | -0.235% | 0¢ | In play | — |
| 11/5 3:27:26 PM | XRP | UP | 2.6 min | -0.351% | 0¢ | In play | — |
| 11/5 3:27:26 PM | ETH | UP | 2.6 min | -0.311% | 1¢ | ❌ Lost | -$0.15 |
| 11/5 3:27:10 PM | BTC | UP | 2.8 min | -0.203% | 1¢ | ❌ Lost | -$0.15 |
| 11/5 3:26:53 PM | SOL | UP | 3.1 min | -0.324% | 1¢ | ❌ Lost | -$0.15 |
| 11/5 3:25:35 PM | DOGE | UP | 4.4 min | -0.483% | 1¢ | ❌ Lost | -$0.15 |
| 11/5 3:14:35 PM | HYPE | UP | 24 sec | -0.145% | 0¢ | ❌ Lost | $0.00 |
| 11/5 3:14:35 PM | NATGAS | DOWN | 24 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/5 3:14:19 PM | ZEC | DOWN | 40 sec | +0.353% | 0¢ | ❌ Lost | $0.00 |
| 11/5 3:13:47 PM | SOL | DOWN | 72 sec | +0.141% | 0¢ | ❌ Lost | -$0.15 |
| 11/5 3:13:47 PM | AUDUSD | DOWN | 72 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/5 3:13:32 PM | NEAR | DOWN | 87 sec | +0.246% | 1¢ | ❌ Lost | -$0.15 |
| 11/5 3:12:44 PM | BNB | DOWN | 2.2 min | +0.145% | 1¢ | ❌ Lost | -$0.15 |
| 11/5 3:12:44 PM | XRP | DOWN | 2.2 min | +0.279% | 1¢ | ❌ Lost | -$0.15 |
| 11/5 3:12:44 PM | ETH | DOWN | 2.2 min | +0.335% | 1¢ | ❌ Lost | -$0.15 |
| 11/5 3:12:29 PM | BTC | DOWN | 2.5 min | +0.259% | 1¢ | ❌ Lost | -$0.15 |
| 11/5 2:59:43 PM | 10YRRATE | UP | 17 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/5 2:59:11 PM | BTC | UP | 48 sec | -0.107% | 0¢ | ❌ Lost | -$0.15 |
| 11/5 2:59:11 PM | ETH | UP | 48 sec | -0.154% | 0¢ | ❌ Lost | $0.00 |
| 11/5 2:58:55 PM | GBPUSD | DOWN | 65 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/5 2:58:55 PM | 2YRRATE | UP | 65 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/5 2:58:55 PM | USDJPY | DOWN | 65 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/5 2:58:55 PM | AUDUSD | DOWN | 65 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/5 2:58:40 PM | SOL | UP | 80 sec | -0.107% | 3¢ | ❌ Lost | -$0.15 |
| 11/5 2:58:40 PM | 5YRRATE | UP | 80 sec | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
