# 15-Minute 1¢ Study

*Updated Thu Oct 22, 7:02 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 2410 finished bets | 1% | $77.15 | +28% | +3.20¢ | $37.05 / $40.10 |

*Expect about **97 buys a day** (~$14.60/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 2226 | $46.95 | +19% |
| Volatility model ≥ 2%, hold to the close | 4451 | $0.15 | +0% |
| Momentum model ≥ 2%, hold to the close | 3718 | -$32.15 | -7% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 28899 | 28891 | 110 (0%) | 1.07% | -$1,982.45 (-56%) | Hold to the close: -$1,982.45 (-56%) |

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
| Volatility model | 18445 | 4.7% | 0.4% (79) | -642% | ❌ Worse |
| Momentum model | 18445 | 4.6% | 0.4% (79) | -666% | ❌ Worse |
| Mean-reversion model | 18445 | 7.9% | 0.4% (79) | -773% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 18445 | 79 | -46% | -87% | -87% | -85% |
| Volatility model ≥ 2% | 4451 | 39 | +0% | -78% | -77% | -73% |
| Volatility model ≥ 5% | 2410 | 25 | +28% | -73% | -72% | -69% |
| Volatility model ≥ 10% | 1370 | 16 | +64% | -63% | -62% | -59% |
| Momentum model ≥ 2% | 3718 | 29 | -7% | -79% | -79% | -76% |
| Momentum model ≥ 5% | 2226 | 21 | +19% | -76% | -75% | -71% |
| Momentum model ≥ 10% | 1465 | 14 | +31% | -69% | -68% | -64% |
| Mean-reversion model ≥ 2% | 7379 | 52 | -23% | -83% | -82% | -80% |
| Mean-reversion model ≥ 5% | 5163 | 43 | -8% | -80% | -80% | -77% |
| Mean-reversion model ≥ 10% | 3434 | 30 | -1% | -78% | -77% | -75% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 18644 | 5% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 6943 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 3304 | 1% | 1% | 1% | 1% | 0% | 0% |
| **All** | 28891 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 110 | 0% | -$1,982.45 | -56% | — |
| Sell at 2¢ | 1065 | 4% | -$3,105.55 | -88% | 47 sec |
| Sell at 3¢ | 726 | 3% | -$3,099.31 | -88% | 48 sec |
| Sell at 5¢ | 511 | 2% | -$3,050.30 | -87% | 61 sec |
| Sell at 10¢ | 313 | 1% | -$2,944.42 | -84% | 64 sec |
| Sell at 25¢ | 173 | 1% | -$2,711.82 | -77% | 82 sec |
| Sell at 50¢ | 114 | 0% | -$2,444.95 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 1215 | 7 | 11% | 4% | -45% | -80% | -83% |
| 2–5 min | 9296 | 52 | 7% | 3% | -45% | -87% | -87% |
| 1–2 min | 7338 | 28 | 3% | 1% | -58% | -93% | -93% |
| Under 1 min | 11038 | 23 | 1% | 0% | -70% | -86% | -86% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 2090 | 12 | 5% | 2% | -28% | -89% | -89% |
| BNB | 2083 | 12 | 5% | 3% | -29% | -83% | -82% |
| HYPE | 2081 | 8 | 5% | 3% | -53% | -89% | -87% |
| ETH | 2072 | 10 | 6% | 3% | -42% | -86% | -85% |
| SOL | 2072 | 3 | 3% | 1% | -82% | -92% | -92% |
| DOGE | 2068 | 4 | 4% | 2% | -76% | -90% | -89% |
| XRP | 2063 | 8 | 3% | 1% | -52% | -88% | -88% |
| NEAR | 2059 | 12 | 6% | 3% | -24% | -80% | -80% |
| BTC | 2056 | 12 | 5% | 2% | -22% | -88% | -90% |
| GOLD | 1135 | 3 | 4% | 1% | -69% | -82% | -83% |
| SILVER | 1096 | 5 | 3% | 1% | -47% | -82% | -82% |
| WTI | 1075 | 3 | 3% | 1% | -67% | -94% | -95% |
| PLATINUM | 954 | 0 | 1% | 1% | -100% | -99% | -98% |
| COPPER | 941 | 3 | 1% | 1% | -70% | -78% | -77% |
| EURUSD | 884 | 3 | 2% | 1% | -68% | -86% | -86% |
| NATGAS | 878 | 5 | 2% | 1% | -47% | -86% | -85% |
| PALLADIUM | 851 | 2 | 1% | 0% | -78% | -87% | -88% |
| GBPUSD | 833 | 1 | 2% | 1% | -89% | -97% | -97% |
| USDJPY | 804 | 4 | 1% | 1% | -54% | -99% | -98% |
| AUDUSD | 378 | 0 | 0% | 0% | -100% | -100% | -99% |
| USDCAD | 337 | 0 | 1% | 0% | -100% | -98% | -99% |
| 10YRRATE | 21 | 0 | 0% | 0% | -100% | -100% | -100% |
| 2YRRATE | 18 | 0 | 0% | 0% | -100% | -100% | -100% |
| 30YRRATE | 18 | 0 | 0% | 0% | -100% | -100% | -100% |
| BRENT | 13 | 0 | 0% | 0% | -100% | -100% | -100% |
| 5YRRATE | 11 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 14586 | 59 | 4% | 2% | -54% | -88% | -87% |
| DOWN (bought NO) | 14305 | 51 | 3% | 1% | -59% | -89% | -89% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 3095 | 15 | 2% | 1% | -19% | -79% | -78% |
| 0.05–0.1% | 3201 | 11 | 3% | 2% | -50% | -92% | -91% |
| 0.1–0.2% | 4783 | 17 | 5% | 2% | -56% | -89% | -89% |
| 0.2–0.5% | 5456 | 28 | 6% | 3% | -44% | -87% | -87% |
| Over 0.5% | 2105 | 10 | 7% | 3% | -51% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 7128 | 30 | 4% | 2% | -52% | -86% | -85% |
| Morning (6am–12pm) | 7002 | 33 | 4% | 2% | -46% | -88% | -87% |
| Afternoon (12–6pm) | 6955 | 21 | 4% | 2% | -64% | -89% | -89% |
| Evening (6pm–12am) | 7806 | 26 | 3% | 2% | -62% | -90% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,681 |
| Time from buy to best bounce (bounced bets) | 49 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/22 6:59:13 PM | ETH | DOWN | 46 sec | +0.045% | 0¢ | ❌ Lost | -$0.15 |
| 10/22 6:58:57 PM | GBPUSD | UP | 62 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/22 6:58:42 PM | SOL | DOWN | 78 sec | +0.093% | 1¢ | ❌ Lost | $0.00 |
| 10/22 6:58:42 PM | NEAR | DOWN | 78 sec | +0.141% | 0¢ | ❌ Lost | -$0.15 |
| 10/22 6:58:26 PM | SILVER | DOWN | 1.6 min | — | 0¢ | ❌ Lost | $0.00 |
| 10/22 6:58:10 PM | PALLADIUM | DOWN | 1.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/22 6:58:10 PM | EURUSD | UP | 1.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/22 6:58:10 PM | DOGE | DOWN | 1.8 min | +0.156% | 0¢ | ❌ Lost | $0.00 |
| 10/22 6:57:54 PM | USDCAD | DOWN | 2.1 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/22 6:57:38 PM | USDJPY | DOWN | 2.4 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/22 6:56:50 PM | HYPE | DOWN | 3.1 min | +0.194% | 1¢ | ❌ Lost | -$0.15 |
| 10/22 6:56:19 PM | XRP | DOWN | 3.7 min | +0.176% | 1¢ | ❌ Lost | -$0.15 |
| 10/22 6:55:47 PM | BNB | DOWN | 4.2 min | +0.097% | 3¢ | ❌ Lost | -$0.15 |
| 10/22 6:55:47 PM | PLATINUM | DOWN | 4.2 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/22 6:54:59 PM | GOLD | DOWN | 5.0 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/22 6:54:27 PM | ZEC | DOWN | 5.5 min | +0.457% | 6¢ | ❌ Lost | -$0.15 |
| 10/22 6:44:47 PM | GBPUSD | DOWN | 12 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/22 6:44:31 PM | PLATINUM | DOWN | 28 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/22 6:44:17 PM | AUDUSD | DOWN | 42 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/22 6:44:17 PM | HYPE | DOWN | 42 sec | +0.134% | 0¢ | ❌ Lost | $0.00 |
| 10/22 6:44:17 PM | DOGE | DOWN | 42 sec | +0.116% | 0¢ | ❌ Lost | $0.00 |
| 10/22 6:44:01 PM | ZEC | DOWN | 59 sec | +0.298% | 0¢ | ❌ Lost | $0.00 |
| 10/22 6:44:01 PM | NEAR | DOWN | 59 sec | +0.404% | 0¢ | ❌ Lost | $0.00 |
| 10/22 6:44:01 PM | WTI | DOWN | 59 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/22 6:43:42 PM | SILVER | DOWN | 77 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/22 6:43:26 PM | BNB | DOWN | 1.6 min | +0.078% | 0¢ | ❌ Lost | $0.00 |
| 10/22 6:43:26 PM | SOL | DOWN | 1.6 min | +0.104% | 0¢ | ❌ Lost | -$0.15 |
| 10/22 6:42:25 PM | XRP | DOWN | 2.6 min | +0.145% | 1¢ | ❌ Lost | -$0.15 |
| 10/22 6:41:32 PM | BTC | DOWN | 3.5 min | +0.192% | 1¢ | ❌ Lost | -$0.15 |
| 10/22 6:40:45 PM | ETH | DOWN | 4.2 min | +0.259% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
