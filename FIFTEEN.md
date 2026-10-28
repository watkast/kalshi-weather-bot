# 15-Minute 1¢ Study

*Updated Wed Oct 28, 3:00 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 2945 finished bets | 1% | $87.75 | +26% | +2.98¢ | $89.10 / -$1.35 |

*Expect about **98 buys a day** (~$14.69/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 2733 | $49.40 | +16% |
| Volatility model ≥ 2%, hold to the close | 5459 | $19.55 | +3% |
| Momentum model ≥ 2%, hold to the close | 4516 | -$50.50 | -10% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 35988 | 35965 | 138 (0%) | 1.07% | -$2,452.80 (-56%) | Hold to the close: -$2,452.80 (-56%) |

*In play or awaiting result: 22. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 22567 | 4.7% | 0.4% (92) | -665% | ❌ Worse |
| Momentum model | 22567 | 4.6% | 0.4% (92) | -690% | ❌ Worse |
| Mean-reversion model | 22567 | 8.0% | 0.4% (92) | -808% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 22567 | 92 | -49% | -88% | -87% | -85% |
| Volatility model ≥ 2% | 5459 | 49 | +3% | -78% | -77% | -74% |
| Volatility model ≥ 5% | 2945 | 30 | +26% | -75% | -74% | -71% |
| Volatility model ≥ 10% | 1673 | 19 | +60% | -68% | -66% | -64% |
| Momentum model ≥ 2% | 4516 | 34 | -10% | -81% | -80% | -78% |
| Momentum model ≥ 5% | 2733 | 25 | +16% | -78% | -77% | -74% |
| Momentum model ≥ 10% | 1797 | 17 | +30% | -72% | -71% | -68% |
| Mean-reversion model ≥ 2% | 9191 | 63 | -25% | -83% | -83% | -81% |
| Mean-reversion model ≥ 5% | 6452 | 53 | -9% | -81% | -80% | -78% |
| Mean-reversion model ≥ 10% | 4313 | 38 | -1% | -79% | -78% | -76% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 22767 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 8551 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 4647 | 2% | 1% | 1% | 1% | 0% | 0% |
| **All** | 35965 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 138 | 0% | -$2,452.80 | -56% | — |
| Sell at 2¢ | 1363 | 4% | -$3,834.42 | -87% | 47 sec |
| Sell at 3¢ | 935 | 3% | -$3,824.15 | -87% | 48 sec |
| Sell at 5¢ | 649 | 2% | -$3,766.95 | -86% | 62 sec |
| Sell at 10¢ | 397 | 1% | -$3,612.73 | -82% | 65 sec |
| Sell at 25¢ | 214 | 1% | -$3,326.46 | -76% | 86 sec |
| Sell at 50¢ | 142 | 0% | -$2,992.30 | -68% | 1.9 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 1598 | 8 | 11% | 4% | -52% | -81% | -82% |
| 2–5 min | 11502 | 66 | 7% | 3% | -43% | -87% | -87% |
| 1–2 min | 9133 | 32 | 3% | 1% | -62% | -92% | -92% |
| Under 1 min | 13728 | 32 | 1% | 0% | -67% | -86% | -85% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 2549 | 12 | 5% | 2% | -40% | -89% | -88% |
| HYPE | 2542 | 8 | 5% | 3% | -61% | -89% | -87% |
| BNB | 2541 | 15 | 5% | 2% | -26% | -85% | -83% |
| SOL | 2535 | 7 | 4% | 2% | -65% | -92% | -92% |
| ETH | 2529 | 11 | 6% | 3% | -47% | -86% | -85% |
| DOGE | 2527 | 5 | 4% | 2% | -75% | -90% | -90% |
| XRP | 2517 | 11 | 3% | 1% | -46% | -89% | -89% |
| NEAR | 2515 | 12 | 5% | 2% | -38% | -82% | -82% |
| BTC | 2512 | 13 | 5% | 2% | -31% | -88% | -89% |
| GOLD | 1355 | 5 | 5% | 2% | -56% | -81% | -83% |
| SILVER | 1324 | 6 | 4% | 2% | -47% | -82% | -82% |
| WTI | 1306 | 4 | 3% | 1% | -64% | -93% | -94% |
| PLATINUM | 1172 | 1 | 2% | 1% | -92% | -97% | -97% |
| COPPER | 1120 | 4 | 1% | 1% | -67% | -73% | -73% |
| EURUSD | 1098 | 3 | 2% | 1% | -74% | -88% | -88% |
| NATGAS | 1080 | 6 | 2% | 1% | -48% | -79% | -79% |
| PALLADIUM | 1039 | 2 | 1% | 0% | -82% | -89% | -90% |
| GBPUSD | 1035 | 2 | 2% | 1% | -82% | -96% | -96% |
| USDJPY | 1021 | 5 | 2% | 1% | -54% | -97% | -96% |
| AUDUSD | 577 | 4 | 1% | 1% | -35% | -81% | -80% |
| USDCAD | 536 | 0 | 1% | 0% | -100% | -97% | -98% |
| BRENT | 155 | 0 | 1% | 1% | -100% | -99% | -98% |
| 10YRRATE | 104 | 0 | 4% | 0% | -100% | -93% | -92% |
| 30YRRATE | 95 | 0 | 0% | 0% | -100% | -100% | -100% |
| 2YRRATE | 92 | 1 | 3% | 1% | +1% | +7% | +7% |
| 5YRRATE | 89 | 1 | 4% | 2% | +5% | -92% | -94% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 18188 | 77 | 4% | 2% | -51% | -87% | -86% |
| DOWN (bought NO) | 17777 | 61 | 4% | 2% | -61% | -88% | -88% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 3755 | 19 | 2% | 1% | -14% | -81% | -80% |
| 0.05–0.1% | 3916 | 14 | 3% | 2% | -47% | -92% | -91% |
| 0.1–0.2% | 5930 | 22 | 5% | 2% | -54% | -90% | -89% |
| 0.2–0.5% | 6688 | 29 | 6% | 3% | -52% | -87% | -86% |
| Over 0.5% | 2474 | 10 | 7% | 3% | -58% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 8992 | 35 | 4% | 2% | -56% | -86% | -86% |
| Morning (6am–12pm) | 8741 | 42 | 4% | 2% | -45% | -86% | -85% |
| Afternoon (12–6pm) | 8419 | 29 | 4% | 2% | -60% | -88% | -88% |
| Evening (6pm–12am) | 9813 | 32 | 3% | 2% | -63% | -91% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,634 |
| Time from buy to best bounce (bounced bets) | 50 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/28 2:59:58 AM | WTI | DOWN | 2 sec | — | 0¢ | In play | — |
| 10/28 2:59:42 AM | USDJPY | UP | 18 sec | — | 0¢ | In play | — |
| 10/28 2:59:42 AM | PALLADIUM | UP | 18 sec | — | 0¢ | In play | — |
| 10/28 2:59:26 AM | GOLD | UP | 34 sec | — | 0¢ | In play | — |
| 10/28 2:59:11 AM | GBPUSD | UP | 48 sec | — | 0¢ | In play | — |
| 10/28 2:59:11 AM | USDCAD | DOWN | 48 sec | — | 0¢ | In play | — |
| 10/28 2:59:11 AM | ZEC | UP | 48 sec | -0.216% | 0¢ | In play | — |
| 10/28 2:59:11 AM | PLATINUM | UP | 48 sec | — | 0¢ | In play | — |
| 10/28 2:58:37 AM | SILVER | UP | 83 sec | — | 0¢ | In play | — |
| 10/28 2:58:21 AM | HYPE | DOWN | 1.6 min | +0.148% | 0¢ | In play | — |
| 10/28 2:58:06 AM | BNB | UP | 1.9 min | -0.164% | 1¢ | In play | — |
| 10/28 2:57:18 AM | NEAR | UP | 2.7 min | -0.483% | 1¢ | ❌ Lost | -$0.15 |
| 10/28 2:56:45 AM | XRP | UP | 3.2 min | -0.262% | 1¢ | In play | — |
| 10/28 2:56:13 AM | DOGE | UP | 3.8 min | -0.214% | 1¢ | In play | — |
| 10/28 2:55:24 AM | BTC | UP | 4.6 min | -0.202% | 1¢ | ❌ Lost | -$0.15 |
| 10/28 2:55:08 AM | ETH | UP | 4.8 min | -0.320% | 1¢ | In play | — |
| 10/28 2:54:33 AM | SOL | UP | 5.5 min | -0.327% | 1¢ | In play | — |
| 10/28 2:44:56 AM | USDCAD | UP | 3 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/28 2:44:56 AM | 30YRRATE | DOWN | 3 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/28 2:44:56 AM | PALLADIUM | DOWN | 3 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/28 2:44:40 AM | USDJPY | DOWN | 19 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/28 2:44:40 AM | NATGAS | UP | 19 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/28 2:44:40 AM | NEAR | UP | 19 sec | -0.363% | 0¢ | ❌ Lost | $0.00 |
| 10/28 2:44:24 AM | ZEC | UP | 35 sec | -0.283% | 0¢ | ❌ Lost | $0.00 |
| 10/28 2:44:24 AM | GBPUSD | UP | 35 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/28 2:44:24 AM | GOLD | DOWN | 35 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/28 2:44:08 AM | BRENT | DOWN | 52 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/28 2:43:49 AM | XRP | DOWN | 71 sec | +0.105% | 0¢ | ❌ Lost | $0.00 |
| 10/28 2:43:49 AM | 10YRRATE | DOWN | 71 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/28 2:43:33 AM | BNB | DOWN | 87 sec | +0.125% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
