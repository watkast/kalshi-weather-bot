# 15-Minute 1¢ Study

*Updated Mon Nov 9, 8:05 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 4104 finished bets | 1% | $187.55 | +41% | +4.57¢ | $91.90 / $95.65 |

*Expect about **97 buys a day** (~$14.54/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 3811 | $105.20 | +25% |
| Volatility model ≥ 2%, hold to the close | 7511 | $75.65 | +8% |
| Momentum model ≥ 2%, hold to the close | 6209 | $0.60 | +0% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 51096 | 51079 | 189 (0%) | 1.07% | -$3,571.95 (-57%) | Hold to the close: -$3,571.95 (-57%) |

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
| Volatility model | 31120 | 4.8% | 0.4% (124) | -685% | ❌ Worse |
| Momentum model | 31120 | 4.6% | 0.4% (124) | -711% | ❌ Worse |
| Mean-reversion model | 31120 | 8.1% | 0.4% (124) | -828% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 31120 | 124 | -49% | -87% | -87% | -84% |
| Volatility model ≥ 2% | 7511 | 70 | +8% | -77% | -75% | -71% |
| Volatility model ≥ 5% | 4104 | 46 | +41% | -71% | -70% | -66% |
| Volatility model ≥ 10% | 2361 | 28 | +70% | -61% | -60% | -56% |
| Momentum model ≥ 2% | 6209 | 51 | +0% | -78% | -77% | -74% |
| Momentum model ≥ 5% | 3811 | 37 | +25% | -73% | -73% | -68% |
| Momentum model ≥ 10% | 2498 | 25 | +41% | -65% | -64% | -59% |
| Mean-reversion model ≥ 2% | 12869 | 90 | -23% | -82% | -82% | -79% |
| Mean-reversion model ≥ 5% | 9023 | 77 | -5% | -79% | -79% | -76% |
| Mean-reversion model ≥ 10% | 6031 | 56 | +6% | -77% | -76% | -74% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 31325 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 12060 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 7694 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 51079 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 189 | 0% | -$3,571.95 | -57% | — |
| Sell at 2¢ | 2022 | 4% | -$5,412.23 | -87% | 47 sec |
| Sell at 3¢ | 1376 | 3% | -$5,401.31 | -87% | 48 sec |
| Sell at 5¢ | 961 | 2% | -$5,285.30 | -85% | 62 sec |
| Sell at 10¢ | 580 | 1% | -$5,066.15 | -81% | 65 sec |
| Sell at 25¢ | 301 | 1% | -$4,717.64 | -76% | 83 sec |
| Sell at 50¢ | 194 | 0% | -$4,306.45 | -69% | 1.8 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 12 | 0 | 25% | 17% | -100% | -57% | -35% |
| 5–10 min | 2531 | 12 | 11% | 4% | -55% | -81% | -82% |
| 2–5 min | 16503 | 88 | 7% | 3% | -47% | -87% | -87% |
| 1–2 min | 12914 | 43 | 3% | 2% | -63% | -92% | -92% |
| Under 1 min | 19119 | 46 | 1% | 0% | -66% | -84% | -84% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 3511 | 15 | 5% | 2% | -45% | -88% | -88% |
| SOL | 3503 | 15 | 4% | 2% | -45% | -87% | -87% |
| HYPE | 3494 | 11 | 5% | 2% | -61% | -89% | -88% |
| BNB | 3488 | 19 | 5% | 2% | -31% | -86% | -85% |
| DOGE | 3486 | 7 | 4% | 2% | -75% | -90% | -89% |
| ETH | 3480 | 14 | 7% | 3% | -50% | -81% | -81% |
| NEAR | 3459 | 16 | 5% | 2% | -40% | -85% | -85% |
| BTC | 3457 | 16 | 5% | 2% | -36% | -87% | -89% |
| XRP | 3447 | 13 | 3% | 1% | -53% | -89% | -89% |
| GOLD | 1835 | 5 | 6% | 2% | -67% | -81% | -83% |
| WTI | 1805 | 6 | 4% | 1% | -60% | -92% | -92% |
| SILVER | 1785 | 8 | 5% | 2% | -47% | -82% | -82% |
| PLATINUM | 1617 | 4 | 2% | 1% | -77% | -96% | -95% |
| EURUSD | 1550 | 4 | 2% | 1% | -76% | -90% | -89% |
| COPPER | 1514 | 6 | 2% | 1% | -63% | -72% | -72% |
| NATGAS | 1476 | 8 | 2% | 1% | -49% | -77% | -77% |
| GBPUSD | 1471 | 4 | 2% | 1% | -75% | -96% | -96% |
| PALLADIUM | 1453 | 3 | 1% | 0% | -81% | -92% | -92% |
| USDJPY | 1452 | 5 | 2% | 1% | -68% | -97% | -96% |
| AUDUSD | 1012 | 5 | 2% | 1% | -54% | -87% | -87% |
| USDCAD | 978 | 0 | 2% | 1% | -100% | -96% | -97% |
| BRENT | 575 | 0 | 2% | 1% | -100% | -97% | -97% |
| 10YRRATE | 327 | 1 | 4% | 2% | -71% | -64% | -62% |
| 2YRRATE | 308 | 3 | 4% | 2% | -9% | -32% | -31% |
| 30YRRATE | 304 | 0 | 2% | 1% | -100% | -97% | -95% |
| 5YRRATE | 284 | 1 | 4% | 1% | -67% | -93% | -95% |
| INX | 8 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 25892 | 98 | 4% | 2% | -56% | -88% | -87% |
| DOWN (bought NO) | 25187 | 91 | 4% | 2% | -58% | -86% | -86% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 5057 | 25 | 2% | 1% | -13% | -77% | -76% |
| 0.05–0.1% | 5351 | 19 | 3% | 2% | -46% | -91% | -91% |
| 0.1–0.2% | 8055 | 27 | 5% | 2% | -58% | -89% | -89% |
| 0.2–0.5% | 9341 | 40 | 6% | 3% | -52% | -87% | -86% |
| Over 0.5% | 3513 | 15 | 7% | 3% | -56% | -87% | -88% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 12671 | 43 | 4% | 2% | -61% | -87% | -87% |
| Morning (6am–12pm) | 12406 | 56 | 4% | 2% | -49% | -84% | -84% |
| Afternoon (12–6pm) | 12200 | 47 | 4% | 2% | -55% | -86% | -86% |
| Evening (6pm–12am) | 13802 | 43 | 4% | 2% | -64% | -90% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,915 |
| Time from buy to best bounce (bounced bets) | 50 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/9 7:59:59 AM | WTI | DOWN | 0 sec | — | 0¢ | ❌ Lost | $0.00 |
| 11/9 7:59:59 AM | PLATINUM | UP | 0 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/9 7:59:59 AM | PALLADIUM | UP | 0 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/9 7:59:59 AM | GBPUSD | UP | 0 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/9 7:59:59 AM | AUDUSD | UP | 0 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/9 7:59:43 AM | BRENT | DOWN | 16 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/9 7:59:43 AM | NATGAS | UP | 16 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/9 7:59:43 AM | SOL | UP | 16 sec | -0.067% | 0¢ | ❌ Lost | $0.00 |
| 11/9 7:59:43 AM | 30YRRATE | DOWN | 16 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/9 7:59:26 AM | 10YRRATE | DOWN | 33 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/9 7:59:26 AM | EURUSD | DOWN | 33 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/9 7:59:07 AM | ETH | DOWN | 53 sec | +0.125% | 1¢ | ❌ Lost | -$0.15 |
| 11/9 7:58:51 AM | 5YRRATE | DOWN | 69 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/9 7:58:51 AM | SILVER | UP | 69 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 11/9 7:58:20 AM | USDCAD | DOWN | 1.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/9 7:58:20 AM | XRP | DOWN | 1.7 min | +0.346% | 7¢ | ❌ Lost | -$0.15 |
| 11/9 7:58:20 AM | ZEC | DOWN | 1.7 min | +0.456% | 15¢ | ❌ Lost | -$0.15 |
| 11/9 7:58:00 AM | DOGE | DOWN | 2.0 min | +0.321% | 4¢ | ❌ Lost | $0.00 |
| 11/9 7:57:44 AM | NEAR | DOWN | 2.2 min | +0.789% | 0¢ | ❌ Lost | -$0.15 |
| 11/9 7:57:44 AM | INX | DOWN | 2.2 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/9 7:56:56 AM | BTC | DOWN | 3.1 min | +0.329% | 1¢ | ❌ Lost | -$0.15 |
| 11/9 7:56:40 AM | BNB | DOWN | 3.3 min | +0.308% | 1¢ | ❌ Lost | -$0.15 |
| 11/9 7:56:24 AM | HYPE | DOWN | 3.6 min | +0.960% | 0¢ | ❌ Lost | $0.00 |
| 11/9 7:52:47 AM | 2YRRATE | DOWN | 7.2 min | — | 13¢ | ❌ Lost | -$0.15 |
| 11/9 7:44:48 AM | EURUSD | UP | 11 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/9 7:44:48 AM | ETH | DOWN | 11 sec | +0.193% | 0¢ | ❌ Lost | $0.00 |
| 11/9 7:44:48 AM | XRP | DOWN | 11 sec | +0.265% | 0¢ | ❌ Lost | $0.00 |
| 11/9 7:44:32 AM | USDCAD | DOWN | 28 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/9 7:44:32 AM | COPPER | DOWN | 28 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/9 7:44:32 AM | GBPUSD | UP | 28 sec | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
