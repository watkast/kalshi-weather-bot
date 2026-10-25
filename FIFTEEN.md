# 15-Minute 1¢ Study

*Updated Sun Oct 25, 5:30 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 2639 finished bets | 1% | $92.90 | +31% | +3.52¢ | $38.00 / $54.90 |

*Expect about **97 buys a day** (~$14.58/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 2433 | $67.20 | +25% |
| Volatility model ≥ 2%, hold to the close | 4867 | $6.20 | +1% |
| Momentum model ≥ 2%, hold to the close | 4065 | -$15.00 | -3% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 31371 | 31354 | 119 (0%) | 1.07% | -$2,145.95 (-56%) | Hold to the close: -$2,145.95 (-56%) |

*In play or awaiting result: 16. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 20147 | 4.6% | 0.4% (84) | -644% | ❌ Worse |
| Momentum model | 20147 | 4.5% | 0.4% (84) | -670% | ❌ Worse |
| Mean-reversion model | 20147 | 7.9% | 0.4% (84) | -780% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 20147 | 84 | -48% | -87% | -87% | -85% |
| Volatility model ≥ 2% | 4867 | 43 | +1% | -78% | -77% | -73% |
| Volatility model ≥ 5% | 2639 | 28 | +31% | -74% | -73% | -69% |
| Volatility model ≥ 10% | 1501 | 18 | +68% | -65% | -64% | -61% |
| Momentum model ≥ 2% | 4065 | 33 | -3% | -80% | -79% | -76% |
| Momentum model ≥ 5% | 2433 | 24 | +25% | -76% | -76% | -71% |
| Momentum model ≥ 10% | 1588 | 16 | +39% | -70% | -69% | -64% |
| Mean-reversion model ≥ 2% | 8100 | 55 | -26% | -83% | -82% | -80% |
| Mean-reversion model ≥ 5% | 5678 | 46 | -11% | -81% | -80% | -77% |
| Mean-reversion model ≥ 10% | 3781 | 33 | -1% | -78% | -78% | -75% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 20347 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 7352 | 2% | 2% | 1% | 1% | 0% | 0% |
| Financials | 3655 | 2% | 1% | 1% | 1% | 0% | 0% |
| **All** | 31354 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 119 | 0% | -$2,145.95 | -56% | — |
| Sell at 2¢ | 1163 | 4% | -$3,341.57 | -88% | 47 sec |
| Sell at 3¢ | 797 | 3% | -$3,333.12 | -87% | 48 sec |
| Sell at 5¢ | 557 | 2% | -$3,281.90 | -86% | 61 sec |
| Sell at 10¢ | 344 | 1% | -$3,151.31 | -83% | 64 sec |
| Sell at 25¢ | 188 | 1% | -$2,909.67 | -76% | 82 sec |
| Sell at 50¢ | 121 | 0% | -$2,631.20 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 1364 | 7 | 11% | 4% | -51% | -81% | -82% |
| 2–5 min | 10015 | 54 | 7% | 3% | -47% | -87% | -87% |
| 1–2 min | 7957 | 30 | 3% | 1% | -59% | -92% | -91% |
| Under 1 min | 12014 | 28 | 1% | 0% | -67% | -86% | -86% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 2280 | 12 | 5% | 2% | -34% | -89% | -89% |
| HYPE | 2274 | 8 | 5% | 3% | -56% | -88% | -86% |
| BNB | 2269 | 12 | 5% | 2% | -34% | -84% | -83% |
| SOL | 2266 | 6 | 3% | 2% | -67% | -92% | -92% |
| ETH | 2262 | 11 | 6% | 3% | -42% | -86% | -86% |
| DOGE | 2255 | 4 | 4% | 2% | -78% | -90% | -90% |
| XRP | 2252 | 9 | 3% | 1% | -50% | -88% | -88% |
| NEAR | 2249 | 12 | 5% | 2% | -31% | -81% | -81% |
| BTC | 2240 | 12 | 5% | 2% | -28% | -88% | -89% |
| GOLD | 1190 | 4 | 4% | 2% | -60% | -81% | -83% |
| SILVER | 1156 | 5 | 4% | 1% | -50% | -82% | -82% |
| WTI | 1143 | 3 | 3% | 1% | -69% | -94% | -95% |
| PLATINUM | 1010 | 0 | 1% | 1% | -100% | -98% | -98% |
| COPPER | 987 | 4 | 1% | 1% | -62% | -69% | -69% |
| EURUSD | 938 | 3 | 2% | 1% | -70% | -86% | -86% |
| NATGAS | 933 | 5 | 2% | 1% | -50% | -86% | -86% |
| PALLADIUM | 897 | 2 | 1% | 0% | -79% | -88% | -88% |
| GBPUSD | 884 | 1 | 2% | 1% | -89% | -96% | -96% |
| USDJPY | 866 | 5 | 1% | 1% | -46% | -98% | -97% |
| AUDUSD | 428 | 0 | 1% | 0% | -100% | -98% | -98% |
| USDCAD | 387 | 0 | 1% | 0% | -100% | -98% | -99% |
| 10YRRATE | 43 | 0 | 0% | 0% | -100% | -100% | -100% |
| 2YRRATE | 40 | 1 | 2% | 0% | +133% | +138% | +133% |
| 30YRRATE | 39 | 0 | 0% | 0% | -100% | -100% | -100% |
| BRENT | 36 | 0 | 0% | 0% | -100% | -100% | -100% |
| 5YRRATE | 30 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 15882 | 65 | 4% | 2% | -53% | -87% | -87% |
| DOWN (bought NO) | 15472 | 54 | 4% | 2% | -60% | -88% | -88% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 3405 | 18 | 2% | 1% | -11% | -80% | -79% |
| 0.05–0.1% | 3511 | 11 | 3% | 2% | -54% | -92% | -92% |
| 0.1–0.2% | 5246 | 19 | 5% | 2% | -55% | -89% | -89% |
| 0.2–0.5% | 5920 | 28 | 6% | 3% | -48% | -87% | -86% |
| Over 0.5% | 2261 | 10 | 7% | 3% | -54% | -87% | -88% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 7877 | 32 | 4% | 2% | -54% | -85% | -85% |
| Morning (6am–12pm) | 7570 | 34 | 4% | 2% | -49% | -88% | -87% |
| Afternoon (12–6pm) | 7332 | 24 | 4% | 2% | -61% | -87% | -88% |
| Evening (6pm–12am) | 8575 | 29 | 3% | 2% | -61% | -90% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,750 |
| Time from buy to best bounce (bounced bets) | 49 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/25 5:29:18 AM | XRP | DOWN | 41 sec | +0.031% | — | In play | — |
| 10/25 5:29:04 AM | SOL | DOWN | 55 sec | +0.046% | — | In play | — |
| 10/25 5:28:19 AM | NEAR | UP | 1.7 min | -0.450% | — | In play | — |
| 10/25 5:27:14 AM | ZEC | DOWN | 2.8 min | +0.369% | — | In play | — |
| 10/25 5:26:12 AM | ETH | DOWN | 3.8 min | +0.157% | — | In play | — |
| 10/25 5:26:12 AM | BTC | DOWN | 3.8 min | +0.105% | — | In play | — |
| 10/25 5:25:56 AM | HYPE | DOWN | 4.0 min | +0.184% | — | In play | — |
| 10/25 5:25:24 AM | DOGE | DOWN | 4.6 min | +0.198% | — | In play | — |
| 10/25 5:24:21 AM | BNB | DOWN | 5.7 min | +0.191% | — | In play | — |
| 10/25 3:58:57 AM | NEAR | DOWN | 63 sec | +0.166% | 0¢ | ❌ Lost | -$0.15 |
| 10/25 3:58:57 AM | ETH | DOWN | 63 sec | +0.055% | 1¢ | ❌ Lost | -$0.15 |
| 10/25 3:58:10 AM | HYPE | DOWN | 1.8 min | +0.119% | 1¢ | ❌ Lost | -$0.15 |
| 10/25 3:57:54 AM | ZEC | DOWN | 2.1 min | +0.287% | 0¢ | ❌ Lost | -$0.15 |
| 10/25 3:56:33 AM | BTC | DOWN | 3.5 min | +0.095% | 1¢ | ❌ Lost | -$0.15 |
| 10/25 3:56:17 AM | BNB | DOWN | 3.7 min | +0.126% | 1¢ | ❌ Lost | -$0.15 |
| 10/25 3:55:27 AM | DOGE | DOWN | 4.5 min | +0.185% | 1¢ | ❌ Lost | -$0.15 |
| 10/25 3:55:11 AM | XRP | DOWN | 4.8 min | +0.209% | 1¢ | ❌ Lost | -$0.15 |
| 10/25 3:54:38 AM | SOL | DOWN | 5.3 min | +0.234% | 1¢ | ❌ Lost | -$0.15 |
| 10/25 3:44:59 AM | NEAR | UP | 1 sec | -0.039% | 0¢ | ❌ Lost | -$0.15 |
| 10/25 3:44:59 AM | XRP | DOWN | 1 sec | +0.015% | 0¢ | ❌ Lost | $0.00 |
| 10/25 3:44:27 AM | ZEC | DOWN | 33 sec | +0.055% | 0¢ | ❌ Lost | $0.00 |
| 10/25 3:44:27 AM | BNB | UP | 33 sec | -0.001% | 0¢ | ❌ Lost | -$0.15 |
| 10/25 3:44:27 AM | SOL | DOWN | 33 sec | +0.055% | 0¢ | ❌ Lost | $0.00 |
| 10/25 3:44:12 AM | HYPE | DOWN | 47 sec | +0.058% | 0¢ | ❌ Lost | -$0.15 |
| 10/25 3:44:12 AM | ETH | DOWN | 47 sec | +0.034% | 1¢ | ❌ Lost | -$0.15 |
| 10/25 3:43:24 AM | DOGE | DOWN | 1.6 min | +0.127% | 0¢ | ❌ Lost | $0.00 |
| 10/25 3:42:35 AM | BTC | DOWN | 2.4 min | +0.095% | 1¢ | ❌ Lost | -$0.15 |
| 10/25 3:29:45 AM | SOL | DOWN | 15 sec | +0.021% | 0¢ | ❌ Lost | $0.00 |
| 10/25 3:29:29 AM | DOGE | DOWN | 31 sec | +0.038% | 0¢ | ❌ Lost | $0.00 |
| 10/25 3:28:40 AM | XRP | UP | 80 sec | -0.178% | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
