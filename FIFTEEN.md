# 15-Minute 1¢ Study

*Updated Mon Nov 16, 10:22 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 4453 finished bets | 1% | $222.00 | +45% | +4.99¢ | $84.60 / $137.40 |

*Expect about **89 buys a day** (~$13.38/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 4201 | $120.55 | +27% |
| Volatility model ≥ 2%, hold to the close | 8289 | $81.40 | +8% |
| Momentum model ≥ 2%, hold to the close | 6892 | $7.65 | +1% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 59249 | 59213 | 227 (0%) | 1.07% | -$4,022.60 (-56%) | Hold to the close: -$4,022.60 (-56%) |

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
| Volatility model | 35623 | 4.6% | 0.4% (148) | -637% | ❌ Worse |
| Momentum model | 35623 | 4.5% | 0.4% (148) | -663% | ❌ Worse |
| Mean-reversion model | 35623 | 7.9% | 0.4% (148) | -774% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 35623 | 148 | -47% | -87% | -87% | -85% |
| Volatility model ≥ 2% | 8289 | 77 | +8% | -77% | -76% | -72% |
| Volatility model ≥ 5% | 4453 | 51 | +45% | -72% | -70% | -67% |
| Volatility model ≥ 10% | 2564 | 30 | +70% | -63% | -61% | -58% |
| Momentum model ≥ 2% | 6892 | 57 | +1% | -79% | -78% | -74% |
| Momentum model ≥ 5% | 4201 | 41 | +27% | -74% | -74% | -70% |
| Momentum model ≥ 10% | 2738 | 26 | +35% | -66% | -66% | -62% |
| Mean-reversion model ≥ 2% | 14584 | 103 | -23% | -82% | -82% | -80% |
| Mean-reversion model ≥ 5% | 10150 | 85 | -7% | -80% | -79% | -77% |
| Mean-reversion model ≥ 10% | 6741 | 61 | +3% | -77% | -77% | -75% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 35829 | 5% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 14045 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 9339 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 59213 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 227 | 0% | -$4,022.60 | -56% | — |
| Sell at 2¢ | 2375 | 4% | -$6,289.10 | -87% | 47 sec |
| Sell at 3¢ | 1603 | 3% | -$6,281.43 | -87% | 48 sec |
| Sell at 5¢ | 1097 | 2% | -$6,165.55 | -86% | 62 sec |
| Sell at 10¢ | 669 | 1% | -$5,918.21 | -82% | 65 sec |
| Sell at 25¢ | 355 | 1% | -$5,493.55 | -76% | 80 sec |
| Sell at 50¢ | 234 | 0% | -$4,963.10 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 13 | 0 | 31% | 23% | -100% | -47% | -20% |
| 5–10 min | 2965 | 13 | 10% | 4% | -58% | -82% | -83% |
| 2–5 min | 19158 | 104 | 7% | 3% | -47% | -87% | -87% |
| 1–2 min | 14895 | 51 | 3% | 2% | -62% | -92% | -92% |
| Under 1 min | 22182 | 59 | 1% | 0% | -62% | -85% | -85% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 4010 | 19 | 5% | 2% | -38% | -88% | -87% |
| SOL | 4005 | 18 | 4% | 2% | -42% | -87% | -87% |
| HYPE | 3997 | 12 | 4% | 2% | -62% | -89% | -88% |
| BNB | 3987 | 20 | 5% | 2% | -36% | -86% | -85% |
| DOGE | 3986 | 11 | 4% | 2% | -65% | -90% | -89% |
| ETH | 3978 | 17 | 7% | 3% | -47% | -82% | -82% |
| BTC | 3961 | 21 | 5% | 2% | -28% | -86% | -88% |
| NEAR | 3959 | 17 | 5% | 2% | -44% | -85% | -86% |
| XRP | 3946 | 15 | 3% | 2% | -52% | -89% | -88% |
| GOLD | 2101 | 5 | 5% | 2% | -71% | -82% | -84% |
| WTI | 2084 | 7 | 4% | 1% | -59% | -91% | -92% |
| SILVER | 2042 | 9 | 5% | 2% | -48% | -83% | -83% |
| PLATINUM | 1863 | 4 | 3% | 1% | -80% | -95% | -95% |
| EURUSD | 1810 | 6 | 2% | 1% | -69% | -91% | -90% |
| COPPER | 1743 | 6 | 2% | 1% | -68% | -75% | -75% |
| GBPUSD | 1737 | 6 | 2% | 1% | -68% | -96% | -96% |
| NATGAS | 1719 | 9 | 2% | 1% | -51% | -75% | -74% |
| USDJPY | 1696 | 6 | 2% | 1% | -67% | -96% | -96% |
| PALLADIUM | 1675 | 4 | 1% | 0% | -78% | -92% | -93% |
| AUDUSD | 1252 | 6 | 2% | 1% | -55% | -89% | -89% |
| USDCAD | 1196 | 1 | 3% | 1% | -92% | -96% | -96% |
| BRENT | 818 | 0 | 2% | 1% | -100% | -97% | -97% |
| 10YRRATE | 418 | 2 | 4% | 1% | -55% | -71% | -70% |
| 2YRRATE | 403 | 4 | 4% | 2% | -7% | -47% | -46% |
| 30YRRATE | 388 | 0 | 2% | 1% | -100% | -96% | -94% |
| 5YRRATE | 375 | 2 | 4% | 2% | -50% | -94% | -95% |
| INX | 64 | 0 | 2% | 0% | -100% | -97% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 30108 | 113 | 4% | 2% | -57% | -88% | -88% |
| DOWN (bought NO) | 29105 | 114 | 4% | 2% | -55% | -86% | -87% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 5430 | 25 | 2% | 1% | -17% | -78% | -77% |
| 0.05–0.1% | 5874 | 24 | 3% | 2% | -37% | -91% | -91% |
| 0.1–0.2% | 8987 | 34 | 5% | 2% | -51% | -89% | -89% |
| 0.2–0.5% | 11070 | 48 | 7% | 3% | -51% | -86% | -86% |
| Over 0.5% | 4459 | 19 | 7% | 3% | -55% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 14411 | 45 | 4% | 2% | -64% | -88% | -88% |
| Morning (6am–12pm) | 13940 | 70 | 4% | 2% | -43% | -85% | -84% |
| Afternoon (12–6pm) | 14631 | 63 | 4% | 2% | -49% | -87% | -87% |
| Evening (6pm–12am) | 16231 | 49 | 4% | 2% | -65% | -89% | -89% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 5,082 |
| Time from buy to best bounce (bounced bets) | 50 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/16 10:22:15 PM | ETH | DOWN | 7.7 min | +0.649% | — | In play | — |
| 11/16 10:21:59 PM | SOL | DOWN | 8.0 min | +0.634% | — | In play | — |
| 11/16 10:14:40 PM | AUDUSD | UP | 20 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/16 10:14:40 PM | USDCAD | UP | 20 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/16 10:14:40 PM | GOLD | UP | 20 sec | — | 0¢ | ❌ Lost | $0.00 |
| 11/16 10:14:24 PM | WTI | UP | 36 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/16 10:14:24 PM | PALLADIUM | UP | 36 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/16 10:13:53 PM | SILVER | UP | 66 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 11/16 10:13:37 PM | COPPER | UP | 83 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/16 10:13:21 PM | USDJPY | UP | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/16 10:13:05 PM | GBPUSD | DOWN | 1.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/16 10:12:18 PM | EURUSD | DOWN | 2.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/16 10:11:39 PM | ZEC | UP | 3.3 min | -0.678% | 0¢ | ❌ Lost | -$0.15 |
| 11/16 10:11:39 PM | PLATINUM | UP | 3.3 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/16 10:10:51 PM | HYPE | UP | 4.1 min | -0.459% | 1¢ | ❌ Lost | -$0.15 |
| 11/16 10:10:51 PM | ETH | UP | 4.1 min | -0.309% | 1¢ | ❌ Lost | -$0.15 |
| 11/16 10:10:20 PM | BTC | UP | 4.7 min | -0.416% | 1¢ | ❌ Lost | -$0.15 |
| 11/16 10:10:20 PM | SOL | UP | 4.7 min | -0.457% | 1¢ | ❌ Lost | -$0.15 |
| 11/16 10:10:04 PM | BNB | UP | 4.9 min | -0.321% | 1¢ | ❌ Lost | -$0.15 |
| 11/16 10:09:48 PM | DOGE | UP | 5.2 min | -0.380% | 1¢ | ❌ Lost | -$0.15 |
| 11/16 10:09:48 PM | NEAR | UP | 5.2 min | -0.831% | 1¢ | ❌ Lost | -$0.15 |
| 11/16 10:09:33 PM | XRP | UP | 5.4 min | -0.362% | 1¢ | ❌ Lost | -$0.15 |
| 11/16 9:59:43 PM | GBPUSD | UP | 16 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/16 9:59:43 PM | WTI | UP | 16 sec | — | 0¢ | ❌ Lost | $0.00 |
| 11/16 9:59:43 PM | COPPER | DOWN | 16 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/16 9:59:27 PM | BTC | DOWN | 32 sec | +0.038% | 0¢ | ❌ Lost | $0.00 |
| 11/16 9:59:27 PM | BNB | DOWN | 32 sec | +0.013% | 0¢ | ❌ Lost | -$0.15 |
| 11/16 9:58:42 PM | DOGE | DOWN | 77 sec | +0.155% | 1¢ | ❌ Lost | -$0.15 |
| 11/16 9:58:42 PM | SOL | DOWN | 77 sec | +0.148% | 1¢ | ❌ Lost | -$0.15 |
| 11/16 9:58:26 PM | XRP | DOWN | 1.6 min | +0.124% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
