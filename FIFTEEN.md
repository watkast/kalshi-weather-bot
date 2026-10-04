# 15-Minute 1¢ Study

*Updated Sun Oct 4, 3:52 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (5+ min left).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| 5+ min left, hold to the close | 188 finished bets | 2% | $14.25 | +51% | +7.58¢ | $14.05 / $0.20 |

*Expect about **28 buys a day** (~$4.15/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 552 | $10.75 | +18% |
| Volatility model ≥ 2%, hold to the close | 1022 | $3.00 | +2% |
| Mean-reversion model ≥ 5%, hold to the close | 1216 | $0.85 | +1% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 7644 | 7638 | 34 (0%) | 1.07% | -$439.45 (-48%) | Hold to the close: -$439.45 (-48%) |

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
| Volatility model | 5102 | 4.3% | 0.4% (22) | -641% | ❌ Worse |
| Momentum model | 5102 | 4.3% | 0.4% (22) | -673% | ❌ Worse |
| Mean-reversion model | 5102 | 7.0% | 0.4% (22) | -742% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 5102 | 22 | -45% | -84% | -85% | -82% |
| Volatility model ≥ 2% | 1022 | 9 | +2% | -68% | -69% | -63% |
| Volatility model ≥ 5% | 552 | 5 | +18% | -54% | -54% | -49% |
| Volatility model ≥ 10% | 346 | 4 | +71% | -34% | -36% | -29% |
| Momentum model ≥ 2% | 899 | 6 | -19% | -69% | -71% | -68% |
| Momentum model ≥ 5% | 555 | 4 | -5% | -60% | -64% | -60% |
| Momentum model ≥ 10% | 384 | 3 | +13% | -47% | -49% | -45% |
| Mean-reversion model ≥ 2% | 1804 | 12 | -28% | -83% | -84% | -78% |
| Mean-reversion model ≥ 5% | 1216 | 11 | +1% | -78% | -79% | -72% |
| Mean-reversion model ≥ 10% | 803 | 8 | +16% | -77% | -77% | -70% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 5299 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 1784 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 555 | 4% | 3% | 2% | 2% | 1% | 1% |
| **All** | 7638 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 34 | 0% | -$439.45 | -48% | — |
| Sell at 2¢ | 310 | 4% | -$806.85 | -88% | 34 sec |
| Sell at 3¢ | 198 | 3% | -$810.23 | -89% | 48 sec |
| Sell at 5¢ | 146 | 2% | -$792.55 | -87% | 62 sec |
| Sell at 10¢ | 100 | 1% | -$742.45 | -81% | 78 sec |
| Sell at 25¢ | 55 | 1% | -$677.40 | -74% | 1.6 min |
| Sell at 50¢ | 33 | 0% | -$594.70 | -65% | 1.9 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 3 | 0 | 100% | 67% | -100% | +73% | +160% |
| 5–10 min | 185 | 3 | 12% | 3% | +54% | -78% | -87% |
| 2–5 min | 2461 | 18 | 8% | 4% | -29% | -86% | -86% |
| 1–2 min | 2011 | 8 | 3% | 2% | -57% | -93% | -93% |
| Under 1 min | 2978 | 5 | 1% | 0% | -75% | -88% | -88% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 598 | 4 | 5% | 3% | -21% | -89% | -89% |
| DOGE | 594 | 2 | 4% | 2% | -56% | -91% | -91% |
| HYPE | 592 | 2 | 5% | 3% | -59% | -88% | -86% |
| ETH | 591 | 5 | 6% | 3% | +6% | -85% | -85% |
| BNB | 588 | 2 | 4% | 2% | -59% | -90% | -92% |
| SOL | 587 | 0 | 3% | 1% | -100% | -93% | -91% |
| BTC | 585 | 3 | 6% | 2% | -33% | -86% | -89% |
| XRP | 583 | 4 | 2% | 1% | -13% | -74% | -74% |
| NEAR | 581 | 2 | 6% | 3% | -54% | -62% | -64% |
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
| UP (bought YES) | 3837 | 19 | 4% | 2% | -42% | -88% | -87% |
| DOWN (bought NO) | 3801 | 15 | 4% | 2% | -54% | -88% | -90% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 900 | 7 | 2% | 1% | +31% | -56% | -56% |
| 0.05–0.1% | 913 | 2 | 4% | 1% | -68% | -90% | -92% |
| 0.1–0.2% | 1304 | 4 | 4% | 2% | -61% | -90% | -91% |
| 0.2–0.5% | 1530 | 7 | 6% | 3% | -49% | -87% | -87% |
| Over 0.5% | 650 | 4 | 7% | 3% | -37% | -86% | -88% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 1882 | 8 | 5% | 2% | -50% | -84% | -86% |
| Morning (6am–12pm) | 2058 | 17 | 5% | 3% | -5% | -89% | -87% |
| Afternoon (12–6pm) | 1640 | 3 | 3% | 1% | -78% | -85% | -87% |
| Evening (6pm–12am) | 2058 | 6 | 3% | 2% | -66% | -93% | -93% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 24 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,111 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 41 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/4 3:44:40 PM | SOL | DOWN | 19 sec | +0.020% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 3:44:32 PM | DOGE | DOWN | 27 sec | +0.069% | 0¢ | ❌ Lost | -$0.15 |
| 10/4 3:44:04 PM | BNB | DOWN | 55 sec | +0.032% | 0¢ | ❌ Lost | -$0.15 |
| 10/4 3:43:59 PM | NEAR | DOWN | 60 sec | +0.073% | 0¢ | ❌ Lost | $0.00 |
| 10/4 3:43:40 PM | ETH | DOWN | 79 sec | +0.098% | 0¢ | ❌ Lost | -$0.15 |
| 10/4 3:42:32 PM | BTC | DOWN | 2.5 min | +0.172% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 3:42:18 PM | HYPE | UP | 2.7 min | -0.231% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 3:41:22 PM | ZEC | DOWN | 3.6 min | +0.460% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 3:29:19 PM | BNB | UP | 40 sec | -0.151% | 0¢ | ❌ Lost | $0.00 |
| 10/4 3:28:39 PM | SOL | UP | 80 sec | -0.115% | 0¢ | ❌ Lost | -$0.15 |
| 10/4 3:28:09 PM | ETH | UP | 1.8 min | -0.117% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 3:28:09 PM | NEAR | UP | 1.8 min | -0.405% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 3:27:59 PM | DOGE | DOWN | 2.0 min | +0.307% | 0¢ | ❌ Lost | -$0.15 |
| 10/4 3:27:59 PM | BTC | UP | 2.0 min | -0.207% | 0¢ | ❌ Lost | -$0.15 |
| 10/4 3:27:31 PM | ZEC | UP | 2.5 min | -0.369% | 0¢ | ❌ Lost | -$0.15 |
| 10/4 3:14:40 PM | ETH | DOWN | 19 sec | +0.058% | 0¢ | ❌ Lost | $0.00 |
| 10/4 3:14:36 PM | HYPE | DOWN | 23 sec | +0.217% | 0¢ | ❌ Lost | $0.00 |
| 10/4 3:13:44 PM | BTC | DOWN | 75 sec | +0.180% | 0¢ | ❌ Lost | $0.00 |
| 10/4 3:13:26 PM | SOL | DOWN | 1.6 min | +0.139% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 3:13:26 PM | XRP | DOWN | 1.6 min | +0.252% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 3:12:49 PM | ZEC | DOWN | 2.2 min | +0.222% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 3:12:49 PM | NEAR | UP | 2.2 min | -0.585% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 3:12:36 PM | DOGE | DOWN | 2.4 min | +0.732% | 0¢ | ❌ Lost | $0.00 |
| 10/4 3:11:26 PM | BNB | DOWN | 3.5 min | +0.240% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 2:59:40 PM | ZEC | UP | 19 sec | -0.168% | 0¢ | ❌ Lost | $0.00 |
| 10/4 2:59:30 PM | NEAR | UP | 29 sec | -0.298% | 0¢ | ❌ Lost | $0.00 |
| 10/4 2:59:30 PM | HYPE | DOWN | 29 sec | +0.032% | 0¢ | ❌ Lost | $0.00 |
| 10/4 2:59:28 PM | BTC | DOWN | 31 sec | +0.083% | 0¢ | ❌ Lost | $0.00 |
| 10/4 2:58:45 PM | BNB | DOWN | 75 sec | +0.071% | 0¢ | ❌ Lost | -$0.15 |
| 10/4 2:58:11 PM | XRP | DOWN | 1.8 min | +0.193% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
