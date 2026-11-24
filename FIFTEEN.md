# 15-Minute 1¢ Study

*Updated Tue Nov 24, 3:59 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 4855 finished bets | 1% | $212.05 | +40% | +4.37¢ | $75.50 / $136.55 |

*Expect about **84 buys a day** (~$12.63/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 4604 | $110.30 | +22% |
| Volatility model ≥ 2%, hold to the close | 9041 | $41.80 | +4% |
| Momentum model ≥ 2%, hold to the close | 7528 | -$30.05 | -4% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 66855 | 66810 | 255 (0%) | 1.07% | -$4,519.35 (-56%) | Hold to the close: -$4,519.35 (-56%) |

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
| Volatility model | 39742 | 4.5% | 0.4% (164) | -644% | ❌ Worse |
| Momentum model | 39742 | 4.4% | 0.4% (164) | -667% | ❌ Worse |
| Mean-reversion model | 39742 | 7.9% | 0.4% (164) | -783% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 39742 | 164 | -46% | -87% | -86% | -84% |
| Volatility model ≥ 2% | 9041 | 80 | +4% | -77% | -76% | -73% |
| Volatility model ≥ 5% | 4855 | 53 | +40% | -73% | -72% | -68% |
| Volatility model ≥ 10% | 2813 | 32 | +68% | -64% | -63% | -59% |
| Momentum model ≥ 2% | 7528 | 59 | -4% | -79% | -79% | -76% |
| Momentum model ≥ 5% | 4604 | 43 | +22% | -75% | -75% | -71% |
| Momentum model ≥ 10% | 3003 | 28 | +34% | -68% | -67% | -63% |
| Mean-reversion model ≥ 2% | 16164 | 112 | -24% | -82% | -82% | -80% |
| Mean-reversion model ≥ 5% | 11249 | 92 | -9% | -80% | -79% | -77% |
| Mean-reversion model ≥ 10% | 7473 | 66 | +1% | -78% | -77% | -75% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 39948 | 5% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 15859 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 11003 | 3% | 2% | 1% | 1% | 0% | 0% |
| **All** | 66810 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 255 | 0% | -$4,519.35 | -56% | — |
| Sell at 2¢ | 2732 | 4% | -$7,085.03 | -88% | 47 sec |
| Sell at 3¢ | 1838 | 3% | -$7,078.53 | -88% | 48 sec |
| Sell at 5¢ | 1250 | 2% | -$6,954.85 | -86% | 62 sec |
| Sell at 10¢ | 766 | 1% | -$6,679.89 | -83% | 65 sec |
| Sell at 25¢ | 412 | 1% | -$6,165.63 | -76% | 79 sec |
| Sell at 50¢ | 265 | 0% | -$5,558.60 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 13 | 0 | 31% | 23% | -100% | -47% | -20% |
| 5–10 min | 3442 | 17 | 11% | 4% | -53% | -81% | -83% |
| 2–5 min | 21629 | 116 | 7% | 3% | -47% | -86% | -86% |
| 1–2 min | 16718 | 57 | 3% | 2% | -62% | -92% | -92% |
| Under 1 min | 25008 | 65 | 1% | 0% | -62% | -87% | -86% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 4466 | 19 | 5% | 2% | -43% | -88% | -87% |
| HYPE | 4460 | 16 | 5% | 2% | -54% | -89% | -88% |
| SOL | 4457 | 20 | 4% | 2% | -42% | -86% | -86% |
| BNB | 4449 | 22 | 5% | 2% | -37% | -86% | -85% |
| DOGE | 4444 | 12 | 5% | 2% | -65% | -89% | -89% |
| ETH | 4440 | 19 | 7% | 3% | -46% | -82% | -82% |
| BTC | 4418 | 24 | 5% | 2% | -25% | -86% | -87% |
| NEAR | 4413 | 18 | 5% | 2% | -47% | -85% | -86% |
| XRP | 4401 | 16 | 4% | 2% | -54% | -89% | -88% |
| GOLD | 2349 | 8 | 5% | 2% | -58% | -82% | -84% |
| WTI | 2335 | 8 | 4% | 2% | -58% | -91% | -92% |
| SILVER | 2291 | 9 | 5% | 2% | -53% | -83% | -84% |
| PLATINUM | 2077 | 5 | 3% | 1% | -78% | -95% | -95% |
| EURUSD | 2037 | 7 | 3% | 1% | -68% | -91% | -90% |
| COPPER | 1970 | 6 | 2% | 1% | -72% | -78% | -78% |
| GBPUSD | 1970 | 8 | 2% | 1% | -62% | -96% | -96% |
| USDJPY | 1936 | 6 | 2% | 1% | -71% | -96% | -96% |
| NATGAS | 1930 | 10 | 2% | 1% | -52% | -77% | -77% |
| PALLADIUM | 1871 | 4 | 1% | 1% | -80% | -93% | -93% |
| AUDUSD | 1489 | 7 | 2% | 1% | -56% | -90% | -90% |
| USDCAD | 1405 | 1 | 3% | 1% | -93% | -96% | -96% |
| BRENT | 1036 | 1 | 2% | 1% | -91% | -96% | -97% |
| 10YRRATE | 538 | 2 | 3% | 1% | -65% | -77% | -75% |
| 2YRRATE | 501 | 4 | 4% | 2% | -25% | -56% | -55% |
| 30YRRATE | 498 | 0 | 3% | 1% | -100% | -95% | -93% |
| 5YRRATE | 488 | 2 | 4% | 2% | -62% | -94% | -95% |
| INX | 124 | 1 | 2% | 1% | -25% | -97% | -98% |
| USDMXN | 17 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 34165 | 131 | 4% | 2% | -56% | -88% | -88% |
| DOWN (bought NO) | 32645 | 124 | 4% | 2% | -56% | -87% | -87% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 5817 | 25 | 2% | 1% | -21% | -79% | -78% |
| 0.05–0.1% | 6368 | 26 | 3% | 2% | -35% | -91% | -90% |
| 0.1–0.2% | 9939 | 36 | 5% | 2% | -52% | -89% | -89% |
| 0.2–0.5% | 12580 | 56 | 7% | 3% | -49% | -86% | -86% |
| Over 0.5% | 5235 | 23 | 7% | 3% | -54% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 16271 | 50 | 4% | 2% | -65% | -88% | -88% |
| Morning (6am–12pm) | 15699 | 81 | 4% | 2% | -41% | -85% | -85% |
| Afternoon (12–6pm) | 16623 | 73 | 4% | 2% | -48% | -87% | -87% |
| Evening (6pm–12am) | 18217 | 51 | 4% | 2% | -68% | -89% | -89% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 5,119 |
| Time from buy to best bounce (bounced bets) | 50 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/24 3:59:43 PM | USDCAD | UP | 17 sec | — | — | In play | — |
| 11/24 3:59:43 PM | WTI | UP | 17 sec | — | — | In play | — |
| 11/24 3:59:22 PM | GBPUSD | UP | 38 sec | — | — | In play | — |
| 11/24 3:59:22 PM | NEAR | UP | 38 sec | -0.094% | — | In play | — |
| 11/24 3:59:06 PM | DOGE | UP | 54 sec | -0.170% | — | In play | — |
| 11/24 3:59:06 PM | HYPE | DOWN | 54 sec | +0.072% | — | In play | — |
| 11/24 3:59:06 PM | ETH | UP | 54 sec | -0.099% | — | In play | — |
| 11/24 3:58:35 PM | XRP | DOWN | 84 sec | +0.076% | — | In play | — |
| 11/24 3:58:35 PM | BNB | UP | 84 sec | -0.138% | — | In play | — |
| 11/24 3:58:17 PM | ZEC | DOWN | 1.7 min | +0.283% | — | In play | — |
| 11/24 3:58:17 PM | BTC | UP | 1.7 min | -0.115% | — | In play | — |
| 11/24 3:44:56 PM | NATGAS | DOWN | 3 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/24 3:44:56 PM | BNB | DOWN | 3 sec | -0.053% | 0¢ | ❌ Lost | $0.00 |
| 11/24 3:44:38 PM | BRENT | DOWN | 21 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/24 3:44:38 PM | USDJPY | UP | 21 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/24 3:44:38 PM | NEAR | UP | 21 sec | -0.139% | 0¢ | ❌ Lost | -$0.15 |
| 11/24 3:44:22 PM | GBPUSD | DOWN | 37 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/24 3:43:50 PM | HYPE | DOWN | 70 sec | +0.173% | 0¢ | ❌ Lost | $0.00 |
| 11/24 3:43:50 PM | EURUSD | DOWN | 70 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/24 3:43:50 PM | BTC | DOWN | 70 sec | +0.082% | 1¢ | ❌ Lost | -$0.15 |
| 11/24 3:43:31 PM | ETH | DOWN | 88 sec | +0.132% | 0¢ | ❌ Lost | $0.00 |
| 11/24 3:43:15 PM | DOGE | DOWN | 1.7 min | +0.096% | 1¢ | ❌ Lost | -$0.15 |
| 11/24 3:42:43 PM | XRP | DOWN | 2.3 min | +0.130% | 0¢ | ❌ Lost | -$0.15 |
| 11/24 3:41:33 PM | ZEC | DOWN | 3.4 min | +0.827% | 0¢ | ❌ Lost | -$0.15 |
| 11/24 3:40:26 PM | SOL | DOWN | 4.6 min | +0.355% | 1¢ | ❌ Lost | -$0.15 |
| 11/24 3:29:10 PM | BNB | DOWN | 49 sec | +0.051% | 0¢ | ❌ Lost | $0.00 |
| 11/24 3:29:10 PM | HYPE | DOWN | 49 sec | +0.262% | 0¢ | ❌ Lost | $0.00 |
| 11/24 3:28:54 PM | DOGE | DOWN | 65 sec | +0.116% | 1¢ | ❌ Lost | -$0.15 |
| 11/24 3:28:54 PM | BTC | DOWN | 65 sec | +0.065% | 1¢ | ❌ Lost | -$0.15 |
| 11/24 3:28:38 PM | USDJPY | DOWN | 81 sec | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
