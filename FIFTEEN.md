# 15-Minute 1¢ Study

*Updated Sun Oct 4, 4:33 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 554 finished bets | 1% | $24.45 | +41% | +4.41¢ | -$16.45 / $40.90 |

*Expect about **83 buys a day** (~$12.48/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Volatility model ≥ 2%, hold to the close | 1024 | $16.70 | +14% |
| 5+ min left, hold to the close | 191 | $13.80 | +49% |
| Momentum model ≥ 5%, hold to the close | 557 | $10.90 | +18% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 7679 | 7673 | 35 (0%) | 1.07% | -$429.80 (-47%) | Hold to the close: -$429.80 (-47%) |

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
| Volatility model | 5128 | 4.2% | 0.4% (23) | -620% | ❌ Worse |
| Momentum model | 5128 | 4.3% | 0.4% (23) | -651% | ❌ Worse |
| Mean-reversion model | 5128 | 7.0% | 0.4% (23) | -719% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 5128 | 23 | -43% | -84% | -85% | -82% |
| Volatility model ≥ 2% | 1024 | 10 | +14% | -68% | -68% | -63% |
| Volatility model ≥ 5% | 554 | 6 | +41% | -54% | -54% | -48% |
| Volatility model ≥ 10% | 346 | 4 | +71% | -34% | -36% | -29% |
| Momentum model ≥ 2% | 902 | 7 | -6% | -69% | -71% | -68% |
| Momentum model ≥ 5% | 557 | 5 | +18% | -60% | -63% | -59% |
| Momentum model ≥ 10% | 386 | 4 | +49% | -47% | -48% | -44% |
| Mean-reversion model ≥ 2% | 1809 | 13 | -22% | -82% | -84% | -78% |
| Mean-reversion model ≥ 5% | 1217 | 11 | +0% | -78% | -79% | -72% |
| Mean-reversion model ≥ 10% | 803 | 8 | +16% | -77% | -77% | -70% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 5325 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 1789 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 559 | 4% | 3% | 2% | 2% | 1% | 1% |
| **All** | 7673 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 35 | 0% | -$429.80 | -47% | — |
| Sell at 2¢ | 311 | 4% | -$810.94 | -88% | 34 sec |
| Sell at 3¢ | 199 | 3% | -$814.19 | -89% | 48 sec |
| Sell at 5¢ | 147 | 2% | -$796.25 | -87% | 61 sec |
| Sell at 10¢ | 101 | 1% | -$745.49 | -81% | 78 sec |
| Sell at 25¢ | 56 | 1% | -$678.44 | -74% | 1.6 min |
| Sell at 50¢ | 34 | 0% | -$592.30 | -64% | 1.9 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 3 | 0 | 100% | 67% | -100% | +73% | +160% |
| 5–10 min | 188 | 3 | 12% | 3% | +51% | -78% | -87% |
| 2–5 min | 2474 | 19 | 8% | 4% | -25% | -86% | -86% |
| 1–2 min | 2020 | 8 | 3% | 2% | -57% | -93% | -93% |
| Under 1 min | 2988 | 5 | 1% | 0% | -75% | -88% | -88% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 601 | 5 | 5% | 3% | -2% | -88% | -88% |
| DOGE | 597 | 2 | 4% | 2% | -57% | -91% | -91% |
| HYPE | 595 | 2 | 5% | 3% | -59% | -88% | -86% |
| ETH | 594 | 5 | 6% | 3% | +6% | -85% | -85% |
| BNB | 591 | 2 | 4% | 2% | -60% | -90% | -92% |
| SOL | 590 | 0 | 3% | 1% | -100% | -93% | -91% |
| BTC | 587 | 3 | 6% | 2% | -33% | -86% | -89% |
| XRP | 586 | 4 | 2% | 1% | -13% | -74% | -75% |
| NEAR | 584 | 2 | 6% | 3% | -54% | -62% | -64% |
| GOLD | 304 | 0 | 5% | 1% | -100% | -90% | -92% |
| SILVER | 285 | 0 | 2% | 1% | -100% | -95% | -95% |
| WTI | 276 | 2 | 3% | 1% | -24% | -94% | -96% |
| COPPER | 255 | 0 | 1% | 0% | -100% | -99% | -99% |
| NATGAS | 226 | 2 | 4% | 2% | -17% | -94% | -92% |
| PLATINUM | 226 | 0 | 0% | 0% | -100% | -100% | -100% |
| PALLADIUM | 217 | 1 | 2% | 1% | -57% | -96% | -98% |
| EURUSD | 197 | 1 | 5% | 3% | -53% | -91% | -89% |
| GBPUSD | 196 | 1 | 4% | 2% | -52% | -93% | -93% |
| USDJPY | 166 | 3 | 2% | 2% | +69% | -96% | -94% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 3858 | 19 | 4% | 2% | -42% | -88% | -87% |
| DOWN (bought NO) | 3815 | 16 | 4% | 2% | -51% | -88% | -90% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 900 | 7 | 2% | 1% | +31% | -56% | -56% |
| 0.05–0.1% | 915 | 2 | 3% | 1% | -68% | -90% | -92% |
| 0.1–0.2% | 1310 | 4 | 4% | 2% | -61% | -90% | -91% |
| 0.2–0.5% | 1540 | 8 | 6% | 4% | -43% | -87% | -87% |
| Over 0.5% | 658 | 4 | 7% | 3% | -38% | -86% | -88% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 1882 | 8 | 5% | 2% | -50% | -84% | -86% |
| Morning (6am–12pm) | 2058 | 17 | 5% | 3% | -5% | -89% | -87% |
| Afternoon (12–6pm) | 1675 | 4 | 3% | 1% | -71% | -86% | -87% |
| Evening (6pm–12am) | 2058 | 6 | 3% | 2% | -66% | -93% | -93% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 24 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,126 |
| Time from buy to best bounce (bounced bets) | 49 sec |
| Price snapshots per bet | 41 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/4 4:29:56 PM | EURUSD | UP | 4 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/4 4:29:40 PM | COPPER | UP | 20 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/4 4:29:30 PM | DOGE | UP | 30 sec | -0.087% | 0¢ | ❌ Lost | $0.00 |
| 10/4 4:29:26 PM | WTI | UP | 34 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/4 4:29:24 PM | SOL | UP | 36 sec | -0.146% | 0¢ | ❌ Lost | $0.00 |
| 10/4 4:29:16 PM | BNB | DOWN | 44 sec | +0.079% | 0¢ | ❌ Lost | $0.00 |
| 10/4 4:29:10 PM | XRP | UP | 50 sec | -0.250% | 0¢ | ❌ Lost | -$0.15 |
| 10/4 4:28:36 PM | PALLADIUM | UP | 84 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/4 4:28:16 PM | HYPE | UP | 1.7 min | -0.391% | 0¢ | ❌ Lost | -$0.15 |
| 10/4 4:27:11 PM | NEAR | UP | 2.8 min | -0.748% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 4:26:09 PM | ETH | DOWN | 3.9 min | +0.631% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 4:14:25 PM | NATGAS | UP | 34 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/4 4:14:09 PM | USDJPY | UP | 50 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/4 4:13:00 PM | DOGE | DOWN | 2.0 min | +0.271% | 0¢ | ❌ Lost | -$0.15 |
| 10/4 4:12:25 PM | WTI | UP | 2.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/4 4:12:15 PM | BNB | DOWN | 2.8 min | +0.203% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 4:12:11 PM | EURUSD | DOWN | 2.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/4 4:11:56 PM | GBPUSD | DOWN | 3.1 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/4 4:11:25 PM | ETH | DOWN | 3.6 min | +0.436% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 4:10:13 PM | HYPE | DOWN | 4.8 min | +0.379% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 4:10:11 PM | SOL | DOWN | 4.8 min | +0.584% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 4:10:09 PM | NEAR | DOWN | 4.8 min | +1.628% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 4:09:55 PM | XRP | DOWN | 5.1 min | +0.630% | 2¢ | ❌ Lost | -$0.15 |
| 10/4 4:09:43 PM | BTC | DOWN | 5.3 min | +0.463% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 4:09:39 PM | ZEC | DOWN | 5.3 min | +1.379% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 3:59:05 PM | HYPE | UP | 54 sec | -0.133% | 0¢ | ❌ Lost | $0.00 |
| 10/4 3:58:59 PM | ZEC | UP | 60 sec | -0.205% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 3:58:41 PM | XRP | UP | 78 sec | -0.179% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 3:58:29 PM | BTC | UP | 1.5 min | -0.172% | 0¢ | ❌ Lost | $0.00 |
| 10/4 3:58:09 PM | ETH | UP | 1.8 min | -0.180% | 0¢ | ❌ Lost | $0.00 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
