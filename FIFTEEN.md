# 15-Minute 1¢ Study

*Updated Fri Oct 16, 12:24 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 1643 finished bets | 1% | $83.45 | +46% | +5.08¢ | $37.05 / $46.40 |

*Expect about **89 buys a day** (~$13.33/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 1515 | $46.05 | +28% |
| Momentum model ≥ 2%, hold to the close | 2569 | -$3.45 | -1% |
| Volatility model ≥ 5%, sell at 50¢ | 1643 | -$19.05 | -10% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 21109 | 21102 | 80 (0%) | 1.07% | -$1,452.65 (-56%) | Hold to the close: -$1,452.65 (-56%) |

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
| Volatility model | 13456 | 4.4% | 0.4% (54) | -638% | ❌ Worse |
| Momentum model | 13456 | 4.4% | 0.4% (54) | -661% | ❌ Worse |
| Mean-reversion model | 13456 | 7.4% | 0.4% (54) | -769% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 13456 | 54 | -50% | -88% | -88% | -85% |
| Volatility model ≥ 2% | 3002 | 24 | -8% | -78% | -78% | -74% |
| Volatility model ≥ 5% | 1643 | 19 | +46% | -74% | -72% | -68% |
| Volatility model ≥ 10% | 953 | 11 | +65% | -65% | -64% | -61% |
| Momentum model ≥ 2% | 2569 | 21 | -1% | -80% | -80% | -77% |
| Momentum model ≥ 5% | 1515 | 15 | +28% | -77% | -77% | -73% |
| Momentum model ≥ 10% | 1009 | 10 | +40% | -72% | -71% | -66% |
| Mean-reversion model ≥ 2% | 5088 | 34 | -27% | -84% | -84% | -81% |
| Mean-reversion model ≥ 5% | 3506 | 27 | -15% | -82% | -82% | -78% |
| Mean-reversion model ≥ 10% | 2303 | 16 | -21% | -80% | -80% | -77% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 13654 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 5253 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 2195 | 2% | 1% | 1% | 1% | 0% | 0% |
| **All** | 21102 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 80 | 0% | -$1,452.65 | -56% | — |
| Sell at 2¢ | 751 | 4% | -$2,279.39 | -89% | 42 sec |
| Sell at 3¢ | 506 | 2% | -$2,277.31 | -89% | 47 sec |
| Sell at 5¢ | 366 | 2% | -$2,236.75 | -87% | 50 sec |
| Sell at 10¢ | 220 | 1% | -$2,158.45 | -84% | 63 sec |
| Sell at 25¢ | 126 | 1% | -$1,987.59 | -77% | 80 sec |
| Sell at 50¢ | 83 | 0% | -$1,774.40 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 718 | 5 | 10% | 3% | -34% | -82% | -85% |
| 2–5 min | 6850 | 37 | 7% | 3% | -47% | -88% | -88% |
| 1–2 min | 5485 | 20 | 3% | 2% | -60% | -92% | -92% |
| Under 1 min | 8045 | 18 | 1% | 0% | -68% | -87% | -87% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 1533 | 11 | 5% | 3% | -11% | -89% | -89% |
| HYPE | 1528 | 5 | 4% | 2% | -60% | -90% | -89% |
| ETH | 1523 | 8 | 5% | 3% | -36% | -88% | -87% |
| DOGE | 1519 | 2 | 4% | 2% | -83% | -90% | -90% |
| BNB | 1519 | 6 | 5% | 2% | -51% | -89% | -89% |
| SOL | 1516 | 2 | 3% | 2% | -84% | -92% | -91% |
| XRP | 1507 | 7 | 2% | 1% | -43% | -86% | -87% |
| BTC | 1506 | 7 | 5% | 2% | -38% | -88% | -91% |
| NEAR | 1503 | 8 | 6% | 3% | -30% | -78% | -78% |
| GOLD | 857 | 1 | 4% | 1% | -86% | -92% | -94% |
| SILVER | 833 | 4 | 3% | 1% | -45% | -80% | -80% |
| WTI | 802 | 3 | 3% | 1% | -57% | -94% | -95% |
| COPPER | 732 | 2 | 2% | 1% | -74% | -84% | -84% |
| PLATINUM | 715 | 0 | 1% | 0% | -100% | -99% | -99% |
| NATGAS | 658 | 5 | 2% | 2% | -29% | -82% | -81% |
| PALLADIUM | 656 | 2 | 1% | 0% | -72% | -84% | -84% |
| EURUSD | 651 | 3 | 3% | 1% | -57% | -81% | -81% |
| GBPUSD | 611 | 1 | 2% | 1% | -85% | -97% | -97% |
| USDJPY | 572 | 3 | 1% | 1% | -51% | -99% | -98% |
| AUDUSD | 195 | 0 | 1% | 0% | -100% | -99% | -99% |
| USDCAD | 166 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 10655 | 40 | 4% | 2% | -57% | -89% | -89% |
| DOWN (bought NO) | 10447 | 40 | 4% | 2% | -56% | -88% | -89% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 2241 | 11 | 2% | 1% | -17% | -79% | -79% |
| 0.05–0.1% | 2339 | 7 | 3% | 1% | -56% | -92% | -92% |
| 0.1–0.2% | 3447 | 11 | 4% | 2% | -60% | -90% | -90% |
| 0.2–0.5% | 4024 | 21 | 6% | 3% | -42% | -88% | -88% |
| Over 0.5% | 1600 | 6 | 6% | 3% | -61% | -88% | -89% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 5359 | 20 | 4% | 2% | -58% | -87% | -88% |
| Morning (6am–12pm) | 5104 | 27 | 4% | 2% | -39% | -87% | -86% |
| Afternoon (12–6pm) | 4837 | 16 | 3% | 1% | -61% | -88% | -89% |
| Evening (6pm–12am) | 5802 | 17 | 3% | 2% | -67% | -92% | -91% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,426 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/16 12:14:30 PM | NEAR | DOWN | 29 sec | +0.243% | 0¢ | ❌ Lost | $0.00 |
| 10/16 12:14:14 PM | USDJPY | UP | 46 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/16 12:14:14 PM | SILVER | UP | 46 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/16 12:14:14 PM | USDCAD | UP | 46 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/16 12:13:56 PM | BNB | DOWN | 64 sec | +0.094% | 0¢ | ❌ Lost | $0.00 |
| 10/16 12:13:56 PM | DOGE | DOWN | 64 sec | +0.197% | 1¢ | ❌ Lost | -$0.15 |
| 10/16 12:13:56 PM | SOL | DOWN | 64 sec | +0.240% | 1¢ | ❌ Lost | -$0.15 |
| 10/16 12:13:56 PM | ETH | DOWN | 64 sec | +0.221% | 0¢ | ❌ Lost | $0.00 |
| 10/16 12:13:56 PM | WTI | DOWN | 64 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/16 12:13:56 PM | EURUSD | DOWN | 64 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/16 12:13:40 PM | XRP | DOWN | 80 sec | +0.223% | 0¢ | ❌ Lost | $0.00 |
| 10/16 12:13:40 PM | BTC | DOWN | 80 sec | +0.154% | 1¢ | ❌ Lost | -$0.15 |
| 10/16 12:13:24 PM | ZEC | UP | 1.6 min | -0.445% | 3¢ | ❌ Lost | -$0.15 |
| 10/16 12:13:24 PM | NATGAS | UP | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/16 12:09:56 PM | HYPE | DOWN | 5.1 min | +0.472% | 1¢ | ❌ Lost | -$0.15 |
| 10/16 11:59:55 AM | GOLD | UP | 5 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/16 11:59:55 AM | WTI | DOWN | 5 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/16 11:59:39 AM | USDJPY | UP | 21 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/16 11:59:23 AM | COPPER | UP | 37 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/16 11:59:23 AM | PLATINUM | UP | 37 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/16 11:58:51 AM | GBPUSD | UP | 69 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/16 11:58:51 AM | PALLADIUM | UP | 69 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/16 11:58:04 AM | AUDUSD | UP | 1.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/16 11:57:48 AM | SILVER | UP | 2.2 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/16 11:57:00 AM | HYPE | UP | 3.0 min | -0.358% | 1¢ | ❌ Lost | -$0.15 |
| 10/16 11:55:55 AM | DOGE | UP | 4.1 min | -0.508% | 1¢ | ❌ Lost | -$0.15 |
| 10/16 11:55:21 AM | BTC | UP | 4.7 min | -0.304% | 1¢ | ❌ Lost | -$0.15 |
| 10/16 11:54:50 AM | NEAR | UP | 5.2 min | -1.366% | 10¢ | ❌ Lost | -$0.15 |
| 10/16 11:54:50 AM | ZEC | UP | 5.2 min | -1.117% | 1¢ | ❌ Lost | -$0.15 |
| 10/16 11:54:50 AM | SOL | UP | 5.2 min | -0.463% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
