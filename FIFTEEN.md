# 15-Minute 1¢ Study

*Updated Sun Oct 25, 7:58 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 2706 finished bets | 1% | $84.35 | +27% | +3.12¢ | $33.65 / $50.70 |

*Expect about **97 buys a day** (~$14.60/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 2500 | $59.25 | +21% |
| Volatility model ≥ 2%, hold to the close | 4999 | -$10.90 | -2% |
| Momentum model ≥ 2%, hold to the close | 4159 | -$25.95 | -5% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 32001 | 31982 | 120 (0%) | 1.07% | -$2,205.45 (-57%) | Hold to the close: -$2,205.45 (-57%) |

*In play or awaiting result: 18. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 20655 | 4.6% | 0.4% (85) | -655% | ❌ Worse |
| Momentum model | 20655 | 4.6% | 0.4% (85) | -680% | ❌ Worse |
| Mean-reversion model | 20655 | 7.9% | 0.4% (85) | -794% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 20655 | 85 | -48% | -88% | -87% | -85% |
| Volatility model ≥ 2% | 4999 | 43 | -2% | -78% | -77% | -74% |
| Volatility model ≥ 5% | 2706 | 28 | +27% | -75% | -73% | -70% |
| Volatility model ≥ 10% | 1532 | 18 | +64% | -66% | -65% | -61% |
| Momentum model ≥ 2% | 4159 | 33 | -5% | -80% | -80% | -77% |
| Momentum model ≥ 5% | 2500 | 24 | +21% | -77% | -76% | -72% |
| Momentum model ≥ 10% | 1631 | 16 | +34% | -71% | -70% | -65% |
| Mean-reversion model ≥ 2% | 8327 | 56 | -27% | -83% | -83% | -80% |
| Mean-reversion model ≥ 5% | 5836 | 47 | -11% | -81% | -80% | -78% |
| Mean-reversion model ≥ 10% | 3887 | 33 | -4% | -78% | -78% | -76% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 20855 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 7416 | 2% | 2% | 1% | 1% | 0% | 0% |
| Financials | 3711 | 2% | 1% | 1% | 1% | 0% | 0% |
| **All** | 31982 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 120 | 0% | -$2,205.45 | -57% | — |
| Sell at 2¢ | 1190 | 4% | -$3,408.05 | -88% | 47 sec |
| Sell at 3¢ | 817 | 3% | -$3,398.82 | -87% | 48 sec |
| Sell at 5¢ | 570 | 2% | -$3,346.95 | -86% | 61 sec |
| Sell at 10¢ | 352 | 1% | -$3,214.33 | -83% | 65 sec |
| Sell at 25¢ | 191 | 1% | -$2,973.24 | -77% | 82 sec |
| Sell at 50¢ | 122 | 0% | -$2,697.95 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 1406 | 7 | 11% | 4% | -53% | -81% | -83% |
| 2–5 min | 10247 | 55 | 7% | 3% | -47% | -87% | -87% |
| 1–2 min | 8089 | 30 | 3% | 1% | -59% | -92% | -91% |
| Under 1 min | 12236 | 28 | 1% | 0% | -67% | -86% | -86% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 2336 | 12 | 5% | 2% | -35% | -89% | -89% |
| HYPE | 2330 | 8 | 5% | 3% | -58% | -89% | -87% |
| BNB | 2326 | 13 | 5% | 3% | -31% | -84% | -83% |
| SOL | 2322 | 6 | 3% | 2% | -68% | -92% | -92% |
| ETH | 2318 | 11 | 6% | 3% | -43% | -86% | -85% |
| DOGE | 2311 | 4 | 4% | 2% | -78% | -91% | -90% |
| NEAR | 2307 | 12 | 5% | 2% | -32% | -81% | -81% |
| XRP | 2307 | 9 | 3% | 1% | -52% | -89% | -88% |
| BTC | 2298 | 12 | 5% | 2% | -30% | -88% | -89% |
| GOLD | 1200 | 4 | 4% | 2% | -60% | -81% | -83% |
| SILVER | 1166 | 5 | 4% | 2% | -50% | -82% | -82% |
| WTI | 1150 | 3 | 3% | 1% | -69% | -94% | -95% |
| PLATINUM | 1019 | 0 | 1% | 1% | -100% | -98% | -97% |
| COPPER | 994 | 4 | 1% | 1% | -62% | -69% | -69% |
| EURUSD | 950 | 3 | 2% | 1% | -71% | -86% | -86% |
| NATGAS | 943 | 5 | 2% | 1% | -51% | -87% | -86% |
| PALLADIUM | 905 | 2 | 1% | 0% | -79% | -88% | -88% |
| GBPUSD | 896 | 1 | 2% | 1% | -90% | -96% | -97% |
| USDJPY | 878 | 5 | 1% | 1% | -47% | -98% | -97% |
| AUDUSD | 437 | 0 | 1% | 0% | -100% | -98% | -98% |
| USDCAD | 398 | 0 | 2% | 0% | -100% | -97% | -99% |
| 10YRRATE | 43 | 0 | 0% | 0% | -100% | -100% | -100% |
| 2YRRATE | 40 | 1 | 2% | 0% | +133% | +138% | +133% |
| 30YRRATE | 39 | 0 | 0% | 0% | -100% | -100% | -100% |
| BRENT | 39 | 0 | 0% | 0% | -100% | -100% | -100% |
| 5YRRATE | 30 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 16216 | 66 | 4% | 2% | -53% | -87% | -87% |
| DOWN (bought NO) | 15766 | 54 | 4% | 2% | -61% | -88% | -88% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 3491 | 18 | 2% | 1% | -13% | -80% | -80% |
| 0.05–0.1% | 3593 | 11 | 3% | 2% | -55% | -92% | -92% |
| 0.1–0.2% | 5398 | 20 | 5% | 2% | -54% | -89% | -89% |
| 0.2–0.5% | 6056 | 28 | 6% | 3% | -49% | -87% | -86% |
| Over 0.5% | 2313 | 10 | 7% | 3% | -55% | -87% | -88% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 7904 | 32 | 4% | 2% | -54% | -85% | -85% |
| Morning (6am–12pm) | 7781 | 35 | 4% | 2% | -49% | -88% | -87% |
| Afternoon (12–6pm) | 7607 | 24 | 4% | 2% | -63% | -87% | -88% |
| Evening (6pm–12am) | 8690 | 29 | 3% | 2% | -62% | -90% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,820 |
| Time from buy to best bounce (bounced bets) | 49 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/25 7:58:24 PM | WTI | UP | 1.6 min | — | — | In play | — |
| 10/25 7:57:37 PM | PALLADIUM | DOWN | 2.4 min | — | — | In play | — |
| 10/25 7:57:05 PM | BTC | DOWN | 2.9 min | +0.253% | — | In play | — |
| 10/25 7:56:34 PM | DOGE | DOWN | 3.4 min | +0.514% | — | In play | — |
| 10/25 7:56:34 PM | XRP | DOWN | 3.4 min | +0.514% | — | In play | — |
| 10/25 7:56:18 PM | ETH | DOWN | 3.7 min | +0.468% | — | In play | — |
| 10/25 7:56:18 PM | BNB | DOWN | 3.7 min | +0.303% | — | In play | — |
| 10/25 7:56:02 PM | SOL | DOWN | 4.0 min | +0.486% | — | In play | — |
| 10/25 7:55:46 PM | NEAR | DOWN | 4.2 min | +0.967% | — | In play | — |
| 10/25 7:55:30 PM | HYPE | DOWN | 4.5 min | +0.541% | — | In play | — |
| 10/25 7:55:30 PM | ZEC | DOWN | 4.5 min | +0.896% | — | In play | — |
| 10/25 7:44:48 PM | USDCAD | DOWN | 12 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/25 7:44:48 PM | USDJPY | UP | 12 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/25 7:44:32 PM | GBPUSD | UP | 28 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/25 7:44:32 PM | GOLD | UP | 28 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/25 7:44:32 PM | PALLADIUM | UP | 28 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/25 7:43:44 PM | COPPER | UP | 75 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/25 7:43:12 PM | SILVER | UP | 1.8 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/25 7:42:41 PM | AUDUSD | UP | 2.3 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/25 7:41:04 PM | BTC | UP | 3.9 min | -0.382% | 3¢ | ❌ Lost | -$0.15 |
| 10/25 7:40:32 PM | DOGE | UP | 4.5 min | -0.661% | 2¢ | ❌ Lost | -$0.15 |
| 10/25 7:40:32 PM | SOL | UP | 4.5 min | -0.497% | 2¢ | ❌ Lost | -$0.15 |
| 10/25 7:40:32 PM | ZEC | UP | 4.5 min | -1.076% | 1¢ | ❌ Lost | -$0.15 |
| 10/25 7:40:32 PM | XRP | UP | 4.5 min | -0.619% | 2¢ | ❌ Lost | -$0.15 |
| 10/25 7:40:16 PM | NEAR | UP | 4.7 min | -1.586% | 0¢ | ❌ Lost | -$0.15 |
| 10/25 7:40:00 PM | BNB | UP | 5.0 min | -0.394% | 0¢ | ❌ Lost | -$0.15 |
| 10/25 7:39:46 PM | HYPE | UP | 5.2 min | -0.494% | 1¢ | ❌ Lost | -$0.15 |
| 10/25 7:39:15 PM | ETH | UP | 5.8 min | -0.615% | 2¢ | ❌ Lost | -$0.15 |
| 10/25 7:29:45 PM | DOGE | UP | 14 sec | -0.095% | 0¢ | ❌ Lost | $0.00 |
| 10/25 7:29:45 PM | SOL | UP | 14 sec | -0.026% | 0¢ | ❌ Lost | $0.00 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
