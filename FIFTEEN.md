# 15-Minute 1¢ Study

*Updated Sun Nov 8, 9:19 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 4061 finished bets | 1% | $192.05 | +42% | +4.73¢ | $94.15 / $97.90 |

*Expect about **97 buys a day** (~$14.54/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 3768 | $109.70 | +27% |
| Volatility model ≥ 2%, hold to the close | 7436 | $84.65 | +9% |
| Momentum model ≥ 2%, hold to the close | 6140 | $8.10 | +1% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 50214 | 50197 | 186 (0%) | 1.07% | -$3,501.15 (-57%) | Hold to the close: -$3,501.15 (-57%) |

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
| Volatility model | 30749 | 4.8% | 0.4% (121) | -690% | ❌ Worse |
| Momentum model | 30749 | 4.6% | 0.4% (121) | -715% | ❌ Worse |
| Mean-reversion model | 30749 | 8.1% | 0.4% (121) | -834% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 30749 | 121 | -50% | -87% | -87% | -84% |
| Volatility model ≥ 2% | 7436 | 70 | +9% | -77% | -75% | -71% |
| Volatility model ≥ 5% | 4061 | 46 | +42% | -71% | -70% | -66% |
| Volatility model ≥ 10% | 2335 | 28 | +71% | -61% | -59% | -56% |
| Momentum model ≥ 2% | 6140 | 51 | +1% | -78% | -77% | -74% |
| Momentum model ≥ 5% | 3768 | 37 | +27% | -73% | -73% | -69% |
| Momentum model ≥ 10% | 2470 | 25 | +42% | -64% | -64% | -59% |
| Mean-reversion model ≥ 2% | 12719 | 89 | -23% | -82% | -82% | -79% |
| Mean-reversion model ≥ 5% | 8918 | 77 | -4% | -79% | -79% | -76% |
| Mean-reversion model ≥ 10% | 5962 | 56 | +7% | -76% | -76% | -74% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 30954 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 11791 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 7452 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 50197 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 186 | 0% | -$3,501.15 | -57% | — |
| Sell at 2¢ | 1966 | 4% | -$5,313.99 | -87% | 47 sec |
| Sell at 3¢ | 1338 | 3% | -$5,303.33 | -87% | 48 sec |
| Sell at 5¢ | 932 | 2% | -$5,191.35 | -85% | 63 sec |
| Sell at 10¢ | 563 | 1% | -$4,975.62 | -81% | 65 sec |
| Sell at 25¢ | 295 | 1% | -$4,624.70 | -76% | 83 sec |
| Sell at 50¢ | 190 | 0% | -$4,220.65 | -69% | 1.9 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 12 | 0 | 25% | 17% | -100% | -57% | -35% |
| 5–10 min | 2487 | 12 | 11% | 4% | -54% | -81% | -82% |
| 2–5 min | 16192 | 87 | 7% | 3% | -47% | -87% | -87% |
| 1–2 min | 12681 | 41 | 3% | 2% | -64% | -92% | -92% |
| Under 1 min | 18825 | 46 | 1% | 0% | -65% | -84% | -84% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 3470 | 13 | 5% | 2% | -51% | -88% | -88% |
| SOL | 3463 | 15 | 4% | 2% | -45% | -87% | -87% |
| HYPE | 3453 | 11 | 5% | 2% | -60% | -89% | -88% |
| BNB | 3446 | 18 | 5% | 2% | -34% | -86% | -85% |
| DOGE | 3445 | 7 | 4% | 2% | -74% | -91% | -90% |
| ETH | 3438 | 14 | 7% | 3% | -50% | -81% | -82% |
| NEAR | 3419 | 16 | 5% | 2% | -40% | -85% | -85% |
| BTC | 3415 | 16 | 5% | 2% | -36% | -88% | -89% |
| XRP | 3405 | 13 | 3% | 1% | -52% | -89% | -89% |
| GOLD | 1799 | 5 | 6% | 2% | -66% | -81% | -83% |
| WTI | 1768 | 6 | 4% | 1% | -59% | -92% | -92% |
| SILVER | 1750 | 8 | 5% | 2% | -46% | -82% | -82% |
| PLATINUM | 1582 | 4 | 2% | 1% | -76% | -96% | -96% |
| EURUSD | 1520 | 4 | 2% | 1% | -75% | -90% | -89% |
| COPPER | 1483 | 6 | 2% | 1% | -62% | -72% | -71% |
| NATGAS | 1447 | 8 | 2% | 1% | -48% | -77% | -76% |
| GBPUSD | 1439 | 4 | 2% | 1% | -74% | -96% | -96% |
| USDJPY | 1423 | 5 | 2% | 1% | -67% | -97% | -96% |
| PALLADIUM | 1422 | 3 | 1% | 0% | -80% | -91% | -92% |
| AUDUSD | 979 | 5 | 2% | 1% | -52% | -87% | -87% |
| USDCAD | 947 | 0 | 2% | 1% | -100% | -97% | -97% |
| BRENT | 540 | 0 | 1% | 1% | -100% | -97% | -97% |
| 10YRRATE | 303 | 1 | 4% | 1% | -69% | -62% | -60% |
| 2YRRATE | 287 | 3 | 4% | 1% | -2% | -28% | -27% |
| 30YRRATE | 285 | 0 | 2% | 1% | -100% | -96% | -95% |
| 5YRRATE | 262 | 1 | 4% | 2% | -64% | -93% | -95% |
| INX | 7 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 25441 | 95 | 4% | 2% | -57% | -88% | -87% |
| DOWN (bought NO) | 24756 | 91 | 4% | 2% | -58% | -86% | -86% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 5038 | 25 | 2% | 1% | -13% | -77% | -76% |
| 0.05–0.1% | 5311 | 19 | 3% | 2% | -46% | -91% | -91% |
| 0.1–0.2% | 7975 | 27 | 4% | 2% | -57% | -90% | -90% |
| 0.2–0.5% | 9174 | 38 | 6% | 3% | -54% | -87% | -86% |
| Over 0.5% | 3448 | 14 | 7% | 3% | -58% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 12179 | 42 | 4% | 2% | -61% | -87% | -87% |
| Morning (6am–12pm) | 12223 | 54 | 4% | 2% | -50% | -84% | -84% |
| Afternoon (12–6pm) | 12200 | 47 | 4% | 2% | -55% | -86% | -86% |
| Evening (6pm–12am) | 13595 | 43 | 3% | 2% | -64% | -90% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,949 |
| Time from buy to best bounce (bounced bets) | 51 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/8 9:14:46 PM | USDJPY | DOWN | 14 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/8 9:14:31 PM | ZEC | DOWN | 28 sec | +0.059% | 1¢ | ❌ Lost | -$0.15 |
| 11/8 9:13:41 PM | HYPE | DOWN | 78 sec | +0.135% | 1¢ | ❌ Lost | -$0.15 |
| 11/8 9:13:26 PM | SOL | DOWN | 1.6 min | +0.175% | 0¢ | ❌ Lost | -$0.15 |
| 11/8 9:13:26 PM | XRP | DOWN | 1.6 min | +0.171% | 1¢ | ❌ Lost | -$0.15 |
| 11/8 9:13:26 PM | EURUSD | DOWN | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/8 9:13:26 PM | PLATINUM | DOWN | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/8 9:13:10 PM | SILVER | DOWN | 1.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/8 9:13:10 PM | PALLADIUM | DOWN | 1.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/8 9:13:10 PM | ETH | DOWN | 1.8 min | +0.143% | 1¢ | ❌ Lost | -$0.15 |
| 11/8 9:12:54 PM | GOLD | DOWN | 2.1 min | — | 3¢ | ❌ Lost | -$0.15 |
| 11/8 9:12:38 PM | NEAR | DOWN | 2.4 min | +0.255% | 1¢ | ❌ Lost | -$0.15 |
| 11/8 9:12:22 PM | BRENT | DOWN | 2.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/8 9:11:49 PM | WTI | DOWN | 3.2 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/8 9:11:33 PM | BTC | DOWN | 3.4 min | +0.189% | 1¢ | ❌ Lost | -$0.15 |
| 11/8 9:11:33 PM | BNB | DOWN | 3.4 min | +0.183% | 1¢ | ❌ Lost | -$0.15 |
| 11/8 9:10:26 PM | COPPER | DOWN | 4.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/8 9:10:26 PM | DOGE | DOWN | 4.6 min | +0.306% | 1¢ | ❌ Lost | -$0.15 |
| 11/8 8:59:45 PM | USDCAD | DOWN | 15 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/8 8:59:45 PM | AUDUSD | UP | 15 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/8 8:59:29 PM | COPPER | UP | 31 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/8 8:59:14 PM | NATGAS | DOWN | 46 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 11/8 8:59:14 PM | USDJPY | UP | 46 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/8 8:58:58 PM | WTI | DOWN | 62 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 11/8 8:57:43 PM | PLATINUM | UP | 2.3 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/8 8:56:52 PM | NEAR | UP | 3.1 min | -0.524% | 1¢ | ❌ Lost | -$0.15 |
| 11/8 8:56:52 PM | SILVER | UP | 3.1 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/8 8:56:52 PM | ZEC | UP | 3.1 min | -0.420% | 1¢ | ❌ Lost | -$0.15 |
| 11/8 8:56:36 PM | PALLADIUM | UP | 3.4 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/8 8:56:20 PM | HYPE | UP | 3.6 min | -0.442% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
