# 15-Minute 1¢ Study

*Updated Fri Oct 16, 10:42 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 1633 finished bets | 1% | $84.95 | +47% | +5.20¢ | $37.65 / $47.30 |

*Expect about **89 buys a day** (~$13.30/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 1511 | $46.65 | +29% |
| Momentum model ≥ 2%, hold to the close | 2556 | -$1.80 | -1% |
| Volatility model ≥ 5%, sell at 50¢ | 1633 | -$17.55 | -10% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 20998 | 20982 | 80 (0%) | 1.07% | -$1,436.00 (-56%) | Hold to the close: -$1,436.00 (-56%) |

*In play or awaiting result: 15. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 13393 | 4.4% | 0.4% (54) | -639% | ❌ Worse |
| Momentum model | 13393 | 4.4% | 0.4% (54) | -662% | ❌ Worse |
| Mean-reversion model | 13393 | 7.4% | 0.4% (54) | -769% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 13393 | 54 | -50% | -88% | -88% | -85% |
| Volatility model ≥ 2% | 2982 | 24 | -7% | -78% | -78% | -74% |
| Volatility model ≥ 5% | 1633 | 19 | +47% | -74% | -72% | -68% |
| Volatility model ≥ 10% | 953 | 11 | +65% | -65% | -64% | -61% |
| Momentum model ≥ 2% | 2556 | 21 | -1% | -80% | -80% | -77% |
| Momentum model ≥ 5% | 1511 | 15 | +29% | -77% | -77% | -73% |
| Momentum model ≥ 10% | 1007 | 10 | +40% | -71% | -71% | -66% |
| Mean-reversion model ≥ 2% | 5052 | 34 | -27% | -84% | -84% | -81% |
| Mean-reversion model ≥ 5% | 3475 | 27 | -14% | -82% | -82% | -78% |
| Mean-reversion model ≥ 10% | 2280 | 16 | -20% | -80% | -80% | -77% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 13591 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 5218 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 2173 | 2% | 1% | 1% | 1% | 0% | 0% |
| **All** | 20982 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 80 | 0% | -$1,436.00 | -56% | — |
| Sell at 2¢ | 747 | 4% | -$2,263.78 | -89% | 42 sec |
| Sell at 3¢ | 503 | 2% | -$2,261.83 | -88% | 47 sec |
| Sell at 5¢ | 364 | 2% | -$2,221.40 | -87% | 50 sec |
| Sell at 10¢ | 219 | 1% | -$2,143.11 | -84% | 63 sec |
| Sell at 25¢ | 126 | 1% | -$1,970.94 | -77% | 80 sec |
| Sell at 50¢ | 83 | 0% | -$1,757.75 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 697 | 5 | 10% | 3% | -32% | -82% | -86% |
| 2–5 min | 6806 | 37 | 7% | 3% | -46% | -88% | -88% |
| 1–2 min | 5459 | 20 | 3% | 2% | -60% | -92% | -92% |
| Under 1 min | 8016 | 18 | 1% | 0% | -68% | -87% | -87% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 1526 | 11 | 5% | 3% | -10% | -89% | -89% |
| HYPE | 1521 | 5 | 4% | 2% | -60% | -90% | -89% |
| ETH | 1516 | 8 | 5% | 3% | -36% | -88% | -87% |
| DOGE | 1512 | 2 | 4% | 2% | -83% | -90% | -90% |
| BNB | 1512 | 6 | 5% | 2% | -51% | -89% | -89% |
| SOL | 1509 | 2 | 3% | 2% | -84% | -92% | -91% |
| XRP | 1500 | 7 | 2% | 1% | -42% | -86% | -87% |
| BTC | 1499 | 7 | 5% | 2% | -38% | -88% | -91% |
| NEAR | 1496 | 8 | 6% | 3% | -30% | -78% | -78% |
| GOLD | 852 | 1 | 4% | 1% | -86% | -92% | -94% |
| SILVER | 827 | 4 | 3% | 1% | -44% | -79% | -80% |
| WTI | 796 | 3 | 3% | 1% | -56% | -94% | -95% |
| COPPER | 727 | 2 | 2% | 1% | -74% | -84% | -84% |
| PLATINUM | 710 | 0 | 1% | 0% | -100% | -99% | -99% |
| NATGAS | 654 | 5 | 2% | 2% | -29% | -82% | -81% |
| PALLADIUM | 652 | 2 | 1% | 0% | -71% | -84% | -84% |
| EURUSD | 646 | 3 | 3% | 1% | -57% | -81% | -81% |
| GBPUSD | 607 | 1 | 2% | 1% | -85% | -97% | -97% |
| USDJPY | 568 | 3 | 1% | 1% | -51% | -99% | -98% |
| AUDUSD | 190 | 0 | 1% | 0% | -100% | -99% | -99% |
| USDCAD | 162 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 10579 | 40 | 4% | 2% | -57% | -89% | -89% |
| DOWN (bought NO) | 10403 | 40 | 4% | 2% | -56% | -88% | -88% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 2241 | 11 | 2% | 1% | -17% | -79% | -79% |
| 0.05–0.1% | 2337 | 7 | 3% | 1% | -56% | -92% | -91% |
| 0.1–0.2% | 3442 | 11 | 4% | 2% | -60% | -90% | -90% |
| 0.2–0.5% | 3992 | 21 | 6% | 3% | -42% | -88% | -88% |
| Over 0.5% | 1576 | 6 | 6% | 3% | -61% | -88% | -89% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 5359 | 20 | 4% | 2% | -58% | -87% | -88% |
| Morning (6am–12pm) | 4999 | 27 | 4% | 2% | -38% | -87% | -86% |
| Afternoon (12–6pm) | 4822 | 16 | 3% | 1% | -61% | -88% | -89% |
| Evening (6pm–12am) | 5802 | 17 | 3% | 2% | -67% | -92% | -91% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,419 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/16 10:42:43 AM | BNB | UP | 2.3 min | -0.134% | — | In play | — |
| 10/16 10:42:27 AM | ZEC | UP | 2.5 min | -0.775% | — | In play | — |
| 10/16 10:42:27 AM | XRP | UP | 2.5 min | -0.297% | — | In play | — |
| 10/16 10:42:11 AM | EURUSD | UP | 2.8 min | — | — | In play | — |
| 10/16 10:41:55 AM | HYPE | UP | 3.1 min | -0.338% | — | In play | — |
| 10/16 10:41:39 AM | BTC | UP | 3.4 min | -0.188% | — | In play | — |
| 10/16 10:41:23 AM | WTI | DOWN | 3.6 min | — | — | In play | — |
| 10/16 10:41:23 AM | COPPER | UP | 3.6 min | — | — | In play | — |
| 10/16 10:41:23 AM | ETH | UP | 3.6 min | -0.247% | — | In play | — |
| 10/16 10:29:51 AM | AUDUSD | DOWN | 8 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/16 10:29:35 AM | HYPE | DOWN | 24 sec | +0.037% | 0¢ | ❌ Lost | $0.00 |
| 10/16 10:29:19 AM | SILVER | UP | 40 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/16 10:29:03 AM | ZEC | UP | 57 sec | -0.328% | 0¢ | ❌ Lost | -$0.15 |
| 10/16 10:28:47 AM | NATGAS | DOWN | 73 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/16 10:28:47 AM | GOLD | UP | 73 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/16 10:28:31 AM | BTC | DOWN | 89 sec | +0.088% | 1¢ | ❌ Lost | -$0.15 |
| 10/16 10:27:26 AM | SOL | DOWN | 2.5 min | +0.205% | 1¢ | ❌ Lost | -$0.15 |
| 10/16 10:27:26 AM | BNB | DOWN | 2.5 min | +0.124% | 1¢ | ❌ Lost | -$0.15 |
| 10/16 10:27:26 AM | XRP | DOWN | 2.5 min | +0.198% | 1¢ | ❌ Lost | -$0.15 |
| 10/16 10:27:10 AM | DOGE | DOWN | 2.8 min | +0.304% | 1¢ | ❌ Lost | -$0.15 |
| 10/16 10:26:54 AM | USDJPY | DOWN | 3.1 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/16 10:26:38 AM | ETH | DOWN | 3.4 min | +0.244% | 1¢ | ❌ Lost | -$0.15 |
| 10/16 10:26:06 AM | WTI | DOWN | 3.9 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/16 10:26:06 AM | NEAR | DOWN | 3.9 min | +0.724% | 1¢ | ❌ Lost | -$0.15 |
| 10/16 10:14:36 AM | AUDUSD | UP | 23 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/16 10:14:20 AM | GBPUSD | UP | 39 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/16 10:14:20 AM | USDJPY | DOWN | 39 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/16 10:14:20 AM | XRP | DOWN | 39 sec | +0.145% | 0¢ | ❌ Lost | -$0.15 |
| 10/16 10:14:20 AM | NEAR | DOWN | 39 sec | +0.257% | 1¢ | ❌ Lost | -$0.15 |
| 10/16 10:14:04 AM | SILVER | DOWN | 56 sec | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
