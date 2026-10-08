# 15-Minute 1¢ Study

*Updated Thu Oct 8, 4:50 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 774 finished bets | 1% | $28.45 | +34% | +3.68¢ | -$13.25 / $41.70 |

*Expect about **76 buys a day** (~$11.41/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 765 | $16.40 | +20% |
| 5+ min left, hold to the close | 315 | $9.50 | +20% |
| Volatility model ≥ 5%, sell at 50¢ | 774 | -$1.55 | -2% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 11600 | 11593 | 49 (0%) | 1.07% | -$721.60 (-51%) | Hold to the close: -$721.60 (-51%) |

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
| Volatility model | 7460 | 4.0% | 0.4% (33) | -562% | ❌ Worse |
| Momentum model | 7460 | 4.1% | 0.4% (33) | -594% | ❌ Worse |
| Mean-reversion model | 7460 | 6.7% | 0.4% (33) | -659% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 7460 | 33 | -45% | -87% | -87% | -85% |
| Volatility model ≥ 2% | 1411 | 12 | -1% | -73% | -73% | -70% |
| Volatility model ≥ 5% | 774 | 8 | +34% | -63% | -62% | -59% |
| Volatility model ≥ 10% | 484 | 6 | +82% | -47% | -48% | -43% |
| Momentum model ≥ 2% | 1251 | 10 | -3% | -74% | -76% | -73% |
| Momentum model ≥ 5% | 765 | 7 | +20% | -67% | -69% | -66% |
| Momentum model ≥ 10% | 530 | 6 | +62% | -57% | -58% | -54% |
| Mean-reversion model ≥ 2% | 2564 | 19 | -20% | -84% | -85% | -81% |
| Mean-reversion model ≥ 5% | 1734 | 15 | -4% | -82% | -81% | -76% |
| Mean-reversion model ≥ 10% | 1147 | 11 | +10% | -80% | -80% | -75% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 7657 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 2941 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 995 | 3% | 2% | 2% | 1% | 1% | 0% |
| **All** | 11593 | 3% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 49 | 0% | -$721.60 | -51% | — |
| Sell at 2¢ | 401 | 3% | -$1,261.34 | -90% | 33 sec |
| Sell at 3¢ | 267 | 2% | -$1,261.47 | -90% | 47 sec |
| Sell at 5¢ | 198 | 2% | -$1,236.90 | -88% | 56 sec |
| Sell at 10¢ | 131 | 1% | -$1,179.99 | -84% | 64 sec |
| Sell at 25¢ | 75 | 1% | -$1,075.35 | -76% | 82 sec |
| Sell at 50¢ | 49 | 0% | -$950.85 | -68% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 311 | 4 | 11% | 4% | +22% | -81% | -85% |
| 2–5 min | 3770 | 25 | 6% | 3% | -35% | -88% | -88% |
| 1–2 min | 3041 | 12 | 3% | 2% | -57% | -94% | -94% |
| Under 1 min | 4467 | 8 | 1% | 0% | -74% | -88% | -88% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 858 | 6 | 5% | 3% | -17% | -90% | -90% |
| HYPE | 857 | 3 | 5% | 3% | -57% | -89% | -88% |
| DOGE | 853 | 2 | 3% | 1% | -70% | -92% | -92% |
| BNB | 852 | 3 | 4% | 2% | -58% | -91% | -92% |
| ETH | 851 | 7 | 5% | 3% | +2% | -89% | -88% |
| NEAR | 848 | 5 | 6% | 3% | -23% | -71% | -72% |
| SOL | 847 | 0 | 3% | 1% | -100% | -93% | -92% |
| BTC | 846 | 4 | 5% | 2% | -38% | -88% | -90% |
| XRP | 845 | 5 | 2% | 1% | -26% | -81% | -81% |
| GOLD | 492 | 0 | 4% | 1% | -100% | -92% | -93% |
| SILVER | 477 | 0 | 3% | 1% | -100% | -94% | -94% |
| WTI | 454 | 3 | 2% | 1% | -28% | -95% | -97% |
| COPPER | 420 | 0 | 1% | 0% | -100% | -99% | -99% |
| PLATINUM | 382 | 0 | 0% | 0% | -100% | -100% | -99% |
| NATGAS | 360 | 3 | 3% | 2% | -22% | -95% | -93% |
| PALLADIUM | 356 | 1 | 1% | 1% | -74% | -98% | -99% |
| EURUSD | 354 | 3 | 3% | 2% | -21% | -68% | -66% |
| GBPUSD | 332 | 1 | 3% | 2% | -72% | -95% | -95% |
| USDJPY | 296 | 3 | 1% | 1% | -5% | -98% | -96% |
| AUDUSD | 7 | 0 | 0% | 0% | -100% | -100% | -100% |
| USDCAD | 6 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 5891 | 26 | 3% | 2% | -49% | -89% | -88% |
| DOWN (bought NO) | 5702 | 23 | 3% | 2% | -54% | -91% | -91% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 1257 | 8 | 2% | 1% | +10% | -67% | -66% |
| 0.05–0.1% | 1305 | 4 | 3% | 1% | -55% | -91% | -92% |
| 0.1–0.2% | 1949 | 6 | 4% | 2% | -62% | -92% | -92% |
| 0.2–0.5% | 2254 | 12 | 6% | 3% | -42% | -89% | -88% |
| Over 0.5% | 890 | 5 | 6% | 2% | -42% | -88% | -90% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 3060 | 17 | 4% | 2% | -36% | -84% | -85% |
| Morning (6am–12pm) | 2706 | 17 | 4% | 2% | -28% | -91% | -90% |
| Afternoon (12–6pm) | 2560 | 7 | 3% | 1% | -68% | -88% | -89% |
| Evening (6pm–12am) | 3267 | 8 | 3% | 1% | -72% | -94% | -94% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 25 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,068 |
| Time from buy to best bounce (bounced bets) | 49 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/8 4:44:43 AM | SOL | UP | 17 sec | -0.008% | 0¢ | ❌ Lost | -$0.15 |
| 10/8 4:44:43 AM | AUDUSD | UP | 17 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/8 4:44:12 AM | GBPUSD | DOWN | 47 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/8 4:43:56 AM | USDJPY | DOWN | 63 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/8 4:43:56 AM | NATGAS | DOWN | 63 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/8 4:42:52 AM | WTI | DOWN | 2.1 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/8 4:42:36 AM | XRP | UP | 2.4 min | -0.299% | 0¢ | ❌ Lost | $0.00 |
| 10/8 4:42:36 AM | BTC | UP | 2.4 min | -0.154% | 1¢ | ❌ Lost | -$0.15 |
| 10/8 4:42:36 AM | HYPE | UP | 2.4 min | -0.212% | 1¢ | ❌ Lost | -$0.15 |
| 10/8 4:42:20 AM | PALLADIUM | UP | 2.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/8 4:42:20 AM | ETH | UP | 2.6 min | -0.249% | 0¢ | ❌ Lost | $0.00 |
| 10/8 4:42:20 AM | SILVER | UP | 2.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/8 4:42:04 AM | DOGE | UP | 2.9 min | -0.243% | 1¢ | ❌ Lost | -$0.15 |
| 10/8 4:42:04 AM | ZEC | UP | 2.9 min | -0.792% | 1¢ | ❌ Lost | -$0.15 |
| 10/8 4:41:48 AM | GOLD | UP | 3.2 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/8 4:39:54 AM | BNB | UP | 5.1 min | -0.264% | 1¢ | ❌ Lost | -$0.15 |
| 10/8 4:39:21 AM | PLATINUM | UP | 5.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/8 4:39:21 AM | COPPER | UP | 5.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/8 4:38:49 AM | NEAR | UP | 6.2 min | -1.058% | 1¢ | ❌ Lost | -$0.15 |
| 10/8 4:28:56 AM | USDCAD | UP | 63 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/8 4:28:08 AM | USDJPY | UP | 1.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/8 4:27:20 AM | COPPER | UP | 2.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/8 4:27:04 AM | SILVER | UP | 2.9 min | — | 2¢ | ❌ Lost | -$0.15 |
| 10/8 4:26:48 AM | NEAR | UP | 3.2 min | -0.827% | 1¢ | ❌ Lost | -$0.15 |
| 10/8 4:26:48 AM | GOLD | UP | 3.2 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/8 4:26:48 AM | DOGE | UP | 3.2 min | -0.295% | 1¢ | ❌ Lost | -$0.15 |
| 10/8 4:26:32 AM | BNB | UP | 3.5 min | -0.244% | 1¢ | ❌ Lost | -$0.15 |
| 10/8 4:26:16 AM | WTI | DOWN | 3.7 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/8 4:26:16 AM | SOL | UP | 3.7 min | -0.324% | 1¢ | ❌ Lost | -$0.15 |
| 10/8 4:25:44 AM | XRP | UP | 4.3 min | -0.382% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
