# 15-Minute 1¢ Study

*Updated Sun Oct 18, 2:18 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 1935 finished bets | 1% | $77.55 | +36% | +4.01¢ | $34.40 / $43.15 |

*Expect about **94 buys a day** (~$14.11/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 1785 | $56.10 | +29% |
| Momentum model ≥ 2%, hold to the close | 2974 | -$11.70 | -3% |
| Volatility model ≥ 2%, hold to the close | 3496 | -$32.95 | -8% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 22874 | 22867 | 87 (0%) | 1.07% | -$1,557.60 (-56%) | Hold to the close: -$1,557.60 (-56%) |

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
| Volatility model | 15143 | 4.6% | 0.4% (61) | -671% | ❌ Worse |
| Momentum model | 15143 | 4.6% | 0.4% (61) | -694% | ❌ Worse |
| Mean-reversion model | 15143 | 7.7% | 0.4% (61) | -803% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 15143 | 61 | -50% | -88% | -88% | -86% |
| Volatility model ≥ 2% | 3496 | 28 | -8% | -79% | -79% | -75% |
| Volatility model ≥ 5% | 1935 | 21 | +36% | -76% | -75% | -72% |
| Volatility model ≥ 10% | 1141 | 13 | +60% | -69% | -68% | -65% |
| Momentum model ≥ 2% | 2974 | 24 | -3% | -81% | -82% | -78% |
| Momentum model ≥ 5% | 1785 | 18 | +29% | -79% | -79% | -75% |
| Momentum model ≥ 10% | 1188 | 12 | +40% | -75% | -75% | -69% |
| Mean-reversion model ≥ 2% | 5851 | 39 | -27% | -84% | -84% | -81% |
| Mean-reversion model ≥ 5% | 4063 | 31 | -16% | -82% | -82% | -79% |
| Mean-reversion model ≥ 10% | 2694 | 20 | -15% | -80% | -81% | -78% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 15341 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 5309 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 2217 | 1% | 1% | 1% | 1% | 0% | 0% |
| **All** | 22867 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 87 | 0% | -$1,557.60 | -56% | — |
| Sell at 2¢ | 835 | 4% | -$2,460.50 | -89% | 44 sec |
| Sell at 3¢ | 565 | 2% | -$2,457.25 | -89% | 47 sec |
| Sell at 5¢ | 407 | 2% | -$2,413.05 | -87% | 50 sec |
| Sell at 10¢ | 246 | 1% | -$2,327.34 | -84% | 63 sec |
| Sell at 25¢ | 137 | 1% | -$2,154.13 | -78% | 77 sec |
| Sell at 50¢ | 91 | 0% | -$1,923.35 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 830 | 5 | 10% | 3% | -43% | -81% | -84% |
| 2–5 min | 7458 | 39 | 7% | 3% | -49% | -87% | -87% |
| 1–2 min | 5878 | 23 | 3% | 2% | -57% | -92% | -92% |
| Under 1 min | 8697 | 20 | 1% | 0% | -67% | -88% | -88% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 1723 | 11 | 4% | 2% | -21% | -90% | -90% |
| HYPE | 1714 | 6 | 5% | 2% | -57% | -90% | -88% |
| BNB | 1712 | 7 | 5% | 2% | -50% | -89% | -88% |
| DOGE | 1708 | 3 | 4% | 2% | -78% | -90% | -90% |
| ETH | 1704 | 9 | 6% | 3% | -37% | -87% | -86% |
| SOL | 1701 | 2 | 3% | 2% | -86% | -92% | -92% |
| XRP | 1695 | 7 | 3% | 1% | -49% | -87% | -87% |
| NEAR | 1692 | 9 | 6% | 3% | -31% | -78% | -79% |
| BTC | 1692 | 9 | 5% | 2% | -28% | -88% | -90% |
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
| UP (bought YES) | 11528 | 42 | 4% | 2% | -58% | -89% | -88% |
| DOWN (bought NO) | 11339 | 45 | 4% | 2% | -54% | -88% | -89% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 2633 | 14 | 2% | 1% | -12% | -82% | -81% |
| 0.05–0.1% | 2673 | 9 | 3% | 2% | -51% | -91% | -91% |
| 0.1–0.2% | 3848 | 13 | 5% | 2% | -58% | -90% | -89% |
| 0.2–0.5% | 4444 | 21 | 6% | 3% | -48% | -88% | -88% |
| Over 0.5% | 1740 | 6 | 7% | 3% | -64% | -87% | -88% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 5767 | 23 | 4% | 2% | -55% | -87% | -88% |
| Morning (6am–12pm) | 5489 | 28 | 4% | 2% | -41% | -87% | -86% |
| Afternoon (12–6pm) | 5380 | 19 | 3% | 1% | -58% | -88% | -89% |
| Evening (6pm–12am) | 6231 | 17 | 3% | 2% | -69% | -92% | -91% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,820 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/18 2:14:56 PM | DOGE | DOWN | 4 sec | +0.012% | 0¢ | ❌ Lost | $0.00 |
| 10/18 2:14:56 PM | NEAR | DOWN | 4 sec | -0.058% | 0¢ | ❌ Lost | $0.00 |
| 10/18 2:14:24 PM | BNB | UP | 36 sec | -0.072% | 0¢ | ❌ Lost | -$0.15 |
| 10/18 2:14:24 PM | BTC | UP | 36 sec | -0.043% | 0¢ | ❌ Lost | $0.00 |
| 10/18 2:13:52 PM | SOL | UP | 68 sec | -0.277% | 1¢ | ❌ Lost | -$0.15 |
| 10/18 2:13:36 PM | ZEC | DOWN | 84 sec | +0.366% | 0¢ | ❌ Lost | $0.00 |
| 10/18 2:12:48 PM | HYPE | UP | 2.2 min | -0.355% | 1¢ | ❌ Lost | -$0.15 |
| 10/18 1:59:38 PM | XRP | DOWN | 22 sec | +0.167% | 0¢ | ❌ Lost | $0.00 |
| 10/18 1:59:38 PM | BNB | DOWN | 22 sec | +0.055% | 0¢ | ❌ Lost | $0.00 |
| 10/18 1:59:38 PM | DOGE | DOWN | 22 sec | +0.121% | 0¢ | ❌ Lost | $0.00 |
| 10/18 1:59:38 PM | SOL | DOWN | 22 sec | +0.060% | 0¢ | ❌ Lost | $0.00 |
| 10/18 1:59:22 PM | NEAR | UP | 38 sec | -0.330% | 0¢ | ❌ Lost | $0.00 |
| 10/18 1:59:22 PM | ZEC | DOWN | 38 sec | +0.266% | 0¢ | ❌ Lost | $0.00 |
| 10/18 1:59:06 PM | ETH | DOWN | 54 sec | +0.155% | 0¢ | ❌ Lost | -$0.15 |
| 10/18 1:59:06 PM | BTC | DOWN | 54 sec | +0.051% | 1¢ | ❌ Lost | -$0.15 |
| 10/18 1:58:50 PM | HYPE | DOWN | 70 sec | +0.191% | 0¢ | ❌ Lost | $0.00 |
| 10/18 1:42:10 PM | NEAR | UP | 2.8 min | -0.727% | 1¢ | ❌ Lost | -$0.15 |
| 10/18 1:41:22 PM | HYPE | UP | 3.6 min | -0.526% | 1¢ | ❌ Lost | -$0.15 |
| 10/18 1:41:06 PM | BTC | UP | 3.9 min | -0.206% | 1¢ | ❌ Lost | -$0.15 |
| 10/18 1:40:50 PM | ZEC | UP | 4.2 min | -1.131% | 1¢ | ❌ Lost | -$0.15 |
| 10/18 1:40:17 PM | DOGE | UP | 4.7 min | -1.159% | 1¢ | ❌ Lost | -$0.15 |
| 10/18 1:39:45 PM | XRP | UP | 5.2 min | -0.780% | 1¢ | ❌ Lost | -$0.15 |
| 10/18 1:39:45 PM | SOL | UP | 5.2 min | -0.620% | 1¢ | ❌ Lost | -$0.15 |
| 10/18 1:39:27 PM | ETH | UP | 5.5 min | -0.849% | 1¢ | ❌ Lost | -$0.15 |
| 10/18 1:39:27 PM | BNB | UP | 5.5 min | -0.505% | 0¢ | ❌ Lost | $0.00 |
| 10/18 1:27:01 PM | BTC | UP | 3.0 min | -0.144% | 1¢ | ❌ Lost | -$0.15 |
| 10/18 1:26:29 PM | XRP | UP | 3.5 min | -0.298% | 1¢ | ❌ Lost | -$0.15 |
| 10/18 1:26:29 PM | NEAR | UP | 3.5 min | -0.743% | 0¢ | ❌ Lost | -$0.15 |
| 10/18 1:25:40 PM | DOGE | UP | 4.3 min | -0.356% | 1¢ | ❌ Lost | -$0.15 |
| 10/18 1:25:24 PM | ETH | UP | 4.6 min | -0.268% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
