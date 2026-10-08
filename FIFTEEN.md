# 15-Minute 1¢ Study

*Updated Thu Oct 8, 3:19 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 767 finished bets | 1% | $29.35 | +36% | +3.83¢ | -$12.95 / $42.30 |

*Expect about **76 buys a day** (~$11.38/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 761 | $16.85 | +21% |
| 5+ min left, hold to the close | 310 | $10.25 | +22% |
| Volatility model ≥ 5%, sell at 50¢ | 767 | -$0.65 | -1% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 11509 | 11502 | 49 (0%) | 1.07% | -$710.35 (-51%) | Hold to the close: -$710.35 (-51%) |

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
| Volatility model | 7406 | 4.0% | 0.4% (33) | -564% | ❌ Worse |
| Momentum model | 7406 | 4.1% | 0.4% (33) | -595% | ❌ Worse |
| Mean-reversion model | 7406 | 6.7% | 0.4% (33) | -659% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 7406 | 33 | -44% | -87% | -87% | -85% |
| Volatility model ≥ 2% | 1403 | 12 | -0% | -73% | -73% | -69% |
| Volatility model ≥ 5% | 767 | 8 | +36% | -63% | -62% | -59% |
| Volatility model ≥ 10% | 481 | 6 | +83% | -47% | -47% | -43% |
| Momentum model ≥ 2% | 1245 | 10 | -3% | -74% | -75% | -73% |
| Momentum model ≥ 5% | 761 | 7 | +21% | -67% | -69% | -66% |
| Momentum model ≥ 10% | 527 | 6 | +63% | -57% | -58% | -54% |
| Mean-reversion model ≥ 2% | 2545 | 19 | -19% | -84% | -85% | -80% |
| Mean-reversion model ≥ 5% | 1722 | 15 | -4% | -82% | -81% | -76% |
| Mean-reversion model ≥ 10% | 1139 | 11 | +11% | -80% | -80% | -75% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 7603 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 2915 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 984 | 3% | 2% | 2% | 1% | 1% | 0% |
| **All** | 11502 | 3% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 49 | 0% | -$710.35 | -51% | — |
| Sell at 2¢ | 400 | 3% | -$1,250.35 | -90% | 33 sec |
| Sell at 3¢ | 267 | 2% | -$1,250.22 | -90% | 47 sec |
| Sell at 5¢ | 198 | 2% | -$1,225.65 | -88% | 56 sec |
| Sell at 10¢ | 131 | 1% | -$1,168.74 | -84% | 64 sec |
| Sell at 25¢ | 75 | 1% | -$1,064.10 | -76% | 82 sec |
| Sell at 50¢ | 49 | 0% | -$939.60 | -67% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 306 | 4 | 11% | 4% | +24% | -81% | -84% |
| 2–5 min | 3730 | 25 | 7% | 3% | -35% | -88% | -88% |
| 1–2 min | 3023 | 12 | 3% | 2% | -57% | -94% | -94% |
| Under 1 min | 4439 | 8 | 1% | 0% | -73% | -88% | -88% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 852 | 6 | 5% | 3% | -16% | -90% | -90% |
| HYPE | 851 | 3 | 5% | 3% | -57% | -89% | -88% |
| DOGE | 847 | 2 | 3% | 1% | -70% | -92% | -92% |
| BNB | 846 | 3 | 4% | 2% | -57% | -91% | -92% |
| ETH | 845 | 7 | 5% | 3% | +3% | -89% | -88% |
| NEAR | 842 | 5 | 6% | 3% | -22% | -71% | -72% |
| SOL | 841 | 0 | 3% | 1% | -100% | -93% | -92% |
| BTC | 840 | 4 | 5% | 2% | -37% | -88% | -90% |
| XRP | 839 | 5 | 2% | 1% | -25% | -81% | -81% |
| GOLD | 488 | 0 | 4% | 1% | -100% | -91% | -93% |
| SILVER | 473 | 0 | 3% | 1% | -100% | -95% | -94% |
| WTI | 451 | 3 | 2% | 1% | -27% | -95% | -97% |
| COPPER | 416 | 0 | 1% | 0% | -100% | -99% | -99% |
| PLATINUM | 378 | 0 | 0% | 0% | -100% | -100% | -99% |
| NATGAS | 357 | 3 | 3% | 2% | -22% | -95% | -93% |
| PALLADIUM | 352 | 1 | 1% | 1% | -73% | -98% | -99% |
| EURUSD | 351 | 3 | 3% | 2% | -20% | -67% | -66% |
| GBPUSD | 330 | 1 | 3% | 2% | -72% | -95% | -95% |
| USDJPY | 292 | 3 | 1% | 1% | -4% | -98% | -96% |
| AUDUSD | 6 | 0 | 0% | 0% | -100% | -100% | -100% |
| USDCAD | 5 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 5833 | 26 | 4% | 2% | -48% | -88% | -88% |
| DOWN (bought NO) | 5669 | 23 | 3% | 2% | -53% | -91% | -91% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 1246 | 8 | 2% | 1% | +11% | -66% | -66% |
| 0.05–0.1% | 1299 | 4 | 3% | 1% | -55% | -91% | -92% |
| 0.1–0.2% | 1938 | 6 | 4% | 2% | -61% | -92% | -92% |
| 0.2–0.5% | 2236 | 12 | 6% | 3% | -41% | -89% | -88% |
| Over 0.5% | 882 | 5 | 6% | 2% | -42% | -88% | -90% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 2969 | 17 | 4% | 2% | -34% | -84% | -84% |
| Morning (6am–12pm) | 2706 | 17 | 4% | 2% | -28% | -91% | -90% |
| Afternoon (12–6pm) | 2560 | 7 | 3% | 1% | -68% | -88% | -89% |
| Evening (6pm–12am) | 3267 | 8 | 3% | 1% | -72% | -94% | -94% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 25 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,098 |
| Time from buy to best bounce (bounced bets) | 49 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/8 3:14:02 AM | NEAR | DOWN | 57 sec | +0.409% | 0¢ | ❌ Lost | $0.00 |
| 10/8 3:14:02 AM | HYPE | DOWN | 57 sec | +0.141% | 0¢ | ❌ Lost | -$0.15 |
| 10/8 3:14:02 AM | XRP | DOWN | 57 sec | +0.149% | 0¢ | ❌ Lost | $0.00 |
| 10/8 3:13:29 AM | SOL | DOWN | 1.5 min | +0.149% | 0¢ | ❌ Lost | $0.00 |
| 10/8 3:12:26 AM | ZEC | DOWN | 2.5 min | +0.319% | 1¢ | ❌ Lost | -$0.15 |
| 10/8 3:12:10 AM | EURUSD | UP | 2.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/8 3:12:10 AM | GBPUSD | UP | 2.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/8 3:11:38 AM | BNB | DOWN | 3.4 min | +0.064% | 1¢ | ❌ Lost | -$0.15 |
| 10/8 3:11:06 AM | DOGE | DOWN | 3.9 min | +0.279% | 1¢ | ❌ Lost | -$0.15 |
| 10/8 3:10:34 AM | BTC | DOWN | 4.4 min | +0.214% | 1¢ | ❌ Lost | -$0.15 |
| 10/8 3:10:18 AM | ETH | DOWN | 4.7 min | +0.246% | 1¢ | ❌ Lost | -$0.15 |
| 10/8 12:59:52 AM | COPPER | UP | 8 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/8 12:59:36 AM | HYPE | DOWN | 24 sec | +0.013% | 0¢ | ❌ Lost | $0.00 |
| 10/8 12:59:36 AM | PALLADIUM | UP | 24 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/8 12:59:36 AM | GOLD | UP | 24 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/8 12:58:31 AM | WTI | DOWN | 88 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/8 12:58:15 AM | ZEC | DOWN | 1.7 min | +0.324% | 0¢ | ❌ Lost | $0.00 |
| 10/8 12:57:59 AM | GBPUSD | UP | 2.0 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/8 12:57:59 AM | BNB | DOWN | 2.0 min | +0.048% | 1¢ | ❌ Lost | -$0.15 |
| 10/8 12:55:16 AM | NEAR | DOWN | 4.7 min | +1.114% | 1¢ | ❌ Lost | -$0.15 |
| 10/8 12:55:16 AM | BTC | DOWN | 4.7 min | +0.254% | 1¢ | ❌ Lost | -$0.15 |
| 10/8 12:55:00 AM | XRP | DOWN | 5.0 min | +0.521% | 2¢ | ❌ Lost | -$0.15 |
| 10/8 12:55:00 AM | SOL | DOWN | 5.0 min | +0.497% | 1¢ | ❌ Lost | -$0.15 |
| 10/8 12:55:00 AM | EURUSD | UP | 5.0 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/8 12:54:45 AM | DOGE | DOWN | 5.2 min | +0.411% | 9¢ | ❌ Lost | -$0.15 |
| 10/8 12:54:29 AM | ETH | DOWN | 5.5 min | +0.250% | 1¢ | ❌ Lost | -$0.15 |
| 10/8 12:44:51 AM | USDCAD | UP | 8 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/8 12:44:51 AM | NATGAS | DOWN | 8 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/8 12:44:51 AM | AUDUSD | DOWN | 8 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/8 12:44:19 AM | ZEC | DOWN | 40 sec | +0.203% | 0¢ | ❌ Lost | $0.00 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
