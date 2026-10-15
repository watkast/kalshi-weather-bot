# 15-Minute 1¢ Study

*Updated Thu Oct 15, 4:36 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 1548 finished bets | 1% | $80.40 | +47% | +5.19¢ | $28.45 / $51.95 |

*Expect about **88 buys a day** (~$13.15/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 1440 | $54.30 | +35% |
| Momentum model ≥ 2%, hold to the close | 2421 | -$0.20 | -0% |
| Volatility model ≥ 5%, sell at 50¢ | 1548 | -$14.85 | -9% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 19832 | 19825 | 78 (0%) | 1.07% | -$1,315.95 (-55%) | Hold to the close: -$1,315.95 (-55%) |

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
| Volatility model | 12765 | 4.4% | 0.4% (53) | -637% | ❌ Worse |
| Momentum model | 12765 | 4.4% | 0.4% (53) | -661% | ❌ Worse |
| Mean-reversion model | 12765 | 7.4% | 0.4% (53) | -761% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 12765 | 53 | -48% | -88% | -88% | -86% |
| Volatility model ≥ 2% | 2815 | 23 | -5% | -78% | -78% | -74% |
| Volatility model ≥ 5% | 1548 | 18 | +47% | -74% | -72% | -68% |
| Volatility model ≥ 10% | 910 | 11 | +71% | -65% | -64% | -60% |
| Momentum model ≥ 2% | 2421 | 20 | -0% | -80% | -80% | -77% |
| Momentum model ≥ 5% | 1440 | 15 | +35% | -77% | -76% | -73% |
| Momentum model ≥ 10% | 963 | 10 | +46% | -71% | -71% | -66% |
| Mean-reversion model ≥ 2% | 4780 | 33 | -25% | -84% | -85% | -81% |
| Mean-reversion model ≥ 5% | 3286 | 26 | -12% | -82% | -82% | -78% |
| Mean-reversion model ≥ 10% | 2152 | 15 | -20% | -81% | -81% | -77% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 12963 | 4% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 4879 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 1983 | 2% | 1% | 1% | 1% | 0% | 0% |
| **All** | 19825 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 78 | 0% | -$1,315.95 | -55% | — |
| Sell at 2¢ | 702 | 4% | -$2,141.43 | -89% | 37 sec |
| Sell at 3¢ | 472 | 2% | -$2,139.87 | -89% | 47 sec |
| Sell at 5¢ | 344 | 2% | -$2,100.35 | -87% | 50 sec |
| Sell at 10¢ | 213 | 1% | -$2,016.92 | -84% | 63 sec |
| Sell at 25¢ | 124 | 1% | -$1,843.51 | -77% | 80 sec |
| Sell at 50¢ | 81 | 0% | -$1,637.20 | -68% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 634 | 5 | 11% | 3% | -25% | -81% | -85% |
| 2–5 min | 6423 | 36 | 7% | 3% | -45% | -88% | -88% |
| 1–2 min | 5160 | 20 | 3% | 2% | -58% | -92% | -91% |
| Under 1 min | 7604 | 17 | 1% | 0% | -68% | -89% | -88% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 1456 | 11 | 5% | 3% | -6% | -89% | -89% |
| HYPE | 1450 | 5 | 4% | 2% | -58% | -90% | -89% |
| ETH | 1444 | 8 | 5% | 3% | -33% | -88% | -87% |
| DOGE | 1443 | 2 | 4% | 2% | -83% | -91% | -90% |
| BNB | 1442 | 5 | 4% | 2% | -57% | -90% | -90% |
| SOL | 1438 | 2 | 3% | 1% | -83% | -93% | -92% |
| XRP | 1433 | 7 | 3% | 1% | -40% | -86% | -86% |
| BTC | 1430 | 7 | 5% | 2% | -34% | -88% | -91% |
| NEAR | 1427 | 8 | 5% | 3% | -27% | -78% | -78% |
| GOLD | 794 | 1 | 4% | 1% | -85% | -92% | -93% |
| SILVER | 774 | 4 | 3% | 1% | -40% | -79% | -79% |
| WTI | 750 | 3 | 3% | 1% | -54% | -94% | -96% |
| COPPER | 684 | 2 | 2% | 1% | -73% | -83% | -83% |
| PLATINUM | 656 | 0 | 1% | 0% | -100% | -99% | -98% |
| NATGAS | 612 | 4 | 2% | 2% | -39% | -96% | -94% |
| PALLADIUM | 609 | 2 | 1% | 0% | -69% | -83% | -83% |
| EURUSD | 603 | 3 | 3% | 1% | -54% | -80% | -79% |
| GBPUSD | 567 | 1 | 2% | 1% | -84% | -97% | -96% |
| USDJPY | 527 | 3 | 1% | 1% | -47% | -99% | -98% |
| AUDUSD | 151 | 0 | 1% | 0% | -100% | -99% | -98% |
| USDCAD | 135 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 9992 | 39 | 3% | 2% | -55% | -89% | -88% |
| DOWN (bought NO) | 9833 | 39 | 4% | 2% | -54% | -89% | -89% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 2169 | 11 | 2% | 1% | -15% | -79% | -78% |
| 0.05–0.1% | 2238 | 7 | 3% | 1% | -55% | -92% | -92% |
| 0.1–0.2% | 3266 | 10 | 4% | 2% | -62% | -90% | -90% |
| 0.2–0.5% | 3779 | 21 | 6% | 3% | -39% | -88% | -88% |
| Over 0.5% | 1508 | 6 | 6% | 2% | -59% | -88% | -89% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 4976 | 20 | 4% | 2% | -54% | -87% | -87% |
| Morning (6am–12pm) | 4701 | 26 | 4% | 2% | -36% | -86% | -86% |
| Afternoon (12–6pm) | 4739 | 16 | 3% | 1% | -60% | -88% | -89% |
| Evening (6pm–12am) | 5409 | 16 | 3% | 2% | -66% | -94% | -93% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,467 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/15 4:29:53 PM | NATGAS | DOWN | 6 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/15 4:29:37 PM | XRP | UP | 22 sec | -0.052% | 0¢ | ❌ Lost | -$0.15 |
| 10/15 4:29:37 PM | BNB | UP | 22 sec | -0.041% | 1¢ | ❌ Lost | $0.00 |
| 10/15 4:29:37 PM | DOGE | UP | 22 sec | -0.086% | 0¢ | ❌ Lost | $0.00 |
| 10/15 4:29:37 PM | NEAR | UP | 22 sec | -0.132% | 0¢ | ❌ Lost | $0.00 |
| 10/15 4:29:05 PM | PLATINUM | UP | 54 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/15 4:29:05 PM | WTI | DOWN | 54 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/15 4:29:05 PM | BTC | DOWN | 54 sec | +0.058% | 1¢ | ❌ Lost | -$0.15 |
| 10/15 4:29:05 PM | PALLADIUM | UP | 54 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/15 4:28:31 PM | USDJPY | DOWN | 88 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/15 4:28:31 PM | SOL | UP | 88 sec | -0.117% | 1¢ | ❌ Lost | -$0.15 |
| 10/15 4:28:15 PM | USDCAD | DOWN | 1.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/15 4:28:15 PM | HYPE | DOWN | 1.7 min | +0.092% | 0¢ | ❌ Lost | -$0.15 |
| 10/15 4:28:00 PM | ZEC | UP | 2.0 min | -0.404% | 0¢ | ❌ Lost | -$0.15 |
| 10/15 4:28:00 PM | ETH | UP | 2.0 min | -0.141% | 1¢ | ❌ Lost | -$0.15 |
| 10/15 4:28:00 PM | GBPUSD | UP | 2.0 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/15 4:27:27 PM | SILVER | UP | 2.5 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/15 4:27:11 PM | GOLD | UP | 2.8 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/15 4:25:03 PM | EURUSD | UP | 5.0 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/15 4:14:55 PM | WTI | UP | 4 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/15 4:14:55 PM | NATGAS | UP | 4 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/15 4:14:55 PM | USDJPY | DOWN | 4 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/15 4:14:39 PM | EURUSD | UP | 20 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/15 4:14:23 PM | DOGE | DOWN | 36 sec | +0.041% | 0¢ | ❌ Lost | $0.00 |
| 10/15 4:14:23 PM | NEAR | UP | 36 sec | -0.283% | 0¢ | ❌ Lost | $0.00 |
| 10/15 4:14:07 PM | XRP | DOWN | 52 sec | +0.097% | 0¢ | ❌ Lost | -$0.15 |
| 10/15 4:14:07 PM | BTC | DOWN | 52 sec | +0.065% | 1¢ | ❌ Lost | -$0.15 |
| 10/15 4:14:07 PM | SOL | DOWN | 52 sec | +0.062% | 1¢ | ❌ Lost | -$0.15 |
| 10/15 4:13:51 PM | HYPE | DOWN | 69 sec | +0.099% | 0¢ | ❌ Lost | $0.00 |
| 10/15 4:13:35 PM | ETH | DOWN | 85 sec | +0.101% | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
