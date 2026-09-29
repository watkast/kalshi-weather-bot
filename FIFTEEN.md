# 15-Minute 1¢ Study

*Updated Tue Sep 29, 12:08 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (5+ min left).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| 5+ min left, hold to the close | 52 finished bets | 4% | $20.20 | +259% | +38.85¢ | $24.10 / -$3.90 |

*Expect about **45 buys a day** (~$6.81/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Mean-reversion model ≥ 5%, hold to the close | 194 | $16.65 | +66% |
| 5+ min left, sell at 50¢ | 52 | $5.70 | +73% |
| Mean-reversion model ≥ 2%, hold to the close | 296 | $3.90 | +10% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 1571 | 1565 | 8 (1%) | 1.07% | -$76.25 (-41%) | Hold to the close: -$76.25 (-41%) |

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
| Volatility model | 792 | 2.8% | 0.5% (4) | -327% | ❌ Worse |
| Momentum model | 792 | 3.0% | 0.5% (4) | -403% | ❌ Worse |
| Mean-reversion model | 792 | 5.7% | 0.5% (4) | -383% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 792 | 4 | -35% | -89% | -90% | -85% |
| Volatility model ≥ 2% | 153 | 1 | -24% | -84% | -85% | -79% |
| Volatility model ≥ 5% | 69 | 0 | -100% | -72% | -69% | -57% |
| Volatility model ≥ 10% | 36 | 0 | -100% | -70% | -66% | -43% |
| Momentum model ≥ 2% | 128 | 0 | -100% | -84% | -89% | -87% |
| Momentum model ≥ 5% | 76 | 0 | -100% | -81% | -91% | -85% |
| Momentum model ≥ 10% | 51 | 0 | -100% | -89% | -84% | -74% |
| Mean-reversion model ≥ 2% | 296 | 3 | +10% | -85% | -85% | -78% |
| Mean-reversion model ≥ 5% | 194 | 3 | +66% | -83% | -82% | -72% |
| Mean-reversion model ≥ 10% | 122 | 2 | +83% | -78% | -77% | -66% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 987 | 4% | 3% | 2% | 2% | 1% | 1% |
| Commodities | 485 | 1% | 1% | 0% | 0% | 0% | 0% |
| Financials | 93 | 3% | 3% | 2% | 2% | 2% | 2% |
| **All** | 1565 | 3% | 2% | 2% | 1% | 1% | 1% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 8 | 1% | -$76.25 | -41% | — |
| Sell at 2¢ | 53 | 3% | -$174.47 | -93% | 47 sec |
| Sell at 3¢ | 34 | 2% | -$174.99 | -93% | 47 sec |
| Sell at 5¢ | 25 | 2% | -$172.00 | -91% | 81 sec |
| Sell at 10¢ | 23 | 1% | -$158.12 | -84% | 1.9 min |
| Sell at 25¢ | 13 | 1% | -$145.22 | -77% | 2.1 min |
| Sell at 50¢ | 9 | 1% | -$127.50 | -68% | 2.4 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| 5–10 min | 52 | 2 | 6% | 4% | +259% | -90% | -85% |
| 2–5 min | 525 | 5 | 7% | 3% | -8% | -88% | -89% |
| 1–2 min | 442 | 1 | 2% | 1% | -75% | -95% | -96% |
| Under 1 min | 546 | 0 | 1% | 0% | -100% | -98% | -98% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ETH | 113 | 2 | 5% | 4% | +120% | -88% | -85% |
| ZEC | 112 | 1 | 6% | 2% | +10% | -86% | -94% |
| DOGE | 111 | 1 | 5% | 3% | +10% | -90% | -85% |
| NEAR | 110 | 0 | 5% | 2% | -100% | -88% | -93% |
| BTC | 110 | 0 | 8% | 3% | -100% | -79% | -86% |
| XRP | 110 | 2 | 4% | 3% | +133% | -91% | -90% |
| SOL | 109 | 0 | 3% | 2% | -100% | -92% | -89% |
| BNB | 107 | 0 | 2% | 1% | -100% | -96% | -94% |
| HYPE | 105 | 0 | 3% | 2% | -100% | -94% | -94% |
| GOLD | 85 | 0 | 2% | 0% | -100% | -95% | -100% |
| WTI | 77 | 0 | 1% | 0% | -100% | -97% | -100% |
| SILVER | 76 | 0 | 1% | 0% | -100% | -97% | -96% |
| COPPER | 67 | 0 | 0% | 0% | -100% | -100% | -100% |
| NATGAS | 67 | 0 | 3% | 1% | -100% | -95% | -92% |
| PLATINUM | 65 | 0 | 0% | 0% | -100% | -100% | -100% |
| PALLADIUM | 48 | 0 | 0% | 0% | -100% | -100% | -100% |
| GBPUSD | 35 | 0 | 3% | 0% | -100% | -95% | -93% |
| EURUSD | 30 | 0 | 0% | 0% | -100% | -100% | -100% |
| USDJPY | 28 | 2 | 7% | 7% | +567% | -88% | -81% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 840 | 5 | 4% | 2% | -30% | -91% | -91% |
| DOWN (bought NO) | 725 | 3 | 3% | 1% | -52% | -94% | -95% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 98 | 0 | 3% | 2% | -100% | -88% | -88% |
| 0.05–0.1% | 111 | 0 | 1% | 0% | -100% | -97% | -100% |
| 0.1–0.2% | 224 | 0 | 4% | 1% | -100% | -91% | -89% |
| 0.2–0.5% | 377 | 2 | 5% | 3% | -41% | -90% | -91% |
| Over 0.5% | 177 | 4 | 7% | 4% | +139% | -86% | -85% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 308 | 1 | 4% | 2% | -62% | -91% | -93% |
| Morning (6am–12pm) | 338 | 4 | 3% | 1% | +36% | -94% | -94% |
| Afternoon (12–6pm) | 330 | 1 | 2% | 1% | -65% | -95% | -96% |
| Evening (6pm–12am) | 589 | 2 | 4% | 2% | -60% | -92% | -91% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 23 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 3,971 |
| Time from buy to best bounce (bounced bets) | 47 sec |
| Price snapshots per bet | 45 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 9/28 11:59:49 PM | PLATINUM | UP | 11 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/28 11:59:17 PM | SILVER | UP | 43 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 9/28 11:59:17 PM | NEAR | DOWN | 43 sec | +0.145% | 0¢ | ❌ Lost | -$0.15 |
| 9/28 11:59:17 PM | ZEC | DOWN | 43 sec | +0.163% | 0¢ | ❌ Lost | $0.00 |
| 9/28 11:59:02 PM | SOL | DOWN | 57 sec | +0.211% | 0¢ | ❌ Lost | $0.00 |
| 9/28 11:58:30 PM | XRP | DOWN | 89 sec | +0.262% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 11:57:58 PM | BTC | DOWN | 2.0 min | +0.143% | 2¢ | ❌ Lost | -$0.15 |
| 9/28 11:57:26 PM | DOGE | DOWN | 2.5 min | +0.440% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 11:56:54 PM | ETH | DOWN | 3.1 min | +0.238% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 11:56:54 PM | WTI | UP | 3.1 min | — | 1¢ | ❌ Lost | -$0.15 |
| 9/28 11:56:54 PM | BNB | DOWN | 3.1 min | +0.164% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 11:56:54 PM | COPPER | DOWN | 3.1 min | — | 1¢ | ❌ Lost | -$0.15 |
| 9/28 11:56:37 PM | HYPE | DOWN | 3.4 min | +0.445% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 11:44:56 PM | XRP | UP | 4 sec | -0.094% | 0¢ | ❌ Lost | $0.00 |
| 9/28 11:44:56 PM | GBPUSD | UP | 4 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/28 11:44:56 PM | BTC | UP | 4 sec | -0.019% | 0¢ | ❌ Lost | $0.00 |
| 9/28 11:44:40 PM | BNB | UP | 20 sec | -0.042% | 0¢ | ❌ Lost | -$0.15 |
| 9/28 11:44:40 PM | SOL | UP | 20 sec | -0.140% | 0¢ | ❌ Lost | $0.00 |
| 9/28 11:43:51 PM | PALLADIUM | DOWN | 68 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/28 11:43:51 PM | GOLD | DOWN | 68 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 9/28 11:43:19 PM | COPPER | DOWN | 1.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 9/28 11:43:05 PM | SILVER | DOWN | 1.9 min | — | 1¢ | ❌ Lost | -$0.15 |
| 9/28 11:42:17 PM | ZEC | UP | 2.7 min | -0.524% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 11:42:17 PM | DOGE | UP | 2.7 min | -0.427% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 11:41:12 PM | ETH | UP | 3.8 min | -0.380% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 11:40:22 PM | NEAR | UP | 4.6 min | -1.019% | 56¢ | ❌ Lost | -$0.15 |
| 9/28 11:39:03 PM | HYPE | UP | 5.9 min | -0.802% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 10:59:56 PM | SILVER | UP | 3 sec | — | 0¢ | ❌ Lost | $0.00 |
| 9/28 10:59:56 PM | COPPER | UP | 3 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/28 10:59:40 PM | WTI | DOWN | 20 sec | — | 0¢ | ❌ Lost | $0.00 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
