# 15-Minute 1¢ Study

*Updated Tue Nov 10, 9:46 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 4165 finished bets | 1% | $181.10 | +39% | +4.35¢ | $88.75 / $92.35 |

*Expect about **96 buys a day** (~$14.39/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 3885 | $97.25 | +23% |
| Volatility model ≥ 2%, hold to the close | 7624 | $62.15 | +7% |
| Momentum model ≥ 2%, hold to the close | 6326 | -$13.05 | -2% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 52339 | 52322 | 201 (0%) | 1.07% | -$3,561.90 (-56%) | Hold to the close: -$3,561.90 (-56%) |

*In play or awaiting result: 9. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 31667 | 4.8% | 0.4% (128) | -678% | ❌ Worse |
| Momentum model | 31667 | 4.6% | 0.4% (128) | -703% | ❌ Worse |
| Mean-reversion model | 31667 | 8.1% | 0.4% (128) | -821% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 31667 | 128 | -48% | -87% | -87% | -84% |
| Volatility model ≥ 2% | 7624 | 70 | +7% | -77% | -76% | -72% |
| Volatility model ≥ 5% | 4165 | 46 | +39% | -72% | -70% | -66% |
| Volatility model ≥ 10% | 2400 | 28 | +67% | -62% | -60% | -56% |
| Momentum model ≥ 2% | 6326 | 51 | -2% | -78% | -77% | -74% |
| Momentum model ≥ 5% | 3885 | 37 | +23% | -74% | -73% | -69% |
| Momentum model ≥ 10% | 2549 | 25 | +38% | -65% | -65% | -60% |
| Mean-reversion model ≥ 2% | 13103 | 91 | -24% | -82% | -82% | -79% |
| Mean-reversion model ≥ 5% | 9184 | 78 | -6% | -79% | -79% | -76% |
| Mean-reversion model ≥ 10% | 6139 | 56 | +4% | -77% | -76% | -74% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 31872 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 12429 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 8021 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 52322 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 201 | 0% | -$3,561.90 | -56% | — |
| Sell at 2¢ | 2079 | 4% | -$5,555.36 | -87% | 47 sec |
| Sell at 3¢ | 1415 | 3% | -$5,544.05 | -87% | 48 sec |
| Sell at 5¢ | 986 | 2% | -$5,427.00 | -85% | 63 sec |
| Sell at 10¢ | 597 | 1% | -$5,201.83 | -82% | 65 sec |
| Sell at 25¢ | 316 | 1% | -$4,825.94 | -76% | 82 sec |
| Sell at 50¢ | 207 | 0% | -$4,376.65 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 12 | 0 | 25% | 17% | -100% | -57% | -35% |
| 5–10 min | 2619 | 12 | 11% | 4% | -56% | -81% | -82% |
| 2–5 min | 16917 | 93 | 7% | 3% | -46% | -87% | -87% |
| 1–2 min | 13195 | 44 | 3% | 2% | -63% | -92% | -92% |
| Under 1 min | 19579 | 52 | 1% | 0% | -62% | -85% | -84% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 3569 | 15 | 5% | 2% | -45% | -88% | -88% |
| SOL | 3564 | 16 | 4% | 2% | -43% | -87% | -86% |
| HYPE | 3557 | 11 | 5% | 2% | -61% | -89% | -88% |
| BNB | 3550 | 19 | 5% | 2% | -33% | -86% | -85% |
| DOGE | 3545 | 8 | 4% | 2% | -72% | -90% | -90% |
| ETH | 3540 | 15 | 7% | 3% | -48% | -82% | -81% |
| BTC | 3520 | 17 | 5% | 2% | -34% | -87% | -88% |
| NEAR | 3519 | 16 | 5% | 2% | -41% | -85% | -85% |
| XRP | 3508 | 13 | 3% | 1% | -54% | -89% | -88% |
| GOLD | 1882 | 5 | 5% | 2% | -68% | -81% | -83% |
| WTI | 1857 | 6 | 4% | 2% | -61% | -91% | -92% |
| SILVER | 1834 | 8 | 5% | 2% | -49% | -83% | -82% |
| PLATINUM | 1661 | 4 | 2% | 1% | -78% | -96% | -95% |
| EURUSD | 1597 | 5 | 2% | 1% | -71% | -90% | -89% |
| COPPER | 1559 | 6 | 2% | 1% | -64% | -73% | -73% |
| NATGAS | 1519 | 8 | 2% | 1% | -51% | -78% | -77% |
| GBPUSD | 1516 | 5 | 2% | 1% | -69% | -96% | -96% |
| USDJPY | 1497 | 6 | 2% | 1% | -63% | -97% | -96% |
| PALLADIUM | 1495 | 4 | 1% | 1% | -75% | -92% | -92% |
| AUDUSD | 1060 | 6 | 2% | 1% | -47% | -87% | -88% |
| USDCAD | 1028 | 0 | 2% | 1% | -100% | -96% | -97% |
| BRENT | 622 | 0 | 2% | 1% | -100% | -97% | -97% |
| 10YRRATE | 347 | 2 | 4% | 2% | -46% | -66% | -63% |
| 2YRRATE | 330 | 4 | 4% | 2% | +13% | -36% | -35% |
| 30YRRATE | 324 | 0 | 2% | 1% | -100% | -96% | -94% |
| 5YRRATE | 305 | 2 | 4% | 2% | -39% | -93% | -95% |
| INX | 17 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 26533 | 105 | 4% | 2% | -54% | -88% | -87% |
| DOWN (bought NO) | 25789 | 96 | 4% | 2% | -57% | -86% | -86% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 5106 | 25 | 2% | 1% | -14% | -77% | -76% |
| 0.05–0.1% | 5435 | 20 | 3% | 2% | -44% | -91% | -91% |
| 0.1–0.2% | 8186 | 30 | 5% | 2% | -54% | -89% | -89% |
| 0.2–0.5% | 9523 | 40 | 6% | 3% | -53% | -87% | -86% |
| Over 0.5% | 3614 | 15 | 7% | 3% | -57% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 12908 | 43 | 4% | 2% | -62% | -88% | -88% |
| Morning (6am–12pm) | 12762 | 58 | 4% | 2% | -48% | -85% | -84% |
| Afternoon (12–6pm) | 12535 | 57 | 4% | 2% | -47% | -86% | -86% |
| Evening (6pm–12am) | 14117 | 43 | 4% | 2% | -65% | -90% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,877 |
| Time from buy to best bounce (bounced bets) | 51 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/10 9:44:54 AM | GOLD | UP | 5 sec | — | 0¢ | ❌ Lost | $0.00 |
| 11/10 9:44:54 AM | SOL | DOWN | 5 sec | +0.102% | 0¢ | ❌ Lost | $0.00 |
| 11/10 9:44:54 AM | 2YRRATE | DOWN | 5 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/10 9:44:54 AM | BRENT | UP | 5 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/10 9:44:54 AM | USDCAD | UP | 5 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/10 9:44:54 AM | WTI | UP | 5 sec | — | 0¢ | ❌ Lost | $0.00 |
| 11/10 9:44:38 AM | INX | UP | 21 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/10 9:44:23 AM | ETH | UP | 36 sec | -0.134% | 0¢ | ❌ Lost | $0.00 |
| 11/10 9:44:23 AM | XRP | DOWN | 36 sec | +0.239% | 0¢ | ❌ Lost | $0.00 |
| 11/10 9:44:04 AM | BTC | UP | 56 sec | -0.170% | 0¢ | ❌ Lost | $0.00 |
| 11/10 9:44:04 AM | USDJPY | DOWN | 56 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/10 9:43:48 AM | NATGAS | DOWN | 72 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/10 9:43:48 AM | BNB | UP | 72 sec | -0.203% | 1¢ | ❌ Lost | -$0.15 |
| 11/10 9:43:48 AM | EURUSD | UP | 72 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 11/10 9:43:32 AM | DOGE | UP | 88 sec | -0.277% | 1¢ | ❌ Lost | -$0.15 |
| 11/10 9:43:32 AM | 5YRRATE | DOWN | 88 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/10 9:43:17 AM | NEAR | UP | 1.7 min | -0.934% | 0¢ | ❌ Lost | $0.00 |
| 11/10 9:42:26 AM | HYPE | UP | 2.6 min | -0.659% | 1¢ | ❌ Lost | -$0.15 |
| 11/10 9:42:11 AM | COPPER | UP | 2.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/10 9:41:36 AM | 30YRRATE | DOWN | 3.4 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/10 9:41:20 AM | GBPUSD | UP | 3.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/10 9:41:05 AM | 10YRRATE | DOWN | 3.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/10 9:36:30 AM | ZEC | UP | 8.5 min | -4.265% | 8¢ | ❌ Lost | -$0.15 |
| 11/10 9:29:56 AM | 10YRRATE | DOWN | 3 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/10 9:29:56 AM | 30YRRATE | DOWN | 3 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/10 9:29:40 AM | SOL | UP | 19 sec | -0.265% | 0¢ | ❌ Lost | $0.00 |
| 11/10 9:29:25 AM | BTC | UP | 34 sec | -0.167% | 0¢ | ❌ Lost | $0.00 |
| 11/10 9:29:25 AM | USDCAD | UP | 34 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/10 9:29:25 AM | XRP | UP | 34 sec | -0.172% | 0¢ | ❌ Lost | -$0.15 |
| 11/10 9:29:08 AM | PALLADIUM | UP | 51 sec | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
