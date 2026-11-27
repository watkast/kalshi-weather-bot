# 15-Minute 1¢ Study

*Updated Fri Nov 27, 12:55 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 5020 finished bets | 1% | $197.50 | +36% | +3.93¢ | $93.60 / $103.90 |

*Expect about **83 buys a day** (~$12.44/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 4758 | $98.00 | +19% |
| Volatility model ≥ 2%, hold to the close | 9372 | $20.85 | +2% |
| Momentum model ≥ 2%, hold to the close | 7796 | -$55.55 | -6% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 69550 | 69509 | 257 (0%) | 1.07% | -$4,816.85 (-57%) | Hold to the close: -$4,816.85 (-57%) |

*In play or awaiting result: 11. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 40989 | 4.5% | 0.4% (165) | -662% | ❌ Worse |
| Momentum model | 40989 | 4.5% | 0.4% (165) | -685% | ❌ Worse |
| Mean-reversion model | 40989 | 7.9% | 0.4% (165) | -803% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 40989 | 165 | -48% | -87% | -87% | -85% |
| Volatility model ≥ 2% | 9372 | 81 | +2% | -77% | -77% | -73% |
| Volatility model ≥ 5% | 5020 | 53 | +36% | -73% | -72% | -68% |
| Volatility model ≥ 10% | 2915 | 32 | +63% | -65% | -64% | -60% |
| Momentum model ≥ 2% | 7796 | 59 | -6% | -79% | -79% | -76% |
| Momentum model ≥ 5% | 4758 | 43 | +19% | -76% | -75% | -71% |
| Momentum model ≥ 10% | 3105 | 28 | +31% | -68% | -68% | -64% |
| Mean-reversion model ≥ 2% | 16741 | 113 | -25% | -82% | -82% | -80% |
| Mean-reversion model ≥ 5% | 11659 | 93 | -11% | -80% | -79% | -77% |
| Mean-reversion model ≥ 10% | 7734 | 66 | -2% | -78% | -78% | -75% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 41195 | 5% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 16637 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 11677 | 3% | 2% | 1% | 1% | 0% | 0% |
| **All** | 69509 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 257 | 0% | -$4,816.85 | -57% | — |
| Sell at 2¢ | 2848 | 4% | -$7,366.37 | -88% | 47 sec |
| Sell at 3¢ | 1913 | 3% | -$7,360.78 | -87% | 48 sec |
| Sell at 5¢ | 1294 | 2% | -$7,237.75 | -86% | 62 sec |
| Sell at 10¢ | 793 | 1% | -$6,956.02 | -83% | 65 sec |
| Sell at 25¢ | 427 | 1% | -$6,427.48 | -76% | 80 sec |
| Sell at 50¢ | 271 | 0% | -$5,829.60 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 13 | 0 | 31% | 23% | -100% | -47% | -20% |
| 5–10 min | 3608 | 17 | 10% | 4% | -55% | -82% | -83% |
| 2–5 min | 22544 | 116 | 7% | 3% | -49% | -86% | -86% |
| 1–2 min | 17284 | 58 | 3% | 2% | -62% | -92% | -92% |
| Under 1 min | 26060 | 66 | 1% | 0% | -63% | -87% | -86% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 4609 | 20 | 5% | 2% | -42% | -88% | -87% |
| HYPE | 4598 | 16 | 5% | 2% | -55% | -89% | -88% |
| SOL | 4592 | 20 | 4% | 2% | -43% | -86% | -86% |
| BNB | 4586 | 22 | 5% | 2% | -39% | -86% | -85% |
| DOGE | 4583 | 12 | 4% | 2% | -66% | -89% | -89% |
| ETH | 4577 | 19 | 7% | 3% | -48% | -82% | -82% |
| BTC | 4556 | 24 | 5% | 2% | -27% | -86% | -88% |
| NEAR | 4551 | 18 | 5% | 2% | -48% | -85% | -86% |
| XRP | 4543 | 16 | 4% | 2% | -55% | -89% | -88% |
| GOLD | 2456 | 8 | 5% | 2% | -60% | -83% | -84% |
| WTI | 2439 | 9 | 4% | 2% | -55% | -86% | -87% |
| SILVER | 2406 | 9 | 5% | 2% | -55% | -83% | -84% |
| PLATINUM | 2173 | 5 | 3% | 1% | -79% | -95% | -95% |
| EURUSD | 2130 | 7 | 2% | 1% | -69% | -91% | -90% |
| GBPUSD | 2077 | 8 | 2% | 1% | -64% | -96% | -95% |
| COPPER | 2061 | 6 | 2% | 1% | -73% | -79% | -79% |
| USDJPY | 2026 | 6 | 2% | 1% | -72% | -97% | -96% |
| NATGAS | 2015 | 10 | 2% | 1% | -54% | -77% | -77% |
| PALLADIUM | 1963 | 4 | 1% | 1% | -81% | -93% | -93% |
| AUDUSD | 1603 | 7 | 2% | 1% | -59% | -90% | -90% |
| USDCAD | 1503 | 1 | 3% | 1% | -94% | -96% | -96% |
| BRENT | 1124 | 1 | 2% | 1% | -92% | -96% | -96% |
| 10YRRATE | 564 | 2 | 3% | 1% | -67% | -78% | -76% |
| 30YRRATE | 526 | 0 | 3% | 1% | -100% | -95% | -93% |
| 2YRRATE | 523 | 4 | 4% | 2% | -29% | -58% | -57% |
| 5YRRATE | 514 | 2 | 4% | 2% | -64% | -94% | -95% |
| INX | 142 | 1 | 2% | 1% | -34% | -96% | -96% |
| USDMXN | 69 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 35356 | 133 | 4% | 2% | -56% | -88% | -88% |
| DOWN (bought NO) | 34153 | 124 | 4% | 2% | -58% | -87% | -87% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 5964 | 25 | 2% | 1% | -22% | -79% | -78% |
| 0.05–0.1% | 6532 | 26 | 3% | 2% | -36% | -91% | -91% |
| 0.1–0.2% | 10206 | 36 | 5% | 2% | -53% | -89% | -89% |
| 0.2–0.5% | 12991 | 56 | 7% | 3% | -51% | -86% | -86% |
| Over 0.5% | 5493 | 24 | 7% | 3% | -54% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 16692 | 51 | 4% | 2% | -65% | -88% | -88% |
| Morning (6am–12pm) | 16558 | 82 | 4% | 2% | -43% | -86% | -85% |
| Afternoon (12–6pm) | 16988 | 73 | 4% | 2% | -49% | -87% | -87% |
| Evening (6pm–12am) | 19271 | 51 | 4% | 2% | -69% | -90% | -89% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 5,066 |
| Time from buy to best bounce (bounced bets) | 51 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/27 12:55:12 PM | BTC | UP | 4.8 min | -0.265% | — | In play | — |
| 11/27 12:55:12 PM | ETH | UP | 4.8 min | -0.253% | — | In play | — |
| 11/27 12:54:38 PM | DOGE | UP | 5.3 min | -0.340% | — | In play | — |
| 11/27 12:53:16 PM | XRP | UP | 6.7 min | -0.305% | — | In play | — |
| 11/27 12:51:34 PM | SOL | UP | 8.4 min | -0.504% | — | In play | — |
| 11/27 12:44:46 PM | USDJPY | UP | 14 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/27 12:44:28 PM | PALLADIUM | DOWN | 31 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/27 12:44:28 PM | AUDUSD | DOWN | 31 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/27 12:44:12 PM | DOGE | DOWN | 47 sec | +0.048% | 1¢ | ❌ Lost | -$0.15 |
| 11/27 12:44:12 PM | NATGAS | UP | 47 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/27 12:44:12 PM | ZEC | UP | 47 sec | -0.182% | 1¢ | ❌ Lost | -$0.15 |
| 11/27 12:43:56 PM | HYPE | UP | 63 sec | -0.121% | 0¢ | ❌ Lost | $0.00 |
| 11/27 12:43:40 PM | WTI | DOWN | 80 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/27 12:43:20 PM | ETH | DOWN | 1.7 min | +0.087% | 2¢ | ❌ Lost | -$0.15 |
| 11/27 12:43:04 PM | COPPER | DOWN | 1.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/27 12:42:48 PM | BTC | DOWN | 2.2 min | +0.106% | 1¢ | ❌ Lost | -$0.15 |
| 11/27 12:42:33 PM | NEAR | DOWN | 2.4 min | +0.121% | 11¢ | ❌ Lost | -$0.15 |
| 11/27 12:42:14 PM | EURUSD | DOWN | 2.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/27 12:42:14 PM | BNB | DOWN | 2.8 min | +0.061% | 1¢ | ❌ Lost | -$0.15 |
| 11/27 12:42:14 PM | GOLD | DOWN | 2.8 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/27 12:42:14 PM | SOL | DOWN | 2.8 min | +0.188% | 1¢ | ❌ Lost | -$0.15 |
| 11/27 12:41:27 PM | SILVER | DOWN | 3.5 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/27 12:41:27 PM | PLATINUM | DOWN | 3.5 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/27 12:41:07 PM | BRENT | UP | 3.9 min | — | 13¢ | ❌ Lost | -$0.15 |
| 11/27 12:41:07 PM | GBPUSD | DOWN | 3.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/27 12:29:53 PM | SILVER | DOWN | 6 sec | — | 0¢ | ❌ Lost | $0.00 |
| 11/27 12:29:35 PM | DOGE | DOWN | 24 sec | -0.029% | 0¢ | ❌ Lost | $0.00 |
| 11/27 12:29:35 PM | EURUSD | DOWN | 24 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/27 12:29:35 PM | ZEC | DOWN | 24 sec | +0.049% | 0¢ | ❌ Lost | $0.00 |
| 11/27 12:28:47 PM | BRENT | DOWN | 73 sec | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
