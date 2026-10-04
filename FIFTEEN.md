# 15-Minute 1¢ Study

*Updated Sun Oct 4, 2:11 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Momentum model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 503 finished bets | 1% | $3.05 | +6% | +0.61¢ | $0.40 / $2.65 |

*Expect about **83 buys a day** (~$12.45/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| 5+ min left, hold to the close | 179 | $1.60 | +6% |
| Volatility model ≥ 5%, hold to the close | 498 | -$10.95 | -21% |
| Volatility model ≥ 5%, sell at 50¢ | 498 | -$11.45 | -22% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 7171 | 7164 | 30 (0%) | 1.07% | -$440.70 (-51%) | Hold to the close: -$440.70 (-51%) |

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
| Volatility model | 4628 | 4.2% | 0.4% (18) | -685% | ❌ Worse |
| Momentum model | 4628 | 4.3% | 0.4% (18) | -720% | ❌ Worse |
| Mean-reversion model | 4628 | 7.0% | 0.4% (18) | -804% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 4628 | 18 | -51% | -84% | -85% | -82% |
| Volatility model ≥ 2% | 939 | 6 | -26% | -68% | -69% | -64% |
| Volatility model ≥ 5% | 498 | 3 | -21% | -52% | -53% | -50% |
| Volatility model ≥ 10% | 304 | 3 | +50% | -28% | -31% | -27% |
| Momentum model ≥ 2% | 824 | 5 | -26% | -68% | -71% | -68% |
| Momentum model ≥ 5% | 503 | 4 | +6% | -57% | -61% | -58% |
| Momentum model ≥ 10% | 343 | 3 | +28% | -42% | -44% | -42% |
| Mean-reversion model ≥ 2% | 1654 | 9 | -41% | -84% | -85% | -80% |
| Mean-reversion model ≥ 5% | 1116 | 8 | -20% | -80% | -81% | -74% |
| Mean-reversion model ≥ 10% | 735 | 6 | -5% | -77% | -79% | -72% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 4825 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 1784 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 555 | 4% | 3% | 2% | 2% | 1% | 1% |
| **All** | 7164 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 30 | 0% | -$440.70 | -51% | — |
| Sell at 2¢ | 276 | 4% | -$760.94 | -88% | 34 sec |
| Sell at 3¢ | 176 | 2% | -$764.06 | -89% | 48 sec |
| Sell at 5¢ | 132 | 2% | -$746.90 | -87% | 62 sec |
| Sell at 10¢ | 88 | 1% | -$703.42 | -82% | 80 sec |
| Sell at 25¢ | 49 | 1% | -$642.51 | -75% | 1.6 min |
| Sell at 50¢ | 29 | 0% | -$566.95 | -66% | 1.9 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 3 | 0 | 100% | 67% | -100% | +73% | +160% |
| 5–10 min | 176 | 2 | 11% | 3% | +8% | -80% | -89% |
| 2–5 min | 2320 | 15 | 8% | 4% | -37% | -86% | -87% |
| 1–2 min | 1870 | 8 | 3% | 2% | -53% | -94% | -93% |
| Under 1 min | 2795 | 5 | 1% | 0% | -73% | -87% | -87% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| DOGE | 543 | 2 | 4% | 1% | -52% | -91% | -92% |
| ZEC | 543 | 4 | 5% | 3% | -13% | -89% | -89% |
| HYPE | 541 | 2 | 5% | 3% | -55% | -89% | -86% |
| ETH | 538 | 4 | 6% | 3% | -5% | -86% | -86% |
| SOL | 534 | 0 | 3% | 1% | -100% | -93% | -92% |
| BNB | 534 | 1 | 4% | 2% | -78% | -91% | -93% |
| BTC | 532 | 1 | 5% | 2% | -75% | -87% | -90% |
| XRP | 532 | 4 | 2% | 1% | -3% | -72% | -72% |
| NEAR | 528 | 2 | 6% | 2% | -49% | -60% | -63% |
| GOLD | 304 | 0 | 5% | 1% | -100% | -90% | -92% |
| SILVER | 285 | 0 | 2% | 1% | -100% | -95% | -95% |
| WTI | 274 | 2 | 3% | 1% | -23% | -94% | -96% |
| COPPER | 254 | 0 | 1% | 0% | -100% | -99% | -99% |
| PLATINUM | 226 | 0 | 0% | 0% | -100% | -100% | -100% |
| NATGAS | 225 | 2 | 4% | 2% | -17% | -94% | -92% |
| PALLADIUM | 216 | 1 | 2% | 1% | -57% | -96% | -98% |
| GBPUSD | 195 | 1 | 4% | 2% | -52% | -93% | -93% |
| EURUSD | 195 | 1 | 5% | 3% | -52% | -91% | -89% |
| USDJPY | 165 | 3 | 2% | 2% | +70% | -96% | -94% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 3615 | 17 | 4% | 2% | -45% | -88% | -88% |
| DOWN (bought NO) | 3549 | 13 | 4% | 2% | -58% | -88% | -90% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 778 | 5 | 2% | 1% | +10% | -51% | -50% |
| 0.05–0.1% | 797 | 0 | 3% | 1% | -100% | -93% | -94% |
| 0.1–0.2% | 1185 | 4 | 4% | 2% | -56% | -91% | -91% |
| 0.2–0.5% | 1438 | 7 | 6% | 3% | -46% | -88% | -87% |
| Over 0.5% | 625 | 4 | 7% | 3% | -34% | -87% | -89% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 1744 | 8 | 4% | 2% | -47% | -84% | -86% |
| Morning (6am–12pm) | 1849 | 13 | 5% | 3% | -20% | -90% | -89% |
| Afternoon (12–6pm) | 1513 | 3 | 3% | 1% | -76% | -85% | -87% |
| Evening (6pm–12am) | 2058 | 6 | 3% | 2% | -66% | -93% | -93% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 24 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 3,876 |
| Time from buy to best bounce (bounced bets) | 49 sec |
| Price snapshots per bet | 41 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/4 2:10:47 AM | HYPE | DOWN | 4.2 min | +0.504% | — | In play | — |
| 10/4 1:59:36 AM | ZEC | UP | 24 sec | -0.041% | 0¢ | ❌ Lost | -$0.15 |
| 10/4 1:59:20 AM | SOL | DOWN | 40 sec | +0.062% | 0¢ | ❌ Lost | -$0.15 |
| 10/4 1:58:32 AM | NEAR | DOWN | 88 sec | +0.307% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 1:58:16 AM | HYPE | DOWN | 1.7 min | +0.110% | 0¢ | ❌ Lost | $0.00 |
| 10/4 1:57:45 AM | BTC | DOWN | 2.2 min | +0.109% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 1:57:45 AM | XRP | DOWN | 2.2 min | +0.194% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 1:57:45 AM | DOGE | DOWN | 2.2 min | +0.205% | 0¢ | ❌ Lost | -$0.15 |
| 10/4 1:55:53 AM | ETH | DOWN | 4.1 min | +0.139% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 1:44:49 AM | BTC | UP | 11 sec | -0.008% | 0¢ | ❌ Lost | $0.00 |
| 10/4 1:44:33 AM | DOGE | DOWN | 27 sec | +0.039% | 0¢ | ❌ Lost | -$0.15 |
| 10/4 1:44:17 AM | BNB | UP | 43 sec | -0.063% | 0¢ | ❌ Lost | $0.00 |
| 10/4 1:44:17 AM | XRP | UP | 43 sec | -0.067% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 1:44:01 AM | SOL | UP | 59 sec | -0.110% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 1:43:45 AM | HYPE | DOWN | 75 sec | +0.098% | 0¢ | ❌ Lost | $0.00 |
| 10/4 1:43:45 AM | ETH | DOWN | 75 sec | +0.070% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 1:42:39 AM | NEAR | UP | 2.4 min | -0.451% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 1:42:07 AM | ZEC | DOWN | 2.9 min | +0.321% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 1:29:34 AM | BTC | UP | 26 sec | -0.026% | 0¢ | ❌ Lost | $0.00 |
| 10/4 1:29:18 AM | SOL | UP | 42 sec | -0.041% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 1:29:03 AM | XRP | UP | 56 sec | -0.060% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 1:29:03 AM | NEAR | UP | 56 sec | -0.351% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 1:28:15 AM | HYPE | DOWN | 1.8 min | +0.147% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 1:28:15 AM | ETH | UP | 1.8 min | -0.088% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 1:27:43 AM | ZEC | DOWN | 2.3 min | +0.322% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 1:27:43 AM | DOGE | UP | 2.3 min | -0.153% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 1:14:35 AM | BNB | UP | 24 sec | -0.077% | 0¢ | ❌ Lost | $0.00 |
| 10/4 1:14:19 AM | XRP | DOWN | 40 sec | +0.093% | 0¢ | ❌ Lost | $0.00 |
| 10/4 1:14:19 AM | NEAR | UP | 40 sec | -0.253% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 1:13:47 AM | ETH | UP | 72 sec | -0.043% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
