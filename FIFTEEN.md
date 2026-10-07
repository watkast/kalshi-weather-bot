# 15-Minute 1¢ Study

*Updated Tue Oct 6, 9:28 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 705 finished bets | 1% | $36.40 | +48% | +5.16¢ | -$10.10 / $46.50 |

*Expect about **80 buys a day** (~$11.93/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 705 | $23.30 | +31% |
| 5+ min left, hold to the close | 262 | $17.15 | +44% |
| Mean-reversion model ≥ 5%, hold to the close | 1539 | $16.65 | +9% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 10196 | 10186 | 46 (0%) | 1.07% | -$586.90 (-48%) | Hold to the close: -$586.90 (-48%) |

*In play or awaiting result: 10. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 6625 | 4.2% | 0.5% (33) | -562% | ❌ Worse |
| Momentum model | 6625 | 4.2% | 0.5% (33) | -591% | ❌ Worse |
| Mean-reversion model | 6625 | 6.8% | 0.5% (33) | -649% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 6625 | 33 | -37% | -86% | -86% | -84% |
| Volatility model ≥ 2% | 1291 | 12 | +8% | -72% | -72% | -68% |
| Volatility model ≥ 5% | 705 | 8 | +48% | -61% | -60% | -57% |
| Volatility model ≥ 10% | 442 | 6 | +101% | -45% | -46% | -40% |
| Momentum model ≥ 2% | 1152 | 10 | +5% | -73% | -75% | -72% |
| Momentum model ≥ 5% | 705 | 7 | +31% | -66% | -68% | -65% |
| Momentum model ≥ 10% | 490 | 6 | +77% | -55% | -56% | -53% |
| Mean-reversion model ≥ 2% | 2271 | 19 | -9% | -83% | -84% | -79% |
| Mean-reversion model ≥ 5% | 1539 | 15 | +9% | -81% | -80% | -74% |
| Mean-reversion model ≥ 10% | 1022 | 11 | +25% | -79% | -79% | -73% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 6822 | 4% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 2538 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 826 | 3% | 2% | 2% | 1% | 1% | 0% |
| **All** | 10186 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 46 | 0% | -$586.90 | -48% | — |
| Sell at 2¢ | 364 | 4% | -$1,108.26 | -90% | 34 sec |
| Sell at 3¢ | 240 | 2% | -$1,109.30 | -90% | 48 sec |
| Sell at 5¢ | 179 | 2% | -$1,086.55 | -88% | 51 sec |
| Sell at 10¢ | 121 | 1% | -$1,030.39 | -84% | 65 sec |
| Sell at 25¢ | 70 | 1% | -$929.20 | -75% | 82 sec |
| Sell at 50¢ | 46 | 0% | -$808.40 | -66% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 3 | 0 | 100% | 67% | -100% | +73% | +160% |
| 5–10 min | 259 | 4 | 10% | 3% | +46% | -82% | -88% |
| 2–5 min | 3275 | 24 | 7% | 3% | -29% | -87% | -88% |
| 1–2 min | 2669 | 11 | 3% | 2% | -56% | -94% | -94% |
| Under 1 min | 3980 | 7 | 1% | 0% | -74% | -91% | -91% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 771 | 6 | 5% | 3% | -7% | -90% | -89% |
| HYPE | 763 | 3 | 5% | 3% | -52% | -88% | -87% |
| DOGE | 761 | 2 | 3% | 1% | -66% | -92% | -92% |
| ETH | 758 | 7 | 5% | 3% | +16% | -88% | -87% |
| BNB | 756 | 3 | 4% | 2% | -52% | -91% | -92% |
| NEAR | 754 | 5 | 6% | 3% | -13% | -68% | -69% |
| SOL | 754 | 0 | 3% | 1% | -100% | -93% | -92% |
| BTC | 753 | 4 | 5% | 3% | -30% | -87% | -89% |
| XRP | 752 | 5 | 2% | 1% | -16% | -80% | -80% |
| GOLD | 425 | 0 | 4% | 1% | -100% | -92% | -95% |
| SILVER | 412 | 0 | 2% | 1% | -100% | -96% | -96% |
| WTI | 392 | 2 | 3% | 1% | -44% | -95% | -97% |
| COPPER | 365 | 0 | 1% | 0% | -100% | -99% | -99% |
| PLATINUM | 324 | 0 | 0% | 0% | -100% | -99% | -99% |
| NATGAS | 310 | 3 | 3% | 2% | -10% | -94% | -92% |
| PALLADIUM | 310 | 1 | 2% | 1% | -70% | -97% | -98% |
| EURUSD | 299 | 1 | 4% | 2% | -69% | -94% | -92% |
| GBPUSD | 283 | 1 | 3% | 2% | -67% | -94% | -94% |
| USDJPY | 244 | 3 | 2% | 1% | +15% | -97% | -96% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 5158 | 24 | 4% | 2% | -46% | -90% | -89% |
| DOWN (bought NO) | 5028 | 22 | 3% | 2% | -50% | -90% | -91% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 1136 | 8 | 2% | 1% | +20% | -64% | -64% |
| 0.05–0.1% | 1177 | 4 | 3% | 1% | -50% | -91% | -92% |
| 0.1–0.2% | 1722 | 6 | 4% | 2% | -56% | -91% | -92% |
| 0.2–0.5% | 1988 | 12 | 6% | 3% | -34% | -88% | -87% |
| Over 0.5% | 797 | 5 | 7% | 3% | -36% | -88% | -89% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 2570 | 15 | 4% | 2% | -32% | -87% | -88% |
| Morning (6am–12pm) | 2536 | 17 | 5% | 3% | -24% | -90% | -89% |
| Afternoon (12–6pm) | 2244 | 7 | 3% | 1% | -63% | -88% | -89% |
| Evening (6pm–12am) | 2836 | 7 | 3% | 1% | -72% | -94% | -94% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 25 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,095 |
| Time from buy to best bounce (bounced bets) | 49 sec |
| Price snapshots per bet | 41 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/6 9:28:53 PM | ETH | UP | 66 sec | -0.144% | — | In play | — |
| 10/6 9:28:38 PM | SILVER | DOWN | 81 sec | — | — | In play | — |
| 10/6 9:27:50 PM | GOLD | DOWN | 2.2 min | — | — | In play | — |
| 10/6 9:27:17 PM | BNB | DOWN | 2.7 min | +0.140% | — | In play | — |
| 10/6 9:14:48 PM | XRP | DOWN | 12 sec | +0.007% | 0¢ | ❌ Lost | $0.00 |
| 10/6 9:14:48 PM | USDJPY | UP | 12 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/6 9:14:32 PM | SILVER | UP | 28 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/6 9:14:32 PM | ETH | UP | 28 sec | -0.037% | 1¢ | ❌ Lost | -$0.15 |
| 10/6 9:14:32 PM | DOGE | UP | 28 sec | -0.086% | 1¢ | ❌ Lost | -$0.15 |
| 10/6 9:14:16 PM | HYPE | UP | 44 sec | -0.128% | 0¢ | ❌ Lost | $0.00 |
| 10/6 9:14:01 PM | GOLD | UP | 58 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/6 9:14:01 PM | SOL | UP | 58 sec | -0.132% | 1¢ | ❌ Lost | -$0.15 |
| 10/6 9:14:01 PM | WTI | DOWN | 58 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/6 9:14:01 PM | ZEC | UP | 58 sec | -0.300% | 1¢ | ❌ Lost | -$0.15 |
| 10/6 9:13:14 PM | NEAR | UP | 1.8 min | -0.500% | 1¢ | ❌ Lost | -$0.15 |
| 10/6 9:12:58 PM | BTC | DOWN | 2.0 min | +0.164% | 1¢ | ❌ Lost | -$0.15 |
| 10/6 9:12:10 PM | EURUSD | DOWN | 2.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/6 9:11:54 PM | GBPUSD | DOWN | 3.1 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/6 9:10:50 PM | BNB | DOWN | 4.2 min | +0.131% | 2¢ | ❌ Lost | -$0.15 |
| 10/6 8:59:29 PM | EURUSD | DOWN | 30 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/6 8:59:29 PM | COPPER | UP | 30 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/6 8:59:13 PM | ETH | UP | 46 sec | -0.076% | 0¢ | ❌ Lost | $0.00 |
| 10/6 8:59:13 PM | SOL | DOWN | 46 sec | +0.063% | 0¢ | ❌ Lost | $0.00 |
| 10/6 8:58:57 PM | BTC | DOWN | 62 sec | +0.070% | 1¢ | ❌ Lost | -$0.15 |
| 10/6 8:58:42 PM | XRP | DOWN | 78 sec | +0.151% | 1¢ | ❌ Lost | -$0.15 |
| 10/6 8:58:42 PM | NEAR | DOWN | 78 sec | +0.411% | 0¢ | ❌ Lost | $0.00 |
| 10/6 8:58:24 PM | BNB | UP | 1.6 min | -0.142% | 0¢ | ❌ Lost | $0.00 |
| 10/6 8:57:53 PM | ZEC | DOWN | 2.1 min | +0.460% | 0¢ | ❌ Lost | -$0.15 |
| 10/6 8:57:38 PM | HYPE | UP | 2.4 min | -0.269% | 6¢ | ❌ Lost | -$0.15 |
| 10/6 8:57:22 PM | PLATINUM | UP | 2.6 min | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
