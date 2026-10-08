# 15-Minute 1¢ Study

*Updated Wed Oct 7, 9:16 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 760 finished bets | 1% | $30.25 | +37% | +3.98¢ | -$12.80 / $43.05 |

*Expect about **77 buys a day** (~$11.57/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 757 | $17.45 | +22% |
| 5+ min left, hold to the close | 301 | $11.45 | +26% |
| Volatility model ≥ 2%, hold to the close | 1395 | $0.30 | +0% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 11352 | 11346 | 49 (0%) | 1.07% | -$690.10 (-50%) | Hold to the close: -$690.10 (-50%) |

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
| Volatility model | 7318 | 4.1% | 0.5% (33) | -566% | ❌ Worse |
| Momentum model | 7318 | 4.1% | 0.5% (33) | -597% | ❌ Worse |
| Mean-reversion model | 7318 | 6.7% | 0.5% (33) | -659% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 7318 | 33 | -43% | -87% | -87% | -84% |
| Volatility model ≥ 2% | 1395 | 12 | +0% | -73% | -73% | -69% |
| Volatility model ≥ 5% | 760 | 8 | +37% | -63% | -61% | -58% |
| Volatility model ≥ 10% | 476 | 6 | +85% | -46% | -47% | -42% |
| Momentum model ≥ 2% | 1237 | 10 | -2% | -74% | -75% | -73% |
| Momentum model ≥ 5% | 757 | 7 | +22% | -67% | -69% | -66% |
| Momentum model ≥ 10% | 524 | 6 | +65% | -56% | -57% | -53% |
| Mean-reversion model ≥ 2% | 2506 | 19 | -18% | -84% | -85% | -80% |
| Mean-reversion model ≥ 5% | 1698 | 15 | -2% | -81% | -81% | -75% |
| Mean-reversion model ≥ 10% | 1126 | 11 | +12% | -80% | -80% | -75% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 7515 | 4% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 2872 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 959 | 3% | 2% | 2% | 1% | 1% | 0% |
| **All** | 11346 | 3% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 49 | 0% | -$690.10 | -50% | — |
| Sell at 2¢ | 397 | 3% | -$1,230.88 | -89% | 33 sec |
| Sell at 3¢ | 264 | 2% | -$1,231.14 | -89% | 47 sec |
| Sell at 5¢ | 196 | 2% | -$1,206.70 | -88% | 50 sec |
| Sell at 10¢ | 130 | 1% | -$1,149.80 | -84% | 64 sec |
| Sell at 25¢ | 75 | 1% | -$1,043.85 | -76% | 82 sec |
| Sell at 50¢ | 49 | 0% | -$919.35 | -67% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 297 | 4 | 10% | 3% | +27% | -82% | -86% |
| 2–5 min | 3668 | 25 | 7% | 3% | -33% | -88% | -88% |
| 1–2 min | 2987 | 12 | 3% | 2% | -57% | -94% | -93% |
| Under 1 min | 4390 | 8 | 1% | 0% | -73% | -88% | -88% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 842 | 6 | 5% | 3% | -15% | -90% | -90% |
| HYPE | 842 | 3 | 5% | 3% | -56% | -89% | -87% |
| DOGE | 838 | 2 | 3% | 1% | -70% | -92% | -92% |
| BNB | 836 | 3 | 4% | 2% | -57% | -90% | -92% |
| ETH | 835 | 7 | 5% | 3% | +4% | -88% | -88% |
| NEAR | 832 | 5 | 6% | 3% | -21% | -70% | -71% |
| SOL | 831 | 0 | 3% | 1% | -100% | -93% | -92% |
| BTC | 830 | 4 | 5% | 2% | -37% | -88% | -90% |
| XRP | 829 | 5 | 2% | 1% | -24% | -81% | -81% |
| GOLD | 480 | 0 | 4% | 1% | -100% | -92% | -95% |
| SILVER | 468 | 0 | 3% | 1% | -100% | -95% | -94% |
| WTI | 444 | 3 | 2% | 1% | -26% | -95% | -97% |
| COPPER | 410 | 0 | 1% | 0% | -100% | -99% | -99% |
| PLATINUM | 372 | 0 | 0% | 0% | -100% | -100% | -99% |
| NATGAS | 352 | 3 | 3% | 2% | -20% | -95% | -93% |
| PALLADIUM | 346 | 1 | 1% | 1% | -73% | -97% | -98% |
| EURUSD | 342 | 3 | 4% | 2% | -18% | -67% | -65% |
| GBPUSD | 324 | 1 | 3% | 2% | -71% | -95% | -95% |
| USDJPY | 286 | 3 | 1% | 1% | -2% | -98% | -96% |
| AUDUSD | 4 | 0 | 0% | 0% | -100% | -100% | -100% |
| USDCAD | 3 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 5751 | 26 | 4% | 2% | -48% | -88% | -88% |
| DOWN (bought NO) | 5595 | 23 | 3% | 2% | -53% | -91% | -91% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 1240 | 8 | 2% | 1% | +11% | -66% | -66% |
| 0.05–0.1% | 1293 | 4 | 3% | 1% | -55% | -91% | -92% |
| 0.1–0.2% | 1914 | 6 | 4% | 2% | -61% | -92% | -92% |
| 0.2–0.5% | 2192 | 12 | 6% | 3% | -40% | -89% | -87% |
| Over 0.5% | 874 | 5 | 6% | 3% | -41% | -88% | -90% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 2890 | 17 | 4% | 2% | -32% | -84% | -84% |
| Morning (6am–12pm) | 2706 | 17 | 4% | 2% | -28% | -91% | -90% |
| Afternoon (12–6pm) | 2560 | 7 | 3% | 1% | -68% | -88% | -89% |
| Evening (6pm–12am) | 3190 | 8 | 3% | 1% | -71% | -94% | -94% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 25 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,100 |
| Time from buy to best bounce (bounced bets) | 49 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/7 9:14:56 PM | USDJPY | DOWN | 3 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/7 9:14:25 PM | PLATINUM | UP | 34 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/7 9:14:25 PM | COPPER | UP | 34 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/7 9:14:25 PM | AUDUSD | UP | 34 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/7 9:14:09 PM | GOLD | UP | 50 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/7 9:14:09 PM | PALLADIUM | UP | 50 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/7 9:14:09 PM | EURUSD | UP | 50 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/7 9:13:53 PM | WTI | DOWN | 66 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/7 9:13:23 PM | SILVER | UP | 1.6 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/7 9:13:23 PM | GBPUSD | UP | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/7 9:12:35 PM | BNB | UP | 2.4 min | -0.157% | 1¢ | ❌ Lost | -$0.15 |
| 10/7 9:12:19 PM | DOGE | UP | 2.7 min | -0.284% | 1¢ | ❌ Lost | -$0.15 |
| 10/7 9:12:03 PM | HYPE | UP | 3.0 min | -0.354% | 1¢ | ❌ Lost | -$0.15 |
| 10/7 9:12:03 PM | XRP | UP | 3.0 min | -0.309% | 0¢ | ❌ Lost | -$0.15 |
| 10/7 9:11:47 PM | BTC | UP | 3.2 min | -0.219% | 1¢ | ❌ Lost | -$0.15 |
| 10/7 9:11:47 PM | ZEC | UP | 3.2 min | -0.581% | 1¢ | ❌ Lost | -$0.15 |
| 10/7 9:11:02 PM | ETH | UP | 4.0 min | -0.272% | 1¢ | ❌ Lost | -$0.15 |
| 10/7 9:10:38 PM | SOL | UP | 4.4 min | -0.329% | 1¢ | ❌ Lost | -$0.15 |
| 10/7 9:08:00 PM | NEAR | UP | 7.0 min | -1.570% | 1¢ | ❌ Lost | -$0.15 |
| 10/7 8:59:19 PM | XRP | UP | 41 sec | -0.077% | 0¢ | ❌ Lost | $0.00 |
| 10/7 8:59:03 PM | PALLADIUM | UP | 57 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/7 8:59:03 PM | BTC | UP | 57 sec | -0.084% | 0¢ | ❌ Lost | $0.00 |
| 10/7 8:59:03 PM | ZEC | UP | 57 sec | -0.244% | 0¢ | ❌ Lost | $0.00 |
| 10/7 8:58:46 PM | SOL | UP | 73 sec | -0.087% | 1¢ | ❌ Lost | -$0.15 |
| 10/7 8:58:46 PM | HYPE | UP | 73 sec | -0.159% | 1¢ | ❌ Lost | -$0.15 |
| 10/7 8:57:58 PM | NEAR | UP | 2.0 min | -0.650% | 1¢ | ❌ Lost | -$0.15 |
| 10/7 8:57:58 PM | ETH | UP | 2.0 min | -0.117% | 1¢ | ❌ Lost | -$0.15 |
| 10/7 8:57:43 PM | DOGE | UP | 2.3 min | -0.188% | 1¢ | ❌ Lost | -$0.15 |
| 10/7 8:57:27 PM | BNB | UP | 2.5 min | -0.111% | 1¢ | ❌ Lost | -$0.15 |
| 10/7 8:57:27 PM | PLATINUM | UP | 2.5 min | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
