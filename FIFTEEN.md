# 15-Minute 1¢ Study

*Updated Mon Nov 2, 7:56 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 3528 finished bets | 1% | $123.65 | +31% | +3.50¢ | $69.80 / $53.85 |

*Expect about **98 buys a day** (~$14.76/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 3260 | $50.95 | +14% |
| Volatility model ≥ 2%, hold to the close | 6523 | $49.80 | +6% |
| Momentum model ≥ 2%, hold to the close | 5387 | -$35.25 | -6% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 43214 | 43196 | 160 (0%) | 1.07% | -$3,018.70 (-57%) | Hold to the close: -$3,018.70 (-57%) |

*In play or awaiting result: 17. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 26755 | 4.7% | 0.4% (106) | -677% | ❌ Worse |
| Momentum model | 26755 | 4.6% | 0.4% (106) | -701% | ❌ Worse |
| Mean-reversion model | 26755 | 8.1% | 0.4% (106) | -823% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 26755 | 106 | -50% | -87% | -87% | -85% |
| Volatility model ≥ 2% | 6523 | 60 | +6% | -79% | -78% | -74% |
| Volatility model ≥ 5% | 3528 | 37 | +31% | -76% | -75% | -71% |
| Volatility model ≥ 10% | 1997 | 22 | +57% | -70% | -68% | -65% |
| Momentum model ≥ 2% | 5387 | 42 | -6% | -81% | -80% | -77% |
| Momentum model ≥ 5% | 3260 | 29 | +14% | -79% | -78% | -74% |
| Momentum model ≥ 10% | 2128 | 19 | +25% | -74% | -73% | -69% |
| Mean-reversion model ≥ 2% | 11050 | 76 | -25% | -83% | -83% | -80% |
| Mean-reversion model ≥ 5% | 7746 | 65 | -7% | -81% | -80% | -77% |
| Mean-reversion model ≥ 10% | 5177 | 46 | +1% | -79% | -79% | -76% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 26957 | 5% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 10179 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 6060 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 43196 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 160 | 0% | -$3,018.70 | -57% | — |
| Sell at 2¢ | 1705 | 4% | -$4,577.40 | -87% | 47 sec |
| Sell at 3¢ | 1170 | 3% | -$4,564.40 | -87% | 48 sec |
| Sell at 5¢ | 812 | 2% | -$4,464.90 | -85% | 63 sec |
| Sell at 10¢ | 490 | 1% | -$4,280.80 | -81% | 65 sec |
| Sell at 25¢ | 255 | 1% | -$3,966.65 | -75% | 82 sec |
| Sell at 50¢ | 166 | 0% | -$3,606.20 | -69% | 1.8 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 11 | 0 | 27% | 18% | -100% | -53% | -29% |
| 5–10 min | 2073 | 9 | 11% | 4% | -59% | -81% | -82% |
| 2–5 min | 13878 | 75 | 7% | 4% | -47% | -86% | -86% |
| 1–2 min | 10901 | 38 | 3% | 2% | -62% | -92% | -92% |
| Under 1 min | 16333 | 38 | 1% | 0% | -67% | -85% | -84% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 3021 | 13 | 5% | 3% | -45% | -88% | -87% |
| SOL | 3012 | 11 | 4% | 2% | -54% | -91% | -90% |
| BNB | 3009 | 17 | 5% | 2% | -29% | -85% | -84% |
| HYPE | 3007 | 9 | 5% | 2% | -63% | -89% | -87% |
| DOGE | 2995 | 6 | 4% | 2% | -75% | -90% | -89% |
| ETH | 2992 | 11 | 7% | 3% | -55% | -85% | -85% |
| BTC | 2976 | 14 | 5% | 2% | -36% | -88% | -89% |
| NEAR | 2975 | 15 | 5% | 2% | -35% | -83% | -84% |
| XRP | 2970 | 12 | 3% | 1% | -50% | -89% | -89% |
| GOLD | 1581 | 5 | 5% | 2% | -62% | -81% | -83% |
| SILVER | 1541 | 7 | 5% | 2% | -46% | -82% | -82% |
| WTI | 1540 | 4 | 3% | 1% | -69% | -93% | -93% |
| PLATINUM | 1371 | 3 | 2% | 1% | -80% | -96% | -96% |
| EURUSD | 1312 | 3 | 2% | 1% | -79% | -89% | -89% |
| COPPER | 1308 | 6 | 2% | 1% | -57% | -69% | -68% |
| NATGAS | 1258 | 7 | 2% | 1% | -48% | -81% | -81% |
| GBPUSD | 1242 | 2 | 2% | 1% | -85% | -96% | -96% |
| PALLADIUM | 1236 | 2 | 1% | 0% | -85% | -90% | -91% |
| USDJPY | 1227 | 5 | 2% | 1% | -62% | -97% | -96% |
| AUDUSD | 769 | 4 | 2% | 1% | -51% | -85% | -84% |
| USDCAD | 735 | 0 | 2% | 1% | -100% | -97% | -98% |
| BRENT | 344 | 0 | 1% | 1% | -100% | -97% | -96% |
| 10YRRATE | 210 | 1 | 5% | 2% | -56% | -46% | -44% |
| 30YRRATE | 198 | 0 | 2% | 0% | -100% | -97% | -96% |
| 2YRRATE | 191 | 2 | 4% | 1% | -2% | +5% | +6% |
| 5YRRATE | 176 | 1 | 6% | 2% | -47% | -90% | -93% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 21976 | 87 | 4% | 2% | -54% | -88% | -87% |
| DOWN (bought NO) | 21220 | 73 | 4% | 2% | -61% | -87% | -87% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 4386 | 21 | 2% | 1% | -17% | -82% | -82% |
| 0.05–0.1% | 4631 | 18 | 3% | 2% | -42% | -91% | -90% |
| 0.1–0.2% | 6977 | 24 | 4% | 2% | -57% | -90% | -90% |
| 0.2–0.5% | 7971 | 33 | 7% | 3% | -54% | -86% | -86% |
| Over 0.5% | 2987 | 12 | 7% | 3% | -59% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 10646 | 37 | 4% | 2% | -60% | -87% | -87% |
| Morning (6am–12pm) | 10804 | 48 | 4% | 2% | -49% | -85% | -85% |
| Afternoon (12–6pm) | 10198 | 38 | 4% | 2% | -56% | -85% | -85% |
| Evening (6pm–12am) | 11548 | 37 | 3% | 2% | -63% | -91% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,767 |
| Time from buy to best bounce (bounced bets) | 51 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/2 7:56:28 PM | ETH | UP | 3.5 min | -0.200% | — | In play | — |
| 11/2 7:56:28 PM | ZEC | UP | 3.5 min | -0.576% | — | In play | — |
| 11/2 7:56:28 PM | DOGE | UP | 3.5 min | -0.241% | — | In play | — |
| 11/2 7:56:28 PM | SOL | UP | 3.5 min | -0.248% | — | In play | — |
| 11/2 7:56:12 PM | BRENT | UP | 3.8 min | — | — | In play | — |
| 11/2 7:55:57 PM | HYPE | UP | 4.0 min | -0.436% | — | In play | — |
| 11/2 7:55:24 PM | NEAR | UP | 4.6 min | -0.565% | — | In play | — |
| 11/2 7:53:27 PM | EURUSD | DOWN | 6.5 min | — | — | In play | — |
| 11/2 7:44:48 PM | USDJPY | DOWN | 11 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/2 7:44:32 PM | AUDUSD | UP | 27 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/2 7:44:32 PM | GOLD | UP | 27 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 11/2 7:44:17 PM | ETH | UP | 42 sec | -0.068% | 4¢ | ❌ Lost | $0.00 |
| 11/2 7:44:17 PM | SOL | UP | 42 sec | -0.060% | 1¢ | ❌ Lost | -$0.15 |
| 11/2 7:44:00 PM | BNB | UP | 59 sec | -0.133% | 1¢ | ❌ Lost | -$0.15 |
| 11/2 7:44:00 PM | COPPER | UP | 59 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/2 7:44:00 PM | DOGE | UP | 59 sec | -0.150% | 1¢ | ❌ Lost | -$0.15 |
| 11/2 7:43:44 PM | NEAR | UP | 75 sec | -0.503% | 0¢ | ❌ Lost | $0.00 |
| 11/2 7:43:44 PM | BTC | UP | 75 sec | -0.128% | 0¢ | ❌ Lost | $0.00 |
| 11/2 7:43:28 PM | HYPE | UP | 1.5 min | -0.240% | 1¢ | ❌ Lost | -$0.15 |
| 11/2 7:43:28 PM | BRENT | DOWN | 1.5 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/2 7:43:28 PM | PALLADIUM | UP | 1.5 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/2 7:43:11 PM | ZEC | UP | 1.8 min | -0.486% | 0¢ | ❌ Lost | $0.00 |
| 11/2 7:42:52 PM | WTI | DOWN | 2.1 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/2 7:42:52 PM | EURUSD | UP | 2.1 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/2 7:42:52 PM | SILVER | UP | 2.1 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/2 7:42:36 PM | PLATINUM | UP | 2.4 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/2 7:29:51 PM | GBPUSD | UP | 8 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/2 7:29:51 PM | USDJPY | DOWN | 8 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/2 7:29:51 PM | AUDUSD | DOWN | 8 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/2 7:29:51 PM | HYPE | DOWN | 8 sec | -0.019% | 0¢ | ❌ Lost | $0.00 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
