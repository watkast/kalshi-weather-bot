# 15-Minute 1¢ Study

*Updated Wed Oct 14, 8:52 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 1446 finished bets | 1% | $91.80 | +57% | +6.35¢ | $34.45 / $57.35 |

*Expect about **86 buys a day** (~$12.88/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 1358 | $63.15 | +43% |
| Momentum model ≥ 2%, hold to the close | 2254 | $18.55 | +7% |
| Volatility model ≥ 2%, hold to the close | 2601 | $7.30 | +2% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 18723 | 18716 | 74 (0%) | 1.07% | -$1,232.75 (-54%) | Hold to the close: -$1,232.75 (-54%) |

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
| Volatility model | 12154 | 4.5% | 0.4% (52) | -635% | ❌ Worse |
| Momentum model | 12154 | 4.4% | 0.4% (52) | -660% | ❌ Worse |
| Mean-reversion model | 12154 | 7.3% | 0.4% (52) | -754% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 12154 | 52 | -46% | -88% | -88% | -86% |
| Volatility model ≥ 2% | 2601 | 23 | +2% | -78% | -77% | -73% |
| Volatility model ≥ 5% | 1446 | 18 | +57% | -73% | -71% | -67% |
| Volatility model ≥ 10% | 866 | 11 | +81% | -64% | -63% | -58% |
| Momentum model ≥ 2% | 2254 | 20 | +7% | -80% | -80% | -77% |
| Momentum model ≥ 5% | 1358 | 15 | +43% | -76% | -76% | -73% |
| Momentum model ≥ 10% | 915 | 10 | +54% | -70% | -70% | -65% |
| Mean-reversion model ≥ 2% | 4472 | 32 | -22% | -84% | -85% | -81% |
| Mean-reversion model ≥ 5% | 3060 | 25 | -10% | -82% | -82% | -78% |
| Mean-reversion model ≥ 10% | 2009 | 14 | -20% | -80% | -80% | -76% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 12352 | 4% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 4585 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 1779 | 2% | 1% | 1% | 1% | 0% | 0% |
| **All** | 18716 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 74 | 0% | -$1,232.75 | -54% | — |
| Sell at 2¢ | 657 | 4% | -$2,041.93 | -90% | 34 sec |
| Sell at 3¢ | 442 | 2% | -$2,040.37 | -90% | 46 sec |
| Sell at 5¢ | 323 | 2% | -$2,002.80 | -88% | 49 sec |
| Sell at 10¢ | 203 | 1% | -$1,918.82 | -85% | 63 sec |
| Sell at 25¢ | 118 | 1% | -$1,752.17 | -77% | 80 sec |
| Sell at 50¢ | 78 | 0% | -$1,546.25 | -68% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 585 | 5 | 10% | 3% | -19% | -82% | -87% |
| 2–5 min | 6038 | 35 | 7% | 3% | -43% | -88% | -88% |
| 1–2 min | 4882 | 18 | 3% | 2% | -60% | -94% | -93% |
| Under 1 min | 7207 | 16 | 1% | 0% | -68% | -90% | -90% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 1386 | 11 | 5% | 3% | -1% | -89% | -89% |
| HYPE | 1379 | 4 | 4% | 2% | -64% | -90% | -89% |
| ETH | 1376 | 8 | 5% | 3% | -29% | -88% | -87% |
| BNB | 1376 | 5 | 5% | 2% | -56% | -90% | -89% |
| DOGE | 1375 | 2 | 4% | 2% | -82% | -91% | -90% |
| SOL | 1372 | 2 | 3% | 1% | -82% | -93% | -92% |
| BTC | 1364 | 7 | 5% | 2% | -31% | -88% | -91% |
| XRP | 1363 | 7 | 2% | 1% | -37% | -86% | -86% |
| NEAR | 1361 | 8 | 5% | 2% | -23% | -77% | -78% |
| GOLD | 747 | 1 | 4% | 1% | -84% | -92% | -93% |
| SILVER | 729 | 4 | 3% | 1% | -36% | -78% | -77% |
| WTI | 701 | 3 | 3% | 1% | -50% | -94% | -96% |
| COPPER | 647 | 1 | 2% | 2% | -86% | -97% | -96% |
| PLATINUM | 620 | 0 | 1% | 0% | -100% | -99% | -98% |
| NATGAS | 571 | 3 | 2% | 2% | -51% | -96% | -95% |
| PALLADIUM | 570 | 1 | 1% | 0% | -84% | -98% | -98% |
| EURUSD | 556 | 3 | 3% | 1% | -50% | -79% | -78% |
| GBPUSD | 523 | 1 | 2% | 1% | -82% | -97% | -97% |
| USDJPY | 476 | 3 | 1% | 1% | -41% | -99% | -98% |
| AUDUSD | 117 | 0 | 1% | 0% | -100% | -99% | -98% |
| USDCAD | 107 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 9462 | 38 | 3% | 2% | -54% | -89% | -88% |
| DOWN (bought NO) | 9254 | 36 | 4% | 2% | -55% | -91% | -92% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 2115 | 11 | 2% | 1% | -13% | -78% | -78% |
| 0.05–0.1% | 2167 | 7 | 3% | 1% | -53% | -92% | -91% |
| 0.1–0.2% | 3129 | 10 | 4% | 2% | -60% | -90% | -90% |
| 0.2–0.5% | 3559 | 20 | 6% | 3% | -38% | -88% | -88% |
| Over 0.5% | 1379 | 6 | 6% | 2% | -55% | -88% | -90% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 4717 | 20 | 4% | 2% | -52% | -87% | -88% |
| Morning (6am–12pm) | 4329 | 23 | 4% | 2% | -38% | -91% | -91% |
| Afternoon (12–6pm) | 4482 | 16 | 3% | 1% | -58% | -87% | -88% |
| Evening (6pm–12am) | 5188 | 15 | 3% | 2% | -67% | -94% | -93% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 25 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,506 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/14 8:44:53 PM | GOLD | DOWN | 6 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 8:44:53 PM | SILVER | DOWN | 6 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/14 8:44:21 PM | COPPER | DOWN | 38 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 8:43:15 PM | NATGAS | DOWN | 1.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 8:43:00 PM | AUDUSD | DOWN | 2.0 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 8:43:00 PM | EURUSD | DOWN | 2.0 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 8:42:44 PM | GBPUSD | DOWN | 2.3 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 8:41:41 PM | BTC | DOWN | 3.3 min | +0.719% | 1¢ | ❌ Lost | $0.00 |
| 10/14 8:41:20 PM | HYPE | DOWN | 3.7 min | +0.843% | 1¢ | ❌ Lost | -$0.15 |
| 10/14 8:41:04 PM | BNB | DOWN | 3.9 min | +0.670% | 1¢ | ❌ Lost | -$0.15 |
| 10/14 8:41:04 PM | DOGE | DOWN | 3.9 min | +1.364% | 1¢ | ❌ Lost | -$0.15 |
| 10/14 8:41:04 PM | SOL | DOWN | 3.9 min | +1.267% | 1¢ | ❌ Lost | -$0.15 |
| 10/14 8:41:04 PM | ZEC | DOWN | 3.9 min | +1.861% | 1¢ | ❌ Lost | -$0.15 |
| 10/14 8:40:17 PM | NEAR | DOWN | 4.7 min | +1.244% | 2¢ | ❌ Lost | -$0.15 |
| 10/14 8:40:17 PM | XRP | DOWN | 4.7 min | +0.965% | 1¢ | ❌ Lost | -$0.15 |
| 10/14 8:40:17 PM | ETH | DOWN | 4.7 min | +1.237% | 1¢ | ❌ Lost | -$0.15 |
| 10/14 8:29:51 PM | WTI | DOWN | 9 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 8:29:35 PM | PLATINUM | UP | 25 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 8:29:19 PM | GOLD | UP | 41 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/14 8:29:04 PM | SILVER | UP | 55 sec | — | 1¢ | ❌ Lost | $0.00 |
| 10/14 8:28:48 PM | NEAR | UP | 71 sec | -1.497% | 0¢ | ❌ Lost | -$0.15 |
| 10/14 8:28:16 PM | EURUSD | UP | 1.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 8:27:44 PM | HYPE | UP | 2.3 min | -0.850% | 1¢ | ❌ Lost | -$0.15 |
| 10/14 8:27:44 PM | GBPUSD | UP | 2.3 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 8:27:28 PM | AUDUSD | UP | 2.5 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 8:27:28 PM | USDJPY | DOWN | 2.5 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 8:26:38 PM | BTC | UP | 3.4 min | -0.806% | 2¢ | ❌ Lost | -$0.15 |
| 10/14 8:24:47 PM | BNB | UP | 5.2 min | -1.683% | 1¢ | ❌ Lost | -$0.15 |
| 10/14 8:24:29 PM | DOGE | UP | 5.5 min | -2.656% | 2¢ | ❌ Lost | -$0.15 |
| 10/14 8:24:29 PM | SOL | UP | 5.5 min | -1.968% | 2¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
