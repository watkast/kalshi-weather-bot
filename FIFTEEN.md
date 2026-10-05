# 15-Minute 1¢ Study

*Updated Mon Oct 5, 5:46 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 619 finished bets | 1% | $31.25 | +47% | +5.05¢ | -$5.90 / $37.15 |

*Expect about **80 buys a day** (~$12.04/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 619 | $17.85 | +27% |
| Volatility model ≥ 2%, hold to the close | 1152 | $15.10 | +11% |
| Mean-reversion model ≥ 5%, hold to the close | 1360 | $10.70 | +6% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 8916 | 8910 | 39 (0%) | 1.07% | -$525.60 (-49%) | Hold to the close: -$525.60 (-49%) |

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
| Volatility model | 5863 | 4.1% | 0.5% (27) | -579% | ❌ Worse |
| Momentum model | 5863 | 4.1% | 0.5% (27) | -604% | ❌ Worse |
| Mean-reversion model | 5863 | 6.8% | 0.5% (27) | -677% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 5863 | 27 | -42% | -85% | -85% | -83% |
| Volatility model ≥ 2% | 1152 | 11 | +11% | -70% | -70% | -66% |
| Volatility model ≥ 5% | 619 | 7 | +47% | -57% | -56% | -53% |
| Volatility model ≥ 10% | 381 | 5 | +94% | -38% | -39% | -34% |
| Momentum model ≥ 2% | 1017 | 9 | +7% | -71% | -73% | -70% |
| Momentum model ≥ 5% | 619 | 6 | +27% | -62% | -65% | -62% |
| Momentum model ≥ 10% | 427 | 5 | +68% | -50% | -51% | -48% |
| Mean-reversion model ≥ 2% | 2027 | 15 | -19% | -83% | -83% | -78% |
| Mean-reversion model ≥ 5% | 1360 | 13 | +6% | -79% | -79% | -72% |
| Mean-reversion model ≥ 10% | 897 | 9 | +16% | -77% | -78% | -71% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 6060 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 2159 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 691 | 3% | 3% | 2% | 2% | 1% | 0% |
| **All** | 8910 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 39 | 0% | -$525.60 | -49% | — |
| Sell at 2¢ | 342 | 4% | -$954.68 | -89% | 33 sec |
| Sell at 3¢ | 224 | 3% | -$956.24 | -89% | 47 sec |
| Sell at 5¢ | 165 | 2% | -$936.35 | -87% | 61 sec |
| Sell at 10¢ | 111 | 1% | -$884.19 | -83% | 66 sec |
| Sell at 25¢ | 61 | 1% | -$799.69 | -75% | 83 sec |
| Sell at 50¢ | 38 | 0% | -$703.10 | -66% | 1.7 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 3 | 0 | 100% | 67% | -100% | +73% | +160% |
| 5–10 min | 223 | 3 | 11% | 3% | +27% | -81% | -88% |
| 2–5 min | 2886 | 21 | 7% | 3% | -29% | -87% | -87% |
| 1–2 min | 2346 | 10 | 3% | 2% | -54% | -93% | -93% |
| Under 1 min | 3452 | 5 | 1% | 0% | -78% | -89% | -89% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 685 | 5 | 5% | 3% | -13% | -89% | -89% |
| DOGE | 676 | 2 | 4% | 1% | -62% | -91% | -90% |
| HYPE | 676 | 3 | 5% | 3% | -46% | -88% | -86% |
| ETH | 675 | 6 | 6% | 3% | +12% | -87% | -86% |
| BNB | 672 | 2 | 4% | 2% | -64% | -90% | -92% |
| XRP | 670 | 4 | 1% | 1% | -24% | -77% | -78% |
| SOL | 670 | 0 | 3% | 1% | -100% | -93% | -92% |
| BTC | 669 | 3 | 5% | 2% | -41% | -87% | -90% |
| NEAR | 667 | 4 | 6% | 3% | -22% | -65% | -66% |
| GOLD | 363 | 0 | 4% | 1% | -100% | -91% | -94% |
| SILVER | 348 | 0 | 2% | 1% | -100% | -96% | -96% |
| WTI | 331 | 2 | 3% | 1% | -35% | -95% | -96% |
| COPPER | 306 | 0 | 1% | 0% | -100% | -99% | -99% |
| PLATINUM | 276 | 0 | 0% | 0% | -100% | -100% | -100% |
| NATGAS | 270 | 2 | 3% | 2% | -31% | -94% | -92% |
| PALLADIUM | 265 | 1 | 2% | 1% | -65% | -97% | -98% |
| EURUSD | 247 | 1 | 4% | 3% | -62% | -92% | -91% |
| GBPUSD | 238 | 1 | 4% | 2% | -61% | -93% | -93% |
| USDJPY | 206 | 3 | 2% | 1% | +36% | -97% | -95% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 4505 | 21 | 4% | 2% | -45% | -89% | -88% |
| DOWN (bought NO) | 4405 | 18 | 4% | 2% | -53% | -90% | -90% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 1004 | 7 | 2% | 1% | +19% | -60% | -59% |
| 0.05–0.1% | 1020 | 3 | 3% | 1% | -56% | -91% | -92% |
| 0.1–0.2% | 1518 | 6 | 4% | 2% | -49% | -91% | -91% |
| 0.2–0.5% | 1778 | 9 | 6% | 3% | -44% | -87% | -87% |
| Over 0.5% | 738 | 4 | 7% | 3% | -45% | -87% | -89% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 2228 | 9 | 4% | 2% | -53% | -86% | -87% |
| Morning (6am–12pm) | 2361 | 17 | 5% | 3% | -18% | -90% | -88% |
| Afternoon (12–6pm) | 1927 | 6 | 3% | 1% | -62% | -86% | -87% |
| Evening (6pm–12am) | 2394 | 7 | 3% | 2% | -66% | -94% | -94% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 25 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,128 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/5 5:44:53 PM | PALLADIUM | UP | 7 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/5 5:44:53 PM | COPPER | UP | 7 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/5 5:44:37 PM | XRP | UP | 23 sec | -0.026% | 0¢ | ❌ Lost | -$0.15 |
| 10/5 5:44:06 PM | DOGE | UP | 53 sec | -0.056% | 1¢ | ❌ Lost | -$0.15 |
| 10/5 5:44:06 PM | SOL | UP | 53 sec | -0.054% | 0¢ | ❌ Lost | $0.00 |
| 10/5 5:43:33 PM | ETH | UP | 87 sec | -0.067% | 1¢ | ❌ Lost | -$0.15 |
| 10/5 5:43:33 PM | BTC | UP | 87 sec | -0.127% | 0¢ | ❌ Lost | $0.00 |
| 10/5 5:43:02 PM | GOLD | UP | 1.9 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/5 5:43:02 PM | BNB | UP | 1.9 min | -0.075% | 1¢ | ❌ Lost | -$0.15 |
| 10/5 5:42:14 PM | SILVER | UP | 2.8 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/5 5:41:58 PM | NEAR | UP | 3.0 min | -0.756% | 1¢ | ❌ Lost | -$0.15 |
| 10/5 5:41:08 PM | HYPE | UP | 3.9 min | -0.164% | 5¢ | ❌ Lost | -$0.15 |
| 10/5 5:40:53 PM | ZEC | UP | 4.1 min | -0.469% | 1¢ | ❌ Lost | -$0.15 |
| 10/5 5:29:59 PM | COPPER | DOWN | 0 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/5 5:29:59 PM | USDJPY | UP | 0 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/5 5:29:43 PM | BNB | DOWN | 16 sec | +0.018% | 0¢ | ❌ Lost | -$0.15 |
| 10/5 5:29:27 PM | ZEC | DOWN | 32 sec | +0.120% | 0¢ | ❌ Lost | $0.00 |
| 10/5 5:29:27 PM | WTI | UP | 32 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/5 5:29:11 PM | ETH | DOWN | 48 sec | +0.053% | 0¢ | ❌ Lost | -$0.15 |
| 10/5 5:29:11 PM | HYPE | UP | 48 sec | -0.140% | 0¢ | ❌ Lost | $0.00 |
| 10/5 5:29:11 PM | EURUSD | DOWN | 48 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/5 5:29:11 PM | BTC | DOWN | 48 sec | +0.051% | 1¢ | ❌ Lost | -$0.15 |
| 10/5 5:28:55 PM | XRP | DOWN | 64 sec | +0.099% | 1¢ | ❌ Lost | -$0.15 |
| 10/5 5:28:55 PM | NEAR | UP | 64 sec | -0.720% | 0¢ | ❌ Lost | -$0.15 |
| 10/5 5:28:39 PM | NATGAS | UP | 80 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/5 5:28:23 PM | GOLD | DOWN | 1.6 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/5 5:28:23 PM | GBPUSD | DOWN | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/5 5:28:23 PM | PLATINUM | DOWN | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/5 5:27:19 PM | SILVER | DOWN | 2.7 min | — | 3¢ | ❌ Lost | -$0.15 |
| 10/5 5:14:35 PM | ETH | UP | 24 sec | -0.118% | 0¢ | ❌ Lost | $0.00 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
