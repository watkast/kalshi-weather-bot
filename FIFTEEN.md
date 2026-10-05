# 15-Minute 1¢ Study

*Updated Mon Oct 5, 7:26 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 590 finished bets | 1% | $34.55 | +54% | +5.86¢ | -$18.40 / $52.95 |

*Expect about **81 buys a day** (~$12.16/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Volatility model ≥ 2%, hold to the close | 1098 | $21.85 | +17% |
| Momentum model ≥ 5%, hold to the close | 588 | $21.45 | +34% |
| 5+ min left, hold to the close | 215 | $10.20 | +32% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 8505 | 8497 | 37 (0%) | 1.07% | -$503.20 (-49%) | Hold to the close: -$503.20 (-49%) |

*In play or awaiting result: 8. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 5615 | 4.1% | 0.4% (25) | -597% | ❌ Worse |
| Momentum model | 5615 | 4.2% | 0.4% (25) | -622% | ❌ Worse |
| Mean-reversion model | 5615 | 6.8% | 0.4% (25) | -699% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 5615 | 25 | -44% | -85% | -85% | -83% |
| Volatility model ≥ 2% | 1098 | 11 | +17% | -69% | -69% | -64% |
| Volatility model ≥ 5% | 590 | 7 | +54% | -56% | -55% | -50% |
| Volatility model ≥ 10% | 366 | 5 | +102% | -36% | -37% | -31% |
| Momentum model ≥ 2% | 962 | 8 | +1% | -70% | -72% | -69% |
| Momentum model ≥ 5% | 588 | 6 | +34% | -61% | -63% | -60% |
| Momentum model ≥ 10% | 409 | 5 | +75% | -48% | -48% | -45% |
| Mean-reversion model ≥ 2% | 1947 | 14 | -22% | -83% | -84% | -79% |
| Mean-reversion model ≥ 5% | 1306 | 12 | +2% | -79% | -79% | -72% |
| Mean-reversion model ≥ 10% | 865 | 9 | +20% | -78% | -78% | -72% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 5812 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 2033 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 652 | 4% | 3% | 2% | 2% | 1% | 0% |
| **All** | 8497 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 37 | 0% | -$503.20 | -49% | — |
| Sell at 2¢ | 329 | 4% | -$907.66 | -89% | 33 sec |
| Sell at 3¢ | 213 | 3% | -$910.13 | -89% | 47 sec |
| Sell at 5¢ | 158 | 2% | -$890.50 | -87% | 61 sec |
| Sell at 10¢ | 106 | 1% | -$840.34 | -82% | 66 sec |
| Sell at 25¢ | 59 | 1% | -$755.91 | -74% | 1.5 min |
| Sell at 50¢ | 36 | 0% | -$666.20 | -65% | 1.8 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 3 | 0 | 100% | 67% | -100% | +73% | +160% |
| 5–10 min | 212 | 3 | 11% | 3% | +34% | -80% | -88% |
| 2–5 min | 2761 | 20 | 7% | 4% | -29% | -87% | -87% |
| 1–2 min | 2234 | 9 | 3% | 2% | -56% | -93% | -93% |
| Under 1 min | 3287 | 5 | 1% | 0% | -77% | -89% | -89% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 657 | 5 | 5% | 3% | -9% | -89% | -89% |
| DOGE | 649 | 2 | 4% | 2% | -60% | -90% | -90% |
| ETH | 648 | 5 | 6% | 3% | -3% | -87% | -86% |
| HYPE | 648 | 3 | 5% | 3% | -43% | -88% | -86% |
| BNB | 645 | 2 | 4% | 2% | -63% | -91% | -93% |
| XRP | 643 | 4 | 2% | 1% | -21% | -76% | -77% |
| SOL | 643 | 0 | 3% | 1% | -100% | -92% | -92% |
| BTC | 641 | 3 | 5% | 2% | -39% | -87% | -90% |
| NEAR | 638 | 3 | 6% | 3% | -39% | -64% | -65% |
| GOLD | 343 | 0 | 4% | 1% | -100% | -91% | -93% |
| SILVER | 330 | 0 | 2% | 1% | -100% | -96% | -96% |
| WTI | 313 | 2 | 3% | 1% | -31% | -94% | -96% |
| COPPER | 288 | 0 | 1% | 0% | -100% | -99% | -99% |
| PLATINUM | 256 | 0 | 0% | 0% | -100% | -100% | -100% |
| NATGAS | 254 | 2 | 4% | 2% | -27% | -94% | -92% |
| PALLADIUM | 249 | 1 | 2% | 1% | -63% | -97% | -98% |
| EURUSD | 233 | 1 | 5% | 3% | -60% | -92% | -90% |
| GBPUSD | 224 | 1 | 4% | 2% | -58% | -94% | -94% |
| USDJPY | 195 | 3 | 2% | 2% | +44% | -96% | -95% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 4288 | 20 | 4% | 2% | -45% | -89% | -88% |
| DOWN (bought NO) | 4209 | 17 | 4% | 2% | -53% | -89% | -90% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 960 | 7 | 2% | 1% | +24% | -58% | -58% |
| 0.05–0.1% | 976 | 2 | 3% | 1% | -70% | -91% | -92% |
| 0.1–0.2% | 1452 | 6 | 4% | 2% | -47% | -91% | -91% |
| 0.2–0.5% | 1720 | 8 | 6% | 3% | -49% | -88% | -87% |
| Over 0.5% | 702 | 4 | 7% | 3% | -42% | -86% | -88% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 2228 | 9 | 4% | 2% | -53% | -86% | -87% |
| Morning (6am–12pm) | 2124 | 17 | 5% | 3% | -8% | -89% | -88% |
| Afternoon (12–6pm) | 1751 | 4 | 3% | 1% | -73% | -86% | -87% |
| Evening (6pm–12am) | 2394 | 7 | 3% | 2% | -66% | -94% | -94% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 25 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,130 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/5 7:25:38 AM | NEAR | UP | 4.4 min | -0.765% | — | In play | — |
| 10/5 7:23:37 AM | COPPER | UP | 6.4 min | — | — | In play | — |
| 10/5 7:14:57 AM | COPPER | UP | 2 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/5 7:14:27 AM | NATGAS | UP | 32 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/5 7:14:17 AM | PALLADIUM | DOWN | 42 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/5 7:14:05 AM | SILVER | DOWN | 54 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/5 7:14:00 AM | GBPUSD | UP | 59 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/5 7:14:00 AM | EURUSD | UP | 59 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/5 7:13:27 AM | GOLD | UP | 1.5 min | — | 0¢ | ❌ Lost | $0.00 |
| 10/5 7:13:15 AM | NEAR | DOWN | 1.7 min | +0.214% | 1¢ | ❌ Lost | -$0.15 |
| 10/5 7:12:30 AM | HYPE | UP | 2.5 min | -0.395% | 0¢ | ❌ Lost | -$0.15 |
| 10/5 7:12:10 AM | ZEC | DOWN | 2.8 min | +0.354% | 0¢ | ❌ Lost | -$0.15 |
| 10/5 7:12:08 AM | DOGE | DOWN | 2.9 min | +0.242% | 1¢ | ❌ Lost | -$0.15 |
| 10/5 7:11:54 AM | SOL | DOWN | 3.1 min | +0.194% | 1¢ | ❌ Lost | -$0.15 |
| 10/5 7:11:28 AM | WTI | UP | 3.5 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/5 7:10:40 AM | XRP | DOWN | 4.3 min | +0.338% | 1¢ | ❌ Lost | -$0.15 |
| 10/5 7:10:32 AM | BTC | DOWN | 4.5 min | +0.256% | 1¢ | ❌ Lost | -$0.15 |
| 10/5 7:10:18 AM | BNB | DOWN | 4.7 min | +0.249% | 1¢ | ❌ Lost | -$0.15 |
| 10/5 7:10:08 AM | ETH | DOWN | 4.9 min | +0.307% | 0¢ | ❌ Lost | -$0.15 |
| 10/5 6:59:50 AM | ZEC | UP | 9 sec | -0.137% | 0¢ | ❌ Lost | $0.00 |
| 10/5 6:59:48 AM | BTC | UP | 11 sec | -0.046% | 0¢ | ❌ Lost | $0.00 |
| 10/5 6:59:34 AM | XRP | DOWN | 25 sec | +0.053% | 0¢ | ❌ Lost | -$0.15 |
| 10/5 6:59:20 AM | GOLD | UP | 39 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/5 6:59:16 AM | BNB | DOWN | 43 sec | +0.032% | 0¢ | ❌ Lost | -$0.15 |
| 10/5 6:58:55 AM | SOL | UP | 64 sec | -0.115% | 1¢ | ❌ Lost | -$0.15 |
| 10/5 6:58:34 AM | HYPE | DOWN | 85 sec | +0.272% | 0¢ | ❌ Lost | -$0.15 |
| 10/5 6:58:32 AM | WTI | UP | 87 sec | — | 3¢ | ❌ Lost | -$0.15 |
| 10/5 6:57:38 AM | DOGE | UP | 2.4 min | -0.227% | 1¢ | ❌ Lost | -$0.15 |
| 10/5 6:56:13 AM | NEAR | DOWN | 3.8 min | +0.363% | 1¢ | ❌ Lost | -$0.15 |
| 10/5 6:44:59 AM | PLATINUM | DOWN | 1 sec | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
