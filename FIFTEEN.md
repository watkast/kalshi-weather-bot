# 15-Minute 1¢ Study

*Updated Wed Oct 14, 6:38 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 1376 finished bets | 1% | $30.65 | +20% | +2.23¢ | $38.20 / -$7.55 |

*Expect about **85 buys a day** (~$12.70/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 1300 | $13.75 | +10% |
| 5+ min left, hold to the close | 547 | -$24.55 | -30% |
| Volatility model ≥ 5%, sell at 50¢ | 1376 | -$28.35 | -19% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 17798 | 17787 | 66 (0%) | 1.07% | -$1,230.15 (-57%) | Hold to the close: -$1,230.15 (-57%) |

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
| Volatility model | 11655 | 4.5% | 0.4% (46) | -682% | ❌ Worse |
| Momentum model | 11655 | 4.4% | 0.4% (46) | -708% | ❌ Worse |
| Mean-reversion model | 11655 | 7.3% | 0.4% (46) | -806% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 11655 | 46 | -51% | -88% | -88% | -86% |
| Volatility model ≥ 2% | 2444 | 18 | -15% | -78% | -78% | -74% |
| Volatility model ≥ 5% | 1376 | 13 | +20% | -73% | -72% | -68% |
| Volatility model ≥ 10% | 839 | 9 | +53% | -64% | -63% | -60% |
| Momentum model ≥ 2% | 2139 | 15 | -15% | -80% | -80% | -78% |
| Momentum model ≥ 5% | 1300 | 11 | +10% | -77% | -77% | -74% |
| Momentum model ≥ 10% | 885 | 8 | +27% | -71% | -70% | -66% |
| Mean-reversion model ≥ 2% | 4234 | 27 | -30% | -85% | -85% | -82% |
| Mean-reversion model ≥ 5% | 2890 | 20 | -23% | -83% | -82% | -78% |
| Mean-reversion model ≥ 10% | 1906 | 14 | -15% | -80% | -80% | -77% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 11853 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 4331 | 2% | 2% | 1% | 1% | 0% | 0% |
| Financials | 1603 | 2% | 1% | 1% | 1% | 0% | 0% |
| **All** | 17787 | 3% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 66 | 0% | -$1,230.15 | -57% | — |
| Sell at 2¢ | 616 | 3% | -$1,951.99 | -91% | 34 sec |
| Sell at 3¢ | 414 | 2% | -$1,950.69 | -91% | 46 sec |
| Sell at 5¢ | 302 | 2% | -$1,915.85 | -89% | 49 sec |
| Sell at 10¢ | 192 | 1% | -$1,832.63 | -85% | 63 sec |
| Sell at 25¢ | 109 | 1% | -$1,695.36 | -79% | 79 sec |
| Sell at 50¢ | 72 | 0% | -$1,500.15 | -70% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 543 | 4 | 10% | 2% | -30% | -82% | -88% |
| 2–5 min | 5718 | 32 | 7% | 3% | -45% | -88% | -88% |
| 1–2 min | 4669 | 18 | 3% | 2% | -58% | -94% | -93% |
| Under 1 min | 6853 | 12 | 1% | 0% | -75% | -92% | -92% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 1328 | 7 | 4% | 2% | -34% | -90% | -90% |
| HYPE | 1325 | 4 | 4% | 2% | -63% | -90% | -89% |
| ETH | 1322 | 8 | 5% | 3% | -26% | -89% | -88% |
| BNB | 1322 | 5 | 4% | 2% | -54% | -90% | -90% |
| DOGE | 1320 | 2 | 4% | 2% | -81% | -91% | -90% |
| SOL | 1316 | 2 | 3% | 1% | -81% | -93% | -92% |
| BTC | 1307 | 6 | 5% | 2% | -39% | -88% | -91% |
| XRP | 1307 | 7 | 2% | 1% | -34% | -86% | -86% |
| NEAR | 1306 | 7 | 5% | 2% | -30% | -77% | -78% |
| GOLD | 703 | 1 | 4% | 1% | -83% | -91% | -93% |
| SILVER | 690 | 2 | 3% | 1% | -66% | -94% | -93% |
| WTI | 663 | 3 | 3% | 1% | -47% | -94% | -96% |
| COPPER | 613 | 1 | 2% | 1% | -85% | -97% | -96% |
| PLATINUM | 583 | 0 | 1% | 1% | -100% | -99% | -98% |
| PALLADIUM | 541 | 1 | 1% | 0% | -83% | -98% | -98% |
| NATGAS | 538 | 3 | 2% | 2% | -48% | -96% | -95% |
| EURUSD | 517 | 3 | 3% | 2% | -46% | -77% | -76% |
| GBPUSD | 484 | 1 | 2% | 1% | -81% | -96% | -96% |
| USDJPY | 443 | 3 | 1% | 1% | -37% | -98% | -98% |
| AUDUSD | 85 | 0 | 0% | 0% | -100% | -100% | -100% |
| USDCAD | 74 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 8935 | 35 | 3% | 2% | -55% | -90% | -89% |
| DOWN (bought NO) | 8852 | 31 | 3% | 2% | -59% | -91% | -92% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 2073 | 10 | 2% | 1% | -19% | -78% | -78% |
| 0.05–0.1% | 2109 | 6 | 3% | 1% | -59% | -92% | -91% |
| 0.1–0.2% | 3028 | 9 | 4% | 2% | -63% | -91% | -91% |
| 0.2–0.5% | 3352 | 18 | 6% | 3% | -41% | -89% | -88% |
| Over 0.5% | 1288 | 5 | 6% | 2% | -60% | -88% | -90% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 4717 | 20 | 4% | 2% | -52% | -87% | -88% |
| Morning (6am–12pm) | 3953 | 21 | 4% | 2% | -38% | -91% | -90% |
| Afternoon (12–6pm) | 4113 | 10 | 3% | 1% | -71% | -91% | -91% |
| Evening (6pm–12am) | 5004 | 15 | 3% | 2% | -66% | -94% | -93% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 25 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,503 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/14 6:37:39 AM | ETH | UP | 7.3 min | -1.233% | — | In play | — |
| 10/14 6:37:39 AM | GOLD | UP | 7.3 min | — | — | In play | — |
| 10/14 6:37:22 AM | SILVER | UP | 7.6 min | — | — | In play | — |
| 10/14 6:36:03 AM | NEAR | UP | 8.9 min | -3.209% | — | In play | — |
| 10/14 6:29:31 AM | AUDUSD | DOWN | 29 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 6:29:31 AM | WTI | UP | 29 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/14 6:29:31 AM | GOLD | DOWN | 29 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/14 6:29:31 AM | NEAR | DOWN | 29 sec | +0.205% | 0¢ | ❌ Lost | $0.00 |
| 10/14 6:29:15 AM | ZEC | UP | 45 sec | -0.458% | 0¢ | ❌ Lost | $0.00 |
| 10/14 6:28:43 AM | XRP | DOWN | 77 sec | +0.225% | 0¢ | ❌ Lost | $0.00 |
| 10/14 6:28:43 AM | COPPER | DOWN | 77 sec | — | 95¢ | ✅ Won | $13.85 |
| 10/14 6:25:54 AM | DOGE | UP | 4.1 min | -0.400% | 66¢ | ❌ Lost | -$0.15 |
| 10/14 6:25:20 AM | ETH | UP | 4.7 min | -0.272% | 67¢ | ❌ Lost | -$0.15 |
| 10/14 6:25:20 AM | BNB | UP | 4.7 min | -0.224% | 83¢ | ❌ Lost | -$0.15 |
| 10/14 6:25:04 AM | SOL | UP | 4.9 min | -0.398% | 53¢ | ❌ Lost | -$0.15 |
| 10/14 6:25:04 AM | HYPE | UP | 4.9 min | -0.383% | 64¢ | ❌ Lost | -$0.15 |
| 10/14 6:14:44 AM | NATGAS | UP | 15 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 6:14:28 AM | WTI | UP | 31 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/14 6:14:28 AM | USDCAD | UP | 31 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 6:14:28 AM | PALLADIUM | DOWN | 31 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 6:13:07 AM | EURUSD | DOWN | 1.9 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/14 6:12:49 AM | PLATINUM | DOWN | 2.2 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 6:12:33 AM | GOLD | DOWN | 2.5 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/14 6:12:33 AM | SILVER | DOWN | 2.5 min | — | 0¢ | ❌ Lost | $0.00 |
| 10/14 6:11:30 AM | NEAR | DOWN | 3.5 min | +0.397% | 1¢ | ❌ Lost | -$0.15 |
| 10/14 6:10:25 AM | ZEC | DOWN | 4.6 min | +0.418% | 1¢ | ❌ Lost | -$0.15 |
| 10/14 6:10:25 AM | COPPER | DOWN | 4.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 6:10:25 AM | BNB | DOWN | 4.6 min | +0.176% | 1¢ | ❌ Lost | -$0.15 |
| 10/14 6:10:09 AM | XRP | DOWN | 4.8 min | +0.408% | 0¢ | ❌ Lost | -$0.15 |
| 10/14 6:10:09 AM | HYPE | DOWN | 4.8 min | +0.417% | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
