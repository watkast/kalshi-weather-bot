# 15-Minute 1¢ Study

*Updated Wed Oct 7, 4:29 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 743 finished bets | 1% | $32.20 | +40% | +4.33¢ | -$11.90 / $44.10 |

*Expect about **77 buys a day** (~$11.56/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 742 | $19.10 | +24% |
| 5+ min left, hold to the close | 289 | $13.10 | +31% |
| Volatility model ≥ 2%, hold to the close | 1366 | $3.75 | +2% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 11073 | 11052 | 49 (0%) | 1.07% | -$653.05 (-49%) | Hold to the close: -$653.05 (-49%) |

*In play or awaiting result: 21. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 7154 | 4.0% | 0.5% (33) | -558% | ❌ Worse |
| Momentum model | 7154 | 4.1% | 0.5% (33) | -587% | ❌ Worse |
| Mean-reversion model | 7154 | 6.7% | 0.5% (33) | -652% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 7154 | 33 | -42% | -87% | -87% | -84% |
| Volatility model ≥ 2% | 1366 | 12 | +2% | -72% | -72% | -69% |
| Volatility model ≥ 5% | 743 | 8 | +40% | -62% | -60% | -57% |
| Volatility model ≥ 10% | 463 | 6 | +92% | -44% | -45% | -40% |
| Momentum model ≥ 2% | 1216 | 10 | -1% | -73% | -75% | -72% |
| Momentum model ≥ 5% | 742 | 7 | +24% | -66% | -68% | -65% |
| Momentum model ≥ 10% | 512 | 6 | +70% | -55% | -56% | -52% |
| Mean-reversion model ≥ 2% | 2445 | 19 | -16% | -84% | -84% | -80% |
| Mean-reversion model ≥ 5% | 1653 | 15 | +1% | -81% | -81% | -75% |
| Mean-reversion model ≥ 10% | 1098 | 11 | +15% | -79% | -79% | -74% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 7351 | 4% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 2786 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 915 | 3% | 2% | 2% | 1% | 1% | 0% |
| **All** | 11052 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 49 | 0% | -$653.05 | -49% | — |
| Sell at 2¢ | 388 | 4% | -$1,196.17 | -89% | 34 sec |
| Sell at 3¢ | 259 | 2% | -$1,196.04 | -89% | 47 sec |
| Sell at 5¢ | 193 | 2% | -$1,171.60 | -87% | 60 sec |
| Sell at 10¢ | 129 | 1% | -$1,114.06 | -83% | 64 sec |
| Sell at 25¢ | 74 | 1% | -$1,010.11 | -75% | 82 sec |
| Sell at 50¢ | 49 | 0% | -$882.30 | -66% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 3 | 0 | 100% | 67% | -100% | +73% | +160% |
| 5–10 min | 286 | 4 | 10% | 3% | +32% | -82% | -86% |
| 2–5 min | 3571 | 25 | 7% | 3% | -32% | -88% | -88% |
| 1–2 min | 2922 | 12 | 3% | 2% | -56% | -94% | -93% |
| Under 1 min | 4270 | 8 | 1% | 0% | -72% | -88% | -88% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 824 | 6 | 5% | 3% | -13% | -90% | -90% |
| HYPE | 824 | 3 | 5% | 3% | -55% | -89% | -87% |
| DOGE | 819 | 2 | 3% | 1% | -69% | -92% | -92% |
| ETH | 818 | 7 | 5% | 3% | +7% | -88% | -88% |
| BNB | 817 | 3 | 4% | 2% | -56% | -90% | -91% |
| NEAR | 814 | 5 | 6% | 3% | -20% | -70% | -71% |
| SOL | 813 | 0 | 3% | 1% | -100% | -94% | -93% |
| BTC | 812 | 4 | 5% | 2% | -35% | -88% | -90% |
| XRP | 810 | 5 | 2% | 1% | -23% | -80% | -81% |
| GOLD | 464 | 0 | 4% | 1% | -100% | -92% | -94% |
| SILVER | 453 | 0 | 2% | 1% | -100% | -95% | -94% |
| WTI | 431 | 3 | 3% | 1% | -24% | -95% | -96% |
| COPPER | 397 | 0 | 1% | 1% | -100% | -99% | -99% |
| PLATINUM | 356 | 0 | 0% | 0% | -100% | -100% | -99% |
| NATGAS | 348 | 3 | 3% | 2% | -20% | -95% | -93% |
| PALLADIUM | 337 | 1 | 1% | 1% | -72% | -97% | -98% |
| EURUSD | 333 | 3 | 4% | 2% | -16% | -66% | -64% |
| GBPUSD | 311 | 1 | 3% | 2% | -70% | -95% | -95% |
| USDJPY | 271 | 3 | 1% | 1% | +3% | -97% | -96% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 5622 | 26 | 4% | 2% | -46% | -88% | -88% |
| DOWN (bought NO) | 5430 | 23 | 3% | 2% | -51% | -90% | -91% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 1210 | 8 | 2% | 1% | +14% | -65% | -65% |
| 0.05–0.1% | 1259 | 4 | 3% | 1% | -54% | -91% | -92% |
| 0.1–0.2% | 1871 | 6 | 3% | 2% | -60% | -92% | -92% |
| 0.2–0.5% | 2150 | 12 | 6% | 3% | -39% | -89% | -88% |
| Over 0.5% | 859 | 5 | 6% | 3% | -40% | -88% | -90% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 2890 | 17 | 4% | 2% | -32% | -84% | -84% |
| Morning (6am–12pm) | 2706 | 17 | 4% | 2% | -28% | -91% | -90% |
| Afternoon (12–6pm) | 2466 | 7 | 3% | 1% | -66% | -88% | -89% |
| Evening (6pm–12am) | 2990 | 8 | 3% | 1% | -69% | -95% | -94% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 25 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,066 |
| Time from buy to best bounce (bounced bets) | 49 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/7 4:29:36 PM | PLATINUM | DOWN | 23 sec | — | — | In play | — |
| 10/7 4:29:20 PM | WTI | DOWN | 39 sec | — | — | In play | — |
| 10/7 4:29:20 PM | GBPUSD | DOWN | 39 sec | — | — | In play | — |
| 10/7 4:29:04 PM | SILVER | UP | 55 sec | — | — | In play | — |
| 10/7 4:28:48 PM | EURUSD | DOWN | 72 sec | — | — | In play | — |
| 10/7 4:28:32 PM | NEAR | DOWN | 87 sec | +0.421% | — | In play | — |
| 10/7 4:28:16 PM | GOLD | UP | 1.7 min | — | — | In play | — |
| 10/7 4:28:16 PM | XRP | DOWN | 1.7 min | +0.127% | — | In play | — |
| 10/7 4:28:00 PM | DOGE | DOWN | 2.0 min | +0.196% | — | In play | — |
| 10/7 4:28:00 PM | ETH | DOWN | 2.0 min | +0.098% | — | In play | — |
| 10/7 4:28:00 PM | BTC | DOWN | 2.0 min | +0.104% | — | In play | — |
| 10/7 4:27:29 PM | ZEC | DOWN | 2.5 min | +0.315% | — | In play | — |
| 10/7 4:27:13 PM | SOL | DOWN | 2.8 min | +0.188% | — | In play | — |
| 10/7 4:27:13 PM | BNB | DOWN | 2.8 min | +0.090% | — | In play | — |
| 10/7 4:25:07 PM | HYPE | DOWN | 4.9 min | +0.344% | — | In play | — |
| 10/7 4:14:53 PM | ETH | DOWN | 7 sec | +0.021% | 0¢ | ❌ Lost | $0.00 |
| 10/7 4:14:38 PM | WTI | DOWN | 22 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/7 4:13:17 PM | NATGAS | DOWN | 1.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/7 4:12:31 PM | EURUSD | DOWN | 2.5 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/7 4:12:31 PM | USDJPY | UP | 2.5 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/7 4:12:31 PM | ZEC | DOWN | 2.5 min | +0.366% | 1¢ | ❌ Lost | -$0.15 |
| 10/7 4:12:15 PM | HYPE | DOWN | 2.7 min | +0.248% | 0¢ | ❌ Lost | $0.00 |
| 10/7 4:12:15 PM | XRP | DOWN | 2.7 min | +0.255% | 1¢ | ❌ Lost | -$0.15 |
| 10/7 4:12:15 PM | NEAR | DOWN | 2.7 min | +0.754% | 1¢ | ❌ Lost | -$0.15 |
| 10/7 4:12:15 PM | BNB | DOWN | 2.7 min | +0.074% | 7¢ | ❌ Lost | -$0.15 |
| 10/7 4:12:15 PM | SOL | DOWN | 2.7 min | +0.275% | 0¢ | ❌ Lost | -$0.15 |
| 10/7 4:11:59 PM | BTC | DOWN | 3.0 min | +0.112% | 1¢ | ❌ Lost | -$0.15 |
| 10/7 4:11:59 PM | DOGE | DOWN | 3.0 min | +0.245% | 1¢ | ❌ Lost | -$0.15 |
| 10/7 3:59:55 PM | HYPE | DOWN | 4 sec | +0.023% | 0¢ | ❌ Lost | $0.00 |
| 10/7 3:59:55 PM | BNB | DOWN | 4 sec | +0.004% | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
