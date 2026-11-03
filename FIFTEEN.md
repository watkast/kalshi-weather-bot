# 15-Minute 1¢ Study

*Updated Mon Nov 2, 8:27 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 3528 finished bets | 1% | $123.65 | +31% | +3.50¢ | $69.80 / $53.85 |

*Expect about **98 buys a day** (~$14.76/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 3260 | $50.95 | +14% |
| Volatility model ≥ 2%, hold to the close | 6527 | $49.20 | +6% |
| Momentum model ≥ 2%, hold to the close | 5388 | -$35.40 | -6% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 43248 | 43237 | 161 (0%) | 1.07% | -$3,010.40 (-57%) | Hold to the close: -$3,010.40 (-57%) |

*In play or awaiting result: 10. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 26773 | 4.7% | 0.4% (106) | -677% | ❌ Worse |
| Momentum model | 26773 | 4.6% | 0.4% (106) | -701% | ❌ Worse |
| Mean-reversion model | 26773 | 8.1% | 0.4% (106) | -823% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 26773 | 106 | -50% | -87% | -87% | -85% |
| Volatility model ≥ 2% | 6527 | 60 | +6% | -79% | -78% | -74% |
| Volatility model ≥ 5% | 3528 | 37 | +31% | -76% | -75% | -71% |
| Volatility model ≥ 10% | 1997 | 22 | +57% | -70% | -68% | -65% |
| Momentum model ≥ 2% | 5388 | 42 | -6% | -81% | -80% | -77% |
| Momentum model ≥ 5% | 3260 | 29 | +14% | -79% | -78% | -74% |
| Momentum model ≥ 10% | 2128 | 19 | +25% | -74% | -73% | -69% |
| Mean-reversion model ≥ 2% | 11059 | 76 | -25% | -83% | -83% | -80% |
| Mean-reversion model ≥ 5% | 7752 | 65 | -7% | -81% | -80% | -77% |
| Mean-reversion model ≥ 10% | 5182 | 46 | +1% | -79% | -79% | -76% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 26975 | 5% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 10193 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 6069 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 43237 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 161 | 0% | -$3,010.40 | -57% | — |
| Sell at 2¢ | 1709 | 4% | -$4,582.06 | -87% | 47 sec |
| Sell at 3¢ | 1172 | 3% | -$4,569.32 | -87% | 49 sec |
| Sell at 5¢ | 813 | 2% | -$4,469.95 | -85% | 63 sec |
| Sell at 10¢ | 490 | 1% | -$4,272.50 | -81% | 65 sec |
| Sell at 25¢ | 255 | 1% | -$3,958.35 | -75% | 82 sec |
| Sell at 50¢ | 166 | 0% | -$3,597.90 | -68% | 1.8 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 11 | 0 | 27% | 18% | -100% | -53% | -29% |
| 5–10 min | 2074 | 9 | 11% | 4% | -59% | -81% | -82% |
| 2–5 min | 13897 | 75 | 7% | 4% | -47% | -86% | -86% |
| 1–2 min | 10912 | 39 | 3% | 2% | -61% | -92% | -92% |
| Under 1 min | 16343 | 38 | 1% | 0% | -67% | -85% | -84% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 3023 | 13 | 5% | 3% | -45% | -88% | -87% |
| SOL | 3014 | 11 | 4% | 2% | -54% | -91% | -90% |
| BNB | 3011 | 17 | 5% | 2% | -29% | -85% | -84% |
| HYPE | 3009 | 9 | 5% | 2% | -63% | -89% | -87% |
| DOGE | 2997 | 6 | 4% | 2% | -75% | -90% | -89% |
| ETH | 2994 | 11 | 7% | 3% | -55% | -85% | -85% |
| BTC | 2978 | 14 | 5% | 2% | -36% | -88% | -89% |
| NEAR | 2977 | 15 | 5% | 2% | -35% | -83% | -84% |
| XRP | 2972 | 12 | 3% | 1% | -50% | -89% | -89% |
| GOLD | 1583 | 5 | 5% | 2% | -62% | -81% | -83% |
| SILVER | 1543 | 7 | 5% | 2% | -46% | -82% | -82% |
| WTI | 1541 | 4 | 3% | 1% | -69% | -92% | -93% |
| PLATINUM | 1373 | 3 | 2% | 1% | -80% | -96% | -96% |
| EURUSD | 1314 | 3 | 2% | 1% | -79% | -89% | -89% |
| COPPER | 1310 | 6 | 2% | 1% | -57% | -69% | -69% |
| NATGAS | 1260 | 7 | 2% | 1% | -48% | -81% | -81% |
| GBPUSD | 1244 | 2 | 2% | 1% | -85% | -96% | -96% |
| PALLADIUM | 1237 | 3 | 1% | 1% | -77% | -90% | -91% |
| USDJPY | 1229 | 5 | 2% | 1% | -62% | -97% | -96% |
| AUDUSD | 771 | 4 | 2% | 1% | -52% | -85% | -84% |
| USDCAD | 736 | 0 | 2% | 1% | -100% | -97% | -98% |
| BRENT | 346 | 0 | 1% | 1% | -100% | -97% | -96% |
| 10YRRATE | 210 | 1 | 5% | 2% | -56% | -46% | -44% |
| 30YRRATE | 198 | 0 | 2% | 0% | -100% | -97% | -96% |
| 2YRRATE | 191 | 2 | 4% | 1% | -2% | +5% | +6% |
| 5YRRATE | 176 | 1 | 6% | 2% | -47% | -90% | -93% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 22000 | 87 | 4% | 2% | -54% | -88% | -87% |
| DOWN (bought NO) | 21237 | 74 | 4% | 2% | -60% | -87% | -87% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 4387 | 21 | 2% | 1% | -17% | -82% | -82% |
| 0.05–0.1% | 4632 | 18 | 3% | 2% | -42% | -91% | -90% |
| 0.1–0.2% | 6982 | 24 | 4% | 2% | -57% | -90% | -90% |
| 0.2–0.5% | 7980 | 33 | 7% | 3% | -54% | -86% | -86% |
| Over 0.5% | 2989 | 12 | 7% | 3% | -59% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 10646 | 37 | 4% | 2% | -60% | -87% | -87% |
| Morning (6am–12pm) | 10804 | 48 | 4% | 2% | -49% | -85% | -85% |
| Afternoon (12–6pm) | 10198 | 38 | 4% | 2% | -56% | -85% | -85% |
| Evening (6pm–12am) | 11589 | 38 | 3% | 2% | -62% | -91% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,768 |
| Time from buy to best bounce (bounced bets) | 51 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/2 8:27:17 PM | GOLD | UP | 2.7 min | — | — | In play | — |
| 11/2 8:14:47 PM | USDJPY | DOWN | 13 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/2 8:14:31 PM | BRENT | DOWN | 29 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/2 8:14:15 PM | ETH | DOWN | 44 sec | +0.049% | 0¢ | ❌ Lost | -$0.15 |
| 11/2 8:14:15 PM | ZEC | DOWN | 44 sec | +0.153% | 1¢ | ❌ Lost | -$0.15 |
| 11/2 8:14:15 PM | NEAR | UP | 44 sec | -0.216% | 1¢ | ❌ Lost | -$0.15 |
| 11/2 8:14:15 PM | EURUSD | UP | 44 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/2 8:14:15 PM | XRP | DOWN | 44 sec | +0.080% | 0¢ | ❌ Lost | $0.00 |
| 11/2 8:14:15 PM | HYPE | UP | 44 sec | -0.131% | 1¢ | ❌ Lost | -$0.15 |
| 11/2 8:13:41 PM | PLATINUM | UP | 79 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/2 8:13:41 PM | GBPUSD | UP | 79 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/2 8:13:25 PM | AUDUSD | UP | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/2 8:13:25 PM | GOLD | UP | 1.6 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/2 8:13:25 PM | SILVER | UP | 1.6 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/2 8:13:25 PM | NATGAS | DOWN | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/2 8:12:37 PM | COPPER | UP | 2.4 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/2 8:12:21 PM | DOGE | DOWN | 2.6 min | +0.233% | 0¢ | ❌ Lost | -$0.15 |
| 11/2 8:12:21 PM | BTC | DOWN | 2.6 min | +0.259% | 1¢ | ❌ Lost | -$0.15 |
| 11/2 8:11:30 PM | BNB | DOWN | 3.5 min | +0.193% | 1¢ | ❌ Lost | -$0.15 |
| 11/2 8:10:59 PM | SOL | DOWN | 4.0 min | +0.355% | 1¢ | ❌ Lost | -$0.15 |
| 11/2 7:59:45 PM | NATGAS | UP | 14 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/2 7:59:29 PM | COPPER | UP | 30 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/2 7:58:40 PM | XRP | UP | 79 sec | -0.120% | 0¢ | ❌ Lost | $0.00 |
| 11/2 7:58:40 PM | PALLADIUM | DOWN | 79 sec | — | 6¢ | ✅ Won | $13.85 |
| 11/2 7:58:24 PM | GBPUSD | DOWN | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/2 7:58:24 PM | USDJPY | UP | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/2 7:58:08 PM | PLATINUM | DOWN | 1.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/2 7:57:50 PM | AUDUSD | DOWN | 2.2 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/2 7:57:50 PM | USDCAD | UP | 2.2 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/2 7:57:50 PM | SILVER | DOWN | 2.2 min | — | 3¢ | ❌ Lost | $0.00 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
