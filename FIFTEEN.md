# 15-Minute 1¢ Study

*Updated Sun Oct 4, 10:01 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (5+ min left).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| 5+ min left, hold to the close | 186 finished bets | 2% | $14.55 | +53% | +7.82¢ | $14.20 / $0.35 |

*Expect about **28 buys a day** (~$4.26/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 531 | -$1.45 | -3% |
| Momentum model ≥ 5%, hold to the close | 538 | -$1.60 | -3% |
| 5+ min left, sell at 50¢ | 186 | -$7.20 | -26% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 7446 | 7440 | 32 (0%) | 1.07% | -$444.95 (-50%) | Hold to the close: -$444.95 (-50%) |

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
| Volatility model | 4904 | 4.2% | 0.4% (20) | -672% | ❌ Worse |
| Momentum model | 4904 | 4.3% | 0.4% (20) | -706% | ❌ Worse |
| Mean-reversion model | 4904 | 7.0% | 0.4% (20) | -778% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 4904 | 20 | -48% | -84% | -84% | -82% |
| Volatility model ≥ 2% | 989 | 7 | -18% | -68% | -68% | -63% |
| Volatility model ≥ 5% | 531 | 4 | -3% | -53% | -53% | -48% |
| Volatility model ≥ 10% | 331 | 4 | +77% | -32% | -34% | -27% |
| Momentum model ≥ 2% | 872 | 5 | -31% | -68% | -71% | -68% |
| Momentum model ≥ 5% | 538 | 4 | -3% | -59% | -63% | -59% |
| Momentum model ≥ 10% | 369 | 3 | +16% | -46% | -47% | -44% |
| Mean-reversion model ≥ 2% | 1742 | 10 | -38% | -83% | -84% | -79% |
| Mean-reversion model ≥ 5% | 1174 | 9 | -15% | -78% | -79% | -72% |
| Mean-reversion model ≥ 10% | 773 | 7 | +5% | -76% | -78% | -70% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 5101 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 1784 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 555 | 4% | 3% | 2% | 2% | 1% | 1% |
| **All** | 7440 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 32 | 0% | -$444.95 | -50% | — |
| Sell at 2¢ | 300 | 4% | -$786.95 | -88% | 34 sec |
| Sell at 3¢ | 193 | 3% | -$789.68 | -88% | 48 sec |
| Sell at 5¢ | 142 | 2% | -$772.65 | -87% | 61 sec |
| Sell at 10¢ | 96 | 1% | -$725.19 | -81% | 78 sec |
| Sell at 25¢ | 53 | 1% | -$661.52 | -74% | 1.6 min |
| Sell at 50¢ | 31 | 0% | -$585.70 | -66% | 1.9 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 3 | 0 | 100% | 67% | -100% | +73% | +160% |
| 5–10 min | 183 | 3 | 13% | 3% | +56% | -78% | -87% |
| 2–5 min | 2402 | 16 | 8% | 4% | -35% | -86% | -86% |
| 1–2 min | 1954 | 8 | 3% | 2% | -55% | -94% | -93% |
| Under 1 min | 2898 | 5 | 1% | 0% | -74% | -88% | -88% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 575 | 4 | 5% | 3% | -18% | -88% | -89% |
| DOGE | 571 | 2 | 4% | 2% | -55% | -90% | -91% |
| ETH | 570 | 4 | 6% | 3% | -11% | -86% | -86% |
| HYPE | 570 | 2 | 5% | 3% | -57% | -89% | -86% |
| BNB | 565 | 2 | 5% | 2% | -58% | -90% | -92% |
| BTC | 564 | 2 | 5% | 2% | -54% | -87% | -90% |
| SOL | 564 | 0 | 3% | 1% | -100% | -93% | -91% |
| XRP | 562 | 4 | 2% | 1% | -9% | -73% | -73% |
| NEAR | 560 | 2 | 6% | 3% | -53% | -61% | -62% |
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
| UP (bought YES) | 3749 | 17 | 4% | 2% | -47% | -88% | -87% |
| DOWN (bought NO) | 3691 | 15 | 4% | 2% | -53% | -88% | -90% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 849 | 5 | 2% | 1% | -1% | -55% | -55% |
| 0.05–0.1% | 867 | 2 | 3% | 1% | -66% | -91% | -93% |
| 0.1–0.2% | 1254 | 4 | 4% | 2% | -59% | -90% | -91% |
| 0.2–0.5% | 1491 | 7 | 6% | 4% | -48% | -87% | -86% |
| Over 0.5% | 638 | 4 | 7% | 3% | -36% | -86% | -88% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 1882 | 8 | 5% | 2% | -50% | -84% | -86% |
| Morning (6am–12pm) | 1987 | 15 | 5% | 3% | -13% | -89% | -88% |
| Afternoon (12–6pm) | 1513 | 3 | 3% | 1% | -76% | -85% | -87% |
| Evening (6pm–12am) | 2058 | 6 | 3% | 2% | -66% | -93% | -93% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 24 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 3,982 |
| Time from buy to best bounce (bounced bets) | 49 sec |
| Price snapshots per bet | 41 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/4 9:59:50 AM | HYPE | UP | 9 sec | -0.035% | 0¢ | ❌ Lost | $0.00 |
| 10/4 9:59:34 AM | ZEC | UP | 25 sec | -0.116% | 0¢ | ❌ Lost | $0.00 |
| 10/4 9:59:18 AM | DOGE | UP | 41 sec | -0.083% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 9:59:18 AM | BNB | DOWN | 41 sec | -0.034% | 0¢ | ❌ Lost | -$0.15 |
| 10/4 9:59:18 AM | ETH | DOWN | 41 sec | +0.030% | 0¢ | ❌ Lost | $0.00 |
| 10/4 9:58:46 AM | BTC | UP | 73 sec | -0.052% | 0¢ | ❌ Lost | -$0.15 |
| 10/4 9:58:30 AM | NEAR | UP | 89 sec | -0.407% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 9:58:30 AM | SOL | UP | 89 sec | -0.103% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 9:58:14 AM | XRP | DOWN | 1.8 min | +0.133% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 9:44:54 AM | HYPE | DOWN | 5 sec | +0.035% | 0¢ | ❌ Lost | $0.00 |
| 10/4 9:44:39 AM | BTC | DOWN | 20 sec | +0.025% | 0¢ | ❌ Lost | -$0.15 |
| 10/4 9:44:23 AM | ETH | UP | 36 sec | -0.034% | 0¢ | ❌ Lost | $0.00 |
| 10/4 9:44:23 AM | SOL | UP | 36 sec | -0.062% | 0¢ | ❌ Lost | $0.00 |
| 10/4 9:44:07 AM | NEAR | UP | 52 sec | -0.434% | 0¢ | ❌ Lost | $0.00 |
| 10/4 9:44:07 AM | XRP | UP | 52 sec | -0.100% | 0¢ | ❌ Lost | -$0.15 |
| 10/4 9:43:20 AM | DOGE | DOWN | 1.6 min | +0.188% | 1¢ | ❌ Lost | $0.00 |
| 10/4 9:42:32 AM | BNB | UP | 2.5 min | -0.108% | 0¢ | ❌ Lost | -$0.15 |
| 10/4 9:41:11 AM | ZEC | UP | 3.8 min | -0.299% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 9:29:49 AM | BNB | UP | 11 sec | -0.069% | 0¢ | ❌ Lost | $0.00 |
| 10/4 9:29:17 AM | ETH | DOWN | 43 sec | +0.033% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 9:29:02 AM | NEAR | DOWN | 57 sec | +0.111% | 0¢ | ❌ Lost | -$0.15 |
| 10/4 9:29:02 AM | ZEC | DOWN | 57 sec | +0.159% | 0¢ | ❌ Lost | -$0.15 |
| 10/4 9:27:43 AM | DOGE | UP | 2.3 min | -0.262% | 22¢ | ❌ Lost | -$0.15 |
| 10/4 9:27:11 AM | SOL | UP | 2.8 min | -0.251% | 4¢ | ❌ Lost | -$0.15 |
| 10/4 9:26:56 AM | HYPE | UP | 3.0 min | -0.271% | 22¢ | ❌ Lost | -$0.15 |
| 10/4 9:14:15 AM | SOL | DOWN | 44 sec | +0.083% | 0¢ | ❌ Lost | -$0.15 |
| 10/4 9:14:15 AM | ZEC | DOWN | 44 sec | +0.153% | 0¢ | ❌ Lost | -$0.15 |
| 10/4 9:13:57 AM | ETH | DOWN | 63 sec | +0.056% | 0¢ | ❌ Lost | -$0.15 |
| 10/4 9:13:41 AM | BTC | DOWN | 79 sec | +0.068% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 9:13:25 AM | DOGE | DOWN | 1.6 min | +0.155% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
