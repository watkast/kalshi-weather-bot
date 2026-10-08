# 15-Minute 1¢ Study

*Updated Wed Oct 7, 6:54 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 753 finished bets | 1% | $31.00 | +38% | +4.12¢ | -$12.65 / $43.65 |

*Expect about **77 buys a day** (~$11.57/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 751 | $18.05 | +23% |
| 5+ min left, hold to the close | 290 | $12.95 | +30% |
| Volatility model ≥ 2%, hold to the close | 1383 | $1.80 | +1% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 11197 | 11188 | 49 (0%) | 1.07% | -$669.40 (-49%) | Hold to the close: -$669.40 (-49%) |

*In play or awaiting result: 9. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 7230 | 4.1% | 0.5% (33) | -563% | ❌ Worse |
| Momentum model | 7230 | 4.1% | 0.5% (33) | -594% | ❌ Worse |
| Mean-reversion model | 7230 | 6.7% | 0.5% (33) | -657% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 7230 | 33 | -43% | -87% | -87% | -84% |
| Volatility model ≥ 2% | 1383 | 12 | +1% | -73% | -73% | -69% |
| Volatility model ≥ 5% | 753 | 8 | +38% | -62% | -61% | -58% |
| Volatility model ≥ 10% | 472 | 6 | +87% | -46% | -46% | -41% |
| Momentum model ≥ 2% | 1229 | 10 | -2% | -74% | -75% | -72% |
| Momentum model ≥ 5% | 751 | 7 | +23% | -67% | -68% | -65% |
| Momentum model ≥ 10% | 520 | 6 | +66% | -56% | -57% | -53% |
| Mean-reversion model ≥ 2% | 2474 | 19 | -17% | -84% | -84% | -80% |
| Mean-reversion model ≥ 5% | 1675 | 15 | -0% | -81% | -81% | -75% |
| Mean-reversion model ≥ 10% | 1112 | 11 | +14% | -80% | -79% | -74% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 7427 | 4% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 2825 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 936 | 3% | 2% | 2% | 1% | 1% | 0% |
| **All** | 11188 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 49 | 0% | -$669.40 | -49% | — |
| Sell at 2¢ | 392 | 4% | -$1,211.48 | -89% | 34 sec |
| Sell at 3¢ | 261 | 2% | -$1,211.61 | -89% | 47 sec |
| Sell at 5¢ | 195 | 2% | -$1,186.65 | -88% | 51 sec |
| Sell at 10¢ | 130 | 1% | -$1,129.10 | -83% | 64 sec |
| Sell at 25¢ | 75 | 1% | -$1,023.15 | -75% | 82 sec |
| Sell at 50¢ | 49 | 0% | -$898.65 | -66% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 3 | 0 | 100% | 67% | -100% | +73% | +160% |
| 5–10 min | 287 | 4 | 10% | 3% | +31% | -82% | -86% |
| 2–5 min | 3605 | 25 | 7% | 3% | -32% | -88% | -88% |
| 1–2 min | 2954 | 12 | 3% | 2% | -56% | -94% | -93% |
| Under 1 min | 4339 | 8 | 1% | 0% | -73% | -88% | -88% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 832 | 6 | 5% | 3% | -14% | -90% | -90% |
| HYPE | 832 | 3 | 5% | 3% | -56% | -89% | -87% |
| DOGE | 828 | 2 | 3% | 1% | -69% | -92% | -92% |
| ETH | 826 | 7 | 5% | 3% | +6% | -89% | -88% |
| BNB | 826 | 3 | 4% | 2% | -56% | -90% | -91% |
| NEAR | 822 | 5 | 6% | 3% | -20% | -70% | -71% |
| BTC | 821 | 4 | 5% | 2% | -36% | -88% | -90% |
| SOL | 821 | 0 | 3% | 1% | -100% | -93% | -92% |
| XRP | 819 | 5 | 2% | 1% | -23% | -81% | -81% |
| GOLD | 472 | 0 | 4% | 1% | -100% | -92% | -94% |
| SILVER | 461 | 0 | 2% | 1% | -100% | -95% | -94% |
| WTI | 438 | 3 | 3% | 1% | -25% | -95% | -97% |
| COPPER | 403 | 0 | 1% | 0% | -100% | -99% | -99% |
| PLATINUM | 362 | 0 | 0% | 0% | -100% | -100% | -99% |
| NATGAS | 350 | 3 | 3% | 2% | -20% | -95% | -93% |
| PALLADIUM | 339 | 1 | 1% | 1% | -72% | -97% | -98% |
| EURUSD | 336 | 3 | 4% | 2% | -17% | -66% | -64% |
| GBPUSD | 317 | 1 | 3% | 2% | -71% | -95% | -95% |
| USDJPY | 278 | 3 | 1% | 1% | +1% | -98% | -96% |
| USDCAD | 3 | 0 | 0% | 0% | -100% | -100% | -100% |
| AUDUSD | 2 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 5679 | 26 | 4% | 2% | -47% | -88% | -88% |
| DOWN (bought NO) | 5509 | 23 | 3% | 2% | -52% | -91% | -91% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 1229 | 8 | 2% | 1% | +12% | -66% | -65% |
| 0.05–0.1% | 1277 | 4 | 3% | 1% | -54% | -91% | -92% |
| 0.1–0.2% | 1888 | 6 | 4% | 2% | -60% | -92% | -92% |
| 0.2–0.5% | 2168 | 12 | 6% | 3% | -39% | -89% | -88% |
| Over 0.5% | 863 | 5 | 6% | 3% | -41% | -88% | -90% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 2890 | 17 | 4% | 2% | -32% | -84% | -84% |
| Morning (6am–12pm) | 2706 | 17 | 4% | 2% | -28% | -91% | -90% |
| Afternoon (12–6pm) | 2560 | 7 | 3% | 1% | -68% | -88% | -89% |
| Evening (6pm–12am) | 3032 | 8 | 3% | 1% | -70% | -94% | -94% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 25 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,084 |
| Time from buy to best bounce (bounced bets) | 49 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/7 6:54:19 PM | PLATINUM | DOWN | 5.7 min | — | — | In play | — |
| 10/7 6:53:47 PM | SILVER | DOWN | 6.2 min | — | — | In play | — |
| 10/7 6:53:47 PM | HYPE | DOWN | 6.2 min | +0.542% | — | In play | — |
| 10/7 6:44:53 PM | BTC | DOWN | 7 sec | -0.012% | 0¢ | ❌ Lost | -$0.15 |
| 10/7 6:44:38 PM | PLATINUM | UP | 22 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/7 6:44:38 PM | BNB | UP | 22 sec | -0.050% | 0¢ | ❌ Lost | $0.00 |
| 10/7 6:44:22 PM | XRP | UP | 38 sec | -0.077% | 1¢ | ❌ Lost | -$0.15 |
| 10/7 6:44:22 PM | GBPUSD | UP | 38 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/7 6:43:50 PM | COPPER | UP | 70 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/7 6:43:34 PM | NEAR | DOWN | 85 sec | +0.278% | 0¢ | ❌ Lost | -$0.15 |
| 10/7 6:43:18 PM | DOGE | UP | 1.7 min | -0.106% | 1¢ | ❌ Lost | -$0.15 |
| 10/7 6:42:46 PM | SOL | UP | 2.2 min | -0.118% | 9¢ | ❌ Lost | -$0.15 |
| 10/7 6:42:46 PM | WTI | DOWN | 2.2 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/7 6:42:31 PM | USDJPY | UP | 2.5 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/7 6:42:15 PM | ZEC | UP | 2.7 min | -0.401% | 0¢ | ❌ Lost | $0.00 |
| 10/7 6:29:54 PM | USDCAD | DOWN | 5 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/7 6:29:39 PM | BTC | DOWN | 20 sec | -0.003% | 1¢ | ❌ Lost | -$0.15 |
| 10/7 6:29:39 PM | COPPER | UP | 20 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/7 6:29:39 PM | WTI | DOWN | 20 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/7 6:29:39 PM | GOLD | UP | 20 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/7 6:29:23 PM | XRP | DOWN | 36 sec | +0.000% | 0¢ | ❌ Lost | -$0.15 |
| 10/7 6:29:23 PM | USDJPY | UP | 36 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/7 6:29:07 PM | SOL | DOWN | 52 sec | +0.079% | 0¢ | ❌ Lost | $0.00 |
| 10/7 6:29:07 PM | ETH | DOWN | 52 sec | +0.062% | 1¢ | ❌ Lost | -$0.15 |
| 10/7 6:29:07 PM | BNB | DOWN | 52 sec | -0.015% | 0¢ | ❌ Lost | -$0.15 |
| 10/7 6:28:51 PM | AUDUSD | UP | 69 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/7 6:28:51 PM | NEAR | UP | 69 sec | -0.541% | 1¢ | ❌ Lost | -$0.15 |
| 10/7 6:28:20 PM | HYPE | UP | 1.6 min | -0.153% | 1¢ | ❌ Lost | -$0.15 |
| 10/7 6:28:04 PM | PLATINUM | UP | 1.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/7 6:28:04 PM | ZEC | UP | 1.9 min | -0.294% | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
