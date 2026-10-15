# 15-Minute 1¢ Study

*Updated Thu Oct 15, 9:10 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 1508 finished bets | 1% | $85.05 | +51% | +5.64¢ | $30.85 / $54.20 |

*Expect about **87 buys a day** (~$13.04/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 1411 | $57.30 | +38% |
| Momentum model ≥ 2%, hold to the close | 2352 | $7.75 | +3% |
| Volatility model ≥ 2%, hold to the close | 2731 | -$8.00 | -2% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 19383 | 19376 | 78 (0%) | 1.07% | -$1,260.30 (-54%) | Hold to the close: -$1,260.30 (-54%) |

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
| Volatility model | 12506 | 4.5% | 0.4% (53) | -637% | ❌ Worse |
| Momentum model | 12506 | 4.4% | 0.4% (53) | -661% | ❌ Worse |
| Mean-reversion model | 12506 | 7.4% | 0.4% (53) | -758% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 12506 | 53 | -47% | -88% | -88% | -86% |
| Volatility model ≥ 2% | 2731 | 23 | -2% | -78% | -77% | -73% |
| Volatility model ≥ 5% | 1508 | 18 | +51% | -73% | -72% | -67% |
| Volatility model ≥ 10% | 893 | 11 | +75% | -64% | -63% | -59% |
| Momentum model ≥ 2% | 2352 | 20 | +3% | -80% | -80% | -77% |
| Momentum model ≥ 5% | 1411 | 15 | +38% | -76% | -76% | -73% |
| Momentum model ≥ 10% | 947 | 10 | +48% | -71% | -70% | -65% |
| Mean-reversion model ≥ 2% | 4658 | 33 | -23% | -84% | -84% | -81% |
| Mean-reversion model ≥ 5% | 3198 | 26 | -10% | -82% | -82% | -78% |
| Mean-reversion model ≥ 10% | 2095 | 15 | -18% | -80% | -80% | -77% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 12704 | 4% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 4768 | 2% | 2% | 1% | 1% | 0% | 0% |
| Financials | 1904 | 2% | 1% | 1% | 1% | 0% | 0% |
| **All** | 19376 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 78 | 0% | -$1,260.30 | -54% | — |
| Sell at 2¢ | 691 | 4% | -$2,088.64 | -89% | 42 sec |
| Sell at 3¢ | 466 | 2% | -$2,086.56 | -89% | 47 sec |
| Sell at 5¢ | 339 | 2% | -$2,047.95 | -87% | 50 sec |
| Sell at 10¢ | 212 | 1% | -$1,962.58 | -83% | 63 sec |
| Sell at 25¢ | 124 | 1% | -$1,787.86 | -76% | 80 sec |
| Sell at 50¢ | 81 | 0% | -$1,581.55 | -67% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 626 | 5 | 11% | 3% | -24% | -81% | -86% |
| 2–5 min | 6274 | 36 | 7% | 3% | -43% | -88% | -88% |
| 1–2 min | 5039 | 20 | 3% | 2% | -57% | -92% | -91% |
| Under 1 min | 7433 | 17 | 1% | 0% | -67% | -88% | -88% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 1426 | 11 | 5% | 3% | -4% | -89% | -90% |
| HYPE | 1420 | 5 | 4% | 2% | -57% | -90% | -89% |
| ETH | 1415 | 8 | 5% | 3% | -31% | -88% | -87% |
| BNB | 1415 | 5 | 5% | 2% | -57% | -90% | -89% |
| DOGE | 1414 | 2 | 4% | 2% | -82% | -91% | -90% |
| SOL | 1410 | 2 | 3% | 1% | -83% | -93% | -92% |
| XRP | 1403 | 7 | 3% | 1% | -38% | -85% | -86% |
| BTC | 1401 | 7 | 5% | 2% | -33% | -88% | -91% |
| NEAR | 1400 | 8 | 5% | 3% | -25% | -78% | -78% |
| GOLD | 777 | 1 | 4% | 1% | -85% | -92% | -93% |
| SILVER | 756 | 4 | 3% | 1% | -39% | -78% | -78% |
| WTI | 729 | 3 | 3% | 1% | -52% | -94% | -96% |
| COPPER | 672 | 2 | 2% | 1% | -72% | -83% | -82% |
| PLATINUM | 643 | 0 | 1% | 0% | -100% | -99% | -98% |
| PALLADIUM | 598 | 2 | 1% | 0% | -69% | -82% | -83% |
| NATGAS | 593 | 4 | 3% | 2% | -37% | -96% | -94% |
| EURUSD | 586 | 3 | 3% | 1% | -52% | -79% | -79% |
| GBPUSD | 549 | 1 | 2% | 1% | -83% | -97% | -96% |
| USDJPY | 507 | 3 | 1% | 1% | -45% | -99% | -98% |
| AUDUSD | 136 | 0 | 1% | 0% | -100% | -99% | -98% |
| USDCAD | 126 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 9799 | 39 | 4% | 2% | -54% | -89% | -88% |
| DOWN (bought NO) | 9577 | 39 | 4% | 2% | -53% | -89% | -89% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 2140 | 11 | 2% | 1% | -14% | -78% | -78% |
| 0.05–0.1% | 2198 | 7 | 3% | 1% | -54% | -92% | -92% |
| 0.1–0.2% | 3188 | 10 | 4% | 2% | -61% | -90% | -90% |
| 0.2–0.5% | 3702 | 21 | 6% | 3% | -37% | -88% | -88% |
| Over 0.5% | 1473 | 6 | 6% | 2% | -58% | -88% | -90% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 4976 | 20 | 4% | 2% | -54% | -87% | -87% |
| Morning (6am–12pm) | 4509 | 26 | 4% | 2% | -33% | -86% | -85% |
| Afternoon (12–6pm) | 4482 | 16 | 3% | 1% | -58% | -87% | -88% |
| Evening (6pm–12am) | 5409 | 16 | 3% | 2% | -66% | -94% | -93% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,482 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/15 8:59:56 AM | NATGAS | UP | 3 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/15 8:59:41 AM | COPPER | DOWN | 18 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/15 8:59:09 AM | WTI | UP | 50 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/15 8:58:38 AM | ZEC | DOWN | 82 sec | +0.472% | 1¢ | ❌ Lost | -$0.15 |
| 10/15 8:58:38 AM | HYPE | DOWN | 82 sec | +0.270% | 1¢ | ❌ Lost | -$0.15 |
| 10/15 8:58:38 AM | SILVER | DOWN | 82 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/15 8:58:06 AM | DOGE | DOWN | 1.9 min | +0.659% | 1¢ | ❌ Lost | -$0.15 |
| 10/15 8:58:06 AM | XRP | DOWN | 1.9 min | +0.478% | 0¢ | ❌ Lost | -$0.15 |
| 10/15 8:57:19 AM | USDCAD | DOWN | 2.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/15 8:57:19 AM | PLATINUM | DOWN | 2.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/15 8:57:19 AM | EURUSD | UP | 2.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/15 8:57:03 AM | GBPUSD | UP | 3.0 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/15 8:57:03 AM | ETH | DOWN | 3.0 min | +0.511% | 0¢ | ❌ Lost | -$0.15 |
| 10/15 8:56:47 AM | BTC | DOWN | 3.2 min | +0.537% | 0¢ | ❌ Lost | $0.00 |
| 10/15 8:56:47 AM | SOL | DOWN | 3.2 min | +0.687% | 1¢ | ❌ Lost | -$0.15 |
| 10/15 8:56:31 AM | NEAR | DOWN | 3.5 min | +1.915% | 1¢ | ❌ Lost | -$0.15 |
| 10/15 8:55:12 AM | BNB | DOWN | 4.8 min | +0.318% | 1¢ | ❌ Lost | -$0.15 |
| 10/15 8:44:31 AM | USDJPY | DOWN | 28 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/15 8:44:15 AM | WTI | DOWN | 44 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/15 8:44:15 AM | NATGAS | DOWN | 44 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/15 8:43:44 AM | COPPER | DOWN | 76 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/15 8:43:44 AM | EURUSD | DOWN | 76 sec | — | 2¢ | ❌ Lost | -$0.15 |
| 10/15 8:43:12 AM | PLATINUM | DOWN | 1.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/15 8:43:12 AM | PALLADIUM | DOWN | 1.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/15 8:42:56 AM | AUDUSD | DOWN | 2.1 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/15 8:42:25 AM | GBPUSD | DOWN | 2.6 min | — | 7¢ | ❌ Lost | -$0.15 |
| 10/15 8:42:09 AM | DOGE | DOWN | 2.9 min | +0.720% | 0¢ | ❌ Lost | -$0.15 |
| 10/15 8:42:09 AM | ETH | DOWN | 2.9 min | +0.558% | 0¢ | ❌ Lost | -$0.15 |
| 10/15 8:42:09 AM | BTC | DOWN | 2.9 min | +0.360% | 0¢ | ❌ Lost | $0.00 |
| 10/15 8:42:09 AM | GOLD | DOWN | 2.9 min | — | 69¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
