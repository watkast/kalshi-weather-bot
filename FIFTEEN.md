# 15-Minute 1¢ Study

*Updated Wed Oct 7, 6:29 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 735 finished bets | 1% | $33.10 | +42% | +4.50¢ | -$11.45 / $44.55 |

*Expect about **80 buys a day** (~$11.93/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 728 | $20.90 | +27% |
| 5+ min left, hold to the close | 273 | $15.50 | +38% |
| Mean-reversion model ≥ 5%, hold to the close | 1604 | $8.10 | +4% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 10699 | 10677 | 49 (0%) | 1.07% | -$606.55 (-47%) | Hold to the close: -$606.55 (-47%) |

*In play or awaiting result: 22. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 6917 | 4.1% | 0.5% (33) | -564% | ❌ Worse |
| Momentum model | 6917 | 4.2% | 0.5% (33) | -592% | ❌ Worse |
| Mean-reversion model | 6917 | 6.8% | 0.5% (33) | -653% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 6917 | 33 | -40% | -87% | -87% | -84% |
| Volatility model ≥ 2% | 1341 | 12 | +4% | -73% | -73% | -69% |
| Volatility model ≥ 5% | 735 | 8 | +42% | -62% | -61% | -58% |
| Volatility model ≥ 10% | 458 | 6 | +94% | -46% | -47% | -42% |
| Momentum model ≥ 2% | 1193 | 10 | +1% | -74% | -75% | -73% |
| Momentum model ≥ 5% | 728 | 7 | +27% | -66% | -68% | -66% |
| Momentum model ≥ 10% | 505 | 6 | +72% | -56% | -57% | -54% |
| Mean-reversion model ≥ 2% | 2367 | 19 | -13% | -84% | -84% | -80% |
| Mean-reversion model ≥ 5% | 1604 | 15 | +4% | -81% | -81% | -75% |
| Mean-reversion model ≥ 10% | 1066 | 11 | +19% | -79% | -79% | -74% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 7114 | 4% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 2684 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 879 | 3% | 2% | 2% | 1% | 1% | 0% |
| **All** | 10677 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 49 | 0% | -$606.55 | -47% | — |
| Sell at 2¢ | 378 | 4% | -$1,152.27 | -89% | 34 sec |
| Sell at 3¢ | 252 | 2% | -$1,152.27 | -89% | 47 sec |
| Sell at 5¢ | 188 | 2% | -$1,128.35 | -87% | 60 sec |
| Sell at 10¢ | 127 | 1% | -$1,070.18 | -83% | 65 sec |
| Sell at 25¢ | 73 | 1% | -$966.92 | -75% | 82 sec |
| Sell at 50¢ | 48 | 0% | -$842.55 | -65% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 3 | 0 | 100% | 67% | -100% | +73% | +160% |
| 5–10 min | 270 | 4 | 10% | 3% | +40% | -82% | -88% |
| 2–5 min | 3433 | 25 | 7% | 3% | -29% | -88% | -88% |
| 1–2 min | 2824 | 12 | 3% | 2% | -54% | -94% | -93% |
| Under 1 min | 4147 | 8 | 1% | 0% | -71% | -88% | -87% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 801 | 6 | 5% | 3% | -10% | -89% | -89% |
| HYPE | 797 | 3 | 5% | 3% | -54% | -89% | -87% |
| DOGE | 793 | 2 | 3% | 1% | -68% | -92% | -92% |
| ETH | 791 | 7 | 5% | 3% | +11% | -88% | -88% |
| BNB | 790 | 3 | 4% | 2% | -54% | -91% | -92% |
| NEAR | 788 | 5 | 6% | 3% | -17% | -69% | -70% |
| SOL | 786 | 0 | 3% | 1% | -100% | -94% | -93% |
| BTC | 785 | 4 | 5% | 2% | -33% | -88% | -90% |
| XRP | 783 | 5 | 2% | 1% | -20% | -80% | -80% |
| GOLD | 448 | 0 | 4% | 1% | -100% | -92% | -94% |
| SILVER | 438 | 0 | 3% | 1% | -100% | -95% | -94% |
| WTI | 415 | 3 | 3% | 1% | -20% | -95% | -96% |
| COPPER | 384 | 0 | 1% | 1% | -100% | -99% | -99% |
| PLATINUM | 343 | 0 | 0% | 0% | -100% | -99% | -99% |
| NATGAS | 328 | 3 | 3% | 2% | -15% | -94% | -92% |
| PALLADIUM | 328 | 1 | 2% | 1% | -72% | -97% | -98% |
| EURUSD | 321 | 3 | 4% | 2% | -13% | -64% | -63% |
| GBPUSD | 300 | 1 | 3% | 2% | -69% | -95% | -95% |
| USDJPY | 258 | 3 | 2% | 1% | +9% | -97% | -96% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 5421 | 26 | 4% | 2% | -44% | -88% | -87% |
| DOWN (bought NO) | 5256 | 23 | 3% | 2% | -50% | -90% | -91% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 1174 | 8 | 2% | 1% | +17% | -65% | -65% |
| 0.05–0.1% | 1234 | 4 | 3% | 1% | -53% | -92% | -92% |
| 0.1–0.2% | 1811 | 6 | 3% | 2% | -58% | -92% | -92% |
| 0.2–0.5% | 2072 | 12 | 6% | 3% | -36% | -88% | -87% |
| Over 0.5% | 821 | 5 | 7% | 3% | -38% | -87% | -90% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 2890 | 17 | 4% | 2% | -32% | -84% | -84% |
| Morning (6am–12pm) | 2553 | 17 | 5% | 3% | -24% | -90% | -89% |
| Afternoon (12–6pm) | 2244 | 7 | 3% | 1% | -63% | -88% | -89% |
| Evening (6pm–12am) | 2990 | 8 | 3% | 1% | -69% | -95% | -94% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 25 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,012 |
| Time from buy to best bounce (bounced bets) | 49 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/7 6:28:25 AM | NEAR | UP | 1.6 min | -0.332% | — | In play | — |
| 10/7 6:28:09 AM | COPPER | UP | 1.8 min | — | — | In play | — |
| 10/7 6:27:52 AM | SILVER | UP | 2.1 min | — | — | In play | — |
| 10/7 6:27:52 AM | PLATINUM | UP | 2.1 min | — | — | In play | — |
| 10/7 6:27:20 AM | PALLADIUM | UP | 2.6 min | — | — | In play | — |
| 10/7 6:27:20 AM | ZEC | UP | 2.6 min | -0.462% | — | In play | — |
| 10/7 6:27:04 AM | EURUSD | UP | 2.9 min | — | — | In play | — |
| 10/7 6:27:04 AM | HYPE | UP | 2.9 min | -0.270% | — | In play | — |
| 10/7 6:27:04 AM | GBPUSD | UP | 2.9 min | — | — | In play | — |
| 10/7 6:26:47 AM | BTC | UP | 3.2 min | -0.205% | — | In play | — |
| 10/7 6:26:31 AM | ETH | UP | 3.5 min | -0.233% | — | In play | — |
| 10/7 6:26:15 AM | GOLD | UP | 3.8 min | — | — | In play | — |
| 10/7 6:25:59 AM | XRP | UP | 4.0 min | -0.434% | — | In play | — |
| 10/7 6:25:26 AM | BNB | UP | 4.5 min | -0.294% | — | In play | — |
| 10/7 6:24:53 AM | DOGE | UP | 5.1 min | -0.488% | — | In play | — |
| 10/7 6:24:53 AM | SOL | UP | 5.1 min | -0.403% | — | In play | — |
| 10/7 6:14:31 AM | USDJPY | DOWN | 29 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/7 6:14:16 AM | BNB | DOWN | 44 sec | -0.005% | 0¢ | ❌ Lost | $0.00 |
| 10/7 6:14:16 AM | HYPE | DOWN | 44 sec | +0.096% | 1¢ | ❌ Lost | -$0.15 |
| 10/7 6:14:16 AM | ETH | DOWN | 44 sec | +0.102% | 0¢ | ❌ Lost | $0.00 |
| 10/7 6:13:59 AM | SILVER | UP | 61 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/7 6:13:43 AM | SOL | DOWN | 77 sec | +0.125% | 1¢ | ❌ Lost | -$0.15 |
| 10/7 6:13:27 AM | COPPER | UP | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/7 6:13:11 AM | NATGAS | DOWN | 1.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/7 6:12:52 AM | BTC | UP | 2.1 min | -0.142% | 1¢ | ❌ Lost | -$0.15 |
| 10/7 6:12:36 AM | XRP | DOWN | 2.4 min | +0.277% | 1¢ | ❌ Lost | -$0.15 |
| 10/7 6:12:20 AM | PLATINUM | UP | 2.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/7 6:12:05 AM | DOGE | DOWN | 2.9 min | +0.307% | 1¢ | ❌ Lost | -$0.15 |
| 10/7 6:12:05 AM | NEAR | DOWN | 2.9 min | +0.648% | 2¢ | ❌ Lost | -$0.15 |
| 10/7 6:11:31 AM | EURUSD | UP | 3.5 min | — | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
