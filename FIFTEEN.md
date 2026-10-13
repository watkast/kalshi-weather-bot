# 15-Minute 1¢ Study

*Updated Tue Oct 13, 3:17 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 1248 finished bets | 1% | $45.35 | +33% | +3.63¢ | $30.95 / $14.40 |

*Expect about **83 buys a day** (~$12.39/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 1195 | $25.15 | +20% |
| 5+ min left, hold to the close | 458 | -$11.80 | -17% |
| Volatility model ≥ 5%, sell at 50¢ | 1248 | -$13.65 | -10% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 16431 | 16424 | 63 (0%) | 1.07% | -$1,106.40 (-56%) | Hold to the close: -$1,106.40 (-56%) |

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
| Volatility model | 10842 | 4.5% | 0.4% (46) | -659% | ❌ Worse |
| Momentum model | 10842 | 4.5% | 0.4% (46) | -686% | ❌ Worse |
| Mean-reversion model | 10842 | 7.2% | 0.4% (46) | -770% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 10842 | 46 | -47% | -88% | -88% | -86% |
| Volatility model ≥ 2% | 2214 | 18 | -6% | -78% | -78% | -75% |
| Volatility model ≥ 5% | 1248 | 13 | +33% | -73% | -71% | -69% |
| Volatility model ≥ 10% | 780 | 9 | +65% | -63% | -63% | -59% |
| Momentum model ≥ 2% | 1947 | 15 | -7% | -79% | -80% | -78% |
| Momentum model ≥ 5% | 1195 | 11 | +20% | -76% | -76% | -73% |
| Momentum model ≥ 10% | 819 | 8 | +38% | -69% | -69% | -64% |
| Mean-reversion model ≥ 2% | 3864 | 27 | -24% | -85% | -85% | -82% |
| Mean-reversion model ≥ 5% | 2643 | 20 | -16% | -83% | -83% | -79% |
| Mean-reversion model ≥ 10% | 1747 | 14 | -7% | -81% | -81% | -79% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 11040 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 3951 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 1433 | 2% | 1% | 1% | 1% | 0% | 0% |
| **All** | 16424 | 3% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 63 | 0% | -$1,106.40 | -56% | — |
| Sell at 2¢ | 554 | 3% | -$1,802.36 | -91% | 33 sec |
| Sell at 3¢ | 365 | 2% | -$1,804.05 | -91% | 46 sec |
| Sell at 5¢ | 264 | 2% | -$1,774.80 | -89% | 49 sec |
| Sell at 10¢ | 174 | 1% | -$1,690.46 | -85% | 63 sec |
| Sell at 25¢ | 99 | 1% | -$1,562.71 | -79% | 79 sec |
| Sell at 50¢ | 64 | 0% | -$1,402.40 | -71% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 454 | 4 | 11% | 3% | -17% | -80% | -87% |
| 2–5 min | 5307 | 32 | 6% | 3% | -41% | -89% | -89% |
| 1–2 min | 4332 | 16 | 3% | 2% | -60% | -94% | -94% |
| Under 1 min | 6327 | 11 | 1% | 0% | -75% | -91% | -91% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 1239 | 7 | 4% | 2% | -30% | -90% | -90% |
| HYPE | 1236 | 4 | 4% | 2% | -60% | -90% | -89% |
| DOGE | 1230 | 2 | 4% | 2% | -80% | -91% | -91% |
| BNB | 1229 | 5 | 4% | 1% | -51% | -91% | -91% |
| ETH | 1228 | 8 | 5% | 2% | -21% | -90% | -89% |
| SOL | 1228 | 2 | 3% | 1% | -80% | -93% | -92% |
| BTC | 1220 | 6 | 5% | 2% | -35% | -88% | -91% |
| NEAR | 1215 | 7 | 5% | 2% | -25% | -77% | -77% |
| XRP | 1215 | 7 | 2% | 1% | -29% | -85% | -85% |
| GOLD | 649 | 0 | 3% | 1% | -100% | -93% | -94% |
| SILVER | 633 | 1 | 3% | 1% | -82% | -94% | -94% |
| WTI | 604 | 3 | 3% | 1% | -43% | -94% | -96% |
| COPPER | 566 | 0 | 1% | 1% | -100% | -98% | -97% |
| PLATINUM | 524 | 0 | 0% | 0% | -100% | -100% | -100% |
| PALLADIUM | 491 | 1 | 1% | 0% | -81% | -98% | -98% |
| NATGAS | 484 | 3 | 2% | 2% | -42% | -96% | -94% |
| EURUSD | 471 | 3 | 3% | 2% | -41% | -75% | -75% |
| GBPUSD | 447 | 1 | 2% | 1% | -79% | -96% | -96% |
| USDJPY | 407 | 3 | 1% | 1% | -31% | -98% | -97% |
| AUDUSD | 55 | 0 | 0% | 0% | -100% | -100% | -100% |
| USDCAD | 53 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 8278 | 34 | 3% | 2% | -53% | -90% | -90% |
| DOWN (bought NO) | 8146 | 29 | 3% | 1% | -59% | -91% | -92% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 1952 | 10 | 2% | 1% | -15% | -77% | -76% |
| 0.05–0.1% | 1955 | 6 | 3% | 1% | -56% | -92% | -92% |
| 0.1–0.2% | 2813 | 9 | 4% | 2% | -61% | -91% | -92% |
| 0.2–0.5% | 3105 | 18 | 5% | 3% | -36% | -89% | -89% |
| Over 0.5% | 1212 | 5 | 6% | 2% | -57% | -88% | -90% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 4176 | 20 | 4% | 2% | -45% | -87% | -87% |
| Morning (6am–12pm) | 3780 | 20 | 4% | 2% | -39% | -91% | -91% |
| Afternoon (12–6pm) | 3818 | 9 | 3% | 1% | -72% | -91% | -91% |
| Evening (6pm–12am) | 4650 | 14 | 3% | 1% | -66% | -94% | -94% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 25 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,509 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/13 3:14:59 AM | PLATINUM | UP | 0 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/13 3:14:59 AM | EURUSD | DOWN | 0 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/13 3:14:44 AM | GBPUSD | DOWN | 15 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/13 3:14:44 AM | AUDUSD | DOWN | 15 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/13 3:14:28 AM | WTI | UP | 31 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/13 3:14:28 AM | USDJPY | DOWN | 31 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/13 3:13:56 AM | BTC | UP | 64 sec | -0.079% | 1¢ | ❌ Lost | -$0.15 |
| 10/13 3:13:39 AM | HYPE | UP | 81 sec | -0.214% | 0¢ | ❌ Lost | $0.00 |
| 10/13 3:13:23 AM | DOGE | UP | 1.6 min | -0.228% | 1¢ | ❌ Lost | -$0.15 |
| 10/13 3:13:23 AM | ZEC | UP | 1.6 min | -0.307% | 0¢ | ❌ Lost | $0.00 |
| 10/13 3:13:07 AM | BNB | UP | 1.9 min | -0.190% | 1¢ | ❌ Lost | -$0.15 |
| 10/13 3:13:07 AM | SILVER | DOWN | 1.9 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/13 3:12:52 AM | SOL | UP | 2.1 min | -0.252% | 0¢ | ❌ Lost | -$0.15 |
| 10/13 3:12:52 AM | NEAR | UP | 2.1 min | -0.654% | 1¢ | ❌ Lost | -$0.15 |
| 10/13 3:12:05 AM | ETH | UP | 2.9 min | -0.224% | 0¢ | ❌ Lost | -$0.15 |
| 10/13 3:12:05 AM | XRP | UP | 2.9 min | -0.313% | 0¢ | ❌ Lost | -$0.15 |
| 10/13 2:59:58 AM | GOLD | UP | 2 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/13 2:59:43 AM | AUDUSD | DOWN | 17 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/13 2:59:11 AM | USDJPY | UP | 49 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/13 2:58:55 AM | PALLADIUM | UP | 65 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/13 2:58:55 AM | SILVER | UP | 65 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/13 2:57:36 AM | ZEC | UP | 2.4 min | -0.595% | 0¢ | ❌ Lost | $0.00 |
| 10/13 2:57:20 AM | BNB | UP | 2.7 min | -0.116% | 1¢ | ❌ Lost | -$0.15 |
| 10/13 2:57:01 AM | HYPE | UP | 3.0 min | -0.225% | 0¢ | ❌ Lost | -$0.15 |
| 10/13 2:56:45 AM | COPPER | DOWN | 3.2 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/13 2:56:14 AM | XRP | UP | 3.8 min | -0.203% | 1¢ | ❌ Lost | -$0.15 |
| 10/13 2:55:26 AM | ETH | UP | 4.5 min | -0.240% | 1¢ | ❌ Lost | -$0.15 |
| 10/13 2:55:10 AM | NEAR | UP | 4.8 min | -0.693% | 0¢ | ❌ Lost | -$0.15 |
| 10/13 2:54:38 AM | BTC | UP | 5.3 min | -0.211% | 3¢ | ❌ Lost | -$0.15 |
| 10/13 2:54:23 AM | DOGE | UP | 5.6 min | -0.422% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
