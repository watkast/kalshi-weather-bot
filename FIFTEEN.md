# 15-Minute 1¢ Study

*Updated Wed Oct 7, 1:42 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 721 finished bets | 1% | $34.60 | +45% | +4.80¢ | -$10.85 / $45.45 |

*Expect about **80 buys a day** (~$11.98/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 718 | $21.95 | +29% |
| 5+ min left, hold to the close | 264 | $16.85 | +43% |
| Mean-reversion model ≥ 5%, hold to the close | 1576 | $11.70 | +6% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 10441 | 10433 | 47 (0%) | 1.07% | -$603.65 (-48%) | Hold to the close: -$603.65 (-48%) |

*In play or awaiting result: 8. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 6769 | 4.2% | 0.5% (33) | -565% | ❌ Worse |
| Momentum model | 6769 | 4.2% | 0.5% (33) | -593% | ❌ Worse |
| Mean-reversion model | 6769 | 6.8% | 0.5% (33) | -654% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 6769 | 33 | -39% | -86% | -87% | -84% |
| Volatility model ≥ 2% | 1320 | 12 | +6% | -73% | -73% | -69% |
| Volatility model ≥ 5% | 721 | 8 | +45% | -62% | -61% | -58% |
| Volatility model ≥ 10% | 452 | 6 | +96% | -45% | -46% | -41% |
| Momentum model ≥ 2% | 1175 | 10 | +3% | -73% | -75% | -73% |
| Momentum model ≥ 5% | 718 | 7 | +29% | -66% | -68% | -65% |
| Momentum model ≥ 10% | 500 | 6 | +73% | -56% | -57% | -54% |
| Mean-reversion model ≥ 2% | 2318 | 19 | -11% | -84% | -84% | -79% |
| Mean-reversion model ≥ 5% | 1576 | 15 | +6% | -81% | -81% | -75% |
| Mean-reversion model ≥ 10% | 1044 | 11 | +22% | -79% | -79% | -74% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 6966 | 4% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 2622 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 845 | 3% | 2% | 2% | 1% | 1% | 0% |
| **All** | 10433 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 47 | 0% | -$603.65 | -48% | — |
| Sell at 2¢ | 371 | 4% | -$1,137.19 | -90% | 33 sec |
| Sell at 3¢ | 247 | 2% | -$1,137.32 | -90% | 47 sec |
| Sell at 5¢ | 185 | 2% | -$1,113.40 | -88% | 60 sec |
| Sell at 10¢ | 124 | 1% | -$1,057.21 | -84% | 65 sec |
| Sell at 25¢ | 71 | 1% | -$956.64 | -76% | 82 sec |
| Sell at 50¢ | 47 | 0% | -$832.40 | -66% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 3 | 0 | 100% | 67% | -100% | +73% | +160% |
| 5–10 min | 261 | 4 | 10% | 3% | +45% | -83% | -88% |
| 2–5 min | 3353 | 25 | 7% | 3% | -27% | -88% | -88% |
| 1–2 min | 2745 | 11 | 3% | 2% | -57% | -94% | -93% |
| Under 1 min | 4071 | 7 | 1% | 0% | -75% | -91% | -91% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 787 | 6 | 5% | 3% | -9% | -90% | -89% |
| HYPE | 780 | 3 | 5% | 3% | -53% | -88% | -86% |
| DOGE | 776 | 2 | 3% | 1% | -67% | -92% | -92% |
| ETH | 774 | 7 | 5% | 3% | +13% | -88% | -87% |
| BNB | 773 | 3 | 4% | 2% | -53% | -91% | -93% |
| NEAR | 771 | 5 | 6% | 3% | -15% | -69% | -70% |
| SOL | 770 | 0 | 3% | 1% | -100% | -93% | -93% |
| BTC | 768 | 4 | 5% | 2% | -31% | -88% | -89% |
| XRP | 767 | 5 | 2% | 1% | -18% | -80% | -80% |
| GOLD | 439 | 0 | 4% | 1% | -100% | -92% | -94% |
| SILVER | 426 | 0 | 2% | 1% | -100% | -95% | -95% |
| WTI | 405 | 3 | 3% | 1% | -19% | -94% | -96% |
| COPPER | 377 | 0 | 1% | 1% | -100% | -99% | -99% |
| PLATINUM | 335 | 0 | 0% | 0% | -100% | -99% | -99% |
| NATGAS | 321 | 3 | 3% | 2% | -13% | -95% | -93% |
| PALLADIUM | 319 | 1 | 2% | 1% | -71% | -97% | -98% |
| EURUSD | 307 | 1 | 4% | 2% | -70% | -94% | -92% |
| GBPUSD | 289 | 1 | 3% | 2% | -68% | -95% | -95% |
| USDJPY | 249 | 3 | 2% | 1% | +12% | -97% | -96% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 5272 | 25 | 4% | 2% | -45% | -90% | -89% |
| DOWN (bought NO) | 5161 | 22 | 3% | 2% | -51% | -90% | -91% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 1156 | 8 | 2% | 1% | +19% | -65% | -64% |
| 0.05–0.1% | 1212 | 4 | 3% | 1% | -52% | -91% | -92% |
| 0.1–0.2% | 1762 | 6 | 4% | 2% | -57% | -92% | -92% |
| 0.2–0.5% | 2029 | 12 | 6% | 3% | -35% | -88% | -87% |
| Over 0.5% | 805 | 5 | 6% | 3% | -36% | -88% | -89% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 2663 | 15 | 4% | 2% | -35% | -87% | -88% |
| Morning (6am–12pm) | 2536 | 17 | 5% | 3% | -24% | -90% | -89% |
| Afternoon (12–6pm) | 2244 | 7 | 3% | 1% | -63% | -88% | -89% |
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
| 10/7 1:41:45 AM | EURUSD | UP | 3.2 min | — | — | In play | — |
| 10/7 1:39:54 AM | BNB | DOWN | 5.1 min | +0.141% | — | In play | — |
| 10/7 1:29:50 AM | WTI | DOWN | 9 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/7 1:29:18 AM | BTC | UP | 41 sec | -0.047% | 0¢ | ❌ Lost | $0.00 |
| 10/7 1:29:18 AM | BNB | DOWN | 41 sec | -0.019% | 0¢ | ❌ Lost | $0.00 |
| 10/7 1:29:02 AM | ETH | UP | 58 sec | -0.055% | 0¢ | ❌ Lost | -$0.15 |
| 10/7 1:28:50 AM | DOGE | UP | 69 sec | -0.097% | 0¢ | ❌ Lost | -$0.15 |
| 10/7 1:28:50 AM | NEAR | UP | 69 sec | -0.298% | 1¢ | ❌ Lost | -$0.15 |
| 10/7 1:28:50 AM | ZEC | UP | 69 sec | -0.146% | 1¢ | ❌ Lost | -$0.15 |
| 10/7 1:28:34 AM | NATGAS | DOWN | 85 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/7 1:28:34 AM | GOLD | DOWN | 85 sec | — | 7¢ | ❌ Lost | -$0.15 |
| 10/7 1:28:34 AM | USDJPY | UP | 85 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/7 1:28:18 AM | COPPER | DOWN | 1.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/7 1:28:02 AM | SILVER | DOWN | 1.9 min | — | 19¢ | ❌ Lost | -$0.15 |
| 10/7 1:27:15 AM | XRP | UP | 2.8 min | -0.217% | 1¢ | ❌ Lost | -$0.15 |
| 10/7 1:27:15 AM | HYPE | UP | 2.8 min | -0.218% | 1¢ | ❌ Lost | -$0.15 |
| 10/7 1:26:27 AM | SOL | UP | 3.5 min | -0.212% | 1¢ | ❌ Lost | -$0.15 |
| 10/7 1:22:29 AM | EURUSD | UP | 7.5 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/7 1:14:45 AM | BTC | DOWN | 15 sec | +0.024% | 0¢ | ❌ Lost | $0.00 |
| 10/7 1:14:13 AM | XRP | DOWN | 47 sec | +0.054% | 0¢ | ❌ Lost | $0.00 |
| 10/7 1:14:13 AM | BNB | UP | 47 sec | -0.085% | 0¢ | ❌ Lost | $0.00 |
| 10/7 1:14:13 AM | GOLD | DOWN | 47 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/7 1:14:13 AM | NEAR | DOWN | 47 sec | +0.303% | 0¢ | ❌ Lost | $0.00 |
| 10/7 1:13:57 AM | EURUSD | UP | 63 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/7 1:13:24 AM | DOGE | DOWN | 1.6 min | +0.116% | 1¢ | ❌ Lost | -$0.15 |
| 10/7 1:13:24 AM | NATGAS | DOWN | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/7 1:13:24 AM | SOL | DOWN | 1.6 min | +0.139% | 0¢ | ❌ Lost | -$0.15 |
| 10/7 1:12:53 AM | USDJPY | DOWN | 2.1 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/7 1:12:38 AM | HYPE | DOWN | 2.4 min | +0.077% | 3¢ | ❌ Lost | -$0.15 |
| 10/7 1:11:50 AM | COPPER | DOWN | 3.2 min | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
