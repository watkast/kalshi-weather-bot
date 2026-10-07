# 15-Minute 1¢ Study

*Updated Wed Oct 7, 12:11 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 717 finished bets | 1% | $35.05 | +46% | +4.89¢ | -$10.70 / $45.75 |

*Expect about **80 buys a day** (~$11.98/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 714 | $22.40 | +30% |
| 5+ min left, hold to the close | 262 | $17.15 | +44% |
| Mean-reversion model ≥ 5%, hold to the close | 1566 | $13.05 | +7% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 10346 | 10340 | 47 (0%) | 1.07% | -$591.35 (-47%) | Hold to the close: -$591.35 (-47%) |

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
| Volatility model | 6717 | 4.2% | 0.5% (33) | -565% | ❌ Worse |
| Momentum model | 6717 | 4.2% | 0.5% (33) | -594% | ❌ Worse |
| Mean-reversion model | 6717 | 6.8% | 0.5% (33) | -653% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 6717 | 33 | -38% | -86% | -87% | -84% |
| Volatility model ≥ 2% | 1314 | 12 | +6% | -73% | -73% | -68% |
| Volatility model ≥ 5% | 717 | 8 | +46% | -62% | -61% | -57% |
| Volatility model ≥ 10% | 448 | 6 | +99% | -45% | -47% | -41% |
| Momentum model ≥ 2% | 1167 | 10 | +4% | -73% | -75% | -73% |
| Momentum model ≥ 5% | 714 | 7 | +30% | -66% | -68% | -65% |
| Momentum model ≥ 10% | 497 | 6 | +74% | -55% | -56% | -53% |
| Mean-reversion model ≥ 2% | 2305 | 19 | -10% | -84% | -84% | -79% |
| Mean-reversion model ≥ 5% | 1566 | 15 | +7% | -81% | -81% | -75% |
| Mean-reversion model ≥ 10% | 1038 | 11 | +23% | -79% | -79% | -74% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 6914 | 4% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 2590 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 836 | 3% | 2% | 2% | 1% | 1% | 0% |
| **All** | 10340 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 47 | 0% | -$591.35 | -47% | — |
| Sell at 2¢ | 367 | 4% | -$1,125.93 | -90% | 33 sec |
| Sell at 3¢ | 243 | 2% | -$1,126.58 | -90% | 47 sec |
| Sell at 5¢ | 182 | 2% | -$1,103.05 | -88% | 50 sec |
| Sell at 10¢ | 123 | 1% | -$1,046.22 | -84% | 65 sec |
| Sell at 25¢ | 71 | 1% | -$944.34 | -76% | 82 sec |
| Sell at 50¢ | 47 | 0% | -$820.10 | -66% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 3 | 0 | 100% | 67% | -100% | +73% | +160% |
| 5–10 min | 259 | 4 | 10% | 3% | +46% | -82% | -88% |
| 2–5 min | 3320 | 25 | 7% | 3% | -27% | -88% | -88% |
| 1–2 min | 2709 | 11 | 3% | 2% | -56% | -94% | -94% |
| Under 1 min | 4049 | 7 | 1% | 0% | -74% | -91% | -91% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 781 | 6 | 5% | 3% | -8% | -90% | -89% |
| HYPE | 774 | 3 | 5% | 3% | -52% | -89% | -87% |
| DOGE | 770 | 2 | 3% | 1% | -67% | -92% | -92% |
| ETH | 769 | 7 | 5% | 3% | +14% | -88% | -87% |
| BNB | 767 | 3 | 4% | 2% | -53% | -91% | -93% |
| NEAR | 765 | 5 | 6% | 3% | -14% | -69% | -69% |
| SOL | 764 | 0 | 3% | 1% | -100% | -93% | -92% |
| BTC | 762 | 4 | 5% | 2% | -31% | -87% | -89% |
| XRP | 762 | 5 | 2% | 1% | -17% | -80% | -80% |
| GOLD | 433 | 0 | 3% | 1% | -100% | -92% | -95% |
| SILVER | 421 | 0 | 2% | 1% | -100% | -95% | -95% |
| WTI | 400 | 3 | 3% | 1% | -18% | -94% | -96% |
| COPPER | 371 | 0 | 1% | 1% | -100% | -99% | -99% |
| PLATINUM | 332 | 0 | 0% | 0% | -100% | -99% | -99% |
| PALLADIUM | 317 | 1 | 2% | 1% | -71% | -97% | -98% |
| NATGAS | 316 | 3 | 3% | 2% | -11% | -95% | -93% |
| EURUSD | 303 | 1 | 4% | 2% | -69% | -94% | -92% |
| GBPUSD | 287 | 1 | 3% | 2% | -67% | -95% | -95% |
| USDJPY | 246 | 3 | 2% | 1% | +14% | -97% | -96% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 5226 | 25 | 4% | 2% | -44% | -90% | -89% |
| DOWN (bought NO) | 5114 | 22 | 3% | 2% | -50% | -90% | -91% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 1150 | 8 | 2% | 1% | +19% | -65% | -64% |
| 0.05–0.1% | 1202 | 4 | 3% | 1% | -51% | -92% | -93% |
| 0.1–0.2% | 1744 | 6 | 4% | 2% | -56% | -92% | -92% |
| 0.2–0.5% | 2013 | 12 | 6% | 3% | -35% | -88% | -87% |
| Over 0.5% | 803 | 5 | 6% | 3% | -36% | -88% | -89% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 2570 | 15 | 4% | 2% | -32% | -87% | -88% |
| Morning (6am–12pm) | 2536 | 17 | 5% | 3% | -24% | -90% | -89% |
| Afternoon (12–6pm) | 2244 | 7 | 3% | 1% | -63% | -88% | -89% |
| Evening (6pm–12am) | 2990 | 8 | 3% | 1% | -69% | -95% | -94% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 25 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,056 |
| Time from buy to best bounce (bounced bets) | 49 sec |
| Price snapshots per bet | 41 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/6 11:59:27 PM | NATGAS | DOWN | 32 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/6 11:59:11 PM | COPPER | UP | 48 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/6 11:59:11 PM | PALLADIUM | UP | 48 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/6 11:58:55 PM | ZEC | DOWN | 64 sec | +0.221% | 0¢ | ❌ Lost | -$0.15 |
| 10/6 11:58:40 PM | BTC | DOWN | 80 sec | +0.086% | 1¢ | ❌ Lost | -$0.15 |
| 10/6 11:58:08 PM | SILVER | UP | 1.9 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/6 11:57:52 PM | PLATINUM | UP | 2.1 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/6 11:57:52 PM | ETH | DOWN | 2.1 min | +0.088% | 1¢ | ❌ Lost | -$0.15 |
| 10/6 11:57:36 PM | SOL | DOWN | 2.4 min | +0.102% | 1¢ | ❌ Lost | -$0.15 |
| 10/6 11:57:36 PM | WTI | UP | 2.4 min | — | 70¢ | ✅ Won | $13.85 |
| 10/6 11:57:20 PM | GOLD | UP | 2.6 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/6 11:57:04 PM | XRP | DOWN | 2.9 min | +0.197% | 1¢ | ❌ Lost | -$0.15 |
| 10/6 11:56:33 PM | BNB | DOWN | 3.5 min | +0.098% | 1¢ | ❌ Lost | -$0.15 |
| 10/6 11:56:33 PM | HYPE | DOWN | 3.5 min | +0.220% | 1¢ | ❌ Lost | -$0.15 |
| 10/6 11:55:29 PM | DOGE | DOWN | 4.5 min | +0.366% | 1¢ | ❌ Lost | -$0.15 |
| 10/6 11:55:13 PM | NEAR | DOWN | 4.8 min | +0.720% | 1¢ | ❌ Lost | -$0.15 |
| 10/6 11:44:47 PM | USDJPY | UP | 12 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/6 11:44:47 PM | BTC | DOWN | 12 sec | +0.027% | 0¢ | ❌ Lost | $0.00 |
| 10/6 11:44:31 PM | PLATINUM | DOWN | 28 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/6 11:44:31 PM | HYPE | DOWN | 28 sec | +0.025% | 0¢ | ❌ Lost | $0.00 |
| 10/6 11:44:31 PM | ZEC | UP | 28 sec | -0.114% | 0¢ | ❌ Lost | $0.00 |
| 10/6 11:44:15 PM | COPPER | DOWN | 44 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/6 11:44:15 PM | SOL | DOWN | 44 sec | +0.057% | 1¢ | ❌ Lost | -$0.15 |
| 10/6 11:44:15 PM | BNB | DOWN | 44 sec | -0.005% | 0¢ | ❌ Lost | -$0.15 |
| 10/6 11:44:15 PM | EURUSD | DOWN | 44 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/6 11:43:27 PM | GBPUSD | DOWN | 1.5 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/6 11:43:27 PM | GOLD | DOWN | 1.5 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/6 11:42:55 PM | ETH | DOWN | 2.1 min | +0.087% | 2¢ | ❌ Lost | -$0.15 |
| 10/6 11:42:22 PM | NEAR | DOWN | 2.6 min | +0.279% | 1¢ | ❌ Lost | -$0.15 |
| 10/6 11:29:57 PM | WTI | DOWN | 2 sec | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
