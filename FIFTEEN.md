# 15-Minute 1¢ Study

*Updated Wed Nov 11, 5:48 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 4221 finished bets | 1% | $175.10 | +37% | +4.15¢ | $85.15 / $89.95 |

*Expect about **94 buys a day** (~$14.15/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 3949 | $104.20 | +24% |
| Volatility model ≥ 2%, hold to the close | 7753 | $46.70 | +5% |
| Momentum model ≥ 2%, hold to the close | 6440 | -$12.40 | -2% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 54038 | 54017 | 206 (0%) | 1.07% | -$3,705.20 (-56%) | Hold to the close: -$3,705.20 (-56%) |

*In play or awaiting result: 9. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 32491 | 4.7% | 0.4% (132) | -668% | ❌ Worse |
| Momentum model | 32491 | 4.6% | 0.4% (132) | -693% | ❌ Worse |
| Mean-reversion model | 32491 | 8.1% | 0.4% (132) | -811% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 32491 | 132 | -48% | -87% | -87% | -84% |
| Volatility model ≥ 2% | 7753 | 70 | +5% | -77% | -76% | -72% |
| Volatility model ≥ 5% | 4221 | 46 | +37% | -72% | -70% | -67% |
| Volatility model ≥ 10% | 2438 | 28 | +65% | -62% | -61% | -57% |
| Momentum model ≥ 2% | 6440 | 52 | -2% | -78% | -77% | -74% |
| Momentum model ≥ 5% | 3949 | 38 | +24% | -74% | -73% | -69% |
| Momentum model ≥ 10% | 2589 | 25 | +36% | -66% | -65% | -61% |
| Mean-reversion model ≥ 2% | 13421 | 92 | -25% | -82% | -82% | -79% |
| Mean-reversion model ≥ 5% | 9381 | 78 | -8% | -80% | -79% | -76% |
| Mean-reversion model ≥ 10% | 6266 | 56 | +2% | -77% | -77% | -74% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 32696 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 12935 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 8386 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 54017 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 206 | 0% | -$3,705.20 | -56% | — |
| Sell at 2¢ | 2150 | 4% | -$5,750.20 | -87% | 47 sec |
| Sell at 3¢ | 1465 | 3% | -$5,737.85 | -87% | 48 sec |
| Sell at 5¢ | 1015 | 2% | -$5,621.45 | -85% | 63 sec |
| Sell at 10¢ | 613 | 1% | -$5,394.17 | -82% | 65 sec |
| Sell at 25¢ | 326 | 1% | -$5,006.14 | -76% | 82 sec |
| Sell at 50¢ | 213 | 0% | -$4,535.45 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 12 | 0 | 25% | 17% | -100% | -57% | -35% |
| 5–10 min | 2698 | 13 | 11% | 4% | -54% | -81% | -83% |
| 2–5 min | 17474 | 95 | 7% | 3% | -46% | -87% | -87% |
| 1–2 min | 13647 | 45 | 3% | 2% | -63% | -92% | -92% |
| Under 1 min | 20186 | 53 | 1% | 0% | -63% | -85% | -85% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 3659 | 17 | 5% | 2% | -40% | -88% | -87% |
| SOL | 3656 | 16 | 4% | 2% | -44% | -87% | -86% |
| HYPE | 3649 | 11 | 5% | 2% | -62% | -89% | -88% |
| BNB | 3641 | 19 | 5% | 2% | -34% | -86% | -85% |
| DOGE | 3637 | 8 | 4% | 2% | -72% | -90% | -90% |
| ETH | 3631 | 16 | 7% | 3% | -45% | -82% | -81% |
| NEAR | 3612 | 17 | 5% | 2% | -39% | -85% | -85% |
| BTC | 3611 | 17 | 5% | 2% | -35% | -87% | -88% |
| XRP | 3600 | 13 | 3% | 1% | -55% | -89% | -89% |
| GOLD | 1946 | 5 | 5% | 2% | -69% | -81% | -83% |
| WTI | 1935 | 6 | 4% | 2% | -63% | -91% | -92% |
| SILVER | 1897 | 8 | 5% | 2% | -50% | -83% | -83% |
| PLATINUM | 1725 | 4 | 2% | 1% | -78% | -96% | -95% |
| EURUSD | 1662 | 5 | 2% | 1% | -72% | -90% | -90% |
| COPPER | 1612 | 6 | 2% | 1% | -65% | -74% | -74% |
| GBPUSD | 1588 | 6 | 2% | 1% | -65% | -96% | -96% |
| NATGAS | 1585 | 8 | 2% | 1% | -53% | -79% | -78% |
| USDJPY | 1564 | 6 | 2% | 1% | -64% | -97% | -96% |
| PALLADIUM | 1551 | 4 | 1% | 1% | -76% | -92% | -92% |
| AUDUSD | 1120 | 6 | 2% | 1% | -50% | -88% | -88% |
| USDCAD | 1086 | 0 | 2% | 1% | -100% | -96% | -96% |
| BRENT | 684 | 0 | 2% | 1% | -100% | -97% | -97% |
| 10YRRATE | 353 | 2 | 4% | 2% | -47% | -66% | -64% |
| 2YRRATE | 338 | 4 | 4% | 2% | +10% | -38% | -36% |
| 30YRRATE | 332 | 0 | 2% | 1% | -100% | -96% | -94% |
| 5YRRATE | 311 | 2 | 4% | 2% | -40% | -93% | -95% |
| INX | 32 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 27402 | 108 | 4% | 2% | -55% | -88% | -88% |
| DOWN (bought NO) | 26615 | 98 | 4% | 2% | -58% | -86% | -87% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 5182 | 25 | 2% | 1% | -15% | -77% | -77% |
| 0.05–0.1% | 5551 | 20 | 3% | 2% | -45% | -91% | -91% |
| 0.1–0.2% | 8392 | 31 | 5% | 2% | -53% | -89% | -89% |
| 0.2–0.5% | 9829 | 41 | 6% | 3% | -53% | -87% | -86% |
| Over 0.5% | 3734 | 17 | 7% | 3% | -53% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 13236 | 43 | 4% | 2% | -63% | -88% | -88% |
| Morning (6am–12pm) | 13083 | 60 | 4% | 2% | -48% | -85% | -84% |
| Afternoon (12–6pm) | 13110 | 58 | 4% | 2% | -48% | -86% | -86% |
| Evening (6pm–12am) | 14588 | 45 | 4% | 2% | -65% | -90% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,871 |
| Time from buy to best bounce (bounced bets) | 50 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/11 5:44:43 PM | BTC | UP | 17 sec | -0.015% | 0¢ | ❌ Lost | -$0.15 |
| 11/11 5:44:43 PM | SOL | DOWN | 17 sec | +0.018% | 0¢ | ❌ Lost | -$0.15 |
| 11/11 5:44:43 PM | WTI | DOWN | 17 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 11/11 5:44:27 PM | ETH | DOWN | 33 sec | +0.059% | 0¢ | ❌ Lost | $0.00 |
| 11/11 5:44:27 PM | HYPE | DOWN | 33 sec | +0.115% | 0¢ | ❌ Lost | $0.00 |
| 11/11 5:44:27 PM | USDJPY | DOWN | 33 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/11 5:44:11 PM | DOGE | DOWN | 49 sec | +0.118% | 0¢ | ❌ Lost | -$0.15 |
| 11/11 5:44:11 PM | BNB | DOWN | 49 sec | +0.065% | 0¢ | ❌ Lost | $0.00 |
| 11/11 5:43:56 PM | NEAR | DOWN | 63 sec | +0.258% | 0¢ | ❌ Lost | -$0.15 |
| 11/11 5:43:37 PM | PLATINUM | DOWN | 83 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/11 5:43:21 PM | GOLD | DOWN | 1.6 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/11 5:42:50 PM | ZEC | DOWN | 2.2 min | +0.606% | 1¢ | ❌ Lost | -$0.15 |
| 11/11 5:42:32 PM | XRP | DOWN | 2.5 min | +0.285% | 1¢ | ❌ Lost | -$0.15 |
| 11/11 5:41:26 PM | AUDUSD | UP | 3.5 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/11 4:14:25 PM | WTI | UP | 34 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/11 4:13:37 PM | GBPUSD | DOWN | 83 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/11 4:13:21 PM | BRENT | UP | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/11 4:13:05 PM | NEAR | UP | 1.9 min | -1.182% | 0¢ | ❌ Lost | -$0.15 |
| 11/11 4:12:50 PM | NATGAS | UP | 2.1 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/11 4:12:50 PM | ZEC | UP | 2.1 min | -1.004% | 1¢ | ❌ Lost | -$0.15 |
| 11/11 4:12:18 PM | USDCAD | UP | 2.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/11 4:12:18 PM | ETH | UP | 2.7 min | -0.438% | 0¢ | ❌ Lost | $0.00 |
| 11/11 4:12:18 PM | BNB | UP | 2.7 min | -0.185% | 0¢ | ❌ Lost | -$0.15 |
| 11/11 4:12:18 PM | DOGE | UP | 2.7 min | -0.763% | 0¢ | ❌ Lost | $0.00 |
| 11/11 4:12:02 PM | XRP | UP | 3.0 min | -0.579% | 0¢ | ❌ Lost | -$0.15 |
| 11/11 4:12:02 PM | EURUSD | DOWN | 3.0 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/11 4:12:02 PM | USDJPY | UP | 3.0 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/11 4:11:46 PM | BTC | UP | 3.2 min | -0.312% | 0¢ | ❌ Lost | -$0.15 |
| 11/11 4:11:14 PM | SOL | UP | 3.8 min | -0.659% | 1¢ | ❌ Lost | -$0.15 |
| 11/11 4:10:58 PM | HYPE | UP | 4.0 min | -0.725% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
