# 15-Minute 1¢ Study

*Updated Mon Oct 12, 6:27 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 1215 finished bets | 1% | $36.00 | +27% | +2.96¢ | $32.45 / $3.55 |

*Expect about **82 buys a day** (~$12.36/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 1161 | $15.35 | +12% |
| 5+ min left, hold to the close | 441 | -$9.25 | -14% |
| Volatility model ≥ 2%, hold to the close | 2140 | -$19.25 | -7% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 16009 | 15995 | 62 (0%) | 1.07% | -$1,062.65 (-55%) | Hold to the close: -$1,062.65 (-55%) |

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
| Volatility model | 10615 | 4.5% | 0.4% (45) | -671% | ❌ Worse |
| Momentum model | 10615 | 4.5% | 0.4% (45) | -697% | ❌ Worse |
| Mean-reversion model | 10615 | 7.2% | 0.4% (45) | -779% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 10615 | 45 | -47% | -88% | -88% | -86% |
| Volatility model ≥ 2% | 2140 | 17 | -7% | -78% | -77% | -74% |
| Volatility model ≥ 5% | 1215 | 12 | +27% | -72% | -71% | -69% |
| Volatility model ≥ 10% | 763 | 8 | +51% | -63% | -63% | -59% |
| Momentum model ≥ 2% | 1883 | 14 | -10% | -79% | -80% | -78% |
| Momentum model ≥ 5% | 1161 | 10 | +12% | -76% | -76% | -73% |
| Momentum model ≥ 10% | 801 | 7 | +24% | -69% | -69% | -65% |
| Mean-reversion model ≥ 2% | 3743 | 26 | -24% | -85% | -85% | -82% |
| Mean-reversion model ≥ 5% | 2558 | 20 | -13% | -83% | -82% | -78% |
| Mean-reversion model ≥ 10% | 1697 | 14 | -4% | -81% | -81% | -78% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 10813 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 3821 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 1361 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 15995 | 3% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 62 | 0% | -$1,062.65 | -55% | — |
| Sell at 2¢ | 543 | 3% | -$1,747.47 | -91% | 33 sec |
| Sell at 3¢ | 359 | 2% | -$1,748.64 | -91% | 47 sec |
| Sell at 5¢ | 261 | 2% | -$1,719.00 | -89% | 50 sec |
| Sell at 10¢ | 171 | 1% | -$1,636.64 | -85% | 64 sec |
| Sell at 25¢ | 97 | 1% | -$1,511.58 | -78% | 80 sec |
| Sell at 50¢ | 64 | 0% | -$1,358.65 | -70% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 437 | 4 | 11% | 3% | -13% | -81% | -86% |
| 2–5 min | 5145 | 32 | 6% | 3% | -39% | -88% | -89% |
| 1–2 min | 4225 | 16 | 3% | 2% | -59% | -94% | -94% |
| Under 1 min | 6184 | 10 | 1% | 0% | -76% | -91% | -91% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 1214 | 7 | 4% | 2% | -29% | -90% | -90% |
| HYPE | 1211 | 4 | 4% | 2% | -59% | -90% | -89% |
| DOGE | 1205 | 2 | 4% | 2% | -79% | -91% | -90% |
| BNB | 1203 | 5 | 4% | 1% | -49% | -91% | -92% |
| ETH | 1202 | 8 | 5% | 2% | -19% | -90% | -89% |
| SOL | 1202 | 2 | 3% | 1% | -79% | -93% | -92% |
| BTC | 1196 | 5 | 5% | 2% | -44% | -88% | -91% |
| NEAR | 1190 | 7 | 5% | 2% | -23% | -76% | -77% |
| XRP | 1190 | 7 | 2% | 1% | -27% | -85% | -85% |
| GOLD | 629 | 0 | 3% | 1% | -100% | -93% | -94% |
| SILVER | 611 | 1 | 3% | 1% | -81% | -94% | -94% |
| WTI | 586 | 3 | 3% | 1% | -42% | -94% | -96% |
| COPPER | 548 | 0 | 1% | 1% | -100% | -98% | -98% |
| PLATINUM | 504 | 0 | 0% | 0% | -100% | -100% | -99% |
| PALLADIUM | 472 | 1 | 1% | 0% | -80% | -98% | -98% |
| NATGAS | 471 | 3 | 3% | 2% | -41% | -96% | -94% |
| EURUSD | 453 | 3 | 3% | 2% | -38% | -75% | -74% |
| GBPUSD | 432 | 1 | 2% | 1% | -78% | -96% | -96% |
| USDJPY | 389 | 3 | 1% | 1% | -28% | -98% | -97% |
| AUDUSD | 44 | 0 | 0% | 0% | -100% | -100% | -100% |
| USDCAD | 43 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 8090 | 34 | 3% | 2% | -51% | -90% | -89% |
| DOWN (bought NO) | 7905 | 28 | 3% | 2% | -59% | -91% | -92% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 1937 | 9 | 2% | 1% | -22% | -77% | -77% |
| 0.05–0.1% | 1932 | 6 | 3% | 1% | -55% | -92% | -92% |
| 0.1–0.2% | 2763 | 9 | 4% | 2% | -60% | -91% | -92% |
| 0.2–0.5% | 3006 | 18 | 5% | 3% | -34% | -89% | -88% |
| Over 0.5% | 1172 | 5 | 6% | 2% | -56% | -88% | -90% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 4019 | 20 | 4% | 2% | -43% | -86% | -86% |
| Morning (6am–12pm) | 3780 | 20 | 4% | 2% | -39% | -91% | -91% |
| Afternoon (12–6pm) | 3818 | 9 | 3% | 1% | -72% | -91% | -91% |
| Evening (6pm–12am) | 4378 | 13 | 3% | 2% | -66% | -94% | -93% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 25 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,536 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 41 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/12 6:27:47 PM | WTI | UP | 2.2 min | — | — | In play | — |
| 10/12 6:27:30 PM | HYPE | UP | 2.5 min | -0.407% | — | In play | — |
| 10/12 6:27:30 PM | XRP | UP | 2.5 min | -0.583% | — | In play | — |
| 10/12 6:27:14 PM | NEAR | UP | 2.8 min | -1.071% | — | In play | — |
| 10/12 6:26:58 PM | BNB | UP | 3.0 min | -0.310% | — | In play | — |
| 10/12 6:26:43 PM | NATGAS | UP | 3.3 min | — | — | In play | — |
| 10/12 6:26:12 PM | ZEC | UP | 3.8 min | -1.250% | — | In play | — |
| 10/12 6:14:25 PM | AUDUSD | UP | 35 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/12 6:14:25 PM | ZEC | UP | 35 sec | -0.222% | 0¢ | ❌ Lost | $0.00 |
| 10/12 6:14:25 PM | DOGE | UP | 35 sec | -0.252% | 0¢ | ❌ Lost | -$0.15 |
| 10/12 6:14:25 PM | GBPUSD | UP | 35 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/12 6:14:09 PM | HYPE | UP | 51 sec | -0.234% | 0¢ | ❌ Lost | -$0.15 |
| 10/12 6:14:09 PM | XRP | UP | 51 sec | -0.179% | 1¢ | ❌ Lost | -$0.15 |
| 10/12 6:13:53 PM | NEAR | DOWN | 67 sec | +0.755% | 0¢ | ❌ Lost | $0.00 |
| 10/12 6:13:37 PM | NATGAS | DOWN | 83 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/12 6:13:21 PM | EURUSD | UP | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/12 6:13:05 PM | COPPER | UP | 1.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/12 6:13:05 PM | WTI | UP | 1.9 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/12 6:12:18 PM | ETH | UP | 2.7 min | -0.791% | 1¢ | ❌ Lost | -$0.15 |
| 10/12 6:11:46 PM | PALLADIUM | UP | 3.2 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/12 6:10:58 PM | BTC | UP | 4.0 min | -0.388% | 2¢ | ❌ Lost | -$0.15 |
| 10/12 6:10:58 PM | GOLD | UP | 4.0 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/12 6:10:42 PM | PLATINUM | UP | 4.3 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/12 6:10:42 PM | SOL | UP | 4.3 min | -1.353% | 4¢ | ❌ Lost | -$0.15 |
| 10/12 6:10:11 PM | SILVER | UP | 4.8 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/12 6:09:39 PM | BNB | UP | 5.3 min | -0.747% | 4¢ | ❌ Lost | -$0.15 |
| 10/12 5:59:58 PM | EURUSD | UP | 1 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/12 5:59:42 PM | ZEC | DOWN | 17 sec | +0.037% | 1¢ | ❌ Lost | -$0.15 |
| 10/12 5:59:42 PM | USDJPY | DOWN | 17 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/12 5:59:26 PM | ETH | UP | 33 sec | -0.091% | 0¢ | ❌ Lost | $0.00 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
