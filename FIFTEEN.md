# 15-Minute 1¢ Study

*Updated Wed Oct 7, 3:28 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 743 finished bets | 1% | $32.20 | +40% | +4.33¢ | -$11.90 / $44.10 |

*Expect about **77 buys a day** (~$11.59/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 741 | $19.25 | +24% |
| 5+ min left, hold to the close | 288 | $13.25 | +31% |
| Volatility model ≥ 2%, hold to the close | 1364 | $4.05 | +2% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 11021 | 11008 | 49 (0%) | 1.07% | -$647.80 (-49%) | Hold to the close: -$647.80 (-49%) |

*In play or awaiting result: 13. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 7118 | 4.1% | 0.5% (33) | -559% | ❌ Worse |
| Momentum model | 7118 | 4.1% | 0.5% (33) | -588% | ❌ Worse |
| Mean-reversion model | 7118 | 6.7% | 0.5% (33) | -653% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 7118 | 33 | -42% | -87% | -87% | -84% |
| Volatility model ≥ 2% | 1364 | 12 | +2% | -73% | -73% | -69% |
| Volatility model ≥ 5% | 743 | 8 | +40% | -62% | -60% | -57% |
| Volatility model ≥ 10% | 463 | 6 | +92% | -44% | -45% | -40% |
| Momentum model ≥ 2% | 1213 | 10 | -0% | -73% | -75% | -72% |
| Momentum model ≥ 5% | 741 | 7 | +24% | -66% | -68% | -65% |
| Momentum model ≥ 10% | 512 | 6 | +70% | -55% | -56% | -52% |
| Mean-reversion model ≥ 2% | 2439 | 19 | -15% | -84% | -84% | -80% |
| Mean-reversion model ≥ 5% | 1650 | 15 | +1% | -81% | -81% | -75% |
| Mean-reversion model ≥ 10% | 1098 | 11 | +15% | -79% | -79% | -74% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 7315 | 4% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 2782 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 911 | 3% | 2% | 2% | 1% | 1% | 0% |
| **All** | 11008 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 49 | 0% | -$647.80 | -49% | — |
| Sell at 2¢ | 387 | 4% | -$1,191.18 | -89% | 34 sec |
| Sell at 3¢ | 258 | 2% | -$1,191.18 | -89% | 47 sec |
| Sell at 5¢ | 192 | 2% | -$1,167.00 | -87% | 56 sec |
| Sell at 10¢ | 129 | 1% | -$1,108.81 | -83% | 64 sec |
| Sell at 25¢ | 74 | 1% | -$1,004.86 | -75% | 82 sec |
| Sell at 50¢ | 49 | 0% | -$877.05 | -66% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 3 | 0 | 100% | 67% | -100% | +73% | +160% |
| 5–10 min | 285 | 4 | 11% | 4% | +32% | -82% | -86% |
| 2–5 min | 3550 | 25 | 7% | 3% | -31% | -88% | -88% |
| 1–2 min | 2912 | 12 | 3% | 2% | -56% | -94% | -93% |
| Under 1 min | 4258 | 8 | 1% | 0% | -72% | -88% | -88% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 820 | 6 | 5% | 3% | -13% | -90% | -89% |
| HYPE | 820 | 3 | 5% | 3% | -55% | -89% | -87% |
| DOGE | 815 | 2 | 3% | 1% | -69% | -92% | -92% |
| ETH | 814 | 7 | 5% | 3% | +7% | -88% | -88% |
| BNB | 813 | 3 | 4% | 2% | -55% | -91% | -92% |
| NEAR | 810 | 5 | 6% | 3% | -19% | -70% | -71% |
| SOL | 809 | 0 | 3% | 1% | -100% | -94% | -92% |
| BTC | 808 | 4 | 5% | 2% | -35% | -88% | -90% |
| XRP | 806 | 5 | 2% | 1% | -22% | -80% | -81% |
| GOLD | 464 | 0 | 4% | 1% | -100% | -92% | -94% |
| SILVER | 453 | 0 | 2% | 1% | -100% | -95% | -94% |
| WTI | 430 | 3 | 3% | 1% | -23% | -95% | -96% |
| COPPER | 397 | 0 | 1% | 1% | -100% | -99% | -99% |
| PLATINUM | 356 | 0 | 0% | 0% | -100% | -100% | -99% |
| NATGAS | 345 | 3 | 3% | 2% | -19% | -94% | -92% |
| PALLADIUM | 337 | 1 | 1% | 1% | -72% | -97% | -98% |
| EURUSD | 330 | 3 | 4% | 2% | -15% | -65% | -64% |
| GBPUSD | 311 | 1 | 3% | 2% | -70% | -95% | -95% |
| USDJPY | 270 | 3 | 1% | 1% | +4% | -97% | -96% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 5601 | 26 | 4% | 2% | -46% | -88% | -88% |
| DOWN (bought NO) | 5407 | 23 | 3% | 2% | -51% | -90% | -91% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 1205 | 8 | 2% | 1% | +15% | -65% | -64% |
| 0.05–0.1% | 1252 | 4 | 3% | 1% | -53% | -92% | -92% |
| 0.1–0.2% | 1864 | 6 | 3% | 2% | -60% | -92% | -92% |
| 0.2–0.5% | 2138 | 12 | 6% | 3% | -39% | -88% | -87% |
| Over 0.5% | 854 | 5 | 6% | 3% | -40% | -88% | -90% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 2890 | 17 | 4% | 2% | -32% | -84% | -84% |
| Morning (6am–12pm) | 2706 | 17 | 4% | 2% | -28% | -91% | -90% |
| Afternoon (12–6pm) | 2422 | 7 | 3% | 1% | -66% | -88% | -89% |
| Evening (6pm–12am) | 2990 | 8 | 3% | 1% | -69% | -95% | -94% |

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
| 10/7 3:28:33 PM | ETH | UP | 86 sec | -0.059% | — | In play | — |
| 10/7 3:28:17 PM | ZEC | UP | 1.7 min | -0.200% | — | In play | — |
| 10/7 3:28:01 PM | HYPE | UP | 2.0 min | -0.324% | — | In play | — |
| 10/7 3:27:30 PM | BNB | UP | 2.5 min | -0.093% | — | In play | — |
| 10/7 3:27:30 PM | SOL | UP | 2.5 min | -0.133% | — | In play | — |
| 10/7 3:27:14 PM | DOGE | UP | 2.8 min | -0.188% | — | In play | — |
| 10/7 3:26:11 PM | NEAR | UP | 3.8 min | -0.995% | — | In play | — |
| 10/7 3:14:52 PM | WTI | UP | 8 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/7 3:14:21 PM | BNB | UP | 38 sec | -0.019% | 1¢ | ❌ Lost | -$0.15 |
| 10/7 3:14:05 PM | HYPE | UP | 54 sec | -0.027% | 2¢ | ❌ Lost | -$0.15 |
| 10/7 3:13:49 PM | NATGAS | DOWN | 71 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/7 3:13:02 PM | ZEC | UP | 1.9 min | -0.161% | 1¢ | ❌ Lost | -$0.15 |
| 10/7 3:13:02 PM | SOL | UP | 1.9 min | -0.105% | 1¢ | ❌ Lost | -$0.15 |
| 10/7 3:13:02 PM | XRP | UP | 1.9 min | -0.134% | 1¢ | ❌ Lost | -$0.15 |
| 10/7 3:12:15 PM | DOGE | UP | 2.7 min | -0.172% | 0¢ | ❌ Lost | -$0.15 |
| 10/7 3:12:15 PM | BTC | UP | 2.7 min | -0.114% | 1¢ | ❌ Lost | -$0.15 |
| 10/7 3:11:43 PM | ETH | UP | 3.3 min | -0.104% | 1¢ | ❌ Lost | -$0.15 |
| 10/7 3:09:52 PM | NEAR | UP | 5.1 min | -1.066% | 1¢ | ❌ Lost | -$0.15 |
| 10/7 2:59:38 PM | SILVER | DOWN | 21 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/7 2:59:22 PM | GBPUSD | DOWN | 37 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/7 2:59:22 PM | NEAR | DOWN | 37 sec | -0.009% | 1¢ | ❌ Lost | -$0.15 |
| 10/7 2:59:22 PM | COPPER | DOWN | 37 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/7 2:59:06 PM | GOLD | DOWN | 53 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/7 2:59:06 PM | ZEC | DOWN | 53 sec | +0.138% | 1¢ | ❌ Lost | -$0.15 |
| 10/7 2:59:06 PM | WTI | UP | 53 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/7 2:58:50 PM | BNB | DOWN | 69 sec | +0.039% | 0¢ | ❌ Lost | -$0.15 |
| 10/7 2:58:50 PM | NATGAS | DOWN | 69 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/7 2:58:35 PM | BTC | DOWN | 84 sec | +0.064% | 1¢ | ❌ Lost | -$0.15 |
| 10/7 2:58:16 PM | PALLADIUM | UP | 1.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/7 2:58:16 PM | HYPE | DOWN | 1.7 min | +0.165% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
