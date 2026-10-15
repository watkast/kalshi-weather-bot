# 15-Minute 1¢ Study

*Updated Wed Oct 14, 8:01 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 1444 finished bets | 1% | $92.10 | +58% | +6.38¢ | $34.45 / $57.65 |

*Expect about **86 buys a day** (~$12.89/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 1358 | $63.15 | +43% |
| Momentum model ≥ 2%, hold to the close | 2253 | $18.70 | +7% |
| Volatility model ≥ 2%, hold to the close | 2595 | $8.20 | +3% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 18670 | 18663 | 74 (0%) | 1.07% | -$1,226.15 (-54%) | Hold to the close: -$1,226.15 (-54%) |

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
| Volatility model | 12127 | 4.5% | 0.4% (52) | -635% | ❌ Worse |
| Momentum model | 12127 | 4.4% | 0.4% (52) | -661% | ❌ Worse |
| Mean-reversion model | 12127 | 7.3% | 0.4% (52) | -754% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 12127 | 52 | -46% | -88% | -88% | -86% |
| Volatility model ≥ 2% | 2595 | 23 | +3% | -78% | -77% | -73% |
| Volatility model ≥ 5% | 1444 | 18 | +58% | -73% | -71% | -66% |
| Volatility model ≥ 10% | 866 | 11 | +81% | -64% | -63% | -58% |
| Momentum model ≥ 2% | 2253 | 20 | +7% | -80% | -80% | -77% |
| Momentum model ≥ 5% | 1358 | 15 | +43% | -76% | -76% | -73% |
| Momentum model ≥ 10% | 915 | 10 | +54% | -70% | -70% | -65% |
| Mean-reversion model ≥ 2% | 4462 | 32 | -22% | -84% | -85% | -81% |
| Mean-reversion model ≥ 5% | 3052 | 25 | -9% | -82% | -82% | -77% |
| Mean-reversion model ≥ 10% | 2002 | 14 | -20% | -80% | -80% | -76% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 12325 | 4% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 4571 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 1767 | 2% | 1% | 1% | 1% | 0% | 0% |
| **All** | 18663 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 74 | 0% | -$1,226.15 | -54% | — |
| Sell at 2¢ | 654 | 4% | -$2,036.11 | -90% | 34 sec |
| Sell at 3¢ | 441 | 2% | -$2,034.16 | -90% | 46 sec |
| Sell at 5¢ | 323 | 2% | -$1,996.20 | -88% | 49 sec |
| Sell at 10¢ | 203 | 1% | -$1,912.22 | -85% | 63 sec |
| Sell at 25¢ | 118 | 1% | -$1,745.57 | -77% | 80 sec |
| Sell at 50¢ | 78 | 0% | -$1,539.65 | -68% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 579 | 5 | 10% | 3% | -18% | -82% | -87% |
| 2–5 min | 6018 | 35 | 7% | 3% | -43% | -88% | -88% |
| 1–2 min | 4871 | 18 | 3% | 2% | -60% | -94% | -93% |
| Under 1 min | 7191 | 16 | 1% | 0% | -68% | -90% | -90% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 1383 | 11 | 5% | 3% | -1% | -89% | -89% |
| HYPE | 1376 | 4 | 4% | 2% | -64% | -90% | -89% |
| ETH | 1373 | 8 | 5% | 3% | -29% | -88% | -87% |
| BNB | 1373 | 5 | 5% | 2% | -55% | -90% | -89% |
| DOGE | 1372 | 2 | 4% | 2% | -82% | -91% | -90% |
| SOL | 1369 | 2 | 3% | 1% | -82% | -93% | -92% |
| BTC | 1361 | 7 | 5% | 2% | -31% | -88% | -91% |
| XRP | 1360 | 7 | 2% | 1% | -36% | -86% | -86% |
| NEAR | 1358 | 8 | 5% | 3% | -23% | -77% | -78% |
| GOLD | 744 | 1 | 4% | 1% | -84% | -92% | -93% |
| SILVER | 726 | 4 | 3% | 1% | -36% | -78% | -77% |
| WTI | 699 | 3 | 3% | 1% | -50% | -94% | -96% |
| COPPER | 646 | 1 | 2% | 2% | -86% | -97% | -96% |
| PLATINUM | 618 | 0 | 1% | 0% | -100% | -99% | -98% |
| NATGAS | 569 | 3 | 2% | 2% | -51% | -96% | -95% |
| PALLADIUM | 569 | 1 | 1% | 0% | -84% | -98% | -98% |
| EURUSD | 553 | 3 | 3% | 1% | -49% | -79% | -78% |
| GBPUSD | 520 | 1 | 2% | 1% | -82% | -97% | -96% |
| USDJPY | 474 | 3 | 1% | 1% | -41% | -99% | -98% |
| AUDUSD | 114 | 0 | 1% | 0% | -100% | -98% | -98% |
| USDCAD | 106 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 9434 | 38 | 3% | 2% | -54% | -89% | -88% |
| DOWN (bought NO) | 9229 | 36 | 4% | 2% | -55% | -91% | -92% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 2115 | 11 | 2% | 1% | -13% | -78% | -78% |
| 0.05–0.1% | 2167 | 7 | 3% | 1% | -53% | -92% | -91% |
| 0.1–0.2% | 3127 | 10 | 4% | 2% | -60% | -90% | -90% |
| 0.2–0.5% | 3552 | 20 | 6% | 3% | -38% | -88% | -88% |
| Over 0.5% | 1361 | 6 | 6% | 2% | -54% | -89% | -90% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 4717 | 20 | 4% | 2% | -52% | -87% | -88% |
| Morning (6am–12pm) | 4329 | 23 | 4% | 2% | -38% | -91% | -91% |
| Afternoon (12–6pm) | 4482 | 16 | 3% | 1% | -58% | -87% | -88% |
| Evening (6pm–12am) | 5135 | 15 | 3% | 2% | -67% | -94% | -93% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 25 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,503 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/14 7:59:53 PM | PLATINUM | UP | 7 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 7:59:21 PM | AUDUSD | UP | 39 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 7:59:21 PM | USDJPY | DOWN | 39 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 7:59:21 PM | EURUSD | UP | 39 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 7:59:04 PM | GBPUSD | UP | 55 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 7:58:16 PM | BNB | UP | 1.7 min | -0.191% | 0¢ | ❌ Lost | -$0.15 |
| 10/14 7:58:00 PM | DOGE | UP | 2.0 min | -0.272% | 1¢ | ❌ Lost | -$0.15 |
| 10/14 7:58:00 PM | HYPE | UP | 2.0 min | -0.196% | 1¢ | ❌ Lost | -$0.15 |
| 10/14 7:57:43 PM | XRP | UP | 2.3 min | -0.234% | 1¢ | ❌ Lost | -$0.15 |
| 10/14 7:57:43 PM | BTC | UP | 2.3 min | -0.168% | 1¢ | ❌ Lost | -$0.15 |
| 10/14 7:57:27 PM | NEAR | UP | 2.5 min | -0.579% | 1¢ | ❌ Lost | -$0.15 |
| 10/14 7:57:11 PM | ETH | UP | 2.8 min | -0.253% | 1¢ | ❌ Lost | -$0.15 |
| 10/14 7:56:55 PM | SOL | UP | 3.1 min | -0.303% | 1¢ | ❌ Lost | -$0.15 |
| 10/14 7:56:55 PM | NATGAS | UP | 3.1 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 7:56:55 PM | COPPER | UP | 3.1 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/14 7:56:55 PM | USDCAD | DOWN | 3.1 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 7:56:23 PM | ZEC | UP | 3.6 min | -0.503% | 1¢ | ❌ Lost | -$0.15 |
| 10/14 7:55:51 PM | WTI | UP | 4.2 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/14 7:44:50 PM | NATGAS | UP | 10 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 7:44:50 PM | PALLADIUM | DOWN | 10 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 7:44:34 PM | COPPER | UP | 26 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 7:44:03 PM | PLATINUM | UP | 56 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 7:44:03 PM | EURUSD | UP | 56 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 7:44:03 PM | SILVER | UP | 56 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/14 7:43:47 PM | GOLD | UP | 72 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/14 7:42:09 PM | NEAR | DOWN | 2.9 min | +0.867% | 1¢ | ❌ Lost | $0.00 |
| 10/14 7:42:09 PM | ZEC | DOWN | 2.9 min | +0.576% | 5¢ | ❌ Lost | -$0.15 |
| 10/14 7:41:54 PM | XRP | DOWN | 3.1 min | +0.393% | 1¢ | ❌ Lost | -$0.15 |
| 10/14 7:41:20 PM | DOGE | DOWN | 3.7 min | +0.429% | 1¢ | ❌ Lost | -$0.15 |
| 10/14 7:41:04 PM | BNB | DOWN | 3.9 min | +0.202% | 1¢ | ❌ Lost | $0.00 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
