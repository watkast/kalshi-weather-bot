# 15-Minute 1¢ Study

*Updated Mon Oct 12, 2:16 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 1176 finished bets | 1% | $40.50 | +32% | +3.44¢ | $34.85 / $5.65 |

*Expect about **84 buys a day** (~$12.54/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 1128 | $19.55 | +16% |
| 5+ min left, hold to the close | 421 | -$6.25 | -10% |
| Volatility model ≥ 2%, hold to the close | 2065 | -$9.80 | -4% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 15397 | 15390 | 62 (0%) | 1.07% | -$987.95 (-53%) | Hold to the close: -$987.95 (-53%) |

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
| Volatility model | 10266 | 4.5% | 0.4% (45) | -661% | ❌ Worse |
| Momentum model | 10266 | 4.5% | 0.4% (45) | -688% | ❌ Worse |
| Mean-reversion model | 10266 | 7.2% | 0.4% (45) | -765% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 10266 | 45 | -45% | -88% | -88% | -86% |
| Volatility model ≥ 2% | 2065 | 17 | -4% | -77% | -77% | -74% |
| Volatility model ≥ 5% | 1176 | 12 | +32% | -71% | -70% | -68% |
| Volatility model ≥ 10% | 744 | 8 | +56% | -62% | -61% | -58% |
| Momentum model ≥ 2% | 1818 | 14 | -6% | -79% | -80% | -77% |
| Momentum model ≥ 5% | 1128 | 10 | +16% | -75% | -75% | -72% |
| Momentum model ≥ 10% | 781 | 7 | +28% | -68% | -68% | -64% |
| Mean-reversion model ≥ 2% | 3601 | 26 | -21% | -85% | -85% | -81% |
| Mean-reversion model ≥ 5% | 2456 | 20 | -9% | -82% | -82% | -78% |
| Mean-reversion model ≥ 10% | 1644 | 14 | -1% | -81% | -81% | -77% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 10464 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 3636 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 1290 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 15390 | 3% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 62 | 0% | -$987.95 | -53% | — |
| Sell at 2¢ | 528 | 3% | -$1,676.67 | -90% | 33 sec |
| Sell at 3¢ | 350 | 2% | -$1,677.45 | -90% | 47 sec |
| Sell at 5¢ | 258 | 2% | -$1,646.25 | -89% | 50 sec |
| Sell at 10¢ | 170 | 1% | -$1,563.25 | -84% | 64 sec |
| Sell at 25¢ | 96 | 1% | -$1,440.19 | -78% | 80 sec |
| Sell at 50¢ | 64 | 0% | -$1,283.95 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 417 | 4 | 11% | 3% | -9% | -81% | -86% |
| 2–5 min | 4960 | 32 | 6% | 3% | -37% | -88% | -89% |
| 1–2 min | 4063 | 16 | 3% | 2% | -57% | -94% | -94% |
| Under 1 min | 5946 | 10 | 1% | 0% | -75% | -91% | -90% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 1175 | 7 | 4% | 3% | -27% | -90% | -90% |
| HYPE | 1173 | 4 | 4% | 2% | -58% | -90% | -89% |
| DOGE | 1166 | 2 | 4% | 2% | -78% | -91% | -90% |
| BNB | 1164 | 5 | 4% | 2% | -48% | -91% | -92% |
| ETH | 1162 | 8 | 5% | 2% | -16% | -89% | -89% |
| SOL | 1162 | 2 | 3% | 1% | -78% | -93% | -92% |
| BTC | 1158 | 5 | 5% | 2% | -42% | -88% | -91% |
| NEAR | 1152 | 7 | 5% | 3% | -20% | -76% | -76% |
| XRP | 1152 | 7 | 2% | 1% | -24% | -84% | -84% |
| GOLD | 596 | 0 | 4% | 1% | -100% | -92% | -94% |
| SILVER | 583 | 1 | 3% | 1% | -80% | -94% | -94% |
| WTI | 559 | 3 | 3% | 1% | -39% | -94% | -96% |
| COPPER | 520 | 0 | 1% | 1% | -100% | -98% | -98% |
| PLATINUM | 482 | 0 | 0% | 0% | -100% | -100% | -99% |
| NATGAS | 450 | 3 | 3% | 2% | -38% | -95% | -94% |
| PALLADIUM | 446 | 1 | 1% | 0% | -79% | -98% | -98% |
| EURUSD | 434 | 3 | 3% | 2% | -35% | -74% | -73% |
| GBPUSD | 415 | 1 | 2% | 1% | -78% | -96% | -96% |
| USDJPY | 375 | 3 | 1% | 1% | -25% | -98% | -97% |
| USDCAD | 34 | 0 | 0% | 0% | -100% | -100% | -100% |
| AUDUSD | 32 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 7720 | 34 | 3% | 2% | -49% | -90% | -89% |
| DOWN (bought NO) | 7670 | 28 | 3% | 2% | -58% | -91% | -92% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 1895 | 9 | 2% | 1% | -20% | -76% | -76% |
| 0.05–0.1% | 1861 | 6 | 3% | 1% | -54% | -92% | -92% |
| 0.1–0.2% | 2683 | 9 | 4% | 2% | -59% | -91% | -92% |
| 0.2–0.5% | 2884 | 18 | 6% | 3% | -31% | -89% | -88% |
| Over 0.5% | 1138 | 5 | 6% | 2% | -55% | -88% | -90% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 3841 | 20 | 4% | 2% | -40% | -86% | -86% |
| Morning (6am–12pm) | 3615 | 20 | 4% | 2% | -36% | -91% | -90% |
| Afternoon (12–6pm) | 3575 | 9 | 3% | 1% | -70% | -90% | -91% |
| Evening (6pm–12am) | 4359 | 13 | 3% | 2% | -66% | -94% | -94% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 25 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,537 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/12 2:13:51 AM | GOLD | UP | 69 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/12 2:13:34 AM | SILVER | UP | 86 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/12 2:13:18 AM | GBPUSD | UP | 1.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/12 2:12:47 AM | XRP | UP | 2.2 min | -0.205% | 1¢ | ❌ Lost | -$0.15 |
| 10/12 2:12:15 AM | COPPER | UP | 2.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/12 2:12:15 AM | SOL | UP | 2.8 min | -0.227% | 0¢ | ❌ Lost | -$0.15 |
| 10/12 2:11:59 AM | PALLADIUM | UP | 3.0 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/12 2:11:44 AM | BNB | UP | 3.2 min | -0.183% | 1¢ | ❌ Lost | -$0.15 |
| 10/12 2:11:29 AM | ETH | UP | 3.5 min | -0.187% | 1¢ | ❌ Lost | -$0.15 |
| 10/12 2:11:29 AM | EURUSD | UP | 3.5 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/12 2:11:13 AM | ZEC | UP | 3.8 min | -0.619% | 1¢ | ❌ Lost | -$0.15 |
| 10/12 2:11:13 AM | PLATINUM | UP | 3.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/12 2:10:57 AM | WTI | DOWN | 4.0 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/12 2:10:41 AM | BTC | UP | 4.3 min | -0.222% | 1¢ | ❌ Lost | -$0.15 |
| 10/12 2:10:26 AM | DOGE | UP | 4.5 min | -0.232% | 2¢ | ❌ Lost | -$0.15 |
| 10/12 2:10:10 AM | NEAR | UP | 4.8 min | -0.945% | 1¢ | ❌ Lost | -$0.15 |
| 10/12 2:09:38 AM | HYPE | UP | 5.4 min | -0.390% | 1¢ | ❌ Lost | -$0.15 |
| 10/12 1:59:53 AM | XRP | UP | 7 sec | -0.071% | 0¢ | ❌ Lost | $0.00 |
| 10/12 1:59:53 AM | WTI | DOWN | 7 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/12 1:59:38 AM | DOGE | DOWN | 22 sec | +0.022% | 0¢ | ❌ Lost | $0.00 |
| 10/12 1:59:38 AM | BTC | DOWN | 22 sec | +0.012% | 1¢ | ❌ Lost | -$0.15 |
| 10/12 1:59:22 AM | BNB | UP | 38 sec | -0.095% | 0¢ | ❌ Lost | -$0.15 |
| 10/12 1:58:50 AM | SOL | UP | 70 sec | -0.086% | 1¢ | ❌ Lost | -$0.15 |
| 10/12 1:58:50 AM | HYPE | DOWN | 70 sec | +0.017% | 1¢ | ❌ Lost | -$0.15 |
| 10/12 1:58:35 AM | ETH | UP | 85 sec | -0.114% | 1¢ | ❌ Lost | -$0.15 |
| 10/12 1:58:35 AM | NEAR | UP | 85 sec | -0.411% | 1¢ | ❌ Lost | -$0.15 |
| 10/12 1:58:03 AM | GBPUSD | DOWN | 1.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/12 1:57:32 AM | PLATINUM | UP | 2.5 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/12 1:57:32 AM | PALLADIUM | UP | 2.5 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/12 1:57:00 AM | COPPER | UP | 3.0 min | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
