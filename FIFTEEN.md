# 15-Minute 1¢ Study

*Updated Sun Nov 8, 9:08 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 4059 finished bets | 1% | $192.35 | +43% | +4.74¢ | $94.30 / $98.05 |

*Expect about **97 buys a day** (~$14.53/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 3766 | $110.00 | +27% |
| Volatility model ≥ 2%, hold to the close | 7431 | $85.40 | +10% |
| Momentum model ≥ 2%, hold to the close | 6137 | $8.55 | +1% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 50196 | 50179 | 186 (0%) | 1.07% | -$3,498.45 (-57%) | Hold to the close: -$3,498.45 (-57%) |

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
| Volatility model | 30740 | 4.8% | 0.4% (121) | -690% | ❌ Worse |
| Momentum model | 30740 | 4.6% | 0.4% (121) | -715% | ❌ Worse |
| Mean-reversion model | 30740 | 8.1% | 0.4% (121) | -834% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 30740 | 121 | -50% | -87% | -87% | -84% |
| Volatility model ≥ 2% | 7431 | 70 | +10% | -77% | -75% | -71% |
| Volatility model ≥ 5% | 4059 | 46 | +43% | -71% | -70% | -66% |
| Volatility model ≥ 10% | 2335 | 28 | +71% | -61% | -59% | -56% |
| Momentum model ≥ 2% | 6137 | 51 | +1% | -78% | -77% | -74% |
| Momentum model ≥ 5% | 3766 | 37 | +27% | -73% | -73% | -69% |
| Momentum model ≥ 10% | 2469 | 25 | +42% | -64% | -64% | -59% |
| Mean-reversion model ≥ 2% | 12712 | 89 | -23% | -82% | -82% | -79% |
| Mean-reversion model ≥ 5% | 8914 | 77 | -4% | -79% | -79% | -76% |
| Mean-reversion model ≥ 10% | 5959 | 56 | +7% | -76% | -76% | -73% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 30945 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 11784 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 7450 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 50179 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 186 | 0% | -$3,498.45 | -57% | — |
| Sell at 2¢ | 1965 | 4% | -$5,311.55 | -87% | 47 sec |
| Sell at 3¢ | 1337 | 3% | -$5,301.02 | -87% | 48 sec |
| Sell at 5¢ | 932 | 2% | -$5,188.65 | -85% | 63 sec |
| Sell at 10¢ | 563 | 1% | -$4,972.92 | -81% | 65 sec |
| Sell at 25¢ | 295 | 1% | -$4,622.00 | -76% | 83 sec |
| Sell at 50¢ | 190 | 0% | -$4,217.95 | -69% | 1.9 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 12 | 0 | 25% | 17% | -100% | -57% | -35% |
| 5–10 min | 2487 | 12 | 11% | 4% | -54% | -81% | -82% |
| 2–5 min | 16184 | 87 | 7% | 3% | -47% | -87% | -87% |
| 1–2 min | 12673 | 41 | 3% | 2% | -64% | -92% | -92% |
| Under 1 min | 18823 | 46 | 1% | 0% | -65% | -84% | -84% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 3469 | 13 | 5% | 2% | -51% | -88% | -88% |
| SOL | 3462 | 15 | 4% | 2% | -45% | -87% | -87% |
| HYPE | 3452 | 11 | 5% | 2% | -60% | -89% | -88% |
| BNB | 3445 | 18 | 5% | 2% | -34% | -86% | -85% |
| DOGE | 3444 | 7 | 4% | 2% | -74% | -91% | -90% |
| ETH | 3437 | 14 | 7% | 3% | -50% | -81% | -82% |
| NEAR | 3418 | 16 | 5% | 2% | -39% | -85% | -85% |
| BTC | 3414 | 16 | 5% | 2% | -36% | -88% | -89% |
| XRP | 3404 | 13 | 3% | 1% | -52% | -89% | -89% |
| GOLD | 1798 | 5 | 6% | 2% | -66% | -81% | -83% |
| WTI | 1767 | 6 | 4% | 1% | -59% | -92% | -92% |
| SILVER | 1749 | 8 | 5% | 2% | -46% | -82% | -82% |
| PLATINUM | 1581 | 4 | 2% | 1% | -76% | -96% | -96% |
| EURUSD | 1519 | 4 | 2% | 1% | -75% | -90% | -89% |
| COPPER | 1482 | 6 | 2% | 1% | -62% | -72% | -71% |
| NATGAS | 1447 | 8 | 2% | 1% | -48% | -77% | -76% |
| GBPUSD | 1439 | 4 | 2% | 1% | -74% | -96% | -96% |
| USDJPY | 1422 | 5 | 2% | 1% | -67% | -97% | -96% |
| PALLADIUM | 1421 | 3 | 1% | 0% | -80% | -91% | -92% |
| AUDUSD | 979 | 5 | 2% | 1% | -52% | -87% | -87% |
| USDCAD | 947 | 0 | 2% | 1% | -100% | -97% | -97% |
| BRENT | 539 | 0 | 1% | 1% | -100% | -97% | -97% |
| 10YRRATE | 303 | 1 | 4% | 1% | -69% | -62% | -60% |
| 2YRRATE | 287 | 3 | 4% | 1% | -2% | -28% | -27% |
| 30YRRATE | 285 | 0 | 2% | 1% | -100% | -96% | -95% |
| 5YRRATE | 262 | 1 | 4% | 2% | -64% | -93% | -95% |
| INX | 7 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 25441 | 95 | 4% | 2% | -57% | -88% | -87% |
| DOWN (bought NO) | 24738 | 91 | 4% | 2% | -58% | -86% | -86% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 5038 | 25 | 2% | 1% | -13% | -77% | -76% |
| 0.05–0.1% | 5310 | 19 | 3% | 2% | -46% | -91% | -91% |
| 0.1–0.2% | 7969 | 27 | 4% | 2% | -57% | -90% | -90% |
| 0.2–0.5% | 9172 | 38 | 6% | 3% | -54% | -87% | -86% |
| Over 0.5% | 3448 | 14 | 7% | 3% | -58% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 12179 | 42 | 4% | 2% | -61% | -87% | -87% |
| Morning (6am–12pm) | 12223 | 54 | 4% | 2% | -50% | -84% | -84% |
| Afternoon (12–6pm) | 12200 | 47 | 4% | 2% | -55% | -86% | -86% |
| Evening (6pm–12am) | 13577 | 43 | 3% | 2% | -64% | -90% | -90% |

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
| 11/8 8:56:05 PM | GOLD | UP | 3.9 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/8 8:56:05 PM | ETH | UP | 3.9 min | -0.348% | 1¢ | ❌ Lost | -$0.15 |
| 11/8 8:56:05 PM | BTC | UP | 3.9 min | -0.315% | 1¢ | ❌ Lost | -$0.15 |
| 11/8 8:56:05 PM | DOGE | UP | 3.9 min | -0.323% | 1¢ | ❌ Lost | -$0.15 |
| 11/8 8:56:05 PM | BNB | UP | 3.9 min | -0.240% | 1¢ | ❌ Lost | -$0.15 |
| 11/8 8:55:48 PM | SOL | UP | 4.2 min | -0.431% | 1¢ | ❌ Lost | -$0.15 |
| 11/8 8:55:32 PM | XRP | UP | 4.5 min | -0.457% | 1¢ | ❌ Lost | -$0.15 |
| 11/8 8:44:27 PM | WTI | UP | 32 sec | — | 0¢ | ❌ Lost | $0.00 |
| 11/8 8:44:27 PM | PLATINUM | DOWN | 32 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/8 8:44:27 PM | AUDUSD | UP | 32 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/8 8:43:54 PM | ETH | DOWN | 66 sec | +0.061% | 0¢ | ❌ Lost | -$0.15 |
| 11/8 8:43:54 PM | BRENT | UP | 66 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/8 8:43:54 PM | PALLADIUM | DOWN | 66 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/8 8:43:38 PM | SOL | DOWN | 82 sec | +0.129% | 1¢ | ❌ Lost | -$0.15 |
| 11/8 8:43:38 PM | BTC | DOWN | 82 sec | +0.071% | 1¢ | ❌ Lost | -$0.15 |
| 11/8 8:43:38 PM | NEAR | DOWN | 82 sec | +0.166% | 1¢ | ❌ Lost | -$0.15 |
| 11/8 8:43:22 PM | BNB | DOWN | 1.6 min | +0.090% | 0¢ | ❌ Lost | $0.00 |
| 11/8 8:43:07 PM | ZEC | DOWN | 1.9 min | +0.466% | 0¢ | ❌ Lost | $0.00 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
