# 15-Minute 1¢ Study

*Updated Fri Oct 16, 11:23 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 1634 finished bets | 1% | $84.80 | +47% | +5.19¢ | $37.50 / $47.30 |

*Expect about **89 buys a day** (~$13.29/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 1513 | $46.35 | +28% |
| Momentum model ≥ 2%, hold to the close | 2560 | -$2.25 | -1% |
| Volatility model ≥ 5%, sell at 50¢ | 1634 | -$17.70 | -10% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 21040 | 21033 | 80 (0%) | 1.07% | -$1,443.20 (-56%) | Hold to the close: -$1,443.20 (-56%) |

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
| Volatility model | 13420 | 4.4% | 0.4% (54) | -638% | ❌ Worse |
| Momentum model | 13420 | 4.4% | 0.4% (54) | -661% | ❌ Worse |
| Mean-reversion model | 13420 | 7.4% | 0.4% (54) | -769% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 13420 | 54 | -50% | -88% | -88% | -85% |
| Volatility model ≥ 2% | 2984 | 24 | -7% | -78% | -78% | -74% |
| Volatility model ≥ 5% | 1634 | 19 | +47% | -74% | -72% | -68% |
| Volatility model ≥ 10% | 953 | 11 | +65% | -65% | -64% | -61% |
| Momentum model ≥ 2% | 2560 | 21 | -1% | -80% | -80% | -77% |
| Momentum model ≥ 5% | 1513 | 15 | +28% | -77% | -77% | -73% |
| Momentum model ≥ 10% | 1008 | 10 | +40% | -71% | -71% | -66% |
| Mean-reversion model ≥ 2% | 5065 | 34 | -27% | -84% | -84% | -81% |
| Mean-reversion model ≥ 5% | 3486 | 27 | -15% | -82% | -81% | -78% |
| Mean-reversion model ≥ 10% | 2288 | 16 | -20% | -80% | -80% | -77% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 13618 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 5232 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 2183 | 2% | 1% | 1% | 1% | 0% | 0% |
| **All** | 21033 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 80 | 0% | -$1,443.20 | -56% | — |
| Sell at 2¢ | 748 | 4% | -$2,270.72 | -89% | 42 sec |
| Sell at 3¢ | 504 | 2% | -$2,268.64 | -89% | 47 sec |
| Sell at 5¢ | 364 | 2% | -$2,228.60 | -87% | 50 sec |
| Sell at 10¢ | 219 | 1% | -$2,150.31 | -84% | 63 sec |
| Sell at 25¢ | 126 | 1% | -$1,978.14 | -77% | 80 sec |
| Sell at 50¢ | 83 | 0% | -$1,764.95 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 701 | 5 | 10% | 3% | -32% | -82% | -85% |
| 2–5 min | 6836 | 37 | 7% | 3% | -47% | -88% | -88% |
| 1–2 min | 5469 | 20 | 3% | 2% | -60% | -92% | -92% |
| Under 1 min | 8023 | 18 | 1% | 0% | -68% | -87% | -87% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 1529 | 11 | 5% | 3% | -11% | -89% | -89% |
| HYPE | 1524 | 5 | 4% | 2% | -60% | -90% | -89% |
| ETH | 1519 | 8 | 5% | 3% | -36% | -88% | -87% |
| DOGE | 1515 | 2 | 4% | 2% | -83% | -90% | -90% |
| BNB | 1515 | 6 | 5% | 2% | -51% | -89% | -89% |
| SOL | 1512 | 2 | 3% | 2% | -84% | -92% | -91% |
| XRP | 1503 | 7 | 2% | 1% | -42% | -86% | -87% |
| BTC | 1502 | 7 | 5% | 2% | -38% | -88% | -91% |
| NEAR | 1499 | 8 | 6% | 3% | -30% | -78% | -78% |
| GOLD | 854 | 1 | 4% | 1% | -86% | -92% | -94% |
| SILVER | 829 | 4 | 3% | 1% | -45% | -79% | -80% |
| WTI | 799 | 3 | 3% | 1% | -56% | -94% | -95% |
| COPPER | 729 | 2 | 2% | 1% | -74% | -84% | -84% |
| PLATINUM | 712 | 0 | 1% | 0% | -100% | -99% | -99% |
| NATGAS | 655 | 5 | 2% | 2% | -29% | -82% | -81% |
| PALLADIUM | 654 | 2 | 1% | 0% | -71% | -84% | -84% |
| EURUSD | 648 | 3 | 3% | 1% | -57% | -81% | -81% |
| GBPUSD | 609 | 1 | 2% | 1% | -85% | -97% | -97% |
| USDJPY | 570 | 3 | 1% | 1% | -51% | -99% | -98% |
| AUDUSD | 192 | 0 | 1% | 0% | -100% | -99% | -99% |
| USDCAD | 164 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 10621 | 40 | 4% | 2% | -57% | -89% | -89% |
| DOWN (bought NO) | 10412 | 40 | 4% | 2% | -56% | -88% | -88% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 2241 | 11 | 2% | 1% | -17% | -79% | -79% |
| 0.05–0.1% | 2338 | 7 | 3% | 1% | -56% | -92% | -92% |
| 0.1–0.2% | 3445 | 11 | 4% | 2% | -60% | -90% | -90% |
| 0.2–0.5% | 4009 | 21 | 6% | 3% | -42% | -88% | -88% |
| Over 0.5% | 1582 | 6 | 6% | 3% | -61% | -88% | -89% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 5359 | 20 | 4% | 2% | -58% | -87% | -88% |
| Morning (6am–12pm) | 5050 | 27 | 4% | 2% | -39% | -87% | -86% |
| Afternoon (12–6pm) | 4822 | 16 | 3% | 1% | -61% | -88% | -89% |
| Evening (6pm–12am) | 5802 | 17 | 3% | 2% | -67% | -92% | -91% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,423 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/16 11:14:41 AM | USDJPY | UP | 18 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/16 11:14:41 AM | WTI | DOWN | 18 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/16 11:13:51 AM | GOLD | UP | 69 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/16 11:13:35 AM | HYPE | UP | 85 sec | -0.275% | 0¢ | ❌ Lost | -$0.15 |
| 10/16 11:13:35 AM | ZEC | UP | 85 sec | -0.387% | 1¢ | ❌ Lost | -$0.15 |
| 10/16 11:13:35 AM | PALLADIUM | UP | 85 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/16 11:13:04 AM | SILVER | UP | 1.9 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/16 11:12:48 AM | XRP | UP | 2.2 min | -0.414% | 1¢ | ❌ Lost | -$0.15 |
| 10/16 11:12:32 AM | COPPER | UP | 2.5 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/16 11:12:16 AM | PLATINUM | UP | 2.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/16 11:12:16 AM | GBPUSD | UP | 2.7 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/16 11:12:16 AM | DOGE | UP | 2.7 min | -0.342% | 0¢ | ❌ Lost | -$0.15 |
| 10/16 11:12:00 AM | SOL | UP | 3.0 min | -0.331% | 1¢ | ❌ Lost | -$0.15 |
| 10/16 11:11:42 AM | USDCAD | DOWN | 3.3 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/16 11:11:10 AM | BNB | UP | 3.8 min | -0.230% | 0¢ | ❌ Lost | -$0.15 |
| 10/16 11:10:55 AM | NEAR | UP | 4.1 min | -0.835% | 1¢ | ❌ Lost | -$0.15 |
| 10/16 11:10:55 AM | BTC | UP | 4.1 min | -0.296% | 1¢ | ❌ Lost | -$0.15 |
| 10/16 11:10:07 AM | AUDUSD | UP | 4.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/16 11:08:30 AM | ETH | UP | 6.5 min | -0.618% | 1¢ | ❌ Lost | -$0.15 |
| 10/16 10:59:53 AM | EURUSD | DOWN | 7 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/16 10:59:37 AM | PLATINUM | UP | 23 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/16 10:59:06 AM | HYPE | DOWN | 53 sec | +0.208% | 1¢ | ❌ Lost | -$0.15 |
| 10/16 10:58:50 AM | NATGAS | DOWN | 69 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/16 10:58:18 AM | USDCAD | UP | 1.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/16 10:57:14 AM | PALLADIUM | UP | 2.8 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/16 10:57:14 AM | BTC | UP | 2.8 min | -0.166% | 1¢ | ❌ Lost | -$0.15 |
| 10/16 10:57:14 AM | SILVER | UP | 2.8 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/16 10:56:25 AM | BNB | UP | 3.6 min | -0.287% | 0¢ | ❌ Lost | $0.00 |
| 10/16 10:56:25 AM | GOLD | UP | 3.6 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/16 10:56:09 AM | XRP | UP | 3.8 min | -0.465% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
