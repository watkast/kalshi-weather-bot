# 15-Minute 1¢ Study

*Updated Fri Oct 23, 10:16 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 2532 finished bets | 1% | $91.20 | +32% | +3.60¢ | $43.10 / $48.10 |

*Expect about **98 buys a day** (~$14.66/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 2339 | $63.40 | +25% |
| Volatility model ≥ 2%, hold to the close | 4692 | $13.35 | +2% |
| Momentum model ≥ 2%, hold to the close | 3903 | -$10.70 | -2% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 30586 | 30578 | 118 (0%) | 1.07% | -$2,077.00 (-56%) | Hold to the close: -$2,077.00 (-56%) |

*In play or awaiting result: 7. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 19371 | 4.6% | 0.4% (83) | -632% | ❌ Worse |
| Momentum model | 19371 | 4.6% | 0.4% (83) | -659% | ❌ Worse |
| Mean-reversion model | 19371 | 7.9% | 0.4% (83) | -762% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 19371 | 83 | -46% | -87% | -87% | -85% |
| Volatility model ≥ 2% | 4692 | 42 | +2% | -77% | -76% | -73% |
| Volatility model ≥ 5% | 2532 | 27 | +32% | -73% | -72% | -68% |
| Volatility model ≥ 10% | 1440 | 17 | +66% | -64% | -63% | -60% |
| Momentum model ≥ 2% | 3903 | 32 | -2% | -79% | -79% | -75% |
| Momentum model ≥ 5% | 2339 | 23 | +25% | -75% | -75% | -71% |
| Momentum model ≥ 10% | 1533 | 15 | +35% | -69% | -68% | -63% |
| Mean-reversion model ≥ 2% | 7793 | 54 | -24% | -83% | -82% | -80% |
| Mean-reversion model ≥ 5% | 5448 | 45 | -9% | -80% | -79% | -77% |
| Mean-reversion model ≥ 10% | 3622 | 32 | +0% | -78% | -77% | -74% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 19571 | 5% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 7352 | 2% | 2% | 1% | 1% | 0% | 0% |
| Financials | 3655 | 2% | 1% | 1% | 1% | 0% | 0% |
| **All** | 30578 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 118 | 0% | -$2,077.00 | -56% | — |
| Sell at 2¢ | 1142 | 4% | -$3,264.08 | -88% | 47 sec |
| Sell at 3¢ | 785 | 3% | -$3,254.85 | -87% | 48 sec |
| Sell at 5¢ | 550 | 2% | -$3,203.50 | -86% | 61 sec |
| Sell at 10¢ | 338 | 1% | -$3,076.22 | -82% | 64 sec |
| Sell at 25¢ | 186 | 1% | -$2,833.34 | -76% | 82 sec |
| Sell at 50¢ | 120 | 0% | -$2,555.00 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 1308 | 7 | 11% | 4% | -49% | -80% | -82% |
| 2–5 min | 9777 | 54 | 7% | 3% | -46% | -87% | -87% |
| 1–2 min | 7780 | 29 | 3% | 1% | -59% | -92% | -91% |
| Under 1 min | 11709 | 28 | 1% | 0% | -66% | -86% | -86% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 2193 | 12 | 5% | 2% | -31% | -89% | -89% |
| HYPE | 2185 | 8 | 5% | 3% | -55% | -88% | -86% |
| BNB | 2183 | 12 | 5% | 2% | -32% | -83% | -82% |
| SOL | 2177 | 5 | 4% | 2% | -72% | -92% | -92% |
| ETH | 2175 | 11 | 6% | 3% | -39% | -86% | -85% |
| DOGE | 2171 | 4 | 4% | 2% | -77% | -90% | -89% |
| XRP | 2166 | 9 | 3% | 1% | -49% | -88% | -88% |
| NEAR | 2161 | 12 | 5% | 3% | -28% | -81% | -81% |
| BTC | 2160 | 12 | 5% | 2% | -26% | -88% | -89% |
| GOLD | 1190 | 4 | 4% | 2% | -60% | -81% | -83% |
| SILVER | 1156 | 5 | 4% | 1% | -50% | -82% | -82% |
| WTI | 1143 | 3 | 3% | 1% | -69% | -94% | -95% |
| PLATINUM | 1010 | 0 | 1% | 1% | -100% | -98% | -98% |
| COPPER | 987 | 4 | 1% | 1% | -62% | -69% | -69% |
| EURUSD | 938 | 3 | 2% | 1% | -70% | -86% | -86% |
| NATGAS | 933 | 5 | 2% | 1% | -50% | -86% | -86% |
| PALLADIUM | 897 | 2 | 1% | 0% | -79% | -88% | -88% |
| GBPUSD | 884 | 1 | 2% | 1% | -89% | -96% | -96% |
| USDJPY | 866 | 5 | 1% | 1% | -46% | -98% | -97% |
| AUDUSD | 428 | 0 | 1% | 0% | -100% | -98% | -98% |
| USDCAD | 387 | 0 | 1% | 0% | -100% | -98% | -99% |
| 10YRRATE | 43 | 0 | 0% | 0% | -100% | -100% | -100% |
| 2YRRATE | 40 | 1 | 2% | 0% | +133% | +138% | +133% |
| 30YRRATE | 39 | 0 | 0% | 0% | -100% | -100% | -100% |
| BRENT | 36 | 0 | 0% | 0% | -100% | -100% | -100% |
| 5YRRATE | 30 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 15444 | 65 | 4% | 2% | -52% | -87% | -86% |
| DOWN (bought NO) | 15134 | 53 | 4% | 2% | -60% | -88% | -88% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 3225 | 17 | 2% | 1% | -11% | -79% | -78% |
| 0.05–0.1% | 3367 | 11 | 3% | 2% | -52% | -92% | -91% |
| 0.1–0.2% | 5044 | 19 | 5% | 2% | -53% | -89% | -89% |
| 0.2–0.5% | 5731 | 28 | 6% | 3% | -46% | -87% | -86% |
| Over 0.5% | 2200 | 10 | 7% | 3% | -53% | -87% | -88% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 7532 | 31 | 4% | 2% | -53% | -84% | -84% |
| Morning (6am–12pm) | 7425 | 34 | 4% | 2% | -48% | -88% | -87% |
| Afternoon (12–6pm) | 7298 | 24 | 4% | 2% | -61% | -87% | -88% |
| Evening (6pm–12am) | 8323 | 29 | 3% | 2% | -60% | -90% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,626 |
| Time from buy to best bounce (bounced bets) | 49 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/23 10:14:56 PM | DOGE | UP | 4 sec | -0.047% | 0¢ | ❌ Lost | $0.00 |
| 10/23 10:14:56 PM | HYPE | DOWN | 4 sec | +0.022% | 0¢ | ❌ Lost | $0.00 |
| 10/23 10:14:40 PM | XRP | DOWN | 20 sec | +0.008% | 0¢ | ❌ Lost | $0.00 |
| 10/23 10:14:08 PM | NEAR | UP | 52 sec | -0.263% | 1¢ | ❌ Lost | -$0.15 |
| 10/23 10:13:53 PM | BTC | UP | 66 sec | -0.091% | 1¢ | ❌ Lost | -$0.15 |
| 10/23 10:13:53 PM | SOL | UP | 66 sec | -0.114% | 0¢ | ❌ Lost | $0.00 |
| 10/23 10:13:53 PM | ETH | UP | 66 sec | -0.087% | 0¢ | ❌ Lost | -$0.15 |
| 10/23 9:59:59 PM | WTI | DOWN | 1 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/23 9:59:59 PM | XRP | DOWN | 1 sec | +0.008% | 0¢ | ❌ Lost | $0.00 |
| 10/23 9:59:43 PM | BTC | DOWN | 17 sec | +0.028% | 0¢ | ❌ Lost | $0.00 |
| 10/23 9:59:10 PM | BNB | DOWN | 49 sec | -0.033% | 1¢ | ❌ Lost | -$0.15 |
| 10/23 9:57:33 PM | HYPE | UP | 2.5 min | -0.129% | 18¢ | ❌ Lost | -$0.15 |
| 10/23 9:57:33 PM | ZEC | UP | 2.5 min | -0.250% | 18¢ | ❌ Lost | -$0.15 |
| 10/23 9:56:45 PM | DOGE | UP | 3.2 min | -0.180% | 2¢ | ❌ Lost | -$0.15 |
| 10/23 9:56:45 PM | SOL | UP | 3.2 min | -0.196% | 1¢ | ❌ Lost | -$0.15 |
| 10/23 9:56:09 PM | ETH | UP | 3.9 min | -0.158% | 1¢ | ❌ Lost | -$0.15 |
| 10/23 9:55:54 PM | NEAR | UP | 4.1 min | -0.512% | 1¢ | ❌ Lost | -$0.15 |
| 10/23 9:44:59 PM | BRENT | UP | 1 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/23 9:44:59 PM | HYPE | DOWN | 1 sec | -0.008% | 0¢ | ❌ Lost | $0.00 |
| 10/23 9:44:43 PM | DOGE | UP | 17 sec | -0.071% | 0¢ | ❌ Lost | $0.00 |
| 10/23 9:44:43 PM | SOL | DOWN | 17 sec | -0.004% | 0¢ | ❌ Lost | -$0.15 |
| 10/23 9:44:43 PM | NATGAS | UP | 17 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/23 9:44:27 PM | BTC | UP | 33 sec | -0.022% | 0¢ | ❌ Lost | $0.00 |
| 10/23 9:44:27 PM | WTI | UP | 33 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/23 9:43:56 PM | BNB | UP | 64 sec | -0.083% | 0¢ | ❌ Lost | $0.00 |
| 10/23 9:43:40 PM | ETH | UP | 80 sec | -0.060% | 1¢ | ❌ Lost | -$0.15 |
| 10/23 9:43:24 PM | XRP | UP | 1.6 min | -0.108% | 1¢ | ❌ Lost | -$0.15 |
| 10/23 9:43:24 PM | NEAR | UP | 1.6 min | -0.331% | 1¢ | ❌ Lost | -$0.15 |
| 10/23 9:41:30 PM | ZEC | DOWN | 3.5 min | +0.613% | 0¢ | ❌ Lost | -$0.15 |
| 10/23 9:29:56 PM | BTC | UP | 3 sec | -0.008% | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
