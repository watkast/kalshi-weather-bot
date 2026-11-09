# 15-Minute 1¢ Study

*Updated Sun Nov 8, 8:33 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 4055 finished bets | 1% | $192.80 | +43% | +4.75¢ | $94.60 / $98.20 |

*Expect about **97 buys a day** (~$14.53/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 3761 | $110.60 | +27% |
| Volatility model ≥ 2%, hold to the close | 7425 | $86.15 | +10% |
| Momentum model ≥ 2%, hold to the close | 6131 | $9.30 | +1% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 50162 | 50145 | 186 (0%) | 1.07% | -$3,493.80 (-57%) | Hold to the close: -$3,493.80 (-57%) |

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
| Volatility model | 30723 | 4.8% | 0.4% (121) | -690% | ❌ Worse |
| Momentum model | 30723 | 4.6% | 0.4% (121) | -716% | ❌ Worse |
| Mean-reversion model | 30723 | 8.1% | 0.4% (121) | -834% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 30723 | 121 | -50% | -87% | -87% | -84% |
| Volatility model ≥ 2% | 7425 | 70 | +10% | -77% | -75% | -71% |
| Volatility model ≥ 5% | 4055 | 46 | +43% | -71% | -70% | -66% |
| Volatility model ≥ 10% | 2335 | 28 | +71% | -61% | -59% | -56% |
| Momentum model ≥ 2% | 6131 | 51 | +1% | -78% | -77% | -74% |
| Momentum model ≥ 5% | 3761 | 37 | +27% | -73% | -73% | -69% |
| Momentum model ≥ 10% | 2465 | 25 | +42% | -64% | -64% | -59% |
| Mean-reversion model ≥ 2% | 12705 | 89 | -23% | -82% | -82% | -79% |
| Mean-reversion model ≥ 5% | 8909 | 77 | -4% | -79% | -79% | -76% |
| Mean-reversion model ≥ 10% | 5957 | 56 | +7% | -76% | -76% | -73% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 30928 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 11771 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 7446 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 50145 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 186 | 0% | -$3,493.80 | -57% | — |
| Sell at 2¢ | 1965 | 4% | -$5,306.90 | -87% | 47 sec |
| Sell at 3¢ | 1337 | 3% | -$5,296.37 | -87% | 48 sec |
| Sell at 5¢ | 932 | 2% | -$5,184.00 | -85% | 63 sec |
| Sell at 10¢ | 563 | 1% | -$4,968.27 | -81% | 65 sec |
| Sell at 25¢ | 295 | 1% | -$4,617.35 | -76% | 83 sec |
| Sell at 50¢ | 190 | 0% | -$4,213.30 | -69% | 1.9 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 12 | 0 | 25% | 17% | -100% | -57% | -35% |
| 5–10 min | 2487 | 12 | 11% | 4% | -54% | -81% | -82% |
| 2–5 min | 16168 | 87 | 7% | 3% | -47% | -87% | -87% |
| 1–2 min | 12663 | 41 | 3% | 2% | -64% | -92% | -92% |
| Under 1 min | 18815 | 46 | 1% | 0% | -65% | -84% | -84% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 3467 | 13 | 5% | 2% | -51% | -88% | -88% |
| SOL | 3460 | 15 | 4% | 2% | -45% | -87% | -87% |
| HYPE | 3451 | 11 | 5% | 2% | -60% | -89% | -88% |
| BNB | 3443 | 18 | 5% | 2% | -34% | -86% | -85% |
| DOGE | 3442 | 7 | 4% | 2% | -74% | -90% | -90% |
| ETH | 3435 | 14 | 7% | 3% | -50% | -81% | -82% |
| NEAR | 3416 | 16 | 5% | 2% | -39% | -85% | -85% |
| BTC | 3412 | 16 | 5% | 2% | -36% | -88% | -89% |
| XRP | 3402 | 13 | 3% | 1% | -52% | -89% | -89% |
| GOLD | 1796 | 5 | 6% | 2% | -66% | -81% | -83% |
| WTI | 1765 | 6 | 4% | 1% | -59% | -92% | -92% |
| SILVER | 1747 | 8 | 5% | 2% | -46% | -82% | -82% |
| PLATINUM | 1579 | 4 | 2% | 1% | -76% | -96% | -96% |
| EURUSD | 1519 | 4 | 2% | 1% | -75% | -90% | -89% |
| COPPER | 1481 | 6 | 2% | 1% | -62% | -72% | -71% |
| NATGAS | 1446 | 8 | 2% | 1% | -48% | -77% | -76% |
| GBPUSD | 1439 | 4 | 2% | 1% | -74% | -96% | -96% |
| USDJPY | 1421 | 5 | 2% | 1% | -67% | -97% | -96% |
| PALLADIUM | 1419 | 3 | 1% | 0% | -80% | -91% | -92% |
| AUDUSD | 977 | 5 | 2% | 1% | -52% | -87% | -87% |
| USDCAD | 946 | 0 | 2% | 1% | -100% | -97% | -97% |
| BRENT | 538 | 0 | 1% | 1% | -100% | -97% | -97% |
| 10YRRATE | 303 | 1 | 4% | 1% | -69% | -62% | -60% |
| 2YRRATE | 287 | 3 | 4% | 1% | -2% | -28% | -27% |
| 30YRRATE | 285 | 0 | 2% | 1% | -100% | -96% | -95% |
| 5YRRATE | 262 | 1 | 4% | 2% | -64% | -93% | -95% |
| INX | 7 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 25422 | 95 | 4% | 2% | -57% | -88% | -87% |
| DOWN (bought NO) | 24723 | 91 | 4% | 2% | -58% | -86% | -86% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 5038 | 25 | 2% | 1% | -13% | -77% | -76% |
| 0.05–0.1% | 5307 | 19 | 3% | 2% | -46% | -91% | -91% |
| 0.1–0.2% | 7966 | 27 | 4% | 2% | -57% | -90% | -89% |
| 0.2–0.5% | 9162 | 38 | 6% | 3% | -54% | -87% | -86% |
| Over 0.5% | 3447 | 14 | 7% | 3% | -58% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 12179 | 42 | 4% | 2% | -61% | -87% | -87% |
| Morning (6am–12pm) | 12223 | 54 | 4% | 2% | -50% | -84% | -84% |
| Afternoon (12–6pm) | 12200 | 47 | 4% | 2% | -55% | -86% | -86% |
| Evening (6pm–12am) | 13543 | 43 | 3% | 2% | -63% | -90% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,946 |
| Time from buy to best bounce (bounced bets) | 51 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/8 8:29:52 PM | BRENT | UP | 7 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/8 8:29:52 PM | EURUSD | UP | 7 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/8 8:29:01 PM | AUDUSD | UP | 58 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/8 8:28:45 PM | WTI | UP | 74 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 11/8 8:28:45 PM | NATGAS | UP | 74 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/8 8:28:45 PM | BTC | DOWN | 74 sec | +0.110% | 0¢ | ❌ Lost | $0.00 |
| 11/8 8:28:14 PM | XRP | DOWN | 1.8 min | +0.244% | 1¢ | ❌ Lost | -$0.15 |
| 11/8 8:28:14 PM | BNB | DOWN | 1.8 min | +0.054% | 1¢ | ❌ Lost | -$0.15 |
| 11/8 8:28:14 PM | USDCAD | DOWN | 1.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/8 8:27:56 PM | NEAR | DOWN | 2.0 min | +0.328% | 1¢ | ❌ Lost | -$0.15 |
| 11/8 8:27:09 PM | ETH | DOWN | 2.8 min | +0.250% | 1¢ | ❌ Lost | -$0.15 |
| 11/8 8:27:09 PM | ZEC | DOWN | 2.8 min | +0.389% | 1¢ | ❌ Lost | -$0.15 |
| 11/8 8:26:35 PM | DOGE | DOWN | 3.4 min | +0.332% | 1¢ | ❌ Lost | -$0.15 |
| 11/8 8:26:19 PM | SOL | DOWN | 3.7 min | +0.462% | 1¢ | ❌ Lost | -$0.15 |
| 11/8 8:26:19 PM | HYPE | DOWN | 3.7 min | +0.435% | 1¢ | ❌ Lost | -$0.15 |
| 11/8 8:14:35 PM | AUDUSD | UP | 25 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/8 8:14:04 PM | USDCAD | DOWN | 56 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/8 8:13:48 PM | GBPUSD | UP | 72 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/8 8:13:32 PM | EURUSD | UP | 88 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/8 8:13:32 PM | GOLD | UP | 88 sec | — | 2¢ | ❌ Lost | -$0.15 |
| 11/8 8:13:09 PM | ETH | UP | 1.9 min | -0.293% | 0¢ | ❌ Lost | -$0.15 |
| 11/8 8:13:09 PM | USDJPY | DOWN | 1.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/8 8:12:52 PM | BRENT | DOWN | 2.1 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/8 8:12:52 PM | HYPE | UP | 2.1 min | -0.310% | 1¢ | ❌ Lost | -$0.15 |
| 11/8 8:12:36 PM | ZEC | UP | 2.4 min | -0.466% | 1¢ | ❌ Lost | -$0.15 |
| 11/8 8:11:47 PM | NEAR | UP | 3.2 min | -0.741% | 0¢ | ❌ Lost | -$0.15 |
| 11/8 8:11:47 PM | BNB | UP | 3.2 min | -0.247% | 1¢ | ❌ Lost | -$0.15 |
| 11/8 8:11:47 PM | BTC | UP | 3.2 min | -0.223% | 1¢ | ❌ Lost | -$0.15 |
| 11/8 8:09:54 PM | WTI | DOWN | 5.1 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/8 8:09:54 PM | DOGE | UP | 5.1 min | -0.595% | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
