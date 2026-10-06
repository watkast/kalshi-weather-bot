# 15-Minute 1¢ Study

*Updated Tue Oct 6, 4:38 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 649 finished bets | 1% | $28.40 | +41% | +4.38¢ | -$7.40 / $35.80 |

*Expect about **79 buys a day** (~$11.92/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| 5+ min left, hold to the close | 243 | $20.00 | +56% |
| Mean-reversion model ≥ 5%, hold to the close | 1427 | $16.90 | +9% |
| Momentum model ≥ 5%, hold to the close | 645 | $15.45 | +23% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 9437 | 9431 | 44 (0%) | 1.07% | -$519.50 (-46%) | Hold to the close: -$519.50 (-46%) |

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
| Volatility model | 6170 | 4.1% | 0.5% (32) | -531% | ❌ Worse |
| Momentum model | 6170 | 4.1% | 0.5% (32) | -557% | ❌ Worse |
| Mean-reversion model | 6170 | 6.7% | 0.5% (32) | -613% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 6170 | 32 | -34% | -86% | -86% | -83% |
| Volatility model ≥ 2% | 1205 | 11 | +6% | -71% | -71% | -67% |
| Volatility model ≥ 5% | 649 | 7 | +41% | -59% | -58% | -55% |
| Volatility model ≥ 10% | 398 | 5 | +89% | -40% | -41% | -36% |
| Momentum model ≥ 2% | 1064 | 9 | +2% | -72% | -74% | -72% |
| Momentum model ≥ 5% | 645 | 6 | +23% | -64% | -66% | -63% |
| Momentum model ≥ 10% | 446 | 5 | +61% | -52% | -52% | -50% |
| Mean-reversion model ≥ 2% | 2122 | 18 | -7% | -83% | -83% | -78% |
| Mean-reversion model ≥ 5% | 1427 | 14 | +9% | -80% | -80% | -73% |
| Mean-reversion model ≥ 10% | 942 | 10 | +23% | -78% | -78% | -72% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 6367 | 4% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 2316 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 748 | 3% | 3% | 2% | 1% | 1% | 0% |
| **All** | 9431 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 44 | 0% | -$519.50 | -46% | — |
| Sell at 2¢ | 351 | 4% | -$1,016.24 | -89% | 33 sec |
| Sell at 3¢ | 230 | 2% | -$1,017.80 | -90% | 47 sec |
| Sell at 5¢ | 171 | 2% | -$996.35 | -88% | 50 sec |
| Sell at 10¢ | 116 | 1% | -$941.54 | -83% | 65 sec |
| Sell at 25¢ | 66 | 1% | -$847.04 | -75% | 82 sec |
| Sell at 50¢ | 43 | 0% | -$733.25 | -65% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 3 | 0 | 100% | 67% | -100% | +73% | +160% |
| 5–10 min | 240 | 4 | 10% | 3% | +58% | -82% | -88% |
| 2–5 min | 3046 | 24 | 7% | 3% | -23% | -87% | -87% |
| 1–2 min | 2484 | 11 | 3% | 2% | -52% | -94% | -93% |
| Under 1 min | 3658 | 5 | 1% | 0% | -80% | -90% | -90% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 721 | 6 | 5% | 3% | -1% | -89% | -89% |
| HYPE | 711 | 3 | 5% | 3% | -48% | -88% | -86% |
| DOGE | 710 | 2 | 4% | 1% | -64% | -91% | -91% |
| ETH | 708 | 7 | 6% | 3% | +24% | -87% | -86% |
| BNB | 706 | 3 | 4% | 2% | -49% | -90% | -92% |
| XRP | 704 | 5 | 2% | 1% | -10% | -78% | -78% |
| BTC | 703 | 4 | 5% | 3% | -25% | -87% | -89% |
| SOL | 703 | 0 | 3% | 1% | -100% | -93% | -92% |
| NEAR | 701 | 4 | 6% | 3% | -25% | -66% | -67% |
| GOLD | 390 | 0 | 4% | 1% | -100% | -92% | -94% |
| SILVER | 374 | 0 | 2% | 1% | -100% | -96% | -97% |
| WTI | 354 | 2 | 3% | 1% | -39% | -95% | -97% |
| COPPER | 332 | 0 | 1% | 0% | -100% | -99% | -99% |
| PLATINUM | 296 | 0 | 0% | 0% | -100% | -100% | -100% |
| NATGAS | 287 | 2 | 3% | 2% | -35% | -95% | -93% |
| PALLADIUM | 283 | 1 | 2% | 1% | -67% | -97% | -98% |
| EURUSD | 270 | 1 | 4% | 3% | -65% | -93% | -91% |
| GBPUSD | 260 | 1 | 3% | 2% | -64% | -94% | -94% |
| USDJPY | 218 | 3 | 2% | 1% | +28% | -97% | -95% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 4751 | 22 | 4% | 2% | -46% | -89% | -88% |
| DOWN (bought NO) | 4680 | 22 | 4% | 2% | -46% | -90% | -91% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 1046 | 7 | 2% | 1% | +15% | -61% | -61% |
| 0.05–0.1% | 1089 | 4 | 3% | 1% | -46% | -91% | -92% |
| 0.1–0.2% | 1594 | 6 | 4% | 2% | -52% | -91% | -91% |
| 0.2–0.5% | 1871 | 12 | 6% | 3% | -29% | -88% | -87% |
| Over 0.5% | 765 | 5 | 7% | 3% | -33% | -87% | -89% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 2491 | 14 | 4% | 2% | -35% | -87% | -88% |
| Morning (6am–12pm) | 2361 | 17 | 5% | 3% | -18% | -90% | -88% |
| Afternoon (12–6pm) | 1943 | 6 | 3% | 1% | -63% | -86% | -88% |
| Evening (6pm–12am) | 2636 | 7 | 3% | 1% | -69% | -94% | -94% |

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
| 10/6 4:29:44 AM | GBPUSD | DOWN | 15 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/6 4:29:44 AM | XRP | DOWN | 15 sec | -0.020% | 0¢ | ❌ Lost | $0.00 |
| 10/6 4:29:28 AM | ETH | DOWN | 31 sec | +0.065% | 0¢ | ❌ Lost | $0.00 |
| 10/6 4:29:28 AM | BTC | UP | 31 sec | -0.025% | 0¢ | ❌ Lost | $0.00 |
| 10/6 4:29:28 AM | SOL | DOWN | 31 sec | +0.174% | 0¢ | ❌ Lost | $0.00 |
| 10/6 4:29:28 AM | NEAR | DOWN | 31 sec | +0.199% | 0¢ | ❌ Lost | $0.00 |
| 10/6 4:29:28 AM | WTI | DOWN | 31 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/6 4:29:28 AM | DOGE | DOWN | 31 sec | +0.042% | 0¢ | ❌ Lost | $0.00 |
| 10/6 4:29:12 AM | SILVER | DOWN | 47 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/6 4:28:54 AM | COPPER | DOWN | 66 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/6 4:28:38 AM | GOLD | DOWN | 82 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/6 4:28:22 AM | ZEC | DOWN | 1.6 min | +0.406% | 1¢ | ❌ Lost | -$0.15 |
| 10/6 4:27:17 AM | HYPE | DOWN | 2.7 min | +0.334% | 0¢ | ❌ Lost | -$0.15 |
| 10/6 4:26:12 AM | BNB | UP | 3.8 min | -0.163% | 1¢ | ❌ Lost | -$0.15 |
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

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
