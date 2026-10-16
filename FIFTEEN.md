# 15-Minute 1¢ Study

*Updated Fri Oct 16, 5:36 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 1611 finished bets | 1% | $73.35 | +41% | +4.55¢ | $39.00 / $34.35 |

*Expect about **88 buys a day** (~$13.27/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 1497 | $48.00 | +30% |
| Momentum model ≥ 2%, hold to the close | 2521 | -$12.20 | -4% |
| Volatility model ≥ 5%, sell at 50¢ | 1611 | -$21.90 | -12% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 20662 | 20655 | 79 (0%) | 1.07% | -$1,408.30 (-56%) | Hold to the close: -$1,408.30 (-56%) |

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
| Volatility model | 13218 | 4.4% | 0.4% (53) | -644% | ❌ Worse |
| Momentum model | 13218 | 4.4% | 0.4% (53) | -668% | ❌ Worse |
| Mean-reversion model | 13218 | 7.4% | 0.4% (53) | -772% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 13218 | 53 | -50% | -88% | -88% | -86% |
| Volatility model ≥ 2% | 2933 | 23 | -9% | -79% | -78% | -74% |
| Volatility model ≥ 5% | 1611 | 18 | +41% | -74% | -72% | -68% |
| Volatility model ≥ 10% | 946 | 11 | +66% | -65% | -64% | -60% |
| Momentum model ≥ 2% | 2521 | 20 | -4% | -80% | -80% | -77% |
| Momentum model ≥ 5% | 1497 | 15 | +30% | -77% | -77% | -73% |
| Momentum model ≥ 10% | 1000 | 10 | +41% | -72% | -71% | -66% |
| Mean-reversion model ≥ 2% | 4956 | 33 | -27% | -84% | -84% | -81% |
| Mean-reversion model ≥ 5% | 3404 | 26 | -16% | -82% | -82% | -78% |
| Mean-reversion model ≥ 10% | 2233 | 15 | -23% | -80% | -80% | -77% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 13416 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 5122 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 2117 | 2% | 1% | 1% | 1% | 0% | 0% |
| **All** | 20655 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 79 | 0% | -$1,408.30 | -56% | — |
| Sell at 2¢ | 730 | 4% | -$2,226.50 | -89% | 42 sec |
| Sell at 3¢ | 488 | 2% | -$2,225.98 | -89% | 47 sec |
| Sell at 5¢ | 354 | 2% | -$2,186.20 | -87% | 50 sec |
| Sell at 10¢ | 218 | 1% | -$2,102.72 | -84% | 63 sec |
| Sell at 25¢ | 125 | 1% | -$1,932.55 | -77% | 80 sec |
| Sell at 50¢ | 82 | 0% | -$1,722.80 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 668 | 5 | 10% | 3% | -29% | -82% | -86% |
| 2–5 min | 6696 | 36 | 7% | 3% | -47% | -88% | -88% |
| 1–2 min | 5385 | 20 | 3% | 2% | -60% | -92% | -92% |
| Under 1 min | 7902 | 18 | 1% | 0% | -67% | -87% | -87% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 1506 | 11 | 5% | 3% | -9% | -89% | -90% |
| HYPE | 1502 | 5 | 4% | 2% | -59% | -90% | -89% |
| ETH | 1496 | 8 | 5% | 3% | -35% | -88% | -87% |
| DOGE | 1492 | 2 | 4% | 2% | -83% | -90% | -89% |
| BNB | 1492 | 5 | 4% | 2% | -59% | -90% | -90% |
| SOL | 1489 | 2 | 3% | 2% | -83% | -92% | -91% |
| XRP | 1483 | 7 | 2% | 1% | -42% | -86% | -87% |
| BTC | 1479 | 7 | 5% | 2% | -37% | -88% | -91% |
| NEAR | 1477 | 8 | 5% | 3% | -29% | -78% | -78% |
| GOLD | 837 | 1 | 4% | 1% | -86% | -92% | -94% |
| SILVER | 812 | 4 | 3% | 1% | -43% | -79% | -79% |
| WTI | 779 | 3 | 3% | 1% | -55% | -94% | -96% |
| COPPER | 715 | 2 | 2% | 1% | -74% | -84% | -83% |
| PLATINUM | 695 | 0 | 1% | 0% | -100% | -99% | -99% |
| PALLADIUM | 644 | 2 | 1% | 0% | -71% | -84% | -84% |
| NATGAS | 640 | 5 | 2% | 2% | -27% | -81% | -80% |
| EURUSD | 635 | 3 | 3% | 1% | -56% | -81% | -80% |
| GBPUSD | 594 | 1 | 2% | 1% | -84% | -97% | -96% |
| USDJPY | 558 | 3 | 1% | 1% | -50% | -99% | -98% |
| AUDUSD | 177 | 0 | 1% | 0% | -100% | -99% | -99% |
| USDCAD | 153 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 10390 | 39 | 4% | 2% | -57% | -89% | -89% |
| DOWN (bought NO) | 10265 | 40 | 4% | 2% | -55% | -88% | -88% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 2226 | 11 | 2% | 1% | -17% | -79% | -79% |
| 0.05–0.1% | 2321 | 7 | 3% | 1% | -56% | -92% | -91% |
| 0.1–0.2% | 3401 | 10 | 4% | 2% | -64% | -90% | -90% |
| 0.2–0.5% | 3926 | 21 | 6% | 3% | -41% | -88% | -88% |
| Over 0.5% | 1539 | 6 | 6% | 2% | -60% | -88% | -89% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 5330 | 20 | 4% | 2% | -58% | -88% | -88% |
| Morning (6am–12pm) | 4701 | 26 | 4% | 2% | -36% | -86% | -86% |
| Afternoon (12–6pm) | 4822 | 16 | 3% | 1% | -61% | -88% | -89% |
| Evening (6pm–12am) | 5802 | 17 | 3% | 2% | -67% | -92% | -91% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,432 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/16 5:29:42 AM | WTI | DOWN | 18 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/16 5:29:26 AM | SOL | UP | 34 sec | -0.160% | 0¢ | ❌ Lost | $0.00 |
| 10/16 5:29:26 AM | COPPER | DOWN | 34 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/16 5:29:26 AM | SILVER | DOWN | 34 sec | — | 4¢ | ❌ Lost | -$0.15 |
| 10/16 5:28:53 AM | NATGAS | UP | 66 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/16 5:28:37 AM | DOGE | DOWN | 82 sec | +0.128% | 2¢ | ❌ Lost | -$0.15 |
| 10/16 5:28:37 AM | ZEC | DOWN | 82 sec | +0.299% | 1¢ | ❌ Lost | -$0.15 |
| 10/16 5:28:37 AM | ETH | DOWN | 82 sec | +0.256% | 0¢ | ❌ Lost | $0.00 |
| 10/16 5:27:35 AM | XRP | DOWN | 2.4 min | +0.319% | 0¢ | ❌ Lost | -$0.15 |
| 10/16 5:27:19 AM | NEAR | DOWN | 2.7 min | +0.484% | 1¢ | ❌ Lost | -$0.15 |
| 10/16 5:26:26 AM | BNB | DOWN | 3.5 min | +0.181% | 0¢ | ❌ Lost | -$0.15 |
| 10/16 5:25:54 AM | BTC | DOWN | 4.1 min | +0.345% | 1¢ | ❌ Lost | -$0.15 |
| 10/16 5:25:38 AM | HYPE | DOWN | 4.3 min | +0.329% | 1¢ | ❌ Lost | -$0.15 |
| 10/16 5:25:21 AM | GOLD | DOWN | 4.6 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/16 5:14:40 AM | WTI | DOWN | 20 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/16 5:14:40 AM | PALLADIUM | DOWN | 20 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/16 5:14:40 AM | GOLD | DOWN | 20 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/16 5:13:51 AM | PLATINUM | DOWN | 69 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/16 5:13:35 AM | HYPE | DOWN | 85 sec | +0.240% | 1¢ | ❌ Lost | -$0.15 |
| 10/16 5:13:35 AM | BNB | DOWN | 85 sec | +0.145% | 0¢ | ❌ Lost | -$0.15 |
| 10/16 5:13:35 AM | ZEC | DOWN | 85 sec | +0.494% | 0¢ | ❌ Lost | $0.00 |
| 10/16 5:13:02 AM | XRP | DOWN | 1.9 min | +0.261% | 1¢ | ❌ Lost | -$0.15 |
| 10/16 5:12:44 AM | NEAR | DOWN | 2.2 min | +0.430% | 1¢ | ❌ Lost | -$0.15 |
| 10/16 5:12:44 AM | DOGE | DOWN | 2.2 min | +0.328% | 0¢ | ❌ Lost | -$0.15 |
| 10/16 5:12:44 AM | SOL | DOWN | 2.2 min | +0.277% | 1¢ | ❌ Lost | -$0.15 |
| 10/16 5:12:12 AM | COPPER | DOWN | 2.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/16 5:11:58 AM | ETH | DOWN | 3.0 min | +0.333% | 1¢ | ❌ Lost | -$0.15 |
| 10/16 5:11:40 AM | BTC | DOWN | 3.3 min | +0.187% | 1¢ | ❌ Lost | -$0.15 |
| 10/16 5:11:24 AM | SILVER | DOWN | 3.6 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/16 5:11:08 AM | USDJPY | DOWN | 3.9 min | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
