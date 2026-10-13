# 15-Minute 1¢ Study

*Updated Tue Oct 13, 5:40 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 1254 finished bets | 1% | $44.45 | +32% | +3.54¢ | $30.80 / $13.65 |

*Expect about **82 buys a day** (~$12.37/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 1202 | $24.40 | +19% |
| 5+ min left, hold to the close | 469 | -$13.45 | -19% |
| Volatility model ≥ 5%, sell at 50¢ | 1254 | -$14.55 | -11% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 16565 | 16558 | 63 (0%) | 1.07% | -$1,123.95 (-56%) | Hold to the close: -$1,123.95 (-56%) |

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
| Volatility model | 10922 | 4.5% | 0.4% (46) | -658% | ❌ Worse |
| Momentum model | 10922 | 4.4% | 0.4% (46) | -685% | ❌ Worse |
| Mean-reversion model | 10922 | 7.2% | 0.4% (46) | -770% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 10922 | 46 | -47% | -88% | -88% | -86% |
| Volatility model ≥ 2% | 2237 | 18 | -7% | -78% | -77% | -74% |
| Volatility model ≥ 5% | 1254 | 13 | +32% | -73% | -72% | -69% |
| Volatility model ≥ 10% | 780 | 9 | +65% | -63% | -63% | -59% |
| Momentum model ≥ 2% | 1967 | 15 | -8% | -79% | -80% | -78% |
| Momentum model ≥ 5% | 1202 | 11 | +19% | -76% | -76% | -73% |
| Momentum model ≥ 10% | 819 | 8 | +38% | -69% | -69% | -64% |
| Mean-reversion model ≥ 2% | 3902 | 27 | -25% | -85% | -85% | -82% |
| Mean-reversion model ≥ 5% | 2663 | 20 | -17% | -83% | -82% | -79% |
| Mean-reversion model ≥ 10% | 1757 | 14 | -8% | -81% | -81% | -78% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 11120 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 3989 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 1449 | 2% | 1% | 1% | 1% | 0% | 0% |
| **All** | 16558 | 3% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 63 | 0% | -$1,123.95 | -56% | — |
| Sell at 2¢ | 565 | 3% | -$1,817.05 | -91% | 33 sec |
| Sell at 3¢ | 373 | 2% | -$1,818.48 | -91% | 46 sec |
| Sell at 5¢ | 268 | 2% | -$1,789.75 | -89% | 49 sec |
| Sell at 10¢ | 174 | 1% | -$1,708.01 | -85% | 63 sec |
| Sell at 25¢ | 99 | 1% | -$1,580.26 | -79% | 79 sec |
| Sell at 50¢ | 64 | 0% | -$1,419.95 | -71% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 465 | 4 | 11% | 3% | -19% | -80% | -86% |
| 2–5 min | 5356 | 32 | 6% | 3% | -41% | -88% | -89% |
| 1–2 min | 4367 | 16 | 3% | 2% | -60% | -94% | -94% |
| Under 1 min | 6366 | 11 | 1% | 0% | -75% | -91% | -91% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 1248 | 7 | 4% | 2% | -31% | -90% | -90% |
| HYPE | 1245 | 4 | 4% | 2% | -60% | -90% | -89% |
| DOGE | 1239 | 2 | 4% | 2% | -80% | -91% | -90% |
| BNB | 1238 | 5 | 4% | 2% | -51% | -91% | -91% |
| ETH | 1237 | 8 | 5% | 2% | -21% | -90% | -89% |
| SOL | 1236 | 2 | 3% | 1% | -80% | -93% | -92% |
| BTC | 1229 | 6 | 5% | 2% | -35% | -88% | -91% |
| NEAR | 1224 | 7 | 5% | 2% | -26% | -77% | -77% |
| XRP | 1224 | 7 | 2% | 1% | -29% | -85% | -85% |
| GOLD | 656 | 0 | 3% | 1% | -100% | -93% | -95% |
| SILVER | 638 | 1 | 3% | 1% | -82% | -94% | -93% |
| WTI | 610 | 3 | 3% | 1% | -44% | -94% | -96% |
| COPPER | 570 | 0 | 1% | 1% | -100% | -98% | -97% |
| PLATINUM | 528 | 0 | 0% | 0% | -100% | -99% | -99% |
| PALLADIUM | 498 | 1 | 1% | 0% | -81% | -98% | -98% |
| NATGAS | 489 | 3 | 3% | 2% | -43% | -95% | -94% |
| EURUSD | 476 | 3 | 3% | 2% | -41% | -76% | -75% |
| GBPUSD | 451 | 1 | 2% | 1% | -79% | -96% | -96% |
| USDJPY | 412 | 3 | 1% | 1% | -32% | -98% | -97% |
| AUDUSD | 56 | 0 | 0% | 0% | -100% | -100% | -100% |
| USDCAD | 54 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 8356 | 34 | 3% | 2% | -53% | -90% | -89% |
| DOWN (bought NO) | 8202 | 29 | 3% | 2% | -59% | -91% | -92% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 1955 | 10 | 2% | 1% | -15% | -77% | -77% |
| 0.05–0.1% | 1966 | 6 | 3% | 1% | -56% | -92% | -92% |
| 0.1–0.2% | 2830 | 9 | 4% | 2% | -61% | -91% | -92% |
| 0.2–0.5% | 3140 | 18 | 6% | 3% | -37% | -89% | -89% |
| Over 0.5% | 1226 | 5 | 6% | 2% | -58% | -88% | -90% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 4310 | 20 | 4% | 2% | -47% | -87% | -87% |
| Morning (6am–12pm) | 3780 | 20 | 4% | 2% | -39% | -91% | -91% |
| Afternoon (12–6pm) | 3818 | 9 | 3% | 1% | -72% | -91% | -91% |
| Evening (6pm–12am) | 4650 | 14 | 3% | 1% | -66% | -94% | -94% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 25 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,492 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/13 5:29:55 AM | GOLD | UP | 5 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/13 5:29:39 AM | PLATINUM | UP | 20 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/13 5:29:39 AM | COPPER | UP | 20 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/13 5:29:23 AM | USDJPY | DOWN | 36 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/13 5:28:04 AM | PALLADIUM | UP | 1.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/13 5:27:48 AM | WTI | DOWN | 2.2 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/13 5:27:01 AM | NEAR | DOWN | 3.0 min | +1.125% | 1¢ | ❌ Lost | -$0.15 |
| 10/13 5:26:13 AM | DOGE | DOWN | 3.8 min | +0.607% | 0¢ | ❌ Lost | -$0.15 |
| 10/13 5:25:26 AM | BTC | DOWN | 4.5 min | +0.431% | 1¢ | ❌ Lost | -$0.15 |
| 10/13 5:24:38 AM | ETH | DOWN | 5.3 min | +0.735% | 1¢ | ❌ Lost | -$0.15 |
| 10/13 5:23:50 AM | SOL | DOWN | 6.2 min | +1.404% | 1¢ | ❌ Lost | -$0.15 |
| 10/13 5:23:19 AM | BNB | DOWN | 6.7 min | +0.363% | 3¢ | ❌ Lost | -$0.15 |
| 10/13 5:23:19 AM | XRP | DOWN | 6.7 min | +1.066% | 1¢ | ❌ Lost | -$0.15 |
| 10/13 5:23:19 AM | ZEC | DOWN | 6.7 min | +1.537% | 4¢ | ❌ Lost | -$0.15 |
| 10/13 5:23:19 AM | HYPE | DOWN | 6.7 min | +1.164% | 1¢ | ❌ Lost | -$0.15 |
| 10/13 5:14:47 AM | PALLADIUM | DOWN | 12 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/13 5:14:47 AM | WTI | DOWN | 12 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/13 5:14:47 AM | EURUSD | DOWN | 12 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/13 5:14:31 AM | NATGAS | DOWN | 28 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/13 5:14:15 AM | USDJPY | UP | 44 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/13 5:13:10 AM | PLATINUM | DOWN | 1.8 min | — | 3¢ | ❌ Lost | -$0.15 |
| 10/13 5:13:10 AM | BTC | UP | 1.8 min | -0.127% | 1¢ | ❌ Lost | -$0.15 |
| 10/13 5:12:55 AM | SILVER | DOWN | 2.1 min | — | 5¢ | ❌ Lost | -$0.15 |
| 10/13 5:12:55 AM | ETH | UP | 2.1 min | -0.165% | 0¢ | ❌ Lost | $0.00 |
| 10/13 5:12:40 AM | NEAR | UP | 2.3 min | -0.650% | 1¢ | ❌ Lost | -$0.15 |
| 10/13 5:11:35 AM | XRP | UP | 3.4 min | -0.449% | 1¢ | ❌ Lost | -$0.15 |
| 10/13 5:11:35 AM | HYPE | UP | 3.4 min | -0.328% | 1¢ | ❌ Lost | -$0.15 |
| 10/13 5:10:33 AM | GOLD | DOWN | 4.4 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/13 5:10:33 AM | BNB | UP | 4.4 min | -0.173% | 6¢ | ❌ Lost | -$0.15 |
| 10/13 5:10:17 AM | DOGE | UP | 4.7 min | -0.347% | 10¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
