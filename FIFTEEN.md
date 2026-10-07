# 15-Minute 1¢ Study

*Updated Wed Oct 7, 2:28 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 740 finished bets | 1% | $32.65 | +41% | +4.41¢ | -$11.75 / $44.40 |

*Expect about **77 buys a day** (~$11.59/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 738 | $19.70 | +25% |
| 5+ min left, hold to the close | 286 | $13.55 | +32% |
| Volatility model ≥ 2%, hold to the close | 1359 | $4.80 | +3% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 10963 | 10952 | 49 (0%) | 1.07% | -$640.45 (-48%) | Hold to the close: -$640.45 (-48%) |

*In play or awaiting result: 11. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 7083 | 4.1% | 0.5% (33) | -560% | ❌ Worse |
| Momentum model | 7083 | 4.1% | 0.5% (33) | -589% | ❌ Worse |
| Mean-reversion model | 7083 | 6.7% | 0.5% (33) | -653% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 7083 | 33 | -41% | -87% | -87% | -84% |
| Volatility model ≥ 2% | 1359 | 12 | +3% | -73% | -73% | -69% |
| Volatility model ≥ 5% | 740 | 8 | +41% | -62% | -60% | -57% |
| Volatility model ≥ 10% | 461 | 6 | +93% | -45% | -45% | -39% |
| Momentum model ≥ 2% | 1206 | 10 | +0% | -74% | -75% | -72% |
| Momentum model ≥ 5% | 738 | 7 | +25% | -66% | -68% | -65% |
| Momentum model ≥ 10% | 509 | 6 | +71% | -55% | -56% | -52% |
| Mean-reversion model ≥ 2% | 2422 | 19 | -15% | -84% | -84% | -80% |
| Mean-reversion model ≥ 5% | 1643 | 15 | +1% | -81% | -81% | -75% |
| Mean-reversion model ≥ 10% | 1092 | 11 | +16% | -79% | -79% | -74% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 7280 | 4% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 2765 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 907 | 3% | 2% | 2% | 1% | 1% | 0% |
| **All** | 10952 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 49 | 0% | -$640.45 | -48% | — |
| Sell at 2¢ | 385 | 4% | -$1,184.35 | -89% | 34 sec |
| Sell at 3¢ | 258 | 2% | -$1,183.83 | -89% | 47 sec |
| Sell at 5¢ | 192 | 2% | -$1,159.65 | -87% | 56 sec |
| Sell at 10¢ | 129 | 1% | -$1,101.46 | -83% | 64 sec |
| Sell at 25¢ | 74 | 1% | -$997.51 | -75% | 82 sec |
| Sell at 50¢ | 49 | 0% | -$869.70 | -66% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 3 | 0 | 100% | 67% | -100% | +73% | +160% |
| 5–10 min | 283 | 4 | 11% | 4% | +33% | -81% | -86% |
| 2–5 min | 3529 | 25 | 7% | 3% | -31% | -88% | -88% |
| 1–2 min | 2900 | 12 | 3% | 2% | -55% | -94% | -93% |
| Under 1 min | 4237 | 8 | 1% | 0% | -72% | -88% | -87% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 817 | 6 | 5% | 3% | -13% | -90% | -89% |
| HYPE | 816 | 3 | 5% | 3% | -55% | -89% | -87% |
| DOGE | 811 | 2 | 3% | 1% | -69% | -92% | -92% |
| ETH | 810 | 7 | 5% | 3% | +8% | -88% | -88% |
| BNB | 809 | 3 | 4% | 2% | -55% | -91% | -92% |
| NEAR | 806 | 5 | 6% | 3% | -19% | -69% | -71% |
| SOL | 805 | 0 | 3% | 1% | -100% | -93% | -92% |
| BTC | 804 | 4 | 5% | 2% | -34% | -88% | -90% |
| XRP | 802 | 5 | 2% | 1% | -22% | -81% | -80% |
| GOLD | 461 | 0 | 4% | 1% | -100% | -92% | -94% |
| SILVER | 450 | 0 | 2% | 1% | -100% | -95% | -94% |
| WTI | 426 | 3 | 3% | 1% | -23% | -95% | -96% |
| COPPER | 395 | 0 | 1% | 1% | -100% | -99% | -99% |
| PLATINUM | 354 | 0 | 0% | 0% | -100% | -100% | -99% |
| NATGAS | 343 | 3 | 3% | 2% | -18% | -94% | -92% |
| PALLADIUM | 336 | 1 | 1% | 1% | -72% | -97% | -98% |
| EURUSD | 329 | 3 | 4% | 2% | -15% | -65% | -64% |
| GBPUSD | 310 | 1 | 3% | 2% | -70% | -95% | -95% |
| USDJPY | 268 | 3 | 1% | 1% | +4% | -97% | -96% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 5572 | 26 | 4% | 2% | -46% | -88% | -87% |
| DOWN (bought NO) | 5380 | 23 | 3% | 2% | -51% | -90% | -91% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 1199 | 8 | 2% | 1% | +16% | -65% | -64% |
| 0.05–0.1% | 1248 | 4 | 3% | 1% | -53% | -92% | -92% |
| 0.1–0.2% | 1849 | 6 | 3% | 2% | -59% | -92% | -92% |
| 0.2–0.5% | 2131 | 12 | 6% | 3% | -38% | -88% | -87% |
| Over 0.5% | 851 | 5 | 6% | 3% | -40% | -88% | -90% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 2890 | 17 | 4% | 2% | -32% | -84% | -84% |
| Morning (6am–12pm) | 2706 | 17 | 4% | 2% | -28% | -91% | -90% |
| Afternoon (12–6pm) | 2366 | 7 | 3% | 1% | -65% | -88% | -89% |
| Evening (6pm–12am) | 2990 | 8 | 3% | 1% | -69% | -95% | -94% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 25 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,044 |
| Time from buy to best bounce (bounced bets) | 49 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/7 2:28:01 PM | COPPER | DOWN | 2.0 min | — | — | In play | — |
| 10/7 2:27:45 PM | WTI | DOWN | 2.2 min | — | — | In play | — |
| 10/7 2:27:28 PM | HYPE | DOWN | 2.5 min | +0.251% | — | In play | — |
| 10/7 2:26:09 PM | GOLD | DOWN | 3.9 min | — | — | In play | — |
| 10/7 2:26:09 PM | SILVER | DOWN | 3.9 min | — | — | In play | — |
| 10/7 2:14:39 PM | GBPUSD | UP | 20 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/7 2:14:23 PM | WTI | DOWN | 36 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/7 2:14:07 PM | USDJPY | DOWN | 52 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/7 2:14:07 PM | PLATINUM | DOWN | 52 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/7 2:14:07 PM | ZEC | DOWN | 52 sec | +0.215% | 0¢ | ❌ Lost | -$0.15 |
| 10/7 2:13:20 PM | COPPER | DOWN | 1.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/7 2:13:20 PM | SILVER | DOWN | 1.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/7 2:12:01 PM | HYPE | DOWN | 3.0 min | +0.381% | 0¢ | ❌ Lost | -$0.15 |
| 10/7 2:12:01 PM | GOLD | DOWN | 3.0 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/7 2:11:45 PM | DOGE | DOWN | 3.2 min | +0.281% | 1¢ | ❌ Lost | -$0.15 |
| 10/7 2:11:45 PM | BTC | DOWN | 3.2 min | +0.165% | 1¢ | ❌ Lost | -$0.15 |
| 10/7 2:11:30 PM | NEAR | DOWN | 3.5 min | +1.569% | 1¢ | ❌ Lost | -$0.15 |
| 10/7 2:11:30 PM | BNB | DOWN | 3.5 min | +0.110% | 1¢ | ❌ Lost | -$0.15 |
| 10/7 2:11:14 PM | XRP | DOWN | 3.8 min | +0.282% | 1¢ | ❌ Lost | -$0.15 |
| 10/7 2:10:26 PM | SOL | DOWN | 4.5 min | +0.348% | 1¢ | ❌ Lost | -$0.15 |
| 10/7 2:10:26 PM | ETH | DOWN | 4.5 min | +0.209% | 1¢ | ❌ Lost | -$0.15 |
| 10/7 1:59:58 PM | NATGAS | UP | 2 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/7 1:59:58 PM | ETH | DOWN | 2 sec | +0.044% | 0¢ | ❌ Lost | $0.00 |
| 10/7 1:59:27 PM | PLATINUM | DOWN | 33 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/7 1:59:27 PM | BTC | UP | 33 sec | -0.034% | 0¢ | ❌ Lost | $0.00 |
| 10/7 1:59:11 PM | COPPER | UP | 49 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/7 1:58:55 PM | DOGE | UP | 65 sec | -0.115% | 1¢ | ❌ Lost | -$0.15 |
| 10/7 1:58:39 PM | SOL | UP | 80 sec | -0.139% | 0¢ | ❌ Lost | -$0.15 |
| 10/7 1:58:39 PM | NEAR | UP | 80 sec | -0.434% | 1¢ | ❌ Lost | -$0.15 |
| 10/7 1:58:23 PM | PALLADIUM | UP | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
