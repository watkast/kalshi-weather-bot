# 15-Minute 1¢ Study

*Updated Tue Oct 13, 10:47 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 1271 finished bets | 1% | $42.80 | +31% | +3.37¢ | $30.05 / $12.75 |

*Expect about **82 buys a day** (~$12.36/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 1218 | $22.90 | +17% |
| 5+ min left, hold to the close | 474 | -$14.20 | -20% |
| Volatility model ≥ 5%, sell at 50¢ | 1271 | -$16.20 | -12% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 16670 | 16663 | 63 (0%) | 1.07% | -$1,135.65 (-56%) | Hold to the close: -$1,135.65 (-56%) |

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
| Volatility model | 10984 | 4.5% | 0.4% (46) | -658% | ❌ Worse |
| Momentum model | 10984 | 4.5% | 0.4% (46) | -687% | ❌ Worse |
| Mean-reversion model | 10984 | 7.2% | 0.4% (46) | -770% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 10984 | 46 | -48% | -88% | -88% | -86% |
| Volatility model ≥ 2% | 2265 | 18 | -8% | -78% | -77% | -74% |
| Volatility model ≥ 5% | 1271 | 13 | +31% | -73% | -72% | -69% |
| Volatility model ≥ 10% | 786 | 9 | +64% | -63% | -62% | -59% |
| Momentum model ≥ 2% | 1992 | 15 | -9% | -79% | -80% | -78% |
| Momentum model ≥ 5% | 1218 | 11 | +17% | -76% | -76% | -73% |
| Momentum model ≥ 10% | 829 | 8 | +37% | -69% | -69% | -64% |
| Mean-reversion model ≥ 2% | 3934 | 27 | -25% | -85% | -85% | -82% |
| Mean-reversion model ≥ 5% | 2686 | 20 | -18% | -83% | -82% | -79% |
| Mean-reversion model ≥ 10% | 1769 | 14 | -8% | -81% | -81% | -78% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 11182 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 4017 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 1464 | 2% | 1% | 1% | 1% | 0% | 0% |
| **All** | 16663 | 3% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 63 | 0% | -$1,135.65 | -56% | — |
| Sell at 2¢ | 567 | 3% | -$1,828.23 | -91% | 33 sec |
| Sell at 3¢ | 375 | 2% | -$1,829.40 | -91% | 46 sec |
| Sell at 5¢ | 270 | 2% | -$1,800.15 | -89% | 49 sec |
| Sell at 10¢ | 174 | 1% | -$1,719.71 | -85% | 63 sec |
| Sell at 25¢ | 99 | 1% | -$1,591.96 | -79% | 79 sec |
| Sell at 50¢ | 64 | 0% | -$1,431.65 | -71% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 470 | 4 | 11% | 3% | -20% | -80% | -86% |
| 2–5 min | 5381 | 32 | 6% | 3% | -41% | -88% | -89% |
| 1–2 min | 4393 | 16 | 3% | 2% | -60% | -94% | -94% |
| Under 1 min | 6415 | 11 | 1% | 0% | -75% | -91% | -91% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 1255 | 7 | 4% | 2% | -31% | -90% | -90% |
| HYPE | 1252 | 4 | 4% | 2% | -61% | -90% | -89% |
| DOGE | 1246 | 2 | 4% | 2% | -80% | -91% | -90% |
| ETH | 1244 | 8 | 5% | 2% | -22% | -90% | -89% |
| BNB | 1244 | 5 | 4% | 2% | -51% | -91% | -91% |
| SOL | 1243 | 2 | 3% | 1% | -80% | -93% | -92% |
| BTC | 1236 | 6 | 5% | 2% | -36% | -88% | -90% |
| NEAR | 1231 | 7 | 5% | 2% | -26% | -77% | -78% |
| XRP | 1231 | 7 | 2% | 1% | -30% | -85% | -85% |
| GOLD | 660 | 0 | 3% | 1% | -100% | -93% | -94% |
| SILVER | 641 | 1 | 3% | 1% | -82% | -94% | -94% |
| WTI | 615 | 3 | 3% | 1% | -44% | -94% | -96% |
| COPPER | 572 | 0 | 1% | 1% | -100% | -98% | -97% |
| PLATINUM | 534 | 0 | 0% | 0% | -100% | -99% | -99% |
| PALLADIUM | 502 | 1 | 1% | 0% | -81% | -98% | -98% |
| NATGAS | 493 | 3 | 3% | 2% | -43% | -95% | -94% |
| EURUSD | 480 | 3 | 3% | 2% | -42% | -76% | -75% |
| GBPUSD | 455 | 1 | 2% | 1% | -79% | -96% | -96% |
| USDJPY | 415 | 3 | 1% | 1% | -33% | -98% | -97% |
| AUDUSD | 59 | 0 | 0% | 0% | -100% | -100% | -100% |
| USDCAD | 55 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 8409 | 34 | 3% | 2% | -53% | -90% | -90% |
| DOWN (bought NO) | 8254 | 29 | 3% | 2% | -59% | -91% | -92% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 1963 | 10 | 2% | 1% | -15% | -77% | -76% |
| 0.05–0.1% | 1983 | 6 | 3% | 1% | -56% | -92% | -92% |
| 0.1–0.2% | 2842 | 9 | 4% | 2% | -61% | -91% | -92% |
| 0.2–0.5% | 3154 | 18 | 5% | 3% | -37% | -89% | -89% |
| Over 0.5% | 1237 | 5 | 6% | 2% | -58% | -89% | -90% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 4344 | 20 | 4% | 2% | -47% | -87% | -87% |
| Morning (6am–12pm) | 3851 | 20 | 4% | 2% | -40% | -91% | -91% |
| Afternoon (12–6pm) | 3818 | 9 | 3% | 1% | -72% | -91% | -91% |
| Evening (6pm–12am) | 4650 | 14 | 3% | 1% | -66% | -94% | -94% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 25 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,481 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/13 10:44:56 AM | NATGAS | DOWN | 3 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/13 10:44:56 AM | PALLADIUM | UP | 3 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/13 10:44:56 AM | ZEC | UP | 3 sec | -0.032% | 0¢ | ❌ Lost | $0.00 |
| 10/13 10:44:40 AM | DOGE | UP | 19 sec | -0.058% | 0¢ | ❌ Lost | $0.00 |
| 10/13 10:44:24 AM | HYPE | UP | 35 sec | -0.219% | 0¢ | ❌ Lost | $0.00 |
| 10/13 10:43:52 AM | BNB | UP | 67 sec | -0.070% | 0¢ | ❌ Lost | $0.00 |
| 10/13 10:43:52 AM | NEAR | DOWN | 67 sec | +0.137% | 1¢ | ❌ Lost | -$0.15 |
| 10/13 10:43:52 AM | ETH | UP | 67 sec | -0.070% | 0¢ | ❌ Lost | -$0.15 |
| 10/13 10:43:52 AM | BTC | UP | 67 sec | -0.092% | 0¢ | ❌ Lost | $0.00 |
| 10/13 10:43:21 AM | XRP | UP | 1.6 min | -0.204% | 1¢ | ❌ Lost | -$0.15 |
| 10/13 10:43:05 AM | SOL | UP | 1.9 min | -0.166% | 1¢ | ❌ Lost | -$0.15 |
| 10/13 10:41:45 AM | GBPUSD | UP | 3.2 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/13 10:40:58 AM | WTI | DOWN | 4.0 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/13 10:29:56 AM | COPPER | UP | 3 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/13 10:29:56 AM | PLATINUM | UP | 3 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/13 10:29:56 AM | PALLADIUM | UP | 3 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/13 10:29:56 AM | SILVER | UP | 3 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/13 10:29:40 AM | NEAR | DOWN | 19 sec | -0.067% | 0¢ | ❌ Lost | $0.00 |
| 10/13 10:29:40 AM | EURUSD | UP | 19 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/13 10:29:40 AM | ETH | DOWN | 19 sec | +0.032% | 0¢ | ❌ Lost | -$0.15 |
| 10/13 10:29:24 AM | DOGE | DOWN | 35 sec | +0.054% | 0¢ | ❌ Lost | $0.00 |
| 10/13 10:29:24 AM | SOL | DOWN | 35 sec | +0.163% | 0¢ | ❌ Lost | $0.00 |
| 10/13 10:29:08 AM | BNB | DOWN | 51 sec | +0.020% | 0¢ | ❌ Lost | $0.00 |
| 10/13 10:29:08 AM | XRP | DOWN | 51 sec | +0.095% | 0¢ | ❌ Lost | -$0.15 |
| 10/13 10:28:21 AM | GOLD | UP | 1.6 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/13 10:27:49 AM | BTC | DOWN | 2.2 min | +0.121% | 1¢ | ❌ Lost | -$0.15 |
| 10/13 10:26:09 AM | ZEC | DOWN | 3.8 min | +0.570% | 0¢ | ❌ Lost | $0.00 |
| 10/13 10:23:14 AM | HYPE | DOWN | 6.8 min | +0.787% | 1¢ | ❌ Lost | -$0.15 |
| 10/13 10:14:57 AM | PLATINUM | UP | 2 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/13 10:14:57 AM | GOLD | DOWN | 2 sec | — | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
