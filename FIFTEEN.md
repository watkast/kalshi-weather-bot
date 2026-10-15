# 15-Minute 1¢ Study

*Updated Wed Oct 14, 7:20 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 1441 finished bets | 1% | $92.55 | +58% | +6.42¢ | $34.60 / $57.95 |

*Expect about **86 buys a day** (~$12.88/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 1354 | $63.75 | +44% |
| Momentum model ≥ 2%, hold to the close | 2242 | $20.20 | +8% |
| Volatility model ≥ 2%, hold to the close | 2584 | $9.70 | +3% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 18622 | 18615 | 74 (0%) | 1.07% | -$1,219.25 (-54%) | Hold to the close: -$1,219.25 (-54%) |

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
| Volatility model | 12101 | 4.5% | 0.4% (52) | -636% | ❌ Worse |
| Momentum model | 12101 | 4.4% | 0.4% (52) | -661% | ❌ Worse |
| Mean-reversion model | 12101 | 7.3% | 0.4% (52) | -754% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 12101 | 52 | -46% | -88% | -88% | -86% |
| Volatility model ≥ 2% | 2584 | 23 | +3% | -78% | -77% | -73% |
| Volatility model ≥ 5% | 1441 | 18 | +58% | -73% | -71% | -66% |
| Volatility model ≥ 10% | 866 | 11 | +81% | -64% | -63% | -58% |
| Momentum model ≥ 2% | 2242 | 20 | +8% | -79% | -80% | -77% |
| Momentum model ≥ 5% | 1354 | 15 | +44% | -77% | -76% | -73% |
| Momentum model ≥ 10% | 914 | 10 | +54% | -70% | -70% | -65% |
| Mean-reversion model ≥ 2% | 4447 | 32 | -21% | -84% | -84% | -81% |
| Mean-reversion model ≥ 5% | 3047 | 25 | -9% | -82% | -81% | -77% |
| Mean-reversion model ≥ 10% | 2001 | 14 | -20% | -80% | -80% | -76% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 12299 | 4% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 4557 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 1759 | 2% | 1% | 1% | 1% | 0% | 0% |
| **All** | 18615 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 74 | 0% | -$1,219.25 | -54% | — |
| Sell at 2¢ | 653 | 4% | -$2,029.47 | -90% | 34 sec |
| Sell at 3¢ | 440 | 2% | -$2,027.65 | -90% | 46 sec |
| Sell at 5¢ | 322 | 2% | -$1,989.95 | -88% | 49 sec |
| Sell at 10¢ | 203 | 1% | -$1,905.32 | -84% | 63 sec |
| Sell at 25¢ | 118 | 1% | -$1,738.67 | -77% | 80 sec |
| Sell at 50¢ | 78 | 0% | -$1,532.75 | -68% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 579 | 5 | 10% | 3% | -18% | -82% | -87% |
| 2–5 min | 5996 | 35 | 7% | 3% | -42% | -88% | -88% |
| 1–2 min | 4861 | 18 | 3% | 2% | -60% | -94% | -93% |
| Under 1 min | 7175 | 16 | 1% | 0% | -68% | -90% | -90% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 1380 | 11 | 5% | 3% | -1% | -89% | -89% |
| HYPE | 1374 | 4 | 4% | 2% | -64% | -90% | -89% |
| ETH | 1370 | 8 | 5% | 3% | -29% | -88% | -87% |
| BNB | 1370 | 5 | 5% | 2% | -55% | -90% | -89% |
| DOGE | 1369 | 2 | 4% | 2% | -82% | -91% | -90% |
| SOL | 1366 | 2 | 3% | 1% | -82% | -93% | -92% |
| BTC | 1358 | 7 | 5% | 2% | -31% | -88% | -91% |
| XRP | 1357 | 7 | 2% | 1% | -36% | -86% | -86% |
| NEAR | 1355 | 8 | 5% | 3% | -23% | -77% | -78% |
| GOLD | 742 | 1 | 4% | 1% | -84% | -91% | -93% |
| SILVER | 725 | 4 | 3% | 1% | -36% | -78% | -77% |
| WTI | 698 | 3 | 3% | 1% | -50% | -94% | -96% |
| COPPER | 643 | 1 | 2% | 2% | -85% | -97% | -96% |
| PLATINUM | 615 | 0 | 1% | 0% | -100% | -99% | -98% |
| NATGAS | 567 | 3 | 2% | 2% | -51% | -96% | -95% |
| PALLADIUM | 567 | 1 | 1% | 0% | -84% | -98% | -98% |
| EURUSD | 550 | 3 | 3% | 1% | -49% | -79% | -78% |
| GBPUSD | 519 | 1 | 2% | 1% | -82% | -97% | -96% |
| USDJPY | 473 | 3 | 1% | 1% | -41% | -99% | -98% |
| AUDUSD | 112 | 0 | 1% | 0% | -100% | -98% | -98% |
| USDCAD | 105 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 9399 | 38 | 3% | 2% | -53% | -89% | -88% |
| DOWN (bought NO) | 9216 | 36 | 4% | 2% | -55% | -91% | -92% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 2115 | 11 | 2% | 1% | -13% | -78% | -78% |
| 0.05–0.1% | 2167 | 7 | 3% | 1% | -53% | -92% | -91% |
| 0.1–0.2% | 3123 | 10 | 4% | 2% | -60% | -90% | -90% |
| 0.2–0.5% | 3536 | 20 | 6% | 3% | -38% | -88% | -88% |
| Over 0.5% | 1355 | 6 | 6% | 2% | -54% | -89% | -90% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 4717 | 20 | 4% | 2% | -52% | -87% | -88% |
| Morning (6am–12pm) | 4329 | 23 | 4% | 2% | -38% | -91% | -91% |
| Afternoon (12–6pm) | 4482 | 16 | 3% | 1% | -58% | -87% | -88% |
| Evening (6pm–12am) | 5087 | 15 | 3% | 2% | -66% | -94% | -93% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 25 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,496 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/14 7:14:48 PM | DOGE | UP | 12 sec | -0.064% | 0¢ | ❌ Lost | $0.00 |
| 10/14 7:14:48 PM | PALLADIUM | DOWN | 12 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 7:14:30 PM | WTI | UP | 30 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/14 7:14:30 PM | NATGAS | UP | 30 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 7:14:30 PM | NEAR | UP | 30 sec | -0.360% | 0¢ | ❌ Lost | $0.00 |
| 10/14 7:14:30 PM | COPPER | DOWN | 30 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 7:14:30 PM | GOLD | DOWN | 30 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/14 7:14:30 PM | ZEC | UP | 30 sec | -0.179% | 0¢ | ❌ Lost | $0.00 |
| 10/14 7:14:14 PM | BTC | DOWN | 46 sec | +0.131% | 0¢ | ❌ Lost | $0.00 |
| 10/14 7:13:58 PM | HYPE | UP | 62 sec | -0.163% | 0¢ | ❌ Lost | -$0.15 |
| 10/14 7:13:43 PM | XRP | UP | 76 sec | -0.158% | 1¢ | ❌ Lost | -$0.15 |
| 10/14 7:13:43 PM | GBPUSD | DOWN | 76 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 7:13:25 PM | USDJPY | UP | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 7:12:22 PM | USDCAD | UP | 2.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 7:11:16 PM | EURUSD | DOWN | 3.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 7:10:29 PM | BNB | DOWN | 4.5 min | +0.186% | 41¢ | ❌ Lost | $0.00 |
| 10/14 6:59:52 PM | XRP | UP | 8 sec | -0.023% | 0¢ | ❌ Lost | $0.00 |
| 10/14 6:59:52 PM | AUDUSD | UP | 8 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 6:59:37 PM | GBPUSD | UP | 23 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 6:59:37 PM | ETH | UP | 23 sec | -0.048% | 0¢ | ❌ Lost | $0.00 |
| 10/14 6:59:37 PM | BNB | DOWN | 23 sec | +0.032% | 0¢ | ❌ Lost | $0.00 |
| 10/14 6:59:37 PM | WTI | UP | 23 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/14 6:59:37 PM | BTC | DOWN | 23 sec | +0.071% | 0¢ | ❌ Lost | $0.00 |
| 10/14 6:59:18 PM | HYPE | UP | 41 sec | -0.064% | 1¢ | ❌ Lost | -$0.15 |
| 10/14 6:59:18 PM | SOL | UP | 41 sec | -0.058% | 0¢ | ❌ Lost | -$0.15 |
| 10/14 6:59:02 PM | GOLD | UP | 57 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/14 6:59:02 PM | NEAR | DOWN | 57 sec | +0.241% | 1¢ | ❌ Lost | -$0.15 |
| 10/14 6:58:46 PM | ZEC | DOWN | 73 sec | +0.300% | 0¢ | ❌ Lost | -$0.15 |
| 10/14 6:58:30 PM | NATGAS | UP | 1.5 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 6:58:30 PM | USDJPY | DOWN | 1.5 min | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
