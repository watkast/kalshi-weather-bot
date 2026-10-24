# 15-Minute 1¢ Study

*Updated Sat Oct 24, 8:01 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 2576 finished bets | 1% | $99.95 | +34% | +3.88¢ | $40.85 / $59.10 |

*Expect about **98 buys a day** (~$14.69/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 2378 | $72.75 | +28% |
| Volatility model ≥ 2%, hold to the close | 4759 | $18.95 | +3% |
| Momentum model ≥ 2%, hold to the close | 3964 | -$3.75 | -1% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 30922 | 30914 | 119 (0%) | 1.07% | -$2,097.95 (-56%) | Hold to the close: -$2,097.95 (-56%) |

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
| Volatility model | 19707 | 4.7% | 0.4% (84) | -635% | ❌ Worse |
| Momentum model | 19707 | 4.6% | 0.4% (84) | -660% | ❌ Worse |
| Mean-reversion model | 19707 | 7.9% | 0.4% (84) | -769% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 19707 | 84 | -47% | -87% | -87% | -85% |
| Volatility model ≥ 2% | 4759 | 43 | +3% | -78% | -77% | -73% |
| Volatility model ≥ 5% | 2576 | 28 | +34% | -73% | -72% | -69% |
| Volatility model ≥ 10% | 1468 | 18 | +72% | -65% | -63% | -60% |
| Momentum model ≥ 2% | 3964 | 33 | -1% | -79% | -79% | -76% |
| Momentum model ≥ 5% | 2378 | 24 | +28% | -76% | -75% | -71% |
| Momentum model ≥ 10% | 1555 | 16 | +41% | -69% | -68% | -63% |
| Mean-reversion model ≥ 2% | 7918 | 55 | -24% | -83% | -82% | -80% |
| Mean-reversion model ≥ 5% | 5540 | 46 | -9% | -81% | -80% | -77% |
| Mean-reversion model ≥ 10% | 3686 | 33 | +1% | -78% | -77% | -75% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 19907 | 5% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 7352 | 2% | 2% | 1% | 1% | 0% | 0% |
| Financials | 3655 | 2% | 1% | 1% | 1% | 0% | 0% |
| **All** | 30914 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 119 | 0% | -$2,097.95 | -56% | — |
| Sell at 2¢ | 1151 | 4% | -$3,296.69 | -88% | 47 sec |
| Sell at 3¢ | 789 | 3% | -$3,288.24 | -87% | 48 sec |
| Sell at 5¢ | 553 | 2% | -$3,236.50 | -86% | 61 sec |
| Sell at 10¢ | 340 | 1% | -$3,108.55 | -83% | 64 sec |
| Sell at 25¢ | 187 | 1% | -$2,864.98 | -76% | 82 sec |
| Sell at 50¢ | 121 | 0% | -$2,583.20 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 1326 | 7 | 11% | 4% | -50% | -80% | -82% |
| 2–5 min | 9870 | 54 | 7% | 3% | -46% | -87% | -87% |
| 1–2 min | 7850 | 30 | 3% | 1% | -58% | -92% | -91% |
| Under 1 min | 11864 | 28 | 1% | 0% | -66% | -86% | -86% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 2232 | 12 | 5% | 2% | -32% | -89% | -89% |
| HYPE | 2224 | 8 | 5% | 3% | -56% | -88% | -86% |
| BNB | 2221 | 12 | 5% | 2% | -33% | -83% | -82% |
| SOL | 2216 | 6 | 4% | 2% | -66% | -92% | -92% |
| ETH | 2211 | 11 | 6% | 3% | -40% | -86% | -85% |
| DOGE | 2207 | 4 | 4% | 2% | -77% | -90% | -90% |
| XRP | 2203 | 9 | 3% | 1% | -49% | -88% | -88% |
| NEAR | 2200 | 12 | 5% | 3% | -29% | -81% | -81% |
| BTC | 2193 | 12 | 5% | 2% | -27% | -88% | -89% |
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
| UP (bought YES) | 15643 | 65 | 4% | 2% | -52% | -87% | -86% |
| DOWN (bought NO) | 15271 | 54 | 4% | 2% | -59% | -88% | -88% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 3323 | 18 | 2% | 1% | -9% | -79% | -79% |
| 0.05–0.1% | 3433 | 11 | 3% | 1% | -53% | -92% | -92% |
| 0.1–0.2% | 5131 | 19 | 5% | 2% | -54% | -89% | -89% |
| 0.2–0.5% | 5799 | 28 | 6% | 3% | -47% | -87% | -86% |
| Over 0.5% | 2217 | 10 | 7% | 3% | -53% | -87% | -88% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 7739 | 32 | 4% | 2% | -53% | -85% | -85% |
| Morning (6am–12pm) | 7492 | 34 | 4% | 2% | -48% | -88% | -87% |
| Afternoon (12–6pm) | 7298 | 24 | 4% | 2% | -61% | -87% | -88% |
| Evening (6pm–12am) | 8385 | 29 | 3% | 2% | -60% | -90% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,662 |
| Time from buy to best bounce (bounced bets) | 49 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/24 7:59:37 AM | SOL | UP | 23 sec | -0.062% | 0¢ | ❌ Lost | $0.00 |
| 10/24 7:59:37 AM | DOGE | UP | 23 sec | -0.093% | 0¢ | ❌ Lost | $0.00 |
| 10/24 7:59:37 AM | BTC | UP | 23 sec | -0.019% | 0¢ | ❌ Lost | -$0.15 |
| 10/24 7:59:21 AM | ETH | DOWN | 39 sec | +0.010% | 0¢ | ❌ Lost | -$0.15 |
| 10/24 7:58:34 AM | HYPE | DOWN | 85 sec | +0.083% | 0¢ | ❌ Lost | -$0.15 |
| 10/24 7:58:34 AM | BNB | UP | 85 sec | -0.079% | 0¢ | ❌ Lost | $0.00 |
| 10/24 7:57:12 AM | ZEC | UP | 2.8 min | -0.339% | 0¢ | ❌ Lost | -$0.15 |
| 10/24 7:57:12 AM | NEAR | UP | 2.8 min | -0.449% | 1¢ | ❌ Lost | -$0.15 |
| 10/24 7:44:54 AM | XRP | UP | 5 sec | -0.047% | 0¢ | ❌ Lost | -$0.15 |
| 10/24 7:44:54 AM | BNB | DOWN | 5 sec | -0.005% | 0¢ | ❌ Lost | $0.00 |
| 10/24 7:44:38 AM | SOL | UP | 21 sec | -0.023% | 0¢ | ❌ Lost | $0.00 |
| 10/24 7:44:38 AM | DOGE | DOWN | 21 sec | -0.009% | 0¢ | ❌ Lost | $0.00 |
| 10/24 7:44:22 AM | ZEC | DOWN | 37 sec | +0.092% | 0¢ | ❌ Lost | $0.00 |
| 10/24 7:43:48 AM | HYPE | DOWN | 72 sec | +0.113% | 0¢ | ❌ Lost | -$0.15 |
| 10/24 7:43:01 AM | NEAR | DOWN | 2.0 min | +0.478% | 1¢ | ❌ Lost | -$0.15 |
| 10/24 7:41:57 AM | BTC | UP | 3.0 min | -0.122% | 1¢ | ❌ Lost | -$0.15 |
| 10/24 7:41:24 AM | ETH | UP | 3.6 min | -0.165% | 1¢ | ❌ Lost | -$0.15 |
| 10/24 7:29:51 AM | ETH | UP | 9 sec | -0.025% | 0¢ | ❌ Lost | $0.00 |
| 10/24 7:29:04 AM | XRP | UP | 55 sec | -0.078% | 1¢ | ❌ Lost | -$0.15 |
| 10/24 7:28:32 AM | BNB | UP | 87 sec | -0.108% | 1¢ | ❌ Lost | -$0.15 |
| 10/24 7:28:32 AM | NEAR | UP | 87 sec | -0.284% | 0¢ | ❌ Lost | -$0.15 |
| 10/24 7:28:16 AM | SOL | UP | 1.7 min | -0.139% | 0¢ | ❌ Lost | -$0.15 |
| 10/24 7:27:26 AM | ZEC | UP | 2.6 min | -0.296% | 1¢ | ❌ Lost | -$0.15 |
| 10/24 7:27:26 AM | DOGE | UP | 2.6 min | -0.177% | 1¢ | ❌ Lost | -$0.15 |
| 10/24 7:27:26 AM | HYPE | UP | 2.6 min | -0.186% | 1¢ | ❌ Lost | -$0.15 |
| 10/24 7:14:53 AM | ZEC | UP | 7 sec | -0.034% | 0¢ | ❌ Lost | $0.00 |
| 10/24 7:14:53 AM | XRP | UP | 7 sec | -0.047% | 0¢ | ❌ Lost | $0.00 |
| 10/24 7:14:37 AM | BTC | UP | 23 sec | -0.022% | 0¢ | ❌ Lost | $0.00 |
| 10/24 7:14:22 AM | BNB | UP | 38 sec | -0.037% | 0¢ | ❌ Lost | -$0.15 |
| 10/24 7:14:22 AM | HYPE | DOWN | 38 sec | +0.049% | 0¢ | ❌ Lost | $0.00 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
