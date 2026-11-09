# 15-Minute 1¢ Study

*Updated Sun Nov 8, 9:39 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 4063 finished bets | 1% | $191.90 | +42% | +4.72¢ | $94.00 / $97.90 |

*Expect about **97 buys a day** (~$14.54/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 3769 | $109.70 | +27% |
| Volatility model ≥ 2%, hold to the close | 7439 | $84.35 | +9% |
| Momentum model ≥ 2%, hold to the close | 6141 | $8.10 | +1% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 50236 | 50219 | 186 (0%) | 1.07% | -$3,503.55 (-57%) | Hold to the close: -$3,503.55 (-57%) |

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
| Volatility model | 30758 | 4.8% | 0.4% (121) | -690% | ❌ Worse |
| Momentum model | 30758 | 4.6% | 0.4% (121) | -715% | ❌ Worse |
| Mean-reversion model | 30758 | 8.1% | 0.4% (121) | -834% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 30758 | 121 | -50% | -87% | -87% | -84% |
| Volatility model ≥ 2% | 7439 | 70 | +9% | -77% | -75% | -71% |
| Volatility model ≥ 5% | 4063 | 46 | +42% | -71% | -70% | -66% |
| Volatility model ≥ 10% | 2337 | 28 | +71% | -61% | -59% | -56% |
| Momentum model ≥ 2% | 6141 | 51 | +1% | -78% | -77% | -74% |
| Momentum model ≥ 5% | 3769 | 37 | +27% | -73% | -73% | -69% |
| Momentum model ≥ 10% | 2471 | 25 | +42% | -64% | -64% | -59% |
| Mean-reversion model ≥ 2% | 12722 | 89 | -23% | -82% | -82% | -79% |
| Mean-reversion model ≥ 5% | 8921 | 77 | -4% | -79% | -79% | -76% |
| Mean-reversion model ≥ 10% | 5965 | 56 | +7% | -76% | -76% | -73% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 30963 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 11799 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 7457 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 50219 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 186 | 0% | -$3,503.55 | -57% | — |
| Sell at 2¢ | 1968 | 4% | -$5,315.87 | -87% | 47 sec |
| Sell at 3¢ | 1340 | 3% | -$5,304.95 | -87% | 48 sec |
| Sell at 5¢ | 934 | 2% | -$5,192.45 | -85% | 63 sec |
| Sell at 10¢ | 565 | 1% | -$4,975.40 | -81% | 65 sec |
| Sell at 25¢ | 296 | 1% | -$4,623.79 | -76% | 83 sec |
| Sell at 50¢ | 190 | 0% | -$4,223.05 | -69% | 1.9 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 12 | 0 | 25% | 17% | -100% | -57% | -35% |
| 5–10 min | 2488 | 12 | 11% | 4% | -54% | -81% | -82% |
| 2–5 min | 16199 | 87 | 7% | 3% | -47% | -87% | -87% |
| 1–2 min | 12685 | 41 | 3% | 2% | -64% | -92% | -92% |
| Under 1 min | 18835 | 46 | 1% | 0% | -65% | -84% | -84% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 3471 | 13 | 5% | 2% | -51% | -88% | -88% |
| SOL | 3464 | 15 | 4% | 2% | -45% | -87% | -87% |
| HYPE | 3454 | 11 | 5% | 2% | -60% | -89% | -88% |
| BNB | 3447 | 18 | 5% | 2% | -34% | -86% | -85% |
| DOGE | 3446 | 7 | 4% | 2% | -74% | -90% | -90% |
| ETH | 3439 | 14 | 7% | 3% | -50% | -81% | -82% |
| NEAR | 3420 | 16 | 5% | 2% | -40% | -85% | -85% |
| BTC | 3416 | 16 | 5% | 2% | -36% | -88% | -89% |
| XRP | 3406 | 13 | 3% | 1% | -52% | -89% | -89% |
| GOLD | 1800 | 5 | 6% | 2% | -66% | -81% | -83% |
| WTI | 1769 | 6 | 4% | 1% | -59% | -92% | -92% |
| SILVER | 1751 | 8 | 5% | 2% | -46% | -82% | -82% |
| PLATINUM | 1583 | 4 | 2% | 1% | -76% | -96% | -96% |
| EURUSD | 1521 | 4 | 2% | 1% | -75% | -90% | -89% |
| COPPER | 1484 | 6 | 2% | 1% | -62% | -72% | -72% |
| NATGAS | 1448 | 8 | 2% | 1% | -48% | -77% | -76% |
| GBPUSD | 1440 | 4 | 2% | 1% | -74% | -96% | -96% |
| USDJPY | 1424 | 5 | 2% | 1% | -67% | -97% | -96% |
| PALLADIUM | 1423 | 3 | 1% | 0% | -80% | -91% | -92% |
| AUDUSD | 980 | 5 | 2% | 1% | -52% | -87% | -87% |
| USDCAD | 948 | 0 | 2% | 1% | -100% | -96% | -97% |
| BRENT | 541 | 0 | 1% | 1% | -100% | -97% | -97% |
| 10YRRATE | 303 | 1 | 4% | 1% | -69% | -62% | -60% |
| 2YRRATE | 287 | 3 | 4% | 1% | -2% | -28% | -27% |
| 30YRRATE | 285 | 0 | 2% | 1% | -100% | -96% | -95% |
| 5YRRATE | 262 | 1 | 4% | 2% | -64% | -93% | -95% |
| INX | 7 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 25448 | 95 | 4% | 2% | -57% | -88% | -87% |
| DOWN (bought NO) | 24771 | 91 | 4% | 2% | -58% | -86% | -86% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 5040 | 25 | 2% | 1% | -13% | -77% | -76% |
| 0.05–0.1% | 5313 | 19 | 3% | 2% | -46% | -91% | -91% |
| 0.1–0.2% | 7978 | 27 | 4% | 2% | -57% | -90% | -90% |
| 0.2–0.5% | 9176 | 38 | 6% | 3% | -54% | -87% | -86% |
| Over 0.5% | 3448 | 14 | 7% | 3% | -58% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 12179 | 42 | 4% | 2% | -61% | -87% | -87% |
| Morning (6am–12pm) | 12223 | 54 | 4% | 2% | -50% | -84% | -84% |
| Afternoon (12–6pm) | 12200 | 47 | 4% | 2% | -55% | -86% | -86% |
| Evening (6pm–12am) | 13617 | 43 | 3% | 2% | -64% | -90% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,947 |
| Time from buy to best bounce (bounced bets) | 51 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/8 9:29:56 PM | USDJPY | DOWN | 3 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/8 9:29:56 PM | ZEC | DOWN | 3 sec | +0.062% | 0¢ | ❌ Lost | $0.00 |
| 11/8 9:29:40 PM | NATGAS | DOWN | 19 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/8 9:29:40 PM | XRP | UP | 19 sec | -0.171% | 0¢ | ❌ Lost | $0.00 |
| 11/8 9:29:40 PM | ETH | UP | 19 sec | -0.108% | 0¢ | ❌ Lost | $0.00 |
| 11/8 9:29:40 PM | BNB | DOWN | 19 sec | -0.007% | 0¢ | ❌ Lost | $0.00 |
| 11/8 9:29:11 PM | HYPE | DOWN | 48 sec | +0.038% | 0¢ | ❌ Lost | -$0.15 |
| 11/8 9:29:11 PM | WTI | DOWN | 48 sec | — | 0¢ | ❌ Lost | $0.00 |
| 11/8 9:29:11 PM | GBPUSD | DOWN | 48 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/8 9:29:11 PM | BTC | UP | 48 sec | -0.092% | 0¢ | ❌ Lost | $0.00 |
| 11/8 9:28:53 PM | SOL | UP | 67 sec | -0.154% | 1¢ | ❌ Lost | -$0.15 |
| 11/8 9:28:53 PM | NEAR | UP | 67 sec | -0.314% | 0¢ | ❌ Lost | -$0.15 |
| 11/8 9:28:53 PM | BRENT | DOWN | 67 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/8 9:28:37 PM | EURUSD | DOWN | 83 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/8 9:27:33 PM | PALLADIUM | DOWN | 2.4 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/8 9:27:17 PM | COPPER | DOWN | 2.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/8 9:27:17 PM | PLATINUM | DOWN | 2.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/8 9:26:44 PM | USDCAD | UP | 3.2 min | — | 12¢ | ❌ Lost | -$0.15 |
| 11/8 9:26:44 PM | AUDUSD | DOWN | 3.2 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/8 9:26:44 PM | GOLD | DOWN | 3.2 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/8 9:26:44 PM | SILVER | DOWN | 3.2 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/8 9:23:26 PM | DOGE | UP | 6.5 min | -0.361% | 42¢ | ❌ Lost | -$0.15 |
| 11/8 9:14:46 PM | USDJPY | DOWN | 14 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/8 9:14:31 PM | ZEC | DOWN | 28 sec | +0.059% | 1¢ | ❌ Lost | -$0.15 |
| 11/8 9:13:41 PM | HYPE | DOWN | 78 sec | +0.135% | 1¢ | ❌ Lost | -$0.15 |
| 11/8 9:13:26 PM | SOL | DOWN | 1.6 min | +0.175% | 0¢ | ❌ Lost | -$0.15 |
| 11/8 9:13:26 PM | XRP | DOWN | 1.6 min | +0.171% | 1¢ | ❌ Lost | -$0.15 |
| 11/8 9:13:26 PM | EURUSD | DOWN | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/8 9:13:26 PM | PLATINUM | DOWN | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/8 9:13:10 PM | SILVER | DOWN | 1.8 min | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
