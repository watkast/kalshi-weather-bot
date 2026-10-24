# 15-Minute 1¢ Study

*Updated Sat Oct 24, 5:47 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 2567 finished bets | 1% | $101.00 | +35% | +3.93¢ | $41.60 / $59.40 |

*Expect about **98 buys a day** (~$14.69/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 2369 | $73.65 | +28% |
| Volatility model ≥ 2%, hold to the close | 4747 | $20.45 | +4% |
| Momentum model ≥ 2%, hold to the close | 3950 | -$2.10 | -0% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 30846 | 30838 | 119 (0%) | 1.07% | -$2,090.00 (-56%) | Hold to the close: -$2,090.00 (-56%) |

*In play or awaiting result: 7. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 19631 | 4.6% | 0.4% (84) | -631% | ❌ Worse |
| Momentum model | 19631 | 4.5% | 0.4% (84) | -657% | ❌ Worse |
| Mean-reversion model | 19631 | 7.9% | 0.4% (84) | -763% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 19631 | 84 | -46% | -87% | -87% | -85% |
| Volatility model ≥ 2% | 4747 | 43 | +4% | -78% | -77% | -73% |
| Volatility model ≥ 5% | 2567 | 28 | +35% | -73% | -72% | -68% |
| Volatility model ≥ 10% | 1462 | 18 | +72% | -65% | -63% | -60% |
| Momentum model ≥ 2% | 3950 | 33 | -0% | -79% | -79% | -76% |
| Momentum model ≥ 5% | 2369 | 24 | +28% | -76% | -75% | -71% |
| Momentum model ≥ 10% | 1549 | 16 | +42% | -69% | -68% | -63% |
| Mean-reversion model ≥ 2% | 7888 | 55 | -24% | -83% | -82% | -80% |
| Mean-reversion model ≥ 5% | 5517 | 46 | -8% | -81% | -80% | -77% |
| Mean-reversion model ≥ 10% | 3672 | 33 | +2% | -78% | -77% | -75% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 19831 | 5% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 7352 | 2% | 2% | 1% | 1% | 0% | 0% |
| Financials | 3655 | 2% | 1% | 1% | 1% | 0% | 0% |
| **All** | 30838 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 119 | 0% | -$2,090.00 | -56% | — |
| Sell at 2¢ | 1148 | 4% | -$3,289.52 | -88% | 47 sec |
| Sell at 3¢ | 787 | 3% | -$3,281.07 | -87% | 48 sec |
| Sell at 5¢ | 552 | 2% | -$3,229.20 | -86% | 61 sec |
| Sell at 10¢ | 340 | 1% | -$3,100.60 | -83% | 64 sec |
| Sell at 25¢ | 187 | 1% | -$2,857.03 | -76% | 82 sec |
| Sell at 50¢ | 121 | 0% | -$2,575.25 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 1321 | 7 | 11% | 4% | -49% | -80% | -82% |
| 2–5 min | 9845 | 54 | 7% | 3% | -46% | -87% | -87% |
| 1–2 min | 7838 | 30 | 3% | 1% | -58% | -92% | -91% |
| Under 1 min | 11830 | 28 | 1% | 0% | -66% | -86% | -86% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 2223 | 12 | 5% | 2% | -32% | -89% | -89% |
| HYPE | 2215 | 8 | 5% | 3% | -55% | -88% | -86% |
| BNB | 2212 | 12 | 5% | 2% | -33% | -83% | -83% |
| SOL | 2207 | 6 | 4% | 2% | -66% | -92% | -92% |
| ETH | 2204 | 11 | 6% | 3% | -40% | -86% | -85% |
| DOGE | 2198 | 4 | 4% | 2% | -77% | -90% | -90% |
| XRP | 2195 | 9 | 3% | 1% | -49% | -88% | -88% |
| NEAR | 2191 | 12 | 5% | 3% | -29% | -81% | -81% |
| BTC | 2186 | 12 | 5% | 2% | -27% | -88% | -89% |
| GOLD | 1190 | 4 | 4% | 2% | -60% | -81% | -83% |
| SILVER | 1156 | 5 | 4% | 1% | -50% | -82% | -82% |
| WTI | 1143 | 3 | 3% | 1% | -69% | -94% | -95% |
| PLATINUM | 1010 | 0 | 1% | 1% | -100% | -98% | -98% |
| COPPER | 987 | 4 | 1% | 1% | -62% | -69% | -69% |
| EURUSD | 938 | 3 | 2% | 1% | -70% | -86% | -86% |
| NATGAS | 933 | 5 | 2% | 1% | -50% | -86% | -86% |
| PALLADIUM | 897 | 2 | 1% | 0% | -79% | -88% | -88% |
| GBPUSD | 884 | 1 | 2% | 1% | -89% | -96% | -96% |
| USDJPY | 866 | 5 | 1% | 1% | -46% | -98% | -97% |
| AUDUSD | 428 | 0 | 1% | 0% | -100% | -98% | -98% |
| USDCAD | 387 | 0 | 1% | 0% | -100% | -98% | -99% |
| 10YRRATE | 43 | 0 | 0% | 0% | -100% | -100% | -100% |
| 2YRRATE | 40 | 1 | 2% | 0% | +133% | +138% | +133% |
| 30YRRATE | 39 | 0 | 0% | 0% | -100% | -100% | -100% |
| BRENT | 36 | 0 | 0% | 0% | -100% | -100% | -100% |
| 5YRRATE | 30 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 15598 | 65 | 4% | 2% | -52% | -87% | -86% |
| DOWN (bought NO) | 15240 | 54 | 4% | 2% | -59% | -88% | -88% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 3300 | 18 | 2% | 1% | -8% | -79% | -79% |
| 0.05–0.1% | 3421 | 11 | 3% | 1% | -53% | -92% | -92% |
| 0.1–0.2% | 5109 | 19 | 5% | 2% | -54% | -89% | -89% |
| 0.2–0.5% | 5784 | 28 | 6% | 3% | -47% | -87% | -86% |
| Over 0.5% | 2213 | 10 | 7% | 3% | -53% | -87% | -88% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 7730 | 32 | 4% | 2% | -53% | -85% | -85% |
| Morning (6am–12pm) | 7425 | 34 | 4% | 2% | -48% | -88% | -87% |
| Afternoon (12–6pm) | 7298 | 24 | 4% | 2% | -61% | -87% | -88% |
| Evening (6pm–12am) | 8385 | 29 | 3% | 2% | -60% | -90% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,651 |
| Time from buy to best bounce (bounced bets) | 49 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/24 5:44:58 AM | ETH | UP | 1 sec | -0.008% | 0¢ | ❌ Lost | $0.00 |
| 10/24 5:44:40 AM | XRP | UP | 20 sec | -0.047% | 0¢ | ❌ Lost | $0.00 |
| 10/24 5:44:08 AM | BNB | UP | 52 sec | -0.079% | 0¢ | ❌ Lost | -$0.15 |
| 10/24 5:44:08 AM | BTC | DOWN | 52 sec | +0.036% | 1¢ | ❌ Lost | -$0.15 |
| 10/24 5:43:35 AM | ZEC | UP | 85 sec | -0.252% | 0¢ | ❌ Lost | $0.00 |
| 10/24 5:43:35 AM | DOGE | UP | 85 sec | -0.127% | 1¢ | ❌ Lost | -$0.15 |
| 10/24 5:43:19 AM | SOL | UP | 1.7 min | -0.131% | 1¢ | ❌ Lost | -$0.15 |
| 10/24 5:43:19 AM | NEAR | UP | 1.7 min | -0.378% | 1¢ | ❌ Lost | -$0.15 |
| 10/24 5:40:22 AM | HYPE | DOWN | 4.6 min | +0.257% | 1¢ | ❌ Lost | -$0.15 |
| 10/24 5:29:32 AM | DOGE | UP | 27 sec | -0.090% | 0¢ | ❌ Lost | $0.00 |
| 10/24 5:28:46 AM | BNB | UP | 74 sec | -0.045% | 0¢ | ❌ Lost | $0.00 |
| 10/24 5:28:12 AM | HYPE | UP | 1.8 min | -0.188% | 0¢ | ❌ Lost | -$0.15 |
| 10/24 5:27:43 AM | ZEC | UP | 2.3 min | -0.319% | 0¢ | ❌ Lost | -$0.15 |
| 10/24 5:27:39 AM | NEAR | UP | 2.4 min | -0.736% | 0¢ | ❌ Lost | $0.00 |
| 10/24 5:27:07 AM | SOL | UP | 2.9 min | -0.120% | 1¢ | ❌ Lost | -$0.15 |
| 10/24 5:27:00 AM | BTC | UP | 3.0 min | -0.091% | 1¢ | ❌ Lost | -$0.15 |
| 10/24 5:26:28 AM | ETH | UP | 3.5 min | -0.133% | 1¢ | ❌ Lost | -$0.15 |
| 10/24 5:25:13 AM | XRP | UP | 4.8 min | -0.250% | 1¢ | ❌ Lost | -$0.15 |
| 10/24 5:14:59 AM | NEAR | DOWN | 0 sec | +0.141% | 0¢ | ❌ Lost | $0.00 |
| 10/24 5:14:49 AM | HYPE | UP | 10 sec | -0.053% | 0¢ | ❌ Lost | $0.00 |
| 10/24 5:14:37 AM | BNB | UP | 22 sec | -0.041% | 0¢ | ❌ Lost | $0.00 |
| 10/24 5:14:25 AM | DOGE | DOWN | 34 sec | +0.048% | 1¢ | ❌ Lost | -$0.15 |
| 10/24 5:14:07 AM | XRP | DOWN | 53 sec | +0.086% | 0¢ | ❌ Lost | $0.00 |
| 10/24 5:13:53 AM | SOL | UP | 67 sec | -0.087% | 0¢ | ❌ Lost | $0.00 |
| 10/24 5:12:23 AM | ZEC | DOWN | 2.6 min | +0.223% | 1¢ | ❌ Lost | -$0.15 |
| 10/24 4:59:58 AM | HYPE | UP | 1 sec | -0.032% | 0¢ | ❌ Lost | $0.00 |
| 10/24 4:59:40 AM | XRP | DOWN | 19 sec | +0.039% | 0¢ | ❌ Lost | $0.00 |
| 10/24 4:59:32 AM | ZEC | DOWN | 27 sec | +0.068% | 0¢ | ❌ Lost | -$0.15 |
| 10/24 4:59:32 AM | SOL | UP | 27 sec | -0.031% | 0¢ | ❌ Lost | -$0.15 |
| 10/24 4:59:26 AM | DOGE | DOWN | 33 sec | +0.039% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
