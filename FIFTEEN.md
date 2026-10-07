# 15-Minute 1¢ Study

*Updated Wed Oct 7, 5:33 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 746 finished bets | 1% | $31.75 | +40% | +4.26¢ | -$12.20 / $43.95 |

*Expect about **77 buys a day** (~$11.53/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 745 | $18.80 | +24% |
| 5+ min left, hold to the close | 289 | $13.10 | +31% |
| Volatility model ≥ 2%, hold to the close | 1373 | $3.00 | +2% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 11116 | 11101 | 49 (0%) | 1.07% | -$658.90 (-49%) | Hold to the close: -$658.90 (-49%) |

*In play or awaiting result: 15. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 7180 | 4.0% | 0.5% (33) | -558% | ❌ Worse |
| Momentum model | 7180 | 4.1% | 0.5% (33) | -587% | ❌ Worse |
| Mean-reversion model | 7180 | 6.7% | 0.5% (33) | -652% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 7180 | 33 | -42% | -87% | -87% | -84% |
| Volatility model ≥ 2% | 1373 | 12 | +2% | -73% | -73% | -69% |
| Volatility model ≥ 5% | 746 | 8 | +40% | -62% | -61% | -57% |
| Volatility model ≥ 10% | 465 | 6 | +90% | -45% | -45% | -40% |
| Momentum model ≥ 2% | 1220 | 10 | -1% | -73% | -75% | -72% |
| Momentum model ≥ 5% | 745 | 7 | +24% | -66% | -68% | -65% |
| Momentum model ≥ 10% | 514 | 6 | +69% | -55% | -56% | -52% |
| Mean-reversion model ≥ 2% | 2456 | 19 | -16% | -84% | -84% | -80% |
| Mean-reversion model ≥ 5% | 1662 | 15 | +0% | -81% | -81% | -75% |
| Mean-reversion model ≥ 10% | 1103 | 11 | +15% | -79% | -79% | -74% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 7377 | 4% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 2803 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 921 | 3% | 2% | 2% | 1% | 1% | 0% |
| **All** | 11101 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 49 | 0% | -$658.90 | -49% | — |
| Sell at 2¢ | 389 | 4% | -$1,201.76 | -89% | 34 sec |
| Sell at 3¢ | 259 | 2% | -$1,201.89 | -89% | 47 sec |
| Sell at 5¢ | 193 | 2% | -$1,177.45 | -88% | 60 sec |
| Sell at 10¢ | 129 | 1% | -$1,119.91 | -83% | 64 sec |
| Sell at 25¢ | 74 | 1% | -$1,015.96 | -76% | 82 sec |
| Sell at 50¢ | 49 | 0% | -$888.15 | -66% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 3 | 0 | 100% | 67% | -100% | +73% | +160% |
| 5–10 min | 286 | 4 | 10% | 3% | +32% | -82% | -86% |
| 2–5 min | 3581 | 25 | 7% | 3% | -32% | -88% | -88% |
| 1–2 min | 2933 | 12 | 3% | 2% | -56% | -94% | -93% |
| Under 1 min | 4298 | 8 | 1% | 0% | -73% | -88% | -88% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 827 | 6 | 5% | 3% | -14% | -90% | -90% |
| HYPE | 827 | 3 | 5% | 3% | -56% | -89% | -87% |
| DOGE | 822 | 2 | 3% | 1% | -69% | -92% | -92% |
| ETH | 821 | 7 | 5% | 3% | +6% | -88% | -88% |
| BNB | 820 | 3 | 4% | 2% | -56% | -90% | -91% |
| NEAR | 816 | 5 | 6% | 3% | -20% | -70% | -71% |
| SOL | 816 | 0 | 3% | 1% | -100% | -94% | -93% |
| BTC | 815 | 4 | 5% | 2% | -35% | -88% | -90% |
| XRP | 813 | 5 | 2% | 1% | -23% | -81% | -81% |
| GOLD | 468 | 0 | 4% | 1% | -100% | -92% | -94% |
| SILVER | 457 | 0 | 2% | 1% | -100% | -95% | -94% |
| WTI | 435 | 3 | 3% | 1% | -24% | -95% | -96% |
| COPPER | 398 | 0 | 1% | 1% | -100% | -99% | -99% |
| PLATINUM | 358 | 0 | 0% | 0% | -100% | -100% | -99% |
| NATGAS | 349 | 3 | 3% | 2% | -20% | -95% | -93% |
| PALLADIUM | 338 | 1 | 1% | 1% | -72% | -97% | -98% |
| EURUSD | 334 | 3 | 4% | 2% | -16% | -66% | -64% |
| GBPUSD | 313 | 1 | 3% | 2% | -70% | -95% | -95% |
| USDJPY | 273 | 3 | 1% | 1% | +3% | -97% | -96% |
| USDCAD | 1 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 5637 | 26 | 4% | 2% | -46% | -88% | -88% |
| DOWN (bought NO) | 5464 | 23 | 3% | 2% | -52% | -91% | -91% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 1215 | 8 | 2% | 1% | +14% | -66% | -65% |
| 0.05–0.1% | 1266 | 4 | 3% | 1% | -54% | -91% | -92% |
| 0.1–0.2% | 1878 | 6 | 3% | 2% | -60% | -92% | -92% |
| 0.2–0.5% | 2155 | 12 | 6% | 3% | -39% | -89% | -88% |
| Over 0.5% | 861 | 5 | 7% | 3% | -40% | -88% | -90% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 2890 | 17 | 4% | 2% | -32% | -84% | -84% |
| Morning (6am–12pm) | 2706 | 17 | 4% | 2% | -28% | -91% | -90% |
| Afternoon (12–6pm) | 2515 | 7 | 3% | 1% | -67% | -88% | -89% |
| Evening (6pm–12am) | 2990 | 8 | 3% | 1% | -69% | -95% | -94% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 25 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,068 |
| Time from buy to best bounce (bounced bets) | 49 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/7 5:29:59 PM | USDCAD | DOWN | 0 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/7 5:29:59 PM | PALLADIUM | DOWN | 0 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/7 5:29:59 PM | WTI | DOWN | 0 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/7 5:29:59 PM | GBPUSD | UP | 0 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/7 5:29:44 PM | GOLD | UP | 15 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/7 5:29:28 PM | SILVER | UP | 31 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/7 5:28:41 PM | ZEC | DOWN | 79 sec | +0.230% | 1¢ | In play | — |
| 10/7 5:28:25 PM | NEAR | UP | 1.6 min | -0.625% | 1¢ | In play | — |
| 10/7 5:27:22 PM | DOGE | DOWN | 2.6 min | +0.134% | 1¢ | In play | — |
| 10/7 5:26:50 PM | BNB | DOWN | 3.2 min | +0.092% | 1¢ | In play | — |
| 10/7 5:26:35 PM | HYPE | DOWN | 3.4 min | +0.303% | 1¢ | In play | — |
| 10/7 5:26:19 PM | SOL | DOWN | 3.7 min | +0.200% | 1¢ | In play | — |
| 10/7 5:26:03 PM | BTC | DOWN | 4.0 min | +0.178% | 1¢ | In play | — |
| 10/7 5:26:03 PM | XRP | DOWN | 4.0 min | +0.254% | 1¢ | In play | — |
| 10/7 5:24:12 PM | ETH | DOWN | 5.8 min | +0.210% | 1¢ | In play | — |
| 10/7 5:14:55 PM | WTI | UP | 4 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/7 5:14:39 PM | PLATINUM | DOWN | 20 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/7 5:14:39 PM | HYPE | DOWN | 20 sec | +0.071% | 0¢ | ❌ Lost | $0.00 |
| 10/7 5:14:39 PM | COPPER | DOWN | 20 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/7 5:14:24 PM | XRP | UP | 36 sec | -0.028% | 0¢ | ❌ Lost | -$0.15 |
| 10/7 5:14:08 PM | SOL | DOWN | 52 sec | +0.086% | 1¢ | ❌ Lost | -$0.15 |
| 10/7 5:13:52 PM | BNB | DOWN | 68 sec | +0.029% | 0¢ | ❌ Lost | -$0.15 |
| 10/7 5:13:21 PM | GOLD | DOWN | 1.6 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/7 5:13:05 PM | SILVER | DOWN | 1.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/7 5:12:46 PM | BTC | UP | 2.2 min | -0.127% | 1¢ | ❌ Lost | -$0.15 |
| 10/7 5:11:59 PM | ETH | UP | 3.0 min | -0.105% | 1¢ | ❌ Lost | -$0.15 |
| 10/7 5:11:59 PM | DOGE | UP | 3.0 min | -0.206% | 1¢ | ❌ Lost | -$0.15 |
| 10/7 5:10:08 PM | ZEC | DOWN | 4.8 min | +0.685% | 0¢ | ❌ Lost | -$0.15 |
| 10/7 4:44:51 PM | SILVER | UP | 8 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/7 4:44:51 PM | BTC | UP | 8 sec | -0.020% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
