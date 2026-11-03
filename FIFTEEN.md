# 15-Minute 1¢ Study

*Updated Mon Nov 2, 7:35 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 3528 finished bets | 1% | $123.65 | +31% | +3.50¢ | $69.80 / $53.85 |

*Expect about **98 buys a day** (~$14.77/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 3260 | $50.95 | +14% |
| Volatility model ≥ 2%, hold to the close | 6523 | $49.80 | +6% |
| Momentum model ≥ 2%, hold to the close | 5387 | -$35.25 | -6% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 43188 | 43178 | 160 (0%) | 1.07% | -$3,016.60 (-57%) | Hold to the close: -$3,016.60 (-57%) |

*In play or awaiting result: 9. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 26747 | 4.7% | 0.4% (106) | -677% | ❌ Worse |
| Momentum model | 26747 | 4.6% | 0.4% (106) | -701% | ❌ Worse |
| Mean-reversion model | 26747 | 8.1% | 0.4% (106) | -823% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 26747 | 106 | -50% | -87% | -87% | -85% |
| Volatility model ≥ 2% | 6523 | 60 | +6% | -79% | -78% | -74% |
| Volatility model ≥ 5% | 3528 | 37 | +31% | -76% | -75% | -71% |
| Volatility model ≥ 10% | 1997 | 22 | +57% | -70% | -68% | -65% |
| Momentum model ≥ 2% | 5387 | 42 | -6% | -81% | -80% | -77% |
| Momentum model ≥ 5% | 3260 | 29 | +14% | -79% | -78% | -74% |
| Momentum model ≥ 10% | 2128 | 19 | +25% | -74% | -73% | -69% |
| Mean-reversion model ≥ 2% | 11049 | 76 | -25% | -83% | -83% | -80% |
| Mean-reversion model ≥ 5% | 7746 | 65 | -7% | -81% | -80% | -77% |
| Mean-reversion model ≥ 10% | 5177 | 46 | +1% | -79% | -79% | -76% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 26949 | 5% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 10172 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 6057 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 43178 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 160 | 0% | -$3,016.60 | -57% | — |
| Sell at 2¢ | 1704 | 4% | -$4,575.56 | -87% | 47 sec |
| Sell at 3¢ | 1169 | 3% | -$4,562.69 | -87% | 49 sec |
| Sell at 5¢ | 812 | 2% | -$4,462.80 | -85% | 63 sec |
| Sell at 10¢ | 490 | 1% | -$4,278.70 | -81% | 65 sec |
| Sell at 25¢ | 255 | 1% | -$3,964.55 | -75% | 82 sec |
| Sell at 50¢ | 166 | 0% | -$3,604.10 | -69% | 1.8 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 11 | 0 | 27% | 18% | -100% | -53% | -29% |
| 5–10 min | 2073 | 9 | 11% | 4% | -59% | -81% | -82% |
| 2–5 min | 13874 | 75 | 7% | 4% | -47% | -86% | -86% |
| 1–2 min | 10895 | 38 | 3% | 2% | -62% | -92% | -92% |
| Under 1 min | 16325 | 38 | 1% | 0% | -67% | -85% | -84% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 3020 | 13 | 5% | 3% | -45% | -88% | -87% |
| SOL | 3011 | 11 | 4% | 2% | -54% | -91% | -90% |
| BNB | 3008 | 17 | 5% | 2% | -29% | -85% | -84% |
| HYPE | 3006 | 9 | 5% | 2% | -63% | -89% | -87% |
| DOGE | 2994 | 6 | 4% | 2% | -75% | -90% | -89% |
| ETH | 2991 | 11 | 6% | 3% | -55% | -85% | -85% |
| BTC | 2975 | 14 | 5% | 2% | -36% | -88% | -89% |
| NEAR | 2974 | 15 | 5% | 2% | -35% | -83% | -84% |
| XRP | 2970 | 12 | 3% | 1% | -50% | -89% | -89% |
| GOLD | 1580 | 5 | 5% | 2% | -62% | -81% | -83% |
| SILVER | 1540 | 7 | 5% | 2% | -46% | -82% | -82% |
| WTI | 1539 | 4 | 3% | 1% | -69% | -93% | -93% |
| PLATINUM | 1370 | 3 | 2% | 1% | -80% | -96% | -96% |
| EURUSD | 1311 | 3 | 2% | 1% | -79% | -89% | -89% |
| COPPER | 1307 | 6 | 2% | 1% | -57% | -69% | -68% |
| NATGAS | 1258 | 7 | 2% | 1% | -48% | -81% | -81% |
| GBPUSD | 1242 | 2 | 2% | 1% | -85% | -96% | -96% |
| PALLADIUM | 1235 | 2 | 1% | 0% | -85% | -90% | -91% |
| USDJPY | 1226 | 5 | 2% | 1% | -62% | -97% | -96% |
| AUDUSD | 768 | 4 | 2% | 1% | -51% | -85% | -84% |
| USDCAD | 735 | 0 | 2% | 1% | -100% | -97% | -98% |
| BRENT | 343 | 0 | 1% | 1% | -100% | -97% | -96% |
| 10YRRATE | 210 | 1 | 5% | 2% | -56% | -46% | -44% |
| 30YRRATE | 198 | 0 | 2% | 0% | -100% | -97% | -96% |
| 2YRRATE | 191 | 2 | 4% | 1% | -2% | +5% | +6% |
| 5YRRATE | 176 | 1 | 6% | 2% | -47% | -90% | -93% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 21961 | 87 | 4% | 2% | -54% | -88% | -87% |
| DOWN (bought NO) | 21217 | 73 | 4% | 2% | -61% | -87% | -87% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 4386 | 21 | 2% | 1% | -17% | -82% | -82% |
| 0.05–0.1% | 4629 | 18 | 3% | 2% | -41% | -91% | -90% |
| 0.1–0.2% | 6974 | 24 | 4% | 2% | -57% | -90% | -90% |
| 0.2–0.5% | 7969 | 33 | 7% | 3% | -54% | -86% | -86% |
| Over 0.5% | 2986 | 12 | 7% | 3% | -59% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 10646 | 37 | 4% | 2% | -60% | -87% | -87% |
| Morning (6am–12pm) | 10804 | 48 | 4% | 2% | -49% | -85% | -85% |
| Afternoon (12–6pm) | 10198 | 38 | 4% | 2% | -56% | -85% | -85% |
| Evening (6pm–12am) | 11530 | 37 | 3% | 2% | -63% | -91% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,767 |
| Time from buy to best bounce (bounced bets) | 51 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/2 7:29:51 PM | GBPUSD | UP | 8 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/2 7:29:51 PM | USDJPY | DOWN | 8 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/2 7:29:51 PM | AUDUSD | DOWN | 8 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/2 7:29:51 PM | HYPE | DOWN | 8 sec | -0.019% | 0¢ | ❌ Lost | $0.00 |
| 11/2 7:29:35 PM | XRP | DOWN | 24 sec | +0.088% | 0¢ | ❌ Lost | $0.00 |
| 11/2 7:29:35 PM | NEAR | DOWN | 24 sec | +0.094% | 0¢ | ❌ Lost | $0.00 |
| 11/2 7:29:35 PM | WTI | DOWN | 24 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 11/2 7:29:35 PM | DOGE | DOWN | 24 sec | +0.042% | 0¢ | ❌ Lost | -$0.15 |
| 11/2 7:29:19 PM | BRENT | DOWN | 41 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/2 7:29:19 PM | BTC | UP | 41 sec | -0.078% | 0¢ | ❌ Lost | $0.00 |
| 11/2 7:29:19 PM | USDCAD | DOWN | 41 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/2 7:28:44 PM | SOL | DOWN | 76 sec | +0.113% | 2¢ | ❌ Lost | -$0.15 |
| 11/2 7:28:44 PM | EURUSD | UP | 76 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/2 7:28:44 PM | PLATINUM | UP | 76 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/2 7:28:28 PM | SILVER | UP | 1.5 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/2 7:28:13 PM | ETH | DOWN | 1.8 min | +0.124% | 1¢ | ❌ Lost | -$0.15 |
| 11/2 7:27:54 PM | PALLADIUM | UP | 2.1 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/2 7:27:22 PM | COPPER | UP | 2.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/2 7:26:49 PM | BNB | DOWN | 3.2 min | +0.128% | 3¢ | ❌ Lost | -$0.15 |
| 11/2 7:26:49 PM | ZEC | DOWN | 3.2 min | +0.466% | 0¢ | ❌ Lost | -$0.15 |
| 11/2 7:26:33 PM | NATGAS | DOWN | 3.5 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/2 7:14:30 PM | EURUSD | UP | 29 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/2 7:14:30 PM | USDCAD | DOWN | 29 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/2 7:13:41 PM | WTI | UP | 78 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 11/2 7:13:09 PM | BRENT | UP | 1.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/2 7:12:34 PM | BTC | UP | 2.4 min | -0.221% | 1¢ | ❌ Lost | -$0.15 |
| 11/2 7:12:18 PM | AUDUSD | UP | 2.7 min | — | 2¢ | ❌ Lost | -$0.15 |
| 11/2 7:12:18 PM | NEAR | UP | 2.7 min | -0.687% | 1¢ | ❌ Lost | -$0.15 |
| 11/2 7:10:57 PM | XRP | UP | 4.0 min | -0.208% | 10¢ | ❌ Lost | -$0.15 |
| 11/2 7:10:57 PM | ZEC | UP | 4.0 min | -0.650% | 4¢ | ❌ Lost | $0.00 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
