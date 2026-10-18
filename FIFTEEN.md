# 15-Minute 1¢ Study

*Updated Sun Oct 18, 4:15 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 1878 finished bets | 1% | $85.20 | +41% | +4.54¢ | $37.55 / $47.65 |

*Expect about **93 buys a day** (~$13.98/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 1725 | $63.75 | +34% |
| Momentum model ≥ 2%, hold to the close | 2886 | -$0.00 | -0% |
| Volatility model ≥ 5%, sell at 50¢ | 1878 | -$31.80 | -15% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 22570 | 22558 | 86 (0%) | 1.07% | -$1,534.70 (-56%) | Hold to the close: -$1,534.70 (-56%) |

*In play or awaiting result: 11. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 14834 | 4.6% | 0.4% (60) | -662% | ❌ Worse |
| Momentum model | 14834 | 4.5% | 0.4% (60) | -685% | ❌ Worse |
| Mean-reversion model | 14834 | 7.6% | 0.4% (60) | -793% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 14834 | 60 | -49% | -88% | -88% | -85% |
| Volatility model ≥ 2% | 3397 | 27 | -8% | -79% | -79% | -75% |
| Volatility model ≥ 5% | 1878 | 21 | +41% | -75% | -75% | -71% |
| Volatility model ≥ 10% | 1108 | 13 | +66% | -69% | -68% | -65% |
| Momentum model ≥ 2% | 2886 | 24 | -0% | -81% | -81% | -78% |
| Momentum model ≥ 5% | 1725 | 18 | +34% | -79% | -79% | -75% |
| Momentum model ≥ 10% | 1148 | 12 | +46% | -75% | -74% | -69% |
| Mean-reversion model ≥ 2% | 5709 | 38 | -27% | -84% | -84% | -81% |
| Mean-reversion model ≥ 5% | 3961 | 30 | -16% | -82% | -82% | -79% |
| Mean-reversion model ≥ 10% | 2626 | 19 | -17% | -80% | -81% | -78% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 15032 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 5309 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 2217 | 1% | 1% | 1% | 1% | 0% | 0% |
| **All** | 22558 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 86 | 0% | -$1,534.70 | -56% | — |
| Sell at 2¢ | 824 | 4% | -$2,426.46 | -89% | 43 sec |
| Sell at 3¢ | 556 | 2% | -$2,423.86 | -89% | 47 sec |
| Sell at 5¢ | 402 | 2% | -$2,379.40 | -87% | 50 sec |
| Sell at 10¢ | 243 | 1% | -$2,294.37 | -84% | 63 sec |
| Sell at 25¢ | 136 | 1% | -$2,120.54 | -77% | 78 sec |
| Sell at 50¢ | 90 | 0% | -$1,893.20 | -69% | 1.5 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 809 | 5 | 11% | 3% | -41% | -81% | -84% |
| 2–5 min | 7330 | 38 | 7% | 3% | -49% | -87% | -87% |
| 1–2 min | 5816 | 23 | 3% | 2% | -57% | -92% | -92% |
| Under 1 min | 8599 | 20 | 1% | 0% | -66% | -88% | -88% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 1688 | 11 | 4% | 2% | -19% | -90% | -90% |
| HYPE | 1680 | 6 | 5% | 2% | -56% | -90% | -88% |
| BNB | 1676 | 7 | 5% | 2% | -49% | -89% | -88% |
| DOGE | 1673 | 3 | 4% | 2% | -78% | -91% | -90% |
| ETH | 1671 | 9 | 6% | 3% | -35% | -87% | -86% |
| SOL | 1667 | 2 | 3% | 2% | -85% | -92% | -92% |
| XRP | 1662 | 7 | 3% | 1% | -48% | -87% | -87% |
| NEAR | 1658 | 9 | 6% | 3% | -30% | -78% | -78% |
| BTC | 1657 | 8 | 5% | 2% | -35% | -88% | -90% |
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
| UP (bought YES) | 11351 | 42 | 4% | 2% | -57% | -89% | -88% |
| DOWN (bought NO) | 11207 | 44 | 4% | 2% | -55% | -88% | -89% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 2588 | 14 | 2% | 1% | -10% | -82% | -81% |
| 0.05–0.1% | 2615 | 8 | 3% | 2% | -56% | -91% | -91% |
| 0.1–0.2% | 3775 | 13 | 5% | 2% | -58% | -90% | -89% |
| 0.2–0.5% | 4343 | 21 | 6% | 3% | -47% | -88% | -88% |
| Over 0.5% | 1708 | 6 | 7% | 3% | -64% | -87% | -88% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 5701 | 23 | 4% | 2% | -54% | -87% | -87% |
| Morning (6am–12pm) | 5315 | 27 | 4% | 2% | -42% | -87% | -86% |
| Afternoon (12–6pm) | 5311 | 19 | 3% | 1% | -57% | -88% | -89% |
| Evening (6pm–12am) | 6231 | 17 | 3% | 2% | -69% | -92% | -91% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,740 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/18 4:14:46 AM | ZEC | DOWN | 14 sec | +0.243% | 1¢ | In play | — |
| 10/18 4:14:46 AM | SOL | DOWN | 14 sec | +0.109% | 0¢ | ❌ Lost | $0.00 |
| 10/18 4:14:46 AM | BTC | DOWN | 14 sec | +0.084% | 0¢ | In play | — |
| 10/18 4:14:30 AM | DOGE | UP | 30 sec | -0.033% | 93¢ | ✅ Won | $13.85 |
| 10/18 4:14:30 AM | HYPE | DOWN | 30 sec | +0.009% | 0¢ | ❌ Lost | -$0.15 |
| 10/18 4:14:14 AM | NEAR | UP | 46 sec | -0.386% | 1¢ | In play | — |
| 10/18 4:13:59 AM | ETH | UP | 60 sec | -0.079% | 1¢ | In play | — |
| 10/18 4:13:59 AM | BNB | UP | 60 sec | -0.054% | 1¢ | In play | — |
| 10/18 3:59:27 AM | DOGE | UP | 32 sec | -0.070% | 0¢ | ❌ Lost | $0.00 |
| 10/18 3:59:27 AM | SOL | UP | 32 sec | -0.079% | 0¢ | ❌ Lost | $0.00 |
| 10/18 3:59:27 AM | BNB | DOWN | 32 sec | +0.008% | 0¢ | ❌ Lost | $0.00 |
| 10/18 3:59:27 AM | XRP | UP | 32 sec | -0.085% | 0¢ | ❌ Lost | $0.00 |
| 10/18 3:59:11 AM | ZEC | UP | 48 sec | -0.221% | 0¢ | ❌ Lost | -$0.15 |
| 10/18 3:59:11 AM | BTC | UP | 48 sec | -0.032% | 1¢ | ❌ Lost | -$0.15 |
| 10/18 3:58:55 AM | NEAR | DOWN | 64 sec | +0.136% | 1¢ | ❌ Lost | -$0.15 |
| 10/18 3:43:51 AM | XRP | DOWN | 68 sec | +0.116% | 0¢ | ❌ Lost | -$0.15 |
| 10/18 3:42:17 AM | NEAR | DOWN | 2.7 min | +0.585% | 7¢ | ❌ Lost | $0.00 |
| 10/18 3:41:29 AM | ZEC | DOWN | 3.5 min | +0.770% | 1¢ | ❌ Lost | -$0.15 |
| 10/18 3:41:29 AM | SOL | DOWN | 3.5 min | +0.384% | 1¢ | ❌ Lost | -$0.15 |
| 10/18 3:41:13 AM | BNB | DOWN | 3.8 min | +0.179% | 1¢ | ❌ Lost | -$0.15 |
| 10/18 3:40:41 AM | BTC | DOWN | 4.3 min | +0.279% | 1¢ | ❌ Lost | -$0.15 |
| 10/18 3:40:23 AM | HYPE | DOWN | 4.6 min | +0.322% | 1¢ | ❌ Lost | -$0.15 |
| 10/18 3:40:09 AM | DOGE | DOWN | 4.8 min | +0.286% | 1¢ | ❌ Lost | -$0.15 |
| 10/18 3:39:53 AM | ETH | DOWN | 5.1 min | +0.260% | 1¢ | ❌ Lost | -$0.15 |
| 10/18 3:29:53 AM | BTC | DOWN | 6 sec | +0.027% | 0¢ | ❌ Lost | $0.00 |
| 10/18 3:29:53 AM | XRP | DOWN | 6 sec | +0.023% | 0¢ | ❌ Lost | $0.00 |
| 10/18 3:29:53 AM | SOL | DOWN | 6 sec | +0.026% | 0¢ | ❌ Lost | $0.00 |
| 10/18 3:29:37 AM | BNB | DOWN | 22 sec | -0.032% | 0¢ | ❌ Lost | $0.00 |
| 10/18 3:26:43 AM | DOGE | UP | 3.3 min | -0.196% | 8¢ | ❌ Lost | -$0.15 |
| 10/18 3:26:43 AM | ETH | UP | 3.3 min | -0.165% | 3¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
