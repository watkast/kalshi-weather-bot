# 15-Minute 1¢ Study

*Updated Tue Nov 10, 1:25 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 4150 finished bets | 1% | $183.05 | +40% | +4.41¢ | $89.20 / $93.85 |

*Expect about **96 buys a day** (~$14.45/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 3857 | $100.85 | +24% |
| Volatility model ≥ 2%, hold to the close | 7585 | $67.40 | +7% |
| Momentum model ≥ 2%, hold to the close | 6279 | -$6.75 | -1% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 51867 | 51845 | 199 (0%) | 1.07% | -$3,528.85 (-56%) | Hold to the close: -$3,528.85 (-56%) |

*In play or awaiting result: 14. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 31473 | 4.8% | 0.4% (128) | -678% | ❌ Worse |
| Momentum model | 31473 | 4.6% | 0.4% (128) | -703% | ❌ Worse |
| Mean-reversion model | 31473 | 8.1% | 0.4% (128) | -820% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 31473 | 128 | -48% | -87% | -87% | -84% |
| Volatility model ≥ 2% | 7585 | 70 | +7% | -77% | -76% | -71% |
| Volatility model ≥ 5% | 4150 | 46 | +40% | -71% | -70% | -66% |
| Volatility model ≥ 10% | 2393 | 28 | +68% | -62% | -60% | -56% |
| Momentum model ≥ 2% | 6279 | 51 | -1% | -78% | -77% | -74% |
| Momentum model ≥ 5% | 3857 | 37 | +24% | -73% | -73% | -69% |
| Momentum model ≥ 10% | 2531 | 25 | +39% | -65% | -64% | -60% |
| Mean-reversion model ≥ 2% | 13028 | 91 | -23% | -82% | -82% | -79% |
| Mean-reversion model ≥ 5% | 9136 | 78 | -5% | -79% | -79% | -76% |
| Mean-reversion model ≥ 10% | 6108 | 56 | +4% | -77% | -76% | -74% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 31678 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 12298 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 7869 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 51845 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 199 | 0% | -$3,528.85 | -56% | — |
| Sell at 2¢ | 2067 | 4% | -$5,497.43 | -87% | 47 sec |
| Sell at 3¢ | 1407 | 3% | -$5,486.12 | -87% | 48 sec |
| Sell at 5¢ | 982 | 2% | -$5,368.55 | -85% | 63 sec |
| Sell at 10¢ | 595 | 1% | -$5,143.40 | -81% | 65 sec |
| Sell at 25¢ | 314 | 1% | -$4,771.51 | -76% | 83 sec |
| Sell at 50¢ | 205 | 0% | -$4,329.10 | -69% | 1.7 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 12 | 0 | 25% | 17% | -100% | -57% | -35% |
| 5–10 min | 2575 | 12 | 11% | 4% | -56% | -81% | -82% |
| 2–5 min | 16755 | 93 | 7% | 3% | -45% | -87% | -86% |
| 1–2 min | 13098 | 44 | 3% | 2% | -63% | -92% | -92% |
| Under 1 min | 19405 | 50 | 1% | 0% | -63% | -85% | -84% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 3548 | 15 | 5% | 2% | -45% | -88% | -88% |
| SOL | 3543 | 16 | 4% | 2% | -42% | -87% | -87% |
| HYPE | 3535 | 11 | 5% | 2% | -61% | -89% | -88% |
| BNB | 3528 | 19 | 5% | 2% | -32% | -86% | -85% |
| DOGE | 3523 | 8 | 4% | 2% | -71% | -90% | -89% |
| ETH | 3519 | 15 | 7% | 3% | -47% | -81% | -81% |
| NEAR | 3498 | 16 | 5% | 2% | -41% | -85% | -85% |
| BTC | 3498 | 17 | 5% | 2% | -33% | -87% | -88% |
| XRP | 3486 | 13 | 3% | 1% | -53% | -89% | -88% |
| GOLD | 1864 | 5 | 6% | 2% | -67% | -81% | -83% |
| WTI | 1838 | 6 | 4% | 2% | -61% | -91% | -92% |
| SILVER | 1816 | 8 | 5% | 2% | -48% | -83% | -82% |
| PLATINUM | 1646 | 4 | 2% | 1% | -77% | -96% | -95% |
| EURUSD | 1580 | 5 | 2% | 1% | -70% | -90% | -89% |
| COPPER | 1543 | 6 | 2% | 1% | -64% | -73% | -72% |
| NATGAS | 1505 | 8 | 2% | 1% | -50% | -78% | -77% |
| GBPUSD | 1500 | 5 | 2% | 1% | -69% | -96% | -96% |
| PALLADIUM | 1482 | 3 | 1% | 0% | -81% | -92% | -92% |
| USDJPY | 1479 | 6 | 2% | 1% | -62% | -96% | -96% |
| AUDUSD | 1040 | 5 | 2% | 1% | -55% | -87% | -88% |
| USDCAD | 1009 | 0 | 2% | 1% | -100% | -96% | -97% |
| BRENT | 604 | 0 | 2% | 1% | -100% | -97% | -97% |
| 10YRRATE | 333 | 2 | 5% | 2% | -44% | -64% | -62% |
| 2YRRATE | 315 | 4 | 4% | 2% | +19% | -33% | -32% |
| 30YRRATE | 310 | 0 | 2% | 1% | -100% | -96% | -94% |
| 5YRRATE | 292 | 2 | 4% | 2% | -36% | -92% | -95% |
| INX | 11 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 26278 | 104 | 4% | 2% | -54% | -88% | -87% |
| DOWN (bought NO) | 25567 | 95 | 4% | 2% | -57% | -86% | -86% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 5101 | 25 | 2% | 1% | -13% | -77% | -76% |
| 0.05–0.1% | 5416 | 20 | 3% | 2% | -44% | -91% | -91% |
| 0.1–0.2% | 8145 | 30 | 5% | 2% | -53% | -89% | -89% |
| 0.2–0.5% | 9465 | 40 | 6% | 3% | -53% | -87% | -86% |
| Over 0.5% | 3543 | 15 | 7% | 3% | -56% | -87% | -88% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 12768 | 43 | 4% | 2% | -62% | -87% | -88% |
| Morning (6am–12pm) | 12425 | 56 | 4% | 2% | -49% | -84% | -84% |
| Afternoon (12–6pm) | 12535 | 57 | 4% | 2% | -47% | -86% | -86% |
| Evening (6pm–12am) | 14117 | 43 | 4% | 2% | -65% | -90% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,906 |
| Time from buy to best bounce (bounced bets) | 50 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/10 1:25:00 AM | NEAR | UP | 5.0 min | -0.777% | — | In play | — |
| 11/10 1:24:44 AM | SOL | UP | 5.2 min | -0.393% | — | In play | — |
| 11/10 1:24:11 AM | HYPE | UP | 5.8 min | -0.592% | — | In play | — |
| 11/10 1:24:11 AM | DOGE | UP | 5.8 min | -0.434% | — | In play | — |
| 11/10 1:23:55 AM | ZEC | UP | 6.1 min | -1.109% | — | In play | — |
| 11/10 1:14:53 AM | BTC | UP | 6 sec | -0.065% | 0¢ | ❌ Lost | $0.00 |
| 11/10 1:14:53 AM | NATGAS | DOWN | 6 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/10 1:14:53 AM | DOGE | UP | 6 sec | -0.039% | 0¢ | ❌ Lost | $0.00 |
| 11/10 1:14:53 AM | AUDUSD | UP | 6 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/10 1:14:53 AM | USDJPY | UP | 6 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/10 1:14:36 AM | SOL | UP | 24 sec | -0.086% | 0¢ | ❌ Lost | $0.00 |
| 11/10 1:14:36 AM | WTI | UP | 24 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 11/10 1:14:20 AM | USDCAD | DOWN | 40 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/10 1:14:20 AM | ETH | DOWN | 40 sec | +0.046% | 0¢ | ❌ Lost | $0.00 |
| 11/10 1:14:20 AM | BRENT | UP | 40 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/10 1:14:04 AM | HYPE | DOWN | 56 sec | +0.109% | 0¢ | ❌ Lost | -$0.15 |
| 11/10 1:13:49 AM | COPPER | DOWN | 70 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/10 1:13:16 AM | ZEC | UP | 1.7 min | -0.321% | 1¢ | ❌ Lost | -$0.15 |
| 11/10 1:13:00 AM | 5YRRATE | UP | 2.0 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/10 1:13:00 AM | BNB | UP | 2.0 min | -0.096% | 0¢ | ❌ Lost | -$0.15 |
| 11/10 1:12:45 AM | NEAR | UP | 2.2 min | -0.404% | 2¢ | ❌ Lost | -$0.15 |
| 11/10 1:12:12 AM | GOLD | DOWN | 2.8 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/10 1:11:41 AM | 10YRRATE | UP | 3.3 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/10 1:11:41 AM | PLATINUM | DOWN | 3.3 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/10 1:10:54 AM | SILVER | DOWN | 4.1 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/10 1:10:38 AM | 30YRRATE | UP | 4.4 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/10 1:10:22 AM | PALLADIUM | DOWN | 4.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/10 1:09:34 AM | XRP | UP | 5.4 min | -0.511% | 1¢ | ❌ Lost | -$0.15 |
| 11/10 12:59:51 AM | 2YRRATE | DOWN | 9 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/10 12:59:51 AM | EURUSD | DOWN | 9 sec | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
