# 15-Minute 1¢ Study

*Updated Tue Nov 10, 1:14 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 4150 finished bets | 1% | $183.05 | +40% | +4.41¢ | $89.20 / $93.85 |

*Expect about **96 buys a day** (~$14.46/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 3856 | $101.00 | +24% |
| Volatility model ≥ 2%, hold to the close | 7584 | $67.55 | +7% |
| Momentum model ≥ 2%, hold to the close | 6277 | -$6.45 | -1% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 51862 | 51822 | 199 (0%) | 1.07% | -$3,526.00 (-56%) | Hold to the close: -$3,526.00 (-56%) |

*In play or awaiting result: 32. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 31464 | 4.8% | 0.4% (128) | -678% | ❌ Worse |
| Momentum model | 31464 | 4.7% | 0.4% (128) | -703% | ❌ Worse |
| Mean-reversion model | 31464 | 8.1% | 0.4% (128) | -820% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 31464 | 128 | -48% | -87% | -87% | -84% |
| Volatility model ≥ 2% | 7584 | 70 | +7% | -77% | -76% | -71% |
| Volatility model ≥ 5% | 4150 | 46 | +40% | -71% | -70% | -66% |
| Volatility model ≥ 10% | 2393 | 28 | +68% | -62% | -60% | -56% |
| Momentum model ≥ 2% | 6277 | 51 | -1% | -78% | -77% | -74% |
| Momentum model ≥ 5% | 3856 | 37 | +24% | -73% | -73% | -68% |
| Momentum model ≥ 10% | 2531 | 25 | +39% | -65% | -64% | -60% |
| Mean-reversion model ≥ 2% | 13025 | 91 | -23% | -82% | -82% | -79% |
| Mean-reversion model ≥ 5% | 9135 | 78 | -5% | -79% | -79% | -76% |
| Mean-reversion model ≥ 10% | 6107 | 56 | +4% | -77% | -76% | -74% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 31669 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 12290 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 7863 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 51822 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 199 | 0% | -$3,526.00 | -56% | — |
| Sell at 2¢ | 2066 | 4% | -$5,494.84 | -87% | 47 sec |
| Sell at 3¢ | 1407 | 3% | -$5,483.27 | -87% | 48 sec |
| Sell at 5¢ | 982 | 2% | -$5,365.70 | -85% | 63 sec |
| Sell at 10¢ | 595 | 1% | -$5,140.55 | -81% | 65 sec |
| Sell at 25¢ | 314 | 1% | -$4,768.66 | -76% | 83 sec |
| Sell at 50¢ | 205 | 0% | -$4,326.25 | -69% | 1.7 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 12 | 0 | 25% | 17% | -100% | -57% | -35% |
| 5–10 min | 2574 | 12 | 11% | 4% | -56% | -81% | -82% |
| 2–5 min | 16746 | 93 | 7% | 3% | -45% | -87% | -86% |
| 1–2 min | 13096 | 44 | 3% | 2% | -63% | -92% | -92% |
| Under 1 min | 19394 | 50 | 1% | 0% | -63% | -85% | -84% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 3547 | 15 | 5% | 2% | -45% | -88% | -88% |
| SOL | 3542 | 16 | 4% | 2% | -42% | -87% | -87% |
| HYPE | 3534 | 11 | 5% | 2% | -61% | -89% | -88% |
| BNB | 3527 | 19 | 5% | 2% | -32% | -86% | -85% |
| DOGE | 3522 | 8 | 4% | 2% | -71% | -90% | -89% |
| ETH | 3518 | 15 | 7% | 3% | -47% | -81% | -81% |
| NEAR | 3497 | 16 | 5% | 2% | -41% | -85% | -85% |
| BTC | 3497 | 17 | 5% | 2% | -33% | -87% | -88% |
| XRP | 3485 | 13 | 3% | 1% | -53% | -89% | -88% |
| GOLD | 1863 | 5 | 6% | 2% | -67% | -81% | -83% |
| WTI | 1837 | 6 | 4% | 2% | -61% | -91% | -92% |
| SILVER | 1815 | 8 | 5% | 2% | -48% | -83% | -82% |
| PLATINUM | 1645 | 4 | 2% | 1% | -77% | -96% | -95% |
| EURUSD | 1580 | 5 | 2% | 1% | -70% | -90% | -89% |
| COPPER | 1542 | 6 | 2% | 1% | -64% | -73% | -72% |
| NATGAS | 1504 | 8 | 2% | 1% | -50% | -78% | -77% |
| GBPUSD | 1500 | 5 | 2% | 1% | -69% | -96% | -96% |
| PALLADIUM | 1481 | 3 | 1% | 0% | -81% | -92% | -92% |
| USDJPY | 1478 | 6 | 2% | 1% | -62% | -96% | -96% |
| AUDUSD | 1039 | 5 | 2% | 1% | -55% | -87% | -88% |
| USDCAD | 1008 | 0 | 2% | 1% | -100% | -96% | -97% |
| BRENT | 603 | 0 | 2% | 1% | -100% | -97% | -97% |
| 10YRRATE | 332 | 2 | 5% | 2% | -44% | -64% | -62% |
| 2YRRATE | 315 | 4 | 4% | 2% | +19% | -33% | -32% |
| 30YRRATE | 309 | 0 | 2% | 1% | -100% | -96% | -94% |
| 5YRRATE | 291 | 2 | 4% | 2% | -36% | -92% | -95% |
| INX | 11 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 26264 | 104 | 4% | 2% | -54% | -88% | -87% |
| DOWN (bought NO) | 25558 | 95 | 4% | 2% | -57% | -86% | -86% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 5099 | 25 | 2% | 1% | -13% | -77% | -76% |
| 0.05–0.1% | 5413 | 20 | 3% | 2% | -44% | -91% | -91% |
| 0.1–0.2% | 8144 | 30 | 5% | 2% | -53% | -89% | -89% |
| 0.2–0.5% | 9463 | 40 | 6% | 3% | -53% | -87% | -86% |
| Over 0.5% | 3542 | 15 | 7% | 3% | -56% | -87% | -88% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 12745 | 43 | 4% | 2% | -61% | -87% | -88% |
| Morning (6am–12pm) | 12425 | 56 | 4% | 2% | -49% | -84% | -84% |
| Afternoon (12–6pm) | 12535 | 57 | 4% | 2% | -47% | -86% | -86% |
| Evening (6pm–12am) | 14117 | 43 | 4% | 2% | -65% | -90% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,907 |
| Time from buy to best bounce (bounced bets) | 50 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/10 1:14:53 AM | BTC | UP | 6 sec | -0.065% | — | In play | — |
| 11/10 1:14:53 AM | NATGAS | DOWN | 6 sec | — | — | In play | — |
| 11/10 1:14:53 AM | DOGE | UP | 6 sec | -0.039% | — | In play | — |
| 11/10 1:14:53 AM | AUDUSD | UP | 6 sec | — | — | In play | — |
| 11/10 1:14:53 AM | USDJPY | UP | 6 sec | — | — | In play | — |
| 11/10 1:14:36 AM | SOL | UP | 24 sec | -0.086% | — | In play | — |
| 11/10 1:14:36 AM | WTI | UP | 24 sec | — | — | In play | — |
| 11/10 1:14:20 AM | USDCAD | DOWN | 40 sec | — | — | In play | — |
| 11/10 1:14:20 AM | ETH | DOWN | 40 sec | +0.046% | — | In play | — |
| 11/10 1:14:20 AM | BRENT | UP | 40 sec | — | — | In play | — |
| 11/10 1:14:04 AM | HYPE | DOWN | 56 sec | +0.109% | — | In play | — |
| 11/10 1:13:49 AM | COPPER | DOWN | 70 sec | — | — | In play | — |
| 11/10 1:13:16 AM | ZEC | UP | 1.7 min | -0.321% | — | In play | — |
| 11/10 1:13:00 AM | 5YRRATE | UP | 2.0 min | — | — | In play | — |
| 11/10 1:13:00 AM | BNB | UP | 2.0 min | -0.096% | — | In play | — |
| 11/10 1:12:45 AM | NEAR | UP | 2.2 min | -0.404% | — | In play | — |
| 11/10 1:12:12 AM | GOLD | DOWN | 2.8 min | — | — | In play | — |
| 11/10 1:11:41 AM | 10YRRATE | UP | 3.3 min | — | — | In play | — |
| 11/10 1:11:41 AM | PLATINUM | DOWN | 3.3 min | — | — | In play | — |
| 11/10 1:10:54 AM | SILVER | DOWN | 4.1 min | — | — | In play | — |
| 11/10 1:10:38 AM | 30YRRATE | UP | 4.4 min | — | — | In play | — |
| 11/10 1:10:22 AM | PALLADIUM | DOWN | 4.6 min | — | — | In play | — |
| 11/10 1:09:34 AM | XRP | UP | 5.4 min | -0.511% | — | In play | — |
| 11/10 12:59:51 AM | 2YRRATE | DOWN | 9 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/10 12:59:51 AM | EURUSD | DOWN | 9 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/10 12:59:51 AM | BTC | UP | 9 sec | -0.034% | 0¢ | ❌ Lost | $0.00 |
| 11/10 12:59:35 AM | 10YRRATE | DOWN | 25 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/10 12:59:35 AM | GOLD | UP | 25 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 11/10 12:59:19 AM | WTI | DOWN | 41 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 11/10 12:59:19 AM | PLATINUM | UP | 41 sec | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
