# 15-Minute 1¢ Study

*Updated Tue Oct 6, 4:07 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 646 finished bets | 1% | $28.70 | +41% | +4.44¢ | -$7.25 / $35.95 |

*Expect about **79 buys a day** (~$11.90/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| 5+ min left, hold to the close | 243 | $20.00 | +56% |
| Mean-reversion model ≥ 5%, hold to the close | 1420 | $17.80 | +10% |
| Momentum model ≥ 5%, hold to the close | 643 | $15.60 | +23% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 9410 | 9404 | 44 (0%) | 1.07% | -$516.35 (-46%) | Hold to the close: -$516.35 (-46%) |

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
| Volatility model | 6152 | 4.0% | 0.5% (32) | -528% | ❌ Worse |
| Momentum model | 6152 | 4.1% | 0.5% (32) | -553% | ❌ Worse |
| Mean-reversion model | 6152 | 6.7% | 0.5% (32) | -610% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 6152 | 32 | -34% | -86% | -86% | -83% |
| Volatility model ≥ 2% | 1197 | 11 | +7% | -71% | -71% | -67% |
| Volatility model ≥ 5% | 646 | 7 | +41% | -59% | -58% | -54% |
| Volatility model ≥ 10% | 397 | 5 | +89% | -40% | -41% | -36% |
| Momentum model ≥ 2% | 1058 | 9 | +3% | -72% | -74% | -72% |
| Momentum model ≥ 5% | 643 | 6 | +23% | -64% | -66% | -63% |
| Momentum model ≥ 10% | 445 | 5 | +61% | -52% | -52% | -50% |
| Mean-reversion model ≥ 2% | 2112 | 18 | -7% | -83% | -83% | -78% |
| Mean-reversion model ≥ 5% | 1420 | 14 | +10% | -80% | -80% | -73% |
| Mean-reversion model ≥ 10% | 938 | 10 | +24% | -78% | -78% | -72% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 6349 | 4% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 2309 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 746 | 3% | 3% | 2% | 1% | 1% | 0% |
| **All** | 9404 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 44 | 0% | -$516.35 | -46% | — |
| Sell at 2¢ | 351 | 4% | -$1,013.09 | -89% | 33 sec |
| Sell at 3¢ | 230 | 2% | -$1,014.65 | -90% | 47 sec |
| Sell at 5¢ | 171 | 2% | -$993.20 | -88% | 50 sec |
| Sell at 10¢ | 116 | 1% | -$938.39 | -83% | 65 sec |
| Sell at 25¢ | 66 | 1% | -$843.89 | -75% | 82 sec |
| Sell at 50¢ | 43 | 0% | -$730.10 | -64% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 3 | 0 | 100% | 67% | -100% | +73% | +160% |
| 5–10 min | 240 | 4 | 10% | 3% | +58% | -82% | -88% |
| 2–5 min | 3037 | 24 | 7% | 3% | -23% | -87% | -87% |
| 1–2 min | 2477 | 11 | 3% | 2% | -52% | -94% | -93% |
| Under 1 min | 3647 | 5 | 1% | 0% | -79% | -90% | -90% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 719 | 6 | 5% | 3% | -0% | -89% | -89% |
| HYPE | 709 | 3 | 5% | 3% | -48% | -88% | -86% |
| DOGE | 708 | 2 | 4% | 1% | -64% | -91% | -91% |
| ETH | 706 | 7 | 6% | 3% | +24% | -87% | -86% |
| BNB | 704 | 3 | 4% | 2% | -48% | -90% | -92% |
| XRP | 702 | 5 | 2% | 1% | -10% | -78% | -78% |
| BTC | 701 | 4 | 5% | 3% | -25% | -87% | -89% |
| SOL | 701 | 0 | 3% | 1% | -100% | -93% | -92% |
| NEAR | 699 | 4 | 6% | 3% | -25% | -66% | -67% |
| GOLD | 389 | 0 | 4% | 1% | -100% | -92% | -94% |
| SILVER | 372 | 0 | 2% | 1% | -100% | -96% | -97% |
| WTI | 353 | 2 | 3% | 1% | -39% | -95% | -97% |
| COPPER | 331 | 0 | 1% | 0% | -100% | -99% | -99% |
| PLATINUM | 295 | 0 | 0% | 0% | -100% | -100% | -100% |
| NATGAS | 287 | 2 | 3% | 2% | -35% | -95% | -93% |
| PALLADIUM | 282 | 1 | 2% | 1% | -67% | -97% | -98% |
| EURUSD | 270 | 1 | 4% | 3% | -65% | -93% | -91% |
| GBPUSD | 258 | 1 | 3% | 2% | -64% | -94% | -94% |
| USDJPY | 218 | 3 | 2% | 1% | +28% | -97% | -95% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 4747 | 22 | 4% | 2% | -46% | -89% | -88% |
| DOWN (bought NO) | 4657 | 22 | 4% | 2% | -46% | -90% | -91% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 1043 | 7 | 2% | 1% | +15% | -61% | -61% |
| 0.05–0.1% | 1088 | 4 | 3% | 1% | -46% | -91% | -92% |
| 0.1–0.2% | 1587 | 6 | 4% | 2% | -52% | -91% | -91% |
| 0.2–0.5% | 1865 | 12 | 6% | 3% | -29% | -88% | -87% |
| Over 0.5% | 764 | 5 | 7% | 3% | -33% | -87% | -89% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 2464 | 14 | 4% | 2% | -34% | -87% | -87% |
| Morning (6am–12pm) | 2361 | 17 | 5% | 3% | -18% | -90% | -88% |
| Afternoon (12–6pm) | 1943 | 6 | 3% | 1% | -63% | -86% | -88% |
| Evening (6pm–12am) | 2636 | 7 | 3% | 1% | -69% | -94% | -94% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 25 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,050 |
| Time from buy to best bounce (bounced bets) | 49 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/6 3:59:44 AM | BNB | DOWN | 16 sec | -0.023% | 0¢ | ❌ Lost | $0.00 |
| 10/6 3:59:11 AM | XRP | DOWN | 48 sec | +0.060% | 1¢ | ❌ Lost | -$0.15 |
| 10/6 3:58:55 AM | BTC | DOWN | 65 sec | +0.111% | 0¢ | ❌ Lost | $0.00 |
| 10/6 3:58:55 AM | GBPUSD | DOWN | 65 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/6 3:58:39 AM | SOL | DOWN | 81 sec | +0.152% | 1¢ | ❌ Lost | -$0.15 |
| 10/6 3:58:39 AM | DOGE | DOWN | 81 sec | +0.142% | 0¢ | ❌ Lost | -$0.15 |
| 10/6 3:58:23 AM | WTI | DOWN | 1.6 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/6 3:58:23 AM | COPPER | UP | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/6 3:58:06 AM | PALLADIUM | UP | 1.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/6 3:58:06 AM | SILVER | UP | 1.9 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/6 3:57:33 AM | ETH | DOWN | 2.5 min | +0.251% | 1¢ | ❌ Lost | -$0.15 |
| 10/6 3:57:01 AM | PLATINUM | UP | 3.0 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/6 3:56:28 AM | ZEC | DOWN | 3.5 min | +0.723% | 1¢ | ❌ Lost | -$0.15 |
| 10/6 3:55:56 AM | HYPE | DOWN | 4.1 min | +0.307% | 2¢ | ❌ Lost | -$0.15 |
| 10/6 3:55:39 AM | NEAR | DOWN | 4.3 min | +0.767% | 1¢ | ❌ Lost | -$0.15 |
| 10/6 3:44:24 AM | GOLD | UP | 36 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/6 3:44:09 AM | GBPUSD | UP | 50 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/6 3:43:53 AM | COPPER | UP | 67 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/6 3:42:30 AM | HYPE | DOWN | 2.5 min | +0.255% | 1¢ | ❌ Lost | -$0.15 |
| 10/6 3:42:14 AM | XRP | DOWN | 2.8 min | +0.274% | 1¢ | ❌ Lost | -$0.15 |
| 10/6 3:42:14 AM | BNB | DOWN | 2.8 min | +0.142% | 0¢ | ❌ Lost | -$0.15 |
| 10/6 3:42:00 AM | BTC | DOWN | 3.0 min | +0.195% | 1¢ | ❌ Lost | -$0.15 |
| 10/6 3:42:00 AM | NEAR | DOWN | 3.0 min | +0.610% | 0¢ | ❌ Lost | -$0.15 |
| 10/6 3:42:00 AM | SOL | DOWN | 3.0 min | +0.319% | 0¢ | ❌ Lost | -$0.15 |
| 10/6 3:41:42 AM | ETH | DOWN | 3.3 min | +0.316% | 1¢ | ❌ Lost | -$0.15 |
| 10/6 3:41:42 AM | ZEC | DOWN | 3.3 min | +0.785% | 1¢ | ❌ Lost | -$0.15 |
| 10/6 3:41:42 AM | DOGE | DOWN | 3.3 min | +0.353% | 1¢ | ❌ Lost | -$0.15 |
| 10/6 3:40:55 AM | WTI | UP | 4.1 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/6 3:29:53 AM | NATGAS | UP | 6 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/6 3:29:21 AM | EURUSD | DOWN | 39 sec | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
