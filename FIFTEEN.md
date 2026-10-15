# 15-Minute 1¢ Study

*Updated Thu Oct 15, 8:39 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 1505 finished bets | 1% | $85.50 | +51% | +5.68¢ | $31.15 / $54.35 |

*Expect about **87 buys a day** (~$13.03/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 1410 | $57.45 | +38% |
| Momentum model ≥ 2%, hold to the close | 2351 | $7.90 | +3% |
| Volatility model ≥ 2%, hold to the close | 2722 | -$6.80 | -2% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 19345 | 19338 | 78 (0%) | 1.07% | -$1,254.90 (-53%) | Hold to the close: -$1,254.90 (-53%) |

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
| Volatility model | 12488 | 4.5% | 0.4% (53) | -637% | ❌ Worse |
| Momentum model | 12488 | 4.4% | 0.4% (53) | -661% | ❌ Worse |
| Mean-reversion model | 12488 | 7.4% | 0.4% (53) | -758% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 12488 | 53 | -47% | -88% | -88% | -86% |
| Volatility model ≥ 2% | 2722 | 23 | -2% | -78% | -77% | -73% |
| Volatility model ≥ 5% | 1505 | 18 | +51% | -73% | -71% | -67% |
| Volatility model ≥ 10% | 893 | 11 | +75% | -64% | -63% | -59% |
| Momentum model ≥ 2% | 2351 | 20 | +3% | -80% | -80% | -77% |
| Momentum model ≥ 5% | 1410 | 15 | +38% | -76% | -76% | -73% |
| Momentum model ≥ 10% | 947 | 10 | +48% | -71% | -70% | -65% |
| Mean-reversion model ≥ 2% | 4643 | 33 | -22% | -84% | -84% | -81% |
| Mean-reversion model ≥ 5% | 3186 | 26 | -10% | -82% | -82% | -78% |
| Mean-reversion model ≥ 10% | 2087 | 15 | -17% | -80% | -80% | -77% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 12686 | 4% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 4756 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 1896 | 2% | 1% | 1% | 1% | 0% | 0% |
| **All** | 19338 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 78 | 0% | -$1,254.90 | -53% | — |
| Sell at 2¢ | 688 | 4% | -$2,084.02 | -89% | 39 sec |
| Sell at 3¢ | 464 | 2% | -$2,081.94 | -89% | 47 sec |
| Sell at 5¢ | 337 | 2% | -$2,043.85 | -87% | 50 sec |
| Sell at 10¢ | 211 | 1% | -$1,958.49 | -83% | 63 sec |
| Sell at 25¢ | 123 | 1% | -$1,785.77 | -76% | 79 sec |
| Sell at 50¢ | 80 | 0% | -$1,582.90 | -67% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 626 | 5 | 11% | 3% | -24% | -81% | -86% |
| 2–5 min | 6251 | 36 | 7% | 3% | -43% | -88% | -88% |
| 1–2 min | 5030 | 20 | 3% | 2% | -57% | -92% | -91% |
| Under 1 min | 7427 | 17 | 1% | 0% | -67% | -88% | -88% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 1424 | 11 | 5% | 3% | -4% | -89% | -90% |
| HYPE | 1418 | 5 | 4% | 2% | -57% | -90% | -89% |
| ETH | 1413 | 8 | 5% | 3% | -31% | -88% | -87% |
| BNB | 1413 | 5 | 5% | 2% | -57% | -90% | -89% |
| DOGE | 1412 | 2 | 4% | 2% | -82% | -91% | -90% |
| SOL | 1408 | 2 | 3% | 1% | -83% | -93% | -92% |
| XRP | 1401 | 7 | 3% | 1% | -38% | -85% | -86% |
| BTC | 1399 | 7 | 5% | 2% | -33% | -88% | -91% |
| NEAR | 1398 | 8 | 5% | 3% | -25% | -77% | -78% |
| GOLD | 776 | 1 | 4% | 1% | -85% | -92% | -94% |
| SILVER | 754 | 4 | 3% | 1% | -38% | -78% | -78% |
| WTI | 727 | 3 | 3% | 1% | -52% | -94% | -96% |
| COPPER | 670 | 2 | 2% | 1% | -72% | -83% | -82% |
| PLATINUM | 641 | 0 | 1% | 0% | -100% | -99% | -98% |
| PALLADIUM | 597 | 2 | 1% | 0% | -69% | -82% | -83% |
| NATGAS | 591 | 4 | 3% | 2% | -37% | -96% | -94% |
| EURUSD | 584 | 3 | 3% | 1% | -52% | -80% | -79% |
| GBPUSD | 547 | 1 | 2% | 1% | -83% | -97% | -97% |
| USDJPY | 506 | 3 | 1% | 1% | -45% | -99% | -98% |
| AUDUSD | 135 | 0 | 1% | 0% | -100% | -99% | -98% |
| USDCAD | 124 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 9794 | 39 | 4% | 2% | -54% | -89% | -88% |
| DOWN (bought NO) | 9544 | 39 | 4% | 2% | -53% | -89% | -89% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 2140 | 11 | 2% | 1% | -14% | -78% | -78% |
| 0.05–0.1% | 2198 | 7 | 3% | 1% | -54% | -92% | -92% |
| 0.1–0.2% | 3188 | 10 | 4% | 2% | -61% | -90% | -90% |
| 0.2–0.5% | 3695 | 21 | 6% | 3% | -37% | -88% | -88% |
| Over 0.5% | 1462 | 6 | 6% | 2% | -58% | -88% | -90% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 4976 | 20 | 4% | 2% | -54% | -87% | -87% |
| Morning (6am–12pm) | 4471 | 26 | 4% | 2% | -33% | -86% | -85% |
| Afternoon (12–6pm) | 4482 | 16 | 3% | 1% | -58% | -87% | -88% |
| Evening (6pm–12am) | 5409 | 16 | 3% | 2% | -66% | -94% | -93% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,474 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/15 8:29:45 AM | DOGE | UP | 14 sec | -0.034% | 0¢ | ❌ Lost | $0.00 |
| 10/15 8:29:45 AM | ZEC | DOWN | 14 sec | -0.002% | 0¢ | ❌ Lost | $0.00 |
| 10/15 8:29:45 AM | XRP | UP | 14 sec | -0.061% | 0¢ | ❌ Lost | $0.00 |
| 10/15 8:29:29 AM | NEAR | DOWN | 30 sec | +0.333% | 0¢ | ❌ Lost | $0.00 |
| 10/15 8:29:29 AM | SOL | UP | 30 sec | -0.073% | 0¢ | ❌ Lost | -$0.15 |
| 10/15 8:29:07 AM | PALLADIUM | DOWN | 53 sec | — | 0¢ | ✅ Won | $13.85 |
| 10/15 8:29:07 AM | BTC | DOWN | 53 sec | +0.071% | 0¢ | ❌ Lost | -$0.15 |
| 10/15 8:28:52 AM | PLATINUM | DOWN | 67 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/15 8:28:52 AM | COPPER | DOWN | 67 sec | — | 0¢ | ✅ Won | $13.85 |
| 10/15 8:28:37 AM | BNB | DOWN | 82 sec | +0.094% | 1¢ | ❌ Lost | -$0.15 |
| 10/15 8:28:21 AM | AUDUSD | DOWN | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/15 8:25:57 AM | GOLD | DOWN | 4.0 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/15 8:25:42 AM | HYPE | DOWN | 4.3 min | +0.911% | 1¢ | ❌ Lost | -$0.15 |
| 10/15 8:25:42 AM | SILVER | DOWN | 4.3 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/15 8:14:55 AM | PALLADIUM | UP | 4 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/15 8:14:55 AM | USDCAD | UP | 4 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/15 8:14:55 AM | GBPUSD | UP | 4 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/15 8:14:40 AM | NATGAS | UP | 20 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/15 8:14:08 AM | EURUSD | UP | 52 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/15 8:13:52 AM | DOGE | DOWN | 68 sec | +0.487% | 0¢ | ❌ Lost | -$0.15 |
| 10/15 8:13:21 AM | GOLD | UP | 1.6 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/15 8:12:17 AM | AUDUSD | DOWN | 2.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/15 8:12:01 AM | USDJPY | DOWN | 3.0 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/15 8:10:58 AM | WTI | DOWN | 4.0 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/15 8:10:11 AM | ZEC | DOWN | 4.8 min | +1.748% | 1¢ | ❌ Lost | -$0.15 |
| 10/15 8:09:55 AM | NEAR | DOWN | 5.1 min | +2.186% | 1¢ | ❌ Lost | -$0.15 |
| 10/15 8:09:39 AM | BNB | DOWN | 5.3 min | +0.680% | 1¢ | ❌ Lost | -$0.15 |
| 10/15 8:09:39 AM | XRP | DOWN | 5.3 min | +1.228% | 1¢ | ❌ Lost | -$0.15 |
| 10/15 8:09:23 AM | SOL | DOWN | 5.6 min | +1.226% | 1¢ | ❌ Lost | -$0.15 |
| 10/15 8:08:41 AM | BTC | DOWN | 6.3 min | +0.794% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
