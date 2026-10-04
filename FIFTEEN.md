# 15-Minute 1¢ Study

*Updated Sun Oct 4, 11:02 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (5+ min left).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| 5+ min left, hold to the close | 187 finished bets | 2% | $14.40 | +52% | +7.70¢ | $14.20 / $0.20 |

*Expect about **28 buys a day** (~$4.25/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 533 | -$1.75 | -3% |
| Momentum model ≥ 5%, hold to the close | 541 | -$2.05 | -4% |
| 5+ min left, sell at 50¢ | 187 | -$7.35 | -27% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 7480 | 7474 | 32 (0%) | 1.07% | -$449.00 (-50%) | Hold to the close: -$449.00 (-50%) |

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
| Volatility model | 4938 | 4.2% | 0.4% (20) | -671% | ❌ Worse |
| Momentum model | 4938 | 4.3% | 0.4% (20) | -705% | ❌ Worse |
| Mean-reversion model | 4938 | 7.0% | 0.4% (20) | -778% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 4938 | 20 | -49% | -84% | -84% | -82% |
| Volatility model ≥ 2% | 996 | 7 | -19% | -68% | -69% | -64% |
| Volatility model ≥ 5% | 533 | 4 | -3% | -54% | -53% | -49% |
| Volatility model ≥ 10% | 332 | 4 | +76% | -32% | -34% | -27% |
| Momentum model ≥ 2% | 877 | 5 | -31% | -69% | -71% | -68% |
| Momentum model ≥ 5% | 541 | 4 | -4% | -60% | -63% | -59% |
| Momentum model ≥ 10% | 371 | 3 | +15% | -46% | -48% | -44% |
| Mean-reversion model ≥ 2% | 1757 | 10 | -38% | -83% | -84% | -78% |
| Mean-reversion model ≥ 5% | 1183 | 9 | -16% | -78% | -79% | -72% |
| Mean-reversion model ≥ 10% | 778 | 7 | +4% | -76% | -77% | -70% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 5135 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 1784 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 555 | 4% | 3% | 2% | 2% | 1% | 1% |
| **All** | 7474 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 32 | 0% | -$449.00 | -50% | — |
| Sell at 2¢ | 303 | 4% | -$790.22 | -88% | 34 sec |
| Sell at 3¢ | 194 | 3% | -$793.34 | -88% | 48 sec |
| Sell at 5¢ | 143 | 2% | -$776.05 | -87% | 61 sec |
| Sell at 10¢ | 97 | 1% | -$727.93 | -81% | 78 sec |
| Sell at 25¢ | 53 | 1% | -$665.57 | -74% | 1.6 min |
| Sell at 50¢ | 31 | 0% | -$589.75 | -66% | 1.9 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 3 | 0 | 100% | 67% | -100% | +73% | +160% |
| 5–10 min | 184 | 3 | 12% | 3% | +55% | -78% | -87% |
| 2–5 min | 2417 | 16 | 8% | 4% | -35% | -86% | -86% |
| 1–2 min | 1962 | 8 | 3% | 2% | -56% | -94% | -93% |
| Under 1 min | 2908 | 5 | 1% | 0% | -74% | -88% | -88% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 579 | 4 | 5% | 3% | -18% | -88% | -89% |
| DOGE | 575 | 2 | 4% | 2% | -55% | -90% | -91% |
| HYPE | 574 | 2 | 5% | 3% | -58% | -89% | -86% |
| ETH | 573 | 4 | 6% | 3% | -12% | -86% | -86% |
| BNB | 569 | 2 | 5% | 2% | -58% | -90% | -92% |
| SOL | 568 | 0 | 3% | 1% | -100% | -92% | -91% |
| BTC | 567 | 2 | 6% | 2% | -54% | -86% | -90% |
| XRP | 566 | 4 | 2% | 1% | -9% | -73% | -74% |
| NEAR | 564 | 2 | 6% | 3% | -53% | -61% | -63% |
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
| UP (bought YES) | 3762 | 17 | 4% | 2% | -47% | -88% | -87% |
| DOWN (bought NO) | 3712 | 15 | 4% | 2% | -53% | -88% | -90% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 855 | 5 | 2% | 1% | -2% | -55% | -55% |
| 0.05–0.1% | 874 | 2 | 3% | 1% | -66% | -91% | -93% |
| 0.1–0.2% | 1265 | 4 | 4% | 2% | -60% | -90% | -91% |
| 0.2–0.5% | 1499 | 7 | 6% | 4% | -48% | -87% | -86% |
| Over 0.5% | 640 | 4 | 7% | 3% | -36% | -86% | -88% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 1882 | 8 | 5% | 2% | -50% | -84% | -86% |
| Morning (6am–12pm) | 2021 | 15 | 5% | 3% | -15% | -89% | -88% |
| Afternoon (12–6pm) | 1513 | 3 | 3% | 1% | -76% | -85% | -87% |
| Evening (6pm–12am) | 2058 | 6 | 3% | 2% | -66% | -93% | -93% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 24 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 3,996 |
| Time from buy to best bounce (bounced bets) | 49 sec |
| Price snapshots per bet | 41 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/4 10:59:48 AM | XRP | UP | 12 sec | -0.027% | 0¢ | ❌ Lost | $0.00 |
| 10/4 10:59:33 AM | BNB | UP | 27 sec | -0.086% | 0¢ | ❌ Lost | -$0.15 |
| 10/4 10:59:33 AM | ETH | UP | 27 sec | -0.036% | 0¢ | ❌ Lost | $0.00 |
| 10/4 10:58:45 AM | BTC | DOWN | 75 sec | +0.039% | 0¢ | ❌ Lost | -$0.15 |
| 10/4 10:57:56 AM | NEAR | DOWN | 2.1 min | +1.035% | 0¢ | ❌ Lost | -$0.15 |
| 10/4 10:57:41 AM | DOGE | DOWN | 2.3 min | +0.219% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 10:57:41 AM | HYPE | DOWN | 2.3 min | +0.095% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 10:56:53 AM | ZEC | DOWN | 3.1 min | +0.332% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 10:56:53 AM | SOL | DOWN | 3.1 min | +0.115% | 2¢ | ❌ Lost | -$0.15 |
| 10/4 10:44:19 AM | BNB | DOWN | 41 sec | +0.028% | 0¢ | ❌ Lost | $0.00 |
| 10/4 10:43:01 AM | DOGE | DOWN | 2.0 min | +0.152% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 10:43:01 AM | XRP | DOWN | 2.0 min | +0.147% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 10:42:12 AM | NEAR | DOWN | 2.8 min | +0.696% | 1¢ | ❌ Lost | $0.00 |
| 10/4 10:42:12 AM | BTC | DOWN | 2.8 min | +0.116% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 10:42:12 AM | SOL | DOWN | 2.8 min | +0.155% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 10:41:26 AM | HYPE | DOWN | 3.6 min | +0.242% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 10:40:23 AM | ZEC | DOWN | 4.6 min | +0.447% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 10:39:34 AM | ETH | DOWN | 5.4 min | +0.170% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 10:29:34 AM | NEAR | UP | 25 sec | -0.216% | 0¢ | ❌ Lost | $0.00 |
| 10/4 10:29:18 AM | DOGE | UP | 41 sec | -0.102% | 0¢ | ❌ Lost | -$0.15 |
| 10/4 10:29:02 AM | BNB | DOWN | 58 sec | +0.005% | 0¢ | ❌ Lost | -$0.15 |
| 10/4 10:29:02 AM | SOL | UP | 58 sec | -0.082% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 10:27:59 AM | BTC | UP | 2.0 min | -0.063% | 3¢ | ❌ Lost | -$0.15 |
| 10/4 10:27:59 AM | ETH | UP | 2.0 min | -0.080% | 3¢ | ❌ Lost | -$0.15 |
| 10/4 10:27:44 AM | XRP | UP | 2.3 min | -0.193% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 10:27:12 AM | HYPE | UP | 2.8 min | -0.244% | 0¢ | ❌ Lost | -$0.15 |
| 10/4 10:27:12 AM | ZEC | DOWN | 2.8 min | +0.388% | 0¢ | ❌ Lost | -$0.15 |
| 10/4 10:14:36 AM | ZEC | UP | 24 sec | -0.108% | 0¢ | ❌ Lost | $0.00 |
| 10/4 10:14:20 AM | SOL | DOWN | 40 sec | +0.035% | 13¢ | ❌ Lost | -$0.15 |
| 10/4 10:13:51 AM | HYPE | UP | 68 sec | -0.147% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
