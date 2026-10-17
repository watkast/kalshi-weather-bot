# 15-Minute 1¢ Study

*Updated Sat Oct 17, 3:29 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 1736 finished bets | 1% | $73.70 | +38% | +4.25¢ | $31.80 / $41.90 |

*Expect about **91 buys a day** (~$13.62/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 1599 | $36.90 | +21% |
| Momentum model ≥ 2%, hold to the close | 2698 | -$18.60 | -6% |
| Volatility model ≥ 5%, sell at 50¢ | 1736 | -$28.80 | -15% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 21715 | 21699 | 81 (0%) | 1.07% | -$1,503.75 (-57%) | Hold to the close: -$1,503.75 (-57%) |

*In play or awaiting result: 15. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 13975 | 4.5% | 0.4% (55) | -663% | ❌ Worse |
| Momentum model | 13975 | 4.4% | 0.4% (55) | -686% | ❌ Worse |
| Mean-reversion model | 13975 | 7.5% | 0.4% (55) | -796% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 13975 | 55 | -51% | -88% | -88% | -86% |
| Volatility model ≥ 2% | 3151 | 24 | -12% | -79% | -78% | -74% |
| Volatility model ≥ 5% | 1736 | 19 | +38% | -74% | -73% | -69% |
| Volatility model ≥ 10% | 1013 | 11 | +55% | -67% | -66% | -63% |
| Momentum model ≥ 2% | 2698 | 21 | -6% | -81% | -81% | -78% |
| Momentum model ≥ 5% | 1599 | 15 | +21% | -78% | -77% | -74% |
| Momentum model ≥ 10% | 1063 | 10 | +32% | -73% | -73% | -68% |
| Mean-reversion model ≥ 2% | 5316 | 35 | -28% | -84% | -84% | -81% |
| Mean-reversion model ≥ 5% | 3670 | 27 | -19% | -82% | -82% | -79% |
| Mean-reversion model ≥ 10% | 2416 | 16 | -24% | -80% | -80% | -78% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 14173 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 5309 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 2217 | 1% | 1% | 1% | 1% | 0% | 0% |
| **All** | 21699 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 81 | 0% | -$1,503.75 | -57% | — |
| Sell at 2¢ | 775 | 4% | -$2,338.25 | -89% | 37 sec |
| Sell at 3¢ | 519 | 2% | -$2,337.34 | -89% | 47 sec |
| Sell at 5¢ | 373 | 2% | -$2,297.30 | -87% | 50 sec |
| Sell at 10¢ | 225 | 1% | -$2,217.00 | -84% | 63 sec |
| Sell at 25¢ | 127 | 1% | -$2,049.38 | -78% | 79 sec |
| Sell at 50¢ | 84 | 0% | -$1,832.75 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 740 | 5 | 10% | 3% | -36% | -82% | -85% |
| 2–5 min | 7009 | 38 | 7% | 3% | -47% | -88% | -88% |
| 1–2 min | 5646 | 20 | 3% | 2% | -61% | -92% | -92% |
| Under 1 min | 8300 | 18 | 1% | 0% | -69% | -88% | -88% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 1593 | 11 | 5% | 3% | -14% | -90% | -90% |
| HYPE | 1588 | 6 | 4% | 2% | -53% | -90% | -88% |
| ETH | 1579 | 8 | 6% | 3% | -39% | -88% | -87% |
| DOGE | 1577 | 2 | 4% | 2% | -84% | -91% | -90% |
| BNB | 1577 | 6 | 5% | 2% | -53% | -89% | -89% |
| SOL | 1572 | 2 | 3% | 2% | -84% | -92% | -92% |
| XRP | 1566 | 7 | 2% | 1% | -45% | -86% | -87% |
| NEAR | 1562 | 8 | 6% | 3% | -33% | -78% | -78% |
| BTC | 1559 | 7 | 5% | 2% | -40% | -88% | -91% |
| GOLD | 864 | 1 | 3% | 1% | -86% | -92% | -94% |
| SILVER | 841 | 4 | 3% | 1% | -45% | -80% | -80% |
| WTI | 821 | 3 | 3% | 1% | -57% | -94% | -95% |
| COPPER | 735 | 2 | 2% | 1% | -75% | -84% | -84% |
| PLATINUM | 722 | 0 | 1% | 0% | -100% | -99% | -99% |
| NATGAS | 667 | 5 | 2% | 2% | -30% | -82% | -81% |
| PALLADIUM | 659 | 2 | 1% | 0% | -72% | -84% | -84% |
| EURUSD | 659 | 3 | 3% | 1% | -58% | -81% | -81% |
| GBPUSD | 615 | 1 | 2% | 1% | -85% | -97% | -97% |
| USDJPY | 574 | 3 | 1% | 1% | -51% | -99% | -98% |
| AUDUSD | 200 | 0 | 0% | 0% | -100% | -99% | -99% |
| USDCAD | 169 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 10937 | 41 | 4% | 2% | -57% | -89% | -89% |
| DOWN (bought NO) | 10762 | 40 | 4% | 2% | -57% | -88% | -89% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 2389 | 11 | 2% | 1% | -23% | -80% | -80% |
| 0.05–0.1% | 2445 | 7 | 3% | 1% | -58% | -92% | -92% |
| 0.1–0.2% | 3569 | 12 | 4% | 2% | -58% | -90% | -90% |
| 0.2–0.5% | 4133 | 21 | 6% | 3% | -44% | -88% | -88% |
| Over 0.5% | 1634 | 6 | 6% | 3% | -62% | -88% | -89% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 5468 | 21 | 4% | 2% | -56% | -88% | -88% |
| Morning (6am–12pm) | 5104 | 27 | 4% | 2% | -39% | -87% | -86% |
| Afternoon (12–6pm) | 5104 | 16 | 3% | 1% | -63% | -88% | -89% |
| Evening (6pm–12am) | 6023 | 17 | 3% | 2% | -68% | -92% | -91% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,503 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/17 3:29:26 AM | SOL | UP | 33 sec | -0.064% | — | In play | — |
| 10/17 3:29:10 AM | BTC | UP | 49 sec | -0.057% | — | In play | — |
| 10/17 3:28:22 AM | ETH | UP | 1.6 min | -0.067% | — | In play | — |
| 10/17 3:28:06 AM | HYPE | UP | 1.9 min | -0.132% | — | In play | — |
| 10/17 3:27:49 AM | XRP | UP | 2.2 min | -0.138% | — | In play | — |
| 10/17 3:27:33 AM | BNB | UP | 2.4 min | -0.051% | — | In play | — |
| 10/17 3:27:33 AM | ZEC | UP | 2.4 min | -0.249% | — | In play | — |
| 10/17 3:27:17 AM | DOGE | UP | 2.7 min | -0.146% | — | In play | — |
| 10/17 3:26:44 AM | NEAR | UP | 3.2 min | -0.630% | — | In play | — |
| 10/17 3:14:58 AM | BTC | UP | 2 sec | -0.005% | 0¢ | ❌ Lost | $0.00 |
| 10/17 3:14:26 AM | ETH | UP | 34 sec | -0.014% | 1¢ | ❌ Lost | -$0.15 |
| 10/17 3:14:10 AM | XRP | UP | 50 sec | -0.061% | 1¢ | ❌ Lost | -$0.15 |
| 10/17 3:13:54 AM | ZEC | DOWN | 66 sec | +0.141% | 0¢ | ❌ Lost | $0.00 |
| 10/17 3:13:38 AM | HYPE | UP | 82 sec | -0.071% | 2¢ | ❌ Lost | $0.00 |
| 10/17 3:13:22 AM | NEAR | DOWN | 1.6 min | +0.344% | 1¢ | ❌ Lost | -$0.15 |
| 10/17 3:13:22 AM | BNB | DOWN | 1.6 min | +0.025% | 1¢ | ❌ Lost | -$0.15 |
| 10/17 3:13:06 AM | DOGE | UP | 1.9 min | -0.091% | 0¢ | ❌ Lost | $0.00 |
| 10/17 2:59:56 AM | HYPE | DOWN | 3 sec | -0.040% | 0¢ | ❌ Lost | $0.00 |
| 10/17 2:59:08 AM | BTC | DOWN | 51 sec | +0.057% | 0¢ | ❌ Lost | $0.00 |
| 10/17 2:58:35 AM | DOGE | UP | 84 sec | -0.056% | 1¢ | ❌ Lost | -$0.15 |
| 10/17 2:58:19 AM | XRP | DOWN | 1.7 min | +0.046% | 1¢ | ❌ Lost | -$0.15 |
| 10/17 2:57:13 AM | NEAR | DOWN | 2.8 min | +0.594% | 1¢ | ❌ Lost | -$0.15 |
| 10/17 2:56:40 AM | ETH | DOWN | 3.3 min | +0.118% | 1¢ | ❌ Lost | -$0.15 |
| 10/17 2:56:24 AM | ZEC | DOWN | 3.6 min | +0.458% | 1¢ | ❌ Lost | -$0.15 |
| 10/17 2:56:24 AM | SOL | DOWN | 3.6 min | +0.133% | 1¢ | ❌ Lost | -$0.15 |
| 10/17 2:44:58 AM | HYPE | UP | 2 sec | -0.034% | 1¢ | ❌ Lost | -$0.15 |
| 10/17 2:44:42 AM | BNB | UP | 18 sec | -0.010% | 0¢ | ❌ Lost | -$0.15 |
| 10/17 2:44:42 AM | ZEC | DOWN | 18 sec | +0.047% | 0¢ | ❌ Lost | -$0.15 |
| 10/17 2:43:37 AM | SOL | UP | 82 sec | -0.069% | 1¢ | ❌ Lost | -$0.15 |
| 10/17 2:43:37 AM | ETH | UP | 82 sec | -0.036% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
