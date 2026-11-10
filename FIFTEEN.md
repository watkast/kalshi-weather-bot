# 15-Minute 1¢ Study

*Updated Tue Nov 10, 2:06 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 4154 finished bets | 1% | $182.60 | +40% | +4.40¢ | $89.05 / $93.55 |

*Expect about **96 buys a day** (~$14.46/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 3862 | $100.25 | +24% |
| Volatility model ≥ 2%, hold to the close | 7593 | $66.35 | +7% |
| Momentum model ≥ 2%, hold to the close | 6286 | -$7.65 | -1% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 51919 | 51900 | 199 (0%) | 1.07% | -$3,535.90 (-56%) | Hold to the close: -$3,535.90 (-56%) |

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
| Volatility model | 31499 | 4.8% | 0.4% (128) | -678% | ❌ Worse |
| Momentum model | 31499 | 4.6% | 0.4% (128) | -703% | ❌ Worse |
| Mean-reversion model | 31499 | 8.1% | 0.4% (128) | -820% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 31499 | 128 | -48% | -87% | -87% | -84% |
| Volatility model ≥ 2% | 7593 | 70 | +7% | -77% | -76% | -71% |
| Volatility model ≥ 5% | 4154 | 46 | +40% | -72% | -70% | -66% |
| Volatility model ≥ 10% | 2394 | 28 | +68% | -62% | -60% | -56% |
| Momentum model ≥ 2% | 6286 | 51 | -1% | -78% | -77% | -74% |
| Momentum model ≥ 5% | 3862 | 37 | +24% | -73% | -73% | -69% |
| Momentum model ≥ 10% | 2532 | 25 | +39% | -65% | -64% | -60% |
| Mean-reversion model ≥ 2% | 13042 | 91 | -23% | -82% | -82% | -79% |
| Mean-reversion model ≥ 5% | 9141 | 78 | -5% | -79% | -79% | -76% |
| Mean-reversion model ≥ 10% | 6112 | 56 | +4% | -77% | -76% | -74% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 31704 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 12313 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 7883 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 51900 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 199 | 0% | -$3,535.90 | -56% | — |
| Sell at 2¢ | 2068 | 4% | -$5,504.22 | -87% | 47 sec |
| Sell at 3¢ | 1407 | 3% | -$5,493.17 | -87% | 48 sec |
| Sell at 5¢ | 982 | 2% | -$5,375.60 | -85% | 63 sec |
| Sell at 10¢ | 595 | 1% | -$5,150.45 | -81% | 65 sec |
| Sell at 25¢ | 314 | 1% | -$4,778.56 | -76% | 83 sec |
| Sell at 50¢ | 205 | 0% | -$4,336.15 | -69% | 1.7 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 12 | 0 | 25% | 17% | -100% | -57% | -35% |
| 5–10 min | 2580 | 12 | 11% | 4% | -56% | -81% | -82% |
| 2–5 min | 16772 | 93 | 7% | 3% | -45% | -87% | -86% |
| 1–2 min | 13107 | 44 | 3% | 2% | -63% | -92% | -92% |
| Under 1 min | 19429 | 50 | 1% | 0% | -63% | -85% | -84% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 3551 | 15 | 5% | 2% | -45% | -88% | -88% |
| SOL | 3546 | 16 | 4% | 2% | -42% | -87% | -87% |
| HYPE | 3538 | 11 | 5% | 2% | -61% | -89% | -88% |
| BNB | 3531 | 19 | 5% | 2% | -32% | -86% | -85% |
| DOGE | 3526 | 8 | 4% | 2% | -71% | -90% | -89% |
| ETH | 3522 | 15 | 7% | 3% | -47% | -81% | -81% |
| BTC | 3501 | 17 | 5% | 2% | -33% | -87% | -88% |
| NEAR | 3500 | 16 | 5% | 2% | -41% | -85% | -85% |
| XRP | 3489 | 13 | 3% | 1% | -53% | -89% | -88% |
| GOLD | 1866 | 5 | 6% | 2% | -67% | -81% | -83% |
| WTI | 1840 | 6 | 4% | 2% | -61% | -91% | -92% |
| SILVER | 1819 | 8 | 5% | 2% | -48% | -83% | -82% |
| PLATINUM | 1648 | 4 | 2% | 1% | -77% | -96% | -95% |
| EURUSD | 1583 | 5 | 2% | 1% | -71% | -90% | -89% |
| COPPER | 1545 | 6 | 2% | 1% | -64% | -73% | -72% |
| NATGAS | 1507 | 8 | 2% | 1% | -50% | -78% | -77% |
| GBPUSD | 1502 | 5 | 2% | 1% | -69% | -96% | -96% |
| PALLADIUM | 1483 | 3 | 1% | 0% | -81% | -92% | -92% |
| USDJPY | 1480 | 6 | 2% | 1% | -62% | -96% | -96% |
| AUDUSD | 1043 | 5 | 2% | 1% | -55% | -87% | -88% |
| USDCAD | 1011 | 0 | 2% | 1% | -100% | -96% | -97% |
| BRENT | 605 | 0 | 2% | 1% | -100% | -97% | -97% |
| 10YRRATE | 334 | 2 | 4% | 2% | -44% | -64% | -62% |
| 2YRRATE | 316 | 4 | 4% | 2% | +18% | -33% | -32% |
| 30YRRATE | 310 | 0 | 2% | 1% | -100% | -96% | -94% |
| 5YRRATE | 293 | 2 | 4% | 2% | -36% | -92% | -95% |
| INX | 11 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 26306 | 104 | 4% | 2% | -55% | -88% | -87% |
| DOWN (bought NO) | 25594 | 95 | 4% | 2% | -57% | -86% | -86% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 5104 | 25 | 2% | 1% | -13% | -77% | -76% |
| 0.05–0.1% | 5420 | 20 | 3% | 2% | -44% | -91% | -91% |
| 0.1–0.2% | 8155 | 30 | 5% | 2% | -54% | -89% | -89% |
| 0.2–0.5% | 9470 | 40 | 6% | 3% | -53% | -87% | -86% |
| Over 0.5% | 3547 | 15 | 7% | 3% | -56% | -87% | -88% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 12823 | 43 | 4% | 2% | -62% | -88% | -88% |
| Morning (6am–12pm) | 12425 | 56 | 4% | 2% | -49% | -84% | -84% |
| Afternoon (12–6pm) | 12535 | 57 | 4% | 2% | -47% | -86% | -86% |
| Evening (6pm–12am) | 14117 | 43 | 4% | 2% | -65% | -90% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,907 |
| Time from buy to best bounce (bounced bets) | 51 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/10 2:06:28 AM | ETH | UP | 8.5 min | -0.689% | — | In play | — |
| 11/10 2:05:41 AM | 2YRRATE | DOWN | 9.3 min | — | — | In play | — |
| 11/10 1:59:46 AM | USDCAD | DOWN | 14 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/10 1:59:30 AM | SILVER | UP | 30 sec | — | 0¢ | ❌ Lost | $0.00 |
| 11/10 1:59:14 AM | ZEC | DOWN | 46 sec | +0.141% | 0¢ | ❌ Lost | $0.00 |
| 11/10 1:59:14 AM | 10YRRATE | UP | 46 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/10 1:59:14 AM | GOLD | UP | 46 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/10 1:59:14 AM | AUDUSD | DOWN | 46 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/10 1:59:14 AM | XRP | DOWN | 46 sec | +0.055% | 1¢ | ❌ Lost | -$0.15 |
| 11/10 1:58:58 AM | 5YRRATE | UP | 61 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/10 1:58:58 AM | 2YRRATE | UP | 61 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/10 1:58:58 AM | WTI | UP | 61 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 11/10 1:58:42 AM | NATGAS | DOWN | 77 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/10 1:58:42 AM | DOGE | DOWN | 77 sec | +0.072% | 0¢ | ❌ Lost | -$0.15 |
| 11/10 1:58:26 AM | HYPE | DOWN | 1.6 min | +0.141% | 1¢ | ❌ Lost | -$0.15 |
| 11/10 1:58:10 AM | EURUSD | DOWN | 1.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/10 1:57:38 AM | BNB | DOWN | 2.4 min | +0.068% | 0¢ | ❌ Lost | $0.00 |
| 11/10 1:57:22 AM | SOL | DOWN | 2.6 min | +0.180% | 0¢ | ❌ Lost | -$0.15 |
| 11/10 1:57:22 AM | BRENT | UP | 2.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/10 1:56:34 AM | BTC | DOWN | 3.4 min | +0.157% | 1¢ | ❌ Lost | -$0.15 |
| 11/10 1:56:34 AM | ETH | DOWN | 3.4 min | +0.153% | 1¢ | ❌ Lost | -$0.15 |
| 11/10 1:44:58 AM | SOL | DOWN | 1 sec | +0.003% | 0¢ | ❌ Lost | -$0.15 |
| 11/10 1:44:58 AM | ETH | DOWN | 1 sec | +0.018% | 0¢ | ❌ Lost | $0.00 |
| 11/10 1:44:58 AM | USDJPY | UP | 1 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/10 1:44:58 AM | GBPUSD | UP | 1 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/10 1:44:40 AM | PALLADIUM | DOWN | 19 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/10 1:44:40 AM | PLATINUM | DOWN | 19 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/10 1:44:24 AM | SILVER | DOWN | 35 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/10 1:44:24 AM | DOGE | DOWN | 35 sec | +0.040% | 0¢ | ❌ Lost | $0.00 |
| 11/10 1:44:08 AM | EURUSD | DOWN | 51 sec | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
