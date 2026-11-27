# 15-Minute 1¢ Study

*Updated Fri Nov 27, 10:28 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 5005 finished bets | 1% | $199.30 | +37% | +3.98¢ | $94.80 / $104.50 |

*Expect about **83 buys a day** (~$12.42/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 4748 | $99.05 | +20% |
| Volatility model ≥ 2%, hold to the close | 9340 | $24.60 | +2% |
| Momentum model ≥ 2%, hold to the close | 7773 | -$53.00 | -6% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 69362 | 69317 | 257 (0%) | 1.07% | -$4,793.30 (-57%) | Hold to the close: -$4,793.30 (-57%) |

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
| Volatility model | 40902 | 4.5% | 0.4% (165) | -661% | ❌ Worse |
| Momentum model | 40902 | 4.5% | 0.4% (165) | -684% | ❌ Worse |
| Mean-reversion model | 40902 | 7.9% | 0.4% (165) | -802% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 40902 | 165 | -47% | -87% | -87% | -85% |
| Volatility model ≥ 2% | 9340 | 81 | +2% | -77% | -76% | -73% |
| Volatility model ≥ 5% | 5005 | 53 | +37% | -73% | -72% | -68% |
| Volatility model ≥ 10% | 2906 | 32 | +64% | -65% | -64% | -60% |
| Momentum model ≥ 2% | 7773 | 59 | -6% | -79% | -79% | -76% |
| Momentum model ≥ 5% | 4748 | 43 | +20% | -76% | -75% | -71% |
| Momentum model ≥ 10% | 3096 | 28 | +32% | -68% | -68% | -64% |
| Mean-reversion model ≥ 2% | 16691 | 113 | -25% | -82% | -82% | -80% |
| Mean-reversion model ≥ 5% | 11624 | 93 | -11% | -80% | -79% | -77% |
| Mean-reversion model ≥ 10% | 7712 | 66 | -2% | -78% | -78% | -75% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 41108 | 5% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 16583 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 11626 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 69317 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 257 | 0% | -$4,793.30 | -57% | — |
| Sell at 2¢ | 2839 | 4% | -$7,345.16 | -88% | 47 sec |
| Sell at 3¢ | 1906 | 3% | -$7,339.96 | -87% | 48 sec |
| Sell at 5¢ | 1288 | 2% | -$7,218.10 | -86% | 62 sec |
| Sell at 10¢ | 787 | 1% | -$6,940.33 | -83% | 65 sec |
| Sell at 25¢ | 425 | 1% | -$6,410.55 | -76% | 80 sec |
| Sell at 50¢ | 271 | 0% | -$5,806.05 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 13 | 0 | 31% | 23% | -100% | -47% | -20% |
| 5–10 min | 3603 | 17 | 10% | 4% | -55% | -82% | -83% |
| 2–5 min | 22471 | 116 | 7% | 3% | -49% | -86% | -86% |
| 1–2 min | 17238 | 58 | 3% | 2% | -62% | -92% | -92% |
| Under 1 min | 25992 | 66 | 1% | 0% | -63% | -87% | -86% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 4599 | 20 | 5% | 2% | -42% | -88% | -87% |
| HYPE | 4588 | 16 | 5% | 2% | -55% | -89% | -88% |
| SOL | 4582 | 20 | 4% | 2% | -43% | -86% | -86% |
| BNB | 4576 | 22 | 5% | 2% | -39% | -86% | -85% |
| DOGE | 4574 | 12 | 4% | 2% | -66% | -89% | -89% |
| ETH | 4568 | 19 | 7% | 3% | -48% | -82% | -82% |
| BTC | 4546 | 24 | 5% | 2% | -27% | -86% | -88% |
| NEAR | 4541 | 18 | 5% | 2% | -48% | -85% | -86% |
| XRP | 4534 | 16 | 4% | 2% | -55% | -88% | -88% |
| GOLD | 2449 | 8 | 5% | 2% | -60% | -83% | -84% |
| WTI | 2432 | 9 | 4% | 2% | -55% | -86% | -87% |
| SILVER | 2398 | 9 | 5% | 2% | -55% | -83% | -84% |
| PLATINUM | 2167 | 5 | 3% | 1% | -78% | -95% | -95% |
| EURUSD | 2122 | 7 | 2% | 1% | -69% | -91% | -91% |
| GBPUSD | 2070 | 8 | 2% | 1% | -64% | -96% | -95% |
| COPPER | 2054 | 6 | 2% | 1% | -73% | -79% | -79% |
| USDJPY | 2020 | 6 | 2% | 1% | -72% | -97% | -96% |
| NATGAS | 2009 | 10 | 2% | 1% | -54% | -77% | -77% |
| PALLADIUM | 1956 | 4 | 1% | 1% | -81% | -93% | -93% |
| AUDUSD | 1595 | 7 | 2% | 1% | -59% | -90% | -90% |
| USDCAD | 1500 | 1 | 3% | 1% | -94% | -95% | -95% |
| BRENT | 1118 | 1 | 2% | 1% | -92% | -96% | -97% |
| 10YRRATE | 561 | 2 | 3% | 1% | -67% | -78% | -76% |
| 30YRRATE | 522 | 0 | 3% | 1% | -100% | -95% | -94% |
| 2YRRATE | 519 | 4 | 4% | 2% | -28% | -57% | -57% |
| 5YRRATE | 511 | 2 | 4% | 2% | -63% | -94% | -95% |
| INX | 141 | 1 | 2% | 1% | -34% | -96% | -96% |
| USDMXN | 65 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 35281 | 133 | 4% | 2% | -56% | -88% | -88% |
| DOWN (bought NO) | 34036 | 124 | 4% | 2% | -58% | -87% | -87% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 5956 | 25 | 2% | 1% | -22% | -79% | -78% |
| 0.05–0.1% | 6521 | 26 | 3% | 2% | -36% | -91% | -91% |
| 0.1–0.2% | 10184 | 36 | 5% | 2% | -53% | -89% | -89% |
| 0.2–0.5% | 12963 | 56 | 7% | 3% | -51% | -86% | -86% |
| Over 0.5% | 5475 | 24 | 7% | 3% | -54% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 16692 | 51 | 4% | 2% | -65% | -88% | -88% |
| Morning (6am–12pm) | 16414 | 82 | 4% | 2% | -43% | -86% | -85% |
| Afternoon (12–6pm) | 16940 | 73 | 4% | 2% | -49% | -87% | -87% |
| Evening (6pm–12am) | 19271 | 51 | 4% | 2% | -69% | -90% | -89% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 5,070 |
| Time from buy to best bounce (bounced bets) | 51 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/27 10:28:37 AM | SILVER | DOWN | 83 sec | — | — | In play | — |
| 11/27 10:28:37 AM | GOLD | DOWN | 83 sec | — | — | In play | — |
| 11/27 10:28:22 AM | BRENT | UP | 1.6 min | — | — | In play | — |
| 11/27 10:27:32 AM | WTI | UP | 2.5 min | — | — | In play | — |
| 11/27 10:27:32 AM | 10YRRATE | DOWN | 2.5 min | — | — | In play | — |
| 11/27 10:26:56 AM | ETH | UP | 3.1 min | -0.359% | — | In play | — |
| 11/27 10:26:09 AM | BNB | UP | 3.9 min | -0.552% | — | In play | — |
| 11/27 10:26:09 AM | BTC | UP | 3.9 min | -0.649% | — | In play | — |
| 11/27 10:26:09 AM | HYPE | UP | 3.9 min | -0.676% | — | In play | — |
| 11/27 10:14:48 AM | GBPUSD | DOWN | 11 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/27 10:14:48 AM | WTI | DOWN | 11 sec | — | 0¢ | ❌ Lost | $0.00 |
| 11/27 10:14:48 AM | 30YRRATE | DOWN | 11 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/27 10:14:48 AM | XRP | DOWN | 11 sec | +0.011% | 0¢ | ❌ Lost | $0.00 |
| 11/27 10:14:48 AM | SILVER | UP | 11 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 11/27 10:14:48 AM | BTC | DOWN | 11 sec | +0.008% | 1¢ | ❌ Lost | -$0.15 |
| 11/27 10:14:48 AM | INX | UP | 11 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/27 10:14:32 AM | BNB | DOWN | 28 sec | +0.024% | 0¢ | ❌ Lost | $0.00 |
| 11/27 10:14:32 AM | SOL | UP | 28 sec | -0.101% | 0¢ | ❌ Lost | $0.00 |
| 11/27 10:14:32 AM | COPPER | DOWN | 28 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/27 10:14:12 AM | NEAR | DOWN | 48 sec | +0.126% | 0¢ | ❌ Lost | $0.00 |
| 11/27 10:14:12 AM | ETH | DOWN | 48 sec | +0.099% | 0¢ | ❌ Lost | $0.00 |
| 11/27 10:13:25 AM | DOGE | DOWN | 1.6 min | +0.269% | 0¢ | ❌ Lost | $0.00 |
| 11/27 10:13:25 AM | BRENT | DOWN | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/27 10:12:35 AM | ZEC | UP | 2.4 min | -0.647% | 1¢ | ❌ Lost | -$0.15 |
| 11/27 10:12:01 AM | HYPE | UP | 3.0 min | -0.487% | 1¢ | ❌ Lost | -$0.15 |
| 11/27 9:59:47 AM | NATGAS | UP | 12 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/27 9:59:47 AM | 5YRRATE | UP | 12 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/27 9:59:33 AM | NEAR | UP | 26 sec | -0.271% | 0¢ | ❌ Lost | $0.00 |
| 11/27 9:59:33 AM | XRP | UP | 26 sec | -0.147% | 0¢ | ❌ Lost | $0.00 |
| 11/27 9:59:17 AM | SOL | UP | 42 sec | -0.182% | 0¢ | ❌ Lost | $0.00 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
