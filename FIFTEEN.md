# 15-Minute 1¢ Study

*Updated Tue Oct 6, 4:18 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 648 finished bets | 1% | $28.40 | +41% | +4.38¢ | -$7.40 / $35.80 |

*Expect about **80 buys a day** (~$11.93/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| 5+ min left, hold to the close | 243 | $20.00 | +56% |
| Mean-reversion model ≥ 5%, hold to the close | 1425 | $17.05 | +10% |
| Momentum model ≥ 5%, hold to the close | 644 | $15.45 | +23% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 9423 | 9417 | 44 (0%) | 1.07% | -$518.30 (-46%) | Hold to the close: -$518.30 (-46%) |

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
| Volatility model | 6161 | 4.0% | 0.5% (32) | -528% | ❌ Worse |
| Momentum model | 6161 | 4.1% | 0.5% (32) | -553% | ❌ Worse |
| Mean-reversion model | 6161 | 6.7% | 0.5% (32) | -610% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 6161 | 32 | -34% | -86% | -86% | -83% |
| Volatility model ≥ 2% | 1202 | 11 | +6% | -71% | -71% | -67% |
| Volatility model ≥ 5% | 648 | 7 | +41% | -59% | -58% | -55% |
| Volatility model ≥ 10% | 397 | 5 | +89% | -40% | -41% | -36% |
| Momentum model ≥ 2% | 1062 | 9 | +2% | -72% | -74% | -72% |
| Momentum model ≥ 5% | 644 | 6 | +23% | -64% | -66% | -63% |
| Momentum model ≥ 10% | 445 | 5 | +61% | -52% | -52% | -50% |
| Mean-reversion model ≥ 2% | 2117 | 18 | -7% | -83% | -83% | -78% |
| Mean-reversion model ≥ 5% | 1425 | 14 | +10% | -80% | -80% | -73% |
| Mean-reversion model ≥ 10% | 941 | 10 | +23% | -78% | -78% | -72% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 6358 | 4% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 2312 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 747 | 3% | 3% | 2% | 1% | 1% | 0% |
| **All** | 9417 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 44 | 0% | -$518.30 | -46% | — |
| Sell at 2¢ | 351 | 4% | -$1,015.04 | -89% | 33 sec |
| Sell at 3¢ | 230 | 2% | -$1,016.60 | -90% | 47 sec |
| Sell at 5¢ | 171 | 2% | -$995.15 | -88% | 50 sec |
| Sell at 10¢ | 116 | 1% | -$940.34 | -83% | 65 sec |
| Sell at 25¢ | 66 | 1% | -$845.84 | -75% | 82 sec |
| Sell at 50¢ | 43 | 0% | -$732.05 | -65% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 3 | 0 | 100% | 67% | -100% | +73% | +160% |
| 5–10 min | 240 | 4 | 10% | 3% | +58% | -82% | -88% |
| 2–5 min | 3044 | 24 | 7% | 3% | -23% | -87% | -87% |
| 1–2 min | 2481 | 11 | 3% | 2% | -52% | -94% | -93% |
| Under 1 min | 3649 | 5 | 1% | 0% | -79% | -90% | -90% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 720 | 6 | 5% | 3% | -0% | -89% | -89% |
| HYPE | 710 | 3 | 5% | 3% | -48% | -88% | -86% |
| DOGE | 709 | 2 | 4% | 1% | -64% | -91% | -91% |
| ETH | 707 | 7 | 6% | 3% | +24% | -87% | -86% |
| BNB | 705 | 3 | 4% | 2% | -48% | -90% | -92% |
| XRP | 703 | 5 | 2% | 1% | -10% | -78% | -78% |
| BTC | 702 | 4 | 5% | 3% | -25% | -87% | -89% |
| SOL | 702 | 0 | 3% | 1% | -100% | -93% | -92% |
| NEAR | 700 | 4 | 6% | 3% | -25% | -66% | -67% |
| GOLD | 389 | 0 | 4% | 1% | -100% | -92% | -94% |
| SILVER | 373 | 0 | 2% | 1% | -100% | -96% | -97% |
| WTI | 353 | 2 | 3% | 1% | -39% | -95% | -97% |
| COPPER | 331 | 0 | 1% | 0% | -100% | -99% | -99% |
| PLATINUM | 296 | 0 | 0% | 0% | -100% | -100% | -100% |
| NATGAS | 287 | 2 | 3% | 2% | -35% | -95% | -93% |
| PALLADIUM | 283 | 1 | 2% | 1% | -67% | -97% | -98% |
| EURUSD | 270 | 1 | 4% | 3% | -65% | -93% | -91% |
| GBPUSD | 259 | 1 | 3% | 2% | -64% | -94% | -94% |
| USDJPY | 218 | 3 | 2% | 1% | +28% | -97% | -95% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 4749 | 22 | 4% | 2% | -46% | -89% | -88% |
| DOWN (bought NO) | 4668 | 22 | 4% | 2% | -46% | -90% | -91% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 1043 | 7 | 2% | 1% | +15% | -61% | -61% |
| 0.05–0.1% | 1088 | 4 | 3% | 1% | -46% | -91% | -92% |
| 0.1–0.2% | 1591 | 6 | 4% | 2% | -52% | -91% | -91% |
| 0.2–0.5% | 1869 | 12 | 6% | 3% | -29% | -88% | -87% |
| Over 0.5% | 765 | 5 | 7% | 3% | -33% | -87% | -89% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 2477 | 14 | 4% | 2% | -35% | -87% | -88% |
| Morning (6am–12pm) | 2361 | 17 | 5% | 3% | -18% | -90% | -88% |
| Afternoon (12–6pm) | 1943 | 6 | 3% | 1% | -63% | -86% | -88% |
| Evening (6pm–12am) | 2636 | 7 | 3% | 1% | -69% | -94% | -94% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 25 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,047 |
| Time from buy to best bounce (bounced bets) | 49 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/6 4:14:26 AM | SILVER | UP | 34 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/6 4:14:11 AM | GBPUSD | DOWN | 48 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/6 4:13:53 AM | NEAR | DOWN | 67 sec | +0.276% | 0¢ | ❌ Lost | -$0.15 |
| 10/6 4:13:37 AM | PALLADIUM | DOWN | 83 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/6 4:13:21 AM | ETH | DOWN | 1.6 min | +0.151% | 0¢ | ❌ Lost | -$0.15 |
| 10/6 4:13:21 AM | SOL | DOWN | 1.6 min | +0.397% | 1¢ | ❌ Lost | -$0.15 |
| 10/6 4:12:32 AM | XRP | DOWN | 2.5 min | +0.206% | 1¢ | ❌ Lost | -$0.15 |
| 10/6 4:12:32 AM | HYPE | DOWN | 2.5 min | +0.157% | 1¢ | ❌ Lost | -$0.15 |
| 10/6 4:12:16 AM | BTC | DOWN | 2.7 min | +0.160% | 1¢ | ❌ Lost | -$0.15 |
| 10/6 4:12:01 AM | PLATINUM | UP | 3.0 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/6 4:11:29 AM | BNB | DOWN | 3.5 min | +0.184% | 1¢ | ❌ Lost | -$0.15 |
| 10/6 4:11:29 AM | DOGE | DOWN | 3.5 min | +0.410% | 1¢ | ❌ Lost | -$0.15 |
| 10/6 4:10:40 AM | ZEC | DOWN | 4.3 min | +1.022% | 1¢ | ❌ Lost | -$0.15 |
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

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
