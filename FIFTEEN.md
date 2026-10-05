# 15-Minute 1¢ Study

*Updated Mon Oct 5, 12:54 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 612 finished bets | 1% | $31.85 | +48% | +5.20¢ | -$5.75 / $37.60 |

*Expect about **82 buys a day** (~$12.23/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 614 | $18.30 | +28% |
| Volatility model ≥ 2%, hold to the close | 1139 | $16.45 | +12% |
| 5+ min left, hold to the close | 224 | $8.85 | +27% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 8776 | 8770 | 37 (0%) | 1.07% | -$537.85 (-51%) | Hold to the close: -$537.85 (-51%) |

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
| Volatility model | 5776 | 4.1% | 0.4% (25) | -603% | ❌ Worse |
| Momentum model | 5776 | 4.2% | 0.4% (25) | -629% | ❌ Worse |
| Mean-reversion model | 5776 | 6.8% | 0.4% (25) | -706% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 5776 | 25 | -45% | -85% | -85% | -83% |
| Volatility model ≥ 2% | 1139 | 11 | +12% | -70% | -70% | -65% |
| Volatility model ≥ 5% | 612 | 7 | +48% | -57% | -56% | -52% |
| Volatility model ≥ 10% | 378 | 5 | +95% | -38% | -39% | -34% |
| Momentum model ≥ 2% | 1005 | 8 | -4% | -71% | -73% | -71% |
| Momentum model ≥ 5% | 614 | 6 | +28% | -62% | -64% | -62% |
| Momentum model ≥ 10% | 424 | 5 | +68% | -49% | -50% | -48% |
| Mean-reversion model ≥ 2% | 2001 | 14 | -24% | -83% | -83% | -79% |
| Mean-reversion model ≥ 5% | 1344 | 12 | -1% | -79% | -80% | -73% |
| Mean-reversion model ≥ 10% | 887 | 9 | +17% | -78% | -78% | -72% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 5973 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 2116 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 681 | 3% | 3% | 2% | 1% | 1% | 0% |
| **All** | 8770 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 37 | 0% | -$537.85 | -51% | — |
| Sell at 2¢ | 336 | 4% | -$940.49 | -89% | 33 sec |
| Sell at 3¢ | 219 | 2% | -$942.44 | -89% | 47 sec |
| Sell at 5¢ | 161 | 2% | -$923.20 | -87% | 61 sec |
| Sell at 10¢ | 107 | 1% | -$873.68 | -83% | 66 sec |
| Sell at 25¢ | 59 | 1% | -$790.56 | -75% | 1.5 min |
| Sell at 50¢ | 36 | 0% | -$700.85 | -66% | 1.8 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 3 | 0 | 100% | 67% | -100% | +73% | +160% |
| 5–10 min | 221 | 3 | 11% | 3% | +28% | -81% | -88% |
| 2–5 min | 2851 | 20 | 7% | 3% | -31% | -87% | -87% |
| 1–2 min | 2313 | 9 | 3% | 2% | -58% | -93% | -93% |
| Under 1 min | 3382 | 5 | 1% | 0% | -78% | -89% | -89% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 675 | 5 | 5% | 3% | -12% | -89% | -89% |
| DOGE | 667 | 2 | 4% | 1% | -61% | -91% | -90% |
| ETH | 666 | 5 | 6% | 3% | -6% | -87% | -87% |
| HYPE | 666 | 3 | 5% | 3% | -45% | -88% | -86% |
| BNB | 662 | 2 | 4% | 2% | -64% | -90% | -92% |
| XRP | 661 | 4 | 2% | 1% | -23% | -77% | -78% |
| SOL | 661 | 0 | 3% | 1% | -100% | -93% | -92% |
| BTC | 659 | 3 | 5% | 2% | -40% | -87% | -89% |
| NEAR | 656 | 3 | 6% | 3% | -40% | -65% | -66% |
| GOLD | 355 | 0 | 4% | 1% | -100% | -91% | -93% |
| SILVER | 341 | 0 | 2% | 1% | -100% | -96% | -96% |
| WTI | 326 | 2 | 3% | 1% | -34% | -94% | -96% |
| COPPER | 300 | 0 | 1% | 0% | -100% | -99% | -99% |
| PLATINUM | 271 | 0 | 0% | 0% | -100% | -100% | -100% |
| NATGAS | 265 | 2 | 3% | 2% | -30% | -94% | -92% |
| PALLADIUM | 258 | 1 | 2% | 1% | -64% | -97% | -98% |
| EURUSD | 244 | 1 | 5% | 3% | -62% | -92% | -90% |
| GBPUSD | 233 | 1 | 3% | 2% | -60% | -94% | -94% |
| USDJPY | 204 | 3 | 2% | 1% | +37% | -97% | -95% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 4423 | 20 | 4% | 2% | -47% | -89% | -88% |
| DOWN (bought NO) | 4347 | 17 | 4% | 2% | -55% | -90% | -91% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 986 | 7 | 2% | 1% | +21% | -59% | -59% |
| 0.05–0.1% | 995 | 2 | 3% | 1% | -70% | -91% | -93% |
| 0.1–0.2% | 1495 | 6 | 4% | 2% | -49% | -91% | -91% |
| 0.2–0.5% | 1764 | 8 | 6% | 3% | -50% | -87% | -87% |
| Over 0.5% | 731 | 4 | 7% | 3% | -44% | -87% | -89% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 2228 | 9 | 4% | 2% | -53% | -86% | -87% |
| Morning (6am–12pm) | 2361 | 17 | 5% | 3% | -18% | -90% | -88% |
| Afternoon (12–6pm) | 1787 | 4 | 3% | 1% | -73% | -86% | -87% |
| Evening (6pm–12am) | 2394 | 7 | 3% | 2% | -66% | -94% | -94% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 25 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,126 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/5 12:44:53 PM | BNB | UP | 7 sec | -0.050% | 1¢ | ❌ Lost | -$0.15 |
| 10/5 12:44:37 PM | ZEC | UP | 23 sec | +0.006% | 0¢ | ❌ Lost | -$0.15 |
| 10/5 12:44:37 PM | SOL | UP | 23 sec | -0.056% | 0¢ | ❌ Lost | $0.00 |
| 10/5 12:44:37 PM | PLATINUM | DOWN | 23 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/5 12:44:21 PM | ETH | UP | 39 sec | -0.025% | 0¢ | ❌ Lost | -$0.15 |
| 10/5 12:44:05 PM | XRP | UP | 55 sec | -0.087% | 1¢ | ❌ Lost | -$0.15 |
| 10/5 12:44:05 PM | SILVER | DOWN | 55 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/5 12:44:05 PM | BTC | DOWN | 55 sec | +0.047% | 1¢ | ❌ Lost | -$0.15 |
| 10/5 12:43:49 PM | DOGE | UP | 71 sec | -0.130% | 1¢ | ❌ Lost | -$0.15 |
| 10/5 12:42:30 PM | WTI | UP | 2.5 min | — | 0¢ | ❌ Lost | $0.00 |
| 10/5 12:42:14 PM | NEAR | DOWN | 2.8 min | +0.303% | 1¢ | ❌ Lost | -$0.15 |
| 10/5 12:41:26 PM | HYPE | UP | 3.6 min | -0.377% | 1¢ | ❌ Lost | $0.00 |
| 10/5 12:29:20 PM | EURUSD | DOWN | 40 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/5 12:29:04 PM | BNB | DOWN | 56 sec | +0.022% | 0¢ | ❌ Lost | -$0.15 |
| 10/5 12:29:04 PM | SOL | DOWN | 56 sec | +0.096% | 0¢ | ❌ Lost | -$0.15 |
| 10/5 12:28:48 PM | NEAR | DOWN | 72 sec | +0.271% | 1¢ | ❌ Lost | -$0.15 |
| 10/5 12:28:32 PM | WTI | UP | 88 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/5 12:28:16 PM | DOGE | DOWN | 1.7 min | +0.167% | 1¢ | ❌ Lost | -$0.15 |
| 10/5 12:28:16 PM | ETH | DOWN | 1.7 min | +0.135% | 1¢ | ❌ Lost | -$0.15 |
| 10/5 12:28:16 PM | NATGAS | DOWN | 1.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/5 12:27:44 PM | BTC | DOWN | 2.3 min | +0.114% | 0¢ | ❌ Lost | -$0.15 |
| 10/5 12:27:44 PM | XRP | DOWN | 2.3 min | +0.127% | 0¢ | ❌ Lost | $0.00 |
| 10/5 12:27:12 PM | HYPE | UP | 2.8 min | -0.238% | 5¢ | ❌ Lost | -$0.15 |
| 10/5 12:27:12 PM | ZEC | DOWN | 2.8 min | +0.414% | 1¢ | ❌ Lost | -$0.15 |
| 10/5 12:14:53 PM | DOGE | DOWN | 7 sec | +0.013% | 0¢ | ❌ Lost | $0.00 |
| 10/5 12:14:53 PM | BNB | UP | 7 sec | -0.046% | 0¢ | ❌ Lost | $0.00 |
| 10/5 12:14:53 PM | BTC | DOWN | 7 sec | +0.028% | 0¢ | ❌ Lost | $0.00 |
| 10/5 12:14:21 PM | ETH | DOWN | 39 sec | +0.050% | 1¢ | ❌ Lost | -$0.15 |
| 10/5 12:14:21 PM | PLATINUM | DOWN | 39 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/5 12:14:21 PM | NEAR | DOWN | 39 sec | +0.177% | 0¢ | ❌ Lost | $0.00 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
