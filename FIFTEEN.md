# 15-Minute 1¢ Study

*Updated Tue Nov 17, 9:34 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 4469 finished bets | 1% | $220.20 | +45% | +4.93¢ | $83.70 / $136.50 |

*Expect about **89 buys a day** (~$13.30/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 4210 | $119.65 | +26% |
| Volatility model ≥ 2%, hold to the close | 8323 | $77.05 | +8% |
| Momentum model ≥ 2%, hold to the close | 6909 | $5.55 | +1% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 59759 | 59725 | 233 (0%) | 1.07% | -$4,004.90 (-55%) | Hold to the close: -$4,004.90 (-55%) |

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
| Volatility model | 35845 | 4.5% | 0.4% (152) | -627% | ❌ Worse |
| Momentum model | 35845 | 4.4% | 0.4% (152) | -653% | ❌ Worse |
| Mean-reversion model | 35845 | 7.9% | 0.4% (152) | -760% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 35845 | 152 | -46% | -87% | -87% | -84% |
| Volatility model ≥ 2% | 8323 | 77 | +8% | -77% | -76% | -72% |
| Volatility model ≥ 5% | 4469 | 51 | +45% | -72% | -70% | -67% |
| Volatility model ≥ 10% | 2570 | 30 | +69% | -63% | -61% | -58% |
| Momentum model ≥ 2% | 6909 | 57 | +1% | -78% | -78% | -74% |
| Momentum model ≥ 5% | 4210 | 41 | +26% | -74% | -74% | -70% |
| Momentum model ≥ 10% | 2742 | 26 | +35% | -66% | -66% | -62% |
| Mean-reversion model ≥ 2% | 14683 | 106 | -21% | -82% | -82% | -79% |
| Mean-reversion model ≥ 5% | 10217 | 88 | -5% | -80% | -79% | -77% |
| Mean-reversion model ≥ 10% | 6790 | 63 | +5% | -77% | -77% | -74% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 36051 | 5% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 14184 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 9490 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 59725 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 233 | 0% | -$4,004.90 | -55% | — |
| Sell at 2¢ | 2413 | 4% | -$6,345.52 | -87% | 47 sec |
| Sell at 3¢ | 1628 | 3% | -$6,337.98 | -87% | 48 sec |
| Sell at 5¢ | 1115 | 2% | -$6,220.15 | -86% | 63 sec |
| Sell at 10¢ | 679 | 1% | -$5,971.41 | -82% | 65 sec |
| Sell at 25¢ | 363 | 1% | -$5,533.37 | -76% | 80 sec |
| Sell at 50¢ | 240 | 0% | -$4,988.90 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 13 | 0 | 31% | 23% | -100% | -47% | -20% |
| 5–10 min | 3018 | 17 | 11% | 4% | -47% | -81% | -82% |
| 2–5 min | 19343 | 105 | 7% | 3% | -47% | -86% | -87% |
| 1–2 min | 14991 | 51 | 3% | 2% | -62% | -92% | -92% |
| Under 1 min | 22360 | 60 | 1% | 0% | -62% | -86% | -85% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 4032 | 19 | 5% | 3% | -38% | -88% | -87% |
| SOL | 4031 | 19 | 4% | 2% | -40% | -86% | -86% |
| HYPE | 4022 | 12 | 5% | 2% | -62% | -89% | -88% |
| BNB | 4012 | 20 | 5% | 2% | -37% | -85% | -85% |
| DOGE | 4011 | 11 | 4% | 2% | -65% | -90% | -89% |
| ETH | 4004 | 18 | 6% | 3% | -44% | -82% | -82% |
| NEAR | 3985 | 18 | 5% | 2% | -41% | -85% | -86% |
| BTC | 3985 | 21 | 5% | 2% | -28% | -86% | -88% |
| XRP | 3969 | 16 | 3% | 2% | -49% | -89% | -88% |
| GOLD | 2123 | 5 | 5% | 2% | -71% | -83% | -84% |
| WTI | 2103 | 7 | 4% | 1% | -60% | -91% | -92% |
| SILVER | 2061 | 9 | 5% | 2% | -48% | -83% | -83% |
| PLATINUM | 1878 | 4 | 3% | 1% | -80% | -95% | -95% |
| EURUSD | 1830 | 6 | 2% | 1% | -69% | -91% | -90% |
| COPPER | 1759 | 6 | 2% | 1% | -68% | -76% | -76% |
| GBPUSD | 1755 | 6 | 2% | 1% | -68% | -96% | -96% |
| NATGAS | 1735 | 10 | 2% | 1% | -46% | -75% | -74% |
| USDJPY | 1716 | 6 | 2% | 1% | -67% | -96% | -96% |
| PALLADIUM | 1690 | 4 | 1% | 0% | -78% | -93% | -93% |
| AUDUSD | 1271 | 6 | 2% | 1% | -56% | -89% | -89% |
| USDCAD | 1219 | 1 | 3% | 1% | -92% | -95% | -96% |
| BRENT | 835 | 0 | 2% | 1% | -100% | -97% | -98% |
| 10YRRATE | 429 | 2 | 3% | 1% | -56% | -72% | -70% |
| 2YRRATE | 415 | 4 | 4% | 2% | -10% | -49% | -48% |
| 30YRRATE | 398 | 0 | 2% | 1% | -100% | -96% | -94% |
| 5YRRATE | 385 | 2 | 4% | 2% | -52% | -93% | -95% |
| INX | 72 | 1 | 3% | 1% | +30% | -95% | -96% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 30390 | 119 | 4% | 2% | -55% | -88% | -88% |
| DOWN (bought NO) | 29335 | 114 | 4% | 2% | -55% | -86% | -87% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 5439 | 25 | 2% | 1% | -17% | -78% | -77% |
| 0.05–0.1% | 5888 | 24 | 3% | 2% | -37% | -91% | -91% |
| 0.1–0.2% | 9045 | 34 | 5% | 2% | -52% | -89% | -89% |
| 0.2–0.5% | 11148 | 48 | 7% | 3% | -51% | -86% | -86% |
| Over 0.5% | 4522 | 23 | 7% | 3% | -47% | -86% | -86% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 14507 | 45 | 4% | 2% | -65% | -88% | -88% |
| Morning (6am–12pm) | 14227 | 76 | 5% | 2% | -39% | -85% | -84% |
| Afternoon (12–6pm) | 14631 | 63 | 4% | 2% | -49% | -87% | -87% |
| Evening (6pm–12am) | 16360 | 49 | 4% | 2% | -66% | -89% | -89% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 5,069 |
| Time from buy to best bounce (bounced bets) | 50 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/17 9:29:52 AM | DOGE | UP | 7 sec | -0.184% | 0¢ | ❌ Lost | $0.00 |
| 11/17 9:29:52 AM | SOL | UP | 7 sec | -0.211% | 0¢ | ❌ Lost | $0.00 |
| 11/17 9:29:52 AM | GOLD | UP | 7 sec | — | 0¢ | ❌ Lost | $0.00 |
| 11/17 9:29:52 AM | NEAR | UP | 7 sec | -0.358% | 0¢ | ❌ Lost | $0.00 |
| 11/17 9:29:36 AM | XRP | UP | 23 sec | -0.290% | 0¢ | ❌ Lost | $0.00 |
| 11/17 9:29:36 AM | ZEC | UP | 23 sec | -0.403% | 0¢ | ❌ Lost | $0.00 |
| 11/17 9:29:20 AM | PLATINUM | UP | 39 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/17 9:29:20 AM | ETH | UP | 39 sec | -0.166% | 0¢ | ❌ Lost | $0.00 |
| 11/17 9:29:20 AM | HYPE | DOWN | 39 sec | +0.242% | 0¢ | ❌ Lost | $0.00 |
| 11/17 9:29:04 AM | BNB | UP | 55 sec | -0.214% | 1¢ | ❌ Lost | -$0.15 |
| 11/17 9:28:48 AM | INX | UP | 71 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/17 9:28:32 AM | WTI | UP | 87 sec | — | 0¢ | ❌ Lost | $0.00 |
| 11/17 9:28:32 AM | AUDUSD | UP | 87 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/17 9:28:32 AM | BRENT | UP | 87 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/17 9:28:16 AM | USDCAD | DOWN | 1.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/17 9:27:45 AM | USDJPY | UP | 2.2 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/17 9:27:45 AM | 30YRRATE | UP | 2.2 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/17 9:26:57 AM | 10YRRATE | UP | 3.0 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/17 9:26:57 AM | BTC | UP | 3.0 min | -0.457% | 1¢ | ❌ Lost | -$0.15 |
| 11/17 9:26:09 AM | GBPUSD | DOWN | 3.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/17 9:25:53 AM | PALLADIUM | UP | 4.1 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/17 9:25:22 AM | 5YRRATE | UP | 4.6 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/17 9:25:06 AM | 2YRRATE | UP | 4.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/17 9:14:59 AM | PALLADIUM | DOWN | 0 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/17 9:14:59 AM | ZEC | DOWN | 0 sec | +0.090% | 0¢ | ❌ Lost | $0.00 |
| 11/17 9:14:27 AM | ETH | DOWN | 32 sec | +0.175% | 0¢ | ❌ Lost | $0.00 |
| 11/17 9:14:27 AM | BNB | DOWN | 32 sec | +0.157% | 0¢ | ❌ Lost | $0.00 |
| 11/17 9:14:11 AM | USDJPY | DOWN | 49 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/17 9:14:11 AM | INX | DOWN | 49 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/17 9:14:11 AM | BTC | DOWN | 49 sec | +0.213% | 0¢ | ❌ Lost | $0.00 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
