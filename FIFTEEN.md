# 15-Minute 1¢ Study

*Updated Sun Oct 25, 8:50 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 2706 finished bets | 1% | $84.35 | +27% | +3.12¢ | $33.65 / $50.70 |

*Expect about **97 buys a day** (~$14.58/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 2502 | $59.10 | +21% |
| Volatility model ≥ 2%, hold to the close | 5003 | -$11.35 | -2% |
| Momentum model ≥ 2%, hold to the close | 4164 | -$26.40 | -5% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 32061 | 32053 | 120 (0%) | 1.07% | -$2,214.15 (-57%) | Hold to the close: -$2,214.15 (-57%) |

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
| Volatility model | 20691 | 4.6% | 0.4% (85) | -655% | ❌ Worse |
| Momentum model | 20691 | 4.5% | 0.4% (85) | -680% | ❌ Worse |
| Mean-reversion model | 20691 | 7.9% | 0.4% (85) | -794% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 20691 | 85 | -48% | -88% | -87% | -85% |
| Volatility model ≥ 2% | 5003 | 43 | -2% | -78% | -77% | -74% |
| Volatility model ≥ 5% | 2706 | 28 | +27% | -75% | -73% | -70% |
| Volatility model ≥ 10% | 1532 | 18 | +64% | -66% | -65% | -61% |
| Momentum model ≥ 2% | 4164 | 33 | -5% | -80% | -80% | -77% |
| Momentum model ≥ 5% | 2502 | 24 | +21% | -77% | -76% | -72% |
| Momentum model ≥ 10% | 1632 | 16 | +34% | -71% | -70% | -65% |
| Mean-reversion model ≥ 2% | 8347 | 56 | -27% | -83% | -83% | -80% |
| Mean-reversion model ≥ 5% | 5849 | 47 | -12% | -81% | -80% | -78% |
| Mean-reversion model ≥ 10% | 3892 | 33 | -4% | -78% | -78% | -76% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 20891 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 7438 | 2% | 2% | 1% | 1% | 0% | 0% |
| Financials | 3724 | 2% | 1% | 1% | 1% | 0% | 0% |
| **All** | 32053 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 120 | 0% | -$2,214.15 | -57% | — |
| Sell at 2¢ | 1191 | 4% | -$3,416.49 | -88% | 47 sec |
| Sell at 3¢ | 817 | 3% | -$3,407.52 | -88% | 48 sec |
| Sell at 5¢ | 570 | 2% | -$3,355.65 | -86% | 61 sec |
| Sell at 10¢ | 352 | 1% | -$3,223.03 | -83% | 65 sec |
| Sell at 25¢ | 191 | 1% | -$2,981.94 | -77% | 82 sec |
| Sell at 50¢ | 122 | 0% | -$2,706.65 | -70% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 1406 | 7 | 11% | 4% | -53% | -81% | -83% |
| 2–5 min | 10276 | 55 | 7% | 3% | -47% | -87% | -87% |
| 1–2 min | 8101 | 30 | 3% | 1% | -59% | -92% | -91% |
| Under 1 min | 12266 | 28 | 1% | 0% | -67% | -86% | -86% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 2340 | 12 | 5% | 2% | -35% | -89% | -89% |
| HYPE | 2334 | 8 | 5% | 3% | -58% | -89% | -87% |
| BNB | 2330 | 13 | 5% | 3% | -31% | -84% | -83% |
| SOL | 2326 | 6 | 3% | 2% | -68% | -92% | -92% |
| ETH | 2322 | 11 | 6% | 3% | -43% | -86% | -85% |
| DOGE | 2315 | 4 | 4% | 2% | -78% | -91% | -90% |
| NEAR | 2311 | 12 | 5% | 2% | -33% | -82% | -81% |
| XRP | 2311 | 9 | 3% | 1% | -52% | -89% | -88% |
| BTC | 2302 | 12 | 5% | 2% | -30% | -88% | -89% |
| GOLD | 1204 | 4 | 4% | 1% | -61% | -81% | -83% |
| SILVER | 1170 | 5 | 4% | 2% | -50% | -82% | -82% |
| WTI | 1152 | 3 | 3% | 1% | -69% | -94% | -95% |
| PLATINUM | 1021 | 0 | 1% | 1% | -100% | -98% | -97% |
| COPPER | 997 | 4 | 1% | 1% | -63% | -69% | -69% |
| EURUSD | 953 | 3 | 2% | 1% | -71% | -86% | -86% |
| NATGAS | 946 | 5 | 2% | 1% | -51% | -87% | -86% |
| PALLADIUM | 908 | 2 | 1% | 0% | -79% | -88% | -88% |
| GBPUSD | 899 | 1 | 2% | 1% | -90% | -96% | -97% |
| USDJPY | 880 | 5 | 1% | 1% | -47% | -98% | -97% |
| AUDUSD | 439 | 0 | 1% | 0% | -100% | -98% | -98% |
| USDCAD | 401 | 0 | 1% | 0% | -100% | -97% | -99% |
| 10YRRATE | 43 | 0 | 0% | 0% | -100% | -100% | -100% |
| 2YRRATE | 40 | 1 | 2% | 0% | +133% | +138% | +133% |
| BRENT | 40 | 0 | 0% | 0% | -100% | -100% | -100% |
| 30YRRATE | 39 | 0 | 0% | 0% | -100% | -100% | -100% |
| 5YRRATE | 30 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 16255 | 66 | 4% | 2% | -53% | -87% | -87% |
| DOWN (bought NO) | 15798 | 54 | 4% | 2% | -61% | -88% | -88% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 3494 | 18 | 2% | 1% | -13% | -80% | -80% |
| 0.05–0.1% | 3595 | 11 | 3% | 2% | -55% | -92% | -92% |
| 0.1–0.2% | 5403 | 20 | 5% | 2% | -54% | -89% | -89% |
| 0.2–0.5% | 6074 | 28 | 6% | 3% | -49% | -87% | -86% |
| Over 0.5% | 2321 | 10 | 7% | 3% | -56% | -87% | -88% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 7904 | 32 | 4% | 2% | -54% | -85% | -85% |
| Morning (6am–12pm) | 7781 | 35 | 4% | 2% | -49% | -88% | -87% |
| Afternoon (12–6pm) | 7607 | 24 | 4% | 2% | -63% | -87% | -88% |
| Evening (6pm–12am) | 8761 | 29 | 3% | 2% | -62% | -90% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,822 |
| Time from buy to best bounce (bounced bets) | 50 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/25 8:44:59 PM | SILVER | UP | 0 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/25 8:44:59 PM | USDJPY | UP | 0 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/25 8:44:59 PM | AUDUSD | UP | 0 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/25 8:44:44 PM | GOLD | DOWN | 15 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/25 8:44:44 PM | NATGAS | DOWN | 15 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/25 8:43:56 PM | USDCAD | UP | 63 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/25 8:43:56 PM | EURUSD | DOWN | 63 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/25 8:43:41 PM | GBPUSD | DOWN | 78 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/25 8:43:25 PM | BTC | UP | 1.6 min | -0.170% | 0¢ | ❌ Lost | $0.00 |
| 10/25 8:43:09 PM | DOGE | UP | 1.8 min | -0.351% | 1¢ | ❌ Lost | $0.00 |
| 10/25 8:42:22 PM | HYPE | UP | 2.6 min | -0.313% | 0¢ | ❌ Lost | -$0.15 |
| 10/25 8:42:22 PM | SOL | UP | 2.6 min | -0.313% | 0¢ | ❌ Lost | $0.00 |
| 10/25 8:42:22 PM | NEAR | UP | 2.6 min | -0.657% | 1¢ | ❌ Lost | -$0.15 |
| 10/25 8:42:06 PM | ZEC | UP | 2.9 min | -0.664% | 0¢ | ❌ Lost | $0.00 |
| 10/25 8:42:06 PM | BNB | UP | 2.9 min | -0.240% | 0¢ | ❌ Lost | -$0.15 |
| 10/25 8:42:06 PM | XRP | UP | 2.9 min | -0.405% | 0¢ | ❌ Lost | -$0.15 |
| 10/25 8:41:19 PM | ETH | UP | 3.7 min | -0.341% | 1¢ | ❌ Lost | -$0.15 |
| 10/25 8:29:49 PM | GOLD | UP | 11 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/25 8:29:02 PM | NEAR | UP | 58 sec | -0.398% | 1¢ | ❌ Lost | -$0.15 |
| 10/25 8:29:02 PM | AUDUSD | DOWN | 58 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/25 8:28:46 PM | DOGE | UP | 74 sec | -0.186% | 0¢ | ❌ Lost | -$0.15 |
| 10/25 8:28:46 PM | BRENT | UP | 74 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/25 8:27:57 PM | COPPER | UP | 2.0 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/25 8:27:57 PM | PALLADIUM | UP | 2.0 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/25 8:27:11 PM | SILVER | UP | 2.8 min | — | 2¢ | ❌ Lost | -$0.15 |
| 10/25 8:27:11 PM | SOL | UP | 2.8 min | -0.293% | 1¢ | ❌ Lost | -$0.15 |
| 10/25 8:26:55 PM | WTI | UP | 3.1 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/25 8:26:55 PM | ZEC | UP | 3.1 min | -0.687% | 1¢ | ❌ Lost | $0.00 |
| 10/25 8:26:55 PM | BNB | UP | 3.1 min | -0.268% | 1¢ | ❌ Lost | -$0.15 |
| 10/25 8:26:55 PM | XRP | UP | 3.1 min | -0.349% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
