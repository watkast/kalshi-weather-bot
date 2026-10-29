# 15-Minute 1¢ Study

*Updated Thu Oct 29, 2:29 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 3093 finished bets | 1% | $87.20 | +25% | +2.82¢ | $80.70 / $6.50 |

*Expect about **98 buys a day** (~$14.70/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 2868 | $36.05 | +11% |
| Volatility model ≥ 2%, hold to the close | 5729 | $4.30 | +1% |
| Volatility model ≥ 5%, sell at 50¢ | 3093 | -$67.05 | -19% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 38250 | 38230 | 141 (0%) | 1.07% | -$2,694.00 (-58%) | Hold to the close: -$2,694.00 (-58%) |

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
| Volatility model | 23572 | 4.7% | 0.4% (93) | -678% | ❌ Worse |
| Momentum model | 23572 | 4.6% | 0.4% (93) | -702% | ❌ Worse |
| Mean-reversion model | 23572 | 8.0% | 0.4% (93) | -826% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 23572 | 93 | -50% | -88% | -87% | -85% |
| Volatility model ≥ 2% | 5729 | 50 | +1% | -79% | -77% | -74% |
| Volatility model ≥ 5% | 3093 | 31 | +25% | -76% | -74% | -71% |
| Volatility model ≥ 10% | 1751 | 19 | +54% | -68% | -66% | -63% |
| Momentum model ≥ 2% | 4736 | 34 | -13% | -81% | -80% | -77% |
| Momentum model ≥ 5% | 2868 | 25 | +11% | -78% | -78% | -74% |
| Momentum model ≥ 10% | 1875 | 17 | +26% | -72% | -72% | -68% |
| Mean-reversion model ≥ 2% | 9637 | 64 | -27% | -83% | -83% | -81% |
| Mean-reversion model ≥ 5% | 6757 | 54 | -12% | -81% | -80% | -77% |
| Mean-reversion model ≥ 10% | 4511 | 39 | -2% | -79% | -78% | -76% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 23773 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 9179 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 5278 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 38230 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 141 | 0% | -$2,694.00 | -58% | — |
| Sell at 2¢ | 1458 | 4% | -$4,092.92 | -88% | 47 sec |
| Sell at 3¢ | 1003 | 3% | -$4,080.83 | -87% | 48 sec |
| Sell at 5¢ | 699 | 2% | -$4,017.65 | -86% | 63 sec |
| Sell at 10¢ | 422 | 1% | -$3,863.18 | -83% | 65 sec |
| Sell at 25¢ | 225 | 1% | -$3,559.25 | -76% | 83 sec |
| Sell at 50¢ | 146 | 0% | -$3,234.50 | -69% | 1.9 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 9 | 0 | 33% | 22% | -100% | -42% | -13% |
| 5–10 min | 1765 | 8 | 11% | 4% | -57% | -80% | -81% |
| 2–5 min | 12174 | 68 | 7% | 3% | -45% | -87% | -86% |
| 1–2 min | 9682 | 32 | 3% | 1% | -64% | -92% | -92% |
| Under 1 min | 14600 | 33 | 1% | 0% | -68% | -86% | -86% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 2660 | 12 | 5% | 2% | -42% | -88% | -88% |
| HYPE | 2656 | 8 | 5% | 3% | -63% | -89% | -87% |
| BNB | 2654 | 15 | 4% | 2% | -29% | -85% | -84% |
| SOL | 2647 | 7 | 4% | 2% | -67% | -92% | -91% |
| DOGE | 2642 | 6 | 4% | 2% | -72% | -90% | -90% |
| ETH | 2641 | 11 | 6% | 3% | -49% | -85% | -85% |
| XRP | 2626 | 11 | 3% | 1% | -48% | -89% | -89% |
| BTC | 2624 | 13 | 5% | 2% | -34% | -88% | -89% |
| NEAR | 2623 | 12 | 5% | 2% | -40% | -82% | -82% |
| GOLD | 1443 | 5 | 4% | 2% | -58% | -82% | -84% |
| SILVER | 1412 | 6 | 4% | 2% | -50% | -82% | -81% |
| WTI | 1395 | 4 | 3% | 1% | -66% | -93% | -94% |
| PLATINUM | 1248 | 2 | 2% | 1% | -85% | -97% | -96% |
| COPPER | 1191 | 4 | 1% | 1% | -69% | -74% | -74% |
| EURUSD | 1186 | 3 | 2% | 1% | -76% | -88% | -88% |
| NATGAS | 1153 | 7 | 2% | 1% | -43% | -80% | -79% |
| GBPUSD | 1124 | 2 | 2% | 1% | -83% | -96% | -96% |
| PALLADIUM | 1115 | 2 | 1% | 0% | -83% | -90% | -90% |
| USDJPY | 1103 | 5 | 2% | 1% | -58% | -97% | -96% |
| AUDUSD | 658 | 4 | 1% | 1% | -43% | -83% | -82% |
| USDCAD | 622 | 0 | 2% | 0% | -100% | -97% | -97% |
| BRENT | 222 | 0 | 0% | 0% | -100% | -99% | -99% |
| 10YRRATE | 156 | 0 | 4% | 1% | -100% | -92% | -90% |
| 30YRRATE | 150 | 0 | 1% | 0% | -100% | -99% | -98% |
| 2YRRATE | 145 | 1 | 4% | 1% | -36% | -28% | -27% |
| 5YRRATE | 134 | 1 | 6% | 2% | -30% | -90% | -92% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 19394 | 77 | 4% | 2% | -54% | -88% | -87% |
| DOWN (bought NO) | 18836 | 64 | 4% | 2% | -61% | -88% | -88% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 3872 | 19 | 2% | 1% | -15% | -81% | -81% |
| 0.05–0.1% | 4083 | 14 | 3% | 2% | -49% | -92% | -92% |
| 0.1–0.2% | 6173 | 22 | 4% | 2% | -56% | -90% | -89% |
| 0.2–0.5% | 7022 | 30 | 6% | 3% | -53% | -87% | -86% |
| Over 0.5% | 2619 | 10 | 7% | 3% | -61% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 9458 | 35 | 4% | 2% | -58% | -86% | -86% |
| Morning (6am–12pm) | 9668 | 43 | 4% | 2% | -50% | -86% | -85% |
| Afternoon (12–6pm) | 8942 | 29 | 4% | 2% | -62% | -88% | -88% |
| Evening (6pm–12am) | 10162 | 34 | 3% | 2% | -62% | -91% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,494 |
| Time from buy to best bounce (bounced bets) | 51 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/29 2:29:10 PM | ETH | DOWN | 50 sec | +0.047% | — | In play | — |
| 10/29 2:29:10 PM | NEAR | DOWN | 50 sec | +0.283% | — | In play | — |
| 10/29 2:29:10 PM | AUDUSD | DOWN | 50 sec | — | — | In play | — |
| 10/29 2:28:55 PM | ZEC | UP | 64 sec | -0.345% | — | In play | — |
| 10/29 2:28:40 PM | BNB | UP | 79 sec | -0.326% | — | In play | — |
| 10/29 2:28:24 PM | NATGAS | UP | 1.6 min | — | — | In play | — |
| 10/29 2:28:24 PM | SOL | DOWN | 1.6 min | +0.262% | — | In play | — |
| 10/29 2:28:24 PM | EURUSD | DOWN | 1.6 min | — | — | In play | — |
| 10/29 2:28:08 PM | COPPER | DOWN | 1.9 min | — | — | In play | — |
| 10/29 2:27:52 PM | HYPE | UP | 2.1 min | -0.662% | — | In play | — |
| 10/29 2:14:17 PM | BRENT | DOWN | 42 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/29 2:14:01 PM | SILVER | UP | 58 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/29 2:13:46 PM | HYPE | UP | 74 sec | -0.426% | 1¢ | ❌ Lost | -$0.15 |
| 10/29 2:13:30 PM | NATGAS | UP | 1.5 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/29 2:10:03 PM | BTC | UP | 5.0 min | -0.646% | 1¢ | ❌ Lost | -$0.15 |
| 10/29 2:10:03 PM | XRP | UP | 5.0 min | -1.038% | 1¢ | ❌ Lost | -$0.15 |
| 10/29 2:10:03 PM | DOGE | UP | 5.0 min | -1.351% | 1¢ | ❌ Lost | -$0.15 |
| 10/29 2:09:31 PM | COPPER | UP | 5.5 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/29 2:09:15 PM | GOLD | DOWN | 5.8 min | — | 2¢ | ❌ Lost | -$0.15 |
| 10/29 2:08:37 PM | USDCAD | UP | 6.4 min | — | 2¢ | ❌ Lost | -$0.15 |
| 10/29 2:07:33 PM | 30YRRATE | UP | 7.5 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/29 2:07:17 PM | NEAR | UP | 7.7 min | -1.927% | 3¢ | ❌ Lost | -$0.15 |
| 10/29 2:07:17 PM | AUDUSD | UP | 7.7 min | — | 5¢ | ❌ Lost | -$0.15 |
| 10/29 2:07:01 PM | SOL | UP | 8.0 min | -1.413% | 1¢ | ❌ Lost | -$0.15 |
| 10/29 2:07:01 PM | EURUSD | DOWN | 8.0 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/29 2:06:29 PM | 10YRRATE | UP | 8.5 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/29 2:06:29 PM | GBPUSD | DOWN | 8.5 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/29 2:05:56 PM | ETH | UP | 9.1 min | -1.134% | 2¢ | ❌ Lost | -$0.15 |
| 10/29 2:05:25 PM | 5YRRATE | UP | 9.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/29 2:05:25 PM | ZEC | UP | 9.6 min | -2.043% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
