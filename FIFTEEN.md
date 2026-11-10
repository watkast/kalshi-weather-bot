# 15-Minute 1¢ Study

*Updated Mon Nov 9, 9:27 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 4130 finished bets | 1% | $184.85 | +40% | +4.48¢ | $90.40 / $94.45 |

*Expect about **96 buys a day** (~$14.44/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 3837 | $102.65 | +25% |
| Volatility model ≥ 2%, hold to the close | 7555 | $70.70 | +8% |
| Momentum model ≥ 2%, hold to the close | 6252 | -$3.90 | -1% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 51559 | 51531 | 199 (0%) | 1.07% | -$3,487.45 (-56%) | Hold to the close: -$3,487.45 (-56%) |

*In play or awaiting result: 20. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 31333 | 4.8% | 0.4% (128) | -676% | ❌ Worse |
| Momentum model | 31333 | 4.6% | 0.4% (128) | -701% | ❌ Worse |
| Mean-reversion model | 31333 | 8.1% | 0.4% (128) | -818% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 31333 | 128 | -48% | -87% | -87% | -84% |
| Volatility model ≥ 2% | 7555 | 70 | +8% | -77% | -75% | -71% |
| Volatility model ≥ 5% | 4130 | 46 | +40% | -71% | -70% | -66% |
| Volatility model ≥ 10% | 2379 | 28 | +68% | -61% | -60% | -56% |
| Momentum model ≥ 2% | 6252 | 51 | -1% | -78% | -77% | -74% |
| Momentum model ≥ 5% | 3837 | 37 | +25% | -73% | -73% | -69% |
| Momentum model ≥ 10% | 2520 | 25 | +40% | -65% | -64% | -60% |
| Mean-reversion model ≥ 2% | 12954 | 91 | -23% | -82% | -82% | -79% |
| Mean-reversion model ≥ 5% | 9087 | 78 | -5% | -79% | -79% | -76% |
| Mean-reversion model ≥ 10% | 6072 | 56 | +5% | -77% | -76% | -74% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 31538 | 5% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 12197 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 7796 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 51531 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 199 | 0% | -$3,487.45 | -56% | — |
| Sell at 2¢ | 2052 | 4% | -$5,459.93 | -87% | 47 sec |
| Sell at 3¢ | 1397 | 3% | -$5,448.62 | -87% | 48 sec |
| Sell at 5¢ | 978 | 2% | -$5,329.75 | -85% | 63 sec |
| Sell at 10¢ | 593 | 1% | -$5,104.62 | -81% | 65 sec |
| Sell at 25¢ | 313 | 1% | -$4,733.42 | -75% | 83 sec |
| Sell at 50¢ | 205 | 0% | -$4,287.70 | -68% | 1.7 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 12 | 0 | 25% | 17% | -100% | -57% | -35% |
| 5–10 min | 2557 | 12 | 11% | 4% | -55% | -81% | -82% |
| 2–5 min | 16629 | 93 | 7% | 3% | -45% | -87% | -86% |
| 1–2 min | 13034 | 44 | 3% | 2% | -62% | -92% | -92% |
| Under 1 min | 19299 | 50 | 1% | 0% | -63% | -84% | -84% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 3532 | 15 | 5% | 2% | -45% | -88% | -88% |
| SOL | 3528 | 16 | 4% | 2% | -42% | -87% | -87% |
| HYPE | 3519 | 11 | 5% | 2% | -61% | -89% | -88% |
| BNB | 3512 | 19 | 5% | 2% | -32% | -86% | -84% |
| DOGE | 3508 | 8 | 4% | 2% | -71% | -90% | -89% |
| ETH | 3503 | 15 | 7% | 3% | -47% | -81% | -81% |
| BTC | 3483 | 17 | 5% | 2% | -33% | -87% | -88% |
| NEAR | 3482 | 16 | 5% | 2% | -41% | -85% | -85% |
| XRP | 3471 | 13 | 3% | 1% | -53% | -89% | -89% |
| GOLD | 1854 | 5 | 6% | 2% | -67% | -81% | -83% |
| WTI | 1825 | 6 | 4% | 2% | -60% | -91% | -92% |
| SILVER | 1802 | 8 | 5% | 2% | -48% | -82% | -82% |
| PLATINUM | 1633 | 4 | 2% | 1% | -77% | -96% | -95% |
| EURUSD | 1566 | 5 | 2% | 1% | -70% | -90% | -89% |
| COPPER | 1530 | 6 | 2% | 1% | -63% | -73% | -72% |
| NATGAS | 1492 | 8 | 2% | 1% | -50% | -78% | -77% |
| GBPUSD | 1488 | 5 | 2% | 1% | -69% | -96% | -96% |
| PALLADIUM | 1468 | 3 | 1% | 0% | -81% | -92% | -92% |
| USDJPY | 1464 | 6 | 2% | 1% | -62% | -97% | -96% |
| AUDUSD | 1027 | 5 | 2% | 1% | -55% | -87% | -88% |
| USDCAD | 995 | 0 | 2% | 1% | -100% | -96% | -97% |
| BRENT | 593 | 0 | 2% | 1% | -100% | -97% | -97% |
| 10YRRATE | 331 | 2 | 5% | 2% | -44% | -64% | -62% |
| 2YRRATE | 314 | 4 | 4% | 2% | +19% | -33% | -31% |
| 30YRRATE | 309 | 0 | 2% | 1% | -100% | -96% | -94% |
| 5YRRATE | 291 | 2 | 4% | 2% | -36% | -92% | -95% |
| INX | 11 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 26131 | 104 | 4% | 2% | -54% | -88% | -87% |
| DOWN (bought NO) | 25400 | 95 | 4% | 2% | -57% | -86% | -86% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 5080 | 25 | 2% | 1% | -13% | -77% | -76% |
| 0.05–0.1% | 5393 | 20 | 3% | 2% | -43% | -91% | -91% |
| 0.1–0.2% | 8109 | 30 | 5% | 2% | -53% | -89% | -89% |
| 0.2–0.5% | 9418 | 40 | 6% | 3% | -53% | -87% | -86% |
| Over 0.5% | 3530 | 15 | 7% | 3% | -56% | -87% | -88% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 12671 | 43 | 4% | 2% | -61% | -87% | -87% |
| Morning (6am–12pm) | 12425 | 56 | 4% | 2% | -49% | -84% | -84% |
| Afternoon (12–6pm) | 12535 | 57 | 4% | 2% | -47% | -86% | -86% |
| Evening (6pm–12am) | 13900 | 43 | 4% | 2% | -64% | -90% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,914 |
| Time from buy to best bounce (bounced bets) | 50 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/9 9:27:17 PM | XRP | DOWN | 2.7 min | +0.321% | — | In play | — |
| 11/9 9:27:17 PM | USDJPY | DOWN | 2.7 min | — | — | In play | — |
| 11/9 9:27:01 PM | BTC | DOWN | 3.0 min | +0.171% | — | In play | — |
| 11/9 9:27:01 PM | BNB | DOWN | 3.0 min | +0.093% | — | In play | — |
| 11/9 9:26:15 PM | ZEC | DOWN | 3.8 min | +0.498% | — | In play | — |
| 11/9 9:26:15 PM | PLATINUM | DOWN | 3.8 min | — | — | In play | — |
| 11/9 9:26:15 PM | COPPER | DOWN | 3.8 min | — | — | In play | — |
| 11/9 9:25:27 PM | NEAR | DOWN | 4.5 min | +0.591% | — | In play | — |
| 11/9 9:25:11 PM | HYPE | DOWN | 4.8 min | +0.464% | — | In play | — |
| 11/9 9:24:55 PM | SILVER | DOWN | 5.1 min | — | — | In play | — |
| 11/9 9:24:23 PM | ETH | DOWN | 5.6 min | +0.331% | — | In play | — |
| 11/9 9:14:56 PM | NATGAS | DOWN | 3 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/9 9:14:40 PM | SILVER | DOWN | 20 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 11/9 9:14:40 PM | PALLADIUM | DOWN | 20 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/9 9:14:40 PM | HYPE | DOWN | 20 sec | +0.077% | 0¢ | ❌ Lost | $0.00 |
| 11/9 9:14:40 PM | NEAR | DOWN | 20 sec | +0.067% | 0¢ | ❌ Lost | $0.00 |
| 11/9 9:14:24 PM | BTC | DOWN | 35 sec | +0.084% | 0¢ | ❌ Lost | $0.00 |
| 11/9 9:14:24 PM | ETH | DOWN | 35 sec | +0.067% | 0¢ | ❌ Lost | -$0.15 |
| 11/9 9:14:08 PM | BNB | DOWN | 51 sec | -0.017% | 0¢ | ❌ Lost | -$0.15 |
| 11/9 9:13:52 PM | SOL | DOWN | 67 sec | +0.123% | 0¢ | ❌ Lost | -$0.15 |
| 11/9 9:13:20 PM | ZEC | UP | 1.6 min | -0.396% | 1¢ | ❌ Lost | -$0.15 |
| 11/9 9:13:20 PM | PLATINUM | UP | 1.6 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/9 9:13:04 PM | WTI | DOWN | 1.9 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/9 9:13:04 PM | BRENT | DOWN | 1.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/9 9:12:32 PM | XRP | UP | 2.5 min | -0.275% | 1¢ | ❌ Lost | -$0.15 |
| 11/9 7:13:15 PM | WTI | DOWN | 1.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/9 7:13:15 PM | ZEC | UP | 1.7 min | -0.508% | 0¢ | ❌ Lost | -$0.15 |
| 11/9 7:12:10 PM | HYPE | UP | 2.8 min | -0.359% | 1¢ | ❌ Lost | -$0.15 |
| 11/9 7:12:10 PM | GOLD | UP | 2.8 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/9 7:11:52 PM | BTC | UP | 3.1 min | -0.177% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
