# 15-Minute 1¢ Study

*Updated Tue Oct 27, 2:48 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 2821 finished bets | 1% | $73.10 | +23% | +2.59¢ | $68.45 / $4.65 |

*Expect about **97 buys a day** (~$14.55/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 2631 | $46.05 | +16% |
| Volatility model ≥ 2%, hold to the close | 5245 | -$25.25 | -4% |
| Momentum model ≥ 2%, hold to the close | 4361 | -$47.55 | -9% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 34211 | 34203 | 126 (0%) | 1.07% | -$2,397.00 (-58%) | Hold to the close: -$2,397.00 (-58%) |

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
| Volatility model | 21733 | 4.6% | 0.4% (86) | -674% | ❌ Worse |
| Momentum model | 21733 | 4.6% | 0.4% (86) | -699% | ❌ Worse |
| Mean-reversion model | 21733 | 8.0% | 0.4% (86) | -818% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 21733 | 86 | -50% | -88% | -87% | -85% |
| Volatility model ≥ 2% | 5245 | 44 | -4% | -78% | -77% | -74% |
| Volatility model ≥ 5% | 2821 | 28 | +23% | -75% | -74% | -70% |
| Volatility model ≥ 10% | 1603 | 18 | +58% | -67% | -65% | -63% |
| Momentum model ≥ 2% | 4361 | 33 | -9% | -80% | -80% | -77% |
| Momentum model ≥ 5% | 2631 | 24 | +16% | -77% | -77% | -73% |
| Momentum model ≥ 10% | 1718 | 16 | +28% | -72% | -71% | -67% |
| Mean-reversion model ≥ 2% | 8802 | 57 | -29% | -83% | -83% | -81% |
| Mean-reversion model ≥ 5% | 6163 | 47 | -16% | -81% | -80% | -78% |
| Mean-reversion model ≥ 10% | 4108 | 33 | -9% | -79% | -78% | -76% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 21933 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 8055 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 4215 | 2% | 1% | 1% | 1% | 0% | 0% |
| **All** | 34203 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 126 | 0% | -$2,397.00 | -58% | — |
| Sell at 2¢ | 1282 | 4% | -$3,659.68 | -88% | 47 sec |
| Sell at 3¢ | 877 | 3% | -$3,650.97 | -88% | 48 sec |
| Sell at 5¢ | 607 | 2% | -$3,598.45 | -86% | 62 sec |
| Sell at 10¢ | 374 | 1% | -$3,447.06 | -83% | 65 sec |
| Sell at 25¢ | 200 | 1% | -$3,191.00 | -77% | 83 sec |
| Sell at 50¢ | 130 | 0% | -$2,891.50 | -69% | 1.7 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 1499 | 8 | 11% | 4% | -49% | -81% | -82% |
| 2–5 min | 10975 | 58 | 7% | 3% | -48% | -87% | -87% |
| 1–2 min | 8668 | 31 | 3% | 1% | -61% | -92% | -92% |
| Under 1 min | 13057 | 29 | 1% | 0% | -68% | -87% | -87% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 2457 | 12 | 5% | 2% | -38% | -89% | -88% |
| HYPE | 2449 | 8 | 5% | 3% | -60% | -88% | -86% |
| BNB | 2447 | 13 | 5% | 2% | -34% | -84% | -83% |
| SOL | 2443 | 6 | 4% | 2% | -69% | -92% | -92% |
| ETH | 2437 | 11 | 6% | 3% | -46% | -86% | -85% |
| DOGE | 2432 | 5 | 4% | 2% | -74% | -90% | -90% |
| NEAR | 2425 | 12 | 5% | 2% | -36% | -82% | -82% |
| XRP | 2424 | 9 | 3% | 1% | -54% | -89% | -89% |
| BTC | 2419 | 12 | 5% | 2% | -33% | -88% | -89% |
| GOLD | 1290 | 5 | 4% | 2% | -54% | -81% | -83% |
| SILVER | 1255 | 6 | 4% | 2% | -44% | -82% | -82% |
| WTI | 1234 | 3 | 3% | 1% | -71% | -94% | -95% |
| PLATINUM | 1105 | 0 | 2% | 1% | -100% | -97% | -97% |
| COPPER | 1066 | 4 | 1% | 1% | -65% | -71% | -71% |
| EURUSD | 1036 | 3 | 2% | 1% | -73% | -87% | -87% |
| NATGAS | 1024 | 5 | 2% | 1% | -54% | -87% | -87% |
| PALLADIUM | 985 | 2 | 1% | 0% | -81% | -89% | -89% |
| GBPUSD | 976 | 1 | 2% | 1% | -90% | -96% | -97% |
| USDJPY | 961 | 5 | 1% | 1% | -51% | -98% | -97% |
| AUDUSD | 520 | 2 | 1% | 1% | -64% | -98% | -96% |
| USDCAD | 479 | 0 | 1% | 0% | -100% | -98% | -99% |
| BRENT | 96 | 0 | 0% | 0% | -100% | -100% | -100% |
| 10YRRATE | 67 | 0 | 3% | 0% | -100% | -95% | -96% |
| 2YRRATE | 60 | 1 | 3% | 0% | +56% | +61% | +60% |
| 30YRRATE | 60 | 0 | 0% | 0% | -100% | -100% | -100% |
| 5YRRATE | 56 | 1 | 4% | 4% | +67% | -94% | -91% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 17358 | 69 | 4% | 2% | -54% | -88% | -87% |
| DOWN (bought NO) | 16845 | 57 | 4% | 2% | -61% | -88% | -89% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 3616 | 18 | 2% | 1% | -15% | -81% | -80% |
| 0.05–0.1% | 3759 | 12 | 3% | 2% | -53% | -92% | -92% |
| 0.1–0.2% | 5684 | 20 | 5% | 2% | -56% | -89% | -89% |
| 0.2–0.5% | 6457 | 28 | 6% | 3% | -52% | -87% | -86% |
| Over 0.5% | 2413 | 10 | 7% | 3% | -57% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 8517 | 33 | 4% | 2% | -56% | -85% | -85% |
| Morning (6am–12pm) | 8268 | 37 | 4% | 2% | -49% | -88% | -88% |
| Afternoon (12–6pm) | 8019 | 25 | 4% | 2% | -63% | -88% | -88% |
| Evening (6pm–12am) | 9399 | 31 | 3% | 2% | -62% | -90% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,697 |
| Time from buy to best bounce (bounced bets) | 50 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/27 2:44:56 AM | AUDUSD | DOWN | 3 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 2:44:56 AM | USDJPY | DOWN | 3 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 2:44:56 AM | BRENT | DOWN | 3 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 2:44:56 AM | GBPUSD | UP | 3 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 2:44:40 AM | PALLADIUM | UP | 19 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 2:44:40 AM | 5YRRATE | UP | 19 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 2:44:40 AM | BTC | UP | 19 sec | -0.034% | 0¢ | ❌ Lost | $0.00 |
| 10/27 2:44:40 AM | COPPER | UP | 19 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 2:44:24 AM | DOGE | DOWN | 35 sec | -0.008% | 1¢ | ❌ Lost | -$0.15 |
| 10/27 2:44:24 AM | SOL | UP | 35 sec | -0.045% | 0¢ | ❌ Lost | -$0.15 |
| 10/27 2:43:53 AM | WTI | DOWN | 67 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/27 2:43:53 AM | GOLD | UP | 67 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/27 2:43:53 AM | XRP | UP | 67 sec | -0.154% | 0¢ | ❌ Lost | $0.00 |
| 10/27 2:43:53 AM | ZEC | UP | 67 sec | -0.292% | 0¢ | ❌ Lost | $0.00 |
| 10/27 2:43:37 AM | USDCAD | UP | 83 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 2:43:37 AM | BNB | UP | 83 sec | -0.098% | 1¢ | ❌ Lost | -$0.15 |
| 10/27 2:43:05 AM | SILVER | UP | 1.9 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/27 2:43:05 AM | NATGAS | UP | 1.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 2:42:49 AM | HYPE | UP | 2.2 min | -0.251% | 1¢ | ❌ Lost | -$0.15 |
| 10/27 2:42:33 AM | ETH | UP | 2.4 min | -0.136% | 2¢ | ❌ Lost | -$0.15 |
| 10/27 2:36:00 AM | NEAR | UP | 9.0 min | -0.361% | 59¢ | ❌ Lost | -$0.15 |
| 10/27 2:28:59 AM | EURUSD | UP | 61 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 2:28:59 AM | XRP | UP | 61 sec | -0.138% | 0¢ | ❌ Lost | $0.00 |
| 10/27 2:28:59 AM | ZEC | UP | 61 sec | -0.239% | 1¢ | ❌ Lost | -$0.15 |
| 10/27 2:28:43 AM | USDCAD | UP | 76 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 2:28:27 AM | PALLADIUM | UP | 1.5 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 2:28:27 AM | BRENT | DOWN | 1.5 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/27 2:28:27 AM | SOL | UP | 1.5 min | -0.205% | 0¢ | ❌ Lost | $0.00 |
| 10/27 2:28:27 AM | ETH | UP | 1.5 min | -0.159% | 0¢ | ❌ Lost | -$0.15 |
| 10/27 2:28:27 AM | 30YRRATE | DOWN | 1.5 min | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
