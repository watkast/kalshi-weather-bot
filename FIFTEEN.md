# 15-Minute 1¢ Study

*Updated Sun Oct 4, 11:33 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 572 finished bets | 1% | $22.35 | +36% | +3.91¢ | -$17.50 / $39.85 |

*Expect about **82 buys a day** (~$12.34/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Volatility model ≥ 2%, hold to the close | 1052 | $13.25 | +10% |
| 5+ min left, hold to the close | 195 | $13.20 | +46% |
| Momentum model ≥ 5%, hold to the close | 577 | $8.50 | +14% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 8067 | 8061 | 36 (0%) | 1.07% | -$462.45 (-48%) | Hold to the close: -$462.45 (-48%) |

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
| Volatility model | 5353 | 4.2% | 0.4% (24) | -611% | ❌ Worse |
| Momentum model | 5353 | 4.3% | 0.4% (24) | -642% | ❌ Worse |
| Mean-reversion model | 5353 | 6.8% | 0.4% (24) | -708% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 5353 | 24 | -43% | -84% | -85% | -82% |
| Volatility model ≥ 2% | 1052 | 10 | +10% | -69% | -69% | -64% |
| Volatility model ≥ 5% | 572 | 6 | +36% | -55% | -55% | -50% |
| Volatility model ≥ 10% | 356 | 4 | +65% | -36% | -38% | -32% |
| Momentum model ≥ 2% | 930 | 7 | -9% | -69% | -72% | -69% |
| Momentum model ≥ 5% | 577 | 5 | +14% | -61% | -64% | -60% |
| Momentum model ≥ 10% | 400 | 4 | +43% | -48% | -49% | -46% |
| Mean-reversion model ≥ 2% | 1857 | 13 | -24% | -82% | -84% | -79% |
| Mean-reversion model ≥ 5% | 1246 | 11 | -2% | -79% | -79% | -72% |
| Mean-reversion model ≥ 10% | 824 | 8 | +12% | -77% | -78% | -71% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 5550 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 1905 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 606 | 4% | 3% | 2% | 2% | 1% | 0% |
| **All** | 8061 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 36 | 0% | -$462.45 | -48% | — |
| Sell at 2¢ | 320 | 4% | -$855.25 | -88% | 33 sec |
| Sell at 3¢ | 206 | 3% | -$858.11 | -89% | 47 sec |
| Sell at 5¢ | 152 | 2% | -$839.65 | -87% | 61 sec |
| Sell at 10¢ | 104 | 1% | -$788.21 | -82% | 72 sec |
| Sell at 25¢ | 57 | 1% | -$707.78 | -73% | 1.6 min |
| Sell at 50¢ | 35 | 0% | -$618.20 | -64% | 1.9 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 3 | 0 | 100% | 67% | -100% | +73% | +160% |
| 5–10 min | 192 | 3 | 12% | 3% | +48% | -79% | -88% |
| 2–5 min | 2588 | 19 | 8% | 4% | -28% | -86% | -86% |
| 1–2 min | 2139 | 9 | 3% | 2% | -54% | -93% | -93% |
| Under 1 min | 3139 | 5 | 1% | 0% | -76% | -88% | -89% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 627 | 5 | 5% | 3% | -6% | -89% | -89% |
| DOGE | 621 | 2 | 4% | 1% | -58% | -91% | -91% |
| ETH | 620 | 5 | 6% | 3% | +2% | -86% | -86% |
| HYPE | 617 | 3 | 5% | 3% | -41% | -88% | -86% |
| BNB | 616 | 2 | 4% | 2% | -61% | -90% | -92% |
| SOL | 615 | 0 | 3% | 1% | -100% | -92% | -91% |
| BTC | 613 | 3 | 6% | 2% | -36% | -86% | -89% |
| XRP | 613 | 4 | 2% | 1% | -16% | -75% | -76% |
| NEAR | 608 | 2 | 6% | 3% | -57% | -63% | -64% |
| GOLD | 323 | 0 | 4% | 1% | -100% | -90% | -93% |
| SILVER | 309 | 0 | 2% | 1% | -100% | -96% | -96% |
| WTI | 295 | 2 | 3% | 1% | -28% | -95% | -96% |
| COPPER | 272 | 0 | 1% | 0% | -100% | -99% | -99% |
| NATGAS | 238 | 2 | 3% | 2% | -22% | -94% | -92% |
| PLATINUM | 238 | 0 | 0% | 0% | -100% | -100% | -100% |
| PALLADIUM | 230 | 1 | 2% | 1% | -59% | -96% | -98% |
| EURUSD | 218 | 1 | 5% | 3% | -57% | -92% | -90% |
| GBPUSD | 207 | 1 | 4% | 2% | -55% | -93% | -94% |
| USDJPY | 181 | 3 | 2% | 2% | +55% | -96% | -94% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 4078 | 20 | 4% | 2% | -42% | -88% | -88% |
| DOWN (bought NO) | 3983 | 16 | 4% | 2% | -53% | -89% | -90% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 934 | 7 | 2% | 1% | +27% | -58% | -57% |
| 0.05–0.1% | 939 | 2 | 4% | 1% | -69% | -90% | -92% |
| 0.1–0.2% | 1375 | 5 | 4% | 2% | -54% | -90% | -91% |
| 0.2–0.5% | 1625 | 8 | 6% | 3% | -45% | -87% | -87% |
| Over 0.5% | 675 | 4 | 7% | 3% | -39% | -87% | -89% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 1882 | 8 | 5% | 2% | -50% | -84% | -86% |
| Morning (6am–12pm) | 2058 | 17 | 5% | 3% | -5% | -89% | -87% |
| Afternoon (12–6pm) | 1751 | 4 | 3% | 1% | -73% | -86% | -87% |
| Evening (6pm–12am) | 2370 | 7 | 3% | 2% | -66% | -94% | -94% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 25 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,182 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 41 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/4 11:29:51 PM | GOLD | UP | 9 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/4 11:29:51 PM | BTC | DOWN | 9 sec | +0.021% | 0¢ | ❌ Lost | $0.00 |
| 10/4 11:29:35 PM | USDJPY | DOWN | 25 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/4 11:29:35 PM | SILVER | UP | 25 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/4 11:29:03 PM | XRP | UP | 57 sec | -0.113% | 0¢ | ❌ Lost | -$0.15 |
| 10/4 11:29:03 PM | BNB | DOWN | 57 sec | +0.025% | 0¢ | ❌ Lost | -$0.15 |
| 10/4 11:29:03 PM | ZEC | DOWN | 57 sec | +0.129% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 11:28:48 PM | DOGE | UP | 71 sec | -0.182% | 0¢ | ❌ Lost | -$0.15 |
| 10/4 11:28:48 PM | SOL | UP | 71 sec | -0.175% | 0¢ | ❌ Lost | -$0.15 |
| 10/4 11:28:48 PM | WTI | DOWN | 71 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/4 11:28:16 PM | ETH | UP | 1.7 min | -0.110% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 11:28:00 PM | NEAR | UP | 2.0 min | -1.295% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 11:14:53 PM | HYPE | UP | 6 sec | -0.112% | 0¢ | ❌ Lost | -$0.15 |
| 10/4 11:14:53 PM | COPPER | DOWN | 6 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/4 11:14:53 PM | BTC | UP | 6 sec | -0.018% | 0¢ | ❌ Lost | $0.00 |
| 10/4 11:14:37 PM | DOGE | DOWN | 22 sec | +0.033% | 0¢ | ❌ Lost | -$0.15 |
| 10/4 11:14:21 PM | SOL | UP | 38 sec | -0.121% | 0¢ | ❌ Lost | $0.00 |
| 10/4 11:14:21 PM | ETH | UP | 38 sec | -0.067% | 0¢ | ❌ Lost | $0.00 |
| 10/4 11:14:21 PM | EURUSD | DOWN | 38 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/4 11:14:21 PM | BNB | UP | 38 sec | -0.021% | 0¢ | ❌ Lost | -$0.15 |
| 10/4 11:14:05 PM | XRP | UP | 55 sec | -0.106% | 0¢ | ❌ Lost | -$0.15 |
| 10/4 11:13:47 PM | PLATINUM | DOWN | 73 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/4 11:13:15 PM | ZEC | DOWN | 1.8 min | +0.325% | 0¢ | ❌ Lost | -$0.15 |
| 10/4 11:13:15 PM | PALLADIUM | DOWN | 1.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/4 11:12:59 PM | WTI | UP | 2.0 min | — | 0¢ | ❌ Lost | $0.00 |
| 10/4 11:12:59 PM | GOLD | DOWN | 2.0 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/4 11:12:25 PM | SILVER | DOWN | 2.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/4 11:12:09 PM | USDJPY | UP | 2.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/4 11:11:06 PM | NEAR | DOWN | 3.9 min | +2.699% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 10:59:54 PM | DOGE | DOWN | 5 sec | +0.027% | 0¢ | ❌ Lost | $0.00 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
