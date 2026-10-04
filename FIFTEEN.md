# 15-Minute 1¢ Study

*Updated Sat Oct 3, 8:00 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Momentum model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 478 finished bets | 1% | $6.05 | +12% | +1.27¢ | $1.60 / $4.45 |

*Expect about **82 buys a day** (~$12.35/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| 5+ min left, hold to the close | 178 | $1.75 | +7% |
| Volatility model ≥ 5%, hold to the close | 475 | -$8.25 | -16% |
| Momentum model ≥ 5%, sell at 50¢ | 478 | -$8.45 | -17% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 6966 | 6956 | 29 (0%) | 1.07% | -$430.10 (-51%) | Hold to the close: -$430.10 (-51%) |

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
| Volatility model | 4420 | 4.1% | 0.4% (17) | -668% | ❌ Worse |
| Momentum model | 4420 | 4.2% | 0.4% (17) | -702% | ❌ Worse |
| Mean-reversion model | 4420 | 7.0% | 0.4% (17) | -792% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 4420 | 17 | -51% | -84% | -84% | -81% |
| Volatility model ≥ 2% | 903 | 6 | -22% | -68% | -68% | -64% |
| Volatility model ≥ 5% | 475 | 3 | -16% | -50% | -51% | -48% |
| Volatility model ≥ 10% | 287 | 3 | +60% | -24% | -27% | -22% |
| Momentum model ≥ 2% | 790 | 5 | -23% | -67% | -70% | -67% |
| Momentum model ≥ 5% | 478 | 4 | +12% | -55% | -59% | -55% |
| Momentum model ≥ 10% | 325 | 3 | +36% | -40% | -42% | -38% |
| Mean-reversion model ≥ 2% | 1598 | 8 | -45% | -84% | -85% | -80% |
| Mean-reversion model ≥ 5% | 1077 | 7 | -28% | -80% | -81% | -74% |
| Mean-reversion model ≥ 10% | 706 | 5 | -18% | -77% | -79% | -72% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 4617 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 1784 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 555 | 4% | 3% | 2% | 2% | 1% | 1% |
| **All** | 6956 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 29 | 0% | -$430.10 | -51% | — |
| Sell at 2¢ | 271 | 4% | -$737.64 | -88% | 34 sec |
| Sell at 3¢ | 172 | 2% | -$741.02 | -89% | 48 sec |
| Sell at 5¢ | 129 | 2% | -$724.25 | -87% | 61 sec |
| Sell at 10¢ | 87 | 1% | -$680.13 | -81% | 78 sec |
| Sell at 25¢ | 48 | 1% | -$621.22 | -74% | 1.6 min |
| Sell at 50¢ | 28 | 0% | -$549.10 | -66% | 1.7 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 3 | 0 | 100% | 67% | -100% | +73% | +160% |
| 5–10 min | 175 | 2 | 11% | 3% | +9% | -80% | -89% |
| 2–5 min | 2257 | 14 | 8% | 4% | -39% | -86% | -87% |
| 1–2 min | 1815 | 8 | 3% | 2% | -52% | -94% | -93% |
| Under 1 min | 2706 | 5 | 1% | 0% | -72% | -87% | -87% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| DOGE | 520 | 2 | 4% | 1% | -50% | -91% | -92% |
| ZEC | 518 | 3 | 5% | 3% | -31% | -89% | -90% |
| ETH | 517 | 4 | 6% | 3% | -1% | -86% | -86% |
| HYPE | 517 | 2 | 5% | 3% | -53% | -89% | -86% |
| BNB | 512 | 1 | 4% | 2% | -77% | -91% | -92% |
| BTC | 509 | 1 | 6% | 2% | -74% | -86% | -89% |
| SOL | 509 | 0 | 3% | 1% | -100% | -93% | -93% |
| XRP | 508 | 4 | 2% | 1% | +2% | -70% | -70% |
| NEAR | 507 | 2 | 6% | 2% | -47% | -58% | -61% |
| GOLD | 304 | 0 | 5% | 1% | -100% | -90% | -92% |
| SILVER | 285 | 0 | 2% | 1% | -100% | -95% | -95% |
| WTI | 274 | 2 | 3% | 1% | -23% | -94% | -96% |
| COPPER | 254 | 0 | 1% | 0% | -100% | -99% | -99% |
| PLATINUM | 226 | 0 | 0% | 0% | -100% | -100% | -100% |
| NATGAS | 225 | 2 | 4% | 2% | -17% | -94% | -92% |
| PALLADIUM | 216 | 1 | 2% | 1% | -57% | -96% | -98% |
| GBPUSD | 195 | 1 | 4% | 2% | -52% | -93% | -93% |
| EURUSD | 195 | 1 | 5% | 3% | -52% | -91% | -89% |
| USDJPY | 165 | 3 | 2% | 2% | +70% | -96% | -94% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 3517 | 17 | 4% | 2% | -43% | -88% | -88% |
| DOWN (bought NO) | 3439 | 12 | 4% | 2% | -60% | -88% | -90% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 712 | 5 | 2% | 1% | +24% | -45% | -45% |
| 0.05–0.1% | 742 | 0 | 3% | 1% | -100% | -92% | -94% |
| 0.1–0.2% | 1130 | 4 | 4% | 2% | -54% | -90% | -91% |
| 0.2–0.5% | 1414 | 6 | 6% | 3% | -53% | -88% | -88% |
| Over 0.5% | 617 | 4 | 7% | 3% | -33% | -86% | -88% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 1673 | 7 | 4% | 2% | -51% | -84% | -85% |
| Morning (6am–12pm) | 1849 | 13 | 5% | 3% | -20% | -90% | -89% |
| Afternoon (12–6pm) | 1513 | 3 | 3% | 1% | -76% | -85% | -87% |
| Evening (6pm–12am) | 1921 | 6 | 3% | 2% | -64% | -93% | -93% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 25 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 3,738 |
| Time from buy to best bounce (bounced bets) | 49 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/3 7:59:17 PM | XRP | UP | 43 sec | -0.047% | 0¢ | In play | — |
| 10/3 7:59:01 PM | DOGE | DOWN | 59 sec | +0.046% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 7:58:45 PM | BTC | DOWN | 75 sec | +0.022% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 7:57:41 PM | ETH | DOWN | 2.3 min | +0.095% | 0¢ | ❌ Lost | -$0.15 |
| 10/3 7:56:54 PM | HYPE | DOWN | 3.1 min | +0.187% | 1¢ | In play | — |
| 10/3 7:56:54 PM | SOL | DOWN | 3.1 min | +0.098% | 1¢ | In play | — |
| 10/3 7:55:20 PM | BNB | DOWN | 4.7 min | +0.094% | 1¢ | In play | — |
| 10/3 7:44:49 PM | BNB | UP | 11 sec | -0.028% | 0¢ | ❌ Lost | -$0.15 |
| 10/3 7:44:49 PM | ZEC | UP | 11 sec | -0.028% | 0¢ | ❌ Lost | -$0.15 |
| 10/3 7:44:00 PM | XRP | DOWN | 60 sec | +0.060% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 7:43:45 PM | NEAR | DOWN | 74 sec | +0.211% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 7:43:45 PM | DOGE | DOWN | 74 sec | +0.022% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 7:43:45 PM | SOL | UP | 74 sec | -0.087% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 7:43:29 PM | ETH | DOWN | 1.5 min | +0.084% | 0¢ | ❌ Lost | $0.00 |
| 10/3 7:43:29 PM | BTC | DOWN | 1.5 min | +0.035% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 7:43:13 PM | HYPE | DOWN | 1.8 min | +0.085% | 0¢ | ❌ Lost | $0.00 |
| 10/3 7:29:18 PM | HYPE | UP | 42 sec | -0.084% | 0¢ | ❌ Lost | -$0.15 |
| 10/3 7:28:46 PM | SOL | UP | 74 sec | -0.089% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 7:28:31 PM | BTC | UP | 89 sec | -0.040% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 7:27:59 PM | XRP | UP | 2.0 min | -0.175% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 7:27:27 PM | BNB | UP | 2.5 min | -0.112% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 7:27:27 PM | NEAR | UP | 2.5 min | -0.686% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 7:26:22 PM | DOGE | UP | 3.6 min | -0.217% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 7:26:06 PM | ETH | UP | 3.9 min | -0.114% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 7:25:50 PM | ZEC | UP | 4.2 min | -0.480% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 7:14:48 PM | BTC | UP | 12 sec | -0.022% | 0¢ | ❌ Lost | $0.00 |
| 10/3 7:14:33 PM | DOGE | DOWN | 26 sec | +0.021% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 7:14:33 PM | SOL | DOWN | 26 sec | -0.000% | 4¢ | ❌ Lost | -$0.15 |
| 10/3 7:14:17 PM | ETH | DOWN | 42 sec | +0.025% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 7:14:01 PM | ZEC | UP | 58 sec | -0.144% | 0¢ | ❌ Lost | $0.00 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
