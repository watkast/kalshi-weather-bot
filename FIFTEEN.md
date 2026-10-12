# 15-Minute 1¢ Study

*Updated Mon Oct 12, 5:47 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 1212 finished bets | 1% | $36.15 | +27% | +2.98¢ | $32.60 / $3.55 |

*Expect about **82 buys a day** (~$12.36/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 1159 | $15.50 | +12% |
| 5+ min left, hold to the close | 440 | -$9.10 | -14% |
| Volatility model ≥ 2%, hold to the close | 2134 | -$18.80 | -7% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 15967 | 15960 | 62 (0%) | 1.07% | -$1,058.45 (-55%) | Hold to the close: -$1,058.45 (-55%) |

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
| Volatility model | 10597 | 4.5% | 0.4% (45) | -671% | ❌ Worse |
| Momentum model | 10597 | 4.5% | 0.4% (45) | -697% | ❌ Worse |
| Mean-reversion model | 10597 | 7.2% | 0.4% (45) | -779% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 10597 | 45 | -47% | -88% | -88% | -86% |
| Volatility model ≥ 2% | 2134 | 17 | -7% | -78% | -77% | -74% |
| Volatility model ≥ 5% | 1212 | 12 | +27% | -72% | -71% | -69% |
| Volatility model ≥ 10% | 763 | 8 | +51% | -63% | -63% | -59% |
| Momentum model ≥ 2% | 1878 | 14 | -10% | -79% | -80% | -78% |
| Momentum model ≥ 5% | 1159 | 10 | +12% | -76% | -76% | -73% |
| Momentum model ≥ 10% | 801 | 7 | +24% | -69% | -69% | -65% |
| Mean-reversion model ≥ 2% | 3734 | 26 | -24% | -85% | -85% | -82% |
| Mean-reversion model ≥ 5% | 2552 | 20 | -13% | -83% | -82% | -78% |
| Mean-reversion model ≥ 10% | 1693 | 14 | -4% | -81% | -81% | -78% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 10795 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 3810 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 1355 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 15960 | 3% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 62 | 0% | -$1,058.45 | -55% | — |
| Sell at 2¢ | 540 | 3% | -$1,744.05 | -91% | 33 sec |
| Sell at 3¢ | 357 | 2% | -$1,745.22 | -91% | 47 sec |
| Sell at 5¢ | 261 | 2% | -$1,714.80 | -89% | 50 sec |
| Sell at 10¢ | 171 | 1% | -$1,632.44 | -85% | 64 sec |
| Sell at 25¢ | 97 | 1% | -$1,507.38 | -78% | 80 sec |
| Sell at 50¢ | 64 | 0% | -$1,354.45 | -70% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 436 | 4 | 11% | 3% | -13% | -81% | -87% |
| 2–5 min | 5133 | 32 | 6% | 3% | -39% | -88% | -89% |
| 1–2 min | 4220 | 16 | 3% | 2% | -59% | -94% | -94% |
| Under 1 min | 6167 | 10 | 1% | 0% | -76% | -91% | -91% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 1212 | 7 | 4% | 2% | -29% | -90% | -90% |
| HYPE | 1209 | 4 | 4% | 2% | -59% | -90% | -89% |
| DOGE | 1203 | 2 | 4% | 2% | -79% | -91% | -90% |
| BNB | 1201 | 5 | 4% | 1% | -49% | -91% | -92% |
| ETH | 1200 | 8 | 5% | 2% | -19% | -90% | -89% |
| SOL | 1200 | 2 | 3% | 1% | -79% | -93% | -92% |
| BTC | 1194 | 5 | 5% | 2% | -44% | -88% | -91% |
| NEAR | 1188 | 7 | 5% | 2% | -23% | -76% | -77% |
| XRP | 1188 | 7 | 2% | 1% | -27% | -85% | -85% |
| GOLD | 627 | 0 | 3% | 1% | -100% | -93% | -94% |
| SILVER | 609 | 1 | 3% | 1% | -81% | -94% | -94% |
| WTI | 585 | 3 | 3% | 1% | -41% | -94% | -96% |
| COPPER | 547 | 0 | 1% | 1% | -100% | -98% | -98% |
| PLATINUM | 502 | 0 | 0% | 0% | -100% | -100% | -99% |
| NATGAS | 470 | 3 | 3% | 2% | -40% | -96% | -94% |
| PALLADIUM | 470 | 1 | 1% | 0% | -80% | -98% | -98% |
| EURUSD | 451 | 3 | 3% | 2% | -38% | -75% | -74% |
| GBPUSD | 431 | 1 | 2% | 1% | -78% | -96% | -96% |
| USDJPY | 388 | 3 | 1% | 1% | -28% | -98% | -97% |
| USDCAD | 43 | 0 | 0% | 0% | -100% | -100% | -100% |
| AUDUSD | 42 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 8063 | 34 | 3% | 2% | -51% | -90% | -89% |
| DOWN (bought NO) | 7897 | 28 | 3% | 2% | -59% | -91% | -92% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 1936 | 9 | 2% | 1% | -22% | -77% | -77% |
| 0.05–0.1% | 1927 | 6 | 3% | 1% | -55% | -92% | -92% |
| 0.1–0.2% | 2761 | 9 | 4% | 2% | -60% | -91% | -92% |
| 0.2–0.5% | 3001 | 18 | 5% | 3% | -34% | -89% | -88% |
| Over 0.5% | 1167 | 5 | 6% | 2% | -56% | -88% | -90% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 4019 | 20 | 4% | 2% | -43% | -86% | -86% |
| Morning (6am–12pm) | 3780 | 20 | 4% | 2% | -39% | -91% | -91% |
| Afternoon (12–6pm) | 3802 | 9 | 3% | 1% | -72% | -91% | -91% |
| Evening (6pm–12am) | 4359 | 13 | 3% | 2% | -66% | -94% | -94% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 25 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,534 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 41 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/12 5:44:58 PM | COPPER | UP | 1 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/12 5:44:42 PM | WTI | UP | 17 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/12 5:44:26 PM | USDJPY | UP | 33 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/12 5:44:10 PM | GOLD | UP | 49 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/12 5:44:10 PM | PALLADIUM | UP | 49 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/12 5:43:07 PM | NEAR | UP | 1.9 min | -0.860% | 1¢ | ❌ Lost | -$0.15 |
| 10/12 5:42:51 PM | GBPUSD | DOWN | 2.1 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/12 5:42:51 PM | USDCAD | UP | 2.1 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/12 5:42:18 PM | NATGAS | UP | 2.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/12 5:42:02 PM | EURUSD | DOWN | 3.0 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/12 5:41:47 PM | BNB | UP | 3.2 min | -0.351% | 1¢ | ❌ Lost | -$0.15 |
| 10/12 5:41:47 PM | XRP | UP | 3.2 min | -0.461% | 1¢ | ❌ Lost | -$0.15 |
| 10/12 5:41:47 PM | BTC | UP | 3.2 min | -0.272% | 1¢ | ❌ Lost | -$0.15 |
| 10/12 5:41:00 PM | ETH | UP | 4.0 min | -0.607% | 1¢ | ❌ Lost | -$0.15 |
| 10/12 5:40:28 PM | DOGE | UP | 4.5 min | -0.843% | 1¢ | ❌ Lost | -$0.15 |
| 10/12 5:40:28 PM | SOL | UP | 4.5 min | -0.481% | 1¢ | ❌ Lost | -$0.15 |
| 10/12 5:39:40 PM | HYPE | UP | 5.3 min | -0.772% | 1¢ | ❌ Lost | -$0.15 |
| 10/12 5:38:37 PM | ZEC | UP | 6.4 min | -1.774% | 1¢ | ❌ Lost | -$0.15 |
| 10/12 5:29:44 PM | BNB | UP | 15 sec | -0.004% | 0¢ | ❌ Lost | -$0.15 |
| 10/12 5:29:44 PM | NEAR | DOWN | 15 sec | +0.105% | 0¢ | ❌ Lost | $0.00 |
| 10/12 5:29:44 PM | ETH | UP | 15 sec | -0.027% | 0¢ | ❌ Lost | $0.00 |
| 10/12 5:29:28 PM | XRP | UP | 31 sec | -0.074% | 1¢ | ❌ Lost | -$0.15 |
| 10/12 5:29:12 PM | PALLADIUM | DOWN | 47 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/12 5:28:56 PM | COPPER | DOWN | 63 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/12 5:27:53 PM | DOGE | UP | 2.1 min | -0.466% | 1¢ | ❌ Lost | -$0.15 |
| 10/12 5:27:53 PM | SOL | UP | 2.1 min | -0.310% | 1¢ | ❌ Lost | $0.00 |
| 10/12 5:27:38 PM | GBPUSD | DOWN | 2.4 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/12 5:27:06 PM | WTI | UP | 2.9 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/12 5:27:06 PM | USDJPY | UP | 2.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/12 5:26:51 PM | HYPE | UP | 3.1 min | -0.483% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
