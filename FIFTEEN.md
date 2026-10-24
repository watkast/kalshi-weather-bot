# 15-Minute 1¢ Study

*Updated Fri Oct 23, 8:24 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 2522 finished bets | 1% | $92.40 | +32% | +3.66¢ | $43.85 / $48.55 |

*Expect about **98 buys a day** (~$14.65/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 2329 | $50.45 | +20% |
| Volatility model ≥ 2%, hold to the close | 4677 | $1.15 | +0% |
| Momentum model ≥ 2%, hold to the close | 3890 | -$23.35 | -5% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 30507 | 30498 | 117 (0%) | 1.07% | -$2,083.20 (-56%) | Hold to the close: -$2,083.20 (-56%) |

*In play or awaiting result: 8. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 19303 | 4.6% | 0.4% (82) | -635% | ❌ Worse |
| Momentum model | 19303 | 4.5% | 0.4% (82) | -661% | ❌ Worse |
| Mean-reversion model | 19303 | 7.9% | 0.4% (82) | -766% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 19303 | 82 | -47% | -87% | -87% | -85% |
| Volatility model ≥ 2% | 4677 | 41 | +0% | -78% | -77% | -73% |
| Volatility model ≥ 5% | 2522 | 27 | +32% | -73% | -72% | -69% |
| Volatility model ≥ 10% | 1434 | 17 | +66% | -64% | -62% | -59% |
| Momentum model ≥ 2% | 3890 | 31 | -5% | -79% | -79% | -76% |
| Momentum model ≥ 5% | 2329 | 22 | +20% | -75% | -75% | -71% |
| Momentum model ≥ 10% | 1526 | 15 | +35% | -69% | -68% | -64% |
| Mean-reversion model ≥ 2% | 7773 | 54 | -24% | -83% | -82% | -80% |
| Mean-reversion model ≥ 5% | 5435 | 45 | -9% | -80% | -79% | -77% |
| Mean-reversion model ≥ 10% | 3613 | 32 | +0% | -78% | -77% | -75% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 19503 | 5% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 7340 | 2% | 2% | 1% | 1% | 0% | 0% |
| Financials | 3655 | 2% | 1% | 1% | 1% | 0% | 0% |
| **All** | 30498 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 117 | 0% | -$2,083.20 | -56% | — |
| Sell at 2¢ | 1138 | 4% | -$3,257.32 | -88% | 47 sec |
| Sell at 3¢ | 782 | 3% | -$3,248.22 | -87% | 48 sec |
| Sell at 5¢ | 547 | 2% | -$3,197.65 | -86% | 61 sec |
| Sell at 10¢ | 335 | 1% | -$3,072.35 | -83% | 64 sec |
| Sell at 25¢ | 185 | 1% | -$2,828.85 | -76% | 82 sec |
| Sell at 50¢ | 119 | 0% | -$2,553.95 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 1307 | 7 | 11% | 4% | -49% | -80% | -82% |
| 2–5 min | 9765 | 53 | 7% | 3% | -46% | -87% | -87% |
| 1–2 min | 7761 | 29 | 3% | 1% | -59% | -91% | -91% |
| Under 1 min | 11661 | 28 | 1% | 0% | -66% | -86% | -85% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 2186 | 12 | 5% | 2% | -31% | -89% | -89% |
| HYPE | 2177 | 8 | 5% | 3% | -55% | -88% | -86% |
| BNB | 2177 | 12 | 5% | 2% | -32% | -83% | -82% |
| SOL | 2169 | 5 | 4% | 2% | -71% | -92% | -92% |
| ETH | 2167 | 10 | 6% | 3% | -45% | -86% | -85% |
| DOGE | 2163 | 4 | 4% | 2% | -77% | -90% | -89% |
| XRP | 2158 | 9 | 3% | 1% | -48% | -88% | -88% |
| NEAR | 2154 | 12 | 5% | 3% | -28% | -81% | -81% |
| BTC | 2152 | 12 | 5% | 2% | -25% | -88% | -89% |
| GOLD | 1190 | 4 | 4% | 2% | -60% | -81% | -83% |
| SILVER | 1156 | 5 | 4% | 1% | -50% | -82% | -82% |
| WTI | 1136 | 3 | 3% | 1% | -69% | -94% | -95% |
| PLATINUM | 1010 | 0 | 1% | 1% | -100% | -98% | -98% |
| COPPER | 987 | 4 | 1% | 1% | -62% | -69% | -69% |
| EURUSD | 938 | 3 | 2% | 1% | -70% | -86% | -86% |
| NATGAS | 931 | 5 | 2% | 1% | -50% | -86% | -86% |
| PALLADIUM | 897 | 2 | 1% | 0% | -79% | -88% | -88% |
| GBPUSD | 884 | 1 | 2% | 1% | -89% | -96% | -96% |
| USDJPY | 866 | 5 | 1% | 1% | -46% | -98% | -97% |
| AUDUSD | 428 | 0 | 1% | 0% | -100% | -98% | -98% |
| USDCAD | 387 | 0 | 1% | 0% | -100% | -98% | -99% |
| 10YRRATE | 43 | 0 | 0% | 0% | -100% | -100% | -100% |
| 2YRRATE | 40 | 1 | 2% | 0% | +133% | +138% | +133% |
| 30YRRATE | 39 | 0 | 0% | 0% | -100% | -100% | -100% |
| BRENT | 33 | 0 | 0% | 0% | -100% | -100% | -100% |
| 5YRRATE | 30 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 15396 | 64 | 4% | 2% | -52% | -87% | -86% |
| DOWN (bought NO) | 15102 | 53 | 4% | 2% | -60% | -88% | -88% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 3203 | 17 | 2% | 1% | -11% | -79% | -78% |
| 0.05–0.1% | 3347 | 11 | 3% | 2% | -52% | -92% | -91% |
| 0.1–0.2% | 5027 | 18 | 5% | 2% | -56% | -89% | -89% |
| 0.2–0.5% | 5725 | 28 | 6% | 3% | -46% | -87% | -86% |
| Over 0.5% | 2197 | 10 | 7% | 3% | -53% | -87% | -88% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 7532 | 31 | 4% | 2% | -53% | -84% | -84% |
| Morning (6am–12pm) | 7425 | 34 | 4% | 2% | -48% | -88% | -87% |
| Afternoon (12–6pm) | 7298 | 24 | 4% | 2% | -61% | -87% | -88% |
| Evening (6pm–12am) | 8243 | 28 | 3% | 2% | -61% | -90% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,622 |
| Time from buy to best bounce (bounced bets) | 49 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/23 8:23:09 PM | ZEC | UP | 6.8 min | -0.593% | — | In play | — |
| 10/23 8:14:09 PM | XRP | DOWN | 50 sec | +0.046% | 0¢ | ❌ Lost | $0.00 |
| 10/23 8:13:51 PM | ETH | DOWN | 69 sec | +0.040% | 0¢ | ❌ Lost | -$0.15 |
| 10/23 8:13:51 PM | DOGE | DOWN | 69 sec | +0.077% | 1¢ | ❌ Lost | -$0.15 |
| 10/23 8:13:04 PM | HYPE | DOWN | 1.9 min | +0.092% | 1¢ | ❌ Lost | -$0.15 |
| 10/23 8:12:46 PM | BNB | DOWN | 2.2 min | +0.130% | 1¢ | ❌ Lost | -$0.15 |
| 10/23 8:11:59 PM | ZEC | DOWN | 3.0 min | +0.283% | 0¢ | ❌ Lost | -$0.15 |
| 10/23 7:59:43 PM | XRP | DOWN | 17 sec | +0.000% | 0¢ | ❌ Lost | $0.00 |
| 10/23 7:59:10 PM | BRENT | UP | 49 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/23 7:58:53 PM | WTI | UP | 66 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/23 7:57:16 PM | DOGE | DOWN | 2.7 min | +0.179% | 1¢ | ❌ Lost | -$0.15 |
| 10/23 7:56:43 PM | NEAR | DOWN | 3.3 min | +0.422% | 1¢ | ❌ Lost | -$0.15 |
| 10/23 7:56:27 PM | SOL | DOWN | 3.5 min | +0.213% | 1¢ | ❌ Lost | -$0.15 |
| 10/23 7:56:11 PM | BTC | DOWN | 3.8 min | +0.141% | 1¢ | ❌ Lost | -$0.15 |
| 10/23 7:55:22 PM | ZEC | DOWN | 4.6 min | +0.650% | 0¢ | ❌ Lost | $0.00 |
| 10/23 7:55:22 PM | ETH | DOWN | 4.6 min | +0.185% | 1¢ | ❌ Lost | -$0.15 |
| 10/23 7:55:06 PM | HYPE | DOWN | 4.9 min | +0.304% | 1¢ | ❌ Lost | -$0.15 |
| 10/23 7:54:36 PM | BNB | DOWN | 5.4 min | +0.168% | 0¢ | ❌ Lost | $0.00 |
| 10/23 7:44:57 PM | SOL | UP | 3 sec | -0.022% | 0¢ | ❌ Lost | $0.00 |
| 10/23 7:44:57 PM | DOGE | DOWN | 3 sec | +0.014% | 0¢ | ❌ Lost | $0.00 |
| 10/23 7:44:41 PM | NEAR | DOWN | 19 sec | +0.037% | 0¢ | ❌ Lost | -$0.15 |
| 10/23 7:44:25 PM | BRENT | UP | 35 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/23 7:44:25 PM | BTC | DOWN | 35 sec | +0.038% | 1¢ | ❌ Lost | -$0.15 |
| 10/23 7:43:50 PM | BNB | DOWN | 69 sec | +0.061% | 0¢ | ❌ Lost | $0.00 |
| 10/23 7:43:50 PM | ZEC | UP | 69 sec | -0.283% | 0¢ | ❌ Lost | -$0.15 |
| 10/23 7:43:35 PM | HYPE | DOWN | 84 sec | +0.111% | 0¢ | ❌ Lost | -$0.15 |
| 10/23 7:43:35 PM | ETH | DOWN | 84 sec | +0.072% | 0¢ | ❌ Lost | -$0.15 |
| 10/23 7:43:03 PM | WTI | UP | 1.9 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/23 7:42:45 PM | XRP | DOWN | 2.2 min | +0.171% | 1¢ | ❌ Lost | -$0.15 |
| 10/23 7:29:41 PM | NEAR | DOWN | 19 sec | -0.013% | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
