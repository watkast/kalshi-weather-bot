# 15-Minute 1¢ Study

*Updated Sun Oct 18, 1:32 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 1868 finished bets | 1% | $86.40 | +42% | +4.63¢ | $38.15 / $48.25 |

*Expect about **93 buys a day** (~$13.99/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 1714 | $51.10 | +27% |
| Momentum model ≥ 2%, hold to the close | 2871 | -$12.05 | -4% |
| Volatility model ≥ 5%, sell at 50¢ | 1868 | -$30.60 | -15% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 22481 | 22474 | 85 (0%) | 1.07% | -$1,538.95 (-56%) | Hold to the close: -$1,538.95 (-56%) |

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
| Volatility model | 14750 | 4.6% | 0.4% (59) | -662% | ❌ Worse |
| Momentum model | 14750 | 4.5% | 0.4% (59) | -685% | ❌ Worse |
| Mean-reversion model | 14750 | 7.6% | 0.4% (59) | -794% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 14750 | 59 | -50% | -88% | -88% | -85% |
| Volatility model ≥ 2% | 3379 | 27 | -8% | -79% | -79% | -75% |
| Volatility model ≥ 5% | 1868 | 21 | +42% | -75% | -74% | -71% |
| Volatility model ≥ 10% | 1100 | 13 | +67% | -69% | -68% | -65% |
| Momentum model ≥ 2% | 2871 | 23 | -4% | -81% | -82% | -78% |
| Momentum model ≥ 5% | 1714 | 17 | +27% | -79% | -79% | -75% |
| Momentum model ≥ 10% | 1142 | 12 | +47% | -74% | -74% | -69% |
| Mean-reversion model ≥ 2% | 5673 | 38 | -27% | -84% | -84% | -81% |
| Mean-reversion model ≥ 5% | 3934 | 30 | -16% | -83% | -82% | -79% |
| Mean-reversion model ≥ 10% | 2604 | 19 | -16% | -81% | -81% | -78% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 14948 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 5309 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 2217 | 1% | 1% | 1% | 1% | 0% | 0% |
| **All** | 22474 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 85 | 0% | -$1,538.95 | -56% | — |
| Sell at 2¢ | 817 | 4% | -$2,418.53 | -89% | 43 sec |
| Sell at 3¢ | 551 | 2% | -$2,416.06 | -89% | 47 sec |
| Sell at 5¢ | 398 | 2% | -$2,372.25 | -87% | 50 sec |
| Sell at 10¢ | 241 | 1% | -$2,287.24 | -84% | 64 sec |
| Sell at 25¢ | 134 | 1% | -$2,117.41 | -78% | 79 sec |
| Sell at 50¢ | 88 | 0% | -$1,896.95 | -70% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 799 | 5 | 11% | 4% | -41% | -81% | -84% |
| 2–5 min | 7309 | 38 | 7% | 3% | -49% | -88% | -87% |
| 1–2 min | 5800 | 23 | 3% | 2% | -57% | -92% | -92% |
| Under 1 min | 8562 | 19 | 1% | 0% | -68% | -88% | -88% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 1680 | 11 | 4% | 2% | -18% | -90% | -90% |
| HYPE | 1671 | 6 | 5% | 3% | -56% | -90% | -88% |
| BNB | 1666 | 7 | 5% | 2% | -49% | -89% | -88% |
| ETH | 1663 | 9 | 6% | 3% | -35% | -87% | -86% |
| DOGE | 1662 | 2 | 4% | 2% | -85% | -91% | -90% |
| SOL | 1657 | 2 | 4% | 2% | -85% | -92% | -92% |
| XRP | 1652 | 7 | 3% | 1% | -48% | -87% | -87% |
| NEAR | 1650 | 9 | 6% | 3% | -29% | -79% | -79% |
| BTC | 1647 | 8 | 5% | 2% | -35% | -88% | -90% |
| GOLD | 864 | 1 | 3% | 1% | -86% | -92% | -94% |
| SILVER | 841 | 4 | 3% | 1% | -45% | -80% | -80% |
| WTI | 821 | 3 | 3% | 1% | -57% | -94% | -95% |
| COPPER | 735 | 2 | 2% | 1% | -75% | -84% | -84% |
| PLATINUM | 722 | 0 | 1% | 0% | -100% | -99% | -99% |
| NATGAS | 667 | 5 | 2% | 2% | -30% | -82% | -81% |
| PALLADIUM | 659 | 2 | 1% | 0% | -72% | -84% | -84% |
| EURUSD | 659 | 3 | 3% | 1% | -58% | -81% | -81% |
| GBPUSD | 615 | 1 | 2% | 1% | -85% | -97% | -97% |
| USDJPY | 574 | 3 | 1% | 1% | -51% | -99% | -98% |
| AUDUSD | 200 | 0 | 0% | 0% | -100% | -99% | -99% |
| USDCAD | 169 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 11314 | 41 | 4% | 2% | -58% | -89% | -88% |
| DOWN (bought NO) | 11160 | 44 | 4% | 2% | -54% | -88% | -89% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 2569 | 13 | 2% | 1% | -16% | -82% | -81% |
| 0.05–0.1% | 2597 | 8 | 3% | 2% | -55% | -91% | -91% |
| 0.1–0.2% | 3754 | 13 | 5% | 2% | -57% | -90% | -89% |
| 0.2–0.5% | 4325 | 21 | 6% | 3% | -47% | -88% | -88% |
| Over 0.5% | 1700 | 6 | 7% | 3% | -64% | -87% | -89% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 5617 | 22 | 4% | 2% | -56% | -87% | -88% |
| Morning (6am–12pm) | 5315 | 27 | 4% | 2% | -42% | -87% | -86% |
| Afternoon (12–6pm) | 5311 | 19 | 3% | 1% | -57% | -88% | -89% |
| Evening (6pm–12am) | 6231 | 17 | 3% | 2% | -69% | -92% | -91% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,725 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/18 1:26:49 AM | ETH | UP | 3.2 min | -0.209% | 1¢ | ❌ Lost | -$0.15 |
| 10/18 1:26:49 AM | HYPE | UP | 3.2 min | -0.298% | 1¢ | ❌ Lost | -$0.15 |
| 10/18 1:26:49 AM | BTC | UP | 3.2 min | -0.156% | 6¢ | ❌ Lost | $0.00 |
| 10/18 1:26:49 AM | NEAR | UP | 3.2 min | -0.639% | 1¢ | ❌ Lost | -$0.15 |
| 10/18 1:26:49 AM | SOL | UP | 3.2 min | -0.342% | 1¢ | ❌ Lost | -$0.15 |
| 10/18 1:26:34 AM | XRP | UP | 3.4 min | -0.247% | 1¢ | ❌ Lost | -$0.15 |
| 10/18 1:26:34 AM | DOGE | UP | 3.4 min | -0.292% | 1¢ | ❌ Lost | -$0.15 |
| 10/18 1:26:34 AM | ZEC | UP | 3.4 min | -0.368% | 2¢ | ❌ Lost | -$0.15 |
| 10/18 1:26:18 AM | BNB | UP | 3.7 min | -0.110% | 6¢ | ❌ Lost | -$0.15 |
| 10/18 1:14:54 AM | SOL | UP | 6 sec | -0.047% | 0¢ | ❌ Lost | $0.00 |
| 10/18 1:14:38 AM | DOGE | UP | 22 sec | -0.062% | 0¢ | ❌ Lost | $0.00 |
| 10/18 1:14:22 AM | XRP | DOWN | 38 sec | +0.015% | 0¢ | ❌ Lost | -$0.15 |
| 10/18 1:14:22 AM | HYPE | UP | 38 sec | -0.128% | 0¢ | ❌ Lost | $0.00 |
| 10/18 1:13:34 AM | NEAR | UP | 85 sec | -0.378% | 0¢ | ❌ Lost | -$0.15 |
| 10/18 1:12:45 AM | BTC | DOWN | 2.2 min | +0.059% | 1¢ | ❌ Lost | -$0.15 |
| 10/18 1:12:13 AM | BNB | DOWN | 2.8 min | +0.037% | 0¢ | ❌ Lost | $0.00 |
| 10/18 1:09:27 AM | ZEC | UP | 5.5 min | -0.612% | 2¢ | ❌ Lost | -$0.15 |
| 10/18 12:59:56 AM | ZEC | UP | 3 sec | -0.060% | 0¢ | ❌ Lost | $0.00 |
| 10/18 12:59:56 AM | SOL | UP | 3 sec | -0.000% | 0¢ | ❌ Lost | -$0.15 |
| 10/18 12:59:41 AM | DOGE | DOWN | 18 sec | +0.025% | 1¢ | ❌ Lost | -$0.15 |
| 10/18 12:58:22 AM | BTC | UP | 1.6 min | -0.048% | 1¢ | ❌ Lost | -$0.15 |
| 10/18 12:58:06 AM | NEAR | UP | 1.9 min | -0.358% | 1¢ | ❌ Lost | -$0.15 |
| 10/18 12:57:34 AM | HYPE | UP | 2.4 min | -0.172% | 0¢ | ❌ Lost | $0.00 |
| 10/18 12:57:18 AM | XRP | UP | 2.7 min | -0.139% | 1¢ | ❌ Lost | -$0.15 |
| 10/18 12:55:42 AM | ETH | UP | 4.3 min | -0.139% | 1¢ | ❌ Lost | -$0.15 |
| 10/18 12:55:27 AM | BNB | UP | 4.5 min | -0.143% | 1¢ | ❌ Lost | -$0.15 |
| 10/18 12:44:01 AM | BTC | DOWN | 59 sec | +0.050% | 0¢ | ❌ Lost | $0.00 |
| 10/18 12:43:40 AM | HYPE | DOWN | 80 sec | +0.121% | 1¢ | ❌ Lost | -$0.15 |
| 10/18 12:43:40 AM | DOGE | DOWN | 80 sec | +0.085% | 1¢ | ❌ Lost | -$0.15 |
| 10/18 12:43:24 AM | XRP | DOWN | 1.6 min | +0.093% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
