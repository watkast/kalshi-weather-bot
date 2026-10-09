# 15-Minute 1¢ Study

*Updated Thu Oct 8, 10:33 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 835 finished bets | 1% | $35.40 | +39% | +4.24¢ | -$16.70 / $52.10 |

*Expect about **77 buys a day** (~$11.48/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 817 | $24.25 | +28% |
| 5+ min left, hold to the close | 358 | $3.20 | +6% |
| Volatility model ≥ 5%, sell at 50¢ | 835 | -$1.85 | -2% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 12508 | 12501 | 51 (0%) | 1.07% | -$804.75 (-53%) | Hold to the close: -$804.75 (-53%) |

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
| Volatility model | 7977 | 4.0% | 0.4% (35) | -568% | ❌ Worse |
| Momentum model | 7977 | 4.1% | 0.4% (35) | -600% | ❌ Worse |
| Mean-reversion model | 7977 | 6.7% | 0.4% (35) | -665% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 7977 | 35 | -45% | -87% | -88% | -85% |
| Volatility model ≥ 2% | 1531 | 13 | -2% | -74% | -75% | -71% |
| Volatility model ≥ 5% | 835 | 9 | +39% | -66% | -64% | -61% |
| Volatility model ≥ 10% | 512 | 7 | +101% | -49% | -50% | -45% |
| Momentum model ≥ 2% | 1353 | 11 | -2% | -75% | -77% | -74% |
| Momentum model ≥ 5% | 817 | 8 | +28% | -69% | -70% | -67% |
| Momentum model ≥ 10% | 557 | 6 | +55% | -59% | -60% | -56% |
| Mean-reversion model ≥ 2% | 2770 | 20 | -21% | -85% | -85% | -81% |
| Mean-reversion model ≥ 5% | 1870 | 16 | -5% | -82% | -82% | -77% |
| Mean-reversion model ≥ 10% | 1235 | 12 | +12% | -80% | -80% | -75% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 8174 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 3199 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 1128 | 2% | 2% | 2% | 1% | 1% | 0% |
| **All** | 12501 | 3% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 51 | 0% | -$804.75 | -53% | — |
| Sell at 2¢ | 426 | 3% | -$1,365.99 | -90% | 33 sec |
| Sell at 3¢ | 281 | 2% | -$1,367.16 | -90% | 47 sec |
| Sell at 5¢ | 207 | 2% | -$1,342.20 | -88% | 51 sec |
| Sell at 10¢ | 136 | 1% | -$1,284.59 | -85% | 64 sec |
| Sell at 25¢ | 78 | 1% | -$1,176.57 | -77% | 82 sec |
| Sell at 50¢ | 51 | 0% | -$1,048.50 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 354 | 4 | 11% | 3% | +7% | -81% | -85% |
| 2–5 min | 4059 | 26 | 6% | 3% | -37% | -88% | -89% |
| 1–2 min | 3279 | 13 | 3% | 2% | -57% | -94% | -94% |
| Under 1 min | 4805 | 8 | 1% | 0% | -76% | -89% | -89% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 915 | 6 | 4% | 3% | -21% | -90% | -90% |
| HYPE | 914 | 3 | 5% | 3% | -59% | -89% | -88% |
| DOGE | 911 | 2 | 3% | 2% | -72% | -92% | -91% |
| BNB | 911 | 4 | 4% | 2% | -47% | -91% | -92% |
| ETH | 909 | 7 | 5% | 3% | -5% | -89% | -88% |
| NEAR | 905 | 5 | 6% | 2% | -28% | -72% | -74% |
| SOL | 904 | 0 | 3% | 1% | -100% | -94% | -93% |
| BTC | 903 | 4 | 5% | 2% | -42% | -87% | -90% |
| XRP | 902 | 6 | 2% | 1% | -17% | -82% | -82% |
| GOLD | 536 | 0 | 4% | 1% | -100% | -92% | -94% |
| SILVER | 521 | 0 | 3% | 1% | -100% | -94% | -94% |
| WTI | 494 | 3 | 3% | 1% | -32% | -95% | -96% |
| COPPER | 456 | 0 | 1% | 0% | -100% | -99% | -99% |
| PLATINUM | 414 | 0 | 0% | 0% | -100% | -100% | -99% |
| NATGAS | 394 | 3 | 3% | 2% | -29% | -95% | -93% |
| EURUSD | 387 | 3 | 3% | 2% | -28% | -71% | -69% |
| PALLADIUM | 384 | 1 | 1% | 1% | -76% | -98% | -99% |
| GBPUSD | 367 | 1 | 3% | 2% | -75% | -95% | -95% |
| USDJPY | 329 | 3 | 1% | 1% | -15% | -98% | -97% |
| AUDUSD | 23 | 0 | 0% | 0% | -100% | -100% | -100% |
| USDCAD | 22 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 6318 | 27 | 3% | 2% | -51% | -89% | -88% |
| DOWN (bought NO) | 6183 | 24 | 3% | 1% | -55% | -91% | -92% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 1317 | 8 | 2% | 1% | +5% | -68% | -67% |
| 0.05–0.1% | 1374 | 4 | 3% | 1% | -57% | -92% | -92% |
| 0.1–0.2% | 2078 | 7 | 4% | 2% | -58% | -91% | -92% |
| 0.2–0.5% | 2396 | 13 | 5% | 3% | -40% | -89% | -88% |
| Over 0.5% | 1007 | 5 | 6% | 2% | -49% | -88% | -90% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 3090 | 17 | 4% | 2% | -37% | -85% | -85% |
| Morning (6am–12pm) | 3025 | 17 | 4% | 2% | -36% | -91% | -90% |
| Afternoon (12–6pm) | 2853 | 8 | 3% | 1% | -67% | -89% | -90% |
| Evening (6pm–12am) | 3533 | 9 | 3% | 1% | -71% | -95% | -94% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 25 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,094 |
| Time from buy to best bounce (bounced bets) | 49 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/8 10:29:58 PM | SILVER | DOWN | 2 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/8 10:29:43 PM | WTI | UP | 17 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/8 10:29:27 PM | DOGE | UP | 33 sec | -0.028% | 0¢ | ❌ Lost | $0.00 |
| 10/8 10:29:11 PM | ZEC | DOWN | 49 sec | +0.160% | 0¢ | ❌ Lost | $0.00 |
| 10/8 10:29:11 PM | BNB | UP | 49 sec | -0.163% | 0¢ | ❌ Lost | $0.00 |
| 10/8 10:28:55 PM | SOL | UP | 65 sec | -0.092% | 1¢ | ❌ Lost | -$0.15 |
| 10/8 10:28:38 PM | NATGAS | DOWN | 82 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/8 10:28:38 PM | BTC | UP | 82 sec | -0.086% | 1¢ | ❌ Lost | -$0.15 |
| 10/8 10:28:38 PM | XRP | UP | 82 sec | -0.165% | 0¢ | ❌ Lost | -$0.15 |
| 10/8 10:28:22 PM | ETH | UP | 1.6 min | -0.083% | 1¢ | ❌ Lost | -$0.15 |
| 10/8 10:27:51 PM | GOLD | DOWN | 2.1 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/8 10:27:20 PM | USDJPY | DOWN | 2.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/8 10:27:04 PM | HYPE | UP | 2.9 min | -0.236% | 1¢ | ❌ Lost | -$0.15 |
| 10/8 10:25:30 PM | NEAR | UP | 4.5 min | -0.951% | 1¢ | ❌ Lost | -$0.15 |
| 10/8 10:14:45 PM | WTI | UP | 15 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/8 10:14:29 PM | NEAR | DOWN | 31 sec | +0.159% | 0¢ | ❌ Lost | $0.00 |
| 10/8 10:14:29 PM | PALLADIUM | UP | 31 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/8 10:14:13 PM | NATGAS | UP | 47 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/8 10:14:13 PM | DOGE | DOWN | 47 sec | +0.047% | 0¢ | ❌ Lost | $0.00 |
| 10/8 10:14:13 PM | COPPER | DOWN | 47 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/8 10:14:13 PM | HYPE | DOWN | 47 sec | +0.071% | 0¢ | ❌ Lost | $0.00 |
| 10/8 10:14:13 PM | GOLD | DOWN | 47 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/8 10:13:57 PM | ZEC | DOWN | 63 sec | +0.253% | 0¢ | ❌ Lost | -$0.15 |
| 10/8 10:13:41 PM | ETH | DOWN | 78 sec | +0.084% | 1¢ | ❌ Lost | -$0.15 |
| 10/8 10:13:07 PM | BTC | DOWN | 1.9 min | +0.117% | 1¢ | ❌ Lost | -$0.15 |
| 10/8 10:13:07 PM | XRP | DOWN | 1.9 min | +0.122% | 1¢ | ❌ Lost | -$0.15 |
| 10/8 10:12:35 PM | SOL | DOWN | 2.4 min | +0.184% | 1¢ | ❌ Lost | -$0.15 |
| 10/8 10:12:03 PM | BNB | DOWN | 2.9 min | +0.117% | 1¢ | ❌ Lost | -$0.15 |
| 10/8 9:59:52 PM | PLATINUM | DOWN | 8 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/8 9:59:21 PM | XRP | DOWN | 39 sec | +0.021% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
