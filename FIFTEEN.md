# 15-Minute 1¢ Study

*Updated Mon Oct 5, 7:38 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 622 finished bets | 1% | $31.10 | +46% | +5.00¢ | -$6.20 / $37.30 |

*Expect about **80 buys a day** (~$11.98/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 622 | $17.70 | +27% |
| Volatility model ≥ 2%, hold to the close | 1156 | $14.80 | +11% |
| Mean-reversion model ≥ 5%, hold to the close | 1373 | $9.35 | +5% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 9023 | 9017 | 39 (0%) | 1.07% | -$538.95 (-50%) | Hold to the close: -$538.95 (-50%) |

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
| Volatility model | 5922 | 4.1% | 0.5% (27) | -577% | ❌ Worse |
| Momentum model | 5922 | 4.1% | 0.5% (27) | -602% | ❌ Worse |
| Mean-reversion model | 5922 | 6.7% | 0.5% (27) | -676% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 5922 | 27 | -42% | -85% | -85% | -83% |
| Volatility model ≥ 2% | 1156 | 11 | +11% | -70% | -70% | -66% |
| Volatility model ≥ 5% | 622 | 7 | +46% | -57% | -56% | -53% |
| Volatility model ≥ 10% | 383 | 5 | +94% | -38% | -39% | -34% |
| Momentum model ≥ 2% | 1022 | 9 | +7% | -71% | -73% | -71% |
| Momentum model ≥ 5% | 622 | 6 | +27% | -62% | -65% | -62% |
| Momentum model ≥ 10% | 428 | 5 | +68% | -50% | -51% | -48% |
| Mean-reversion model ≥ 2% | 2043 | 15 | -20% | -83% | -83% | -78% |
| Mean-reversion model ≥ 5% | 1373 | 13 | +5% | -79% | -79% | -73% |
| Mean-reversion model ≥ 10% | 904 | 9 | +15% | -78% | -78% | -71% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 6119 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 2196 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 702 | 3% | 3% | 2% | 2% | 1% | 0% |
| **All** | 9017 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 39 | 0% | -$538.95 | -50% | — |
| Sell at 2¢ | 342 | 4% | -$968.03 | -89% | 33 sec |
| Sell at 3¢ | 224 | 2% | -$969.59 | -89% | 47 sec |
| Sell at 5¢ | 165 | 2% | -$949.70 | -88% | 61 sec |
| Sell at 10¢ | 111 | 1% | -$897.54 | -83% | 66 sec |
| Sell at 25¢ | 61 | 1% | -$813.04 | -75% | 83 sec |
| Sell at 50¢ | 38 | 0% | -$716.45 | -66% | 1.7 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 3 | 0 | 100% | 67% | -100% | +73% | +160% |
| 5–10 min | 226 | 3 | 11% | 3% | +26% | -81% | -88% |
| 2–5 min | 2917 | 21 | 7% | 3% | -30% | -87% | -87% |
| 1–2 min | 2380 | 10 | 3% | 2% | -54% | -93% | -93% |
| Under 1 min | 3491 | 5 | 1% | 0% | -79% | -89% | -89% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 692 | 5 | 5% | 3% | -14% | -89% | -89% |
| DOGE | 683 | 2 | 4% | 1% | -62% | -91% | -91% |
| HYPE | 683 | 3 | 5% | 3% | -46% | -88% | -86% |
| ETH | 682 | 6 | 6% | 3% | +10% | -87% | -86% |
| BNB | 679 | 2 | 4% | 2% | -64% | -90% | -92% |
| BTC | 676 | 3 | 5% | 2% | -42% | -87% | -90% |
| XRP | 676 | 4 | 1% | 1% | -25% | -78% | -78% |
| SOL | 675 | 0 | 3% | 1% | -100% | -93% | -92% |
| NEAR | 673 | 4 | 6% | 3% | -22% | -65% | -66% |
| GOLD | 369 | 0 | 4% | 1% | -100% | -92% | -94% |
| SILVER | 354 | 0 | 2% | 1% | -100% | -96% | -96% |
| WTI | 335 | 2 | 3% | 1% | -36% | -95% | -96% |
| COPPER | 313 | 0 | 1% | 0% | -100% | -99% | -99% |
| PLATINUM | 281 | 0 | 0% | 0% | -100% | -100% | -100% |
| NATGAS | 274 | 2 | 3% | 2% | -32% | -94% | -92% |
| PALLADIUM | 270 | 1 | 2% | 1% | -65% | -97% | -98% |
| EURUSD | 252 | 1 | 4% | 3% | -63% | -92% | -91% |
| GBPUSD | 241 | 1 | 4% | 2% | -61% | -94% | -94% |
| USDJPY | 209 | 3 | 2% | 1% | +34% | -97% | -95% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 4556 | 21 | 4% | 2% | -46% | -89% | -88% |
| DOWN (bought NO) | 4461 | 18 | 4% | 2% | -53% | -90% | -91% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 1011 | 7 | 2% | 1% | +18% | -60% | -60% |
| 0.05–0.1% | 1039 | 3 | 3% | 1% | -57% | -91% | -92% |
| 0.1–0.2% | 1534 | 6 | 4% | 2% | -50% | -91% | -91% |
| 0.2–0.5% | 1791 | 9 | 6% | 3% | -45% | -88% | -87% |
| Over 0.5% | 742 | 4 | 7% | 3% | -45% | -87% | -89% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 2228 | 9 | 4% | 2% | -53% | -86% | -87% |
| Morning (6am–12pm) | 2361 | 17 | 5% | 3% | -18% | -90% | -88% |
| Afternoon (12–6pm) | 1943 | 6 | 3% | 1% | -63% | -86% | -88% |
| Evening (6pm–12am) | 2485 | 7 | 3% | 1% | -67% | -94% | -94% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 25 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,130 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/5 7:29:17 PM | SOL | UP | 42 sec | -0.059% | 0¢ | ❌ Lost | $0.00 |
| 10/5 7:29:01 PM | NATGAS | DOWN | 59 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/5 7:29:01 PM | NEAR | UP | 59 sec | -0.474% | 0¢ | ❌ Lost | $0.00 |
| 10/5 7:28:13 PM | EURUSD | DOWN | 1.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/5 7:27:41 PM | BTC | UP | 2.3 min | -0.155% | 1¢ | ❌ Lost | -$0.15 |
| 10/5 7:27:25 PM | ZEC | UP | 2.6 min | -0.385% | 1¢ | ❌ Lost | -$0.15 |
| 10/5 7:27:25 PM | ETH | UP | 2.6 min | -0.141% | 1¢ | ❌ Lost | -$0.15 |
| 10/5 7:26:37 PM | XRP | UP | 3.4 min | -0.298% | 1¢ | ❌ Lost | -$0.15 |
| 10/5 7:26:21 PM | COPPER | UP | 3.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/5 7:26:21 PM | DOGE | UP | 3.6 min | -0.328% | 1¢ | ❌ Lost | -$0.15 |
| 10/5 7:26:21 PM | PALLADIUM | UP | 3.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/5 7:25:31 PM | BNB | UP | 4.5 min | -0.271% | 1¢ | ❌ Lost | -$0.15 |
| 10/5 7:25:15 PM | HYPE | UP | 4.8 min | -0.439% | 1¢ | ❌ Lost | -$0.15 |
| 10/5 7:24:44 PM | GOLD | UP | 5.2 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/5 7:24:44 PM | SILVER | UP | 5.2 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/5 7:24:27 PM | PLATINUM | UP | 5.5 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/5 7:14:35 PM | HYPE | DOWN | 24 sec | +0.077% | 0¢ | ❌ Lost | $0.00 |
| 10/5 7:14:19 PM | ETH | DOWN | 40 sec | +0.007% | 0¢ | ❌ Lost | $0.00 |
| 10/5 7:14:03 PM | SOL | DOWN | 57 sec | +0.091% | 0¢ | ❌ Lost | -$0.15 |
| 10/5 7:14:03 PM | GBPUSD | DOWN | 57 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/5 7:14:03 PM | PLATINUM | UP | 57 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/5 7:14:03 PM | EURUSD | DOWN | 57 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/5 7:14:03 PM | BNB | UP | 57 sec | -0.090% | 0¢ | ❌ Lost | -$0.15 |
| 10/5 7:13:46 PM | XRP | DOWN | 73 sec | +0.172% | 0¢ | ❌ Lost | -$0.15 |
| 10/5 7:13:46 PM | ZEC | DOWN | 73 sec | +0.214% | 1¢ | ❌ Lost | -$0.15 |
| 10/5 7:13:30 PM | PALLADIUM | UP | 89 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/5 7:13:14 PM | DOGE | DOWN | 1.8 min | +0.141% | 1¢ | ❌ Lost | -$0.15 |
| 10/5 7:13:14 PM | NATGAS | UP | 1.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/5 7:13:14 PM | SILVER | UP | 1.8 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/5 7:13:14 PM | WTI | DOWN | 1.8 min | — | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
