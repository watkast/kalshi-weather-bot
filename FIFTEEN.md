# 15-Minute 1¢ Study

*Updated Fri Oct 16, 11:03 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 1633 finished bets | 1% | $84.95 | +47% | +5.20¢ | $37.65 / $47.30 |

*Expect about **89 buys a day** (~$13.29/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 1512 | $46.50 | +28% |
| Momentum model ≥ 2%, hold to the close | 2559 | -$2.10 | -1% |
| Volatility model ≥ 5%, sell at 50¢ | 1633 | -$17.55 | -10% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 21021 | 21014 | 80 (0%) | 1.07% | -$1,440.35 (-56%) | Hold to the close: -$1,440.35 (-56%) |

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
| Volatility model | 13411 | 4.4% | 0.4% (54) | -638% | ❌ Worse |
| Momentum model | 13411 | 4.4% | 0.4% (54) | -661% | ❌ Worse |
| Mean-reversion model | 13411 | 7.4% | 0.4% (54) | -769% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 13411 | 54 | -50% | -88% | -88% | -85% |
| Volatility model ≥ 2% | 2983 | 24 | -7% | -78% | -78% | -74% |
| Volatility model ≥ 5% | 1633 | 19 | +47% | -74% | -72% | -68% |
| Volatility model ≥ 10% | 953 | 11 | +65% | -65% | -64% | -61% |
| Momentum model ≥ 2% | 2559 | 21 | -1% | -80% | -80% | -77% |
| Momentum model ≥ 5% | 1512 | 15 | +28% | -77% | -77% | -73% |
| Momentum model ≥ 10% | 1007 | 10 | +40% | -71% | -71% | -66% |
| Mean-reversion model ≥ 2% | 5059 | 34 | -27% | -84% | -84% | -81% |
| Mean-reversion model ≥ 5% | 3481 | 27 | -14% | -82% | -81% | -78% |
| Mean-reversion model ≥ 10% | 2286 | 16 | -20% | -80% | -80% | -77% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 13609 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 5226 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 2179 | 2% | 1% | 1% | 1% | 0% | 0% |
| **All** | 21014 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 80 | 0% | -$1,440.35 | -56% | — |
| Sell at 2¢ | 748 | 4% | -$2,267.87 | -89% | 42 sec |
| Sell at 3¢ | 504 | 2% | -$2,265.79 | -88% | 47 sec |
| Sell at 5¢ | 364 | 2% | -$2,225.75 | -87% | 50 sec |
| Sell at 10¢ | 219 | 1% | -$2,147.46 | -84% | 63 sec |
| Sell at 25¢ | 126 | 1% | -$1,975.29 | -77% | 80 sec |
| Sell at 50¢ | 83 | 0% | -$1,762.10 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 700 | 5 | 10% | 3% | -32% | -82% | -85% |
| 2–5 min | 6825 | 37 | 7% | 3% | -47% | -88% | -88% |
| 1–2 min | 5464 | 20 | 3% | 2% | -60% | -92% | -92% |
| Under 1 min | 8021 | 18 | 1% | 0% | -68% | -87% | -87% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 1528 | 11 | 5% | 3% | -11% | -89% | -89% |
| HYPE | 1523 | 5 | 4% | 2% | -60% | -90% | -89% |
| ETH | 1518 | 8 | 5% | 3% | -36% | -88% | -87% |
| DOGE | 1514 | 2 | 4% | 2% | -83% | -90% | -90% |
| BNB | 1514 | 6 | 5% | 2% | -51% | -89% | -89% |
| SOL | 1511 | 2 | 3% | 2% | -84% | -92% | -91% |
| XRP | 1502 | 7 | 2% | 1% | -42% | -86% | -87% |
| BTC | 1501 | 7 | 5% | 2% | -38% | -88% | -91% |
| NEAR | 1498 | 8 | 6% | 3% | -30% | -78% | -78% |
| GOLD | 853 | 1 | 4% | 1% | -86% | -92% | -94% |
| SILVER | 828 | 4 | 3% | 1% | -44% | -79% | -80% |
| WTI | 798 | 3 | 3% | 1% | -56% | -94% | -95% |
| COPPER | 728 | 2 | 2% | 1% | -74% | -84% | -84% |
| PLATINUM | 711 | 0 | 1% | 0% | -100% | -99% | -99% |
| NATGAS | 655 | 5 | 2% | 2% | -29% | -82% | -81% |
| PALLADIUM | 653 | 2 | 1% | 0% | -71% | -84% | -84% |
| EURUSD | 648 | 3 | 3% | 1% | -57% | -81% | -81% |
| GBPUSD | 608 | 1 | 2% | 1% | -85% | -97% | -97% |
| USDJPY | 569 | 3 | 1% | 1% | -51% | -99% | -98% |
| AUDUSD | 191 | 0 | 1% | 0% | -100% | -99% | -99% |
| USDCAD | 163 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 10604 | 40 | 4% | 2% | -57% | -89% | -89% |
| DOWN (bought NO) | 10410 | 40 | 4% | 2% | -56% | -88% | -88% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 2241 | 11 | 2% | 1% | -17% | -79% | -79% |
| 0.05–0.1% | 2338 | 7 | 3% | 1% | -56% | -92% | -92% |
| 0.1–0.2% | 3445 | 11 | 4% | 2% | -60% | -90% | -90% |
| 0.2–0.5% | 4002 | 21 | 6% | 3% | -42% | -88% | -88% |
| Over 0.5% | 1580 | 6 | 6% | 3% | -61% | -88% | -89% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 5359 | 20 | 4% | 2% | -58% | -87% | -88% |
| Morning (6am–12pm) | 5031 | 27 | 4% | 2% | -38% | -87% | -86% |
| Afternoon (12–6pm) | 4822 | 16 | 3% | 1% | -61% | -88% | -89% |
| Evening (6pm–12am) | 5802 | 17 | 3% | 2% | -67% | -92% | -91% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,422 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
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
| 10/16 10:55:53 AM | SOL | UP | 4.1 min | -0.492% | 1¢ | ❌ Lost | -$0.15 |
| 10/16 10:55:36 AM | DOGE | UP | 4.4 min | -0.531% | 1¢ | ❌ Lost | -$0.15 |
| 10/16 10:55:20 AM | WTI | DOWN | 4.7 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/16 10:54:00 AM | NEAR | UP | 6.0 min | -1.228% | 2¢ | ❌ Lost | -$0.15 |
| 10/16 10:53:44 AM | ETH | UP | 6.3 min | -0.398% | 4¢ | ❌ Lost | -$0.15 |
| 10/16 10:53:07 AM | ZEC | UP | 6.9 min | -1.762% | 2¢ | ❌ Lost | -$0.15 |
| 10/16 10:44:53 AM | SOL | DOWN | 7 sec | +0.068% | 0¢ | ❌ Lost | -$0.15 |
| 10/16 10:44:37 AM | AUDUSD | UP | 23 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/16 10:43:48 AM | NEAR | UP | 71 sec | -0.453% | 0¢ | ❌ Lost | $0.00 |
| 10/16 10:43:16 AM | GBPUSD | UP | 1.7 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/16 10:43:16 AM | USDJPY | DOWN | 1.7 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/16 10:43:00 AM | DOGE | UP | 2.0 min | -0.305% | 1¢ | ❌ Lost | -$0.15 |
| 10/16 10:42:43 AM | BNB | UP | 2.3 min | -0.134% | 1¢ | ❌ Lost | -$0.15 |
| 10/16 10:42:27 AM | ZEC | UP | 2.5 min | -0.775% | 0¢ | ❌ Lost | -$0.15 |
| 10/16 10:42:27 AM | XRP | UP | 2.5 min | -0.297% | 0¢ | ❌ Lost | -$0.15 |
| 10/16 10:42:11 AM | EURUSD | UP | 2.8 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/16 10:41:55 AM | HYPE | UP | 3.1 min | -0.338% | 0¢ | ❌ Lost | $0.00 |
| 10/16 10:41:39 AM | BTC | UP | 3.4 min | -0.188% | 1¢ | ❌ Lost | -$0.15 |
| 10/16 10:41:23 AM | WTI | DOWN | 3.6 min | — | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
