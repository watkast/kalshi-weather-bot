# 15-Minute 1¢ Study

*Updated Wed Nov 11, 12:58 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 4216 finished bets | 1% | $175.70 | +38% | +4.17¢ | $85.45 / $90.25 |

*Expect about **95 buys a day** (~$14.20/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 3944 | $90.65 | +21% |
| Volatility model ≥ 2%, hold to the close | 7739 | $48.35 | +5% |
| Momentum model ≥ 2%, hold to the close | 6430 | -$25.20 | -3% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 53814 | 53785 | 205 (0%) | 1.07% | -$3,691.15 (-56%) | Hold to the close: -$3,691.15 (-56%) |

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
| Volatility model | 32357 | 4.7% | 0.4% (131) | -672% | ❌ Worse |
| Momentum model | 32357 | 4.6% | 0.4% (131) | -697% | ❌ Worse |
| Mean-reversion model | 32357 | 8.1% | 0.4% (131) | -814% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 32357 | 131 | -48% | -87% | -87% | -84% |
| Volatility model ≥ 2% | 7739 | 70 | +5% | -77% | -76% | -72% |
| Volatility model ≥ 5% | 4216 | 46 | +38% | -72% | -70% | -67% |
| Volatility model ≥ 10% | 2436 | 28 | +65% | -62% | -61% | -57% |
| Momentum model ≥ 2% | 6430 | 51 | -3% | -78% | -77% | -74% |
| Momentum model ≥ 5% | 3944 | 37 | +21% | -74% | -73% | -69% |
| Momentum model ≥ 10% | 2587 | 25 | +36% | -66% | -65% | -61% |
| Mean-reversion model ≥ 2% | 13377 | 92 | -25% | -82% | -82% | -79% |
| Mean-reversion model ≥ 5% | 9353 | 78 | -8% | -80% | -79% | -76% |
| Mean-reversion model ≥ 10% | 6249 | 56 | +2% | -77% | -77% | -74% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 32562 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 12878 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 8345 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 53785 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 205 | 0% | -$3,691.15 | -56% | — |
| Sell at 2¢ | 2142 | 4% | -$5,724.23 | -87% | 47 sec |
| Sell at 3¢ | 1459 | 3% | -$5,712.14 | -87% | 48 sec |
| Sell at 5¢ | 1013 | 2% | -$5,594.70 | -85% | 63 sec |
| Sell at 10¢ | 612 | 1% | -$5,367.43 | -82% | 65 sec |
| Sell at 25¢ | 325 | 1% | -$4,981.40 | -76% | 82 sec |
| Sell at 50¢ | 212 | 0% | -$4,514.15 | -69% | 1.7 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 12 | 0 | 25% | 17% | -100% | -57% | -35% |
| 5–10 min | 2694 | 13 | 11% | 4% | -54% | -81% | -83% |
| 2–5 min | 17407 | 94 | 7% | 3% | -47% | -87% | -87% |
| 1–2 min | 13576 | 45 | 3% | 2% | -63% | -92% | -92% |
| Under 1 min | 20096 | 53 | 1% | 0% | -62% | -85% | -85% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 3645 | 17 | 5% | 2% | -40% | -88% | -88% |
| SOL | 3641 | 16 | 4% | 2% | -44% | -87% | -86% |
| HYPE | 3634 | 11 | 5% | 2% | -62% | -89% | -88% |
| BNB | 3626 | 19 | 5% | 2% | -34% | -86% | -85% |
| DOGE | 3622 | 8 | 4% | 2% | -72% | -90% | -90% |
| ETH | 3615 | 15 | 7% | 3% | -49% | -82% | -81% |
| NEAR | 3597 | 17 | 5% | 2% | -39% | -85% | -85% |
| BTC | 3597 | 17 | 5% | 2% | -35% | -87% | -88% |
| XRP | 3585 | 13 | 3% | 1% | -55% | -89% | -89% |
| GOLD | 1940 | 5 | 5% | 2% | -68% | -81% | -83% |
| WTI | 1923 | 6 | 4% | 2% | -62% | -91% | -92% |
| SILVER | 1892 | 8 | 5% | 2% | -50% | -83% | -83% |
| PLATINUM | 1719 | 4 | 3% | 1% | -78% | -96% | -95% |
| EURUSD | 1655 | 5 | 2% | 1% | -72% | -90% | -89% |
| COPPER | 1606 | 6 | 2% | 1% | -65% | -74% | -74% |
| GBPUSD | 1579 | 6 | 2% | 1% | -65% | -96% | -96% |
| NATGAS | 1575 | 8 | 2% | 1% | -53% | -79% | -78% |
| USDJPY | 1557 | 6 | 2% | 1% | -64% | -97% | -96% |
| PALLADIUM | 1544 | 4 | 1% | 1% | -76% | -92% | -92% |
| AUDUSD | 1113 | 6 | 2% | 1% | -50% | -88% | -88% |
| USDCAD | 1078 | 0 | 3% | 1% | -100% | -96% | -96% |
| BRENT | 679 | 0 | 2% | 1% | -100% | -97% | -97% |
| 10YRRATE | 353 | 2 | 4% | 2% | -47% | -66% | -64% |
| 2YRRATE | 338 | 4 | 4% | 2% | +10% | -38% | -36% |
| 30YRRATE | 332 | 0 | 2% | 1% | -100% | -96% | -94% |
| 5YRRATE | 311 | 2 | 4% | 2% | -40% | -93% | -95% |
| INX | 29 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 27275 | 108 | 4% | 2% | -55% | -88% | -88% |
| DOWN (bought NO) | 26510 | 97 | 4% | 2% | -58% | -86% | -87% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 5171 | 25 | 2% | 1% | -14% | -77% | -76% |
| 0.05–0.1% | 5531 | 20 | 3% | 2% | -45% | -91% | -91% |
| 0.1–0.2% | 8362 | 30 | 5% | 2% | -55% | -89% | -89% |
| 0.2–0.5% | 9780 | 41 | 6% | 3% | -53% | -87% | -86% |
| Over 0.5% | 3710 | 17 | 7% | 3% | -53% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 13236 | 43 | 4% | 2% | -63% | -88% | -88% |
| Morning (6am–12pm) | 13083 | 60 | 4% | 2% | -48% | -85% | -84% |
| Afternoon (12–6pm) | 12878 | 57 | 4% | 2% | -48% | -86% | -86% |
| Evening (6pm–12am) | 14588 | 45 | 4% | 2% | -65% | -90% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,862 |
| Time from buy to best bounce (bounced bets) | 50 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/11 12:58:51 PM | NATGAS | DOWN | 68 sec | — | — | In play | — |
| 11/11 12:58:51 PM | BNB | DOWN | 68 sec | +0.050% | — | In play | — |
| 11/11 12:58:03 PM | DOGE | DOWN | 1.9 min | +0.184% | — | In play | — |
| 11/11 12:58:03 PM | SOL | DOWN | 1.9 min | +0.122% | — | In play | — |
| 11/11 12:56:58 PM | HYPE | DOWN | 3.0 min | +0.256% | — | In play | — |
| 11/11 12:56:25 PM | XRP | DOWN | 3.6 min | +0.284% | — | In play | — |
| 11/11 12:55:36 PM | ZEC | DOWN | 4.4 min | +0.722% | — | In play | — |
| 11/11 12:54:30 PM | NEAR | DOWN | 5.5 min | +0.501% | — | In play | — |
| 11/11 12:44:54 PM | INX | DOWN | 6 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/11 12:44:22 PM | SILVER | UP | 38 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 11/11 12:44:07 PM | ZEC | UP | 53 sec | -0.229% | 1¢ | ❌ Lost | -$0.15 |
| 11/11 12:43:49 PM | GBPUSD | DOWN | 71 sec | — | 3¢ | ❌ Lost | -$0.15 |
| 11/11 12:43:49 PM | BTC | UP | 71 sec | -0.084% | 0¢ | ❌ Lost | -$0.15 |
| 11/11 12:43:33 PM | GOLD | UP | 87 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 11/11 12:43:17 PM | HYPE | UP | 1.7 min | -0.248% | 1¢ | ❌ Lost | -$0.15 |
| 11/11 12:43:17 PM | BNB | UP | 1.7 min | -0.066% | 1¢ | ❌ Lost | -$0.15 |
| 11/11 12:43:02 PM | WTI | UP | 1.9 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/11 12:43:02 PM | BRENT | UP | 1.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/11 12:42:14 PM | ETH | UP | 2.8 min | -0.250% | 1¢ | ❌ Lost | -$0.15 |
| 11/11 12:42:14 PM | NEAR | UP | 2.8 min | -0.580% | 1¢ | ❌ Lost | -$0.15 |
| 11/11 12:41:11 PM | XRP | UP | 3.8 min | -0.463% | 1¢ | ❌ Lost | -$0.15 |
| 11/11 12:41:11 PM | SOL | UP | 3.8 min | -0.325% | 1¢ | ❌ Lost | -$0.15 |
| 11/11 12:40:40 PM | DOGE | UP | 4.3 min | -0.456% | 1¢ | ❌ Lost | -$0.15 |
| 11/11 12:29:44 PM | GOLD | DOWN | 16 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 11/11 12:29:44 PM | COPPER | DOWN | 16 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/11 12:29:44 PM | NATGAS | UP | 16 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/11 12:29:28 PM | SILVER | DOWN | 32 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 11/11 12:29:13 PM | BNB | DOWN | 47 sec | +0.052% | 0¢ | ❌ Lost | $0.00 |
| 11/11 12:29:13 PM | PLATINUM | DOWN | 47 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/11 12:29:13 PM | XRP | DOWN | 47 sec | +0.104% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
