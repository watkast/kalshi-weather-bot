# 15-Minute 1¢ Study

*Updated Sat Oct 3, 5:49 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Momentum model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 471 finished bets | 1% | $6.65 | +13% | +1.41¢ | $2.20 / $4.45 |

*Expect about **82 buys a day** (~$12.37/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| 5+ min left, hold to the close | 177 | $1.90 | +7% |
| Volatility model ≥ 5%, hold to the close | 470 | -$7.80 | -16% |
| Momentum model ≥ 5%, sell at 50¢ | 471 | -$7.85 | -16% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 6890 | 6884 | 29 (0%) | 1.07% | -$421.85 (-51%) | Hold to the close: -$421.85 (-51%) |

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
| Volatility model | 4348 | 4.1% | 0.4% (17) | -665% | ❌ Worse |
| Momentum model | 4348 | 4.2% | 0.4% (17) | -698% | ❌ Worse |
| Mean-reversion model | 4348 | 7.0% | 0.4% (17) | -790% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 4348 | 17 | -50% | -83% | -84% | -81% |
| Volatility model ≥ 2% | 896 | 6 | -22% | -68% | -69% | -63% |
| Volatility model ≥ 5% | 470 | 3 | -16% | -50% | -52% | -47% |
| Volatility model ≥ 10% | 283 | 3 | +63% | -24% | -28% | -21% |
| Momentum model ≥ 2% | 782 | 5 | -22% | -67% | -70% | -67% |
| Momentum model ≥ 5% | 471 | 4 | +13% | -55% | -60% | -55% |
| Momentum model ≥ 10% | 320 | 3 | +38% | -40% | -42% | -37% |
| Mean-reversion model ≥ 2% | 1580 | 8 | -45% | -84% | -85% | -80% |
| Mean-reversion model ≥ 5% | 1067 | 7 | -27% | -80% | -81% | -74% |
| Mean-reversion model ≥ 10% | 701 | 5 | -17% | -78% | -80% | -72% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 4545 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 1784 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 555 | 4% | 3% | 2% | 2% | 1% | 1% |
| **All** | 6884 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 29 | 0% | -$421.85 | -51% | — |
| Sell at 2¢ | 270 | 4% | -$729.65 | -88% | 34 sec |
| Sell at 3¢ | 171 | 2% | -$733.16 | -89% | 48 sec |
| Sell at 5¢ | 129 | 2% | -$716.00 | -86% | 61 sec |
| Sell at 10¢ | 87 | 1% | -$671.88 | -81% | 78 sec |
| Sell at 25¢ | 48 | 1% | -$612.97 | -74% | 1.6 min |
| Sell at 50¢ | 28 | 0% | -$540.85 | -65% | 1.7 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 3 | 0 | 100% | 67% | -100% | +73% | +160% |
| 5–10 min | 174 | 2 | 11% | 3% | +9% | -80% | -89% |
| 2–5 min | 2242 | 14 | 8% | 4% | -39% | -86% | -87% |
| 1–2 min | 1785 | 8 | 3% | 2% | -51% | -94% | -93% |
| Under 1 min | 2680 | 5 | 1% | 0% | -72% | -87% | -87% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| DOGE | 511 | 2 | 4% | 1% | -49% | -91% | -91% |
| ZEC | 510 | 3 | 5% | 3% | -31% | -89% | -90% |
| ETH | 509 | 4 | 6% | 3% | +0% | -86% | -85% |
| HYPE | 509 | 2 | 5% | 4% | -52% | -88% | -85% |
| BNB | 504 | 1 | 4% | 2% | -76% | -91% | -92% |
| XRP | 501 | 4 | 2% | 1% | +3% | -70% | -70% |
| SOL | 501 | 0 | 3% | 1% | -100% | -93% | -93% |
| NEAR | 500 | 2 | 6% | 2% | -46% | -58% | -60% |
| BTC | 500 | 1 | 6% | 2% | -74% | -86% | -89% |
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
| UP (bought YES) | 3483 | 17 | 4% | 2% | -43% | -88% | -87% |
| DOWN (bought NO) | 3401 | 12 | 4% | 2% | -59% | -88% | -90% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 688 | 5 | 2% | 1% | +30% | -43% | -43% |
| 0.05–0.1% | 726 | 0 | 3% | 1% | -100% | -92% | -93% |
| 0.1–0.2% | 1112 | 4 | 4% | 2% | -53% | -90% | -91% |
| 0.2–0.5% | 1404 | 6 | 6% | 3% | -53% | -88% | -87% |
| Over 0.5% | 613 | 4 | 7% | 3% | -33% | -86% | -88% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 1673 | 7 | 4% | 2% | -51% | -84% | -85% |
| Morning (6am–12pm) | 1849 | 13 | 5% | 3% | -20% | -90% | -89% |
| Afternoon (12–6pm) | 1504 | 3 | 3% | 1% | -76% | -85% | -87% |
| Evening (6pm–12am) | 1858 | 6 | 3% | 2% | -62% | -93% | -93% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 25 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 3,682 |
| Time from buy to best bounce (bounced bets) | 49 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/3 5:44:59 PM | HYPE | UP | 1 sec | -0.017% | 0¢ | ❌ Lost | $0.00 |
| 10/3 5:44:43 PM | SOL | UP | 16 sec | -0.027% | 0¢ | ❌ Lost | $0.00 |
| 10/3 5:44:27 PM | DOGE | DOWN | 32 sec | -0.030% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 5:44:27 PM | BNB | DOWN | 32 sec | -0.028% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 5:44:27 PM | ETH | DOWN | 32 sec | +0.015% | 0¢ | ❌ Lost | -$0.15 |
| 10/3 5:44:11 PM | XRP | DOWN | 48 sec | +0.027% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 5:43:55 PM | NEAR | UP | 64 sec | -0.311% | 0¢ | ❌ Lost | $0.00 |
| 10/3 5:43:06 PM | BTC | DOWN | 1.9 min | +0.054% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 5:42:03 PM | ZEC | UP | 2.9 min | -0.255% | 77¢ | ❌ Lost | -$0.15 |
| 10/3 5:29:39 PM | SOL | DOWN | 21 sec | +0.025% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 5:29:39 PM | XRP | UP | 21 sec | -0.034% | 0¢ | ❌ Lost | $0.00 |
| 10/3 5:29:39 PM | ETH | DOWN | 21 sec | +0.024% | 0¢ | ❌ Lost | $0.00 |
| 10/3 5:29:23 PM | BTC | UP | 37 sec | -0.032% | 0¢ | ❌ Lost | $0.00 |
| 10/3 5:29:07 PM | DOGE | UP | 53 sec | -0.098% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 5:29:07 PM | NEAR | UP | 53 sec | -0.447% | 0¢ | ❌ Lost | -$0.15 |
| 10/3 5:28:04 PM | BNB | UP | 1.9 min | -0.152% | 0¢ | ❌ Lost | -$0.15 |
| 10/3 5:27:01 PM | HYPE | UP | 3.0 min | -0.218% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 5:26:30 PM | ZEC | DOWN | 3.5 min | +0.673% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 5:14:34 PM | SOL | UP | 25 sec | -0.042% | 0¢ | ❌ Lost | $0.00 |
| 10/3 5:14:34 PM | BTC | UP | 25 sec | -0.021% | 0¢ | ❌ Lost | -$0.15 |
| 10/3 5:14:34 PM | HYPE | UP | 25 sec | +0.002% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 5:13:13 PM | DOGE | UP | 1.8 min | -0.119% | 2¢ | ❌ Lost | -$0.15 |
| 10/3 5:13:13 PM | ZEC | UP | 1.8 min | -0.405% | 0¢ | ❌ Lost | -$0.15 |
| 10/3 5:11:39 PM | NEAR | DOWN | 3.3 min | +0.616% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 5:11:08 PM | BNB | UP | 3.9 min | -0.190% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 4:59:38 PM | BTC | UP | 22 sec | -0.029% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 4:58:35 PM | BNB | DOWN | 85 sec | +0.030% | 0¢ | ❌ Lost | -$0.15 |
| 10/3 4:58:35 PM | ETH | UP | 85 sec | -0.035% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 4:58:17 PM | DOGE | UP | 1.7 min | -0.118% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 4:58:17 PM | SOL | UP | 1.7 min | -0.105% | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
