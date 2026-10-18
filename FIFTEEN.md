# 15-Minute 1¢ Study

*Updated Sat Oct 17, 9:20 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 1855 finished bets | 1% | $87.90 | +43% | +4.74¢ | $39.20 / $48.70 |

*Expect about **93 buys a day** (~$14.01/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 1698 | $53.05 | +29% |
| Momentum model ≥ 2%, hold to the close | 2846 | -$8.75 | -3% |
| Volatility model ≥ 2%, hold to the close | 3347 | -$27.45 | -7% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 22334 | 22327 | 85 (0%) | 1.07% | -$1,520.65 (-56%) | Hold to the close: -$1,520.65 (-56%) |

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
| Volatility model | 14603 | 4.6% | 0.4% (59) | -658% | ❌ Worse |
| Momentum model | 14603 | 4.5% | 0.4% (59) | -681% | ❌ Worse |
| Mean-reversion model | 14603 | 7.6% | 0.4% (59) | -790% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 14603 | 59 | -49% | -88% | -88% | -85% |
| Volatility model ≥ 2% | 3347 | 27 | -7% | -79% | -79% | -75% |
| Volatility model ≥ 5% | 1855 | 21 | +43% | -75% | -74% | -71% |
| Volatility model ≥ 10% | 1088 | 13 | +69% | -68% | -67% | -65% |
| Momentum model ≥ 2% | 2846 | 23 | -3% | -81% | -81% | -78% |
| Momentum model ≥ 5% | 1698 | 17 | +29% | -79% | -79% | -75% |
| Momentum model ≥ 10% | 1131 | 12 | +48% | -74% | -74% | -69% |
| Mean-reversion model ≥ 2% | 5614 | 38 | -26% | -84% | -84% | -81% |
| Mean-reversion model ≥ 5% | 3888 | 30 | -15% | -82% | -82% | -79% |
| Mean-reversion model ≥ 10% | 2574 | 19 | -15% | -80% | -81% | -78% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 14801 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 5309 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 2217 | 1% | 1% | 1% | 1% | 0% | 0% |
| **All** | 22327 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 85 | 0% | -$1,520.65 | -56% | — |
| Sell at 2¢ | 809 | 4% | -$2,402.31 | -89% | 42 sec |
| Sell at 3¢ | 547 | 2% | -$2,399.32 | -89% | 47 sec |
| Sell at 5¢ | 395 | 2% | -$2,355.90 | -87% | 50 sec |
| Sell at 10¢ | 241 | 1% | -$2,268.94 | -84% | 64 sec |
| Sell at 25¢ | 134 | 1% | -$2,099.11 | -77% | 79 sec |
| Sell at 50¢ | 88 | 0% | -$1,878.65 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 789 | 5 | 10% | 3% | -40% | -82% | -84% |
| 2–5 min | 7242 | 38 | 7% | 3% | -48% | -88% | -87% |
| 1–2 min | 5769 | 23 | 3% | 2% | -56% | -92% | -92% |
| Under 1 min | 8523 | 19 | 1% | 0% | -68% | -88% | -88% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 1663 | 11 | 4% | 2% | -17% | -90% | -90% |
| HYPE | 1655 | 6 | 5% | 3% | -55% | -90% | -88% |
| BNB | 1650 | 7 | 5% | 2% | -48% | -89% | -88% |
| ETH | 1648 | 9 | 6% | 3% | -34% | -87% | -86% |
| DOGE | 1646 | 2 | 4% | 2% | -85% | -91% | -90% |
| SOL | 1640 | 2 | 4% | 2% | -85% | -92% | -91% |
| XRP | 1635 | 7 | 3% | 1% | -47% | -87% | -87% |
| NEAR | 1633 | 9 | 6% | 3% | -28% | -78% | -79% |
| BTC | 1631 | 8 | 5% | 2% | -34% | -88% | -90% |
| GOLD | 864 | 1 | 3% | 1% | -86% | -92% | -94% |
| SILVER | 841 | 4 | 3% | 1% | -45% | -80% | -80% |
| WTI | 821 | 3 | 3% | 1% | -57% | -94% | -95% |
| COPPER | 735 | 2 | 2% | 1% | -75% | -84% | -84% |
| PLATINUM | 722 | 0 | 1% | 0% | -100% | -99% | -99% |
| NATGAS | 667 | 5 | 2% | 2% | -30% | -82% | -81% |
| PALLADIUM | 659 | 2 | 1% | 0% | -72% | -84% | -84% |
| EURUSD | 659 | 3 | 3% | 1% | -58% | -81% | -81% |
| GBPUSD | 615 | 1 | 2% | 1% | -85% | -97% | -97% |
| USDJPY | 574 | 3 | 1% | 1% | -51% | -99% | -98% |
| AUDUSD | 200 | 0 | 0% | 0% | -100% | -99% | -99% |
| USDCAD | 169 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 11225 | 41 | 4% | 2% | -58% | -89% | -88% |
| DOWN (bought NO) | 11102 | 44 | 4% | 2% | -54% | -88% | -89% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 2543 | 13 | 2% | 1% | -15% | -81% | -81% |
| 0.05–0.1% | 2566 | 8 | 3% | 2% | -55% | -91% | -91% |
| 0.1–0.2% | 3710 | 13 | 5% | 2% | -57% | -90% | -89% |
| 0.2–0.5% | 4292 | 21 | 6% | 3% | -46% | -88% | -88% |
| Over 0.5% | 1687 | 6 | 6% | 3% | -63% | -88% | -88% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 5566 | 22 | 4% | 2% | -55% | -87% | -88% |
| Morning (6am–12pm) | 5315 | 27 | 4% | 2% | -42% | -87% | -86% |
| Afternoon (12–6pm) | 5311 | 19 | 3% | 1% | -57% | -88% | -89% |
| Evening (6pm–12am) | 6135 | 17 | 3% | 2% | -68% | -92% | -91% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,685 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/17 9:12:38 PM | ZEC | DOWN | 2.4 min | +0.470% | 1¢ | ❌ Lost | -$0.15 |
| 10/17 9:12:06 PM | BNB | DOWN | 2.9 min | +0.118% | 0¢ | ❌ Lost | $0.00 |
| 10/17 9:12:06 PM | SOL | DOWN | 2.9 min | +0.223% | 1¢ | ❌ Lost | -$0.15 |
| 10/17 9:11:51 PM | BTC | DOWN | 3.1 min | +0.169% | 1¢ | ❌ Lost | -$0.15 |
| 10/17 9:11:51 PM | DOGE | DOWN | 3.1 min | +0.269% | 1¢ | ❌ Lost | -$0.15 |
| 10/17 9:11:51 PM | HYPE | DOWN | 3.1 min | +0.321% | 1¢ | ❌ Lost | -$0.15 |
| 10/17 9:11:04 PM | NEAR | DOWN | 3.9 min | +0.906% | 1¢ | ❌ Lost | -$0.15 |
| 10/17 9:11:04 PM | XRP | DOWN | 3.9 min | +0.255% | 1¢ | ❌ Lost | -$0.15 |
| 10/17 9:11:04 PM | ETH | DOWN | 3.9 min | +0.181% | 2¢ | ❌ Lost | -$0.15 |
| 10/17 8:57:42 PM | BTC | DOWN | 2.3 min | +0.122% | 1¢ | ❌ Lost | -$0.15 |
| 10/17 8:57:42 PM | HYPE | DOWN | 2.3 min | +0.166% | 0¢ | ❌ Lost | -$0.15 |
| 10/17 8:57:26 PM | DOGE | DOWN | 2.6 min | +0.180% | 1¢ | ❌ Lost | -$0.15 |
| 10/17 8:57:26 PM | XRP | DOWN | 2.6 min | +0.185% | 1¢ | ❌ Lost | -$0.15 |
| 10/17 8:57:26 PM | SOL | DOWN | 2.6 min | +0.231% | 1¢ | ❌ Lost | -$0.15 |
| 10/17 8:57:10 PM | NEAR | DOWN | 2.8 min | +0.848% | 1¢ | ❌ Lost | -$0.15 |
| 10/17 8:56:38 PM | ZEC | DOWN | 3.4 min | +0.416% | 1¢ | ❌ Lost | -$0.15 |
| 10/17 8:56:22 PM | ETH | DOWN | 3.6 min | +0.149% | 0¢ | ❌ Lost | -$0.15 |
| 10/17 8:55:49 PM | BNB | DOWN | 4.2 min | +0.061% | 1¢ | ❌ Lost | -$0.15 |
| 10/17 8:44:40 PM | BTC | UP | 20 sec | -0.040% | 0¢ | ❌ Lost | -$0.15 |
| 10/17 8:44:40 PM | DOGE | UP | 20 sec | -0.038% | 0¢ | ❌ Lost | $0.00 |
| 10/17 8:44:40 PM | BNB | UP | 20 sec | -0.033% | 0¢ | ❌ Lost | -$0.15 |
| 10/17 8:44:40 PM | HYPE | UP | 20 sec | -0.076% | 0¢ | ❌ Lost | $0.00 |
| 10/17 8:44:40 PM | ETH | UP | 20 sec | -0.040% | 0¢ | ❌ Lost | $0.00 |
| 10/17 8:44:40 PM | ZEC | UP | 20 sec | -0.227% | 0¢ | ❌ Lost | $0.00 |
| 10/17 8:44:24 PM | SOL | UP | 36 sec | -0.083% | 0¢ | ❌ Lost | $0.00 |
| 10/17 8:43:03 PM | XRP | UP | 1.9 min | -0.170% | 1¢ | ❌ Lost | -$0.15 |
| 10/17 8:42:48 PM | NEAR | DOWN | 2.2 min | +0.279% | 1¢ | ❌ Lost | -$0.15 |
| 10/17 8:28:40 PM | BTC | DOWN | 79 sec | +0.090% | 0¢ | ❌ Lost | $0.00 |
| 10/17 8:28:40 PM | NEAR | DOWN | 79 sec | +0.266% | 1¢ | ❌ Lost | -$0.15 |
| 10/17 8:28:40 PM | BNB | DOWN | 79 sec | +0.025% | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
