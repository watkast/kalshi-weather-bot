# 15-Minute 1¢ Study

*Updated Sun Nov 15, 11:29 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 4391 finished bets | 1% | $226.20 | +46% | +5.15¢ | $73.75 / $152.45 |

*Expect about **91 buys a day** (~$13.59/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 4138 | $124.75 | +28% |
| Volatility model ≥ 2%, hold to the close | 8167 | $65.55 | +7% |
| Momentum model ≥ 2%, hold to the close | 6786 | $2.95 | +0% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 57716 | 57687 | 222 (0%) | 1.07% | -$3,907.65 (-56%) | Hold to the close: -$3,907.65 (-56%) |

*In play or awaiting result: 17. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 34820 | 4.6% | 0.4% (143) | -641% | ❌ Worse |
| Momentum model | 34820 | 4.5% | 0.4% (143) | -666% | ❌ Worse |
| Mean-reversion model | 34820 | 7.9% | 0.4% (143) | -779% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 34820 | 143 | -47% | -87% | -87% | -85% |
| Volatility model ≥ 2% | 8167 | 75 | +7% | -77% | -76% | -72% |
| Volatility model ≥ 5% | 4391 | 51 | +46% | -72% | -70% | -67% |
| Volatility model ≥ 10% | 2521 | 30 | +71% | -63% | -61% | -58% |
| Momentum model ≥ 2% | 6786 | 56 | +0% | -78% | -78% | -74% |
| Momentum model ≥ 5% | 4138 | 41 | +28% | -74% | -74% | -70% |
| Momentum model ≥ 10% | 2693 | 26 | +36% | -66% | -66% | -62% |
| Mean-reversion model ≥ 2% | 14291 | 100 | -23% | -82% | -82% | -80% |
| Mean-reversion model ≥ 5% | 9948 | 84 | -6% | -80% | -79% | -77% |
| Mean-reversion model ≥ 10% | 6606 | 60 | +3% | -77% | -77% | -75% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 35026 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 13651 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 9010 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 57687 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 222 | 0% | -$3,907.65 | -56% | — |
| Sell at 2¢ | 2320 | 4% | -$6,118.45 | -87% | 47 sec |
| Sell at 3¢ | 1565 | 3% | -$6,111.30 | -87% | 48 sec |
| Sell at 5¢ | 1073 | 2% | -$5,996.20 | -85% | 62 sec |
| Sell at 10¢ | 653 | 1% | -$5,754.22 | -82% | 65 sec |
| Sell at 25¢ | 343 | 1% | -$5,348.32 | -76% | 80 sec |
| Sell at 50¢ | 228 | 0% | -$4,818.65 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 13 | 0 | 31% | 23% | -100% | -47% | -20% |
| 5–10 min | 2888 | 13 | 11% | 4% | -57% | -81% | -82% |
| 2–5 min | 18627 | 100 | 7% | 3% | -47% | -87% | -87% |
| 1–2 min | 14551 | 51 | 3% | 2% | -61% | -92% | -92% |
| Under 1 min | 21608 | 58 | 1% | 0% | -62% | -85% | -85% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 3921 | 19 | 5% | 2% | -37% | -88% | -87% |
| SOL | 3915 | 17 | 4% | 2% | -44% | -86% | -86% |
| HYPE | 3913 | 12 | 4% | 2% | -61% | -89% | -88% |
| DOGE | 3898 | 10 | 4% | 2% | -68% | -90% | -89% |
| BNB | 3896 | 20 | 5% | 2% | -35% | -85% | -85% |
| ETH | 3888 | 16 | 6% | 3% | -49% | -82% | -82% |
| BTC | 3869 | 20 | 5% | 2% | -30% | -86% | -88% |
| NEAR | 3868 | 17 | 5% | 2% | -43% | -85% | -86% |
| XRP | 3858 | 14 | 3% | 2% | -54% | -89% | -89% |
| GOLD | 2047 | 5 | 5% | 2% | -70% | -82% | -84% |
| WTI | 2031 | 7 | 4% | 2% | -58% | -91% | -92% |
| SILVER | 1988 | 9 | 5% | 2% | -46% | -83% | -83% |
| PLATINUM | 1809 | 4 | 3% | 1% | -79% | -95% | -95% |
| EURUSD | 1754 | 6 | 3% | 1% | -68% | -90% | -90% |
| COPPER | 1699 | 6 | 2% | 1% | -67% | -75% | -75% |
| GBPUSD | 1679 | 6 | 2% | 1% | -67% | -96% | -96% |
| NATGAS | 1674 | 9 | 2% | 1% | -50% | -74% | -74% |
| USDJPY | 1646 | 6 | 2% | 1% | -66% | -97% | -96% |
| PALLADIUM | 1626 | 4 | 1% | 0% | -77% | -92% | -93% |
| AUDUSD | 1199 | 6 | 2% | 1% | -53% | -89% | -89% |
| USDCAD | 1162 | 1 | 3% | 1% | -92% | -96% | -96% |
| BRENT | 777 | 0 | 2% | 1% | -100% | -97% | -97% |
| 10YRRATE | 401 | 2 | 4% | 1% | -53% | -70% | -68% |
| 2YRRATE | 384 | 4 | 4% | 2% | -3% | -45% | -43% |
| 30YRRATE | 376 | 0 | 2% | 1% | -100% | -96% | -94% |
| 5YRRATE | 355 | 2 | 4% | 2% | -47% | -93% | -95% |
| INX | 54 | 0 | 2% | 0% | -100% | -97% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 29386 | 112 | 4% | 2% | -56% | -88% | -88% |
| DOWN (bought NO) | 28301 | 110 | 4% | 2% | -55% | -86% | -86% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 5354 | 25 | 2% | 1% | -17% | -77% | -77% |
| 0.05–0.1% | 5793 | 23 | 3% | 2% | -39% | -91% | -91% |
| 0.1–0.2% | 8820 | 34 | 5% | 2% | -51% | -89% | -89% |
| 0.2–0.5% | 10740 | 44 | 6% | 3% | -54% | -86% | -86% |
| Over 0.5% | 4310 | 19 | 7% | 3% | -54% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 14049 | 44 | 4% | 2% | -64% | -88% | -88% |
| Morning (6am–12pm) | 13875 | 67 | 4% | 2% | -45% | -85% | -84% |
| Afternoon (12–6pm) | 13991 | 62 | 4% | 2% | -48% | -87% | -87% |
| Evening (6pm–12am) | 15772 | 49 | 4% | 2% | -64% | -89% | -89% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 5,069 |
| Time from buy to best bounce (bounced bets) | 50 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/15 11:29:23 AM | ETH | UP | 37 sec | -0.115% | — | In play | — |
| 11/15 11:29:23 AM | XRP | UP | 37 sec | -0.095% | — | In play | — |
| 11/15 11:28:51 AM | SOL | UP | 69 sec | -0.385% | — | In play | — |
| 11/15 11:28:21 AM | NEAR | DOWN | 1.6 min | +0.173% | — | In play | — |
| 11/15 11:27:32 AM | DOGE | DOWN | 2.5 min | +0.285% | — | In play | — |
| 11/15 11:27:32 AM | XRP | DOWN | 2.5 min | +0.253% | — | In play | — |
| 11/15 11:27:16 AM | BTC | DOWN | 2.7 min | +0.242% | — | In play | — |
| 11/15 11:26:44 AM | HYPE | DOWN | 3.2 min | +0.336% | — | In play | — |
| 11/15 11:14:55 AM | BTC | DOWN | 4 sec | +0.025% | 0¢ | ❌ Lost | $0.00 |
| 11/15 11:14:25 AM | ZEC | UP | 34 sec | -0.154% | 0¢ | ❌ Lost | $0.00 |
| 11/15 11:14:25 AM | ETH | DOWN | 34 sec | +0.092% | 1¢ | ❌ Lost | -$0.15 |
| 11/15 11:13:54 AM | BNB | UP | 65 sec | -0.086% | 1¢ | ❌ Lost | -$0.15 |
| 11/15 11:13:54 AM | XRP | UP | 65 sec | -0.158% | 0¢ | ❌ Lost | $0.00 |
| 11/15 11:13:46 AM | NEAR | UP | 73 sec | -0.383% | 0¢ | ❌ Lost | $0.00 |
| 11/15 11:13:30 AM | DOGE | UP | 89 sec | -0.169% | 1¢ | ❌ Lost | -$0.15 |
| 11/15 11:13:30 AM | SOL | UP | 89 sec | -0.266% | 1¢ | ❌ Lost | -$0.15 |
| 11/15 11:13:30 AM | HYPE | UP | 89 sec | -0.299% | 1¢ | ❌ Lost | -$0.15 |
| 11/15 10:59:49 AM | HYPE | DOWN | 11 sec | +0.139% | 0¢ | ❌ Lost | $0.00 |
| 11/15 10:59:49 AM | XRP | UP | 11 sec | +0.021% | 1¢ | ❌ Lost | -$0.15 |
| 11/15 10:59:33 AM | SOL | DOWN | 27 sec | +0.032% | 0¢ | ❌ Lost | -$0.15 |
| 11/15 10:59:33 AM | NEAR | UP | 27 sec | -0.204% | 0¢ | ❌ Lost | -$0.15 |
| 11/15 10:59:09 AM | DOGE | DOWN | 50 sec | +0.072% | 1¢ | ❌ Lost | -$0.15 |
| 11/15 10:58:53 AM | BTC | UP | 66 sec | -0.145% | 1¢ | ❌ Lost | -$0.15 |
| 11/15 10:58:37 AM | ETH | DOWN | 82 sec | +0.151% | 1¢ | ❌ Lost | -$0.15 |
| 11/15 10:41:51 AM | ZEC | UP | 3.1 min | -0.731% | 0¢ | ❌ Lost | $0.00 |
| 11/15 10:41:51 AM | SOL | UP | 3.1 min | -0.414% | 4¢ | ❌ Lost | -$0.15 |
| 11/15 10:41:51 AM | XRP | UP | 3.1 min | -0.358% | 11¢ | ❌ Lost | -$0.15 |
| 11/15 10:41:51 AM | NEAR | UP | 3.1 min | -0.646% | 1¢ | ❌ Lost | -$0.15 |
| 11/15 10:41:18 AM | DOGE | UP | 3.7 min | -0.351% | 6¢ | ❌ Lost | -$0.15 |
| 11/15 10:39:43 AM | ETH | UP | 5.3 min | -0.597% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
