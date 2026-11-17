# 15-Minute 1¢ Study

*Updated Mon Nov 16, 11:45 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 4458 finished bets | 1% | $221.40 | +45% | +4.97¢ | $84.45 / $136.95 |

*Expect about **89 buys a day** (~$13.38/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 4202 | $120.55 | +27% |
| Volatility model ≥ 2%, hold to the close | 8299 | $80.05 | +8% |
| Momentum model ≥ 2%, hold to the close | 6893 | $7.65 | +1% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 59358 | 59311 | 227 (0%) | 1.07% | -$4,035.80 (-56%) | Hold to the close: -$4,035.80 (-56%) |

*In play or awaiting result: 19. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 35671 | 4.6% | 0.4% (148) | -638% | ❌ Worse |
| Momentum model | 35671 | 4.5% | 0.4% (148) | -664% | ❌ Worse |
| Mean-reversion model | 35671 | 7.9% | 0.4% (148) | -775% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 35671 | 148 | -47% | -87% | -87% | -85% |
| Volatility model ≥ 2% | 8299 | 77 | +8% | -77% | -76% | -72% |
| Volatility model ≥ 5% | 4458 | 51 | +45% | -72% | -70% | -67% |
| Volatility model ≥ 10% | 2565 | 30 | +70% | -63% | -61% | -58% |
| Momentum model ≥ 2% | 6893 | 57 | +1% | -79% | -78% | -74% |
| Momentum model ≥ 5% | 4202 | 41 | +27% | -74% | -74% | -70% |
| Momentum model ≥ 10% | 2739 | 26 | +35% | -66% | -66% | -62% |
| Mean-reversion model ≥ 2% | 14608 | 103 | -23% | -82% | -82% | -80% |
| Mean-reversion model ≥ 5% | 10165 | 85 | -7% | -80% | -79% | -77% |
| Mean-reversion model ≥ 10% | 6750 | 61 | +3% | -77% | -77% | -75% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 35877 | 5% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 14076 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 9358 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 59311 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 227 | 0% | -$4,035.80 | -56% | — |
| Sell at 2¢ | 2380 | 4% | -$6,301.00 | -87% | 47 sec |
| Sell at 3¢ | 1606 | 3% | -$6,293.46 | -87% | 48 sec |
| Sell at 5¢ | 1099 | 2% | -$6,177.45 | -86% | 63 sec |
| Sell at 10¢ | 669 | 1% | -$5,931.41 | -82% | 65 sec |
| Sell at 25¢ | 355 | 1% | -$5,506.75 | -76% | 80 sec |
| Sell at 50¢ | 234 | 0% | -$4,976.30 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 13 | 0 | 31% | 23% | -100% | -47% | -20% |
| 5–10 min | 2975 | 13 | 10% | 4% | -59% | -82% | -83% |
| 2–5 min | 19200 | 104 | 7% | 3% | -47% | -87% | -87% |
| 1–2 min | 14914 | 51 | 3% | 2% | -62% | -92% | -92% |
| Under 1 min | 22209 | 59 | 1% | 0% | -62% | -85% | -85% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 4015 | 19 | 5% | 3% | -38% | -88% | -87% |
| SOL | 4011 | 18 | 4% | 2% | -43% | -86% | -87% |
| HYPE | 4002 | 12 | 4% | 2% | -62% | -89% | -88% |
| BNB | 3993 | 20 | 5% | 2% | -37% | -86% | -85% |
| DOGE | 3991 | 11 | 4% | 2% | -65% | -90% | -89% |
| ETH | 3983 | 17 | 7% | 3% | -47% | -82% | -82% |
| BTC | 3966 | 21 | 5% | 2% | -28% | -86% | -88% |
| NEAR | 3965 | 17 | 5% | 2% | -44% | -85% | -86% |
| XRP | 3951 | 15 | 3% | 2% | -52% | -89% | -88% |
| GOLD | 2105 | 5 | 5% | 2% | -71% | -82% | -84% |
| WTI | 2088 | 7 | 4% | 1% | -59% | -91% | -92% |
| SILVER | 2047 | 9 | 5% | 2% | -48% | -83% | -83% |
| PLATINUM | 1866 | 4 | 3% | 1% | -80% | -95% | -95% |
| EURUSD | 1813 | 6 | 2% | 1% | -69% | -91% | -90% |
| COPPER | 1747 | 6 | 2% | 1% | -68% | -75% | -75% |
| GBPUSD | 1742 | 6 | 2% | 1% | -68% | -96% | -96% |
| NATGAS | 1723 | 9 | 2% | 1% | -51% | -75% | -74% |
| USDJPY | 1699 | 6 | 2% | 1% | -67% | -96% | -96% |
| PALLADIUM | 1678 | 4 | 1% | 0% | -78% | -92% | -93% |
| AUDUSD | 1256 | 6 | 2% | 1% | -55% | -89% | -89% |
| USDCAD | 1200 | 1 | 3% | 1% | -92% | -96% | -96% |
| BRENT | 822 | 0 | 2% | 1% | -100% | -97% | -97% |
| 10YRRATE | 418 | 2 | 4% | 1% | -55% | -71% | -70% |
| 2YRRATE | 403 | 4 | 4% | 2% | -7% | -47% | -46% |
| 30YRRATE | 388 | 0 | 2% | 1% | -100% | -96% | -94% |
| 5YRRATE | 375 | 2 | 4% | 2% | -50% | -94% | -95% |
| INX | 64 | 0 | 2% | 0% | -100% | -97% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 30169 | 113 | 4% | 2% | -57% | -88% | -88% |
| DOWN (bought NO) | 29142 | 114 | 4% | 2% | -55% | -86% | -87% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 5435 | 25 | 2% | 1% | -17% | -78% | -77% |
| 0.05–0.1% | 5878 | 24 | 3% | 2% | -37% | -91% | -91% |
| 0.1–0.2% | 8999 | 34 | 5% | 2% | -52% | -89% | -89% |
| 0.2–0.5% | 11090 | 48 | 7% | 3% | -51% | -86% | -86% |
| Over 0.5% | 4466 | 19 | 7% | 3% | -55% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 14411 | 45 | 4% | 2% | -64% | -88% | -88% |
| Morning (6am–12pm) | 13940 | 70 | 4% | 2% | -43% | -85% | -84% |
| Afternoon (12–6pm) | 14631 | 63 | 4% | 2% | -49% | -87% | -87% |
| Evening (6pm–12am) | 16329 | 49 | 4% | 2% | -66% | -89% | -89% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 5,083 |
| Time from buy to best bounce (bounced bets) | 50 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/16 11:44:47 PM | USDCAD | UP | 13 sec | — | 0¢ | In play | — |
| 11/16 11:44:47 PM | BNB | UP | 13 sec | -0.046% | 1¢ | ❌ Lost | -$0.15 |
| 11/16 11:44:31 PM | SILVER | UP | 29 sec | — | 1¢ | In play | — |
| 11/16 11:44:31 PM | GOLD | UP | 29 sec | — | 1¢ | In play | — |
| 11/16 11:44:31 PM | NATGAS | UP | 29 sec | — | 0¢ | In play | — |
| 11/16 11:44:15 PM | USDJPY | UP | 45 sec | — | 0¢ | In play | — |
| 11/16 11:44:15 PM | AUDUSD | UP | 45 sec | — | 0¢ | In play | — |
| 11/16 11:43:43 PM | NEAR | UP | 76 sec | -0.314% | 2¢ | ❌ Lost | -$0.15 |
| 11/16 11:43:11 PM | COPPER | UP | 1.8 min | — | 0¢ | In play | — |
| 11/16 11:39:29 PM | ZEC | UP | 5.5 min | -0.958% | 1¢ | In play | — |
| 11/16 11:39:29 PM | DOGE | UP | 5.5 min | -0.470% | 1¢ | In play | — |
| 11/16 11:38:42 PM | SOL | UP | 6.3 min | -0.693% | 1¢ | ❌ Lost | -$0.15 |
| 11/16 11:38:26 PM | BTC | UP | 6.6 min | -0.446% | 2¢ | In play | — |
| 11/16 11:38:10 PM | XRP | UP | 6.8 min | -0.573% | 1¢ | In play | — |
| 11/16 11:37:23 PM | ETH | UP | 7.6 min | -0.653% | 1¢ | In play | — |
| 11/16 11:36:36 PM | HYPE | UP | 8.4 min | -0.995% | 1¢ | In play | — |
| 11/16 11:29:56 PM | GOLD | DOWN | 3 sec | — | 0¢ | ❌ Lost | $0.00 |
| 11/16 11:29:56 PM | SOL | UP | 3 sec | -0.082% | 0¢ | ❌ Lost | $0.00 |
| 11/16 11:29:41 PM | SILVER | DOWN | 18 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 11/16 11:29:41 PM | USDCAD | DOWN | 18 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/16 11:29:41 PM | COPPER | DOWN | 18 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/16 11:29:25 PM | HYPE | UP | 34 sec | -0.131% | 0¢ | ❌ Lost | -$0.15 |
| 11/16 11:29:25 PM | DOGE | UP | 34 sec | -0.027% | 0¢ | ❌ Lost | -$0.15 |
| 11/16 11:28:53 PM | EURUSD | UP | 67 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/16 11:28:38 PM | AUDUSD | UP | 81 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/16 11:28:22 PM | ZEC | UP | 1.6 min | -0.422% | 0¢ | ❌ Lost | -$0.15 |
| 11/16 11:28:22 PM | USDJPY | DOWN | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/16 11:28:06 PM | BRENT | DOWN | 1.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/16 11:27:33 PM | ETH | UP | 2.5 min | -0.214% | 1¢ | ❌ Lost | -$0.15 |
| 11/16 11:27:33 PM | WTI | DOWN | 2.5 min | — | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
