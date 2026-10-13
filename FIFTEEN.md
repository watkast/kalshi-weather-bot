# 15-Minute 1¢ Study

*Updated Tue Oct 13, 4:18 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 1250 finished bets | 1% | $45.05 | +33% | +3.60¢ | $30.80 / $14.25 |

*Expect about **83 buys a day** (~$12.38/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 1199 | $24.85 | +19% |
| 5+ min left, hold to the close | 461 | -$12.25 | -18% |
| Volatility model ≥ 5%, sell at 50¢ | 1250 | -$13.95 | -10% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 16488 | 16481 | 63 (0%) | 1.07% | -$1,113.60 (-56%) | Hold to the close: -$1,113.60 (-56%) |

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
| Volatility model | 10877 | 4.5% | 0.4% (46) | -658% | ❌ Worse |
| Momentum model | 10877 | 4.5% | 0.4% (46) | -686% | ❌ Worse |
| Mean-reversion model | 10877 | 7.2% | 0.4% (46) | -769% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 10877 | 46 | -47% | -88% | -88% | -86% |
| Volatility model ≥ 2% | 2226 | 18 | -6% | -78% | -78% | -74% |
| Volatility model ≥ 5% | 1250 | 13 | +33% | -73% | -72% | -69% |
| Volatility model ≥ 10% | 780 | 9 | +65% | -63% | -63% | -59% |
| Momentum model ≥ 2% | 1957 | 15 | -7% | -79% | -80% | -78% |
| Momentum model ≥ 5% | 1199 | 11 | +19% | -76% | -76% | -73% |
| Momentum model ≥ 10% | 819 | 8 | +38% | -69% | -69% | -64% |
| Mean-reversion model ≥ 2% | 3882 | 27 | -24% | -85% | -85% | -82% |
| Mean-reversion model ≥ 5% | 2650 | 20 | -16% | -83% | -83% | -79% |
| Mean-reversion model ≥ 10% | 1749 | 14 | -8% | -81% | -81% | -79% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 11075 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 3965 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 1441 | 2% | 1% | 1% | 1% | 0% | 0% |
| **All** | 16481 | 3% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 63 | 0% | -$1,113.60 | -56% | — |
| Sell at 2¢ | 557 | 3% | -$1,808.78 | -91% | 33 sec |
| Sell at 3¢ | 366 | 2% | -$1,810.86 | -91% | 46 sec |
| Sell at 5¢ | 265 | 2% | -$1,781.35 | -89% | 49 sec |
| Sell at 10¢ | 174 | 1% | -$1,697.66 | -85% | 63 sec |
| Sell at 25¢ | 99 | 1% | -$1,569.91 | -79% | 79 sec |
| Sell at 50¢ | 64 | 0% | -$1,409.60 | -71% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 457 | 4 | 11% | 3% | -17% | -80% | -87% |
| 2–5 min | 5328 | 32 | 6% | 3% | -41% | -88% | -89% |
| 1–2 min | 4346 | 16 | 3% | 2% | -60% | -94% | -94% |
| Under 1 min | 6346 | 11 | 1% | 0% | -75% | -91% | -91% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 1243 | 7 | 4% | 2% | -30% | -90% | -90% |
| HYPE | 1240 | 4 | 4% | 2% | -60% | -90% | -89% |
| DOGE | 1234 | 2 | 4% | 2% | -80% | -91% | -90% |
| BNB | 1233 | 5 | 4% | 1% | -51% | -91% | -91% |
| ETH | 1232 | 8 | 5% | 2% | -21% | -90% | -89% |
| SOL | 1231 | 2 | 3% | 1% | -80% | -93% | -92% |
| BTC | 1224 | 6 | 5% | 2% | -35% | -88% | -91% |
| NEAR | 1219 | 7 | 5% | 2% | -25% | -77% | -77% |
| XRP | 1219 | 7 | 2% | 1% | -29% | -85% | -85% |
| GOLD | 653 | 0 | 3% | 1% | -100% | -93% | -94% |
| SILVER | 635 | 1 | 3% | 1% | -82% | -94% | -94% |
| WTI | 606 | 3 | 3% | 1% | -44% | -94% | -96% |
| COPPER | 567 | 0 | 1% | 1% | -100% | -98% | -97% |
| PLATINUM | 525 | 0 | 0% | 0% | -100% | -100% | -100% |
| PALLADIUM | 493 | 1 | 1% | 0% | -81% | -98% | -98% |
| NATGAS | 486 | 3 | 2% | 2% | -42% | -96% | -94% |
| EURUSD | 473 | 3 | 3% | 2% | -41% | -76% | -75% |
| GBPUSD | 449 | 1 | 2% | 1% | -79% | -96% | -96% |
| USDJPY | 409 | 3 | 1% | 1% | -32% | -98% | -97% |
| AUDUSD | 56 | 0 | 0% | 0% | -100% | -100% | -100% |
| USDCAD | 54 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 8313 | 34 | 3% | 2% | -53% | -90% | -90% |
| DOWN (bought NO) | 8168 | 29 | 3% | 2% | -59% | -91% | -92% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 1954 | 10 | 2% | 1% | -15% | -77% | -77% |
| 0.05–0.1% | 1961 | 6 | 3% | 1% | -56% | -92% | -92% |
| 0.1–0.2% | 2819 | 9 | 4% | 2% | -61% | -91% | -92% |
| 0.2–0.5% | 3122 | 18 | 5% | 3% | -37% | -89% | -89% |
| Over 0.5% | 1216 | 5 | 6% | 2% | -57% | -88% | -90% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 4233 | 20 | 4% | 2% | -46% | -87% | -87% |
| Morning (6am–12pm) | 3780 | 20 | 4% | 2% | -39% | -91% | -91% |
| Afternoon (12–6pm) | 3818 | 9 | 3% | 1% | -72% | -91% | -91% |
| Evening (6pm–12am) | 4650 | 14 | 3% | 1% | -66% | -94% | -94% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 25 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,500 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/13 4:14:59 AM | ZEC | UP | 0 sec | -0.018% | 0¢ | ❌ Lost | $0.00 |
| 10/13 4:14:44 AM | SILVER | UP | 15 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/13 4:14:28 AM | GOLD | UP | 31 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/13 4:14:28 AM | EURUSD | DOWN | 31 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/13 4:14:12 AM | SOL | DOWN | 47 sec | +0.097% | 0¢ | ❌ Lost | -$0.15 |
| 10/13 4:14:12 AM | BNB | UP | 47 sec | -0.071% | 1¢ | ❌ Lost | -$0.15 |
| 10/13 4:13:41 AM | PALLADIUM | UP | 79 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/13 4:13:25 AM | ETH | UP | 1.6 min | -0.166% | 0¢ | ❌ Lost | $0.00 |
| 10/13 4:13:25 AM | BTC | UP | 1.6 min | -0.137% | 1¢ | ❌ Lost | -$0.15 |
| 10/13 4:13:25 AM | USDJPY | DOWN | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/13 4:13:25 AM | PLATINUM | UP | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/13 4:13:25 AM | NATGAS | UP | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/13 4:12:53 AM | HYPE | DOWN | 2.1 min | +0.247% | 3¢ | ❌ Lost | -$0.15 |
| 10/13 4:12:03 AM | NEAR | DOWN | 2.9 min | +0.593% | 1¢ | ❌ Lost | -$0.15 |
| 10/13 4:12:03 AM | DOGE | DOWN | 2.9 min | +0.209% | 7¢ | ❌ Lost | -$0.15 |
| 10/13 4:10:31 AM | XRP | DOWN | 4.5 min | +0.331% | 1¢ | ❌ Lost | -$0.15 |
| 10/13 3:59:28 AM | BTC | UP | 32 sec | -0.015% | 1¢ | ❌ Lost | -$0.15 |
| 10/13 3:59:28 AM | GOLD | DOWN | 32 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/13 3:59:12 AM | ETH | DOWN | 48 sec | +0.054% | 0¢ | ❌ Lost | $0.00 |
| 10/13 3:59:12 AM | USDCAD | UP | 48 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/13 3:59:12 AM | COPPER | DOWN | 48 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/13 3:58:25 AM | BNB | UP | 1.6 min | -0.093% | 0¢ | ❌ Lost | $0.00 |
| 10/13 3:57:33 AM | WTI | UP | 2.5 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/13 3:57:17 AM | ZEC | UP | 2.7 min | -0.376% | 0¢ | ❌ Lost | $0.00 |
| 10/13 3:56:45 AM | SOL | UP | 3.2 min | -0.333% | 1¢ | ❌ Lost | -$0.15 |
| 10/13 3:56:45 AM | DOGE | UP | 3.2 min | -0.263% | 1¢ | ❌ Lost | -$0.15 |
| 10/13 3:56:27 AM | XRP | UP | 3.5 min | -0.374% | 0¢ | ❌ Lost | -$0.15 |
| 10/13 3:56:11 AM | NEAR | UP | 3.8 min | -0.843% | 1¢ | ❌ Lost | -$0.15 |
| 10/13 3:54:38 AM | HYPE | UP | 5.4 min | -0.396% | 1¢ | ❌ Lost | -$0.15 |
| 10/13 3:44:53 AM | WTI | DOWN | 6 sec | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
