# 15-Minute 1¢ Study

*Updated Thu Oct 8, 3:47 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 805 finished bets | 1% | $39.00 | +45% | +4.84¢ | -$14.90 / $53.90 |

*Expect about **76 buys a day** (~$11.36/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 801 | $25.90 | +30% |
| 5+ min left, hold to the close | 350 | $4.40 | +9% |
| Volatility model ≥ 2%, hold to the close | 1482 | $3.20 | +2% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 12111 | 12104 | 50 (0%) | 1.07% | -$769.25 (-52%) | Hold to the close: -$769.25 (-52%) |

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
| Volatility model | 7745 | 4.0% | 0.4% (34) | -562% | ❌ Worse |
| Momentum model | 7745 | 4.1% | 0.4% (34) | -595% | ❌ Worse |
| Mean-reversion model | 7745 | 6.7% | 0.4% (34) | -658% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 7745 | 34 | -45% | -87% | -87% | -85% |
| Volatility model ≥ 2% | 1482 | 13 | +2% | -74% | -74% | -70% |
| Volatility model ≥ 5% | 805 | 9 | +45% | -64% | -63% | -60% |
| Volatility model ≥ 10% | 496 | 7 | +108% | -48% | -48% | -43% |
| Momentum model ≥ 2% | 1314 | 11 | +1% | -75% | -77% | -74% |
| Momentum model ≥ 5% | 801 | 8 | +30% | -69% | -70% | -67% |
| Momentum model ≥ 10% | 546 | 6 | +57% | -58% | -59% | -56% |
| Mean-reversion model ≥ 2% | 2678 | 20 | -19% | -84% | -85% | -81% |
| Mean-reversion model ≥ 5% | 1807 | 16 | -2% | -82% | -81% | -76% |
| Mean-reversion model ≥ 10% | 1194 | 12 | +16% | -80% | -80% | -74% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 7942 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 3093 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 1069 | 2% | 2% | 2% | 1% | 1% | 0% |
| **All** | 12104 | 3% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 50 | 0% | -$769.25 | -52% | — |
| Sell at 2¢ | 417 | 3% | -$1,318.83 | -90% | 33 sec |
| Sell at 3¢ | 275 | 2% | -$1,320.00 | -90% | 47 sec |
| Sell at 5¢ | 203 | 2% | -$1,295.30 | -88% | 50 sec |
| Sell at 10¢ | 132 | 1% | -$1,240.33 | -84% | 64 sec |
| Sell at 25¢ | 76 | 1% | -$1,133.69 | -77% | 82 sec |
| Sell at 50¢ | 50 | 0% | -$1,005.75 | -68% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 346 | 4 | 11% | 3% | +10% | -81% | -85% |
| 2–5 min | 3936 | 25 | 6% | 3% | -38% | -88% | -89% |
| 1–2 min | 3160 | 13 | 3% | 2% | -56% | -94% | -94% |
| Under 1 min | 4658 | 8 | 1% | 0% | -75% | -89% | -89% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 890 | 6 | 4% | 3% | -19% | -90% | -90% |
| HYPE | 888 | 3 | 5% | 2% | -58% | -89% | -88% |
| DOGE | 885 | 2 | 3% | 2% | -71% | -92% | -91% |
| BNB | 884 | 3 | 4% | 2% | -59% | -91% | -92% |
| ETH | 883 | 7 | 5% | 2% | -2% | -89% | -88% |
| NEAR | 879 | 5 | 6% | 3% | -26% | -72% | -73% |
| SOL | 879 | 0 | 3% | 1% | -100% | -94% | -92% |
| BTC | 878 | 4 | 5% | 2% | -40% | -87% | -90% |
| XRP | 876 | 6 | 2% | 1% | -14% | -81% | -81% |
| GOLD | 514 | 0 | 4% | 1% | -100% | -91% | -94% |
| SILVER | 501 | 0 | 3% | 1% | -100% | -95% | -94% |
| WTI | 478 | 3 | 3% | 1% | -30% | -95% | -97% |
| COPPER | 440 | 0 | 1% | 0% | -100% | -99% | -99% |
| PLATINUM | 403 | 0 | 0% | 0% | -100% | -100% | -99% |
| NATGAS | 383 | 3 | 3% | 2% | -27% | -95% | -93% |
| PALLADIUM | 374 | 1 | 1% | 1% | -75% | -98% | -99% |
| EURUSD | 370 | 3 | 3% | 2% | -24% | -69% | -68% |
| GBPUSD | 351 | 1 | 3% | 2% | -73% | -95% | -95% |
| USDJPY | 315 | 3 | 1% | 1% | -11% | -98% | -97% |
| AUDUSD | 17 | 0 | 0% | 0% | -100% | -100% | -100% |
| USDCAD | 16 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 6163 | 26 | 3% | 2% | -51% | -89% | -88% |
| DOWN (bought NO) | 5941 | 24 | 3% | 2% | -54% | -91% | -91% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 1284 | 8 | 2% | 1% | +8% | -67% | -66% |
| 0.05–0.1% | 1334 | 4 | 3% | 1% | -56% | -92% | -92% |
| 0.1–0.2% | 2010 | 7 | 4% | 2% | -56% | -92% | -92% |
| 0.2–0.5% | 2329 | 12 | 5% | 3% | -43% | -89% | -88% |
| Over 0.5% | 983 | 5 | 6% | 2% | -48% | -88% | -90% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 3090 | 17 | 4% | 2% | -37% | -85% | -85% |
| Morning (6am–12pm) | 3025 | 17 | 4% | 2% | -36% | -91% | -90% |
| Afternoon (12–6pm) | 2722 | 8 | 3% | 1% | -65% | -89% | -89% |
| Evening (6pm–12am) | 3267 | 8 | 3% | 1% | -72% | -94% | -94% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 25 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,046 |
| Time from buy to best bounce (bounced bets) | 49 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/8 3:44:49 PM | BNB | DOWN | 10 sec | -0.033% | 0¢ | ❌ Lost | -$0.15 |
| 10/8 3:44:33 PM | ETH | DOWN | 26 sec | -0.005% | 0¢ | ❌ Lost | $0.00 |
| 10/8 3:44:33 PM | WTI | UP | 26 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/8 3:44:33 PM | DOGE | UP | 26 sec | -0.025% | 0¢ | ❌ Lost | -$0.15 |
| 10/8 3:44:17 PM | NATGAS | UP | 42 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/8 3:44:01 PM | NEAR | DOWN | 59 sec | +0.243% | 0¢ | ❌ Lost | $0.00 |
| 10/8 3:44:01 PM | ZEC | DOWN | 59 sec | +0.139% | 0¢ | ❌ Lost | $0.00 |
| 10/8 3:44:01 PM | BTC | DOWN | 59 sec | +0.026% | 4¢ | ❌ Lost | -$0.15 |
| 10/8 3:43:30 PM | SOL | DOWN | 1.5 min | +0.158% | 1¢ | ❌ Lost | -$0.15 |
| 10/8 3:42:41 PM | XRP | UP | 2.3 min | -0.254% | 1¢ | ❌ Lost | -$0.15 |
| 10/8 3:29:46 PM | DOGE | UP | 14 sec | +0.004% | 0¢ | ❌ Lost | -$0.15 |
| 10/8 3:29:30 PM | USDJPY | UP | 30 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/8 3:29:30 PM | ZEC | DOWN | 30 sec | +0.079% | 0¢ | ❌ Lost | $0.00 |
| 10/8 3:29:30 PM | EURUSD | DOWN | 30 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/8 3:29:30 PM | SOL | DOWN | 30 sec | +0.057% | 0¢ | ❌ Lost | $0.00 |
| 10/8 3:29:30 PM | BNB | UP | 30 sec | -0.103% | 0¢ | ❌ Lost | $0.00 |
| 10/8 3:29:30 PM | XRP | DOWN | 30 sec | -0.007% | 0¢ | ❌ Lost | -$0.15 |
| 10/8 3:29:14 PM | WTI | UP | 46 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/8 3:29:14 PM | HYPE | UP | 46 sec | -0.081% | 0¢ | ❌ Lost | -$0.15 |
| 10/8 3:28:42 PM | ETH | DOWN | 77 sec | +0.087% | 1¢ | ❌ Lost | -$0.15 |
| 10/8 3:28:42 PM | BTC | UP | 77 sec | -0.092% | 0¢ | ❌ Lost | $0.00 |
| 10/8 3:25:59 PM | NEAR | UP | 4.0 min | -0.979% | 2¢ | ❌ Lost | -$0.15 |
| 10/8 3:14:55 PM | WTI | DOWN | 4 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/8 3:14:55 PM | XRP | UP | 4 sec | -0.065% | 0¢ | ❌ Lost | $0.00 |
| 10/8 3:14:40 PM | HYPE | UP | 19 sec | -0.045% | 0¢ | ❌ Lost | $0.00 |
| 10/8 3:14:24 PM | SOL | DOWN | 35 sec | +0.086% | 0¢ | ❌ Lost | $0.00 |
| 10/8 3:14:24 PM | BNB | UP | 35 sec | -0.050% | 0¢ | ❌ Lost | $0.00 |
| 10/8 3:13:36 PM | NATGAS | DOWN | 83 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/8 3:13:20 PM | ZEC | UP | 1.6 min | -0.360% | 0¢ | ❌ Lost | $0.00 |
| 10/8 3:13:04 PM | DOGE | UP | 1.9 min | -0.110% | 6¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
