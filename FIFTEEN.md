# 15-Minute 1¢ Study

*Updated Thu Nov 26, 9:36 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 4975 finished bets | 1% | $201.70 | +37% | +4.05¢ | $96.60 / $105.10 |

*Expect about **83 buys a day** (~$12.46/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 4718 | $101.30 | +20% |
| Volatility model ≥ 2%, hold to the close | 9277 | $30.90 | +3% |
| Momentum model ≥ 2%, hold to the close | 7727 | -$48.95 | -6% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 68915 | 68881 | 257 (0%) | 1.07% | -$4,741.10 (-57%) | Hold to the close: -$4,741.10 (-57%) |

*In play or awaiting result: 6. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 40703 | 4.5% | 0.4% (165) | -658% | ❌ Worse |
| Momentum model | 40703 | 4.4% | 0.4% (165) | -681% | ❌ Worse |
| Mean-reversion model | 40703 | 7.9% | 0.4% (165) | -798% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 40703 | 165 | -47% | -87% | -87% | -85% |
| Volatility model ≥ 2% | 9277 | 81 | +3% | -77% | -76% | -73% |
| Volatility model ≥ 5% | 4975 | 53 | +37% | -73% | -72% | -68% |
| Volatility model ≥ 10% | 2885 | 32 | +65% | -65% | -64% | -60% |
| Momentum model ≥ 2% | 7727 | 59 | -6% | -79% | -79% | -76% |
| Momentum model ≥ 5% | 4718 | 43 | +20% | -76% | -75% | -71% |
| Momentum model ≥ 10% | 3076 | 28 | +32% | -68% | -68% | -64% |
| Mean-reversion model ≥ 2% | 16589 | 113 | -25% | -82% | -82% | -80% |
| Mean-reversion model ≥ 5% | 11548 | 93 | -10% | -80% | -79% | -77% |
| Mean-reversion model ≥ 10% | 7663 | 66 | -1% | -78% | -78% | -75% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 40909 | 5% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 16461 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 11511 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 68881 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 257 | 0% | -$4,741.10 | -57% | — |
| Sell at 2¢ | 2825 | 4% | -$7,296.60 | -87% | 47 sec |
| Sell at 3¢ | 1897 | 3% | -$7,291.27 | -87% | 48 sec |
| Sell at 5¢ | 1284 | 2% | -$7,168.50 | -86% | 62 sec |
| Sell at 10¢ | 786 | 1% | -$6,889.44 | -83% | 65 sec |
| Sell at 25¢ | 425 | 1% | -$6,358.35 | -76% | 80 sec |
| Sell at 50¢ | 271 | 0% | -$5,753.85 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 13 | 0 | 31% | 23% | -100% | -47% | -20% |
| 5–10 min | 3566 | 17 | 10% | 4% | -55% | -82% | -83% |
| 2–5 min | 22343 | 116 | 7% | 3% | -49% | -86% | -86% |
| 1–2 min | 17148 | 58 | 3% | 2% | -62% | -92% | -92% |
| Under 1 min | 25811 | 66 | 1% | 0% | -63% | -86% | -86% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 4577 | 20 | 5% | 2% | -42% | -87% | -87% |
| HYPE | 4569 | 16 | 5% | 2% | -55% | -89% | -88% |
| SOL | 4560 | 20 | 4% | 2% | -43% | -86% | -86% |
| BNB | 4553 | 22 | 5% | 2% | -38% | -86% | -85% |
| DOGE | 4551 | 12 | 4% | 2% | -66% | -89% | -89% |
| ETH | 4546 | 19 | 7% | 3% | -47% | -82% | -82% |
| BTC | 4523 | 24 | 5% | 2% | -27% | -86% | -88% |
| NEAR | 4519 | 18 | 5% | 2% | -48% | -86% | -86% |
| XRP | 4511 | 16 | 4% | 2% | -55% | -88% | -88% |
| GOLD | 2430 | 8 | 5% | 2% | -60% | -82% | -84% |
| WTI | 2417 | 9 | 4% | 2% | -54% | -86% | -87% |
| SILVER | 2378 | 9 | 5% | 2% | -55% | -83% | -83% |
| PLATINUM | 2156 | 5 | 3% | 1% | -78% | -95% | -95% |
| EURUSD | 2107 | 7 | 2% | 1% | -69% | -91% | -91% |
| GBPUSD | 2053 | 8 | 2% | 1% | -64% | -96% | -96% |
| COPPER | 2040 | 6 | 2% | 1% | -73% | -79% | -79% |
| USDJPY | 2002 | 6 | 2% | 1% | -72% | -97% | -96% |
| NATGAS | 1994 | 10 | 2% | 1% | -53% | -77% | -77% |
| PALLADIUM | 1942 | 4 | 1% | 1% | -81% | -93% | -93% |
| AUDUSD | 1575 | 7 | 2% | 1% | -59% | -90% | -90% |
| USDCAD | 1484 | 1 | 3% | 1% | -94% | -95% | -95% |
| BRENT | 1104 | 1 | 2% | 1% | -92% | -96% | -96% |
| 10YRRATE | 557 | 2 | 3% | 1% | -66% | -78% | -76% |
| 30YRRATE | 518 | 0 | 3% | 1% | -100% | -95% | -93% |
| 2YRRATE | 515 | 4 | 4% | 2% | -28% | -57% | -57% |
| 5YRRATE | 506 | 2 | 4% | 2% | -63% | -94% | -95% |
| INX | 139 | 1 | 2% | 1% | -33% | -96% | -96% |
| USDMXN | 55 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 35110 | 133 | 4% | 2% | -56% | -88% | -88% |
| DOWN (bought NO) | 33771 | 124 | 4% | 2% | -58% | -87% | -87% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 5930 | 25 | 2% | 1% | -22% | -79% | -78% |
| 0.05–0.1% | 6499 | 26 | 3% | 2% | -36% | -91% | -91% |
| 0.1–0.2% | 10124 | 36 | 5% | 2% | -53% | -89% | -89% |
| 0.2–0.5% | 12901 | 56 | 7% | 3% | -50% | -86% | -86% |
| Over 0.5% | 5446 | 24 | 7% | 3% | -54% | -86% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 16499 | 51 | 4% | 2% | -65% | -87% | -88% |
| Morning (6am–12pm) | 16354 | 82 | 4% | 2% | -43% | -86% | -85% |
| Afternoon (12–6pm) | 16940 | 73 | 4% | 2% | -49% | -87% | -87% |
| Evening (6pm–12am) | 19088 | 51 | 4% | 2% | -69% | -90% | -89% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 5,081 |
| Time from buy to best bounce (bounced bets) | 51 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/26 9:29:48 PM | ETH | UP | 12 sec | -0.016% | 0¢ | ❌ Lost | $0.00 |
| 11/26 9:29:33 PM | NATGAS | DOWN | 26 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/26 9:29:33 PM | GOLD | DOWN | 26 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/26 9:29:15 PM | SOL | DOWN | 44 sec | +0.103% | 1¢ | ❌ Lost | -$0.15 |
| 11/26 9:29:15 PM | BTC | UP | 44 sec | -0.055% | 0¢ | ❌ Lost | -$0.15 |
| 11/26 9:29:15 PM | AUDUSD | UP | 44 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/26 9:29:15 PM | SILVER | UP | 44 sec | — | 0¢ | ❌ Lost | $0.00 |
| 11/26 9:28:59 PM | XRP | UP | 60 sec | -0.115% | 1¢ | ❌ Lost | -$0.15 |
| 11/26 9:28:59 PM | USDCAD | DOWN | 60 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/26 9:28:59 PM | WTI | DOWN | 60 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 11/26 9:28:43 PM | HYPE | UP | 76 sec | -0.432% | 0¢ | ❌ Lost | -$0.15 |
| 11/26 9:28:43 PM | BNB | UP | 76 sec | -0.162% | 0¢ | ❌ Lost | $0.00 |
| 11/26 9:28:10 PM | ZEC | UP | 1.8 min | -0.528% | 1¢ | ❌ Lost | -$0.15 |
| 11/26 9:27:54 PM | PLATINUM | UP | 2.1 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/26 9:27:38 PM | NEAR | UP | 2.4 min | -0.491% | 1¢ | ❌ Lost | -$0.15 |
| 11/26 9:26:27 PM | GBPUSD | DOWN | 3.5 min | — | 15¢ | ❌ Lost | -$0.15 |
| 11/26 7:59:56 PM | USDJPY | DOWN | 4 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/26 7:59:56 PM | NATGAS | UP | 4 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/26 7:59:56 PM | WTI | DOWN | 4 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 11/26 7:59:30 PM | EURUSD | UP | 29 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/26 7:59:14 PM | NEAR | UP | 46 sec | -0.380% | 0¢ | ❌ Lost | $0.00 |
| 11/26 7:59:14 PM | PALLADIUM | UP | 46 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/26 7:59:14 PM | ZEC | UP | 46 sec | -0.393% | 0¢ | ❌ Lost | $0.00 |
| 11/26 7:58:58 PM | GOLD | UP | 61 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 11/26 7:58:58 PM | DOGE | UP | 61 sec | -0.198% | 0¢ | ❌ Lost | -$0.15 |
| 11/26 7:58:58 PM | SILVER | UP | 61 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 11/26 7:58:58 PM | SOL | UP | 61 sec | -0.196% | 1¢ | ❌ Lost | -$0.15 |
| 11/26 7:58:42 PM | XRP | UP | 77 sec | -0.250% | 0¢ | ❌ Lost | -$0.15 |
| 11/26 7:58:42 PM | GBPUSD | UP | 77 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/26 7:58:26 PM | ETH | UP | 1.6 min | -0.262% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
