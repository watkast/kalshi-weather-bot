# 15-Minute 1¢ Study

*Updated Tue Oct 6, 9:49 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 708 finished bets | 1% | $35.95 | +47% | +5.08¢ | -$10.25 / $46.20 |

*Expect about **80 buys a day** (~$11.96/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 706 | $23.15 | +31% |
| 5+ min left, hold to the close | 262 | $17.15 | +44% |
| Mean-reversion model ≥ 5%, hold to the close | 1547 | $15.60 | +8% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 10218 | 10212 | 46 (0%) | 1.07% | -$589.45 (-48%) | Hold to the close: -$589.45 (-48%) |

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
| Volatility model | 6643 | 4.2% | 0.5% (33) | -562% | ❌ Worse |
| Momentum model | 6643 | 4.2% | 0.5% (33) | -591% | ❌ Worse |
| Mean-reversion model | 6643 | 6.8% | 0.5% (33) | -649% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 6643 | 33 | -37% | -86% | -86% | -84% |
| Volatility model ≥ 2% | 1299 | 12 | +8% | -72% | -73% | -68% |
| Volatility model ≥ 5% | 708 | 8 | +47% | -61% | -61% | -57% |
| Volatility model ≥ 10% | 444 | 6 | +100% | -45% | -46% | -40% |
| Momentum model ≥ 2% | 1155 | 10 | +5% | -73% | -75% | -73% |
| Momentum model ≥ 5% | 706 | 7 | +31% | -66% | -68% | -65% |
| Momentum model ≥ 10% | 491 | 6 | +76% | -55% | -56% | -53% |
| Mean-reversion model ≥ 2% | 2280 | 19 | -9% | -83% | -84% | -79% |
| Mean-reversion model ≥ 5% | 1547 | 15 | +8% | -81% | -81% | -74% |
| Mean-reversion model ≥ 10% | 1026 | 11 | +24% | -79% | -79% | -73% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 6840 | 4% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 2546 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 826 | 3% | 2% | 2% | 1% | 1% | 0% |
| **All** | 10212 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 46 | 0% | -$589.45 | -48% | — |
| Sell at 2¢ | 364 | 4% | -$1,110.81 | -90% | 34 sec |
| Sell at 3¢ | 240 | 2% | -$1,111.85 | -90% | 48 sec |
| Sell at 5¢ | 179 | 2% | -$1,089.10 | -88% | 51 sec |
| Sell at 10¢ | 121 | 1% | -$1,032.94 | -84% | 65 sec |
| Sell at 25¢ | 70 | 1% | -$931.75 | -76% | 82 sec |
| Sell at 50¢ | 46 | 0% | -$810.95 | -66% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 3 | 0 | 100% | 67% | -100% | +73% | +160% |
| 5–10 min | 259 | 4 | 10% | 3% | +46% | -82% | -88% |
| 2–5 min | 3282 | 24 | 7% | 3% | -29% | -87% | -88% |
| 1–2 min | 2676 | 11 | 3% | 2% | -56% | -94% | -94% |
| Under 1 min | 3992 | 7 | 1% | 0% | -74% | -91% | -91% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 773 | 6 | 5% | 3% | -7% | -90% | -89% |
| HYPE | 765 | 3 | 5% | 3% | -52% | -88% | -87% |
| DOGE | 763 | 2 | 3% | 1% | -66% | -92% | -92% |
| ETH | 760 | 7 | 5% | 3% | +15% | -88% | -87% |
| BNB | 758 | 3 | 4% | 2% | -52% | -91% | -92% |
| NEAR | 756 | 5 | 6% | 3% | -13% | -68% | -69% |
| SOL | 756 | 0 | 3% | 1% | -100% | -93% | -92% |
| BTC | 755 | 4 | 5% | 3% | -30% | -87% | -89% |
| XRP | 754 | 5 | 2% | 1% | -16% | -80% | -80% |
| GOLD | 427 | 0 | 4% | 1% | -100% | -92% | -95% |
| SILVER | 414 | 0 | 2% | 1% | -100% | -96% | -96% |
| WTI | 394 | 2 | 3% | 1% | -44% | -95% | -97% |
| COPPER | 366 | 0 | 1% | 0% | -100% | -99% | -99% |
| PLATINUM | 325 | 0 | 0% | 0% | -100% | -99% | -99% |
| NATGAS | 310 | 3 | 3% | 2% | -10% | -94% | -92% |
| PALLADIUM | 310 | 1 | 2% | 1% | -70% | -97% | -98% |
| EURUSD | 299 | 1 | 4% | 2% | -69% | -94% | -92% |
| GBPUSD | 283 | 1 | 3% | 2% | -67% | -94% | -94% |
| USDJPY | 244 | 3 | 2% | 1% | +15% | -97% | -96% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 5161 | 24 | 4% | 2% | -46% | -90% | -89% |
| DOWN (bought NO) | 5051 | 22 | 3% | 2% | -50% | -90% | -91% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 1139 | 8 | 2% | 1% | +20% | -65% | -64% |
| 0.05–0.1% | 1182 | 4 | 3% | 1% | -50% | -91% | -92% |
| 0.1–0.2% | 1730 | 6 | 4% | 2% | -56% | -91% | -92% |
| 0.2–0.5% | 1990 | 12 | 6% | 3% | -34% | -88% | -87% |
| Over 0.5% | 797 | 5 | 7% | 3% | -36% | -88% | -89% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 2570 | 15 | 4% | 2% | -32% | -87% | -88% |
| Morning (6am–12pm) | 2536 | 17 | 5% | 3% | -24% | -90% | -89% |
| Afternoon (12–6pm) | 2244 | 7 | 3% | 1% | -63% | -88% | -89% |
| Evening (6pm–12am) | 2862 | 7 | 3% | 1% | -72% | -95% | -94% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 25 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,098 |
| Time from buy to best bounce (bounced bets) | 49 sec |
| Price snapshots per bet | 41 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/6 9:44:19 PM | HYPE | DOWN | 40 sec | +0.096% | 1¢ | ❌ Lost | -$0.15 |
| 10/6 9:44:19 PM | WTI | DOWN | 40 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/6 9:44:19 PM | PLATINUM | DOWN | 40 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/6 9:44:03 PM | ZEC | DOWN | 56 sec | +0.258% | 0¢ | ❌ Lost | $0.00 |
| 10/6 9:43:48 PM | GOLD | DOWN | 71 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/6 9:43:16 PM | DOGE | DOWN | 1.7 min | +0.165% | 0¢ | ❌ Lost | $0.00 |
| 10/6 9:43:16 PM | COPPER | DOWN | 1.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/6 9:43:16 PM | SILVER | DOWN | 1.7 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/6 9:43:00 PM | NEAR | DOWN | 2.0 min | +0.413% | 1¢ | ❌ Lost | -$0.15 |
| 10/6 9:42:44 PM | SOL | DOWN | 2.2 min | +0.130% | 1¢ | ❌ Lost | -$0.15 |
| 10/6 9:42:30 PM | XRP | DOWN | 2.5 min | +0.198% | 1¢ | ❌ Lost | -$0.15 |
| 10/6 9:41:58 PM | BNB | DOWN | 3.0 min | +0.095% | 1¢ | ❌ Lost | -$0.15 |
| 10/6 9:41:19 PM | BTC | DOWN | 3.7 min | +0.178% | 1¢ | ❌ Lost | -$0.15 |
| 10/6 9:41:03 PM | ETH | DOWN | 3.9 min | +0.141% | 1¢ | ❌ Lost | -$0.15 |
| 10/6 9:29:57 PM | SOL | DOWN | 2 sec | +0.021% | 0¢ | ❌ Lost | $0.00 |
| 10/6 9:29:40 PM | XRP | DOWN | 20 sec | +0.041% | 0¢ | ❌ Lost | $0.00 |
| 10/6 9:29:40 PM | ZEC | UP | 20 sec | -0.098% | 1¢ | ❌ Lost | -$0.15 |
| 10/6 9:29:24 PM | WTI | UP | 36 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/6 9:29:24 PM | NEAR | DOWN | 36 sec | +0.119% | 0¢ | ❌ Lost | $0.00 |
| 10/6 9:29:24 PM | BTC | DOWN | 36 sec | +0.014% | 1¢ | ❌ Lost | -$0.15 |
| 10/6 9:29:08 PM | DOGE | DOWN | 52 sec | +0.082% | 1¢ | ❌ Lost | -$0.15 |
| 10/6 9:29:08 PM | HYPE | DOWN | 52 sec | +0.065% | 1¢ | ❌ Lost | -$0.15 |
| 10/6 9:28:53 PM | ETH | UP | 66 sec | -0.144% | 0¢ | ❌ Lost | $0.00 |
| 10/6 9:28:38 PM | SILVER | DOWN | 81 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/6 9:27:50 PM | GOLD | DOWN | 2.2 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/6 9:27:17 PM | BNB | DOWN | 2.7 min | +0.140% | 0¢ | ❌ Lost | $0.00 |
| 10/6 9:14:48 PM | XRP | DOWN | 12 sec | +0.007% | 0¢ | ❌ Lost | $0.00 |
| 10/6 9:14:48 PM | USDJPY | UP | 12 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/6 9:14:32 PM | SILVER | UP | 28 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/6 9:14:32 PM | ETH | UP | 28 sec | -0.037% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
