# 15-Minute 1¢ Study

*Updated Sun Oct 18, 4:21 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 1950 finished bets | 1% | $75.75 | +35% | +3.88¢ | $33.35 / $42.40 |

*Expect about **94 buys a day** (~$14.16/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 1792 | $55.50 | +28% |
| Momentum model ≥ 2%, hold to the close | 2991 | -$13.80 | -4% |
| Volatility model ≥ 2%, hold to the close | 3519 | -$35.95 | -8% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 22953 | 22946 | 87 (0%) | 1.07% | -$1,568.25 (-56%) | Hold to the close: -$1,568.25 (-56%) |

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
| Volatility model | 15214 | 4.6% | 0.4% (61) | -674% | ❌ Worse |
| Momentum model | 15214 | 4.6% | 0.4% (61) | -697% | ❌ Worse |
| Mean-reversion model | 15214 | 7.7% | 0.4% (61) | -808% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 15214 | 61 | -50% | -88% | -88% | -86% |
| Volatility model ≥ 2% | 3519 | 28 | -8% | -80% | -79% | -75% |
| Volatility model ≥ 5% | 1950 | 21 | +35% | -76% | -75% | -72% |
| Volatility model ≥ 10% | 1146 | 13 | +59% | -70% | -68% | -66% |
| Momentum model ≥ 2% | 2991 | 24 | -4% | -82% | -82% | -78% |
| Momentum model ≥ 5% | 1792 | 18 | +28% | -79% | -79% | -75% |
| Momentum model ≥ 10% | 1191 | 12 | +39% | -75% | -75% | -70% |
| Mean-reversion model ≥ 2% | 5891 | 39 | -28% | -84% | -84% | -81% |
| Mean-reversion model ≥ 5% | 4092 | 31 | -16% | -83% | -82% | -79% |
| Mean-reversion model ≥ 10% | 2711 | 20 | -16% | -81% | -81% | -78% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 15412 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 5311 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 2223 | 1% | 1% | 1% | 1% | 0% | 0% |
| **All** | 22946 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 87 | 0% | -$1,568.25 | -56% | — |
| Sell at 2¢ | 835 | 4% | -$2,471.15 | -89% | 44 sec |
| Sell at 3¢ | 565 | 2% | -$2,467.90 | -89% | 47 sec |
| Sell at 5¢ | 407 | 2% | -$2,423.70 | -87% | 50 sec |
| Sell at 10¢ | 246 | 1% | -$2,337.99 | -84% | 63 sec |
| Sell at 25¢ | 137 | 1% | -$2,164.78 | -78% | 77 sec |
| Sell at 50¢ | 91 | 0% | -$1,934.00 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 840 | 5 | 10% | 3% | -43% | -82% | -85% |
| 2–5 min | 7504 | 39 | 7% | 3% | -49% | -88% | -87% |
| 1–2 min | 5890 | 23 | 3% | 2% | -57% | -92% | -92% |
| Under 1 min | 8708 | 20 | 1% | 0% | -67% | -88% | -88% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 1731 | 11 | 4% | 2% | -21% | -90% | -90% |
| HYPE | 1722 | 6 | 5% | 2% | -57% | -90% | -88% |
| BNB | 1720 | 7 | 5% | 2% | -50% | -89% | -88% |
| DOGE | 1716 | 3 | 4% | 2% | -78% | -90% | -90% |
| ETH | 1711 | 9 | 6% | 3% | -37% | -87% | -87% |
| SOL | 1709 | 2 | 3% | 2% | -86% | -92% | -92% |
| XRP | 1703 | 7 | 3% | 1% | -49% | -87% | -88% |
| NEAR | 1700 | 9 | 6% | 3% | -32% | -78% | -79% |
| BTC | 1700 | 9 | 5% | 2% | -29% | -88% | -90% |
| GOLD | 864 | 1 | 3% | 1% | -86% | -92% | -94% |
| SILVER | 841 | 4 | 3% | 1% | -45% | -80% | -80% |
| WTI | 822 | 3 | 3% | 1% | -58% | -94% | -95% |
| COPPER | 735 | 2 | 2% | 1% | -75% | -84% | -84% |
| PLATINUM | 722 | 0 | 1% | 0% | -100% | -99% | -99% |
| NATGAS | 668 | 5 | 2% | 2% | -30% | -82% | -81% |
| EURUSD | 662 | 3 | 3% | 1% | -58% | -81% | -81% |
| PALLADIUM | 659 | 2 | 1% | 0% | -72% | -84% | -84% |
| GBPUSD | 616 | 1 | 2% | 1% | -85% | -97% | -97% |
| USDJPY | 575 | 3 | 1% | 1% | -51% | -99% | -98% |
| AUDUSD | 201 | 0 | 0% | 0% | -100% | -99% | -99% |
| USDCAD | 169 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 11545 | 42 | 4% | 2% | -58% | -89% | -88% |
| DOWN (bought NO) | 11401 | 45 | 4% | 2% | -54% | -88% | -89% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 2637 | 14 | 2% | 1% | -12% | -82% | -81% |
| 0.05–0.1% | 2677 | 9 | 3% | 2% | -51% | -91% | -91% |
| 0.1–0.2% | 3864 | 13 | 5% | 2% | -59% | -90% | -89% |
| 0.2–0.5% | 4480 | 21 | 6% | 3% | -49% | -88% | -88% |
| Over 0.5% | 1751 | 6 | 7% | 3% | -65% | -88% | -89% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 5767 | 23 | 4% | 2% | -55% | -87% | -88% |
| Morning (6am–12pm) | 5489 | 28 | 4% | 2% | -41% | -87% | -86% |
| Afternoon (12–6pm) | 5459 | 19 | 3% | 1% | -59% | -88% | -89% |
| Evening (6pm–12am) | 6231 | 17 | 3% | 2% | -69% | -92% | -91% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,854 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/18 4:14:17 PM | USDJPY | UP | 42 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/18 4:13:14 PM | EURUSD | DOWN | 1.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/18 4:12:42 PM | GBPUSD | DOWN | 2.3 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/18 4:11:38 PM | NATGAS | UP | 3.4 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/18 4:08:55 PM | ETH | DOWN | 6.1 min | +0.806% | 1¢ | ❌ Lost | -$0.15 |
| 10/18 4:08:39 PM | DOGE | DOWN | 6.3 min | +1.323% | 1¢ | ❌ Lost | -$0.15 |
| 10/18 4:08:39 PM | BNB | DOWN | 6.3 min | +0.512% | 1¢ | ❌ Lost | -$0.15 |
| 10/18 4:08:23 PM | BTC | DOWN | 6.6 min | +0.452% | 1¢ | ❌ Lost | -$0.15 |
| 10/18 4:08:23 PM | WTI | UP | 6.6 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/18 4:08:23 PM | XRP | DOWN | 6.6 min | +1.090% | 1¢ | ❌ Lost | -$0.15 |
| 10/18 4:08:07 PM | HYPE | DOWN | 6.9 min | +0.772% | 1¢ | ❌ Lost | -$0.15 |
| 10/18 4:08:07 PM | SOL | DOWN | 6.9 min | +1.137% | 2¢ | ❌ Lost | -$0.15 |
| 10/18 4:07:02 PM | ZEC | DOWN | 8.0 min | +1.543% | 1¢ | ❌ Lost | -$0.15 |
| 10/18 4:05:26 PM | NEAR | DOWN | 9.6 min | +1.841% | 1¢ | ❌ Lost | -$0.15 |
| 10/18 3:59:20 PM | AUDUSD | DOWN | 40 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/18 3:59:20 PM | EURUSD | DOWN | 40 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/18 3:57:28 PM | SOL | DOWN | 2.5 min | +0.274% | 0¢ | ❌ Lost | -$0.15 |
| 10/18 3:57:12 PM | BTC | DOWN | 2.8 min | +0.107% | 1¢ | ❌ Lost | -$0.15 |
| 10/18 3:56:56 PM | ETH | DOWN | 3.1 min | +0.190% | 1¢ | ❌ Lost | -$0.15 |
| 10/18 3:56:39 PM | HYPE | DOWN | 3.3 min | +0.291% | 1¢ | ❌ Lost | -$0.15 |
| 10/18 3:56:23 PM | XRP | DOWN | 3.6 min | +0.299% | 1¢ | ❌ Lost | -$0.15 |
| 10/18 3:56:07 PM | DOGE | DOWN | 3.9 min | +0.382% | 1¢ | ❌ Lost | -$0.15 |
| 10/18 3:55:51 PM | NEAR | DOWN | 4.2 min | +0.476% | 1¢ | ❌ Lost | -$0.15 |
| 10/18 3:55:37 PM | BNB | DOWN | 4.4 min | +0.135% | 0¢ | ❌ Lost | -$0.15 |
| 10/18 3:55:21 PM | ZEC | DOWN | 4.7 min | +0.595% | 1¢ | ❌ Lost | -$0.15 |
| 10/18 3:44:08 PM | EURUSD | DOWN | 51 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/18 3:41:08 PM | XRP | DOWN | 3.9 min | +0.269% | 1¢ | ❌ Lost | -$0.15 |
| 10/18 3:41:08 PM | SOL | DOWN | 3.9 min | +0.301% | 1¢ | ❌ Lost | -$0.15 |
| 10/18 3:40:54 PM | NEAR | DOWN | 4.1 min | +0.461% | 1¢ | ❌ Lost | -$0.15 |
| 10/18 3:40:54 PM | ETH | DOWN | 4.1 min | +0.248% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
