# 15-Minute 1¢ Study

*Updated Sun Oct 11, 12:21 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 1049 finished bets | 1% | $24.95 | +22% | +2.38¢ | -$0.40 / $25.35 |

*Expect about **81 buys a day** (~$12.12/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 1008 | $2.50 | +2% |
| 5+ min left, hold to the close | 398 | -$2.80 | -5% |
| Volatility model ≥ 5%, sell at 50¢ | 1049 | -$19.55 | -17% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 14288 | 14281 | 56 (0%) | 1.07% | -$942.50 (-55%) | Hold to the close: -$942.50 (-55%) |

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
| Volatility model | 9436 | 4.3% | 0.4% (39) | -638% | ❌ Worse |
| Momentum model | 9436 | 4.3% | 0.4% (39) | -667% | ❌ Worse |
| Mean-reversion model | 9436 | 7.0% | 0.4% (39) | -743% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 9436 | 39 | -48% | -88% | -88% | -86% |
| Volatility model ≥ 2% | 1851 | 14 | -13% | -76% | -76% | -73% |
| Volatility model ≥ 5% | 1049 | 10 | +22% | -70% | -69% | -66% |
| Volatility model ≥ 10% | 655 | 8 | +74% | -58% | -58% | -53% |
| Momentum model ≥ 2% | 1629 | 11 | -19% | -78% | -79% | -77% |
| Momentum model ≥ 5% | 1008 | 8 | +2% | -73% | -74% | -71% |
| Momentum model ≥ 10% | 697 | 6 | +21% | -65% | -66% | -62% |
| Mean-reversion model ≥ 2% | 3283 | 23 | -24% | -85% | -85% | -81% |
| Mean-reversion model ≥ 5% | 2232 | 17 | -16% | -82% | -82% | -77% |
| Mean-reversion model ≥ 10% | 1486 | 13 | +1% | -81% | -81% | -77% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 9634 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 3444 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 1203 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 14281 | 3% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 56 | 0% | -$942.50 | -55% | — |
| Sell at 2¢ | 484 | 3% | -$1,558.66 | -90% | 33 sec |
| Sell at 3¢ | 320 | 2% | -$1,559.70 | -90% | 47 sec |
| Sell at 5¢ | 234 | 2% | -$1,532.40 | -89% | 50 sec |
| Sell at 10¢ | 153 | 1% | -$1,456.07 | -84% | 64 sec |
| Sell at 25¢ | 87 | 1% | -$1,340.53 | -78% | 81 sec |
| Sell at 50¢ | 57 | 0% | -$1,201.75 | -70% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 394 | 4 | 11% | 3% | -4% | -81% | -86% |
| 2–5 min | 4615 | 28 | 6% | 3% | -41% | -89% | -89% |
| 1–2 min | 3748 | 15 | 3% | 2% | -56% | -94% | -94% |
| Under 1 min | 5520 | 9 | 1% | 0% | -76% | -90% | -90% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 1078 | 6 | 4% | 3% | -32% | -90% | -90% |
| HYPE | 1078 | 3 | 4% | 2% | -66% | -90% | -89% |
| DOGE | 1076 | 2 | 4% | 2% | -76% | -91% | -91% |
| BNB | 1074 | 5 | 4% | 2% | -44% | -91% | -92% |
| ETH | 1069 | 8 | 5% | 3% | -8% | -89% | -89% |
| SOL | 1068 | 1 | 3% | 1% | -88% | -94% | -93% |
| BTC | 1065 | 4 | 5% | 2% | -50% | -88% | -91% |
| NEAR | 1064 | 6 | 5% | 2% | -27% | -75% | -76% |
| XRP | 1062 | 6 | 2% | 1% | -30% | -84% | -84% |
| GOLD | 568 | 0 | 4% | 1% | -100% | -92% | -94% |
| SILVER | 555 | 1 | 3% | 1% | -79% | -94% | -94% |
| WTI | 529 | 3 | 3% | 1% | -35% | -94% | -96% |
| COPPER | 490 | 0 | 1% | 0% | -100% | -99% | -99% |
| PLATINUM | 451 | 0 | 0% | 0% | -100% | -100% | -99% |
| NATGAS | 431 | 3 | 3% | 2% | -35% | -95% | -93% |
| PALLADIUM | 420 | 1 | 1% | 0% | -78% | -98% | -99% |
| EURUSD | 412 | 3 | 3% | 2% | -32% | -72% | -71% |
| GBPUSD | 389 | 1 | 3% | 2% | -76% | -96% | -95% |
| USDJPY | 353 | 3 | 1% | 1% | -21% | -98% | -97% |
| AUDUSD | 25 | 0 | 0% | 0% | -100% | -100% | -100% |
| USDCAD | 24 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 7195 | 29 | 3% | 2% | -53% | -89% | -89% |
| DOWN (bought NO) | 7086 | 27 | 3% | 1% | -56% | -91% | -92% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 1694 | 9 | 2% | 1% | -12% | -74% | -74% |
| 0.05–0.1% | 1713 | 5 | 3% | 1% | -58% | -92% | -92% |
| 0.1–0.2% | 2467 | 8 | 4% | 2% | -60% | -91% | -92% |
| 0.2–0.5% | 2676 | 14 | 5% | 3% | -43% | -89% | -88% |
| Over 0.5% | 1081 | 5 | 6% | 2% | -52% | -88% | -90% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 3533 | 19 | 4% | 2% | -38% | -85% | -86% |
| Morning (6am–12pm) | 3425 | 18 | 4% | 2% | -40% | -91% | -91% |
| Afternoon (12–6pm) | 3332 | 9 | 3% | 1% | -68% | -90% | -90% |
| Evening (6pm–12am) | 3991 | 10 | 3% | 1% | -71% | -94% | -94% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 25 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,399 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/11 12:14:35 AM | ZEC | DOWN | 25 sec | +0.040% | 0¢ | ❌ Lost | $0.00 |
| 10/11 12:14:35 AM | XRP | DOWN | 25 sec | +0.014% | 0¢ | ❌ Lost | -$0.15 |
| 10/11 12:14:19 AM | SOL | DOWN | 41 sec | +0.040% | 1¢ | ❌ Lost | -$0.15 |
| 10/11 12:14:19 AM | NEAR | DOWN | 41 sec | +0.096% | 0¢ | ❌ Lost | $0.00 |
| 10/11 12:14:04 AM | ETH | UP | 55 sec | -0.028% | 0¢ | ❌ Lost | -$0.15 |
| 10/11 12:14:04 AM | DOGE | UP | 55 sec | -0.056% | 13¢ | ❌ Lost | -$0.15 |
| 10/11 12:13:18 AM | HYPE | UP | 1.7 min | -0.102% | 1¢ | ❌ Lost | -$0.15 |
| 10/11 12:13:18 AM | BNB | UP | 1.7 min | -0.084% | 1¢ | ❌ Lost | -$0.15 |
| 10/10 11:59:22 PM | HYPE | UP | 37 sec | -0.130% | 0¢ | ❌ Lost | -$0.15 |
| 10/10 11:59:22 PM | ZEC | UP | 37 sec | -0.144% | 0¢ | ❌ Lost | $0.00 |
| 10/10 11:59:06 PM | XRP | UP | 54 sec | -0.093% | 0¢ | ❌ Lost | $0.00 |
| 10/10 11:59:06 PM | NEAR | UP | 54 sec | -0.269% | 0¢ | ❌ Lost | $0.00 |
| 10/10 11:58:51 PM | ETH | UP | 68 sec | -0.045% | 1¢ | ❌ Lost | -$0.15 |
| 10/10 11:58:51 PM | BNB | UP | 68 sec | -0.082% | 0¢ | ❌ Lost | $0.00 |
| 10/10 11:58:35 PM | DOGE | UP | 84 sec | -0.110% | 1¢ | ❌ Lost | -$0.15 |
| 10/10 11:58:19 PM | BTC | UP | 1.7 min | -0.029% | 1¢ | ❌ Lost | -$0.15 |
| 10/10 11:57:34 PM | SOL | UP | 2.4 min | -0.145% | 0¢ | ❌ Lost | -$0.15 |
| 10/10 11:44:26 PM | BTC | DOWN | 34 sec | +0.014% | 1¢ | ❌ Lost | -$0.15 |
| 10/10 11:44:10 PM | XRP | UP | 50 sec | -0.100% | 0¢ | ❌ Lost | $0.00 |
| 10/10 11:44:10 PM | DOGE | UP | 50 sec | -0.071% | 0¢ | ❌ Lost | -$0.15 |
| 10/10 11:43:40 PM | NEAR | UP | 80 sec | -0.330% | 1¢ | ❌ Lost | -$0.15 |
| 10/10 11:43:09 PM | BNB | UP | 1.8 min | -0.082% | 0¢ | ❌ Lost | -$0.15 |
| 10/10 11:42:53 PM | SOL | UP | 2.1 min | -0.155% | 1¢ | ❌ Lost | -$0.15 |
| 10/10 11:42:53 PM | HYPE | UP | 2.1 min | -0.150% | 1¢ | ❌ Lost | -$0.15 |
| 10/10 11:42:11 PM | ETH | UP | 2.8 min | -0.058% | 2¢ | ❌ Lost | -$0.15 |
| 10/10 11:41:06 PM | ZEC | UP | 3.9 min | -0.347% | 0¢ | ❌ Lost | $0.00 |
| 10/10 11:29:52 PM | NEAR | DOWN | 7 sec | -0.143% | 0¢ | ❌ Lost | -$0.15 |
| 10/10 11:29:33 PM | BNB | UP | 26 sec | -0.061% | 0¢ | ❌ Lost | $0.00 |
| 10/10 11:29:33 PM | DOGE | UP | 26 sec | -0.083% | 0¢ | ❌ Lost | $0.00 |
| 10/10 11:29:17 PM | XRP | DOWN | 42 sec | +0.014% | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
