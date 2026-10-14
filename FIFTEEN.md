# 15-Minute 1¢ Study

*Updated Wed Oct 14, 5:02 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 1433 finished bets | 1% | $79.60 | +50% | +5.55¢ | $35.20 / $44.40 |

*Expect about **86 buys a day** (~$12.89/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 1346 | $50.65 | +35% |
| Momentum model ≥ 2%, hold to the close | 2225 | $8.30 | +3% |
| Volatility model ≥ 2%, hold to the close | 2568 | -$2.20 | -1% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 18478 | 18471 | 72 (0%) | 1.07% | -$1,230.60 (-55%) | Hold to the close: -$1,230.60 (-55%) |

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
| Volatility model | 12025 | 4.5% | 0.4% (51) | -645% | ❌ Worse |
| Momentum model | 12025 | 4.4% | 0.4% (51) | -671% | ❌ Worse |
| Mean-reversion model | 12025 | 7.3% | 0.4% (51) | -765% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 12025 | 51 | -47% | -88% | -88% | -86% |
| Volatility model ≥ 2% | 2568 | 22 | -1% | -78% | -78% | -74% |
| Volatility model ≥ 5% | 1433 | 17 | +50% | -73% | -71% | -67% |
| Volatility model ≥ 10% | 861 | 10 | +65% | -64% | -63% | -59% |
| Momentum model ≥ 2% | 2225 | 19 | +3% | -80% | -80% | -77% |
| Momentum model ≥ 5% | 1346 | 14 | +35% | -77% | -77% | -74% |
| Momentum model ≥ 10% | 908 | 9 | +40% | -70% | -70% | -66% |
| Mean-reversion model ≥ 2% | 4422 | 31 | -23% | -84% | -85% | -81% |
| Mean-reversion model ≥ 5% | 3031 | 24 | -12% | -82% | -82% | -78% |
| Mean-reversion model ≥ 10% | 1996 | 14 | -19% | -80% | -80% | -76% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 12223 | 4% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 4518 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 1730 | 2% | 1% | 1% | 1% | 0% | 0% |
| **All** | 18471 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 72 | 0% | -$1,230.60 | -55% | — |
| Sell at 2¢ | 648 | 4% | -$2,014.12 | -90% | 34 sec |
| Sell at 3¢ | 435 | 2% | -$2,012.95 | -90% | 46 sec |
| Sell at 5¢ | 317 | 2% | -$1,976.55 | -88% | 49 sec |
| Sell at 10¢ | 200 | 1% | -$1,892.60 | -85% | 64 sec |
| Sell at 25¢ | 116 | 1% | -$1,742.64 | -78% | 80 sec |
| Sell at 50¢ | 77 | 0% | -$1,536.85 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 579 | 5 | 10% | 3% | -18% | -82% | -87% |
| 2–5 min | 5958 | 35 | 7% | 3% | -42% | -88% | -88% |
| 1–2 min | 4824 | 18 | 3% | 2% | -59% | -94% | -93% |
| Under 1 min | 7106 | 14 | 1% | 0% | -71% | -90% | -90% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 1371 | 11 | 5% | 3% | -0% | -89% | -89% |
| HYPE | 1365 | 4 | 4% | 2% | -64% | -90% | -89% |
| ETH | 1362 | 8 | 5% | 3% | -28% | -88% | -87% |
| DOGE | 1362 | 2 | 4% | 2% | -82% | -91% | -90% |
| BNB | 1361 | 5 | 4% | 2% | -55% | -90% | -90% |
| SOL | 1358 | 2 | 3% | 1% | -82% | -93% | -92% |
| BTC | 1349 | 6 | 5% | 2% | -41% | -88% | -91% |
| XRP | 1348 | 7 | 2% | 1% | -36% | -86% | -86% |
| NEAR | 1347 | 8 | 5% | 3% | -22% | -77% | -78% |
| GOLD | 733 | 1 | 4% | 1% | -84% | -91% | -93% |
| SILVER | 720 | 3 | 3% | 1% | -51% | -78% | -78% |
| WTI | 691 | 3 | 3% | 1% | -50% | -94% | -96% |
| COPPER | 638 | 1 | 2% | 2% | -85% | -97% | -96% |
| PLATINUM | 610 | 0 | 1% | 0% | -100% | -99% | -98% |
| PALLADIUM | 565 | 1 | 1% | 0% | -83% | -98% | -98% |
| NATGAS | 561 | 3 | 2% | 2% | -50% | -96% | -95% |
| EURUSD | 546 | 3 | 3% | 1% | -49% | -78% | -78% |
| GBPUSD | 513 | 1 | 2% | 1% | -82% | -97% | -96% |
| USDJPY | 466 | 3 | 1% | 1% | -40% | -99% | -98% |
| AUDUSD | 106 | 0 | 1% | 0% | -100% | -98% | -98% |
| USDCAD | 99 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 9322 | 36 | 3% | 2% | -55% | -89% | -88% |
| DOWN (bought NO) | 9149 | 36 | 4% | 2% | -54% | -91% | -92% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 2101 | 10 | 2% | 1% | -20% | -78% | -78% |
| 0.05–0.1% | 2150 | 7 | 3% | 1% | -53% | -92% | -91% |
| 0.1–0.2% | 3104 | 10 | 4% | 2% | -60% | -91% | -91% |
| 0.2–0.5% | 3511 | 20 | 6% | 3% | -37% | -88% | -88% |
| Over 0.5% | 1354 | 6 | 6% | 2% | -54% | -89% | -90% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 4717 | 20 | 4% | 2% | -52% | -87% | -88% |
| Morning (6am–12pm) | 4329 | 23 | 4% | 2% | -38% | -91% | -91% |
| Afternoon (12–6pm) | 4421 | 14 | 3% | 1% | -63% | -87% | -88% |
| Evening (6pm–12am) | 5004 | 15 | 3% | 2% | -66% | -94% | -93% |

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
| 10/14 4:59:34 PM | WTI | UP | 26 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 4:58:27 PM | SILVER | UP | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 4:58:08 PM | HYPE | DOWN | 1.9 min | +0.185% | 1¢ | ❌ Lost | -$0.15 |
| 10/14 4:58:08 PM | GOLD | UP | 1.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 4:56:47 PM | NEAR | DOWN | 3.2 min | +0.469% | 3¢ | ❌ Lost | -$0.15 |
| 10/14 4:56:47 PM | XRP | DOWN | 3.2 min | +0.203% | 1¢ | ❌ Lost | -$0.15 |
| 10/14 4:56:47 PM | GBPUSD | DOWN | 3.2 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 4:56:31 PM | SOL | DOWN | 3.5 min | +0.420% | 1¢ | ❌ Lost | -$0.15 |
| 10/14 4:56:15 PM | USDCAD | UP | 3.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 4:56:15 PM | EURUSD | DOWN | 3.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 4:55:56 PM | BTC | DOWN | 4.0 min | +0.211% | 1¢ | ❌ Lost | -$0.15 |
| 10/14 4:55:40 PM | ZEC | DOWN | 4.3 min | +0.523% | 1¢ | ❌ Lost | -$0.15 |
| 10/14 4:55:24 PM | ETH | DOWN | 4.6 min | +0.305% | 1¢ | ❌ Lost | -$0.15 |
| 10/14 4:55:24 PM | DOGE | DOWN | 4.6 min | +0.348% | 1¢ | ❌ Lost | -$0.15 |
| 10/14 4:51:48 PM | BNB | DOWN | 8.2 min | +0.238% | 1¢ | ❌ Lost | -$0.15 |
| 10/14 4:44:55 PM | PLATINUM | DOWN | 5 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 4:44:55 PM | ZEC | DOWN | 5 sec | +0.034% | 0¢ | ❌ Lost | -$0.15 |
| 10/14 4:44:38 PM | SILVER | UP | 21 sec | — | 1¢ | ✅ Won | $13.85 |
| 10/14 4:44:06 PM | SOL | UP | 54 sec | -0.124% | 0¢ | ❌ Lost | -$0.15 |
| 10/14 4:44:06 PM | GOLD | DOWN | 54 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/14 4:43:50 PM | USDCAD | UP | 70 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 4:43:50 PM | NEAR | DOWN | 70 sec | +0.313% | 1¢ | ❌ Lost | -$0.15 |
| 10/14 4:43:13 PM | ETH | UP | 1.8 min | -0.211% | 0¢ | ❌ Lost | -$0.15 |
| 10/14 4:43:13 PM | EURUSD | DOWN | 1.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 4:43:13 PM | USDJPY | UP | 1.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 4:43:13 PM | COPPER | UP | 1.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 4:42:57 PM | DOGE | UP | 2.0 min | -0.279% | 1¢ | ❌ Lost | -$0.15 |
| 10/14 4:42:41 PM | BNB | UP | 2.3 min | -0.147% | 0¢ | ❌ Lost | $0.00 |
| 10/14 4:42:41 PM | BTC | UP | 2.3 min | -0.198% | 1¢ | ❌ Lost | -$0.15 |
| 10/14 4:42:26 PM | HYPE | UP | 2.5 min | -0.353% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
