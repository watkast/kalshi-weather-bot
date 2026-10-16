# 15-Minute 1¢ Study

*Updated Fri Oct 16, 2:58 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 1599 finished bets | 1% | $74.25 | +42% | +4.64¢ | $39.75 / $34.50 |

*Expect about **88 buys a day** (~$13.26/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 1486 | $48.90 | +30% |
| Momentum model ≥ 2%, hold to the close | 2498 | -$9.80 | -3% |
| Volatility model ≥ 5%, sell at 50¢ | 1599 | -$21.00 | -12% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 20496 | 20481 | 79 (0%) | 1.07% | -$1,385.65 (-56%) | Hold to the close: -$1,385.65 (-56%) |

*In play or awaiting result: 14. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 13126 | 4.4% | 0.4% (53) | -643% | ❌ Worse |
| Momentum model | 13126 | 4.4% | 0.4% (53) | -667% | ❌ Worse |
| Mean-reversion model | 13126 | 7.3% | 0.4% (53) | -769% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 13126 | 53 | -49% | -88% | -88% | -86% |
| Volatility model ≥ 2% | 2911 | 23 | -9% | -79% | -78% | -74% |
| Volatility model ≥ 5% | 1599 | 18 | +42% | -74% | -73% | -68% |
| Volatility model ≥ 10% | 937 | 11 | +67% | -65% | -64% | -60% |
| Momentum model ≥ 2% | 2498 | 20 | -3% | -80% | -81% | -77% |
| Momentum model ≥ 5% | 1486 | 15 | +30% | -77% | -77% | -74% |
| Momentum model ≥ 10% | 993 | 10 | +41% | -72% | -71% | -66% |
| Mean-reversion model ≥ 2% | 4921 | 33 | -27% | -84% | -84% | -81% |
| Mean-reversion model ≥ 5% | 3383 | 26 | -15% | -82% | -82% | -78% |
| Mean-reversion model ≥ 10% | 2216 | 15 | -22% | -80% | -80% | -77% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 13324 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 5070 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 2087 | 2% | 1% | 1% | 1% | 0% | 0% |
| **All** | 20481 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 79 | 0% | -$1,385.65 | -56% | — |
| Sell at 2¢ | 722 | 4% | -$2,205.93 | -89% | 42 sec |
| Sell at 3¢ | 483 | 2% | -$2,205.28 | -89% | 47 sec |
| Sell at 5¢ | 352 | 2% | -$2,164.85 | -87% | 50 sec |
| Sell at 10¢ | 217 | 1% | -$2,081.38 | -84% | 63 sec |
| Sell at 25¢ | 125 | 1% | -$1,909.90 | -77% | 80 sec |
| Sell at 50¢ | 82 | 0% | -$1,700.15 | -68% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 660 | 5 | 11% | 3% | -28% | -81% | -86% |
| 2–5 min | 6638 | 36 | 7% | 3% | -46% | -88% | -88% |
| 1–2 min | 5331 | 20 | 3% | 2% | -59% | -92% | -92% |
| Under 1 min | 7848 | 18 | 1% | 0% | -67% | -87% | -87% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 1495 | 11 | 5% | 3% | -9% | -89% | -90% |
| HYPE | 1491 | 5 | 4% | 2% | -59% | -90% | -89% |
| ETH | 1485 | 8 | 5% | 3% | -35% | -88% | -87% |
| BNB | 1483 | 5 | 4% | 2% | -59% | -90% | -90% |
| DOGE | 1482 | 2 | 4% | 2% | -83% | -91% | -90% |
| SOL | 1478 | 2 | 3% | 2% | -83% | -92% | -91% |
| XRP | 1473 | 7 | 3% | 1% | -41% | -86% | -86% |
| BTC | 1470 | 7 | 5% | 2% | -36% | -88% | -91% |
| NEAR | 1467 | 8 | 5% | 3% | -29% | -78% | -79% |
| GOLD | 827 | 1 | 4% | 1% | -86% | -92% | -94% |
| SILVER | 805 | 4 | 3% | 1% | -43% | -79% | -80% |
| WTI | 773 | 3 | 3% | 1% | -55% | -94% | -96% |
| COPPER | 708 | 2 | 2% | 1% | -74% | -84% | -83% |
| PLATINUM | 687 | 0 | 1% | 0% | -100% | -99% | -98% |
| PALLADIUM | 637 | 2 | 1% | 0% | -71% | -83% | -84% |
| NATGAS | 633 | 5 | 2% | 2% | -26% | -81% | -80% |
| EURUSD | 627 | 3 | 3% | 1% | -55% | -80% | -80% |
| GBPUSD | 588 | 1 | 2% | 1% | -84% | -97% | -96% |
| USDJPY | 553 | 3 | 1% | 1% | -49% | -99% | -98% |
| AUDUSD | 171 | 0 | 1% | 0% | -100% | -99% | -98% |
| USDCAD | 148 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 10311 | 39 | 4% | 2% | -57% | -89% | -89% |
| DOWN (bought NO) | 10170 | 40 | 4% | 2% | -55% | -88% | -88% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 2215 | 11 | 2% | 1% | -17% | -79% | -78% |
| 0.05–0.1% | 2307 | 7 | 3% | 1% | -56% | -92% | -92% |
| 0.1–0.2% | 3375 | 10 | 4% | 2% | -63% | -90% | -90% |
| 0.2–0.5% | 3891 | 21 | 6% | 3% | -41% | -88% | -88% |
| Over 0.5% | 1533 | 6 | 6% | 2% | -59% | -88% | -89% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 5156 | 20 | 4% | 2% | -56% | -87% | -88% |
| Morning (6am–12pm) | 4701 | 26 | 4% | 2% | -36% | -86% | -86% |
| Afternoon (12–6pm) | 4822 | 16 | 3% | 1% | -61% | -88% | -89% |
| Evening (6pm–12am) | 5802 | 17 | 3% | 2% | -67% | -92% | -91% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,446 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/16 2:58:25 AM | GOLD | DOWN | 1.6 min | — | — | In play | — |
| 10/16 2:58:25 AM | USDCAD | UP | 1.6 min | — | — | In play | — |
| 10/16 2:58:11 AM | GBPUSD | DOWN | 1.8 min | — | — | In play | — |
| 10/16 2:57:55 AM | ZEC | UP | 2.1 min | -0.337% | — | In play | — |
| 10/16 2:57:55 AM | SILVER | DOWN | 2.1 min | — | — | In play | — |
| 10/16 2:57:23 AM | PALLADIUM | UP | 2.6 min | — | — | In play | — |
| 10/16 2:57:07 AM | PLATINUM | UP | 2.9 min | — | — | In play | — |
| 10/16 2:56:17 AM | COPPER | DOWN | 3.7 min | — | — | In play | — |
| 10/16 2:44:49 AM | PALLADIUM | UP | 11 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/16 2:44:33 AM | XRP | DOWN | 27 sec | +0.097% | 0¢ | ❌ Lost | $0.00 |
| 10/16 2:44:33 AM | NEAR | DOWN | 27 sec | +0.202% | 0¢ | ❌ Lost | $0.00 |
| 10/16 2:44:17 AM | BNB | DOWN | 43 sec | +0.018% | 1¢ | ❌ Lost | -$0.15 |
| 10/16 2:44:17 AM | BTC | DOWN | 43 sec | +0.080% | 0¢ | ❌ Lost | $0.00 |
| 10/16 2:44:17 AM | SOL | DOWN | 43 sec | +0.110% | 0¢ | ❌ Lost | $0.00 |
| 10/16 2:44:00 AM | EURUSD | UP | 59 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/16 2:43:44 AM | ZEC | UP | 75 sec | -0.344% | 1¢ | ❌ Lost | -$0.15 |
| 10/16 2:43:28 AM | USDJPY | DOWN | 1.5 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/16 2:43:28 AM | ETH | DOWN | 1.5 min | +0.080% | 2¢ | ❌ Lost | -$0.15 |
| 10/16 2:43:12 AM | GBPUSD | UP | 1.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/16 2:42:56 AM | HYPE | DOWN | 2.0 min | +0.109% | 1¢ | ❌ Lost | -$0.15 |
| 10/16 2:42:42 AM | DOGE | DOWN | 2.3 min | +0.196% | 1¢ | ❌ Lost | -$0.15 |
| 10/16 2:29:53 AM | BNB | DOWN | 7 sec | -0.007% | 0¢ | ❌ Lost | $0.00 |
| 10/16 2:29:53 AM | NATGAS | UP | 7 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/16 2:29:37 AM | AUDUSD | DOWN | 23 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/16 2:29:37 AM | DOGE | DOWN | 23 sec | +0.048% | 0¢ | ❌ Lost | -$0.15 |
| 10/16 2:29:21 AM | XRP | DOWN | 39 sec | +0.105% | 0¢ | ❌ Lost | $0.00 |
| 10/16 2:29:21 AM | ETH | DOWN | 39 sec | +0.078% | 0¢ | ❌ Lost | $0.00 |
| 10/16 2:29:21 AM | BTC | UP | 39 sec | -0.025% | 1¢ | ❌ Lost | -$0.15 |
| 10/16 2:29:05 AM | WTI | UP | 55 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/16 2:29:05 AM | ZEC | UP | 55 sec | -0.164% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
