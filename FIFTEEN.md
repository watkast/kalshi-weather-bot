# 15-Minute 1¢ Study

*Updated Sun Oct 4, 11:52 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (5+ min left).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| 5+ min left, hold to the close | 187 finished bets | 2% | $14.40 | +52% | +7.70¢ | $14.20 / $0.20 |

*Expect about **28 buys a day** (~$4.23/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 536 | $11.80 | +20% |
| Volatility model ≥ 2%, hold to the close | 1003 | $4.35 | +4% |
| Mean-reversion model ≥ 5%, hold to the close | 1190 | $3.40 | +2% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 7508 | 7502 | 34 (0%) | 1.07% | -$424.75 (-47%) | Hold to the close: -$424.75 (-47%) |

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
| Volatility model | 4966 | 4.2% | 0.4% (22) | -627% | ❌ Worse |
| Momentum model | 4966 | 4.3% | 0.4% (22) | -660% | ❌ Worse |
| Mean-reversion model | 4966 | 7.0% | 0.4% (22) | -726% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 4966 | 22 | -44% | -84% | -84% | -82% |
| Volatility model ≥ 2% | 1003 | 9 | +4% | -68% | -68% | -63% |
| Volatility model ≥ 5% | 536 | 5 | +20% | -54% | -53% | -48% |
| Volatility model ≥ 10% | 333 | 4 | +75% | -33% | -34% | -28% |
| Momentum model ≥ 2% | 883 | 6 | -18% | -69% | -71% | -68% |
| Momentum model ≥ 5% | 542 | 4 | -4% | -60% | -63% | -59% |
| Momentum model ≥ 10% | 372 | 3 | +14% | -46% | -48% | -44% |
| Mean-reversion model ≥ 2% | 1767 | 12 | -26% | -82% | -83% | -78% |
| Mean-reversion model ≥ 5% | 1190 | 11 | +2% | -78% | -79% | -71% |
| Mean-reversion model ≥ 10% | 782 | 8 | +18% | -76% | -77% | -69% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 5163 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 1784 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 555 | 4% | 3% | 2% | 2% | 1% | 1% |
| **All** | 7502 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 34 | 0% | -$424.75 | -47% | — |
| Sell at 2¢ | 306 | 4% | -$793.19 | -88% | 34 sec |
| Sell at 3¢ | 197 | 3% | -$795.92 | -88% | 48 sec |
| Sell at 5¢ | 145 | 2% | -$778.50 | -86% | 61 sec |
| Sell at 10¢ | 99 | 1% | -$729.06 | -81% | 78 sec |
| Sell at 25¢ | 55 | 1% | -$662.70 | -74% | 1.6 min |
| Sell at 50¢ | 33 | 0% | -$580.00 | -64% | 1.9 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 3 | 0 | 100% | 67% | -100% | +73% | +160% |
| 5–10 min | 184 | 3 | 12% | 3% | +55% | -78% | -87% |
| 2–5 min | 2429 | 18 | 8% | 4% | -28% | -85% | -86% |
| 1–2 min | 1970 | 8 | 3% | 2% | -56% | -94% | -93% |
| Under 1 min | 2916 | 5 | 1% | 0% | -74% | -88% | -88% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 582 | 4 | 5% | 3% | -19% | -88% | -89% |
| DOGE | 578 | 2 | 4% | 2% | -55% | -90% | -91% |
| HYPE | 577 | 2 | 5% | 3% | -58% | -89% | -86% |
| ETH | 576 | 5 | 6% | 3% | +10% | -85% | -85% |
| BNB | 572 | 2 | 5% | 2% | -58% | -90% | -92% |
| BTC | 571 | 3 | 6% | 2% | -32% | -86% | -89% |
| SOL | 571 | 0 | 3% | 1% | -100% | -92% | -91% |
| XRP | 569 | 4 | 2% | 1% | -10% | -73% | -74% |
| NEAR | 567 | 2 | 6% | 3% | -53% | -61% | -63% |
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
| UP (bought YES) | 3775 | 19 | 4% | 2% | -41% | -88% | -87% |
| DOWN (bought NO) | 3727 | 15 | 4% | 2% | -54% | -88% | -89% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 861 | 7 | 2% | 1% | +36% | -55% | -54% |
| 0.05–0.1% | 882 | 2 | 3% | 1% | -66% | -91% | -93% |
| 0.1–0.2% | 1273 | 4 | 4% | 2% | -60% | -90% | -91% |
| 0.2–0.5% | 1501 | 7 | 6% | 4% | -48% | -87% | -86% |
| Over 0.5% | 644 | 4 | 7% | 3% | -36% | -86% | -88% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 1882 | 8 | 5% | 2% | -50% | -84% | -86% |
| Morning (6am–12pm) | 2049 | 17 | 5% | 3% | -5% | -89% | -87% |
| Afternoon (12–6pm) | 1513 | 3 | 3% | 1% | -76% | -85% | -87% |
| Evening (6pm–12am) | 2058 | 6 | 3% | 2% | -66% | -93% | -93% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 24 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,020 |
| Time from buy to best bounce (bounced bets) | 49 sec |
| Price snapshots per bet | 41 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/4 11:44:48 AM | BTC | DOWN | 11 sec | +0.056% | 0¢ | ❌ Lost | -$0.15 |
| 10/4 11:44:32 AM | HYPE | DOWN | 27 sec | +0.049% | 0¢ | ❌ Lost | -$0.15 |
| 10/4 11:44:16 AM | XRP | DOWN | 43 sec | +0.107% | 0¢ | ❌ Lost | $0.00 |
| 10/4 11:43:45 AM | ZEC | DOWN | 75 sec | +0.150% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 11:43:29 AM | NEAR | DOWN | 1.5 min | +0.369% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 11:43:13 AM | DOGE | DOWN | 1.8 min | +0.612% | 0¢ | ❌ Lost | -$0.15 |
| 10/4 11:42:57 AM | ETH | UP | 2.0 min | -0.036% | 98¢ | ✅ Won | $13.85 |
| 10/4 11:42:42 AM | BNB | UP | 2.3 min | -0.113% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 11:42:42 AM | BTC | UP | 2.3 min | -0.049% | 99¢ | ✅ Won | $13.85 |
| 10/4 11:42:10 AM | SOL | UP | 2.8 min | -0.183% | 0¢ | ❌ Lost | -$0.15 |
| 10/4 11:29:44 AM | HYPE | DOWN | 15 sec | +0.009% | 0¢ | ❌ Lost | $0.00 |
| 10/4 11:29:12 AM | NEAR | DOWN | 47 sec | +0.184% | 0¢ | ❌ Lost | -$0.15 |
| 10/4 11:28:56 AM | DOGE | DOWN | 63 sec | +0.198% | 0¢ | ❌ Lost | -$0.15 |
| 10/4 11:28:56 AM | XRP | UP | 63 sec | -0.106% | 0¢ | ❌ Lost | -$0.15 |
| 10/4 11:27:53 AM | BNB | DOWN | 2.1 min | +0.032% | 0¢ | ❌ Lost | -$0.15 |
| 10/4 11:27:53 AM | ETH | DOWN | 2.1 min | +0.068% | 4¢ | ❌ Lost | -$0.15 |
| 10/4 11:27:53 AM | SOL | DOWN | 2.1 min | +0.088% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 11:27:06 AM | ZEC | DOWN | 2.9 min | +0.361% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 11:27:06 AM | BTC | DOWN | 2.9 min | +0.092% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 11:14:17 AM | NEAR | UP | 43 sec | -0.564% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 11:14:01 AM | XRP | UP | 59 sec | -0.100% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 11:14:01 AM | ETH | UP | 59 sec | -0.035% | 0¢ | ❌ Lost | -$0.15 |
| 10/4 11:13:46 AM | SOL | UP | 74 sec | -0.087% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 11:13:30 AM | BNB | UP | 1.5 min | -0.090% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 11:13:14 AM | BTC | UP | 1.8 min | -0.058% | 1¢ | ❌ Lost | $0.00 |
| 10/4 11:12:43 AM | DOGE | DOWN | 2.3 min | +0.594% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 11:12:43 AM | HYPE | UP | 2.3 min | -0.175% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 11:12:27 AM | ZEC | UP | 2.5 min | -0.516% | 0¢ | ❌ Lost | -$0.15 |
| 10/4 10:59:48 AM | XRP | UP | 12 sec | -0.027% | 0¢ | ❌ Lost | $0.00 |
| 10/4 10:59:33 AM | BNB | UP | 27 sec | -0.086% | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
