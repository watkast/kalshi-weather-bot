# 15-Minute 1¢ Study

*Updated Thu Oct 1, 5:22 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (5+ min left).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| 5+ min left, hold to the close | 143 finished bets | 1% | $7.00 | +33% | +4.90¢ | $17.35 / -$10.35 |

*Expect about **37 buys a day** (~$5.55/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 292 | -$3.80 | -12% |
| Volatility model ≥ 5%, sell at 25¢ | 282 | -$6.97 | -23% |
| 5+ min left, sell at 50¢ | 143 | -$7.50 | -36% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 4776 | 4770 | 15 (0%) | 1.07% | -$373.80 (-64%) | Hold to the close: -$373.80 (-64%) |

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
| Volatility model | 2742 | 3.6% | 0.2% (6) | -695% | ❌ Worse |
| Momentum model | 2742 | 3.7% | 0.2% (6) | -750% | ❌ Worse |
| Mean-reversion model | 2742 | 6.6% | 0.2% (6) | -881% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 2742 | 6 | -72% | -85% | -87% | -84% |
| Volatility model ≥ 2% | 563 | 3 | -39% | -64% | -65% | -62% |
| Volatility model ≥ 5% | 282 | 1 | -55% | -35% | -36% | -34% |
| Volatility model ≥ 10% | 159 | 1 | -7% | +11% | +9% | +15% |
| Momentum model ≥ 2% | 507 | 2 | -53% | -62% | -65% | -62% |
| Momentum model ≥ 5% | 292 | 2 | -12% | -41% | -44% | -40% |
| Momentum model ≥ 10% | 195 | 1 | -27% | -17% | -16% | -13% |
| Mean-reversion model ≥ 2% | 1038 | 3 | -69% | -85% | -88% | -84% |
| Mean-reversion model ≥ 5% | 682 | 3 | -52% | -82% | -85% | -79% |
| Mean-reversion model ≥ 10% | 433 | 2 | -48% | -78% | -80% | -75% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 2938 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 1403 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 429 | 4% | 3% | 2% | 2% | 1% | 1% |
| **All** | 4770 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 15 | 0% | -$373.80 | -64% | — |
| Sell at 2¢ | 176 | 4% | -$524.04 | -90% | 46 sec |
| Sell at 3¢ | 106 | 2% | -$528.46 | -91% | 49 sec |
| Sell at 5¢ | 77 | 2% | -$519.75 | -89% | 66 sec |
| Sell at 10¢ | 56 | 1% | -$482.44 | -83% | 81 sec |
| Sell at 25¢ | 26 | 1% | -$455.74 | -78% | 1.6 min |
| Sell at 50¢ | 13 | 0% | -$426.05 | -73% | 2.1 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 3 | 0 | 100% | 67% | -100% | +73% | +160% |
| 5–10 min | 140 | 2 | 13% | 3% | +36% | -77% | -89% |
| 2–5 min | 1573 | 7 | 7% | 3% | -57% | -88% | -89% |
| 1–2 min | 1250 | 4 | 3% | 2% | -66% | -94% | -93% |
| Under 1 min | 1804 | 2 | 1% | 0% | -84% | -90% | -91% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| DOGE | 332 | 1 | 4% | 1% | -61% | -90% | -92% |
| ETH | 329 | 2 | 5% | 3% | -25% | -88% | -85% |
| ZEC | 327 | 1 | 5% | 2% | -64% | -89% | -94% |
| BNB | 327 | 0 | 4% | 1% | -100% | -91% | -94% |
| HYPE | 326 | 1 | 5% | 3% | -63% | -90% | -88% |
| BTC | 325 | 0 | 6% | 3% | -100% | -85% | -88% |
| NEAR | 324 | 0 | 5% | 2% | -100% | -87% | -91% |
| XRP | 324 | 3 | 2% | 1% | +20% | -56% | -56% |
| SOL | 324 | 0 | 3% | 1% | -100% | -92% | -92% |
| GOLD | 241 | 0 | 4% | 1% | -100% | -91% | -93% |
| SILVER | 223 | 0 | 2% | 1% | -100% | -96% | -96% |
| WTI | 216 | 1 | 3% | 1% | -52% | -95% | -96% |
| COPPER | 200 | 0 | 1% | 0% | -100% | -98% | -99% |
| NATGAS | 183 | 1 | 4% | 2% | -49% | -93% | -91% |
| PLATINUM | 175 | 0 | 0% | 0% | -100% | -100% | -100% |
| PALLADIUM | 165 | 0 | 2% | 1% | -100% | -97% | -98% |
| EURUSD | 152 | 1 | 4% | 2% | -39% | -93% | -93% |
| GBPUSD | 151 | 1 | 5% | 2% | -38% | -92% | -93% |
| USDJPY | 126 | 3 | 3% | 2% | +122% | -94% | -92% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 2431 | 9 | 4% | 2% | -58% | -92% | -92% |
| DOWN (bought NO) | 2339 | 6 | 4% | 1% | -71% | -87% | -89% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 343 | 1 | 1% | 1% | -45% | -41% | -41% |
| 0.05–0.1% | 413 | 0 | 2% | 0% | -100% | -93% | -95% |
| 0.1–0.2% | 713 | 1 | 4% | 1% | -82% | -91% | -92% |
| 0.2–0.5% | 991 | 2 | 6% | 3% | -78% | -88% | -89% |
| Over 0.5% | 477 | 4 | 7% | 2% | -13% | -87% | -90% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 1116 | 2 | 4% | 1% | -80% | -92% | -94% |
| Morning (6am–12pm) | 1285 | 7 | 4% | 2% | -38% | -91% | -91% |
| Afternoon (12–6pm) | 1056 | 2 | 3% | 1% | -78% | -82% | -85% |
| Evening (6pm–12am) | 1313 | 4 | 4% | 2% | -65% | -92% | -92% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 24 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 3,192 |
| Time from buy to best bounce (bounced bets) | 50 sec |
| Price snapshots per bet | 43 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/1 5:14:41 PM | COPPER | DOWN | 19 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/1 5:14:39 PM | ZEC | DOWN | 21 sec | +0.024% | 0¢ | ❌ Lost | $0.00 |
| 10/1 5:14:23 PM | WTI | UP | 37 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/1 5:13:50 PM | HYPE | UP | 70 sec | -0.117% | 0¢ | ❌ Lost | -$0.15 |
| 10/1 5:13:48 PM | PLATINUM | UP | 72 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/1 5:13:46 PM | DOGE | UP | 74 sec | -0.143% | 0¢ | ❌ Lost | $0.00 |
| 10/1 5:13:32 PM | SOL | UP | 88 sec | -0.163% | 0¢ | ❌ Lost | -$0.15 |
| 10/1 5:13:30 PM | NEAR | UP | 1.5 min | -0.467% | 0¢ | ❌ Lost | $0.00 |
| 10/1 5:13:24 PM | BTC | UP | 1.6 min | -0.087% | 0¢ | ❌ Lost | -$0.15 |
| 10/1 5:13:16 PM | XRP | UP | 1.7 min | -0.248% | 1¢ | ❌ Lost | -$0.15 |
| 10/1 5:12:08 PM | ETH | UP | 2.9 min | -0.105% | 1¢ | ❌ Lost | -$0.15 |
| 10/1 5:11:31 PM | BNB | UP | 3.5 min | -0.128% | 1¢ | ❌ Lost | -$0.15 |
| 10/1 4:59:25 PM | USDJPY | UP | 34 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/1 4:59:23 PM | NEAR | DOWN | 36 sec | +0.232% | 0¢ | ❌ Lost | $0.00 |
| 10/1 4:59:23 PM | BNB | DOWN | 36 sec | +0.022% | 0¢ | ❌ Lost | $0.00 |
| 10/1 4:59:17 PM | EURUSD | DOWN | 42 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/1 4:59:07 PM | SOL | DOWN | 52 sec | +0.120% | 0¢ | ❌ Lost | $0.00 |
| 10/1 4:59:06 PM | ETH | DOWN | 54 sec | +0.063% | 1¢ | ❌ Lost | -$0.15 |
| 10/1 4:59:06 PM | XRP | DOWN | 54 sec | +0.141% | 0¢ | ❌ Lost | -$0.15 |
| 10/1 4:59:00 PM | COPPER | DOWN | 60 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/1 4:58:52 PM | GOLD | DOWN | 68 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/1 4:58:52 PM | BTC | DOWN | 68 sec | +0.063% | 0¢ | ❌ Lost | $0.00 |
| 10/1 4:58:48 PM | HYPE | DOWN | 72 sec | +0.219% | 0¢ | ❌ Lost | $0.00 |
| 10/1 4:58:40 PM | DOGE | DOWN | 80 sec | +0.147% | 0¢ | ❌ Lost | $0.00 |
| 10/1 4:58:18 PM | SILVER | DOWN | 1.7 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/1 4:56:56 PM | ZEC | DOWN | 3.1 min | +0.385% | 1¢ | ❌ Lost | -$0.15 |
| 10/1 4:44:53 PM | BTC | UP | 7 sec | -0.037% | 0¢ | ❌ Lost | $0.00 |
| 10/1 4:44:45 PM | SOL | DOWN | 15 sec | -0.005% | 0¢ | ❌ Lost | $0.00 |
| 10/1 4:44:43 PM | ETH | DOWN | 17 sec | +0.051% | 0¢ | ❌ Lost | $0.00 |
| 10/1 4:44:31 PM | EURUSD | DOWN | 29 sec | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
