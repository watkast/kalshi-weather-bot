# 15-Minute 1¢ Study

*Updated Tue Oct 6, 5:39 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 654 finished bets | 1% | $27.80 | +40% | +4.25¢ | -$7.55 / $35.35 |

*Expect about **80 buys a day** (~$11.95/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| 5+ min left, hold to the close | 245 | $19.70 | +54% |
| Mean-reversion model ≥ 5%, hold to the close | 1436 | $15.70 | +9% |
| Momentum model ≥ 5%, hold to the close | 651 | $14.85 | +21% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 9502 | 9496 | 45 (0%) | 1.07% | -$513.15 (-45%) | Hold to the close: -$513.15 (-45%) |

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
| Volatility model | 6206 | 4.1% | 0.5% (32) | -534% | ❌ Worse |
| Momentum model | 6206 | 4.1% | 0.5% (32) | -564% | ❌ Worse |
| Mean-reversion model | 6206 | 6.7% | 0.5% (32) | -616% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 6206 | 32 | -35% | -86% | -86% | -83% |
| Volatility model ≥ 2% | 1213 | 11 | +5% | -71% | -71% | -67% |
| Volatility model ≥ 5% | 654 | 7 | +40% | -59% | -58% | -55% |
| Volatility model ≥ 10% | 401 | 5 | +87% | -40% | -42% | -36% |
| Momentum model ≥ 2% | 1075 | 9 | +1% | -72% | -74% | -72% |
| Momentum model ≥ 5% | 651 | 6 | +21% | -64% | -66% | -64% |
| Momentum model ≥ 10% | 450 | 5 | +60% | -52% | -53% | -50% |
| Mean-reversion model ≥ 2% | 2131 | 18 | -8% | -83% | -83% | -79% |
| Mean-reversion model ≥ 5% | 1436 | 14 | +9% | -80% | -80% | -73% |
| Mean-reversion model ≥ 10% | 948 | 10 | +22% | -78% | -79% | -72% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 6403 | 4% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 2340 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 753 | 3% | 3% | 2% | 1% | 1% | 0% |
| **All** | 9496 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 45 | 0% | -$513.15 | -45% | — |
| Sell at 2¢ | 352 | 4% | -$1,023.63 | -90% | 33 sec |
| Sell at 3¢ | 231 | 2% | -$1,025.06 | -90% | 47 sec |
| Sell at 5¢ | 172 | 2% | -$1,003.35 | -88% | 50 sec |
| Sell at 10¢ | 117 | 1% | -$947.88 | -83% | 65 sec |
| Sell at 25¢ | 67 | 1% | -$851.38 | -74% | 82 sec |
| Sell at 50¢ | 44 | 0% | -$734.15 | -64% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 3 | 0 | 100% | 67% | -100% | +73% | +160% |
| 5–10 min | 242 | 4 | 10% | 3% | +56% | -82% | -88% |
| 2–5 min | 3062 | 24 | 7% | 3% | -23% | -87% | -87% |
| 1–2 min | 2505 | 11 | 3% | 2% | -52% | -94% | -93% |
| Under 1 min | 3684 | 6 | 1% | 0% | -76% | -90% | -90% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 725 | 6 | 5% | 3% | -1% | -89% | -89% |
| HYPE | 715 | 3 | 5% | 3% | -48% | -88% | -87% |
| DOGE | 714 | 2 | 4% | 1% | -64% | -91% | -91% |
| ETH | 712 | 7 | 6% | 3% | +24% | -87% | -86% |
| BNB | 710 | 3 | 4% | 2% | -49% | -90% | -92% |
| XRP | 708 | 5 | 2% | 1% | -11% | -78% | -79% |
| BTC | 707 | 4 | 5% | 3% | -25% | -87% | -89% |
| SOL | 707 | 0 | 3% | 1% | -100% | -93% | -92% |
| NEAR | 705 | 4 | 6% | 3% | -26% | -66% | -67% |
| GOLD | 394 | 0 | 4% | 1% | -100% | -92% | -94% |
| SILVER | 378 | 0 | 2% | 1% | -100% | -96% | -97% |
| WTI | 357 | 2 | 3% | 1% | -39% | -95% | -97% |
| COPPER | 335 | 0 | 1% | 0% | -100% | -99% | -99% |
| PLATINUM | 300 | 0 | 0% | 0% | -100% | -100% | -100% |
| NATGAS | 290 | 3 | 3% | 2% | -3% | -94% | -92% |
| PALLADIUM | 286 | 1 | 2% | 1% | -67% | -97% | -98% |
| EURUSD | 272 | 1 | 4% | 3% | -66% | -93% | -91% |
| GBPUSD | 262 | 1 | 3% | 2% | -64% | -94% | -94% |
| USDJPY | 219 | 3 | 2% | 1% | +28% | -97% | -95% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 4779 | 23 | 4% | 2% | -44% | -89% | -88% |
| DOWN (bought NO) | 4717 | 22 | 4% | 2% | -46% | -90% | -91% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 1054 | 7 | 2% | 1% | +14% | -62% | -61% |
| 0.05–0.1% | 1098 | 4 | 3% | 1% | -46% | -91% | -92% |
| 0.1–0.2% | 1604 | 6 | 4% | 2% | -53% | -91% | -91% |
| 0.2–0.5% | 1880 | 12 | 6% | 3% | -30% | -88% | -87% |
| Over 0.5% | 765 | 5 | 7% | 3% | -33% | -87% | -89% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 2556 | 15 | 4% | 2% | -32% | -87% | -88% |
| Morning (6am–12pm) | 2361 | 17 | 5% | 3% | -18% | -90% | -88% |
| Afternoon (12–6pm) | 1943 | 6 | 3% | 1% | -63% | -86% | -88% |
| Evening (6pm–12am) | 2636 | 7 | 3% | 1% | -69% | -94% | -94% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 25 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,014 |
| Time from buy to best bounce (bounced bets) | 49 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/6 5:29:56 AM | BTC | DOWN | 3 sec | +0.003% | 0¢ | ❌ Lost | $0.00 |
| 10/6 5:29:40 AM | WTI | UP | 19 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/6 5:29:40 AM | DOGE | DOWN | 19 sec | +0.068% | 0¢ | ❌ Lost | $0.00 |
| 10/6 5:29:40 AM | BNB | DOWN | 19 sec | -0.013% | 0¢ | ❌ Lost | $0.00 |
| 10/6 5:29:24 AM | USDJPY | UP | 35 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/6 5:29:24 AM | SOL | UP | 35 sec | -0.029% | 0¢ | ❌ Lost | -$0.15 |
| 10/6 5:29:08 AM | NEAR | UP | 51 sec | -0.410% | 0¢ | ❌ Lost | $0.00 |
| 10/6 5:29:08 AM | ZEC | UP | 51 sec | -0.225% | 0¢ | ❌ Lost | -$0.15 |
| 10/6 5:28:20 AM | GOLD | DOWN | 1.6 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/6 5:28:20 AM | PALLADIUM | DOWN | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/6 5:28:04 AM | NATGAS | DOWN | 1.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/6 5:27:46 AM | ETH | DOWN | 2.2 min | +0.133% | 1¢ | ❌ Lost | -$0.15 |
| 10/6 5:27:30 AM | EURUSD | DOWN | 2.5 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/6 5:27:14 AM | GBPUSD | DOWN | 2.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/6 5:26:59 AM | XRP | DOWN | 3.0 min | +0.305% | 1¢ | ❌ Lost | -$0.15 |
| 10/6 5:26:59 AM | COPPER | DOWN | 3.0 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/6 5:26:11 AM | PLATINUM | DOWN | 3.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/6 5:24:50 AM | HYPE | DOWN | 5.2 min | +0.445% | 1¢ | ❌ Lost | -$0.15 |
| 10/6 5:23:28 AM | SILVER | DOWN | 6.5 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/6 5:14:58 AM | ETH | UP | 2 sec | -0.000% | 0¢ | ❌ Lost | $0.00 |
| 10/6 5:14:58 AM | SOL | DOWN | 2 sec | +0.003% | 0¢ | ❌ Lost | $0.00 |
| 10/6 5:14:58 AM | ZEC | UP | 2 sec | -0.080% | 0¢ | ❌ Lost | $0.00 |
| 10/6 5:14:58 AM | BNB | DOWN | 2 sec | +0.009% | 0¢ | ❌ Lost | -$0.15 |
| 10/6 5:14:58 AM | SILVER | DOWN | 2 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/6 5:14:58 AM | GOLD | DOWN | 2 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/6 5:14:42 AM | NATGAS | UP | 18 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/6 5:14:42 AM | HYPE | UP | 18 sec | -0.036% | 0¢ | ❌ Lost | $0.00 |
| 10/6 5:14:11 AM | BTC | DOWN | 48 sec | +0.074% | 0¢ | ❌ Lost | $0.00 |
| 10/6 5:14:11 AM | XRP | DOWN | 48 sec | +0.080% | 0¢ | ❌ Lost | -$0.15 |
| 10/6 5:13:54 AM | NEAR | DOWN | 65 sec | +0.191% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
