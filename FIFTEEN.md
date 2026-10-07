# 15-Minute 1¢ Study

*Updated Wed Oct 7, 2:58 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 740 finished bets | 1% | $32.65 | +41% | +4.41¢ | -$11.75 / $44.40 |

*Expect about **77 buys a day** (~$11.57/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 738 | $19.70 | +25% |
| 5+ min left, hold to the close | 287 | $13.40 | +31% |
| Volatility model ≥ 2%, hold to the close | 1359 | $4.80 | +3% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 10993 | 10981 | 49 (0%) | 1.07% | -$643.75 (-48%) | Hold to the close: -$643.75 (-48%) |

*In play or awaiting result: 12. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 7100 | 4.1% | 0.5% (33) | -559% | ❌ Worse |
| Momentum model | 7100 | 4.1% | 0.5% (33) | -588% | ❌ Worse |
| Mean-reversion model | 7100 | 6.7% | 0.5% (33) | -652% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 7100 | 33 | -42% | -87% | -87% | -84% |
| Volatility model ≥ 2% | 1359 | 12 | +3% | -73% | -73% | -69% |
| Volatility model ≥ 5% | 740 | 8 | +41% | -62% | -60% | -57% |
| Volatility model ≥ 10% | 461 | 6 | +93% | -45% | -45% | -39% |
| Momentum model ≥ 2% | 1207 | 10 | +0% | -74% | -75% | -72% |
| Momentum model ≥ 5% | 738 | 7 | +25% | -66% | -68% | -65% |
| Momentum model ≥ 10% | 509 | 6 | +71% | -55% | -56% | -52% |
| Mean-reversion model ≥ 2% | 2429 | 19 | -15% | -84% | -84% | -80% |
| Mean-reversion model ≥ 5% | 1646 | 15 | +1% | -81% | -81% | -75% |
| Mean-reversion model ≥ 10% | 1095 | 11 | +16% | -79% | -79% | -74% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 7297 | 4% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 2774 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 910 | 3% | 2% | 2% | 1% | 1% | 0% |
| **All** | 10981 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 49 | 0% | -$643.75 | -48% | — |
| Sell at 2¢ | 385 | 4% | -$1,187.65 | -89% | 34 sec |
| Sell at 3¢ | 258 | 2% | -$1,187.13 | -89% | 47 sec |
| Sell at 5¢ | 192 | 2% | -$1,162.95 | -87% | 56 sec |
| Sell at 10¢ | 129 | 1% | -$1,104.76 | -83% | 64 sec |
| Sell at 25¢ | 74 | 1% | -$1,000.81 | -75% | 82 sec |
| Sell at 50¢ | 49 | 0% | -$873.00 | -66% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 3 | 0 | 100% | 67% | -100% | +73% | +160% |
| 5–10 min | 284 | 4 | 11% | 4% | +33% | -81% | -86% |
| 2–5 min | 3543 | 25 | 7% | 3% | -31% | -88% | -88% |
| 1–2 min | 2903 | 12 | 3% | 2% | -55% | -94% | -93% |
| Under 1 min | 4248 | 8 | 1% | 0% | -72% | -88% | -88% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 818 | 6 | 5% | 3% | -13% | -90% | -89% |
| HYPE | 818 | 3 | 5% | 3% | -55% | -89% | -87% |
| DOGE | 813 | 2 | 3% | 1% | -69% | -92% | -92% |
| ETH | 812 | 7 | 5% | 3% | +8% | -88% | -88% |
| BNB | 811 | 3 | 4% | 2% | -55% | -91% | -92% |
| NEAR | 808 | 5 | 6% | 3% | -19% | -70% | -71% |
| SOL | 807 | 0 | 3% | 1% | -100% | -93% | -92% |
| BTC | 806 | 4 | 5% | 2% | -34% | -88% | -90% |
| XRP | 804 | 5 | 2% | 1% | -22% | -81% | -81% |
| GOLD | 463 | 0 | 4% | 1% | -100% | -92% | -94% |
| SILVER | 452 | 0 | 2% | 1% | -100% | -95% | -94% |
| WTI | 428 | 3 | 3% | 1% | -23% | -95% | -96% |
| COPPER | 396 | 0 | 1% | 1% | -100% | -99% | -99% |
| PLATINUM | 356 | 0 | 0% | 0% | -100% | -100% | -99% |
| NATGAS | 343 | 3 | 3% | 2% | -18% | -94% | -92% |
| PALLADIUM | 336 | 1 | 1% | 1% | -72% | -97% | -98% |
| EURUSD | 330 | 3 | 4% | 2% | -15% | -65% | -64% |
| GBPUSD | 310 | 1 | 3% | 2% | -70% | -95% | -95% |
| USDJPY | 270 | 3 | 1% | 1% | +4% | -97% | -96% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 5589 | 26 | 4% | 2% | -46% | -88% | -87% |
| DOWN (bought NO) | 5392 | 23 | 3% | 2% | -51% | -91% | -91% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 1201 | 8 | 2% | 1% | +16% | -65% | -64% |
| 0.05–0.1% | 1251 | 4 | 3% | 1% | -53% | -92% | -92% |
| 0.1–0.2% | 1852 | 6 | 3% | 2% | -59% | -92% | -92% |
| 0.2–0.5% | 2138 | 12 | 6% | 3% | -39% | -88% | -87% |
| Over 0.5% | 853 | 5 | 6% | 3% | -40% | -88% | -90% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 2890 | 17 | 4% | 2% | -32% | -84% | -84% |
| Morning (6am–12pm) | 2706 | 17 | 4% | 2% | -28% | -91% | -90% |
| Afternoon (12–6pm) | 2395 | 7 | 3% | 1% | -65% | -88% | -89% |
| Evening (6pm–12am) | 2990 | 8 | 3% | 1% | -69% | -95% | -94% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 25 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,055 |
| Time from buy to best bounce (bounced bets) | 49 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/7 2:58:16 PM | PALLADIUM | UP | 1.7 min | — | — | In play | — |
| 10/7 2:58:16 PM | HYPE | DOWN | 1.7 min | +0.165% | — | In play | — |
| 10/7 2:57:28 PM | SOL | DOWN | 2.5 min | +0.161% | — | In play | — |
| 10/7 2:57:28 PM | XRP | DOWN | 2.5 min | +0.183% | — | In play | — |
| 10/7 2:56:27 PM | DOGE | DOWN | 3.5 min | +0.191% | — | In play | — |
| 10/7 2:56:11 PM | ETH | DOWN | 3.8 min | +0.134% | — | In play | — |
| 10/7 2:44:36 PM | EURUSD | UP | 23 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/7 2:44:20 PM | PLATINUM | UP | 39 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/7 2:44:20 PM | XRP | UP | 39 sec | -0.105% | 0¢ | ❌ Lost | $0.00 |
| 10/7 2:43:33 PM | WTI | UP | 86 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/7 2:42:45 PM | NEAR | UP | 2.2 min | -0.764% | 1¢ | ❌ Lost | -$0.15 |
| 10/7 2:42:30 PM | GOLD | UP | 2.5 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/7 2:42:30 PM | USDJPY | DOWN | 2.5 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/7 2:41:42 PM | DOGE | UP | 3.3 min | -0.214% | 1¢ | ❌ Lost | -$0.15 |
| 10/7 2:41:42 PM | SILVER | UP | 3.3 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/7 2:41:27 PM | HYPE | UP | 3.5 min | -0.409% | 1¢ | ❌ Lost | -$0.15 |
| 10/7 2:40:55 PM | BTC | UP | 4.1 min | -0.263% | 1¢ | ❌ Lost | -$0.15 |
| 10/7 2:40:24 PM | SOL | UP | 4.6 min | -0.258% | 1¢ | ❌ Lost | -$0.15 |
| 10/7 2:40:08 PM | ZEC | UP | 4.8 min | -0.662% | 1¢ | ❌ Lost | -$0.15 |
| 10/7 2:40:08 PM | BNB | UP | 4.8 min | -0.175% | 0¢ | ❌ Lost | $0.00 |
| 10/7 2:39:21 PM | ETH | UP | 5.7 min | -0.314% | 1¢ | ❌ Lost | -$0.15 |
| 10/7 2:29:51 PM | BNB | UP | 8 sec | -0.029% | 0¢ | ❌ Lost | $0.00 |
| 10/7 2:29:51 PM | BTC | DOWN | 8 sec | +0.020% | 0¢ | ❌ Lost | $0.00 |
| 10/7 2:29:36 PM | PLATINUM | DOWN | 23 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/7 2:29:20 PM | ETH | DOWN | 39 sec | +0.065% | 0¢ | ❌ Lost | $0.00 |
| 10/7 2:29:20 PM | NEAR | DOWN | 39 sec | +0.301% | 0¢ | ❌ Lost | $0.00 |
| 10/7 2:29:20 PM | USDJPY | UP | 39 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/7 2:29:20 PM | SOL | DOWN | 39 sec | +0.067% | 0¢ | ❌ Lost | $0.00 |
| 10/7 2:29:20 PM | XRP | UP | 39 sec | -0.063% | 1¢ | ❌ Lost | -$0.15 |
| 10/7 2:28:33 PM | DOGE | DOWN | 86 sec | +0.108% | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
