# 15-Minute 1¢ Study

*Updated Sun Oct 25, 8:19 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 2706 finished bets | 1% | $84.35 | +27% | +3.12¢ | $33.65 / $50.70 |

*Expect about **97 buys a day** (~$14.59/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 2502 | $59.10 | +21% |
| Volatility model ≥ 2%, hold to the close | 5001 | -$11.05 | -2% |
| Momentum model ≥ 2%, hold to the close | 4162 | -$26.10 | -5% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 32028 | 32020 | 120 (0%) | 1.07% | -$2,210.25 (-57%) | Hold to the close: -$2,210.25 (-57%) |

*In play or awaiting result: 7. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 20673 | 4.6% | 0.4% (85) | -655% | ❌ Worse |
| Momentum model | 20673 | 4.5% | 0.4% (85) | -680% | ❌ Worse |
| Mean-reversion model | 20673 | 7.9% | 0.4% (85) | -794% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 20673 | 85 | -48% | -88% | -87% | -85% |
| Volatility model ≥ 2% | 5001 | 43 | -2% | -78% | -77% | -74% |
| Volatility model ≥ 5% | 2706 | 28 | +27% | -75% | -73% | -70% |
| Volatility model ≥ 10% | 1532 | 18 | +64% | -66% | -65% | -61% |
| Momentum model ≥ 2% | 4162 | 33 | -5% | -80% | -80% | -77% |
| Momentum model ≥ 5% | 2502 | 24 | +21% | -77% | -76% | -72% |
| Momentum model ≥ 10% | 1632 | 16 | +34% | -71% | -70% | -65% |
| Mean-reversion model ≥ 2% | 8336 | 56 | -27% | -83% | -83% | -80% |
| Mean-reversion model ≥ 5% | 5843 | 47 | -12% | -81% | -80% | -78% |
| Mean-reversion model ≥ 10% | 3891 | 33 | -4% | -78% | -78% | -76% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 20873 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 7429 | 2% | 2% | 1% | 1% | 0% | 0% |
| Financials | 3718 | 2% | 1% | 1% | 1% | 0% | 0% |
| **All** | 32020 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 120 | 0% | -$2,210.25 | -57% | — |
| Sell at 2¢ | 1190 | 4% | -$3,412.85 | -88% | 47 sec |
| Sell at 3¢ | 817 | 3% | -$3,403.62 | -87% | 48 sec |
| Sell at 5¢ | 570 | 2% | -$3,351.75 | -86% | 61 sec |
| Sell at 10¢ | 352 | 1% | -$3,219.13 | -83% | 65 sec |
| Sell at 25¢ | 191 | 1% | -$2,978.04 | -77% | 82 sec |
| Sell at 50¢ | 122 | 0% | -$2,702.75 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 1406 | 7 | 11% | 4% | -53% | -81% | -83% |
| 2–5 min | 10258 | 55 | 7% | 3% | -47% | -87% | -87% |
| 1–2 min | 8094 | 30 | 3% | 1% | -59% | -92% | -91% |
| Under 1 min | 12258 | 28 | 1% | 0% | -67% | -86% | -86% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 2338 | 12 | 5% | 2% | -35% | -89% | -89% |
| HYPE | 2332 | 8 | 5% | 3% | -58% | -89% | -87% |
| BNB | 2328 | 13 | 5% | 3% | -31% | -84% | -83% |
| SOL | 2324 | 6 | 3% | 2% | -68% | -92% | -92% |
| ETH | 2320 | 11 | 6% | 3% | -43% | -86% | -85% |
| DOGE | 2313 | 4 | 4% | 2% | -78% | -91% | -90% |
| NEAR | 2309 | 12 | 5% | 2% | -32% | -82% | -81% |
| XRP | 2309 | 9 | 3% | 1% | -52% | -89% | -88% |
| BTC | 2300 | 12 | 5% | 2% | -30% | -88% | -89% |
| GOLD | 1202 | 4 | 4% | 1% | -61% | -81% | -83% |
| SILVER | 1168 | 5 | 4% | 2% | -50% | -82% | -82% |
| WTI | 1151 | 3 | 3% | 1% | -69% | -94% | -95% |
| PLATINUM | 1021 | 0 | 1% | 1% | -100% | -98% | -97% |
| COPPER | 996 | 4 | 1% | 1% | -63% | -69% | -69% |
| EURUSD | 952 | 3 | 2% | 1% | -71% | -86% | -86% |
| NATGAS | 945 | 5 | 2% | 1% | -51% | -87% | -86% |
| PALLADIUM | 907 | 2 | 1% | 0% | -79% | -88% | -88% |
| GBPUSD | 898 | 1 | 2% | 1% | -90% | -96% | -97% |
| USDJPY | 879 | 5 | 1% | 1% | -47% | -98% | -97% |
| AUDUSD | 437 | 0 | 1% | 0% | -100% | -98% | -98% |
| USDCAD | 400 | 0 | 2% | 0% | -100% | -97% | -99% |
| 10YRRATE | 43 | 0 | 0% | 0% | -100% | -100% | -100% |
| 2YRRATE | 40 | 1 | 2% | 0% | +133% | +138% | +133% |
| 30YRRATE | 39 | 0 | 0% | 0% | -100% | -100% | -100% |
| BRENT | 39 | 0 | 0% | 0% | -100% | -100% | -100% |
| 5YRRATE | 30 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 16227 | 66 | 4% | 2% | -53% | -87% | -87% |
| DOWN (bought NO) | 15793 | 54 | 4% | 2% | -61% | -88% | -88% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 3494 | 18 | 2% | 1% | -13% | -80% | -80% |
| 0.05–0.1% | 3595 | 11 | 3% | 2% | -55% | -92% | -92% |
| 0.1–0.2% | 5401 | 20 | 5% | 2% | -54% | -89% | -89% |
| 0.2–0.5% | 6061 | 28 | 6% | 3% | -49% | -87% | -86% |
| Over 0.5% | 2318 | 10 | 7% | 3% | -56% | -87% | -88% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 7904 | 32 | 4% | 2% | -54% | -85% | -85% |
| Morning (6am–12pm) | 7781 | 35 | 4% | 2% | -49% | -88% | -87% |
| Afternoon (12–6pm) | 7607 | 24 | 4% | 2% | -63% | -87% | -88% |
| Evening (6pm–12am) | 8728 | 29 | 3% | 2% | -62% | -90% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,821 |
| Time from buy to best bounce (bounced bets) | 50 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/25 8:14:52 PM | PLATINUM | UP | 7 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/25 8:14:52 PM | USDCAD | UP | 7 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/25 8:14:52 PM | COPPER | UP | 7 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/25 8:14:37 PM | SOL | DOWN | 22 sec | +0.027% | 0¢ | ❌ Lost | -$0.15 |
| 10/25 8:14:37 PM | GBPUSD | DOWN | 22 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/25 8:14:37 PM | EURUSD | DOWN | 22 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/25 8:14:37 PM | ETH | UP | 22 sec | -0.049% | 1¢ | ❌ Lost | -$0.15 |
| 10/25 8:14:37 PM | BNB | DOWN | 22 sec | +0.029% | 0¢ | ❌ Lost | $0.00 |
| 10/25 8:14:37 PM | XRP | DOWN | 22 sec | +0.054% | 0¢ | ❌ Lost | -$0.15 |
| 10/25 8:14:21 PM | DOGE | DOWN | 38 sec | +0.063% | 0¢ | ❌ Lost | $0.00 |
| 10/25 8:14:21 PM | ZEC | UP | 38 sec | -0.127% | 0¢ | ❌ Lost | $0.00 |
| 10/25 8:14:21 PM | PALLADIUM | DOWN | 38 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/25 8:14:05 PM | NEAR | UP | 54 sec | -0.366% | 0¢ | ❌ Lost | -$0.15 |
| 10/25 8:14:05 PM | HYPE | UP | 54 sec | -0.160% | 0¢ | ❌ Lost | $0.00 |
| 10/25 8:13:49 PM | NATGAS | DOWN | 71 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/25 8:13:49 PM | USDJPY | UP | 71 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/25 8:13:32 PM | GOLD | DOWN | 88 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/25 8:13:32 PM | SILVER | DOWN | 88 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/25 8:12:45 PM | BTC | DOWN | 2.2 min | +0.161% | 1¢ | ❌ Lost | -$0.15 |
| 10/25 7:59:59 PM | GBPUSD | DOWN | 1 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/25 7:59:59 PM | EURUSD | DOWN | 1 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/25 7:59:59 PM | GOLD | DOWN | 1 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/25 7:59:59 PM | COPPER | UP | 1 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/25 7:59:59 PM | NATGAS | UP | 1 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/25 7:59:43 PM | PLATINUM | DOWN | 16 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/25 7:59:27 PM | SILVER | DOWN | 32 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/25 7:59:27 PM | USDCAD | DOWN | 32 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/25 7:58:24 PM | WTI | UP | 1.6 min | — | 0¢ | ❌ Lost | $0.00 |
| 10/25 7:57:37 PM | PALLADIUM | DOWN | 2.4 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/25 7:57:05 PM | BTC | DOWN | 2.9 min | +0.253% | 2¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
