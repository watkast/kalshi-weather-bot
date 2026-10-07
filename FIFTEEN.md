# 15-Minute 1¢ Study

*Updated Wed Oct 7, 1:06 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 739 finished bets | 1% | $32.80 | +41% | +4.44¢ | -$11.60 / $44.40 |

*Expect about **78 buys a day** (~$11.65/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 738 | $19.70 | +25% |
| 5+ min left, hold to the close | 284 | $13.85 | +33% |
| Volatility model ≥ 2%, hold to the close | 1353 | $5.70 | +4% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 10882 | 10876 | 49 (0%) | 1.07% | -$631.00 (-48%) | Hold to the close: -$631.00 (-48%) |

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
| Volatility model | 7038 | 4.1% | 0.5% (33) | -561% | ❌ Worse |
| Momentum model | 7038 | 4.1% | 0.5% (33) | -590% | ❌ Worse |
| Mean-reversion model | 7038 | 6.8% | 0.5% (33) | -653% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 7038 | 33 | -41% | -87% | -87% | -84% |
| Volatility model ≥ 2% | 1353 | 12 | +4% | -73% | -73% | -69% |
| Volatility model ≥ 5% | 739 | 8 | +41% | -62% | -61% | -57% |
| Volatility model ≥ 10% | 460 | 6 | +94% | -45% | -45% | -39% |
| Momentum model ≥ 2% | 1206 | 10 | +0% | -74% | -75% | -72% |
| Momentum model ≥ 5% | 738 | 7 | +25% | -66% | -68% | -65% |
| Momentum model ≥ 10% | 509 | 6 | +71% | -55% | -56% | -52% |
| Mean-reversion model ≥ 2% | 2407 | 19 | -14% | -84% | -84% | -80% |
| Mean-reversion model ≥ 5% | 1631 | 15 | +2% | -81% | -81% | -75% |
| Mean-reversion model ≥ 10% | 1086 | 11 | +17% | -79% | -79% | -74% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 7235 | 4% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 2741 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 900 | 3% | 2% | 2% | 1% | 1% | 0% |
| **All** | 10876 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 49 | 0% | -$631.00 | -48% | — |
| Sell at 2¢ | 384 | 4% | -$1,175.16 | -89% | 34 sec |
| Sell at 3¢ | 257 | 2% | -$1,174.77 | -89% | 47 sec |
| Sell at 5¢ | 192 | 2% | -$1,150.20 | -87% | 56 sec |
| Sell at 10¢ | 129 | 1% | -$1,092.01 | -83% | 64 sec |
| Sell at 25¢ | 74 | 1% | -$988.06 | -75% | 82 sec |
| Sell at 50¢ | 49 | 0% | -$860.25 | -65% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 3 | 0 | 100% | 67% | -100% | +73% | +160% |
| 5–10 min | 281 | 4 | 10% | 4% | +34% | -82% | -87% |
| 2–5 min | 3507 | 25 | 7% | 3% | -30% | -88% | -88% |
| 1–2 min | 2877 | 12 | 3% | 2% | -55% | -94% | -93% |
| Under 1 min | 4208 | 8 | 1% | 0% | -72% | -88% | -87% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 812 | 6 | 5% | 3% | -12% | -90% | -89% |
| HYPE | 811 | 3 | 5% | 3% | -55% | -89% | -87% |
| DOGE | 806 | 2 | 3% | 1% | -68% | -92% | -92% |
| ETH | 805 | 7 | 5% | 3% | +8% | -88% | -87% |
| BNB | 804 | 3 | 4% | 2% | -55% | -91% | -92% |
| NEAR | 801 | 5 | 6% | 3% | -18% | -69% | -70% |
| SOL | 800 | 0 | 3% | 1% | -100% | -93% | -92% |
| BTC | 799 | 4 | 5% | 2% | -34% | -88% | -90% |
| XRP | 797 | 5 | 2% | 1% | -21% | -80% | -80% |
| GOLD | 457 | 0 | 4% | 1% | -100% | -92% | -94% |
| SILVER | 447 | 0 | 2% | 1% | -100% | -95% | -94% |
| WTI | 423 | 3 | 3% | 1% | -22% | -95% | -96% |
| COPPER | 390 | 0 | 1% | 1% | -100% | -99% | -99% |
| PLATINUM | 350 | 0 | 0% | 0% | -100% | -100% | -99% |
| NATGAS | 340 | 3 | 3% | 2% | -18% | -94% | -92% |
| PALLADIUM | 334 | 1 | 1% | 1% | -72% | -97% | -98% |
| EURUSD | 328 | 3 | 4% | 2% | -15% | -65% | -64% |
| GBPUSD | 307 | 1 | 3% | 2% | -70% | -95% | -95% |
| USDJPY | 265 | 3 | 2% | 1% | +6% | -97% | -96% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 5533 | 26 | 4% | 2% | -45% | -88% | -87% |
| DOWN (bought NO) | 5343 | 23 | 3% | 2% | -50% | -90% | -91% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 1191 | 8 | 2% | 1% | +16% | -65% | -64% |
| 0.05–0.1% | 1241 | 4 | 3% | 1% | -53% | -92% | -92% |
| 0.1–0.2% | 1840 | 6 | 3% | 2% | -59% | -92% | -92% |
| 0.2–0.5% | 2118 | 12 | 6% | 3% | -38% | -88% | -87% |
| Over 0.5% | 843 | 5 | 7% | 3% | -39% | -88% | -90% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 2890 | 17 | 4% | 2% | -32% | -84% | -84% |
| Morning (6am–12pm) | 2706 | 17 | 4% | 2% | -28% | -91% | -90% |
| Afternoon (12–6pm) | 2290 | 7 | 3% | 1% | -64% | -88% | -88% |
| Evening (6pm–12am) | 2990 | 8 | 3% | 1% | -69% | -95% | -94% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 25 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,044 |
| Time from buy to best bounce (bounced bets) | 49 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/7 12:59:38 PM | DOGE | DOWN | 22 sec | +0.036% | 0¢ | ❌ Lost | $0.00 |
| 10/7 12:59:06 PM | NATGAS | UP | 54 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/7 12:58:35 PM | XRP | DOWN | 85 sec | +0.112% | 0¢ | ❌ Lost | $0.00 |
| 10/7 12:58:19 PM | SOL | UP | 1.7 min | -0.157% | 1¢ | ❌ Lost | -$0.15 |
| 10/7 12:56:44 PM | ETH | DOWN | 3.3 min | +0.204% | 1¢ | ❌ Lost | -$0.15 |
| 10/7 12:56:44 PM | BTC | DOWN | 3.3 min | +0.142% | 1¢ | ❌ Lost | -$0.15 |
| 10/7 12:55:57 PM | ZEC | DOWN | 4.0 min | +0.671% | 1¢ | ❌ Lost | -$0.15 |
| 10/7 12:55:26 PM | HYPE | DOWN | 4.6 min | +0.487% | 1¢ | ❌ Lost | -$0.15 |
| 10/7 12:54:54 PM | BNB | DOWN | 5.1 min | +0.160% | 1¢ | ❌ Lost | -$0.15 |
| 10/7 12:53:19 PM | NEAR | DOWN | 6.7 min | +1.840% | 3¢ | ❌ Lost | -$0.15 |
| 10/7 12:44:49 PM | ETH | UP | 10 sec | -0.011% | 0¢ | ❌ Lost | $0.00 |
| 10/7 12:44:34 PM | BNB | UP | 25 sec | -0.048% | 0¢ | ❌ Lost | -$0.15 |
| 10/7 12:44:34 PM | BTC | UP | 25 sec | -0.039% | 0¢ | ❌ Lost | $0.00 |
| 10/7 12:44:02 PM | USDJPY | UP | 57 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/7 12:43:15 PM | WTI | DOWN | 1.7 min | — | 0¢ | ❌ Lost | $0.00 |
| 10/7 12:43:15 PM | XRP | DOWN | 1.7 min | +0.190% | 1¢ | ❌ Lost | -$0.15 |
| 10/7 12:42:59 PM | HYPE | DOWN | 2.0 min | +0.309% | 0¢ | ❌ Lost | $0.00 |
| 10/7 12:42:12 PM | NEAR | UP | 2.8 min | -0.915% | 0¢ | ❌ Lost | $0.00 |
| 10/7 12:41:56 PM | SOL | UP | 3.0 min | -0.271% | 1¢ | ❌ Lost | -$0.15 |
| 10/7 12:29:51 PM | HYPE | UP | 9 sec | -0.047% | 0¢ | ❌ Lost | $0.00 |
| 10/7 12:29:51 PM | XRP | DOWN | 9 sec | +0.056% | 0¢ | ❌ Lost | -$0.15 |
| 10/7 12:29:51 PM | GOLD | UP | 9 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/7 12:29:51 PM | BTC | DOWN | 9 sec | +0.017% | 0¢ | ❌ Lost | -$0.15 |
| 10/7 12:29:34 PM | BNB | DOWN | 26 sec | +0.025% | 0¢ | ❌ Lost | -$0.15 |
| 10/7 12:29:34 PM | PALLADIUM | UP | 26 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/7 12:29:02 PM | DOGE | UP | 58 sec | +0.025% | 52¢ | ❌ Lost | $0.00 |
| 10/7 12:29:02 PM | ETH | UP | 58 sec | -0.025% | 9¢ | ❌ Lost | -$0.15 |
| 10/7 12:29:02 PM | NATGAS | DOWN | 58 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/7 12:28:47 PM | SOL | UP | 72 sec | -0.114% | 23¢ | ❌ Lost | $0.00 |
| 10/7 12:28:32 PM | ZEC | UP | 87 sec | -0.234% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
