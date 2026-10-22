# 15-Minute 1¢ Study

*Updated Thu Oct 22, 12:28 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 2383 finished bets | 1% | $80.75 | +30% | +3.39¢ | $38.85 / $41.90 |

*Expect about **97 buys a day** (~$14.60/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 2199 | $50.10 | +21% |
| Volatility model ≥ 2%, hold to the close | 4385 | $9.00 | +2% |
| Momentum model ≥ 2%, hold to the close | 3678 | -$27.20 | -6% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 28454 | 28434 | 108 (0%) | 1.07% | -$1,953.90 (-56%) | Hold to the close: -$1,953.90 (-56%) |

*In play or awaiting result: 19. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 18207 | 4.7% | 0.4% (78) | -644% | ❌ Worse |
| Momentum model | 18207 | 4.6% | 0.4% (78) | -670% | ❌ Worse |
| Mean-reversion model | 18207 | 7.9% | 0.4% (78) | -774% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 18207 | 78 | -46% | -87% | -87% | -85% |
| Volatility model ≥ 2% | 4385 | 39 | +2% | -78% | -77% | -73% |
| Volatility model ≥ 5% | 2383 | 25 | +30% | -73% | -72% | -69% |
| Volatility model ≥ 10% | 1356 | 16 | +66% | -63% | -61% | -59% |
| Momentum model ≥ 2% | 3678 | 29 | -6% | -79% | -79% | -76% |
| Momentum model ≥ 5% | 2199 | 21 | +21% | -76% | -75% | -71% |
| Momentum model ≥ 10% | 1444 | 14 | +33% | -69% | -68% | -63% |
| Mean-reversion model ≥ 2% | 7270 | 52 | -22% | -83% | -82% | -79% |
| Mean-reversion model ≥ 5% | 5077 | 43 | -7% | -80% | -79% | -77% |
| Mean-reversion model ≥ 10% | 3377 | 30 | +1% | -78% | -77% | -74% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 18406 | 5% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 6836 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 3192 | 1% | 1% | 1% | 1% | 0% | 0% |
| **All** | 28434 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 108 | 0% | -$1,953.90 | -56% | — |
| Sell at 2¢ | 1040 | 4% | -$3,055.50 | -88% | 47 sec |
| Sell at 3¢ | 711 | 3% | -$3,048.61 | -88% | 48 sec |
| Sell at 5¢ | 499 | 2% | -$3,001.55 | -87% | 61 sec |
| Sell at 10¢ | 307 | 1% | -$2,895.73 | -84% | 64 sec |
| Sell at 25¢ | 170 | 1% | -$2,665.20 | -77% | 86 sec |
| Sell at 50¢ | 112 | 0% | -$2,401.90 | -69% | 1.7 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 1185 | 7 | 11% | 4% | -43% | -81% | -83% |
| 2–5 min | 9154 | 51 | 7% | 3% | -45% | -87% | -87% |
| 1–2 min | 7235 | 27 | 3% | 1% | -59% | -93% | -93% |
| Under 1 min | 10856 | 23 | 1% | 0% | -70% | -86% | -86% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 2063 | 12 | 5% | 2% | -27% | -89% | -89% |
| BNB | 2058 | 12 | 5% | 3% | -28% | -83% | -81% |
| HYPE | 2055 | 8 | 5% | 3% | -52% | -88% | -87% |
| ETH | 2045 | 10 | 6% | 3% | -41% | -86% | -86% |
| SOL | 2045 | 3 | 3% | 2% | -82% | -92% | -92% |
| DOGE | 2042 | 4 | 4% | 2% | -76% | -90% | -90% |
| XRP | 2035 | 7 | 3% | 1% | -58% | -88% | -88% |
| NEAR | 2032 | 12 | 6% | 3% | -23% | -80% | -80% |
| BTC | 2031 | 12 | 5% | 2% | -21% | -88% | -90% |
| GOLD | 1115 | 3 | 3% | 1% | -68% | -82% | -84% |
| SILVER | 1079 | 4 | 3% | 1% | -57% | -82% | -82% |
| WTI | 1057 | 3 | 3% | 1% | -67% | -94% | -95% |
| PLATINUM | 939 | 0 | 1% | 0% | -100% | -99% | -98% |
| COPPER | 931 | 3 | 1% | 1% | -70% | -78% | -77% |
| EURUSD | 867 | 3 | 2% | 1% | -68% | -85% | -85% |
| NATGAS | 865 | 5 | 2% | 1% | -46% | -86% | -85% |
| PALLADIUM | 840 | 2 | 1% | 0% | -78% | -87% | -87% |
| GBPUSD | 814 | 1 | 2% | 1% | -89% | -97% | -96% |
| USDJPY | 785 | 4 | 1% | 1% | -52% | -99% | -98% |
| AUDUSD | 368 | 0 | 0% | 0% | -100% | -100% | -99% |
| USDCAD | 323 | 0 | 1% | 0% | -100% | -99% | -99% |
| 10YRRATE | 13 | 0 | 0% | 0% | -100% | -100% | -100% |
| BRENT | 10 | 0 | 0% | 0% | -100% | -100% | -100% |
| 2YRRATE | 9 | 0 | 0% | 0% | -100% | -100% | -100% |
| 30YRRATE | 9 | 0 | 0% | 0% | -100% | -100% | -100% |
| 5YRRATE | 4 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 14367 | 57 | 4% | 2% | -54% | -88% | -87% |
| DOWN (bought NO) | 14067 | 51 | 3% | 1% | -58% | -89% | -89% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 3053 | 15 | 2% | 1% | -18% | -78% | -78% |
| 0.05–0.1% | 3161 | 11 | 3% | 2% | -49% | -92% | -91% |
| 0.1–0.2% | 4709 | 17 | 5% | 2% | -55% | -89% | -89% |
| 0.2–0.5% | 5395 | 27 | 6% | 3% | -45% | -87% | -87% |
| Over 0.5% | 2084 | 10 | 7% | 3% | -50% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 7128 | 30 | 4% | 2% | -52% | -86% | -85% |
| Morning (6am–12pm) | 7002 | 33 | 4% | 2% | -46% | -88% | -87% |
| Afternoon (12–6pm) | 6562 | 20 | 4% | 2% | -64% | -89% | -89% |
| Evening (6pm–12am) | 7742 | 25 | 3% | 2% | -63% | -90% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,684 |
| Time from buy to best bounce (bounced bets) | 49 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/22 12:27:59 PM | USDJPY | UP | 2.0 min | — | — | In play | — |
| 10/22 12:27:26 PM | 5YRRATE | UP | 2.6 min | — | — | In play | — |
| 10/22 12:27:10 PM | 2YRRATE | UP | 2.8 min | — | — | In play | — |
| 10/22 12:27:10 PM | 10YRRATE | UP | 2.8 min | — | — | In play | — |
| 10/22 12:26:55 PM | WTI | UP | 3.1 min | — | — | In play | — |
| 10/22 12:26:55 PM | DOGE | DOWN | 3.1 min | +0.303% | — | In play | — |
| 10/22 12:26:40 PM | 30YRRATE | UP | 3.3 min | — | — | In play | — |
| 10/22 12:26:40 PM | ETH | DOWN | 3.3 min | +0.171% | — | In play | — |
| 10/22 12:25:51 PM | BNB | DOWN | 4.1 min | +0.164% | — | In play | — |
| 10/22 12:25:36 PM | NATGAS | UP | 4.4 min | — | — | In play | — |
| 10/22 12:24:33 PM | HYPE | DOWN | 5.5 min | +0.515% | — | In play | — |
| 10/22 12:21:23 PM | ZEC | DOWN | 8.6 min | +0.938% | — | In play | — |
| 10/22 12:14:45 PM | 30YRRATE | DOWN | 14 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/22 12:14:45 PM | HYPE | UP | 14 sec | -0.027% | 0¢ | ❌ Lost | $0.00 |
| 10/22 12:14:29 PM | BNB | UP | 30 sec | -0.036% | 1¢ | ❌ Lost | -$0.15 |
| 10/22 12:14:13 PM | ZEC | UP | 46 sec | -0.114% | 1¢ | ❌ Lost | -$0.15 |
| 10/22 12:14:13 PM | ETH | UP | 46 sec | -0.119% | 0¢ | ❌ Lost | $0.00 |
| 10/22 12:14:13 PM | WTI | UP | 46 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/22 12:13:57 PM | DOGE | UP | 62 sec | -0.174% | 1¢ | ❌ Lost | -$0.15 |
| 10/22 12:13:42 PM | BTC | UP | 77 sec | -0.088% | 1¢ | ❌ Lost | -$0.15 |
| 10/22 12:13:42 PM | SOL | UP | 77 sec | -0.216% | 0¢ | ❌ Lost | $0.00 |
| 10/22 12:13:26 PM | NATGAS | UP | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/22 12:12:54 PM | NEAR | UP | 2.1 min | -0.400% | 1¢ | ❌ Lost | -$0.15 |
| 10/22 12:12:23 PM | 10YRRATE | DOWN | 2.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/22 12:12:23 PM | GBPUSD | UP | 2.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/22 12:12:23 PM | AUDUSD | UP | 2.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/22 12:12:23 PM | USDJPY | DOWN | 2.6 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/22 12:12:07 PM | 2YRRATE | DOWN | 2.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/22 12:12:07 PM | 5YRRATE | DOWN | 2.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/22 12:10:31 PM | XRP | UP | 4.5 min | -0.451% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
