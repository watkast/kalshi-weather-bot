# 15-Minute 1¢ Study

*Updated Sun Oct 18, 5:47 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 1887 finished bets | 1% | $84.00 | +40% | +4.45¢ | $37.10 / $46.90 |

*Expect about **93 buys a day** (~$14.00/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 1733 | $62.70 | +33% |
| Momentum model ≥ 2%, hold to the close | 2899 | -$1.80 | -1% |
| Volatility model ≥ 5%, sell at 50¢ | 1887 | -$33.00 | -16% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 22622 | 22615 | 86 (0%) | 1.07% | -$1,541.30 (-56%) | Hold to the close: -$1,541.30 (-56%) |

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
| Volatility model | 14891 | 4.6% | 0.4% (60) | -668% | ❌ Worse |
| Momentum model | 14891 | 4.5% | 0.4% (60) | -691% | ❌ Worse |
| Mean-reversion model | 14891 | 7.7% | 0.4% (60) | -800% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 14891 | 60 | -50% | -88% | -88% | -85% |
| Volatility model ≥ 2% | 3417 | 27 | -9% | -79% | -79% | -75% |
| Volatility model ≥ 5% | 1887 | 21 | +40% | -76% | -75% | -71% |
| Volatility model ≥ 10% | 1116 | 13 | +64% | -69% | -68% | -66% |
| Momentum model ≥ 2% | 2899 | 24 | -1% | -81% | -81% | -78% |
| Momentum model ≥ 5% | 1733 | 18 | +33% | -79% | -79% | -75% |
| Momentum model ≥ 10% | 1155 | 12 | +45% | -75% | -75% | -70% |
| Mean-reversion model ≥ 2% | 5735 | 38 | -28% | -84% | -84% | -81% |
| Mean-reversion model ≥ 5% | 3981 | 30 | -17% | -82% | -82% | -79% |
| Mean-reversion model ≥ 10% | 2641 | 19 | -18% | -81% | -81% | -78% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 15089 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 5309 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 2217 | 1% | 1% | 1% | 1% | 0% | 0% |
| **All** | 22615 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 86 | 0% | -$1,541.30 | -56% | — |
| Sell at 2¢ | 826 | 4% | -$2,432.54 | -89% | 44 sec |
| Sell at 3¢ | 557 | 2% | -$2,430.07 | -89% | 47 sec |
| Sell at 5¢ | 403 | 2% | -$2,385.35 | -87% | 50 sec |
| Sell at 10¢ | 243 | 1% | -$2,300.97 | -84% | 63 sec |
| Sell at 25¢ | 136 | 1% | -$2,127.14 | -77% | 78 sec |
| Sell at 50¢ | 90 | 0% | -$1,899.80 | -69% | 1.5 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 810 | 5 | 10% | 3% | -41% | -81% | -84% |
| 2–5 min | 7349 | 38 | 7% | 3% | -49% | -87% | -87% |
| 1–2 min | 5826 | 23 | 3% | 2% | -57% | -92% | -92% |
| Under 1 min | 8626 | 20 | 1% | 0% | -66% | -88% | -88% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 1695 | 11 | 4% | 2% | -19% | -90% | -90% |
| HYPE | 1685 | 6 | 5% | 2% | -56% | -90% | -88% |
| BNB | 1683 | 7 | 5% | 2% | -49% | -89% | -88% |
| DOGE | 1679 | 3 | 4% | 2% | -78% | -91% | -90% |
| ETH | 1678 | 9 | 6% | 3% | -35% | -87% | -86% |
| SOL | 1673 | 2 | 3% | 2% | -85% | -92% | -92% |
| XRP | 1668 | 7 | 3% | 1% | -48% | -87% | -87% |
| NEAR | 1665 | 9 | 6% | 3% | -30% | -78% | -78% |
| BTC | 1663 | 8 | 5% | 2% | -35% | -88% | -90% |
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
| UP (bought YES) | 11386 | 42 | 4% | 2% | -58% | -89% | -88% |
| DOWN (bought NO) | 11229 | 44 | 4% | 2% | -55% | -88% | -89% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 2599 | 14 | 2% | 1% | -11% | -82% | -81% |
| 0.05–0.1% | 2633 | 8 | 3% | 2% | -56% | -92% | -91% |
| 0.1–0.2% | 3788 | 13 | 5% | 2% | -58% | -90% | -89% |
| 0.2–0.5% | 4357 | 21 | 6% | 3% | -47% | -88% | -88% |
| Over 0.5% | 1709 | 6 | 7% | 3% | -64% | -87% | -88% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 5758 | 23 | 4% | 2% | -55% | -87% | -88% |
| Morning (6am–12pm) | 5315 | 27 | 4% | 2% | -42% | -87% | -86% |
| Afternoon (12–6pm) | 5311 | 19 | 3% | 1% | -57% | -88% | -89% |
| Evening (6pm–12am) | 6231 | 17 | 3% | 2% | -69% | -92% | -91% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,750 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/18 5:43:04 AM | BTC | UP | 1.9 min | -0.098% | 1¢ | ❌ Lost | -$0.15 |
| 10/18 5:42:49 AM | ZEC | UP | 2.2 min | -0.322% | 0¢ | ❌ Lost | -$0.15 |
| 10/18 5:42:32 AM | XRP | UP | 2.5 min | -0.208% | 1¢ | ❌ Lost | -$0.15 |
| 10/18 5:42:32 AM | SOL | UP | 2.5 min | -0.214% | 1¢ | ❌ Lost | -$0.15 |
| 10/18 5:41:45 AM | HYPE | UP | 3.2 min | -0.237% | 1¢ | ❌ Lost | -$0.15 |
| 10/18 5:41:45 AM | ETH | UP | 3.2 min | -0.117% | 1¢ | ❌ Lost | -$0.15 |
| 10/18 5:40:25 AM | BNB | UP | 4.6 min | -0.120% | 0¢ | ❌ Lost | -$0.15 |
| 10/18 5:40:09 AM | NEAR | UP | 4.8 min | -0.993% | 1¢ | ❌ Lost | -$0.15 |
| 10/18 5:39:38 AM | DOGE | UP | 5.3 min | -0.257% | 1¢ | ❌ Lost | -$0.15 |
| 10/18 5:29:44 AM | BTC | DOWN | 16 sec | -0.003% | 1¢ | ❌ Lost | -$0.15 |
| 10/18 5:29:28 AM | BNB | DOWN | 32 sec | -0.005% | 1¢ | ❌ Lost | -$0.15 |
| 10/18 5:29:12 AM | HYPE | DOWN | 48 sec | +0.045% | 0¢ | ❌ Lost | $0.00 |
| 10/18 5:29:12 AM | ETH | DOWN | 48 sec | +0.055% | 0¢ | ❌ Lost | -$0.15 |
| 10/18 5:29:12 AM | SOL | DOWN | 48 sec | +0.070% | 0¢ | ❌ Lost | $0.00 |
| 10/18 5:28:56 AM | ZEC | DOWN | 64 sec | +0.150% | 1¢ | ❌ Lost | -$0.15 |
| 10/18 5:26:49 AM | NEAR | DOWN | 3.2 min | +0.378% | 3¢ | ❌ Lost | -$0.15 |
| 10/18 5:25:30 AM | DOGE | DOWN | 4.5 min | +0.155% | 1¢ | ❌ Lost | -$0.15 |
| 10/18 5:25:30 AM | XRP | DOWN | 4.5 min | +0.278% | 1¢ | ❌ Lost | -$0.15 |
| 10/18 5:14:28 AM | DOGE | UP | 31 sec | -0.049% | 0¢ | ❌ Lost | -$0.15 |
| 10/18 5:14:28 AM | SOL | DOWN | 31 sec | +0.029% | 0¢ | ❌ Lost | -$0.15 |
| 10/18 5:14:12 AM | ETH | UP | 47 sec | -0.072% | 0¢ | ❌ Lost | $0.00 |
| 10/18 5:14:12 AM | XRP | UP | 47 sec | -0.139% | 0¢ | ❌ Lost | $0.00 |
| 10/18 5:13:43 AM | ZEC | UP | 77 sec | -0.236% | 0¢ | ❌ Lost | -$0.15 |
| 10/18 5:12:55 AM | NEAR | UP | 2.1 min | -0.455% | 1¢ | ❌ Lost | -$0.15 |
| 10/18 5:10:31 AM | BNB | DOWN | 4.5 min | +0.073% | 1¢ | ❌ Lost | -$0.15 |
| 10/18 4:58:43 AM | DOGE | UP | 76 sec | -0.102% | 1¢ | ❌ Lost | -$0.15 |
| 10/18 4:58:11 AM | XRP | UP | 1.8 min | -0.131% | 1¢ | ❌ Lost | -$0.15 |
| 10/18 4:57:40 AM | BNB | UP | 2.3 min | -0.093% | 1¢ | ❌ Lost | -$0.15 |
| 10/18 4:57:24 AM | NEAR | UP | 2.6 min | -0.348% | 8¢ | ❌ Lost | -$0.15 |
| 10/18 4:57:24 AM | SOL | UP | 2.6 min | -0.180% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
