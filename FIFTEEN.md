# 15-Minute 1¢ Study

*Updated Wed Oct 7, 5:12 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 745 finished bets | 1% | $31.90 | +40% | +4.28¢ | -$12.05 / $43.95 |

*Expect about **77 buys a day** (~$11.53/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 744 | $18.95 | +24% |
| 5+ min left, hold to the close | 289 | $13.10 | +31% |
| Volatility model ≥ 2%, hold to the close | 1372 | $3.15 | +2% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 11092 | 11082 | 49 (0%) | 1.07% | -$656.35 (-49%) | Hold to the close: -$656.35 (-49%) |

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
| Volatility model | 7172 | 4.0% | 0.5% (33) | -558% | ❌ Worse |
| Momentum model | 7172 | 4.1% | 0.5% (33) | -587% | ❌ Worse |
| Mean-reversion model | 7172 | 6.7% | 0.5% (33) | -652% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 7172 | 33 | -42% | -87% | -87% | -84% |
| Volatility model ≥ 2% | 1372 | 12 | +2% | -73% | -73% | -69% |
| Volatility model ≥ 5% | 745 | 8 | +40% | -62% | -61% | -57% |
| Volatility model ≥ 10% | 465 | 6 | +90% | -45% | -45% | -40% |
| Momentum model ≥ 2% | 1219 | 10 | -1% | -73% | -75% | -72% |
| Momentum model ≥ 5% | 744 | 7 | +24% | -66% | -68% | -65% |
| Momentum model ≥ 10% | 513 | 6 | +69% | -55% | -56% | -52% |
| Mean-reversion model ≥ 2% | 2453 | 19 | -16% | -84% | -84% | -80% |
| Mean-reversion model ≥ 5% | 1659 | 15 | +0% | -81% | -81% | -75% |
| Mean-reversion model ≥ 10% | 1103 | 11 | +15% | -79% | -79% | -74% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 7369 | 4% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 2794 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 919 | 3% | 2% | 2% | 1% | 1% | 0% |
| **All** | 11082 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 49 | 0% | -$656.35 | -49% | — |
| Sell at 2¢ | 389 | 4% | -$1,199.21 | -89% | 34 sec |
| Sell at 3¢ | 259 | 2% | -$1,199.34 | -89% | 47 sec |
| Sell at 5¢ | 193 | 2% | -$1,174.90 | -88% | 60 sec |
| Sell at 10¢ | 129 | 1% | -$1,117.36 | -83% | 64 sec |
| Sell at 25¢ | 74 | 1% | -$1,013.41 | -75% | 82 sec |
| Sell at 50¢ | 49 | 0% | -$885.60 | -66% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 3 | 0 | 100% | 67% | -100% | +73% | +160% |
| 5–10 min | 286 | 4 | 10% | 3% | +32% | -82% | -86% |
| 2–5 min | 3577 | 25 | 7% | 3% | -32% | -88% | -88% |
| 1–2 min | 2930 | 12 | 3% | 2% | -56% | -94% | -93% |
| Under 1 min | 4286 | 8 | 1% | 0% | -72% | -88% | -88% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 826 | 6 | 5% | 3% | -13% | -90% | -90% |
| HYPE | 826 | 3 | 5% | 3% | -56% | -89% | -87% |
| DOGE | 821 | 2 | 3% | 1% | -69% | -92% | -92% |
| ETH | 820 | 7 | 5% | 3% | +7% | -88% | -88% |
| BNB | 819 | 3 | 4% | 2% | -56% | -90% | -91% |
| NEAR | 816 | 5 | 6% | 3% | -20% | -70% | -71% |
| SOL | 815 | 0 | 3% | 1% | -100% | -94% | -93% |
| BTC | 814 | 4 | 5% | 2% | -35% | -88% | -90% |
| XRP | 812 | 5 | 2% | 1% | -23% | -81% | -81% |
| GOLD | 466 | 0 | 4% | 1% | -100% | -92% | -94% |
| SILVER | 455 | 0 | 2% | 1% | -100% | -95% | -94% |
| WTI | 433 | 3 | 3% | 1% | -24% | -95% | -96% |
| COPPER | 397 | 0 | 1% | 1% | -100% | -99% | -99% |
| PLATINUM | 357 | 0 | 0% | 0% | -100% | -100% | -99% |
| NATGAS | 349 | 3 | 3% | 2% | -20% | -95% | -93% |
| PALLADIUM | 337 | 1 | 1% | 1% | -72% | -97% | -98% |
| EURUSD | 334 | 3 | 4% | 2% | -16% | -66% | -64% |
| GBPUSD | 312 | 1 | 3% | 2% | -70% | -95% | -95% |
| USDJPY | 273 | 3 | 1% | 1% | +3% | -97% | -96% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 5629 | 26 | 4% | 2% | -46% | -88% | -88% |
| DOWN (bought NO) | 5453 | 23 | 3% | 2% | -51% | -90% | -91% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 1213 | 8 | 2% | 1% | +14% | -65% | -65% |
| 0.05–0.1% | 1264 | 4 | 3% | 1% | -54% | -91% | -92% |
| 0.1–0.2% | 1876 | 6 | 3% | 2% | -60% | -92% | -92% |
| 0.2–0.5% | 2154 | 12 | 6% | 3% | -39% | -89% | -88% |
| Over 0.5% | 860 | 5 | 7% | 3% | -40% | -88% | -90% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 2890 | 17 | 4% | 2% | -32% | -84% | -84% |
| Morning (6am–12pm) | 2706 | 17 | 4% | 2% | -28% | -91% | -90% |
| Afternoon (12–6pm) | 2496 | 7 | 3% | 1% | -67% | -88% | -89% |
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
| 10/7 5:12:46 PM | BTC | UP | 2.2 min | -0.127% | — | In play | — |
| 10/7 5:11:59 PM | ETH | UP | 3.0 min | -0.105% | — | In play | — |
| 10/7 5:11:59 PM | DOGE | UP | 3.0 min | -0.206% | — | In play | — |
| 10/7 5:10:08 PM | ZEC | DOWN | 4.8 min | +0.685% | — | In play | — |
| 10/7 4:44:51 PM | SILVER | UP | 8 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/7 4:44:51 PM | BTC | UP | 8 sec | -0.020% | 1¢ | ❌ Lost | -$0.15 |
| 10/7 4:44:51 PM | GOLD | UP | 8 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/7 4:44:51 PM | NATGAS | UP | 8 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/7 4:44:34 PM | DOGE | DOWN | 26 sec | +0.054% | 0¢ | ❌ Lost | -$0.15 |
| 10/7 4:44:34 PM | HYPE | DOWN | 26 sec | +0.040% | 0¢ | ❌ Lost | $0.00 |
| 10/7 4:44:18 PM | ETH | DOWN | 42 sec | +0.050% | 1¢ | ❌ Lost | -$0.15 |
| 10/7 4:44:18 PM | WTI | DOWN | 42 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/7 4:44:18 PM | SOL | DOWN | 42 sec | +0.081% | 0¢ | ❌ Lost | $0.00 |
| 10/7 4:44:18 PM | USDJPY | DOWN | 42 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/7 4:44:18 PM | XRP | DOWN | 42 sec | +0.127% | 0¢ | ❌ Lost | $0.00 |
| 10/7 4:43:15 PM | NEAR | DOWN | 1.8 min | +0.476% | 0¢ | ❌ Lost | $0.00 |
| 10/7 4:42:44 PM | BNB | DOWN | 2.2 min | +0.049% | 1¢ | ❌ Lost | -$0.15 |
| 10/7 4:40:38 PM | ZEC | DOWN | 4.4 min | +0.601% | 2¢ | ❌ Lost | -$0.15 |
| 10/7 4:29:52 PM | USDJPY | UP | 7 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/7 4:29:36 PM | PLATINUM | DOWN | 23 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/7 4:29:20 PM | WTI | DOWN | 39 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/7 4:29:20 PM | GBPUSD | DOWN | 39 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/7 4:29:04 PM | SILVER | UP | 55 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/7 4:28:48 PM | EURUSD | DOWN | 72 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/7 4:28:32 PM | NEAR | DOWN | 87 sec | +0.421% | 1¢ | ❌ Lost | -$0.15 |
| 10/7 4:28:16 PM | GOLD | UP | 1.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/7 4:28:16 PM | XRP | DOWN | 1.7 min | +0.127% | 0¢ | ❌ Lost | -$0.15 |
| 10/7 4:28:00 PM | DOGE | DOWN | 2.0 min | +0.196% | 0¢ | ❌ Lost | -$0.15 |
| 10/7 4:28:00 PM | ETH | DOWN | 2.0 min | +0.098% | 1¢ | ❌ Lost | -$0.15 |
| 10/7 4:28:00 PM | BTC | DOWN | 2.0 min | +0.104% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
