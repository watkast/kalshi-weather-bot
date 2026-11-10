# 15-Minute 1¢ Study

*Updated Tue Nov 10, 9:15 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 4164 finished bets | 1% | $181.25 | +39% | +4.35¢ | $88.75 / $92.50 |

*Expect about **96 buys a day** (~$14.39/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 3883 | $97.55 | +23% |
| Volatility model ≥ 2%, hold to the close | 7621 | $62.60 | +7% |
| Momentum model ≥ 2%, hold to the close | 6323 | -$12.60 | -2% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 52290 | 52252 | 201 (0%) | 1.07% | -$3,553.35 (-56%) | Hold to the close: -$3,553.35 (-56%) |

*In play or awaiting result: 30. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 31645 | 4.8% | 0.4% (128) | -678% | ❌ Worse |
| Momentum model | 31645 | 4.6% | 0.4% (128) | -703% | ❌ Worse |
| Mean-reversion model | 31645 | 8.1% | 0.4% (128) | -821% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 31645 | 128 | -48% | -87% | -87% | -84% |
| Volatility model ≥ 2% | 7621 | 70 | +7% | -77% | -76% | -72% |
| Volatility model ≥ 5% | 4164 | 46 | +39% | -72% | -70% | -66% |
| Volatility model ≥ 10% | 2400 | 28 | +67% | -62% | -60% | -56% |
| Momentum model ≥ 2% | 6323 | 51 | -2% | -78% | -77% | -74% |
| Momentum model ≥ 5% | 3883 | 37 | +23% | -74% | -73% | -69% |
| Momentum model ≥ 10% | 2547 | 25 | +38% | -65% | -65% | -60% |
| Mean-reversion model ≥ 2% | 13098 | 91 | -24% | -82% | -82% | -79% |
| Mean-reversion model ≥ 5% | 9183 | 78 | -6% | -79% | -79% | -76% |
| Mean-reversion model ≥ 10% | 6139 | 56 | +4% | -77% | -76% | -74% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 31850 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 12409 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 7993 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 52252 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 201 | 0% | -$3,553.35 | -56% | — |
| Sell at 2¢ | 2077 | 4% | -$5,547.33 | -87% | 47 sec |
| Sell at 3¢ | 1414 | 3% | -$5,535.89 | -87% | 48 sec |
| Sell at 5¢ | 985 | 2% | -$5,419.10 | -85% | 63 sec |
| Sell at 10¢ | 597 | 1% | -$5,193.28 | -82% | 65 sec |
| Sell at 25¢ | 316 | 1% | -$4,817.39 | -76% | 82 sec |
| Sell at 50¢ | 207 | 0% | -$4,368.10 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 12 | 0 | 25% | 17% | -100% | -57% | -35% |
| 5–10 min | 2616 | 12 | 11% | 4% | -56% | -81% | -82% |
| 2–5 min | 16896 | 93 | 7% | 3% | -46% | -87% | -87% |
| 1–2 min | 13180 | 44 | 3% | 2% | -63% | -92% | -92% |
| Under 1 min | 19548 | 52 | 1% | 0% | -62% | -85% | -84% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 3566 | 15 | 5% | 2% | -45% | -88% | -88% |
| SOL | 3562 | 16 | 4% | 2% | -43% | -87% | -86% |
| HYPE | 3555 | 11 | 5% | 2% | -61% | -89% | -88% |
| BNB | 3547 | 19 | 5% | 2% | -32% | -86% | -85% |
| DOGE | 3542 | 8 | 4% | 2% | -72% | -90% | -90% |
| ETH | 3538 | 15 | 7% | 3% | -48% | -82% | -81% |
| NEAR | 3517 | 16 | 5% | 2% | -41% | -85% | -85% |
| BTC | 3517 | 17 | 5% | 2% | -34% | -87% | -88% |
| XRP | 3506 | 13 | 3% | 1% | -54% | -89% | -88% |
| GOLD | 1879 | 5 | 5% | 2% | -68% | -81% | -83% |
| WTI | 1854 | 6 | 4% | 2% | -61% | -91% | -92% |
| SILVER | 1832 | 8 | 5% | 2% | -49% | -83% | -82% |
| PLATINUM | 1659 | 4 | 2% | 1% | -77% | -96% | -95% |
| EURUSD | 1594 | 5 | 2% | 1% | -71% | -90% | -89% |
| COPPER | 1556 | 6 | 2% | 1% | -64% | -73% | -73% |
| NATGAS | 1516 | 8 | 2% | 1% | -51% | -78% | -77% |
| GBPUSD | 1513 | 5 | 2% | 1% | -69% | -96% | -96% |
| PALLADIUM | 1494 | 4 | 1% | 1% | -75% | -92% | -92% |
| USDJPY | 1494 | 6 | 2% | 1% | -63% | -97% | -96% |
| AUDUSD | 1058 | 6 | 2% | 1% | -47% | -87% | -87% |
| USDCAD | 1025 | 0 | 2% | 1% | -100% | -96% | -97% |
| BRENT | 619 | 0 | 2% | 1% | -100% | -97% | -97% |
| 10YRRATE | 344 | 2 | 4% | 2% | -46% | -65% | -63% |
| 2YRRATE | 327 | 4 | 4% | 2% | +14% | -35% | -34% |
| 30YRRATE | 321 | 0 | 2% | 1% | -100% | -96% | -94% |
| 5YRRATE | 302 | 2 | 4% | 2% | -38% | -93% | -95% |
| INX | 15 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 26492 | 105 | 4% | 2% | -54% | -88% | -87% |
| DOWN (bought NO) | 25760 | 96 | 4% | 2% | -57% | -86% | -86% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 5106 | 25 | 2% | 1% | -14% | -77% | -76% |
| 0.05–0.1% | 5435 | 20 | 3% | 2% | -44% | -91% | -91% |
| 0.1–0.2% | 8179 | 30 | 5% | 2% | -54% | -89% | -89% |
| 0.2–0.5% | 9516 | 40 | 6% | 3% | -53% | -87% | -86% |
| Over 0.5% | 3606 | 15 | 7% | 3% | -57% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 12908 | 43 | 4% | 2% | -62% | -88% | -88% |
| Morning (6am–12pm) | 12692 | 58 | 4% | 2% | -48% | -84% | -84% |
| Afternoon (12–6pm) | 12535 | 57 | 4% | 2% | -47% | -86% | -86% |
| Evening (6pm–12am) | 14117 | 43 | 4% | 2% | -65% | -90% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,886 |
| Time from buy to best bounce (bounced bets) | 50 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/10 9:14:56 AM | WTI | DOWN | 4 sec | — | 0¢ | In play | — |
| 11/10 9:14:56 AM | 5YRRATE | DOWN | 4 sec | — | 0¢ | In play | — |
| 11/10 9:14:56 AM | 2YRRATE | DOWN | 4 sec | — | 0¢ | In play | — |
| 11/10 9:14:40 AM | BRENT | DOWN | 20 sec | — | 0¢ | In play | — |
| 11/10 9:14:40 AM | 10YRRATE | DOWN | 20 sec | — | 0¢ | In play | — |
| 11/10 9:14:25 AM | SILVER | UP | 35 sec | — | 0¢ | In play | — |
| 11/10 9:14:25 AM | PLATINUM | UP | 35 sec | — | 0¢ | In play | — |
| 11/10 9:14:25 AM | NEAR | DOWN | 35 sec | +0.182% | 0¢ | ❌ Lost | $0.00 |
| 11/10 9:14:25 AM | 30YRRATE | DOWN | 35 sec | — | 0¢ | In play | — |
| 11/10 9:14:06 AM | INX | DOWN | 54 sec | — | 0¢ | In play | — |
| 11/10 9:14:06 AM | BTC | DOWN | 54 sec | +0.194% | 0¢ | In play | — |
| 11/10 9:14:06 AM | AUDUSD | UP | 54 sec | — | 0¢ | In play | — |
| 11/10 9:14:06 AM | ZEC | UP | 54 sec | -0.364% | 0¢ | In play | — |
| 11/10 9:13:50 AM | BNB | DOWN | 70 sec | +0.177% | 0¢ | In play | — |
| 11/10 9:13:50 AM | GBPUSD | UP | 70 sec | — | 0¢ | In play | — |
| 11/10 9:13:50 AM | ETH | DOWN | 70 sec | +0.243% | 1¢ | ❌ Lost | -$0.15 |
| 11/10 9:13:50 AM | XRP | DOWN | 70 sec | +0.336% | 0¢ | ❌ Lost | $0.00 |
| 11/10 9:13:34 AM | GOLD | UP | 86 sec | — | 1¢ | In play | — |
| 11/10 9:13:19 AM | NATGAS | DOWN | 1.7 min | — | 0¢ | In play | — |
| 11/10 9:13:00 AM | EURUSD | UP | 2.0 min | — | 0¢ | In play | — |
| 11/10 9:13:00 AM | HYPE | DOWN | 2.0 min | +0.584% | 0¢ | ❌ Lost | $0.00 |
| 11/10 9:13:00 AM | USDJPY | DOWN | 2.0 min | — | 0¢ | In play | — |
| 11/10 9:13:00 AM | DOGE | DOWN | 2.0 min | +0.469% | 0¢ | In play | — |
| 11/10 9:12:13 AM | USDCAD | DOWN | 2.8 min | — | 0¢ | In play | — |
| 11/10 9:11:52 AM | COPPER | UP | 3.1 min | — | 0¢ | In play | — |
| 11/10 8:59:55 AM | SILVER | UP | 4 sec | — | 0¢ | ❌ Lost | $0.00 |
| 11/10 8:59:39 AM | GOLD | UP | 20 sec | — | 0¢ | ❌ Lost | $0.00 |
| 11/10 8:59:39 AM | HYPE | DOWN | 20 sec | +0.182% | 0¢ | ❌ Lost | $0.00 |
| 11/10 8:59:39 AM | 10YRRATE | UP | 20 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/10 8:59:22 AM | INX | UP | 37 sec | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
