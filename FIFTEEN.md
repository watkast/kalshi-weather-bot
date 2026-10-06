# 15-Minute 1¢ Study

*Updated Tue Oct 6, 9:36 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 658 finished bets | 1% | $27.35 | +39% | +4.16¢ | -$7.70 / $35.05 |

*Expect about **79 buys a day** (~$11.79/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| 5+ min left, hold to the close | 245 | $19.70 | +54% |
| Mean-reversion model ≥ 5%, hold to the close | 1443 | $14.80 | +8% |
| Momentum model ≥ 5%, hold to the close | 655 | $14.40 | +21% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 9548 | 9542 | 45 (0%) | 1.07% | -$519.00 (-45%) | Hold to the close: -$519.00 (-45%) |

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
| Volatility model | 6230 | 4.1% | 0.5% (32) | -538% | ❌ Worse |
| Momentum model | 6230 | 4.1% | 0.5% (32) | -567% | ❌ Worse |
| Mean-reversion model | 6230 | 6.7% | 0.5% (32) | -620% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 6230 | 32 | -35% | -86% | -86% | -83% |
| Volatility model ≥ 2% | 1220 | 11 | +5% | -72% | -72% | -67% |
| Volatility model ≥ 5% | 658 | 7 | +39% | -60% | -59% | -55% |
| Volatility model ≥ 10% | 403 | 5 | +87% | -40% | -42% | -37% |
| Momentum model ≥ 2% | 1080 | 9 | +1% | -72% | -74% | -72% |
| Momentum model ≥ 5% | 655 | 6 | +21% | -64% | -66% | -64% |
| Momentum model ≥ 10% | 452 | 5 | +60% | -52% | -53% | -50% |
| Mean-reversion model ≥ 2% | 2140 | 18 | -8% | -83% | -84% | -79% |
| Mean-reversion model ≥ 5% | 1443 | 14 | +8% | -80% | -80% | -73% |
| Mean-reversion model ≥ 10% | 952 | 10 | +22% | -78% | -79% | -72% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 6427 | 4% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 2355 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 760 | 3% | 2% | 2% | 1% | 1% | 0% |
| **All** | 9542 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 45 | 0% | -$519.00 | -45% | — |
| Sell at 2¢ | 354 | 4% | -$1,028.96 | -90% | 33 sec |
| Sell at 3¢ | 233 | 2% | -$1,030.13 | -90% | 47 sec |
| Sell at 5¢ | 174 | 2% | -$1,007.90 | -88% | 50 sec |
| Sell at 10¢ | 119 | 1% | -$951.11 | -83% | 65 sec |
| Sell at 25¢ | 68 | 1% | -$853.92 | -74% | 82 sec |
| Sell at 50¢ | 44 | 0% | -$740.00 | -64% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 3 | 0 | 100% | 67% | -100% | +73% | +160% |
| 5–10 min | 242 | 4 | 10% | 3% | +56% | -82% | -88% |
| 2–5 min | 3078 | 24 | 7% | 3% | -24% | -87% | -87% |
| 1–2 min | 2521 | 11 | 3% | 2% | -53% | -94% | -93% |
| Under 1 min | 3698 | 6 | 1% | 0% | -76% | -90% | -90% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 728 | 6 | 5% | 3% | -1% | -89% | -89% |
| HYPE | 718 | 3 | 5% | 3% | -48% | -89% | -87% |
| DOGE | 717 | 2 | 4% | 1% | -64% | -91% | -91% |
| ETH | 715 | 7 | 6% | 3% | +23% | -87% | -86% |
| BNB | 712 | 3 | 4% | 2% | -49% | -91% | -92% |
| BTC | 710 | 4 | 5% | 3% | -26% | -87% | -89% |
| SOL | 710 | 0 | 3% | 1% | -100% | -93% | -92% |
| XRP | 709 | 5 | 2% | 1% | -11% | -79% | -79% |
| NEAR | 708 | 4 | 6% | 3% | -26% | -66% | -68% |
| GOLD | 396 | 0 | 4% | 1% | -100% | -92% | -94% |
| SILVER | 381 | 0 | 2% | 1% | -100% | -96% | -97% |
| WTI | 359 | 2 | 3% | 1% | -39% | -95% | -97% |
| COPPER | 337 | 0 | 1% | 0% | -100% | -99% | -99% |
| PLATINUM | 303 | 0 | 0% | 0% | -100% | -99% | -99% |
| NATGAS | 291 | 3 | 3% | 2% | -4% | -94% | -92% |
| PALLADIUM | 288 | 1 | 2% | 1% | -68% | -97% | -98% |
| EURUSD | 275 | 1 | 4% | 3% | -66% | -93% | -91% |
| GBPUSD | 264 | 1 | 3% | 2% | -65% | -94% | -94% |
| USDJPY | 221 | 3 | 2% | 1% | +27% | -97% | -95% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 4794 | 23 | 4% | 2% | -44% | -89% | -88% |
| DOWN (bought NO) | 4748 | 22 | 4% | 2% | -47% | -90% | -91% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 1059 | 7 | 2% | 1% | +14% | -62% | -61% |
| 0.05–0.1% | 1102 | 4 | 3% | 1% | -46% | -91% | -92% |
| 0.1–0.2% | 1607 | 6 | 4% | 2% | -53% | -91% | -91% |
| 0.2–0.5% | 1890 | 12 | 6% | 3% | -30% | -88% | -87% |
| Over 0.5% | 767 | 5 | 7% | 3% | -33% | -87% | -89% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 2570 | 15 | 4% | 2% | -32% | -87% | -88% |
| Morning (6am–12pm) | 2393 | 17 | 5% | 3% | -19% | -90% | -89% |
| Afternoon (12–6pm) | 1943 | 6 | 3% | 1% | -63% | -86% | -88% |
| Evening (6pm–12am) | 2636 | 7 | 3% | 1% | -69% | -94% | -94% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 25 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,000 |
| Time from buy to best bounce (bounced bets) | 49 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/6 9:29:34 AM | NEAR | UP | 25 sec | -0.244% | 0¢ | ❌ Lost | $0.00 |
| 10/6 9:29:34 AM | SILVER | DOWN | 25 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/6 9:29:02 AM | BNB | UP | 58 sec | -0.125% | 0¢ | ❌ Lost | -$0.15 |
| 10/6 9:28:44 AM | GBPUSD | DOWN | 76 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/6 9:28:44 AM | NATGAS | UP | 76 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/6 9:28:28 AM | WTI | DOWN | 1.5 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/6 9:28:12 AM | PALLADIUM | DOWN | 1.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/6 9:28:12 AM | PLATINUM | DOWN | 1.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/6 9:27:57 AM | EURUSD | DOWN | 2.0 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/6 9:27:57 AM | COPPER | UP | 2.0 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/6 9:27:25 AM | DOGE | UP | 2.6 min | -0.330% | 1¢ | ❌ Lost | -$0.15 |
| 10/6 9:27:25 AM | SOL | UP | 2.6 min | -0.305% | 1¢ | ❌ Lost | -$0.15 |
| 10/6 9:26:53 AM | HYPE | UP | 3.1 min | -0.389% | 0¢ | ❌ Lost | $0.00 |
| 10/6 9:26:19 AM | XRP | UP | 3.7 min | -0.401% | 1¢ | ❌ Lost | -$0.15 |
| 10/6 9:26:03 AM | ETH | UP | 4.0 min | -0.309% | 1¢ | ❌ Lost | -$0.15 |
| 10/6 9:26:03 AM | BTC | UP | 4.0 min | -0.376% | 1¢ | ❌ Lost | -$0.15 |
| 10/6 9:26:03 AM | ZEC | UP | 4.0 min | -0.692% | 1¢ | ❌ Lost | -$0.15 |
| 10/6 9:14:52 AM | BTC | DOWN | 7 sec | +0.002% | 1¢ | ❌ Lost | -$0.15 |
| 10/6 9:14:36 AM | EURUSD | DOWN | 23 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/6 9:14:36 AM | BNB | DOWN | 23 sec | -0.028% | 0¢ | ❌ Lost | $0.00 |
| 10/6 9:14:36 AM | ETH | DOWN | 23 sec | +0.032% | 0¢ | ❌ Lost | -$0.15 |
| 10/6 9:14:36 AM | SOL | DOWN | 23 sec | +0.008% | 1¢ | ❌ Lost | -$0.15 |
| 10/6 9:14:20 AM | USDJPY | DOWN | 39 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/6 9:14:04 AM | DOGE | UP | 55 sec | -0.064% | 1¢ | ❌ Lost | -$0.15 |
| 10/6 9:13:49 AM | ZEC | DOWN | 71 sec | +0.254% | 0¢ | ❌ Lost | $0.00 |
| 10/6 9:13:33 AM | NEAR | DOWN | 87 sec | +0.235% | 1¢ | ❌ Lost | -$0.15 |
| 10/6 9:13:17 AM | HYPE | DOWN | 1.7 min | +0.151% | 1¢ | ❌ Lost | -$0.15 |
| 10/6 9:13:17 AM | PLATINUM | DOWN | 1.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/6 9:12:45 AM | SILVER | DOWN | 2.2 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/6 9:12:45 AM | GOLD | DOWN | 2.2 min | — | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
