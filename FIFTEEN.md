# 15-Minute 1¢ Study

*Updated Tue Sep 29, 10:15 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (5+ min left).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| 5+ min left, hold to the close | 81 finished bets | 2% | $15.85 | +130% | +19.57¢ | $22.00 / -$6.15 |

*Expect about **39 buys a day** (~$5.88/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| 5+ min left, sell at 50¢ | 81 | $1.35 | +11% |
| Momentum model ≥ 5%, hold to the close | 140 | -$1.75 | -11% |
| Volatility model ≥ 5%, sell at 25¢ | 128 | -$3.57 | -26% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 2667 | 2654 | 11 (0%) | 1.07% | -$168.80 (-52%) | Hold to the close: -$168.80 (-52%) |

*In play or awaiting result: 13. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 1463 | 2.8% | 0.3% (5) | -429% | ❌ Worse |
| Momentum model | 1463 | 3.0% | 0.3% (5) | -479% | ❌ Worse |
| Mean-reversion model | 1463 | 5.7% | 0.3% (5) | -532% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 1463 | 5 | -57% | -91% | -91% | -88% |
| Volatility model ≥ 2% | 279 | 2 | -18% | -85% | -87% | -85% |
| Volatility model ≥ 5% | 128 | 0 | -100% | -77% | -77% | -71% |
| Volatility model ≥ 10% | 69 | 0 | -100% | -75% | -75% | -69% |
| Momentum model ≥ 2% | 244 | 1 | -52% | -87% | -89% | -89% |
| Momentum model ≥ 5% | 140 | 1 | -11% | -83% | -88% | -83% |
| Momentum model ≥ 10% | 89 | 0 | -100% | -88% | -87% | -85% |
| Mean-reversion model ≥ 2% | 535 | 3 | -40% | -86% | -87% | -83% |
| Mean-reversion model ≥ 5% | 353 | 3 | -10% | -84% | -84% | -78% |
| Mean-reversion model ≥ 10% | 218 | 2 | +2% | -79% | -82% | -76% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 1659 | 4% | 3% | 2% | 2% | 1% | 0% |
| Commodities | 809 | 2% | 1% | 1% | 0% | 0% | 0% |
| Financials | 186 | 5% | 3% | 3% | 2% | 2% | 1% |
| **All** | 2654 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 11 | 0% | -$168.80 | -52% | — |
| Sell at 2¢ | 95 | 4% | -$298.10 | -92% | 34 sec |
| Sell at 3¢ | 60 | 2% | -$299.40 | -93% | 47 sec |
| Sell at 5¢ | 42 | 2% | -$295.50 | -92% | 65 sec |
| Sell at 10¢ | 35 | 1% | -$262.95 | -81% | 1.6 min |
| Sell at 25¢ | 18 | 1% | -$249.22 | -77% | 1.7 min |
| Sell at 50¢ | 10 | 0% | -$227.30 | -70% | 2.3 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| 5–10 min | 81 | 2 | 11% | 2% | +130% | -81% | -87% |
| 2–5 min | 876 | 6 | 6% | 3% | -34% | -89% | -90% |
| 1–2 min | 715 | 2 | 3% | 2% | -70% | -94% | -93% |
| Under 1 min | 982 | 1 | 1% | 0% | -85% | -97% | -98% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| DOGE | 188 | 1 | 4% | 2% | -30% | -91% | -90% |
| ETH | 186 | 2 | 4% | 3% | +31% | -90% | -87% |
| ZEC | 186 | 1 | 5% | 3% | -36% | -88% | -91% |
| NEAR | 185 | 0 | 5% | 1% | -100% | -87% | -90% |
| BTC | 184 | 0 | 7% | 2% | -100% | -85% | -90% |
| XRP | 184 | 2 | 2% | 2% | +40% | -95% | -94% |
| SOL | 183 | 0 | 3% | 2% | -100% | -92% | -90% |
| BNB | 182 | 0 | 2% | 1% | -100% | -97% | -97% |
| HYPE | 181 | 1 | 4% | 2% | -31% | -91% | -90% |
| GOLD | 144 | 0 | 5% | 1% | -100% | -89% | -91% |
| WTI | 128 | 0 | 3% | 1% | -100% | -94% | -95% |
| SILVER | 127 | 0 | 2% | 1% | -100% | -95% | -95% |
| COPPER | 119 | 0 | 1% | 1% | -100% | -99% | -98% |
| NATGAS | 109 | 0 | 3% | 1% | -100% | -95% | -93% |
| PLATINUM | 94 | 0 | 0% | 0% | -100% | -100% | -100% |
| PALLADIUM | 88 | 0 | 1% | 0% | -100% | -98% | -100% |
| GBPUSD | 69 | 1 | 6% | 3% | +35% | -90% | -89% |
| EURUSD | 62 | 1 | 5% | 2% | +51% | -92% | -96% |
| USDJPY | 55 | 2 | 4% | 4% | +239% | -94% | -91% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 1397 | 8 | 4% | 2% | -34% | -92% | -92% |
| DOWN (bought NO) | 1257 | 3 | 4% | 2% | -72% | -92% | -93% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 175 | 0 | 2% | 1% | -100% | -94% | -94% |
| 0.05–0.1% | 214 | 0 | 1% | 0% | -100% | -97% | -98% |
| 0.1–0.2% | 394 | 1 | 4% | 1% | -65% | -91% | -92% |
| 0.2–0.5% | 604 | 2 | 5% | 3% | -64% | -90% | -90% |
| Over 0.5% | 271 | 4 | 6% | 3% | +53% | -88% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 577 | 1 | 3% | 1% | -80% | -93% | -96% |
| Morning (6am–12pm) | 647 | 6 | 4% | 2% | +7% | -91% | -90% |
| Afternoon (12–6pm) | 583 | 1 | 3% | 1% | -81% | -94% | -97% |
| Evening (6pm–12am) | 847 | 3 | 4% | 2% | -59% | -92% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 23 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 3,660 |
| Time from buy to best bounce (bounced bets) | 47 sec |
| Price snapshots per bet | 43 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 9/29 10:14:45 PM | NATGAS | UP | 14 sec | — | 0¢ | In play | — |
| 9/29 10:14:45 PM | HYPE | UP | 14 sec | -0.052% | 0¢ | In play | — |
| 9/29 10:14:45 PM | EURUSD | UP | 14 sec | — | 0¢ | In play | — |
| 9/29 10:14:29 PM | WTI | UP | 30 sec | — | 1¢ | In play | — |
| 9/29 10:14:29 PM | USDJPY | DOWN | 30 sec | — | 0¢ | In play | — |
| 9/29 10:13:42 PM | ETH | DOWN | 78 sec | +0.087% | 0¢ | ❌ Lost | -$0.15 |
| 9/29 10:13:42 PM | DOGE | DOWN | 78 sec | +0.146% | 0¢ | ❌ Lost | $0.00 |
| 9/29 10:13:42 PM | XRP | DOWN | 78 sec | +0.174% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 10:13:26 PM | BTC | DOWN | 1.6 min | +0.082% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 10:12:07 PM | SOL | DOWN | 2.9 min | +0.332% | 1¢ | In play | — |
| 9/29 10:11:50 PM | ZEC | DOWN | 3.1 min | +0.368% | 1¢ | In play | — |
| 9/29 10:11:33 PM | BNB | DOWN | 3.4 min | +0.213% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 10:10:47 PM | NEAR | DOWN | 4.2 min | +0.780% | 0¢ | ❌ Lost | -$0.15 |
| 9/29 9:59:29 PM | GBPUSD | UP | 31 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/29 9:59:29 PM | PALLADIUM | UP | 31 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/29 9:59:29 PM | EURUSD | UP | 31 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/29 9:58:57 PM | PLATINUM | UP | 63 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/29 9:58:41 PM | WTI | DOWN | 78 sec | — | 3¢ | ❌ Lost | -$0.15 |
| 9/29 9:58:25 PM | GOLD | UP | 1.6 min | — | 1¢ | ❌ Lost | -$0.15 |
| 9/29 9:58:25 PM | COPPER | UP | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 9/29 9:57:53 PM | XRP | UP | 2.1 min | -0.314% | 1¢ | ❌ Lost | $0.00 |
| 9/29 9:57:22 PM | BTC | UP | 2.6 min | -0.140% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 9:57:22 PM | ETH | UP | 2.6 min | -0.194% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 9:57:22 PM | SILVER | UP | 2.6 min | — | 1¢ | ❌ Lost | -$0.15 |
| 9/29 9:57:22 PM | HYPE | UP | 2.6 min | -0.161% | 96¢ | ✅ Won | $13.85 |
| 9/29 9:56:50 PM | DOGE | UP | 3.2 min | -0.404% | 0¢ | ❌ Lost | -$0.15 |
| 9/29 9:56:19 PM | BNB | UP | 3.7 min | -0.132% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 9:56:03 PM | SOL | UP | 4.0 min | -0.454% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 9:56:03 PM | ZEC | UP | 4.0 min | -0.508% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 9:55:31 PM | NEAR | UP | 4.5 min | -1.082% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
