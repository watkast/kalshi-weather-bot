# 15-Minute 1¢ Study

*Updated Tue Oct 6, 4:18 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 679 finished bets | 1% | $39.40 | +54% | +5.80¢ | -$8.90 / $48.30 |

*Expect about **78 buys a day** (~$11.77/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 679 | $26.15 | +36% |
| Mean-reversion model ≥ 5%, hold to the close | 1493 | $22.35 | +12% |
| 5+ min left, hold to the close | 251 | $18.80 | +51% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 9898 | 9892 | 46 (0%) | 1.07% | -$549.40 (-46%) | Hold to the close: -$549.40 (-46%) |

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
| Volatility model | 6451 | 4.1% | 0.5% (33) | -545% | ❌ Worse |
| Momentum model | 6451 | 4.2% | 0.5% (33) | -573% | ❌ Worse |
| Mean-reversion model | 6451 | 6.8% | 0.5% (33) | -628% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 6451 | 33 | -35% | -86% | -86% | -83% |
| Volatility model ≥ 2% | 1254 | 12 | +11% | -72% | -72% | -67% |
| Volatility model ≥ 5% | 679 | 8 | +54% | -60% | -59% | -56% |
| Volatility model ≥ 10% | 420 | 6 | +115% | -42% | -43% | -38% |
| Momentum model ≥ 2% | 1120 | 10 | +8% | -73% | -74% | -72% |
| Momentum model ≥ 5% | 679 | 7 | +36% | -65% | -67% | -64% |
| Momentum model ≥ 10% | 470 | 6 | +85% | -53% | -54% | -50% |
| Mean-reversion model ≥ 2% | 2213 | 19 | -6% | -83% | -84% | -79% |
| Mean-reversion model ≥ 5% | 1493 | 15 | +12% | -80% | -80% | -74% |
| Mean-reversion model ≥ 10% | 984 | 11 | +30% | -79% | -79% | -73% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 6648 | 4% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 2450 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 794 | 3% | 2% | 2% | 1% | 1% | 0% |
| **All** | 9892 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 46 | 0% | -$549.40 | -46% | — |
| Sell at 2¢ | 360 | 4% | -$1,071.80 | -90% | 33 sec |
| Sell at 3¢ | 237 | 2% | -$1,072.97 | -90% | 47 sec |
| Sell at 5¢ | 177 | 2% | -$1,050.35 | -88% | 50 sec |
| Sell at 10¢ | 121 | 1% | -$992.89 | -83% | 65 sec |
| Sell at 25¢ | 70 | 1% | -$891.70 | -75% | 82 sec |
| Sell at 50¢ | 46 | 0% | -$770.90 | -65% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 3 | 0 | 100% | 67% | -100% | +73% | +160% |
| 5–10 min | 248 | 4 | 10% | 4% | +52% | -82% | -87% |
| 2–5 min | 3186 | 24 | 7% | 3% | -27% | -87% | -87% |
| 1–2 min | 2606 | 11 | 3% | 2% | -54% | -94% | -93% |
| Under 1 min | 3849 | 7 | 1% | 0% | -73% | -90% | -90% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 753 | 6 | 5% | 3% | -4% | -89% | -89% |
| HYPE | 744 | 3 | 5% | 3% | -50% | -89% | -87% |
| DOGE | 742 | 2 | 4% | 1% | -66% | -92% | -91% |
| ETH | 739 | 7 | 5% | 3% | +19% | -87% | -87% |
| BNB | 737 | 3 | 4% | 2% | -51% | -91% | -92% |
| NEAR | 734 | 5 | 6% | 3% | -10% | -67% | -68% |
| SOL | 734 | 0 | 3% | 1% | -100% | -93% | -92% |
| BTC | 733 | 4 | 5% | 3% | -28% | -87% | -89% |
| XRP | 732 | 5 | 2% | 1% | -14% | -79% | -79% |
| GOLD | 411 | 0 | 4% | 1% | -100% | -92% | -94% |
| SILVER | 395 | 0 | 2% | 1% | -100% | -96% | -96% |
| WTI | 377 | 2 | 3% | 1% | -42% | -95% | -97% |
| COPPER | 353 | 0 | 1% | 0% | -100% | -99% | -99% |
| PLATINUM | 312 | 0 | 0% | 0% | -100% | -99% | -99% |
| NATGAS | 304 | 3 | 3% | 2% | -8% | -94% | -92% |
| PALLADIUM | 298 | 1 | 2% | 1% | -69% | -97% | -98% |
| EURUSD | 286 | 1 | 4% | 2% | -67% | -93% | -92% |
| GBPUSD | 275 | 1 | 3% | 2% | -66% | -94% | -94% |
| USDJPY | 233 | 3 | 2% | 1% | +20% | -97% | -96% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 4986 | 24 | 4% | 2% | -44% | -89% | -89% |
| DOWN (bought NO) | 4906 | 22 | 3% | 2% | -48% | -90% | -91% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 1099 | 8 | 2% | 1% | +25% | -63% | -62% |
| 0.05–0.1% | 1137 | 4 | 3% | 1% | -48% | -91% | -92% |
| 0.1–0.2% | 1680 | 6 | 4% | 2% | -55% | -91% | -92% |
| 0.2–0.5% | 1952 | 12 | 6% | 3% | -32% | -88% | -87% |
| Over 0.5% | 778 | 5 | 7% | 3% | -34% | -87% | -89% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 2570 | 15 | 4% | 2% | -32% | -87% | -88% |
| Morning (6am–12pm) | 2536 | 17 | 5% | 3% | -24% | -90% | -89% |
| Afternoon (12–6pm) | 2150 | 7 | 3% | 1% | -61% | -87% | -88% |
| Evening (6pm–12am) | 2636 | 7 | 3% | 1% | -69% | -94% | -94% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 25 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,056 |
| Time from buy to best bounce (bounced bets) | 49 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/6 4:14:50 PM | WTI | DOWN | 10 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/6 4:14:50 PM | XRP | DOWN | 10 sec | -0.047% | 0¢ | ❌ Lost | -$0.15 |
| 10/6 4:14:34 PM | ETH | UP | 26 sec | -0.052% | 0¢ | ❌ Lost | -$0.15 |
| 10/6 4:14:34 PM | BTC | UP | 26 sec | -0.037% | 0¢ | ❌ Lost | $0.00 |
| 10/6 4:14:34 PM | USDJPY | DOWN | 26 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/6 4:14:34 PM | NATGAS | UP | 26 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/6 4:13:44 PM | GBPUSD | DOWN | 76 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/6 4:13:12 PM | NEAR | UP | 1.8 min | -0.454% | 1¢ | ❌ Lost | -$0.15 |
| 10/6 4:12:41 PM | BNB | DOWN | 2.3 min | +0.046% | 1¢ | ❌ Lost | -$0.15 |
| 10/6 4:12:25 PM | ZEC | DOWN | 2.6 min | +0.365% | 0¢ | ❌ Lost | -$0.15 |
| 10/6 4:10:17 PM | HYPE | DOWN | 4.7 min | +0.236% | 2¢ | ❌ Lost | -$0.15 |
| 10/6 4:10:01 PM | SOL | DOWN | 5.0 min | +0.356% | 1¢ | ❌ Lost | -$0.15 |
| 10/6 3:59:30 PM | BNB | DOWN | 29 sec | -0.004% | 0¢ | ❌ Lost | $0.00 |
| 10/6 3:59:30 PM | HYPE | UP | 29 sec | -0.073% | 0¢ | ❌ Lost | $0.00 |
| 10/6 3:59:14 PM | ETH | DOWN | 45 sec | +0.044% | 0¢ | ❌ Lost | -$0.15 |
| 10/6 3:59:14 PM | BTC | DOWN | 45 sec | +0.026% | 1¢ | ❌ Lost | -$0.15 |
| 10/6 3:59:14 PM | DOGE | UP | 45 sec | -0.123% | 1¢ | ❌ Lost | -$0.15 |
| 10/6 3:59:14 PM | SOL | UP | 45 sec | -0.117% | 0¢ | ❌ Lost | $0.00 |
| 10/6 3:57:55 PM | NEAR | UP | 2.1 min | -0.453% | 1¢ | ❌ Lost | -$0.15 |
| 10/6 3:44:50 PM | WTI | DOWN | 10 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/6 3:44:50 PM | USDJPY | UP | 10 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/6 3:44:34 PM | EURUSD | DOWN | 26 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/6 3:44:01 PM | GBPUSD | DOWN | 58 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/6 3:44:01 PM | BTC | DOWN | 58 sec | +0.022% | 0¢ | ❌ Lost | -$0.15 |
| 10/6 3:43:27 PM | BNB | UP | 1.5 min | -0.092% | 1¢ | ❌ Lost | -$0.15 |
| 10/6 3:43:27 PM | DOGE | UP | 1.5 min | -0.135% | 1¢ | ❌ Lost | -$0.15 |
| 10/6 3:42:41 PM | NEAR | UP | 2.3 min | -0.451% | 1¢ | ❌ Lost | -$0.15 |
| 10/6 3:42:41 PM | SOL | DOWN | 2.3 min | +0.168% | 1¢ | ❌ Lost | -$0.15 |
| 10/6 3:42:25 PM | HYPE | UP | 2.6 min | -0.238% | 1¢ | ❌ Lost | -$0.15 |
| 10/6 3:42:09 PM | ZEC | DOWN | 2.8 min | +0.310% | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
