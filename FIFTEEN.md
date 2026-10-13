# 15-Minute 1¢ Study

*Updated Tue Oct 13, 6:00 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 1261 finished bets | 1% | $43.85 | +32% | +3.48¢ | $30.35 / $13.50 |

*Expect about **83 buys a day** (~$12.46/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 1206 | $24.10 | +19% |
| 5+ min left, hold to the close | 469 | -$13.45 | -19% |
| Volatility model ≥ 5%, sell at 50¢ | 1261 | -$15.15 | -11% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 16599 | 16579 | 63 (0%) | 1.07% | -$1,126.20 (-56%) | Hold to the close: -$1,126.20 (-56%) |

*In play or awaiting result: 19. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 10934 | 4.5% | 0.4% (46) | -657% | ❌ Worse |
| Momentum model | 10934 | 4.4% | 0.4% (46) | -684% | ❌ Worse |
| Mean-reversion model | 10934 | 7.2% | 0.4% (46) | -770% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 10934 | 46 | -47% | -88% | -88% | -86% |
| Volatility model ≥ 2% | 2246 | 18 | -7% | -78% | -77% | -74% |
| Volatility model ≥ 5% | 1261 | 13 | +32% | -73% | -72% | -69% |
| Volatility model ≥ 10% | 780 | 9 | +65% | -63% | -63% | -59% |
| Momentum model ≥ 2% | 1975 | 15 | -8% | -79% | -80% | -78% |
| Momentum model ≥ 5% | 1206 | 11 | +19% | -76% | -76% | -73% |
| Momentum model ≥ 10% | 821 | 8 | +38% | -69% | -69% | -64% |
| Mean-reversion model ≥ 2% | 3912 | 27 | -25% | -85% | -85% | -82% |
| Mean-reversion model ≥ 5% | 2670 | 20 | -17% | -83% | -82% | -79% |
| Mean-reversion model ≥ 10% | 1760 | 14 | -8% | -81% | -81% | -78% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 11132 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 3994 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 1453 | 2% | 1% | 1% | 1% | 0% | 0% |
| **All** | 16579 | 3% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 63 | 0% | -$1,126.20 | -56% | — |
| Sell at 2¢ | 565 | 3% | -$1,819.30 | -91% | 33 sec |
| Sell at 3¢ | 373 | 2% | -$1,820.73 | -91% | 46 sec |
| Sell at 5¢ | 268 | 2% | -$1,792.00 | -89% | 49 sec |
| Sell at 10¢ | 174 | 1% | -$1,710.26 | -85% | 63 sec |
| Sell at 25¢ | 99 | 1% | -$1,582.51 | -79% | 79 sec |
| Sell at 50¢ | 64 | 0% | -$1,422.20 | -71% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 465 | 4 | 11% | 3% | -19% | -80% | -86% |
| 2–5 min | 5363 | 32 | 6% | 3% | -41% | -88% | -89% |
| 1–2 min | 4374 | 16 | 3% | 2% | -60% | -94% | -94% |
| Under 1 min | 6373 | 11 | 1% | 0% | -75% | -91% | -91% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 1250 | 7 | 4% | 2% | -31% | -90% | -90% |
| HYPE | 1246 | 4 | 4% | 2% | -60% | -90% | -89% |
| DOGE | 1240 | 2 | 4% | 2% | -80% | -91% | -90% |
| BNB | 1239 | 5 | 4% | 2% | -51% | -91% | -91% |
| ETH | 1238 | 8 | 5% | 2% | -21% | -90% | -89% |
| SOL | 1237 | 2 | 3% | 1% | -80% | -93% | -92% |
| BTC | 1231 | 6 | 5% | 2% | -35% | -88% | -91% |
| XRP | 1226 | 7 | 2% | 1% | -29% | -85% | -85% |
| NEAR | 1225 | 7 | 5% | 2% | -26% | -77% | -78% |
| GOLD | 657 | 0 | 3% | 1% | -100% | -93% | -95% |
| SILVER | 639 | 1 | 3% | 1% | -82% | -94% | -94% |
| WTI | 611 | 3 | 3% | 1% | -44% | -94% | -96% |
| COPPER | 570 | 0 | 1% | 1% | -100% | -98% | -97% |
| PLATINUM | 529 | 0 | 0% | 0% | -100% | -99% | -99% |
| PALLADIUM | 498 | 1 | 1% | 0% | -81% | -98% | -98% |
| NATGAS | 490 | 3 | 3% | 2% | -43% | -95% | -94% |
| EURUSD | 477 | 3 | 3% | 2% | -41% | -76% | -75% |
| GBPUSD | 452 | 1 | 2% | 1% | -79% | -96% | -96% |
| USDJPY | 412 | 3 | 1% | 1% | -32% | -98% | -97% |
| AUDUSD | 57 | 0 | 0% | 0% | -100% | -100% | -100% |
| USDCAD | 55 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 8364 | 34 | 3% | 2% | -53% | -90% | -90% |
| DOWN (bought NO) | 8215 | 29 | 3% | 2% | -59% | -91% | -92% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 1956 | 10 | 2% | 1% | -15% | -77% | -77% |
| 0.05–0.1% | 1969 | 6 | 3% | 1% | -56% | -92% | -92% |
| 0.1–0.2% | 2833 | 9 | 4% | 2% | -61% | -91% | -92% |
| 0.2–0.5% | 3143 | 18 | 6% | 3% | -37% | -89% | -89% |
| Over 0.5% | 1228 | 5 | 6% | 2% | -58% | -88% | -90% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 4331 | 20 | 4% | 2% | -47% | -87% | -87% |
| Morning (6am–12pm) | 3780 | 20 | 4% | 2% | -39% | -91% | -91% |
| Afternoon (12–6pm) | 3818 | 9 | 3% | 1% | -72% | -91% | -91% |
| Evening (6pm–12am) | 4650 | 14 | 3% | 1% | -66% | -94% | -94% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 25 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,490 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/13 5:59:47 AM | AUDUSD | DOWN | 12 sec | — | 0¢ | In play | — |
| 10/13 5:59:47 AM | EURUSD | UP | 12 sec | — | 0¢ | In play | — |
| 10/13 5:59:47 AM | NATGAS | UP | 12 sec | — | 0¢ | In play | — |
| 10/13 5:59:31 AM | PLATINUM | UP | 28 sec | — | 0¢ | In play | — |
| 10/13 5:59:15 AM | SILVER | UP | 44 sec | — | 0¢ | In play | — |
| 10/13 5:58:44 AM | USDJPY | DOWN | 76 sec | — | 0¢ | In play | — |
| 10/13 5:57:23 AM | BNB | UP | 2.6 min | -0.153% | 1¢ | ❌ Lost | -$0.15 |
| 10/13 5:57:23 AM | NEAR | UP | 2.6 min | -0.903% | 1¢ | In play | — |
| 10/13 5:57:07 AM | PALLADIUM | UP | 2.9 min | — | 0¢ | In play | — |
| 10/13 5:56:52 AM | HYPE | UP | 3.1 min | -0.246% | 1¢ | In play | — |
| 10/13 5:56:21 AM | XRP | UP | 3.6 min | -0.316% | 1¢ | ❌ Lost | -$0.15 |
| 10/13 5:56:05 AM | BTC | UP | 3.9 min | -0.250% | 1¢ | ❌ Lost | -$0.15 |
| 10/13 5:56:05 AM | ETH | UP | 3.9 min | -0.294% | 1¢ | In play | — |
| 10/13 5:55:32 AM | ZEC | UP | 4.5 min | -0.764% | 1¢ | ❌ Lost | -$0.15 |
| 10/13 5:55:16 AM | WTI | DOWN | 4.7 min | — | 1¢ | In play | — |
| 10/13 5:55:16 AM | DOGE | UP | 4.7 min | -0.347% | 1¢ | In play | — |
| 10/13 5:54:14 AM | SOL | UP | 5.8 min | -0.631% | 1¢ | In play | — |
| 10/13 5:44:44 AM | BTC | DOWN | 15 sec | +0.036% | 0¢ | ❌ Lost | $0.00 |
| 10/13 5:44:28 AM | WTI | DOWN | 31 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/13 5:44:28 AM | DOGE | DOWN | 31 sec | +0.093% | 0¢ | ❌ Lost | $0.00 |
| 10/13 5:44:12 AM | AUDUSD | DOWN | 47 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/13 5:44:12 AM | SOL | DOWN | 47 sec | +0.088% | 0¢ | ❌ Lost | $0.00 |
| 10/13 5:44:12 AM | ZEC | UP | 47 sec | -0.167% | 0¢ | ❌ Lost | $0.00 |
| 10/13 5:44:12 AM | ETH | DOWN | 47 sec | +0.075% | 1¢ | ❌ Lost | -$0.15 |
| 10/13 5:43:56 AM | GBPUSD | DOWN | 63 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/13 5:43:41 AM | XRP | DOWN | 79 sec | +0.133% | 0¢ | ❌ Lost | $0.00 |
| 10/13 5:43:41 AM | EURUSD | DOWN | 79 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/13 5:43:09 AM | PLATINUM | DOWN | 1.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/13 5:43:09 AM | GOLD | DOWN | 1.9 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/13 5:43:09 AM | SILVER | DOWN | 1.9 min | — | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
