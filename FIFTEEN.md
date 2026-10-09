# 15-Minute 1¢ Study

*Updated Fri Oct 9, 4:04 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 894 finished bets | 1% | $28.65 | +29% | +3.20¢ | -$5.40 / $34.05 |

*Expect about **77 buys a day** (~$11.52/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 871 | $18.40 | +20% |
| 5+ min left, hold to the close | 383 | -$0.55 | -1% |
| Volatility model ≥ 5%, sell at 50¢ | 894 | -$8.60 | -9% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 13277 | 13270 | 52 (0%) | 1.07% | -$882.70 (-55%) | Hold to the close: -$882.70 (-55%) |

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
| Volatility model | 8441 | 4.0% | 0.4% (35) | -587% | ❌ Worse |
| Momentum model | 8441 | 4.1% | 0.4% (35) | -621% | ❌ Worse |
| Mean-reversion model | 8441 | 6.7% | 0.4% (35) | -687% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 8441 | 35 | -48% | -88% | -88% | -86% |
| Volatility model ≥ 2% | 1630 | 13 | -8% | -75% | -75% | -72% |
| Volatility model ≥ 5% | 894 | 9 | +29% | -68% | -66% | -64% |
| Volatility model ≥ 10% | 547 | 7 | +87% | -52% | -52% | -48% |
| Momentum model ≥ 2% | 1442 | 11 | -8% | -77% | -78% | -75% |
| Momentum model ≥ 5% | 871 | 8 | +20% | -71% | -72% | -69% |
| Momentum model ≥ 10% | 597 | 6 | +44% | -62% | -63% | -59% |
| Mean-reversion model ≥ 2% | 2946 | 20 | -26% | -85% | -85% | -81% |
| Mean-reversion model ≥ 5% | 1988 | 16 | -11% | -82% | -82% | -77% |
| Mean-reversion model ≥ 10% | 1305 | 12 | +5% | -81% | -81% | -76% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 8638 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 3429 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 1203 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 13270 | 3% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 52 | 0% | -$882.70 | -55% | — |
| Sell at 2¢ | 443 | 3% | -$1,453.52 | -90% | 33 sec |
| Sell at 3¢ | 295 | 2% | -$1,453.65 | -90% | 47 sec |
| Sell at 5¢ | 216 | 2% | -$1,428.30 | -89% | 56 sec |
| Sell at 10¢ | 142 | 1% | -$1,354.68 | -84% | 64 sec |
| Sell at 25¢ | 81 | 1% | -$1,244.59 | -77% | 81 sec |
| Sell at 50¢ | 53 | 0% | -$1,112.95 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 379 | 4 | 10% | 3% | +0% | -82% | -86% |
| 2–5 min | 4288 | 26 | 6% | 3% | -41% | -89% | -89% |
| 1–2 min | 3461 | 13 | 3% | 2% | -59% | -94% | -94% |
| Under 1 min | 5138 | 9 | 1% | 0% | -74% | -90% | -90% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 966 | 6 | 4% | 3% | -25% | -90% | -90% |
| HYPE | 966 | 3 | 5% | 2% | -61% | -89% | -88% |
| DOGE | 964 | 2 | 3% | 1% | -74% | -92% | -92% |
| BNB | 963 | 4 | 4% | 2% | -50% | -91% | -92% |
| ETH | 959 | 7 | 5% | 2% | -10% | -89% | -89% |
| NEAR | 956 | 5 | 6% | 3% | -31% | -73% | -74% |
| BTC | 956 | 4 | 5% | 2% | -45% | -88% | -90% |
| SOL | 955 | 0 | 3% | 1% | -100% | -94% | -93% |
| XRP | 953 | 6 | 2% | 1% | -21% | -82% | -82% |
| GOLD | 568 | 0 | 4% | 1% | -100% | -92% | -94% |
| SILVER | 555 | 1 | 3% | 1% | -79% | -94% | -94% |
| WTI | 524 | 3 | 3% | 1% | -35% | -94% | -96% |
| COPPER | 490 | 0 | 1% | 0% | -100% | -99% | -99% |
| PLATINUM | 451 | 0 | 0% | 0% | -100% | -100% | -99% |
| NATGAS | 421 | 3 | 3% | 2% | -33% | -95% | -93% |
| PALLADIUM | 420 | 1 | 1% | 0% | -78% | -98% | -99% |
| EURUSD | 412 | 3 | 3% | 2% | -32% | -72% | -71% |
| GBPUSD | 389 | 1 | 3% | 2% | -76% | -96% | -95% |
| USDJPY | 353 | 3 | 1% | 1% | -21% | -98% | -97% |
| AUDUSD | 25 | 0 | 0% | 0% | -100% | -100% | -100% |
| USDCAD | 24 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 6685 | 27 | 3% | 2% | -53% | -89% | -89% |
| DOWN (bought NO) | 6585 | 25 | 3% | 1% | -56% | -91% | -92% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 1398 | 8 | 2% | 1% | -1% | -70% | -69% |
| 0.05–0.1% | 1464 | 4 | 3% | 1% | -60% | -92% | -92% |
| 0.1–0.2% | 2205 | 7 | 4% | 2% | -60% | -92% | -92% |
| 0.2–0.5% | 2522 | 13 | 5% | 3% | -43% | -89% | -88% |
| Over 0.5% | 1047 | 5 | 6% | 2% | -51% | -88% | -90% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 3343 | 18 | 4% | 2% | -38% | -85% | -85% |
| Morning (6am–12pm) | 3238 | 17 | 4% | 2% | -40% | -91% | -91% |
| Afternoon (12–6pm) | 3068 | 8 | 3% | 1% | -69% | -90% | -90% |
| Evening (6pm–12am) | 3621 | 9 | 3% | 1% | -72% | -95% | -95% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 25 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,036 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/9 3:59:54 PM | WTI | UP | 6 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/9 3:59:54 PM | BTC | UP | 6 sec | -0.021% | 1¢ | ❌ Lost | -$0.15 |
| 10/9 3:59:54 PM | ETH | DOWN | 6 sec | +0.029% | 0¢ | ❌ Lost | $0.00 |
| 10/9 3:59:54 PM | DOGE | DOWN | 6 sec | -0.018% | 0¢ | ❌ Lost | -$0.15 |
| 10/9 3:59:38 PM | XRP | DOWN | 22 sec | +0.029% | 0¢ | ❌ Lost | $0.00 |
| 10/9 3:59:22 PM | ZEC | UP | 38 sec | -0.058% | 0¢ | ❌ Lost | $0.00 |
| 10/9 3:59:22 PM | BNB | UP | 38 sec | -0.066% | 0¢ | ❌ Lost | $0.00 |
| 10/9 3:59:06 PM | HYPE | UP | 54 sec | -0.050% | 1¢ | ❌ Lost | -$0.15 |
| 10/9 3:59:06 PM | SOL | UP | 54 sec | -0.072% | 1¢ | ❌ Lost | -$0.15 |
| 10/9 3:58:01 PM | NEAR | DOWN | 2.0 min | +0.380% | 0¢ | ❌ Lost | -$0.15 |
| 10/9 3:44:32 PM | XRP | UP | 28 sec | -0.036% | 1¢ | ❌ Lost | -$0.15 |
| 10/9 3:44:32 PM | NATGAS | DOWN | 28 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/9 3:44:32 PM | BNB | DOWN | 28 sec | -0.026% | 0¢ | ❌ Lost | $0.00 |
| 10/9 3:44:32 PM | HYPE | DOWN | 28 sec | +0.021% | 0¢ | ❌ Lost | -$0.15 |
| 10/9 3:44:16 PM | ETH | DOWN | 44 sec | +0.034% | 1¢ | ❌ Lost | -$0.15 |
| 10/9 3:44:01 PM | BTC | UP | 58 sec | -0.040% | 0¢ | ❌ Lost | -$0.15 |
| 10/9 3:44:01 PM | SOL | UP | 58 sec | -0.065% | 1¢ | ❌ Lost | -$0.15 |
| 10/9 3:43:29 PM | ZEC | DOWN | 1.5 min | +0.114% | 1¢ | ❌ Lost | -$0.15 |
| 10/9 3:42:57 PM | NEAR | DOWN | 2.0 min | +0.572% | 0¢ | ❌ Lost | $0.00 |
| 10/9 3:42:57 PM | DOGE | DOWN | 2.0 min | +0.132% | 1¢ | ❌ Lost | -$0.15 |
| 10/9 3:29:50 PM | BTC | DOWN | 10 sec | +0.010% | 0¢ | ❌ Lost | $0.00 |
| 10/9 3:29:34 PM | XRP | DOWN | 26 sec | +0.022% | 0¢ | ❌ Lost | $0.00 |
| 10/9 3:29:18 PM | NATGAS | UP | 42 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/9 3:28:31 PM | HYPE | DOWN | 88 sec | +0.128% | 0¢ | ❌ Lost | -$0.15 |
| 10/9 3:28:31 PM | SOL | DOWN | 88 sec | +0.076% | 0¢ | ❌ Lost | -$0.15 |
| 10/9 3:27:43 PM | BNB | DOWN | 2.3 min | +0.047% | 0¢ | ❌ Lost | -$0.15 |
| 10/9 3:27:27 PM | ZEC | DOWN | 2.5 min | +0.408% | 0¢ | ❌ Lost | -$0.15 |
| 10/9 3:27:27 PM | DOGE | DOWN | 2.5 min | +0.158% | 1¢ | ❌ Lost | -$0.15 |
| 10/9 3:27:11 PM | NEAR | DOWN | 2.8 min | +0.492% | 1¢ | ❌ Lost | -$0.15 |
| 10/9 3:14:54 PM | ZEC | DOWN | 6 sec | +0.088% | 0¢ | ❌ Lost | $0.00 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
