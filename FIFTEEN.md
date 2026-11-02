# 15-Minute 1¢ Study

*Updated Sun Nov 1, 10:00 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 3465 finished bets | 1% | $130.85 | +34% | +3.78¢ | $74.00 / $56.85 |

*Expect about **99 buys a day** (~$14.88/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 3194 | $58.45 | +17% |
| Volatility model ≥ 2%, hold to the close | 6398 | $51.25 | +7% |
| Momentum model ≥ 2%, hold to the close | 5270 | -$35.45 | -6% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 42030 | 42008 | 158 (0%) | 1.07% | -$2,899.40 (-57%) | Hold to the close: -$2,899.40 (-57%) |

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
| Volatility model | 26221 | 4.7% | 0.4% (105) | -676% | ❌ Worse |
| Momentum model | 26221 | 4.6% | 0.4% (105) | -698% | ❌ Worse |
| Mean-reversion model | 26221 | 8.1% | 0.4% (105) | -824% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 26221 | 105 | -49% | -88% | -87% | -85% |
| Volatility model ≥ 2% | 6398 | 59 | +7% | -79% | -78% | -73% |
| Volatility model ≥ 5% | 3465 | 37 | +34% | -76% | -74% | -70% |
| Volatility model ≥ 10% | 1963 | 22 | +60% | -70% | -68% | -65% |
| Momentum model ≥ 2% | 5270 | 41 | -6% | -81% | -80% | -77% |
| Momentum model ≥ 5% | 3194 | 29 | +17% | -78% | -78% | -74% |
| Momentum model ≥ 10% | 2085 | 19 | +27% | -74% | -73% | -68% |
| Mean-reversion model ≥ 2% | 10838 | 75 | -24% | -83% | -83% | -80% |
| Mean-reversion model ≥ 5% | 7599 | 64 | -7% | -81% | -80% | -77% |
| Mean-reversion model ≥ 10% | 5084 | 46 | +3% | -79% | -79% | -76% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 26423 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 9827 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 5758 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 42008 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 158 | 0% | -$2,899.40 | -57% | — |
| Sell at 2¢ | 1648 | 4% | -$4,458.92 | -87% | 47 sec |
| Sell at 3¢ | 1132 | 3% | -$4,445.92 | -87% | 48 sec |
| Sell at 5¢ | 787 | 2% | -$4,347.85 | -85% | 63 sec |
| Sell at 10¢ | 474 | 1% | -$4,168.46 | -82% | 65 sec |
| Sell at 25¢ | 250 | 1% | -$3,849.90 | -75% | 83 sec |
| Sell at 50¢ | 163 | 0% | -$3,493.15 | -68% | 1.9 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 11 | 0 | 27% | 18% | -100% | -53% | -29% |
| 5–10 min | 1996 | 9 | 11% | 4% | -57% | -81% | -82% |
| 2–5 min | 13482 | 75 | 7% | 3% | -45% | -87% | -86% |
| 1–2 min | 10618 | 37 | 3% | 2% | -62% | -92% | -92% |
| Under 1 min | 15901 | 37 | 1% | 0% | -67% | -85% | -85% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 2960 | 13 | 5% | 3% | -44% | -88% | -87% |
| SOL | 2950 | 11 | 4% | 2% | -53% | -91% | -90% |
| BNB | 2948 | 17 | 5% | 2% | -28% | -85% | -84% |
| HYPE | 2947 | 9 | 5% | 3% | -62% | -89% | -87% |
| DOGE | 2935 | 6 | 4% | 2% | -74% | -90% | -90% |
| ETH | 2934 | 11 | 6% | 3% | -54% | -85% | -85% |
| BTC | 2918 | 14 | 5% | 2% | -35% | -87% | -89% |
| NEAR | 2916 | 15 | 5% | 2% | -33% | -83% | -83% |
| XRP | 2915 | 11 | 3% | 1% | -53% | -89% | -89% |
| GOLD | 1533 | 5 | 5% | 2% | -61% | -82% | -84% |
| SILVER | 1495 | 7 | 5% | 2% | -44% | -82% | -81% |
| WTI | 1492 | 4 | 3% | 1% | -68% | -93% | -93% |
| PLATINUM | 1328 | 3 | 2% | 1% | -79% | -96% | -96% |
| COPPER | 1267 | 5 | 1% | 1% | -63% | -75% | -75% |
| EURUSD | 1265 | 3 | 2% | 1% | -78% | -89% | -89% |
| NATGAS | 1223 | 7 | 2% | 1% | -47% | -81% | -80% |
| GBPUSD | 1197 | 2 | 2% | 1% | -84% | -96% | -96% |
| PALLADIUM | 1190 | 2 | 1% | 0% | -84% | -90% | -91% |
| USDJPY | 1186 | 5 | 2% | 1% | -61% | -97% | -96% |
| AUDUSD | 720 | 4 | 2% | 1% | -48% | -84% | -83% |
| USDCAD | 698 | 0 | 2% | 1% | -100% | -97% | -97% |
| BRENT | 299 | 0 | 1% | 1% | -100% | -98% | -97% |
| 10YRRATE | 188 | 1 | 5% | 2% | -50% | -41% | -39% |
| 30YRRATE | 177 | 0 | 1% | 0% | -100% | -98% | -97% |
| 2YRRATE | 170 | 2 | 5% | 1% | +10% | +18% | +19% |
| 5YRRATE | 157 | 1 | 6% | 3% | -41% | -89% | -92% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 21314 | 87 | 4% | 2% | -53% | -88% | -87% |
| DOWN (bought NO) | 20694 | 71 | 4% | 2% | -61% | -87% | -87% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 4316 | 21 | 2% | 1% | -16% | -82% | -81% |
| 0.05–0.1% | 4549 | 17 | 3% | 2% | -44% | -91% | -91% |
| 0.1–0.2% | 6834 | 24 | 4% | 2% | -56% | -90% | -89% |
| 0.2–0.5% | 7789 | 33 | 7% | 3% | -53% | -86% | -86% |
| Over 0.5% | 2930 | 12 | 7% | 3% | -58% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 10303 | 36 | 4% | 2% | -60% | -86% | -86% |
| Morning (6am–12pm) | 10513 | 48 | 5% | 2% | -48% | -85% | -84% |
| Afternoon (12–6pm) | 9923 | 37 | 4% | 2% | -56% | -87% | -87% |
| Evening (6pm–12am) | 11269 | 37 | 3% | 2% | -62% | -91% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,812 |
| Time from buy to best bounce (bounced bets) | 51 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/1 9:59:51 PM | GOLD | UP | 9 sec | — | 0¢ | In play | — |
| 11/1 9:59:51 PM | BRENT | UP | 9 sec | — | 0¢ | In play | — |
| 11/1 9:59:51 PM | EURUSD | DOWN | 9 sec | — | 0¢ | In play | — |
| 11/1 9:59:51 PM | PLATINUM | UP | 9 sec | — | 0¢ | In play | — |
| 11/1 9:59:35 PM | ZEC | DOWN | 25 sec | +0.056% | 0¢ | ❌ Lost | $0.00 |
| 11/1 9:59:20 PM | WTI | UP | 39 sec | — | 0¢ | In play | — |
| 11/1 9:59:20 PM | PALLADIUM | UP | 39 sec | — | 0¢ | In play | — |
| 11/1 9:59:01 PM | GBPUSD | DOWN | 58 sec | — | 0¢ | In play | — |
| 11/1 9:58:45 PM | DOGE | UP | 74 sec | -0.116% | 0¢ | ❌ Lost | $0.00 |
| 11/1 9:58:45 PM | BTC | UP | 74 sec | -0.109% | 0¢ | ❌ Lost | -$0.15 |
| 11/1 9:58:29 PM | NEAR | UP | 1.5 min | -0.292% | 1¢ | ❌ Lost | -$0.15 |
| 11/1 9:58:14 PM | XRP | UP | 1.8 min | -0.120% | 1¢ | In play | — |
| 11/1 9:58:14 PM | BNB | UP | 1.8 min | -0.119% | 0¢ | ❌ Lost | $0.00 |
| 11/1 9:57:08 PM | AUDUSD | DOWN | 2.9 min | — | 0¢ | In play | — |
| 11/1 9:57:08 PM | SOL | UP | 2.9 min | -0.221% | 1¢ | In play | — |
| 11/1 9:57:08 PM | HYPE | UP | 2.9 min | -0.300% | 0¢ | ❌ Lost | -$0.15 |
| 11/1 9:56:02 PM | USDJPY | UP | 4.0 min | — | 0¢ | In play | — |
| 11/1 9:54:21 PM | ETH | UP | 5.7 min | -0.371% | 1¢ | In play | — |
| 11/1 9:44:44 PM | USDJPY | DOWN | 16 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/1 9:44:28 PM | AUDUSD | DOWN | 32 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/1 9:44:28 PM | ZEC | UP | 32 sec | -0.323% | 0¢ | ❌ Lost | -$0.15 |
| 11/1 9:43:56 PM | PALLADIUM | UP | 63 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/1 9:42:36 PM | COPPER | UP | 2.4 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/1 9:42:36 PM | BTC | UP | 2.4 min | -0.163% | 1¢ | ❌ Lost | -$0.15 |
| 11/1 9:42:20 PM | NATGAS | DOWN | 2.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/1 9:42:04 PM | GOLD | UP | 2.9 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/1 9:41:16 PM | HYPE | UP | 3.7 min | -0.429% | 1¢ | ❌ Lost | -$0.15 |
| 11/1 9:41:01 PM | BRENT | DOWN | 4.0 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/1 9:40:45 PM | ETH | UP | 4.2 min | -0.205% | 0¢ | ❌ Lost | $0.00 |
| 11/1 9:40:45 PM | XRP | UP | 4.2 min | -0.207% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
