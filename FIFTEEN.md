# 15-Minute 1¢ Study

*Updated Sun Oct 4, 9:30 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (5+ min left).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| 5+ min left, hold to the close | 186 finished bets | 2% | $14.55 | +53% | +7.82¢ | $14.20 / $0.35 |

*Expect about **28 buys a day** (~$4.27/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 530 | -$1.30 | -2% |
| Momentum model ≥ 5%, hold to the close | 537 | -$1.45 | -3% |
| 5+ min left, sell at 50¢ | 186 | -$7.20 | -26% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 7428 | 7418 | 32 (0%) | 1.07% | -$443.00 (-50%) | Hold to the close: -$443.00 (-50%) |

*In play or awaiting result: 10. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 4882 | 4.2% | 0.4% (20) | -667% | ❌ Worse |
| Momentum model | 4882 | 4.3% | 0.4% (20) | -701% | ❌ Worse |
| Mean-reversion model | 4882 | 7.0% | 0.4% (20) | -773% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 4882 | 20 | -48% | -84% | -85% | -82% |
| Volatility model ≥ 2% | 987 | 7 | -18% | -68% | -68% | -63% |
| Volatility model ≥ 5% | 530 | 4 | -2% | -53% | -53% | -48% |
| Volatility model ≥ 10% | 330 | 4 | +78% | -32% | -33% | -27% |
| Momentum model ≥ 2% | 870 | 5 | -31% | -68% | -71% | -68% |
| Momentum model ≥ 5% | 537 | 4 | -3% | -59% | -63% | -59% |
| Momentum model ≥ 10% | 368 | 3 | +16% | -45% | -47% | -43% |
| Mean-reversion model ≥ 2% | 1737 | 10 | -37% | -83% | -84% | -79% |
| Mean-reversion model ≥ 5% | 1171 | 9 | -15% | -78% | -79% | -72% |
| Mean-reversion model ≥ 10% | 770 | 7 | +5% | -77% | -78% | -71% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 5079 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 1784 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 555 | 4% | 3% | 2% | 2% | 1% | 1% |
| **All** | 7418 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 32 | 0% | -$443.00 | -50% | — |
| Sell at 2¢ | 297 | 4% | -$785.78 | -88% | 34 sec |
| Sell at 3¢ | 190 | 3% | -$788.90 | -89% | 48 sec |
| Sell at 5¢ | 140 | 2% | -$772.00 | -87% | 61 sec |
| Sell at 10¢ | 94 | 1% | -$725.86 | -81% | 78 sec |
| Sell at 25¢ | 53 | 1% | -$659.57 | -74% | 1.6 min |
| Sell at 50¢ | 31 | 0% | -$583.75 | -66% | 1.9 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 3 | 0 | 100% | 67% | -100% | +73% | +160% |
| 5–10 min | 183 | 3 | 13% | 3% | +56% | -78% | -87% |
| 2–5 min | 2397 | 16 | 8% | 4% | -35% | -86% | -86% |
| 1–2 min | 1949 | 8 | 3% | 2% | -55% | -94% | -93% |
| Under 1 min | 2886 | 5 | 1% | 0% | -74% | -88% | -88% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 573 | 4 | 5% | 3% | -18% | -88% | -89% |
| ETH | 568 | 4 | 6% | 3% | -11% | -86% | -86% |
| DOGE | 568 | 2 | 4% | 1% | -54% | -91% | -91% |
| HYPE | 567 | 2 | 5% | 3% | -57% | -89% | -86% |
| BTC | 562 | 2 | 6% | 2% | -53% | -87% | -90% |
| BNB | 562 | 2 | 5% | 2% | -58% | -90% | -92% |
| SOL | 561 | 0 | 3% | 1% | -100% | -93% | -92% |
| XRP | 560 | 4 | 2% | 1% | -8% | -73% | -73% |
| NEAR | 558 | 2 | 6% | 3% | -52% | -61% | -62% |
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
| UP (bought YES) | 3733 | 17 | 4% | 2% | -46% | -88% | -88% |
| DOWN (bought NO) | 3685 | 15 | 4% | 2% | -53% | -88% | -90% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 843 | 5 | 2% | 1% | -0% | -55% | -55% |
| 0.05–0.1% | 862 | 2 | 3% | 1% | -65% | -91% | -93% |
| 0.1–0.2% | 1249 | 4 | 4% | 2% | -59% | -90% | -91% |
| 0.2–0.5% | 1485 | 7 | 6% | 3% | -48% | -87% | -87% |
| Over 0.5% | 638 | 4 | 7% | 3% | -36% | -86% | -88% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 1882 | 8 | 5% | 2% | -50% | -84% | -86% |
| Morning (6am–12pm) | 1965 | 15 | 5% | 3% | -13% | -89% | -88% |
| Afternoon (12–6pm) | 1513 | 3 | 3% | 1% | -76% | -85% | -87% |
| Evening (6pm–12am) | 2058 | 6 | 3% | 2% | -66% | -93% | -93% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 24 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 3,974 |
| Time from buy to best bounce (bounced bets) | 49 sec |
| Price snapshots per bet | 41 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/4 9:29:49 AM | BNB | UP | 11 sec | -0.069% | 0¢ | In play | — |
| 10/4 9:29:17 AM | ETH | DOWN | 43 sec | +0.033% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 9:29:02 AM | NEAR | DOWN | 57 sec | +0.111% | 0¢ | ❌ Lost | -$0.15 |
| 10/4 9:29:02 AM | ZEC | DOWN | 57 sec | +0.159% | 0¢ | ❌ Lost | -$0.15 |
| 10/4 9:27:43 AM | DOGE | UP | 2.3 min | -0.262% | 22¢ | In play | — |
| 10/4 9:27:11 AM | SOL | UP | 2.8 min | -0.251% | 4¢ | In play | — |
| 10/4 9:26:56 AM | HYPE | UP | 3.0 min | -0.271% | 22¢ | In play | — |
| 10/4 9:14:15 AM | SOL | DOWN | 44 sec | +0.083% | 0¢ | ❌ Lost | -$0.15 |
| 10/4 9:14:15 AM | ZEC | DOWN | 44 sec | +0.153% | 0¢ | ❌ Lost | -$0.15 |
| 10/4 9:13:57 AM | ETH | DOWN | 63 sec | +0.056% | 0¢ | ❌ Lost | -$0.15 |
| 10/4 9:13:41 AM | BTC | DOWN | 79 sec | +0.068% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 9:13:25 AM | DOGE | DOWN | 1.6 min | +0.155% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 9:13:10 AM | XRP | DOWN | 1.8 min | +0.200% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 9:12:53 AM | NEAR | UP | 2.1 min | -0.537% | 4¢ | ❌ Lost | -$0.15 |
| 10/4 9:12:21 AM | BNB | DOWN | 2.6 min | +0.061% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 8:59:46 AM | NEAR | DOWN | 14 sec | -0.126% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 8:59:15 AM | BNB | DOWN | 45 sec | -0.008% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 8:59:15 AM | ZEC | DOWN | 45 sec | +0.118% | 0¢ | ❌ Lost | -$0.15 |
| 10/4 8:58:10 AM | ETH | DOWN | 1.8 min | +0.113% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 8:57:19 AM | DOGE | DOWN | 2.7 min | +0.270% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 8:57:19 AM | XRP | DOWN | 2.7 min | +0.173% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 8:55:59 AM | SOL | DOWN | 4.0 min | +0.206% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 8:55:59 AM | BTC | DOWN | 4.0 min | +0.129% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 8:44:35 AM | XRP | UP | 24 sec | -0.007% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 8:44:19 AM | ZEC | DOWN | 40 sec | +0.108% | 0¢ | ❌ Lost | $0.00 |
| 10/4 8:44:19 AM | BNB | UP | 40 sec | -0.085% | 0¢ | ❌ Lost | -$0.15 |
| 10/4 8:44:04 AM | SOL | UP | 55 sec | -0.056% | 1¢ | ❌ Lost | $0.00 |
| 10/4 8:44:04 AM | ETH | UP | 55 sec | -0.048% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 8:43:44 AM | DOGE | DOWN | 75 sec | +0.156% | 0¢ | ❌ Lost | -$0.15 |
| 10/4 8:43:28 AM | NEAR | DOWN | 1.5 min | +0.246% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
