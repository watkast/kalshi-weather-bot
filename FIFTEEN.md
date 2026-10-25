# 15-Minute 1¢ Study

*Updated Sun Oct 25, 3:29 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 2685 finished bets | 1% | $86.75 | +28% | +3.23¢ | $35.30 / $51.45 |

*Expect about **97 buys a day** (~$14.59/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 2470 | $62.55 | +23% |
| Volatility model ≥ 2%, hold to the close | 4961 | -$6.55 | -1% |
| Momentum model ≥ 2%, hold to the close | 4122 | -$22.20 | -5% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 31723 | 31706 | 120 (0%) | 1.07% | -$2,172.30 (-56%) | Hold to the close: -$2,172.30 (-56%) |

*In play or awaiting result: 16. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 20499 | 4.6% | 0.4% (85) | -647% | ❌ Worse |
| Momentum model | 20499 | 4.5% | 0.4% (85) | -671% | ❌ Worse |
| Mean-reversion model | 20499 | 7.9% | 0.4% (85) | -785% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 20499 | 85 | -48% | -88% | -87% | -85% |
| Volatility model ≥ 2% | 4961 | 43 | -1% | -78% | -77% | -74% |
| Volatility model ≥ 5% | 2685 | 28 | +28% | -74% | -73% | -70% |
| Volatility model ≥ 10% | 1520 | 18 | +65% | -66% | -64% | -61% |
| Momentum model ≥ 2% | 4122 | 33 | -5% | -80% | -80% | -76% |
| Momentum model ≥ 5% | 2470 | 24 | +23% | -76% | -76% | -72% |
| Momentum model ≥ 10% | 1613 | 16 | +36% | -70% | -70% | -65% |
| Mean-reversion model ≥ 2% | 8270 | 56 | -26% | -83% | -83% | -80% |
| Mean-reversion model ≥ 5% | 5793 | 47 | -11% | -81% | -80% | -78% |
| Mean-reversion model ≥ 10% | 3860 | 33 | -4% | -78% | -78% | -76% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 20699 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 7352 | 2% | 2% | 1% | 1% | 0% | 0% |
| Financials | 3655 | 2% | 1% | 1% | 1% | 0% | 0% |
| **All** | 31706 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 120 | 0% | -$2,172.30 | -56% | — |
| Sell at 2¢ | 1170 | 4% | -$3,380.10 | -88% | 47 sec |
| Sell at 3¢ | 802 | 3% | -$3,371.52 | -88% | 48 sec |
| Sell at 5¢ | 561 | 2% | -$3,319.65 | -86% | 61 sec |
| Sell at 10¢ | 346 | 1% | -$3,189.04 | -83% | 64 sec |
| Sell at 25¢ | 189 | 1% | -$2,946.71 | -76% | 82 sec |
| Sell at 50¢ | 122 | 0% | -$2,664.80 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 1393 | 7 | 11% | 4% | -52% | -81% | -83% |
| 2–5 min | 10160 | 55 | 7% | 3% | -47% | -87% | -87% |
| 1–2 min | 8029 | 30 | 3% | 1% | -59% | -92% | -91% |
| Under 1 min | 12120 | 28 | 1% | 0% | -67% | -86% | -86% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 2319 | 12 | 5% | 3% | -35% | -89% | -89% |
| HYPE | 2313 | 8 | 5% | 3% | -57% | -89% | -87% |
| BNB | 2308 | 13 | 5% | 3% | -30% | -84% | -83% |
| SOL | 2305 | 6 | 3% | 2% | -68% | -92% | -92% |
| ETH | 2300 | 11 | 6% | 3% | -43% | -86% | -86% |
| DOGE | 2295 | 4 | 4% | 2% | -78% | -91% | -90% |
| XRP | 2290 | 9 | 3% | 1% | -51% | -88% | -88% |
| NEAR | 2289 | 12 | 5% | 2% | -32% | -82% | -81% |
| BTC | 2280 | 12 | 5% | 2% | -30% | -88% | -90% |
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
| UP (bought YES) | 16055 | 66 | 4% | 2% | -53% | -87% | -87% |
| DOWN (bought NO) | 15651 | 54 | 4% | 1% | -60% | -88% | -88% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 3468 | 18 | 2% | 1% | -13% | -80% | -80% |
| 0.05–0.1% | 3568 | 11 | 3% | 2% | -55% | -92% | -92% |
| 0.1–0.2% | 5356 | 20 | 5% | 2% | -54% | -89% | -89% |
| 0.2–0.5% | 6014 | 28 | 6% | 3% | -49% | -87% | -86% |
| Over 0.5% | 2289 | 10 | 7% | 3% | -55% | -87% | -88% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 7904 | 32 | 4% | 2% | -54% | -85% | -85% |
| Morning (6am–12pm) | 7781 | 35 | 4% | 2% | -49% | -88% | -87% |
| Afternoon (12–6pm) | 7446 | 24 | 4% | 2% | -62% | -87% | -88% |
| Evening (6pm–12am) | 8575 | 29 | 3% | 2% | -61% | -90% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,821 |
| Time from buy to best bounce (bounced bets) | 49 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/25 3:29:40 PM | HYPE | UP | 19 sec | -0.047% | — | In play | — |
| 10/25 3:29:40 PM | BNB | DOWN | 19 sec | +0.026% | — | In play | — |
| 10/25 3:29:24 PM | BTC | DOWN | 35 sec | +0.036% | — | In play | — |
| 10/25 3:29:08 PM | XRP | UP | 51 sec | -0.123% | — | In play | — |
| 10/25 3:29:08 PM | DOGE | DOWN | 51 sec | +0.031% | — | In play | — |
| 10/25 3:28:37 PM | EURUSD | UP | 83 sec | — | — | In play | — |
| 10/25 3:25:10 PM | NEAR | UP | 4.8 min | -0.788% | — | In play | — |
| 10/25 3:25:10 PM | ZEC | UP | 4.8 min | -0.964% | — | In play | — |
| 10/25 3:25:10 PM | ETH | UP | 4.8 min | -0.283% | — | In play | — |
| 10/25 3:14:52 PM | XRP | DOWN | 7 sec | -0.023% | 0¢ | ❌ Lost | -$0.15 |
| 10/25 3:14:36 PM | BTC | DOWN | 23 sec | +0.032% | 0¢ | ❌ Lost | $0.00 |
| 10/25 3:14:04 PM | SOL | UP | 55 sec | -0.058% | 0¢ | ❌ Lost | -$0.15 |
| 10/25 3:13:33 PM | BNB | UP | 87 sec | -0.128% | 0¢ | ❌ Lost | -$0.15 |
| 10/25 3:12:12 PM | NEAR | UP | 2.8 min | -0.593% | 0¢ | ❌ Lost | -$0.15 |
| 10/25 3:12:12 PM | ZEC | UP | 2.8 min | -0.459% | 0¢ | ❌ Lost | $0.00 |
| 10/25 3:12:12 PM | DOGE | UP | 2.8 min | -0.257% | 1¢ | ❌ Lost | -$0.15 |
| 10/25 3:12:12 PM | ETH | UP | 2.8 min | -0.140% | 1¢ | ❌ Lost | -$0.15 |
| 10/25 3:11:56 PM | HYPE | UP | 3.0 min | -0.258% | 1¢ | ❌ Lost | -$0.15 |
| 10/25 2:59:48 PM | ZEC | UP | 12 sec | -0.007% | 0¢ | ❌ Lost | $0.00 |
| 10/25 2:59:48 PM | ETH | DOWN | 12 sec | +0.007% | 0¢ | ❌ Lost | $0.00 |
| 10/25 2:59:32 PM | SOL | UP | 28 sec | -0.037% | 1¢ | ❌ Lost | -$0.15 |
| 10/25 2:59:32 PM | DOGE | DOWN | 28 sec | +0.018% | 1¢ | ❌ Lost | -$0.15 |
| 10/25 2:59:16 PM | HYPE | DOWN | 44 sec | +0.035% | 0¢ | ❌ Lost | -$0.15 |
| 10/25 2:59:14 PM | BTC | UP | 46 sec | -0.032% | 1¢ | ❌ Lost | -$0.15 |
| 10/25 2:59:14 PM | XRP | DOWN | 46 sec | +0.015% | 0¢ | ❌ Lost | -$0.15 |
| 10/25 2:59:14 PM | BNB | UP | 46 sec | -0.068% | 0¢ | ❌ Lost | $0.00 |
| 10/25 2:58:46 PM | NEAR | DOWN | 73 sec | +0.083% | 1¢ | ❌ Lost | -$0.15 |
| 10/25 2:44:46 PM | SOL | UP | 14 sec | -0.052% | 0¢ | ❌ Lost | $0.00 |
| 10/25 2:44:30 PM | DOGE | UP | 30 sec | -0.044% | 1¢ | ❌ Lost | -$0.15 |
| 10/25 2:44:14 PM | BTC | UP | 46 sec | -0.084% | 0¢ | ❌ Lost | $0.00 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
