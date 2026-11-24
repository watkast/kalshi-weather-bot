# 15-Minute 1¢ Study

*Updated Tue Nov 24, 2:15 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 4846 finished bets | 1% | $213.10 | +40% | +4.40¢ | $75.65 / $137.45 |

*Expect about **84 buys a day** (~$12.62/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 4595 | $111.35 | +23% |
| Volatility model ≥ 2%, hold to the close | 9027 | $43.60 | +4% |
| Momentum model ≥ 2%, hold to the close | 7516 | -$28.55 | -3% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 66758 | 66711 | 255 (0%) | 1.07% | -$4,507.05 (-56%) | Hold to the close: -$4,507.05 (-56%) |

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
| Volatility model | 39687 | 4.5% | 0.4% (164) | -643% | ❌ Worse |
| Momentum model | 39687 | 4.4% | 0.4% (164) | -666% | ❌ Worse |
| Mean-reversion model | 39687 | 7.9% | 0.4% (164) | -781% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 39687 | 164 | -46% | -87% | -86% | -84% |
| Volatility model ≥ 2% | 9027 | 80 | +4% | -77% | -76% | -73% |
| Volatility model ≥ 5% | 4846 | 53 | +40% | -73% | -71% | -68% |
| Volatility model ≥ 10% | 2808 | 32 | +68% | -64% | -63% | -59% |
| Momentum model ≥ 2% | 7516 | 59 | -3% | -79% | -79% | -75% |
| Momentum model ≥ 5% | 4595 | 43 | +23% | -75% | -75% | -71% |
| Momentum model ≥ 10% | 2998 | 28 | +35% | -68% | -67% | -63% |
| Mean-reversion model ≥ 2% | 16134 | 112 | -24% | -82% | -82% | -80% |
| Mean-reversion model ≥ 5% | 11227 | 92 | -9% | -80% | -79% | -77% |
| Mean-reversion model ≥ 10% | 7462 | 66 | +1% | -78% | -77% | -75% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 39893 | 5% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 15834 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 10984 | 3% | 2% | 1% | 1% | 0% | 0% |
| **All** | 66711 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 255 | 0% | -$4,507.05 | -56% | — |
| Sell at 2¢ | 2728 | 4% | -$7,073.77 | -88% | 47 sec |
| Sell at 3¢ | 1836 | 3% | -$7,067.01 | -87% | 48 sec |
| Sell at 5¢ | 1250 | 2% | -$6,942.55 | -86% | 62 sec |
| Sell at 10¢ | 766 | 1% | -$6,667.59 | -83% | 65 sec |
| Sell at 25¢ | 412 | 1% | -$6,153.33 | -76% | 79 sec |
| Sell at 50¢ | 265 | 0% | -$5,546.30 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 13 | 0 | 31% | 23% | -100% | -47% | -20% |
| 5–10 min | 3440 | 17 | 11% | 4% | -53% | -81% | -83% |
| 2–5 min | 21599 | 116 | 7% | 3% | -47% | -86% | -86% |
| 1–2 min | 16686 | 57 | 3% | 2% | -62% | -92% | -92% |
| Under 1 min | 24973 | 65 | 1% | 0% | -62% | -87% | -86% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 4460 | 19 | 5% | 2% | -43% | -88% | -87% |
| HYPE | 4454 | 16 | 5% | 2% | -54% | -89% | -88% |
| SOL | 4451 | 20 | 4% | 2% | -42% | -86% | -86% |
| BNB | 4442 | 22 | 5% | 2% | -37% | -86% | -85% |
| DOGE | 4438 | 12 | 4% | 2% | -65% | -89% | -89% |
| ETH | 4434 | 19 | 7% | 3% | -46% | -82% | -82% |
| BTC | 4412 | 24 | 5% | 2% | -25% | -86% | -87% |
| NEAR | 4407 | 18 | 5% | 2% | -46% | -85% | -86% |
| XRP | 4395 | 16 | 4% | 2% | -53% | -89% | -88% |
| GOLD | 2346 | 8 | 5% | 2% | -58% | -83% | -84% |
| WTI | 2331 | 8 | 4% | 2% | -58% | -91% | -92% |
| SILVER | 2287 | 9 | 5% | 2% | -53% | -83% | -84% |
| PLATINUM | 2076 | 5 | 3% | 1% | -78% | -95% | -95% |
| EURUSD | 2036 | 7 | 3% | 1% | -68% | -91% | -90% |
| COPPER | 1968 | 6 | 2% | 1% | -72% | -78% | -78% |
| GBPUSD | 1968 | 8 | 2% | 1% | -62% | -96% | -96% |
| USDJPY | 1934 | 6 | 2% | 1% | -71% | -96% | -96% |
| NATGAS | 1927 | 10 | 2% | 1% | -52% | -77% | -77% |
| PALLADIUM | 1868 | 4 | 1% | 1% | -80% | -93% | -93% |
| AUDUSD | 1488 | 7 | 2% | 1% | -56% | -90% | -90% |
| USDCAD | 1403 | 1 | 3% | 1% | -93% | -96% | -96% |
| BRENT | 1031 | 1 | 2% | 1% | -91% | -96% | -97% |
| 10YRRATE | 534 | 2 | 3% | 1% | -65% | -77% | -75% |
| 2YRRATE | 501 | 4 | 4% | 2% | -25% | -56% | -55% |
| 30YRRATE | 494 | 0 | 3% | 1% | -100% | -95% | -93% |
| 5YRRATE | 486 | 2 | 4% | 2% | -62% | -94% | -95% |
| INX | 124 | 1 | 2% | 1% | -25% | -97% | -98% |
| USDMXN | 16 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 34137 | 131 | 4% | 2% | -56% | -88% | -88% |
| DOWN (bought NO) | 32574 | 124 | 4% | 2% | -56% | -87% | -87% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 5815 | 25 | 2% | 1% | -21% | -79% | -78% |
| 0.05–0.1% | 6353 | 26 | 3% | 2% | -35% | -91% | -90% |
| 0.1–0.2% | 9924 | 36 | 5% | 2% | -52% | -89% | -89% |
| 0.2–0.5% | 12560 | 56 | 7% | 3% | -49% | -86% | -86% |
| Over 0.5% | 5232 | 23 | 7% | 3% | -54% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 16271 | 50 | 4% | 2% | -65% | -88% | -88% |
| Morning (6am–12pm) | 15699 | 81 | 4% | 2% | -41% | -85% | -85% |
| Afternoon (12–6pm) | 16524 | 73 | 4% | 2% | -48% | -87% | -87% |
| Evening (6pm–12am) | 18217 | 51 | 4% | 2% | -68% | -89% | -89% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 5,117 |
| Time from buy to best bounce (bounced bets) | 50 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/24 2:14:54 PM | NATGAS | UP | 6 sec | — | 0¢ | In play | — |
| 11/24 2:14:54 PM | USDMXN | DOWN | 6 sec | — | 0¢ | In play | — |
| 11/24 2:14:54 PM | XRP | DOWN | 6 sec | -0.011% | 0¢ | ❌ Lost | $0.00 |
| 11/24 2:14:54 PM | WTI | DOWN | 6 sec | — | 0¢ | In play | — |
| 11/24 2:14:36 PM | ETH | UP | 23 sec | -0.100% | 0¢ | ❌ Lost | $0.00 |
| 11/24 2:14:36 PM | BRENT | DOWN | 23 sec | — | 0¢ | In play | — |
| 11/24 2:14:36 PM | BTC | UP | 23 sec | -0.076% | 0¢ | ❌ Lost | $0.00 |
| 11/24 2:14:36 PM | 5YRRATE | DOWN | 23 sec | — | 0¢ | In play | — |
| 11/24 2:14:36 PM | AUDUSD | UP | 23 sec | — | 0¢ | In play | — |
| 11/24 2:14:20 PM | NEAR | UP | 39 sec | -0.137% | 0¢ | ❌ Lost | $0.00 |
| 11/24 2:14:04 PM | BNB | UP | 55 sec | -0.118% | 1¢ | In play | — |
| 11/24 2:14:04 PM | GOLD | UP | 55 sec | — | 0¢ | In play | — |
| 11/24 2:13:47 PM | HYPE | DOWN | 72 sec | +0.190% | 1¢ | ❌ Lost | -$0.15 |
| 11/24 2:13:47 PM | SILVER | UP | 72 sec | — | 0¢ | In play | — |
| 11/24 2:13:47 PM | SOL | UP | 72 sec | -0.158% | 0¢ | ❌ Lost | $0.00 |
| 11/24 2:13:47 PM | DOGE | UP | 72 sec | -0.165% | 0¢ | ❌ Lost | -$0.15 |
| 11/24 2:13:47 PM | USDCAD | DOWN | 72 sec | — | 0¢ | In play | — |
| 11/24 2:13:47 PM | 10YRRATE | DOWN | 72 sec | — | 0¢ | In play | — |
| 11/24 2:13:14 PM | PALLADIUM | DOWN | 1.8 min | — | 0¢ | In play | — |
| 11/24 2:12:58 PM | ZEC | UP | 2.0 min | -0.328% | 1¢ | ❌ Lost | -$0.15 |
| 11/24 2:06:33 PM | 30YRRATE | DOWN | 8.4 min | — | 0¢ | In play | — |
| 11/24 1:59:29 PM | USDMXN | UP | 31 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/24 1:59:29 PM | 30YRRATE | DOWN | 31 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/24 1:59:13 PM | NATGAS | DOWN | 47 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/24 1:58:58 PM | COPPER | DOWN | 61 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/24 1:58:58 PM | GOLD | DOWN | 61 sec | — | 2¢ | ❌ Lost | -$0.15 |
| 11/24 1:58:58 PM | SILVER | DOWN | 61 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 11/24 1:58:58 PM | WTI | DOWN | 61 sec | — | 0¢ | ❌ Lost | $0.00 |
| 11/24 1:58:58 PM | AUDUSD | DOWN | 61 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/24 1:58:38 PM | BRENT | DOWN | 82 sec | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
