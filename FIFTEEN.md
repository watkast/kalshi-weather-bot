# 15-Minute 1¢ Study

*Updated Wed Oct 7, 8:15 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 756 finished bets | 1% | $30.70 | +38% | +4.06¢ | -$12.80 / $43.50 |

*Expect about **77 buys a day** (~$11.57/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 754 | $17.75 | +22% |
| 5+ min left, hold to the close | 296 | $12.05 | +27% |
| Volatility model ≥ 2%, hold to the close | 1388 | $1.20 | +1% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 11288 | 11271 | 49 (0%) | 1.07% | -$681.10 (-50%) | Hold to the close: -$681.10 (-50%) |

*In play or awaiting result: 17. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 7277 | 4.1% | 0.5% (33) | -562% | ❌ Worse |
| Momentum model | 7277 | 4.1% | 0.5% (33) | -593% | ❌ Worse |
| Mean-reversion model | 7277 | 6.7% | 0.5% (33) | -656% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 7277 | 33 | -43% | -87% | -87% | -84% |
| Volatility model ≥ 2% | 1388 | 12 | +1% | -73% | -73% | -69% |
| Volatility model ≥ 5% | 756 | 8 | +38% | -62% | -61% | -58% |
| Volatility model ≥ 10% | 473 | 6 | +87% | -46% | -46% | -41% |
| Momentum model ≥ 2% | 1234 | 10 | -2% | -74% | -75% | -73% |
| Momentum model ≥ 5% | 754 | 7 | +22% | -67% | -68% | -66% |
| Momentum model ≥ 10% | 521 | 6 | +66% | -56% | -57% | -53% |
| Mean-reversion model ≥ 2% | 2491 | 19 | -17% | -84% | -84% | -80% |
| Mean-reversion model ≥ 5% | 1686 | 15 | -1% | -81% | -81% | -75% |
| Mean-reversion model ≥ 10% | 1116 | 11 | +14% | -79% | -80% | -75% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 7474 | 4% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 2851 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 946 | 3% | 2% | 2% | 1% | 1% | 0% |
| **All** | 11271 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 49 | 0% | -$681.10 | -50% | — |
| Sell at 2¢ | 396 | 4% | -$1,222.14 | -89% | 34 sec |
| Sell at 3¢ | 263 | 2% | -$1,222.53 | -89% | 47 sec |
| Sell at 5¢ | 195 | 2% | -$1,198.35 | -88% | 51 sec |
| Sell at 10¢ | 130 | 1% | -$1,140.80 | -83% | 64 sec |
| Sell at 25¢ | 75 | 1% | -$1,034.85 | -76% | 82 sec |
| Sell at 50¢ | 49 | 0% | -$910.35 | -67% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 292 | 4 | 11% | 3% | +29% | -81% | -86% |
| 2–5 min | 3643 | 25 | 7% | 3% | -33% | -88% | -88% |
| 1–2 min | 2971 | 12 | 3% | 2% | -57% | -94% | -93% |
| Under 1 min | 4361 | 8 | 1% | 0% | -73% | -88% | -88% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 837 | 6 | 5% | 3% | -15% | -90% | -90% |
| HYPE | 837 | 3 | 5% | 3% | -56% | -89% | -87% |
| DOGE | 833 | 2 | 3% | 1% | -70% | -92% | -92% |
| ETH | 831 | 7 | 5% | 3% | +5% | -89% | -88% |
| BNB | 831 | 3 | 4% | 2% | -56% | -90% | -92% |
| NEAR | 828 | 5 | 6% | 3% | -21% | -70% | -71% |
| SOL | 827 | 0 | 3% | 1% | -100% | -93% | -92% |
| BTC | 826 | 4 | 5% | 2% | -36% | -88% | -90% |
| XRP | 824 | 5 | 2% | 1% | -24% | -81% | -81% |
| GOLD | 476 | 0 | 4% | 1% | -100% | -92% | -94% |
| SILVER | 464 | 0 | 3% | 1% | -100% | -95% | -94% |
| WTI | 442 | 3 | 2% | 1% | -26% | -95% | -97% |
| COPPER | 408 | 0 | 1% | 0% | -100% | -99% | -99% |
| PLATINUM | 367 | 0 | 0% | 0% | -100% | -100% | -99% |
| NATGAS | 351 | 3 | 3% | 2% | -20% | -95% | -93% |
| PALLADIUM | 343 | 1 | 1% | 1% | -73% | -97% | -98% |
| EURUSD | 339 | 3 | 4% | 2% | -17% | -66% | -65% |
| GBPUSD | 320 | 1 | 3% | 2% | -71% | -95% | -95% |
| USDJPY | 281 | 3 | 1% | 1% | -0% | -98% | -96% |
| USDCAD | 3 | 0 | 0% | 0% | -100% | -100% | -100% |
| AUDUSD | 3 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 5711 | 26 | 4% | 2% | -47% | -88% | -88% |
| DOWN (bought NO) | 5560 | 23 | 3% | 2% | -52% | -91% | -91% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 1234 | 8 | 2% | 1% | +12% | -66% | -65% |
| 0.05–0.1% | 1282 | 4 | 3% | 1% | -55% | -91% | -92% |
| 0.1–0.2% | 1905 | 6 | 4% | 2% | -61% | -92% | -92% |
| 0.2–0.5% | 2181 | 12 | 6% | 3% | -40% | -89% | -88% |
| Over 0.5% | 870 | 5 | 6% | 3% | -41% | -88% | -90% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 2890 | 17 | 4% | 2% | -32% | -84% | -84% |
| Morning (6am–12pm) | 2706 | 17 | 4% | 2% | -28% | -91% | -90% |
| Afternoon (12–6pm) | 2560 | 7 | 3% | 1% | -68% | -88% | -89% |
| Evening (6pm–12am) | 3115 | 8 | 3% | 1% | -70% | -94% | -94% |

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
| 10/7 8:14:49 PM | DOGE | DOWN | 10 sec | +0.044% | 0¢ | In play | — |
| 10/7 8:14:49 PM | HYPE | DOWN | 10 sec | +0.017% | 0¢ | In play | — |
| 10/7 8:14:34 PM | BNB | DOWN | 25 sec | -0.023% | 1¢ | In play | — |
| 10/7 8:14:34 PM | XRP | UP | 25 sec | -0.056% | 1¢ | In play | — |
| 10/7 8:14:34 PM | ZEC | UP | 25 sec | -0.143% | 0¢ | In play | — |
| 10/7 8:14:18 PM | GBPUSD | DOWN | 41 sec | — | 0¢ | In play | — |
| 10/7 8:14:02 PM | USDJPY | UP | 57 sec | — | 0¢ | In play | — |
| 10/7 8:13:31 PM | SOL | DOWN | 88 sec | +0.139% | 0¢ | ❌ Lost | -$0.15 |
| 10/7 8:13:15 PM | PALLADIUM | DOWN | 1.7 min | — | 0¢ | In play | — |
| 10/7 8:13:15 PM | SILVER | DOWN | 1.7 min | — | 1¢ | In play | — |
| 10/7 8:13:15 PM | PLATINUM | DOWN | 1.7 min | — | 0¢ | In play | — |
| 10/7 8:12:59 PM | NEAR | DOWN | 2.0 min | +0.486% | 0¢ | ❌ Lost | $0.00 |
| 10/7 8:11:39 PM | GOLD | DOWN | 3.4 min | — | 1¢ | In play | — |
| 10/7 7:59:52 PM | PLATINUM | UP | 7 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/7 7:59:52 PM | COPPER | UP | 7 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/7 7:58:49 PM | WTI | DOWN | 71 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/7 7:58:18 PM | AUDUSD | DOWN | 1.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/7 7:58:02 PM | ZEC | UP | 2.0 min | -0.394% | 0¢ | ❌ Lost | -$0.15 |
| 10/7 7:58:02 PM | XRP | UP | 2.0 min | -0.253% | 1¢ | ❌ Lost | -$0.15 |
| 10/7 7:57:46 PM | EURUSD | DOWN | 2.2 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/7 7:57:31 PM | DOGE | UP | 2.5 min | -0.142% | 1¢ | ❌ Lost | -$0.15 |
| 10/7 7:57:31 PM | NEAR | UP | 2.5 min | -1.002% | 1¢ | ❌ Lost | -$0.15 |
| 10/7 7:57:31 PM | GBPUSD | DOWN | 2.5 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/7 7:57:31 PM | HYPE | UP | 2.5 min | -0.214% | 1¢ | ❌ Lost | -$0.15 |
| 10/7 7:57:15 PM | ETH | UP | 2.8 min | -0.140% | 1¢ | ❌ Lost | -$0.15 |
| 10/7 7:57:15 PM | SOL | UP | 2.8 min | -0.181% | 1¢ | ❌ Lost | -$0.15 |
| 10/7 7:57:15 PM | BTC | UP | 2.8 min | -0.144% | 1¢ | ❌ Lost | -$0.15 |
| 10/7 7:56:26 PM | NATGAS | DOWN | 3.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/7 7:56:26 PM | BNB | UP | 3.6 min | -0.189% | 0¢ | ❌ Lost | -$0.15 |
| 10/7 7:44:49 PM | PLATINUM | DOWN | 10 sec | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
